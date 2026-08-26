#!/usr/bin/env python3
"""Normalize the supplied two-sided lighter reference into a reusable template."""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageEnhance, ImageFilter, ImageOps


TILE_INTERIORS = (
    (101, 178, 274, 296),
    (101, 350, 274, 472),
    (101, 530, 274, 652),
    (602, 178, 775, 296),
    (602, 350, 775, 472),
    (602, 530, 775, 652),
)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path, help="supplied lighter reference image")
    parser.add_argument("output", type=Path, help="normalized template PNG")
    args = parser.parse_args()

    source = Image.open(args.source).convert("RGBA")
    white = Image.new("RGBA", source.size, "white")
    white.alpha_composite(source)
    gray = ImageOps.grayscale(white.convert("RGB"))
    gray = ImageEnhance.Contrast(gray).enhance(1.35).filter(ImageFilter.MedianFilter(3))
    template = gray.point(lambda value: 0 if value < 190 else 255).convert("RGB")

    # Remove the screenshot divider and original example pictograms while
    # retaining the photographed lighter bodies and their tile frames.
    template.paste("white", (430, 0, 480, template.height))
    for box in TILE_INTERIORS:
        template.paste("white", box)
    # Remove the few tall tips that extend above the central erase boxes in
    # the supplied cannabis and bar examples without touching tile borders.
    template.paste("white", (145, 335, 225, 360))
    template.paste("white", (145, 510, 225, 540))

    args.output.parent.mkdir(parents=True, exist_ok=True)
    template.save(args.output)
    print(f"Wrote: {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
