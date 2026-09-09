#!/usr/bin/env python3
"""Build a local visual review sheet for the supplied Standalone Batch C reference."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import cairosvg
import io

ROOT = Path(__file__).resolve().parents[1]
IDS = ["body_mouth", "rel_here", "rel_up", "rel_down", "nature_moon"]


def render(path: Path, px: int) -> Image.Image:
    svg = path.read_text(encoding="utf-8")
    svg = svg.replace('viewBox="0 0 32 32"', 'viewBox="0 0 32 32" color="#000000"', 1)
    data = cairosvg.svg2png(bytestring=svg.encode("utf-8"), output_width=px, output_height=px)
    return Image.open(io.BytesIO(data)).convert("RGBA")


def fit(image: Image.Image, box: tuple[int, int]) -> Image.Image:
    canvas = Image.new("RGBA", box, (255, 255, 255, 0))
    copy = image.convert("RGBA")
    copy.thumbnail((box[0], box[1]), Image.Resampling.LANCZOS)
    x = (box[0] - copy.width) // 2
    y = (box[1] - copy.height) // 2
    canvas.alpha_composite(copy, (x, y))
    return canvas


def main() -> None:
    out = ROOT / "build/qa/batch-c.png"
    out.parent.mkdir(parents=True, exist_ok=True)
    cell_w, cell_h = 430, 250
    sheet = Image.new("RGB", (cell_w * len(IDS), cell_h), "white")
    draw = ImageDraw.Draw(sheet)

    for index, icon_id in enumerate(IDS):
        x = index * cell_w
        source = Image.open(ROOT / "inputs/silhouettes/batch-c" / f"{icon_id}.png")
        source = fit(source, (140, 140))
        sheet.paste(source, (x + 14, 54), source)

        for image, pos in (
            (render(ROOT / "icons/svg" / f"{icon_id}.svg", 192), (x + 160, 16)),
            (render(ROOT / "icons/svg" / f"{icon_id}.svg", 64), (x + 360, 62)),
            (render(ROOT / "icons/svg" / f"{icon_id}.svg", 24), (x + 380, 145)),
        ):
            sheet.paste(image, pos, image)

        draw.text((x + 14, 14), icon_id, fill="black")
        draw.text((x + 145, 225), "source crop / canonical 192 / 64 / 24 px", fill="black")

    sheet.save(out)
    print(out)


if __name__ == "__main__":
    main()
