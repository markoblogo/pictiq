#!/usr/bin/env python3
"""Build an icon overview contact sheet from icons/svg as A4 PDF (+ optional PNG)."""

from __future__ import annotations

import math
import sys
import tempfile
from pathlib import Path

from reportlab.lib.pagesizes import A4
from reportlab.lib.utils import ImageReader
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas

from render_png import (
    _detect_backend,
    _inject_current_color,
    _render_with_cairosvg,
    _render_with_inkscape,
)


PREVIEW_SIZE = 256
MARGIN_MM = 12
COLUMNS = 6
LABEL_FONT = "Helvetica"
LABEL_SIZE = 7


def _render_preview(svg_path: Path, png_path: Path, backend: str) -> None:
    svg_text = svg_path.read_text(encoding="utf-8")
    colored_svg = _inject_current_color(svg_text, "#000000")
    if backend == "cairosvg":
        _render_with_cairosvg(colored_svg, png_path, PREVIEW_SIZE, PREVIEW_SIZE)
    else:
        _render_with_inkscape(colored_svg, png_path, PREVIEW_SIZE, PREVIEW_SIZE)


def _build_pdf(previews: list[tuple[str, Path]], out_pdf: Path) -> None:
    page_w, page_h = A4
    margin = MARGIN_MM * mm
    grid_w = page_w - 2 * margin
    grid_h = page_h - 2 * margin
    cell_w = grid_w / COLUMNS
    cell_h = cell_w + 16
    rows_per_page = max(1, int(grid_h // cell_h))
    per_page = COLUMNS * rows_per_page

    out_pdf.parent.mkdir(parents=True, exist_ok=True)
    c = canvas.Canvas(str(out_pdf), pagesize=A4, pageCompression=1)
    c.setAuthor("Pictiq")
    c.setTitle("Pictiq Core Grid")

    for idx, (icon_id, png_path) in enumerate(previews):
        slot = idx % per_page
        if idx > 0 and slot == 0:
            c.showPage()

        row = slot // COLUMNS
        col = slot % COLUMNS

        x = margin + col * cell_w
        y_top = page_h - margin - row * cell_h

        img_size = min(cell_w - 8, cell_h - 18)
        img_x = x + (cell_w - img_size) / 2
        img_y = y_top - img_size - 2
        c.drawImage(
            ImageReader(str(png_path)),
            img_x,
            img_y,
            width=img_size,
            height=img_size,
            preserveAspectRatio=True,
            mask="auto",
        )

        c.setFont(LABEL_FONT, LABEL_SIZE)
        c.drawCentredString(x + cell_w / 2, img_y - 8, icon_id)

    c.save()


def _build_optional_png(previews: list[tuple[str, Path]], out_png: Path) -> bool:
    try:
        from PIL import Image, ImageDraw, ImageFont
    except Exception:
        return False

    cols = COLUMNS
    rows = max(1, math.ceil(len(previews) / cols))
    tile = 256
    label_h = 22
    margin = 24
    spacing = 16

    width = margin * 2 + cols * tile + (cols - 1) * spacing
    height = margin * 2 + rows * (tile + label_h) + (rows - 1) * spacing
    page = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(page)
    font = ImageFont.load_default()

    for idx, (icon_id, preview_path) in enumerate(previews):
        col = idx % cols
        row = idx // cols
        x = margin + col * (tile + spacing)
        y = margin + row * (tile + label_h + spacing)

        icon_img = Image.open(preview_path).convert("RGBA")
        page.paste(icon_img, (x, y), icon_img)

        bbox = draw.textbbox((0, 0), icon_id, font=font)
        text_w = bbox[2] - bbox[0]
        tx = x + (tile - text_w) // 2
        ty = y + tile + 4
        draw.text((tx, ty), icon_id, fill="black", font=font)

    out_png.parent.mkdir(parents=True, exist_ok=True)
    page.save(out_png)
    return True


def main() -> int:
    repo = Path(__file__).resolve().parents[1]
    icons_dir = repo / "icons" / "svg"
    out_pdf = repo / "docs" / "overview" / "pictiq-core-grid.pdf"
    out_png = repo / "docs" / "overview" / "pictiq-core-grid.png"

    svgs = sorted(p for p in icons_dir.glob("*.svg") if p.name != ".gitkeep")
    if not svgs:
        print(f"No SVG icons found in {icons_dir}")
        return 1

    backend = _detect_backend("auto")
    print(f"Rendering previews with: {backend}")

    with tempfile.TemporaryDirectory(prefix="pictiq_contact_sheet_") as td:
        tmp = Path(td)
        previews: list[tuple[str, Path]] = []
        for svg in svgs:
            icon_id = svg.stem
            preview = tmp / f"{icon_id}.png"
            _render_preview(svg, preview, backend)
            previews.append((icon_id, preview))

        _build_pdf(previews, out_pdf)
        png_written = _build_optional_png(previews, out_png)

    print(f"Wrote: {out_pdf}")
    if png_written:
        print(f"Wrote: {out_png}")
    else:
        print("Skipped optional PNG contact sheet (Pillow not available).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
