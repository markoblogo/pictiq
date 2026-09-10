#!/usr/bin/env python3
"""Render representative Batch C phrase and relation examples for review."""
from pathlib import Path
from PIL import Image, ImageDraw
import cairosvg
import io

ROOT = Path(__file__).resolve().parents[1]
ROWS = [
    ("body_mouth + need_food", ["body_mouth", "need_food"]),
    ("body_mouth + need_water", ["body_mouth", "need_water"]),
    ("rel_here + place_home", ["rel_here", "place_home"]),
    ("rel_here + time", ["rel_here", "time"]),
    ("move_feet + rel_up", ["move_feet", "rel_up"]),
    ("move_feet + rel_down", ["move_feet", "rel_down"]),
    ("time + nature_sun", ["time", "nature_sun"]),
    ("time + nature_moon", ["time", "nature_moon"]),
]


def tile(icon_id: str) -> Image.Image:
    svg_path = ROOT / "icons/svg" / f"{icon_id}.svg"
    svg = svg_path.read_text(encoding="utf-8")
    svg = svg.replace('viewBox="0 0 32 32"', 'viewBox="0 0 32 32" color="#000000"', 1)
    data = cairosvg.svg2png(bytestring=svg.encode("utf-8"), output_width=96, output_height=96)
    return Image.open(io.BytesIO(data)).convert("RGBA")


def main() -> None:
    out = ROOT / "build/qa/batch-c-compositions.png"
    out.parent.mkdir(parents=True, exist_ok=True)
    sheet = Image.new("RGB", (760, len(ROWS) * 112), "white")
    draw = ImageDraw.Draw(sheet)

    for i, (label, ids) in enumerate(ROWS):
        y = i * 112
        draw.text((12, y + 44), label, fill="black")
        x = 430
        for icon_id in ids:
            image = tile(icon_id)
            sheet.paste(image, (x, y + 8), image)
            x += 104

    sheet.save(out)
    print(out)


if __name__ == "__main__":
    main()
