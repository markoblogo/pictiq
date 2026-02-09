#!/usr/bin/env python3
"""
Render tile SVGs into PNG variants.

Input:
- icons/svg/{id}.svg

Output:
- icons/png/black/{id}.png
- icons/png/white/{id}.png

Rendering backends:
1) Prefer cairosvg (Python import)
2) Fallback to Inkscape CLI (if installed)

Coloring:
This script assumes SVGs are authored using `currentColor` (fill/stroke) so we can
render black/white by injecting a `color: ...` style on the <svg> root element.
"""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Literal


ColorVariant = Literal["black", "white"]


def _inject_current_color(svg_text: str, color_hex: str) -> str:
    """
    Ensure <svg> root has `color: <hex>` in its style.

    Works for typical single-root SVGs. If the SVG doesn't use currentColor,
    this won't change appearance; that's by design (authoring requirement).
    """

    m = re.search(r"<svg\\b[^>]*>", svg_text, flags=re.IGNORECASE | re.DOTALL)
    if not m:
        return svg_text

    tag = m.group(0)

    # If style exists, append (preserving quote type).
    style_m = re.search(r"\\bstyle\\s*=\\s*(['\"])(.*?)\\1", tag, flags=re.IGNORECASE | re.DOTALL)
    if style_m:
        q = style_m.group(1)
        style_val = style_m.group(2).strip()
        if style_val and not style_val.endswith(";"):
            style_val += ";"
        style_val += f"color:{color_hex};"
        tag2 = tag[: style_m.start(2)] + style_val + tag[style_m.end(2) :]
    else:
        # Insert a style attribute before the closing '>'
        tag2 = tag[:-1] + f' style="color:{color_hex};">'

    return svg_text[: m.start()] + tag2 + svg_text[m.end() :]


def _detect_backend(prefer: str) -> str:
    if prefer in ("cairosvg", "auto"):
        try:
            import cairosvg  # noqa: F401

            return "cairosvg"
        except Exception:
            if prefer == "cairosvg":
                raise

    if prefer in ("inkscape", "auto"):
        if shutil.which("inkscape"):
            return "inkscape"
        if prefer == "inkscape":
            raise RuntimeError("inkscape not found in PATH")

    raise RuntimeError("no renderer available: install cairosvg or inkscape")


def _render_with_cairosvg(svg_text: str, out_path: Path, width: int, height: int) -> None:
    import cairosvg

    out_path.parent.mkdir(parents=True, exist_ok=True)
    cairosvg.svg2png(
        bytestring=svg_text.encode("utf-8"),
        write_to=str(out_path),
        output_width=width,
        output_height=height,
    )


def _render_with_inkscape(svg_text: str, out_path: Path, width: int, height: int) -> None:
    inkscape = shutil.which("inkscape")
    if not inkscape:
        raise RuntimeError("inkscape not found in PATH")

    out_path.parent.mkdir(parents=True, exist_ok=True)

    with tempfile.NamedTemporaryFile("w", suffix=".svg", delete=False, encoding="utf-8") as f:
        tmp_svg = Path(f.name)
        f.write(svg_text)

    try:
        # Try newer CLI first.
        cmd1 = [
            inkscape,
            str(tmp_svg),
            "--export-type=png",
            f"--export-filename={out_path}",
            "-w",
            str(width),
            "-h",
            str(height),
        ]
        r = subprocess.run(cmd1, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if r.returncode == 0:
            return

        # Fallback flags for some versions.
        cmd2 = [
            inkscape,
            str(tmp_svg),
            "--export-type=png",
            f"--export-filename={out_path}",
            f"--export-width={width}",
            f"--export-height={height}",
        ]
        r2 = subprocess.run(cmd2, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if r2.returncode != 0:
            raise RuntimeError(
                "inkscape export failed.\n"
                f"cmd: {' '.join(cmd1)}\n"
                f"stderr: {r.stderr.strip()}\n"
                f"cmd: {' '.join(cmd2)}\n"
                f"stderr: {r2.stderr.strip()}"
            )
    finally:
        try:
            tmp_svg.unlink(missing_ok=True)
        except Exception:
            pass


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description="Render icons/svg/*.svg to icons/png/{black,white}/*.png")
    ap.add_argument("--width", type=int, default=2400, help="PNG width (default: 2400)")
    ap.add_argument("--height", type=int, default=3200, help="PNG height (default: 3200)")
    ap.add_argument(
        "--renderer",
        choices=["auto", "cairosvg", "inkscape"],
        default="auto",
        help="Renderer backend (default: auto)",
    )
    ap.add_argument("--dry-run", action="store_true", help="Print planned outputs, do not write files")
    args = ap.parse_args(argv)

    repo = Path(__file__).resolve().parents[1]
    in_dir = repo / "icons" / "svg"
    out_black = repo / "icons" / "png" / "black"
    out_white = repo / "icons" / "png" / "white"

    svgs = sorted(p for p in in_dir.glob("*.svg") if p.name != ".gitkeep")
    if not svgs:
        print(f"No SVGs found in {in_dir} (nothing to render).")
        return 0

    backend = _detect_backend(args.renderer)
    render_fn = _render_with_cairosvg if backend == "cairosvg" else _render_with_inkscape

    print(f"Renderer: {backend}")
    print(f"Input: {in_dir}")
    print(f"Output: {out_black} and {out_white}")
    print(f"Size: {args.width}x{args.height}")

    for svg_path in svgs:
        svg_text = svg_path.read_text(encoding="utf-8")
        for variant, color in (("black", "#000000"), ("white", "#ffffff")):
            out_dir = out_black if variant == "black" else out_white
            out_path = out_dir / (svg_path.stem + ".png")
            if args.dry_run:
                print(f"[dry-run] {svg_path.name} -> {variant}/{out_path.name}")
                continue

            colored_svg = _inject_current_color(svg_text, color)
            render_fn(colored_svg, out_path, args.width, args.height)

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

