#!/usr/bin/env python3
"""Build a framed 32x32 Pictiq icon SVG from a silhouette PNG."""

from __future__ import annotations

import argparse
import shutil
import subprocess
import tempfile
import xml.etree.ElementTree as ET
from pathlib import Path

from PIL import Image, ImageOps


SVG_NS = "http://www.w3.org/2000/svg"
ET.register_namespace("", SVG_NS)


def svg_el(tag: str, **attrs: str) -> ET.Element:
    return ET.Element(f"{{{SVG_NS}}}{tag}", attrs)


def preprocess_to_pbm(inp: Path, out_pbm: Path) -> tuple[int, int]:
    img = Image.open(inp).convert("L")
    # Otsu-ish fixed threshold for MVP.
    bw = img.point(lambda p: 255 if p > 180 else 0, mode="L")

    # Auto-invert if likely white foreground on black background.
    black_pixels = sum(1 for p in bw.getdata() if p == 0)
    white_pixels = bw.width * bw.height - black_pixels
    # We expect background (white) to dominate.
    if black_pixels > white_pixels:
        bw = ImageOps.invert(bw)

    one = bw.convert("1")
    one.save(out_pbm)
    return one.width, one.height


def trace_with_potrace(pbm_path: Path, out_svg: Path) -> None:
    cmd = ["potrace", str(pbm_path), "-s", "-o", str(out_svg)]
    r = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if r.returncode != 0:
        raise RuntimeError(f"potrace failed: {r.stderr.strip() or r.stdout.strip()}")


def trace_with_inkscape(png_path: Path, out_svg: Path) -> None:
    # CLI action names vary by Inkscape version; attempt common one.
    cmd = [
        "inkscape",
        str(png_path),
        "--batch-process",
        "--actions",
        f"select-all;selection-trace-bitmap;export-filename:{out_svg};export-do",
    ]
    r = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if r.returncode != 0:
        raise RuntimeError(f"inkscape trace failed: {r.stderr.strip() or r.stdout.strip()}")


def extract_paths(traced_svg: Path) -> tuple[list[str], float, float]:
    tree = ET.parse(traced_svg)
    root = tree.getroot()

    vb = root.attrib.get("viewBox", "").replace(",", " ").split()
    if len(vb) == 4:
        src_w = float(vb[2])
        src_h = float(vb[3])
    else:
        src_w = float(root.attrib.get("width", "0") or 0)
        src_h = float(root.attrib.get("height", "0") or 0)
    if src_w <= 0 or src_h <= 0:
        raise RuntimeError("traced SVG missing valid size/viewBox")

    paths: list[str] = []
    for el in root.iter():
        tag = el.tag.split("}", 1)[-1]
        if tag == "path" and el.attrib.get("d"):
            paths.append(el.attrib["d"])
    if not paths:
        raise RuntimeError("traced SVG contains no path data")

    return paths, src_w, src_h


def build_final_svg(icon_id: str, path_data: list[str], src_w: float, src_h: float, out_svg: Path) -> None:
    # Effective inner placement box: safe-area 24x24 with 1px inner padding => 22x22 at (5,5).
    target_x, target_y, target_w, target_h = 5.0, 5.0, 22.0, 22.0
    scale = min(target_w / src_w, target_h / src_h)
    tx = target_x + (target_w - src_w * scale) / 2.0
    ty = target_y + (target_h - src_h * scale) / 2.0

    root = svg_el("svg", viewBox="0 0 32 32")

    frame = svg_el(
        "rect",
        x="1",
        y="1",
        width="30",
        height="30",
        rx="4.8",
        ry="4.8",
        stroke="currentColor",
        **{"stroke-width": "2"},
        fill="none",
    )
    root.append(frame)

    g = svg_el("g", id=f"shape_{icon_id}", transform=f"translate({tx:.6f} {ty:.6f}) scale({scale:.6f})")
    for d in path_data:
        g.append(svg_el("path", d=d, fill="currentColor", stroke="none"))
    root.append(g)

    out_svg.parent.mkdir(parents=True, exist_ok=True)
    ET.ElementTree(root).write(out_svg, encoding="utf-8", xml_declaration=True)


def main() -> int:
    parser = argparse.ArgumentParser(description="Build Pictiq tile icon from silhouette PNG")
    parser.add_argument("--id", required=True, help="icon id")
    parser.add_argument("--input", required=True, help="input silhouette png")
    parser.add_argument("--out", required=True, help="output svg path")
    args = parser.parse_args()

    icon_id = args.id.strip()
    input_path = Path(args.input)
    out_path = Path(args.out)

    if not input_path.is_file():
        raise SystemExit(f"Input file not found: {input_path}")

    has_potrace = shutil.which("potrace") is not None
    has_inkscape = shutil.which("inkscape") is not None
    if not has_potrace and not has_inkscape:
        raise SystemExit(
            "No vectorizer available. Install potrace (recommended) or inkscape CLI and retry."
        )

    with tempfile.TemporaryDirectory(prefix="pictiq-trace-") as td:
        td_path = Path(td)
        pbm_path = td_path / "mask.pbm"
        traced_svg = td_path / "traced.svg"

        preprocess_to_pbm(input_path, pbm_path)

        if has_potrace:
            trace_with_potrace(pbm_path, traced_svg)
        else:
            trace_with_inkscape(input_path, traced_svg)

        paths, src_w, src_h = extract_paths(traced_svg)
        build_final_svg(icon_id, paths, src_w, src_h, out_path)

    print(f"Built icon: {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
