#!/usr/bin/env python3
"""Render a two-face disposable-lighter layout from a content profile."""

from __future__ import annotations

import argparse
import json
import tempfile
from pathlib import Path

from PIL import Image, ImageOps

from make_merch_layout import tile_bitmap
from render_png import _detect_backend


CANVAS = (900, 2400)
TILE = 650
TOP = 170
GAP = 90
PREVIEW_SCALE = 3
PREVIEW_ICON_BOXES = (
    (101, 165, 274, 296),
    (101, 340, 274, 472),
    (101, 520, 274, 652),
    (602, 165, 775, 296),
    (602, 340, 775, 472),
    (602, 520, 775, 652),
)


def render_side(icon_ids: list[str], temp_dir: Path, icons_dir: Path, backend: str) -> Image.Image:
    if len(icon_ids) != 3:
        raise ValueError(f"lighter side needs exactly 3 icons, got {len(icon_ids)}")
    image = Image.new("RGB", CANVAS, "white")
    x = (image.width - TILE) // 2
    for index, icon_id in enumerate(icon_ids):
        tile = tile_bitmap(temp_dir, icons_dir, icon_id, TILE, backend)
        image.paste(tile, (x, TOP + index * (TILE + GAP)))
    return image


def pictogram_bitmap(tile: Image.Image) -> Image.Image:
    """Remove the canonical tile frame while retaining its pictogram."""
    mono = tile.convert("L")
    pixels = mono.load()
    seen: set[tuple[int, int]] = set()
    components: list[list[tuple[int, int]]] = []
    for y in range(mono.height):
        for x in range(mono.width):
            if pixels[x, y] >= 128 or (x, y) in seen:
                continue
            stack = [(x, y)]
            seen.add((x, y))
            component: list[tuple[int, int]] = []
            while stack:
                px, py = stack.pop()
                component.append((px, py))
                for neighbor in ((px - 1, py), (px + 1, py), (px, py - 1), (px, py + 1)):
                    nx, ny = neighbor
                    if (
                        0 <= nx < mono.width
                        and 0 <= ny < mono.height
                        and neighbor not in seen
                        and pixels[nx, ny] < 128
                    ):
                        seen.add(neighbor)
                        stack.append(neighbor)
            components.append(component)

    result = tile.copy()
    frame = next(
        (
            component
            for component in components
            if (max(x for x, _ in component) - min(x for x, _ in component)) >= mono.width * 0.9
            and (max(y for _, y in component) - min(y for _, y in component)) >= mono.height * 0.9
        ),
        None,
    )
    if frame:
        for x, y in frame:
            result.putpixel((x, y), (255, 255, 255))
    return result


def render_preview(
    template_path: Path,
    icon_ids: list[str],
    temp_dir: Path,
    icons_dir: Path,
    backend: str,
) -> Image.Image:
    if not template_path.exists():
        raise FileNotFoundError(f"missing lighter preview template: {template_path}")
    preview = Image.open(template_path).convert("RGB")
    for icon_id, box in zip(icon_ids, PREVIEW_ICON_BOXES, strict=True):
        width, height = box[2] - box[0], box[3] - box[1]
        icon = pictogram_bitmap(tile_bitmap(temp_dir, icons_dir, icon_id, min(width, height), backend))
        content_box = ImageOps.invert(icon.convert("L")).getbbox()
        if content_box:
            icon = icon.crop(content_box)
            target_width, target_height = int(width * 0.80), int(height * 0.82)
            scale = min(target_width / icon.width, target_height / icon.height)
            icon = icon.resize(
                (max(1, round(icon.width * scale)), max(1, round(icon.height * scale))),
                Image.Resampling.LANCZOS,
            )
        x = box[0] + (width - icon.width) // 2
        y = box[1] + (height - icon.height) // 2
        preview.paste(icon, (x, y))
    return preview.resize(
        (preview.width * PREVIEW_SCALE, preview.height * PREVIEW_SCALE),
        Image.Resampling.LANCZOS,
    )


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
        temp_dir = Path(tmp)
        side_a_image = render_side(side_a, temp_dir, icons_dir, backend)
        side_b_image = render_side(side_b, temp_dir, icons_dir, backend)
        preview = render_preview(
            repo / "inputs" / "layout-templates" / "lighter-two-sided.png",
            side_a + side_b,
            temp_dir,
            icons_dir,
            backend,
        )
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
