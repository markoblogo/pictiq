#!/usr/bin/env python3
"""Prepare deterministic, self-contained HTML evidence for human visual QA."""
from __future__ import annotations

import argparse
import base64
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def data_uri(data: bytes, mime: str) -> str:
    return f"data:{mime};base64," + base64.b64encode(data).decode('ascii')


def build_sheet(icon_id: str, *, small_px: int = 24,
                neighbors: list[str] | None = None, layout: Path | None = None,
                root: Path = ROOT) -> str:
    """Embed original SVG bytes; isolate each image's IDs and clip paths."""
    if not 1 <= small_px <= 256:
        raise ValueError('small-px must be between 1 and 256 (review setting only)')
    entries = json.loads((root / 'lexicon/icon-index.json').read_text())['icons']
    index = {entry['id']: entry for entry in entries}
    if icon_id not in index:
        raise ValueError(f'Unknown icon ID: {icon_id}')
    if neighbors is None:
        neighbors = sorted((key for key in index if key != icon_id), key=lambda key: (
            index[key]['category'] != index[icon_id]['category'], key))[:8]
    neighbors = list(dict.fromkeys(key for key in neighbors if key != icon_id))
    if not neighbors:
        raise ValueError('Grid requires at least one neighbor')
    images = {}
    for key in [icon_id, *neighbors]:
        if key not in index or Path(key).name != key:
            raise ValueError(f'Unknown or invalid icon ID: {key}')
        images[key] = data_uri((root / 'icons/svg' / f'{key}.svg').read_bytes(), 'image/svg+xml')

    def tile(key: str, size: int) -> str:
        # Generic alt avoids supplying the intended meaning during a blind first pass.
        return f'<img alt="Pictiq tile" width="{size}" height="{size}" src="{images[key]}">'

    grid_ids = neighbors.copy()
    grid_ids.insert(len(grid_ids) // 2, icon_id)
    grid = ''.join(tile(key, 48) for key in grid_ids)
    layout_html = '<p>Not supplied — pending for a known use case; otherwise record a deferral reason.</p>'
    if layout is not None:
        data = layout.read_bytes()
        if data.startswith(b'\x89PNG\r\n\x1a\n'):
            mime = 'image/png'
        elif data.startswith(b'\xff\xd8\xff'):
            mime = 'image/jpeg'
        else:
            raise ValueError('Layout must be a PNG or JPEG render')
        layout_html = (f'<p>{html.escape(layout.name)}</p><img class="layout" '
                       f'alt="Supplied layout for human review" src="{data_uri(data, mime)}">'
                       '<p>Preview is scaled to fit. Verify original at intended size and distance; '
                       'reviewer must confirm the target icon is present.</p>')
    return f'''<!doctype html>
<html lang="en"><meta charset="utf-8"><title>Pictiq visual QA — {html.escape(icon_id)}</title>
<style>
body {{font:16px sans-serif; margin:32px; color:#000; background:#fff; max-width:960px}}
section {{border-top:1px solid #aaa; padding:16px 0}}
img {{object-fit:contain; vertical-align:middle}}
.grid {{display:grid; grid-template-columns:repeat(3,48px); gap:16px}}
.layout {{max-width:100%; height:auto}}
</style>
<h1>Pictiq visual QA evidence</h1>
<p>Human review pending. Generation does not establish structural validity or perceptual acceptance.</p>
<p>Review without labels first. Use 100% browser zoom; CSS pixels are not physical measurements.
Display settings below are review examples, not normative icon geometry.</p>
<section><h2>1 — Canonical render</h2><p>192 CSS px: silhouette, safe area, concept, accidental geometry.</p>
{tile(icon_id, 192)}</section>
<section><h2>2 — Small-size render</h2><p>{small_px} CSS px: negative spaces, merged details, star/blob effects, distinctive features.</p>
{tile(icon_id, small_px)}</section>
<section><h2>3 — Grid render</h2><p>48 CSS px tiles: distinguishability, weight, scale, confusion pairs.
Default neighbors favor the same category; supply likely confusions explicitly.</p>
<div class="grid">{grid}</div></section>
<section><h2>4 — Layout render</h2>{layout_html}</section>
<details><summary>Reveal review metadata after first pass</summary>
<p>Target: {html.escape(icon_id)}. Grid in reading order: {html.escape(', '.join(grid_ids))}.</p></details>
<p>Record source revision, reviewer/date, sizes, viewing conditions, layout/deferral,
observations and pass/fail/pending per stage in the change/PR.</p>
</html>
'''


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('icon_id')
    parser.add_argument('--small-px', type=int, default=24, help='Review size in CSS px (default: 24)')
    parser.add_argument('--neighbors', nargs='+', help='Explicit comparison IDs')
    parser.add_argument('--layout', type=Path, help='Existing PNG/JPEG layout render to embed')
    args = parser.parse_args()
    try:
        sheet = build_sheet(args.icon_id, small_px=args.small_px,
                            neighbors=args.neighbors, layout=args.layout)
    except (ValueError, OSError) as exc:
        parser.error(str(exc))
    output = ROOT / 'build/qa' / f'{args.icon_id}.html'
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(sheet, encoding='utf-8')
    print(output)


if __name__ == '__main__':
    main()
