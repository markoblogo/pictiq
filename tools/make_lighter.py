#!/usr/bin/env python3
"""Render a two-face disposable-lighter layout from a content profile."""

from __future__ import annotations

import argparse
import json
import tempfile
from pathlib import Path

from PIL import Image

from make_merch_layout import tile_bitmap
from render_png import _detect_backend
from layout_preview import draw_lighter_outline, place_artwork


CANVAS = (900, 2400)
TILE = 650
TOP = 170
GAP = 90
PREVIEW_MARGIN = 120
PREVIEW_GAP = 180


def render_side(icon_ids: list[str], temp_dir: Path, icons_dir: Path, backend: str) -> Image.Image:
    if len(icon_ids) != 3:
        raise ValueError(f"lighter side needs exactly 3 icons, got {len(icon_ids)}")
    image = Image.new("RGB", CANVAS, "white")
    x = (image.width - TILE) // 2
    for index, icon_id in enumerate(icon_ids):
        tile = tile_bitmap(temp_dir, icons_dir, icon_id, TILE, backend)
        image.paste(tile, (x, TOP + index * (TILE + GAP)))
    return image


def main() -> int:
    parser = argparse.ArgumentParser(description="Render a Pictiq disposable-lighter layout from a content profile")
    parser.add_argument("--profile", required=True, help="Profile ID from layouts/profiles/")
    parser.add_argument("--out-dir", help="Output directory (default: layouts/lighter/<profile>)")
    args = parser.parse_args()
    repo = Path(__file__).resolve().parents[1]
    profile = json.loads((repo / "layouts" / "profiles" / f"{args.profile}.json").read_text(encoding="utf-8"))
    lighter = profile.get("lighter")
    if not isinstance(lighter, dict):
        raise ValueError(f"profile {args.profile} has no lighter layout")
    side_a, side_b = lighter.get("side_a"), lighter.get("side_b")
    if not isinstance(side_a, list) or not isinstance(side_b, list):
        raise ValueError("lighter.side_a and lighter.side_b must be icon arrays")
    icons_dir = repo / "icons" / "svg"
    missing = [icon_id for icon_id in side_a + side_b if not (icons_dir / f"{icon_id}.svg").exists()]
    if missing:
        raise FileNotFoundError(f"missing SVG icons: {', '.join(missing)}")
    backend = _detect_backend("auto")
    out_dir = Path(args.out_dir) if args.out_dir else repo / "layouts" / "lighter" / args.profile
    out_dir.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="pictiq_lighter_") as tmp:
        side_a_image = render_side(side_a, Path(tmp), icons_dir, backend)
        side_b_image = render_side(side_b, Path(tmp), icons_dir, backend)
    preview = Image.new("RGB", (2600, 2800), "white")
    left=draw_lighter_outline(preview,(170,120,1190,2680)); right=draw_lighter_outline(preview,(1410,120,2430,2680))
    place_artwork(preview,side_a_image,left); place_artwork(preview,side_b_image,right)
    side_a_image.save(out_dir / "side-a.png")
    side_b_image.save(out_dir / "side-b.png")
    preview.save(out_dir / "preview.png")
    print(f"Renderer backend: {backend}")
    print(f"Wrote: {out_dir / 'side-a.png'}")
    print(f"Wrote: {out_dir / 'side-b.png'}")
    print(f"Wrote: {out_dir / 'preview.png'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
