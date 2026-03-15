#!/usr/bin/env python3
"""Generate handbook PNG figure assets from canonical Pictiq SVG tiles."""

from __future__ import annotations

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
PADDING = 36
GAP = 28


def _render_svg(svg_path: Path, out_png: Path, size: int, backend: str) -> None:
    svg_text = svg_path.read_text(encoding="utf-8")
    black_svg = _inject_current_color(svg_text, "#000000")
    if backend == "cairosvg":
        _render_with_cairosvg(black_svg, out_png, size, size)
    else:
        _render_with_inkscape(black_svg, out_png, size, size)


def _open_bw_tile(tmp_dir: Path, icons_dir: Path, icon_id: str, backend: str) -> Image.Image:
    tmp_png = tmp_dir / f"{icon_id}_{TILE_SIZE}.png"
    _render_svg(icons_dir / f"{icon_id}.svg", tmp_png, TILE_SIZE, backend)
    rgba = Image.open(tmp_png).convert("RGBA")
    alpha = rgba.split()[3]
    # Hard-threshold alpha to keep output strictly black-and-white.
    mask = alpha.point(lambda p: 255 if p >= 64 else 0, mode="1")
    bw = Image.new("RGB", rgba.size, "white")
    black = Image.new("RGB", rgba.size, "black")
    bw.paste(black, mask=mask.convert("L"))
    return bw


def _compose_grid(out_path: Path, rows: list[list[str]], icons_dir: Path, backend: str) -> None:
    cols = max(len(r) for r in rows)
    width = PADDING * 2 + cols * TILE_SIZE + (cols - 1) * GAP
    height = PADDING * 2 + len(rows) * TILE_SIZE + (len(rows) - 1) * GAP
    canvas = Image.new("RGB", (width, height), "white")

    with tempfile.TemporaryDirectory(prefix="pictiq_ch3_figs_") as td:
        tmp_dir = Path(td)
        for row_idx, row in enumerate(rows):
            row_w = len(row) * TILE_SIZE + (len(row) - 1) * GAP
            x0 = (width - row_w) // 2
            y0 = PADDING + row_idx * (TILE_SIZE + GAP)
            for col_idx, icon_id in enumerate(row):
                tile = _open_bw_tile(tmp_dir, icons_dir, icon_id, backend)
                x = x0 + col_idx * (TILE_SIZE + GAP)
                canvas.paste(tile, (x, y0))

    out_path.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(out_path)


def main() -> int:
    repo = Path(__file__).resolve().parents[1]
    icons_dir = repo / "icons" / "svg"
    out_dir = repo / "docs" / "handbook" / "figures"
    backend = _detect_backend("auto")
    print(f"Renderer backend: {backend}")

    fig_3_2_rows = [
        ["punct_question", "punct_exclaim", "logic_yes", "logic_no"],
        ["time", "qty_plus", "qty_minus", "qty_5"],
    ]
    fig_3_3_rows = [
        ["qty_1", "qty_2", "qty_5", "qty_plus", "qty_minus"],
    ]

    _compose_grid(out_dir / "fig-3-2-punct-logic.png", fig_3_2_rows, icons_dir, backend)
    _compose_grid(out_dir / "fig-3-3-quantity.png", fig_3_3_rows, icons_dir, backend)
    print(f"Wrote figures to: {out_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
