#!/usr/bin/env python3
"""Render a two-sided Pictiq wallet card from a content profile."""

from __future__ import annotations

import argparse
import json
import tempfile
from pathlib import Path

from PIL import Image, ImageDraw

from make_merch_layout import tile_bitmap
from render_png import _detect_backend


# 4280 / 2699 is the exact 85.60 / 53.98 mm ID-1 aspect ratio at 1270 dpi.
DPI = 1270
CARD_MM = (85.60, 53.98)
CARD_SIZE = (4280, 2699)
PX_PER_MM = DPI / 25.4
OUTLINE_WIDTH = round(0.4 * PX_PER_MM)
OUTLINE_RADIUS = round(3.18 * PX_PER_MM)
SAFE_INSET = round(3.5 * PX_PER_MM)
PREVIEW_GAP = round(2.4 * PX_PER_MM)
PREVIEW_MARGIN = round(1.6 * PX_PER_MM)


def select_group(profile: dict, group: str) -> list[str]:
    exclusions = set(profile.get("wallet_card", {}).get(f"exclude_{group}", []))
    return [icon_id for icon_id in profile[group] if icon_id not in exclusions]


def render_side(
    icon_ids: list[str],
    columns: int,
    rows: int,
    vertical_gap_mm: float,
    temp_dir: Path,
    icons_dir: Path,
    backend: str,
) -> Image.Image:
    if len(icon_ids) > columns * rows:
        raise ValueError(f"{len(icon_ids)} icons exceed {columns}x{rows} capacity")

    canvas = Image.new("RGB", CARD_SIZE, "white")
    draw = ImageDraw.Draw(canvas)
    outline_inset = OUTLINE_WIDTH // 2 + 1
    draw.rounded_rectangle(
        (outline_inset, outline_inset, canvas.width - outline_inset - 1, canvas.height - outline_inset - 1),
        radius=OUTLINE_RADIUS,
        outline="black",
        width=OUTLINE_WIDTH,
    )

    safe_width = canvas.width - 2 * SAFE_INSET
    safe_height = canvas.height - 2 * SAFE_INSET
    gap_y = round(vertical_gap_mm * PX_PER_MM)
    tile_size = (safe_height - (rows - 1) * gap_y) // rows
    gap_x = (safe_width - columns * tile_size) // (columns - 1)
    width = columns * tile_size + (columns - 1) * gap_x
    height = rows * tile_size + (rows - 1) * gap_y
    x0 = (canvas.width - width) // 2
    y0 = (canvas.height - height) // 2

    for index, icon_id in enumerate(icon_ids):
        row, col = divmod(index, columns)
        tile = tile_bitmap(temp_dir, icons_dir, icon_id, tile_size, backend)
        canvas.paste(tile, (x0 + col * (tile_size + gap_x), y0 + row * (tile_size + gap_y)))
    return canvas


def make_preview(front: Image.Image, back: Image.Image) -> Image.Image:
    width = front.width * 2 + PREVIEW_GAP + PREVIEW_MARGIN * 2
    height = front.height + PREVIEW_MARGIN * 2
    preview = Image.new("RGB", (width, height), "white")
    preview.paste(front, (PREVIEW_MARGIN, PREVIEW_MARGIN))
    preview.paste(back, (PREVIEW_MARGIN + front.width + PREVIEW_GAP, PREVIEW_MARGIN))
    return preview


def main() -> int:
    parser = argparse.ArgumentParser(description="Render a Pictiq wallet card from a content profile")
    parser.add_argument("--profile", required=True, help="Profile ID from layouts/profiles/")
    parser.add_argument("--out-dir", help="Output directory (default: layouts/wallet-card/<profile>)")
    args = parser.parse_args()

    repo = Path(__file__).resolve().parents[1]
    profile_path = repo / "layouts" / "profiles" / f"{args.profile}.json"
    if not profile_path.exists():
        parser.error(f"profile not found: {profile_path}")
    profile = json.loads(profile_path.read_text(encoding="utf-8"))
    primary = select_group(profile, "primary")
    secondary = select_group(profile, "secondary")
    if len(primary) > 12 or len(secondary) > 20:
        raise ValueError(f"wallet-card capacity exceeded: primary={len(primary)}/12, secondary={len(secondary)}/20")

    icons_dir = repo / "icons" / "svg"
    required = primary + secondary
    missing = [icon_id for icon_id in required if not (icons_dir / f"{icon_id}.svg").exists()]
    if missing:
        raise FileNotFoundError(f"missing SVG icons: {', '.join(missing)}")
    backend = _detect_backend("auto")
    out_dir = Path(args.out_dir) if args.out_dir else repo / "layouts" / "wallet-card" / args.profile
    out_dir.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory(prefix="pictiq_wallet_card_") as tmp:
        temp_dir = Path(tmp)
        front = render_side(primary, columns=4, rows=3, vertical_gap_mm=1.2, temp_dir=temp_dir, icons_dir=icons_dir, backend=backend)
        back = render_side(secondary, columns=5, rows=4, vertical_gap_mm=1.0, temp_dir=temp_dir, icons_dir=icons_dir, backend=backend)

    preview = make_preview(front, back)
    front.save(out_dir / "front.png", dpi=(DPI, DPI))
    back.save(out_dir / "back.png", dpi=(DPI, DPI))
    preview.save(out_dir / "preview.png", dpi=(DPI, DPI))
    front.save(out_dir / f"{args.profile}-wallet-card.pdf", "PDF", resolution=DPI, save_all=True, append_images=[back])
    print(f"Renderer backend: {backend}")
    print(f"Front grid: 3 rows x 4 columns ({len(primary)}/12)")
    print(f"Back grid: 4 rows x 5 columns ({len(secondary)}/20)")
    for path in (out_dir / "front.png", out_dir / "back.png", out_dir / "preview.png", out_dir / f"{args.profile}-wallet-card.pdf"):
        print(f"Wrote: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
