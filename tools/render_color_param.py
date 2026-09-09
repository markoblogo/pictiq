#!/usr/bin/env python3
"""Render deterministic COLOR parameter demo instances and a grayscale sheet."""
from pathlib import Path
import argparse
from PIL import Image, ImageDraw
import cairosvg

COLORS = {"red": "#ff0000", "blue": "#264653", "yellow": "#f4d35e", "dark-grey-green": "#747b72", "very-light": "#eeeeee"}

def svg(value: str) -> str:
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" style="color:{value}">
<rect x="1" y="1" width="30" height="30" rx="4.8" fill="none" stroke="#000000" stroke-width="2"/>
<circle cx="16" cy="16" r="9" fill="currentColor"/>
</svg>'''

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", type=Path, default=Path("build/qa/color-param"))
    args = ap.parse_args(); args.out.mkdir(parents=True, exist_ok=True)
    images = []
    for name, value in COLORS.items():
        (args.out / f"{name}.svg").write_text(svg(value), encoding="utf-8")
        png = args.out / f"{name}.png"
        cairosvg.svg2png(bytestring=svg(value).encode(), write_to=str(png), output_width=192, output_height=192)
        images.append((name, Image.open(png).convert("RGB")))
    sheet = Image.new("RGB", (len(images) * 220, 250), "white"); draw = ImageDraw.Draw(sheet)
    for i, (name, image) in enumerate(images):
        x = i * 220 + 14; sheet.paste(image, (x, 10)); draw.text((x, 210), name, fill="black")
    sheet.save(args.out / "grayscale-source.png")
    gray = sheet.convert("L"); gray.save(args.out / "grayscale-comparison.png")
    print(f"OK: rendered {len(COLORS)} COLOR parameter values to {args.out}")

if __name__ == "__main__":
    main()
