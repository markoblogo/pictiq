#!/usr/bin/env python3
"""Generate Paris merch artwork layouts from canonical SVG icons."""

from __future__ import annotations

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


PRINT_SIZE = (2400, 3200)
PREVIEW_SIZE = (1200, 1600)
OUTER_MARGIN = 160
BLOCK_GAP = 90

TOP_TILE = 360
TOP_SPACE = 40
TOP_COLS = 5

BOTTOM_TILE = 250
BOTTOM_SPACE = 28
BOTTOM_COLS = 6

BOTTOM_SUBSET = [
    "punct_question",
    "punct_exclaim",
    "logic_yes",
    "logic_no",
    "time",
    "qty_1",
    "qty_2",
    "qty_5",
    "qty_minus",
    "qty_plus",
    "money_coins",
    "money_card",
    "money_atm_bank",
    "comm_wifi",
    "comm_phone",
    "power_plug",
    "need_toilet",
    "need_water",
    "need_food",
    "need_bar",
    "place_hotel",
    "place_shop",
    "place_landmark_park",
    "move_feet",
    "move_taxi",
    "move_public",
    "place_airport",
]


def render_black_svg(svg_path: Path, out_png: Path, size: int, backend: str) -> None:
    svg_text = svg_path.read_text(encoding="utf-8")
    black_svg = _inject_current_color(svg_text, "#000000")
    if backend == "cairosvg":
        _render_with_cairosvg(black_svg, out_png, size, size)
    else:
        _render_with_inkscape(black_svg, out_png, size, size)


def tile_bitmap(temp_dir: Path, icons_dir: Path, icon_id: str, size: int, backend: str) -> Image.Image:
    out = temp_dir / f"{icon_id}_{size}.png"
    render_black_svg(icons_dir / f"{icon_id}.svg", out, size, backend)
    rgba = Image.open(out).convert("RGBA")
    alpha = rgba.split()[3]
    mask = alpha.point(lambda p: 255 if p >= 64 else 0, mode="1")
    tile = Image.new("RGB", (size, size), "white")
    tile.paste(Image.new("RGB", (size, size), "black"), mask=mask.convert("L"))
    return tile


def block_dims(count: int, cols: int, tile: int, gap: int) -> tuple[int, int, int]:
    rows = max(1, math.ceil(count / cols))
    width = cols * tile + (cols - 1) * gap
    height = rows * tile + (rows - 1) * gap
    return width, height, rows


def place_block(
    canvas: Image.Image,
    icons: list[str],
    cols: int,
    tile: int,
    gap: int,
    y_start: int,
    temp_dir: Path,
    icons_dir: Path,
    backend: str,
) -> int:
    draw_w, draw_h = canvas.size
    block_w, block_h, rows = block_dims(len(icons), cols, tile, gap)
    x0 = (draw_w - block_w) // 2

    for idx, icon_id in enumerate(icons):
        row = idx // cols
        col = idx % cols
        x = x0 + col * (tile + gap)
        y = y_start + row * (tile + gap)
        tile_img = tile_bitmap(temp_dir, icons_dir, icon_id, tile, backend)
        canvas.paste(tile_img, (x, y))

    return y_start + block_h


def main() -> int:
    repo = Path(__file__).resolve().parents[1]
    icons_dir = repo / "icons" / "svg"
    pack_path = repo / "packs" / "city-paris-v0.1.json"
    out_dir = repo / "docs" / "merch"
    out_print = out_dir / "paris-shirt-print-2400x3200.png"
    out_preview = out_dir / "paris-shirt-preview-1200x1600.png"

    pack = json.loads(pack_path.read_text(encoding="utf-8"))
    top_icons = list(pack.get("icons", []))

    required = list(top_icons) + list(BOTTOM_SUBSET)
    missing = sorted({icon_id for icon_id in required if not (icons_dir / f"{icon_id}.svg").exists()})
    if missing:
        print("Missing required SVG icons:")
        for icon_id in missing:
            print(f"- {icons_dir / f'{icon_id}.svg'}")
        return 1

    backend = _detect_backend("auto")
    print(f"Renderer backend: {backend}")

    out_dir.mkdir(parents=True, exist_ok=True)
    canvas = Image.new("RGB", PRINT_SIZE, "white")

    with tempfile.TemporaryDirectory(prefix="pictiq_merch_layout_") as td:
        temp_dir = Path(td)

        top_w, top_h, _ = block_dims(len(top_icons), TOP_COLS, TOP_TILE, TOP_SPACE)
        bot_w, bot_h, _ = block_dims(len(BOTTOM_SUBSET), BOTTOM_COLS, BOTTOM_TILE, BOTTOM_SPACE)
        total_h = top_h + BLOCK_GAP + bot_h
        available_h = PRINT_SIZE[1] - 2 * OUTER_MARGIN
        if total_h > available_h:
            print(
                f"Layout overflow: required {total_h}px, available {available_h}px "
                f"(top={top_h}, bottom={bot_h}, gap={BLOCK_GAP})."
            )
            return 1

        y = OUTER_MARGIN
        y = place_block(canvas, top_icons, TOP_COLS, TOP_TILE, TOP_SPACE, y, temp_dir, icons_dir, backend)
        y += BLOCK_GAP
        place_block(canvas, BOTTOM_SUBSET, BOTTOM_COLS, BOTTOM_TILE, BOTTOM_SPACE, y, temp_dir, icons_dir, backend)

    canvas.save(out_print)
    preview = canvas.resize(PREVIEW_SIZE, resample=Image.Resampling.NEAREST)
    preview.save(out_preview)

    print(f"Wrote: {out_print}")
    print(f"Wrote: {out_preview}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
