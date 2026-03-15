#!/usr/bin/env python3
"""Generate a black-and-white pack grid (PNG + PDF) from a pack JSON file."""

from __future__ import annotations

import argparse
import json
import math
import tempfile
from pathlib import Path

from PIL import Image

from render_png import (
    _detect_backend,
    _inject_current_color,
    _render_with_cairosvg,
    _render_with_inkscape,
)


TILE_SIZE = 256
GAP = 28
MARGIN = 36


def render_svg_black(svg_path: Path, out_png: Path, size: int, backend: str) -> None:
    svg_text = svg_path.read_text(encoding="utf-8")
    black_svg = _inject_current_color(svg_text, "#000000")
    if backend == "cairosvg":
        _render_with_cairosvg(black_svg, out_png, size, size)
    else:
        _render_with_inkscape(black_svg, out_png, size, size)


def open_bw_tile(temp_dir: Path, icons_dir: Path, icon_id: str, backend: str) -> Image.Image:
    tile_png = temp_dir / f"{icon_id}_{TILE_SIZE}.png"
    render_svg_black(icons_dir / f"{icon_id}.svg", tile_png, TILE_SIZE, backend)
    rgba = Image.open(tile_png).convert("RGBA")
    alpha = rgba.split()[3]
    # Hard threshold to keep pure black/white output.
    mask = alpha.point(lambda p: 255 if p >= 64 else 0, mode="1")
    tile = Image.new("RGB", (TILE_SIZE, TILE_SIZE), "white")
    black = Image.new("RGB", (TILE_SIZE, TILE_SIZE), "black")
    tile.paste(black, mask=mask.convert("L"))
    return tile


def build_pack_grid(pack_icons: list[str], icons_dir: Path, backend: str, columns: int) -> Image.Image:
    rows = max(1, math.ceil(len(pack_icons) / columns))
    width = MARGIN * 2 + columns * TILE_SIZE + (columns - 1) * GAP
    height = MARGIN * 2 + rows * TILE_SIZE + (rows - 1) * GAP
    canvas = Image.new("RGB", (width, height), "white")

    with tempfile.TemporaryDirectory(prefix="pictiq_pack_grid_") as td:
        tmp = Path(td)
        for idx, icon_id in enumerate(pack_icons):
            row = idx // columns
            col = idx % columns
            x = MARGIN + col * (TILE_SIZE + GAP)
            y = MARGIN + row * (TILE_SIZE + GAP)
            tile = open_bw_tile(tmp, icons_dir, icon_id, backend)
            canvas.paste(tile, (x, y))

    return canvas


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate pack grid PNG/PDF from pack JSON")
    parser.add_argument("--pack", default="packs/city-paris-v0.1.json", help="Path to pack JSON")
    parser.add_argument("--out-png", default="docs/overview/paris-pack-grid.png", help="Output PNG path")
    parser.add_argument("--out-pdf", default="docs/overview/paris-pack-grid.pdf", help="Output PDF path")
    parser.add_argument("--columns", type=int, default=5, help="Grid columns (default: 5)")
    args = parser.parse_args()

    repo = Path(__file__).resolve().parents[1]
    pack_path = repo / args.pack
    out_png = repo / args.out_png
    out_pdf = repo / args.out_pdf
    icons_dir = repo / "icons" / "svg"

    pack_data = json.loads(pack_path.read_text(encoding="utf-8"))
    icon_ids = list(pack_data.get("icons", []))
    if not icon_ids:
        raise RuntimeError(f"No icons in pack: {pack_path}")

    missing = [icon_id for icon_id in icon_ids if not (icons_dir / f"{icon_id}.svg").exists()]
    if missing:
        raise RuntimeError("Missing SVG(s): " + ", ".join(missing))

    backend = _detect_backend("auto")
    print(f"Renderer backend: {backend}")
    image = build_pack_grid(icon_ids, icons_dir, backend, args.columns)

    out_png.parent.mkdir(parents=True, exist_ok=True)
    out_pdf.parent.mkdir(parents=True, exist_ok=True)
    image.save(out_png)
    image.save(out_pdf, "PDF", resolution=300.0)

    print(f"Wrote: {out_png}")
    print(f"Wrote: {out_pdf}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
