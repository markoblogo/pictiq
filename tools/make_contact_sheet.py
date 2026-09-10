#!/usr/bin/env python3
"""Build the canonical icon overview contact sheet as PNG and PDF."""

from __future__ import annotations

import hashlib
import math
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from render_png import _detect_backend, _inject_current_color, _render_with_cairosvg, _render_with_inkscape


PREVIEW_SIZE = 256
COLUMNS = 7


def _render_with_quicklook(svg_text: str, png_path: Path, size: int) -> None:
    qlmanage = shutil.which("qlmanage")
    if not qlmanage:
        raise RuntimeError("qlmanage not found")
    png_path.parent.mkdir(parents=True, exist_ok=True)
    digest = hashlib.sha1(svg_text.encode("utf-8")).hexdigest()[:10]
    with tempfile.TemporaryDirectory(prefix="pictiq_ql_") as td:
        tmp_dir = Path(td)
        tmp_svg = tmp_dir / f"icon_{digest}.svg"
        tmp_svg.write_text(svg_text, encoding="utf-8")
        subprocess.run(
            [qlmanage, "-t", "-s", str(size), "-o", str(tmp_dir), str(tmp_svg)],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=True,
        )
        rendered = tmp_dir / f"{tmp_svg.name}.png"
        if not rendered.exists():
            candidates = list(tmp_dir.glob("*.png"))
            if not candidates:
                raise RuntimeError(f"QuickLook did not render {tmp_svg}")
            rendered = candidates[0]
        png_path.write_bytes(rendered.read_bytes())


def _render_preview(svg_path: Path, png_path: Path, backend: str) -> None:
    svg_text = _inject_current_color(svg_path.read_text(encoding="utf-8"), "#000000")
    if backend == "quicklook":
        _render_with_quicklook(svg_text, png_path, PREVIEW_SIZE)
    elif backend == "cairosvg":
        _render_with_cairosvg(svg_text, png_path, PREVIEW_SIZE, PREVIEW_SIZE)
    else:
        _render_with_inkscape(svg_text, png_path, PREVIEW_SIZE, PREVIEW_SIZE)


def _choose_backend() -> str:
    # QuickLook handles the full set of currentColor fill/stroke SVGs correctly on macOS.
    if shutil.which("qlmanage"):
        return "quicklook"
    return _detect_backend("auto")


def _load_fonts():
    from PIL import ImageFont

    def load(path: str, size: int):
        try:
            return ImageFont.truetype(path, size)
        except Exception:
            return ImageFont.load_default()

    return (
        load("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 30),
        load("/System/Library/Fonts/Supplemental/Arial.ttf", 18),
    )


def _build_png(previews: list[tuple[str, Path]], out_png: Path) -> None:
    from PIL import Image, ImageDraw

    title_font, label_font = _load_fonts()
    cols = COLUMNS
    tile = 192
    label_h = 28
    margin = 32
    spacing = 18
    header_h = 76
    rows = max(1, math.ceil(len(previews) / cols))

    width = margin * 2 + cols * tile + (cols - 1) * spacing
    height = margin * 2 + header_h + rows * (tile + label_h) + (rows - 1) * spacing
    page = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(page)
    draw.text((margin, 24), "Pictiq canonical ordinary icon grid", fill="black", font=title_font)
    draw.text(
        (margin, 58),
        f"{len(previews)} ordinary canonical icons; entity symbols and numeric notation are separate registries.",
        fill=(80, 88, 96),
        font=label_font,
    )

    for idx, (icon_id, preview_path) in enumerate(previews):
        col = idx % cols
        row = idx // cols
        x = margin + col * (tile + spacing)
        y = margin + header_h + row * (tile + label_h + spacing)

        icon_img = Image.open(preview_path).convert("RGBA")
        icon_img.thumbnail((tile, tile), Image.Resampling.LANCZOS)
        page.paste(icon_img, (x + (tile - icon_img.width) // 2, y + (tile - icon_img.height) // 2), icon_img)

        bbox = draw.textbbox((0, 0), icon_id, font=label_font)
        draw.text((x + (tile - (bbox[2] - bbox[0])) // 2, y + tile + 6), icon_id, fill="black", font=label_font)

    out_png.parent.mkdir(parents=True, exist_ok=True)
    page.save(out_png)


def _build_pdf_from_png(out_png: Path, out_pdf: Path) -> None:
    from PIL import Image

    img = Image.open(out_png).convert("RGB")
    img.save(out_pdf, "PDF", resolution=144.0)


def main() -> int:
    repo = Path(__file__).resolve().parents[1]
    icons_dir = repo / "icons" / "svg"
    lexicon = repo / "lexicon" / "icon-index.json"
    out_pdf = repo / "docs" / "overview" / "pictiq-core-grid.pdf"
    out_png = repo / "docs" / "overview" / "pictiq-core-grid.png"

    import json

    ids = [item["id"] for item in json.loads(lexicon.read_text(encoding="utf-8"))["icons"]]
    backend = _choose_backend()
    print(f"Rendering previews with: {backend}")

    with tempfile.TemporaryDirectory(prefix="pictiq_contact_sheet_") as td:
        tmp = Path(td)
        previews: list[tuple[str, Path]] = []
        for icon_id in ids:
            svg = icons_dir / f"{icon_id}.svg"
            preview = tmp / f"{icon_id}.png"
            _render_preview(svg, preview, backend)
            previews.append((icon_id, preview))
        _build_png(previews, out_png)
        _build_pdf_from_png(out_png, out_pdf)

    print(f"Wrote: {out_png}")
    print(f"Wrote: {out_pdf}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
