#!/usr/bin/env python3
"""Render a two-sided Pictiq wallet card from a content profile."""

from __future__ import annotations

import argparse
import json
import tempfile
from pathlib import Path

from PIL import Image

from make_merch_layout import tile_bitmap
from render_png import _detect_backend


DPI = 300
CARD_MM = (85.60, 53.98)
CARD_SIZE = tuple(round(mm / 25.4 * DPI) for mm in CARD_MM)
PREVIEW_GAP = 120
PREVIEW_MARGIN = 80


def select_group(profile: dict, group: str) -> list[str]:
    exclusions = set(profile.get("wallet_card", {}).get(f"exclude_{group}", []))
    return [icon_id for icon_id in profile[group] if icon_id not in exclusions]


def render_side(
    icon_ids: list[str],
    columns: int,
    rows: int,
    tile_size: int,
    gap: int,
    temp_dir: Path,
    icons_dir: Path,
    backend: str,
) -> Image.Image:
    if len(icon_ids) > columns * rows:
        raise ValueError(f"{len(icon_ids)} icons exceed {columns}x{rows} capacity")

    canvas = Image.new("RGB", CARD_SIZE, "white")
    width = columns * tile_size + (columns - 1) * gap
    height = rows * tile_size + (rows - 1) * gap
    x0 = (canvas.width - width) // 2
    y0 = (canvas.height - height) // 2

    for index, icon_id in enumerate(icon_ids):
        row, col = divmod(index, columns)
        tile = tile_bitmap(temp_dir, icons_dir, icon_id, tile_size, backend)
        canvas.paste(tile, (x0 + col * (tile_size + gap), y0 + row * (tile_size + gap)))
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
        front = render_side(primary, columns=3, rows=4, tile_size=122, gap=22, temp_dir=temp_dir, icons_dir=icons_dir, backend=backend)
        back = render_side(secondary, columns=4, rows=5, tile_size=98, gap=10, temp_dir=temp_dir, icons_dir=icons_dir, backend=backend)

    preview = make_preview(front, back)
    front.save(out_dir / "front.png", dpi=(DPI, DPI))
    back.save(out_dir / "back.png", dpi=(DPI, DPI))
    preview.save(out_dir / "preview.png", dpi=(DPI, DPI))
    front.save(out_dir / f"{args.profile}-wallet-card.pdf", "PDF", resolution=DPI, save_all=True, append_images=[back])
    print(f"Renderer backend: {backend}")
    print(f"Primary: {len(primary)}/12")
    print(f"Secondary: {len(secondary)}/20")
    for path in (out_dir / "front.png", out_dir / "back.png", out_dir / "preview.png", out_dir / f"{args.profile}-wallet-card.pdf"):
        print(f"Wrote: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
