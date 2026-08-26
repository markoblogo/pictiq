#!/usr/bin/env python3
"""Render a non-canonical review sheet for the Nightlife layout assets."""

from __future__ import annotations

import tempfile
from pathlib import Path

from PIL import Image

from make_merch_layout import tile_bitmap
from render_png import _detect_backend


def fit(image: Image.Image, max_size: tuple[int, int]) -> Image.Image:
    copy = image.copy()
    copy.thumbnail(max_size, Image.Resampling.LANCZOS)
    return copy


def main() -> int:
    repo = Path(__file__).resolve().parents[1]
    wallet = repo / "layouts" / "wallet-card" / "nightlife"
    lighter = repo / "layouts" / "lighter" / "nightlife"
    out = repo / "layouts" / "overview" / "nightlife.png"
    out.parent.mkdir(parents=True, exist_ok=True)
    sheet = Image.new("RGB", (4200, 3000), "white")
    front = fit(Image.open(wallet / "front.png").convert("RGB"), (1850, 1200))
    back = fit(Image.open(wallet / "back.png").convert("RGB"), (1850, 1200))
    side_a = fit(Image.open(lighter / "side-a.png").convert("RGB"), (750, 1500))
    side_b = fit(Image.open(lighter / "side-b.png").convert("RGB"), (750, 1500))
    sheet.paste(front, (150, 140))
    sheet.paste(back, (2200, 140))
    sheet.paste(side_a, (450, 1380))
    sheet.paste(side_b, (1350, 1380))
    backend = _detect_backend("auto")
    with tempfile.TemporaryDirectory(prefix="pictiq_nightlife_overview_") as tmp:
        for index, icon_id in enumerate(("item_cigarette", "item_cannabis", "drink_beer", "love_heart", "item_condom")):
            tile = tile_bitmap(Path(tmp), repo / "icons" / "svg", icon_id, 360, backend)
            sheet.paste(tile, (2250 + index * 380, 1920))
    sheet.save(out)
    print(f"Wrote: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
