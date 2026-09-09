#!/usr/bin/env python3
"""Build a local visual review sheet for the supplied Standalone Batch B reference."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import cairosvg

ROOT = Path(__file__).resolve().parents[1]
IDS = ["eye_look", "item_clothing", "comm_speak", "comm_sound", "media_text", "media_image", "nature_sun", "state_light", "food_produce", "food_bakery", "rel_greater", "rel_lesser"]

def render(path: Path, px: int) -> Image.Image:
    data = cairosvg.svg2png(url=str(path), output_width=px, output_height=px)
    import io
    return Image.open(io.BytesIO(data)).convert("RGBA")

def main() -> None:
    out = ROOT / "build/qa/standalone-batch-b.png"; out.parent.mkdir(parents=True, exist_ok=True)
    cell_w, cell_h = 430, 230
    sheet = Image.new("RGB", (cell_w * 4, cell_h * 3), "white"); draw = ImageDraw.Draw(sheet)
    for index, icon_id in enumerate(IDS):
        x, y = (index % 4) * cell_w, (index // 4) * cell_h
        src = Image.open(ROOT / "inputs/silhouettes/standalone-batch-b" / f"{icon_id}.png").convert("RGB").resize((120, 120))
        sheet.paste(src, (x + 12, y + 42))
        for image, pos in ((render(ROOT / "icons/svg" / f"{icon_id}.svg", 192), (x + 145, y + 8)), (render(ROOT / "icons/svg" / f"{icon_id}.svg", 64), (x + 345, y + 50)), (render(ROOT / "icons/svg" / f"{icon_id}.svg", 24), (x + 365, y + 125))):
            sheet.paste(image, pos, image)
        draw.text((x + 12, y + 12), icon_id, fill="black")
        draw.text((x + 140, y + 205), "source crop / canonical 192 / 64 / 24 px", fill="black")
    sheet.save(out)
    print(out)

if __name__ == "__main__":
    main()
