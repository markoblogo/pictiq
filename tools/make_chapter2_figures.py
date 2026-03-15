#!/usr/bin/env python3
"""Generate Chapter 2 handbook figures from canonical Pictiq SVG icons."""

from __future__ import annotations

import json
import tempfile
import xml.etree.ElementTree as ET
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

from render_png import (
    _detect_backend,
    _inject_current_color,
    _render_with_cairosvg,
    _render_with_inkscape,
)


SVG_NS = "http://www.w3.org/2000/svg"
ET.register_namespace("", SVG_NS)

TILE_L = 128
TILE_S = 84
SPACE = 20
MARGIN = 36


def render_svg(svg_path: Path, out_path: Path, size: int, backend: str) -> None:
    svg_text = svg_path.read_text(encoding="utf-8")
    black_svg = _inject_current_color(svg_text, "#000000")
    if backend == "cairosvg":
        _render_with_cairosvg(black_svg, out_path, size, size)
    else:
        _render_with_inkscape(black_svg, out_path, size, size)


def open_icon(temp_dir: Path, icons_dir: Path, icon_id: str, size: int, backend: str) -> Image.Image:
    out = temp_dir / f"{icon_id}_{size}.png"
    render_svg(icons_dir / f"{icon_id}.svg", out, size, backend)
    return Image.open(out).convert("RGBA")


def load_core_ids(pack_path: Path) -> list[str]:
    data = json.loads(pack_path.read_text(encoding="utf-8"))
    return list(data["icons"])


def figure_2_1(temp_dir: Path, repo: Path, out_dir: Path, backend: str) -> None:
    template = ET.parse(repo / "templates" / "tile-template.svg")
    root = template.getroot()

    guides = None
    icon_group = None
    for el in root.findall(f"{{{SVG_NS}}}g"):
        if el.attrib.get("id") == "guides":
            guides = el
        if el.attrib.get("id") == "icon":
            icon_group = el
    if guides is None or icon_group is None:
        raise RuntimeError("Template missing guides/icon group")
    guides.attrib["style"] = "display:inline"

    logic_yes = ET.parse(repo / "icons" / "svg" / "logic_yes.svg").getroot()
    src_icon_group = None
    for el in logic_yes.findall(f"{{{SVG_NS}}}g"):
        if el.attrib.get("id") == "icon":
            src_icon_group = el
            break
    if src_icon_group is None:
        raise RuntimeError("logic_yes.svg missing icon group")
    for child in list(src_icon_group):
        icon_group.append(child)

    tmp_svg = temp_dir / "fig_2_1_template.svg"
    template.write(tmp_svg, encoding="utf-8", xml_declaration=True)
    tmp_png = temp_dir / "fig_2_1_base.png"
    render_svg(tmp_svg, tmp_png, 620, backend)

    base = Image.new("RGB", (980, 760), "white")
    tile = Image.open(tmp_png).convert("RGBA")
    x = (base.width - tile.width) // 2
    y = 52
    base.paste(tile, (x, y), tile)

    draw = ImageDraw.Draw(base)
    font = ImageFont.load_default()
    # Numeric markers only (text explanation is external in the book).
    draw.text((x + 306, y - 22), "1", fill="black", font=font)
    draw.text((x + 524, y + 130), "2", fill="black", font=font)
    draw.text((x + 305, y + 340), "3", fill="black", font=font)

    out_dir.mkdir(parents=True, exist_ok=True)
    base.save(out_dir / "fig-2-1-tile-anatomy.png")


def figure_2_2a(temp_dir: Path, repo: Path, out_dir: Path, backend: str) -> None:
    icons_dir = repo / "icons" / "svg"
    core_ids = load_core_ids(repo / "packs" / "universal-core.json")
    top_ids = core_ids[:14]

    width = 1700
    top_rows = 2
    top_cols = 7
    bottom_cols = 8
    bottom_rows = (len(core_ids) + bottom_cols - 1) // bottom_cols
    height = (
        MARGIN * 2
        + top_rows * TILE_L
        + (top_rows - 1) * SPACE
        + 56
        + bottom_rows * TILE_S
        + (bottom_rows - 1) * SPACE
    )
    img = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(img)

    top_block_w = top_cols * TILE_L + (top_cols - 1) * SPACE
    top_x = (width - top_block_w) // 2
    y = MARGIN
    for i, icon_id in enumerate(top_ids):
        row = i // top_cols
        col = i % top_cols
        px = top_x + col * (TILE_L + SPACE)
        py = y + row * (TILE_L + SPACE)
        icon = open_icon(temp_dir, icons_dir, icon_id, TILE_L, backend)
        img.paste(icon, (px, py), icon)

    split_y = y + top_rows * TILE_L + (top_rows - 1) * SPACE + 28
    draw.line((MARGIN, split_y, width - MARGIN, split_y), fill="black", width=2)

    bottom_block_w = bottom_cols * TILE_S + (bottom_cols - 1) * SPACE
    bottom_x = (width - bottom_block_w) // 2
    by = split_y + 28
    for i, icon_id in enumerate(core_ids):
        row = i // bottom_cols
        col = i % bottom_cols
        px = bottom_x + col * (TILE_S + SPACE)
        py = by + row * (TILE_S + SPACE)
        icon = open_icon(temp_dir, icons_dir, icon_id, TILE_S, backend)
        img.paste(icon, (px, py), icon)

    out_dir.mkdir(parents=True, exist_ok=True)
    img.save(out_dir / "fig-2-2a-grid-split.png")


def figure_2_2b(temp_dir: Path, repo: Path, out_dir: Path, backend: str) -> None:
    icons_dir = repo / "icons" / "svg"
    lines = [
        ["need_toilet", "punct_question"],
        ["safety_medical", "punct_exclaim"],
        ["need_water", "qty_2"],
        ["move_taxi", "punct_question"],
        ["money_card", "punct_question"],
        ["money_card", "logic_no"],
        ["place_hotel", "comm_wifi", "punct_question"],
        ["move_public", "time", "punct_question"],
    ]

    cols = max(len(line) for line in lines)
    width = MARGIN * 2 + cols * TILE_L + (cols - 1) * SPACE
    height = MARGIN * 2 + len(lines) * TILE_L + (len(lines) - 1) * SPACE
    img = Image.new("RGB", (width, height), "white")

    for row, line in enumerate(lines):
        row_w = len(line) * TILE_L + (len(line) - 1) * SPACE
        x = (width - row_w) // 2
        y = MARGIN + row * (TILE_L + SPACE)
        for col, icon_id in enumerate(line):
            px = x + col * (TILE_L + SPACE)
            icon = open_icon(temp_dir, icons_dir, icon_id, TILE_L, backend)
            img.paste(icon, (px, y), icon)

    out_dir.mkdir(parents=True, exist_ok=True)
    img.save(out_dir / "fig-2-2b-phrase-lines.png")


def figure_2_3(temp_dir: Path, repo: Path, out_dir: Path, backend: str) -> None:
    icons_dir = repo / "icons" / "svg"
    rows = [
        ["need_water"],
        ["need_water", "punct_question"],
        ["safety_medical", "punct_exclaim"],
        ["money_card", "logic_no"],
        ["place_shop", "comm_phone"],
    ]

    width = 1280
    header_h = 64
    footer_h = 44
    body_h = len(rows) * TILE_L + (len(rows) - 1) * SPACE
    height = MARGIN * 2 + header_h + body_h + footer_h
    img = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(img)
    font = ImageFont.load_default()

    draw.text((MARGIN, MARGIN), "Pictiq quick rules", fill="black", font=font)

    y0 = MARGIN + header_h
    for row, line in enumerate(rows):
        row_w = len(line) * TILE_L + (len(line) - 1) * SPACE
        x = (width - row_w) // 2
        y = y0 + row * (TILE_L + SPACE)
        for col, icon_id in enumerate(line):
            px = x + col * (TILE_L + SPACE)
            icon = open_icon(temp_dir, icons_dir, icon_id, TILE_L, backend)
            img.paste(icon, (px, y), icon)

    draw.text((MARGIN, height - MARGIN - 14), "Point to tiles; combine tokens left to right.", fill="black", font=font)

    out_dir.mkdir(parents=True, exist_ok=True)
    img.save(out_dir / "fig-2-3-rules-card.png")


def main() -> int:
    repo = Path(__file__).resolve().parents[1]
    out_dir = repo / "docs" / "handbook" / "figures"
    backend = _detect_backend("auto")
    print(f"Renderer backend: {backend}")

    with tempfile.TemporaryDirectory(prefix="pictiq_ch2_figs_") as td:
        temp_dir = Path(td)
        figure_2_1(temp_dir, repo, out_dir, backend)
        figure_2_2a(temp_dir, repo, out_dir, backend)
        figure_2_2b(temp_dir, repo, out_dir, backend)
        figure_2_3(temp_dir, repo, out_dir, backend)

    print(f"Wrote figures to: {out_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
