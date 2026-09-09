#!/usr/bin/env python3
"""Build a local visual review sheet for Pictiq entity-symbol examples."""
from __future__ import annotations

import io
import json
from pathlib import Path

import cairosvg
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[1]


def render(svg_path: Path, px: int) -> Image.Image:
    svg = svg_path.read_text(encoding="utf-8")
    svg = svg.replace('viewBox="0 0 32 32"', 'viewBox="0 0 32 32" color="#000000"', 1)
    data = cairosvg.svg2png(bytestring=svg.encode("utf-8"), output_width=px, output_height=px)
    return Image.open(io.BytesIO(data)).convert("RGBA")


def fit(image: Image.Image, box: tuple[int, int]) -> Image.Image:
    canvas = Image.new("RGBA", box, (255, 255, 255, 0))
    copy = image.convert("RGBA")
    copy.thumbnail(box, Image.Resampling.LANCZOS)
    canvas.alpha_composite(copy, ((box[0] - copy.width) // 2, (box[1] - copy.height) // 2))
    return canvas


def main() -> None:
    registry = json.loads((ROOT / "entities" / "entity-index.json").read_text(encoding="utf-8"))["symbols"]
    out = ROOT / "build" / "qa" / "entity-symbols-demo.png"
    out.parent.mkdir(parents=True, exist_ok=True)

    cell_w, cell_h = 620, 270
    columns = 2
    sheet = Image.new("RGB", (cell_w * columns, cell_h * 3), "white")
    draw = ImageDraw.Draw(sheet)

    for index, symbol in enumerate(registry):
        x = (index % columns) * cell_w
        y = (index // columns) * cell_h
        crop = fit(Image.open(ROOT / symbol["provenance"]["source_crop_path"]), (118, 142))
        sheet.paste(crop, (x + 14, y + 58), crop)

        canonical = render(ROOT / symbol["icon_path"], 192)
        small64 = render(ROOT / symbol["icon_path"], 64)
        small24 = render(ROOT / symbol["icon_path"], 24)
        sheet.paste(canonical, (x + 160, y + 18), canonical)
        sheet.paste(small64, (x + 370, y + 74), small64)
        sheet.paste(small24, (x + 455, y + 94), small24)

        label = symbol["display_name"]
        draw.text((x + 14, y + 14), label, fill="black")
        draw.text((x + 14, y + 222), symbol["id"], fill="black")
        draw.text((x + 160, y + 244), "reference / canonical frame / 64 / 24 px", fill="black")

    sheet.save(out)
    print(out)


if __name__ == "__main__":
    main()
