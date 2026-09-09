#!/usr/bin/env python3
"""Render representative Batch B phrase and comparison examples for review."""
from pathlib import Path
from PIL import Image, ImageDraw
import cairosvg, io

ROOT = Path(__file__).resolve().parents[1]
ROWS = [
    ("person_generic + eye_look", ["person_generic", "eye_look"]),
    ("person_generic + item_clothing", ["person_generic", "item_clothing"]),
    ("comm_speak + punct_question", ["comm_speak", "punct_question"]),
    ("comm_sound + logic_no", ["comm_sound", "logic_no"]),
    ("media_text + punct_question", ["media_text", "punct_question"]),
    ("media_image + punct_question", ["media_image", "punct_question"]),
    ("nature_sun + state_hot", ["nature_sun", "state_hot"]),
    ("state_light + logic_no", ["state_light", "logic_no"]),
    ("need_food + food_produce", ["need_food", "food_produce"]),
    ("place_shop + food_bakery", ["place_shop", "food_bakery"]),
    ("OBJECT_A + rel_greater + OBJECT_B", ["rel_greater"]),
    ("OBJECT_A + rel_lesser + OBJECT_B", ["rel_lesser"]),
    ("move_feet + rel_greater", ["move_feet", "rel_greater"]),
    ("move_feet + rel_lesser", ["move_feet", "rel_lesser"]),
]

def tile(icon_id: str) -> Image.Image:
    data = cairosvg.svg2png(url=str(ROOT / "icons/svg" / f"{icon_id}.svg"), output_width=96, output_height=96)
    return Image.open(io.BytesIO(data)).convert("RGBA")

def main() -> None:
    out = ROOT / "build/qa/standalone-batch-b-compositions.png"; out.parent.mkdir(parents=True, exist_ok=True)
    sheet = Image.new("RGB", (760, len(ROWS) * 112), "white"); draw = ImageDraw.Draw(sheet)
    for i, (label, ids) in enumerate(ROWS):
        y = i * 112; draw.text((12, y + 44), label, fill="black")
        x = 430
        for icon_id in ids:
            image = tile(icon_id); sheet.paste(image, (x, y + 8), image); x += 104
    sheet.save(out); print(out)

if __name__ == "__main__":
    main()
