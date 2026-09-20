#!/usr/bin/env python3
"""Build the text-free 05A PNG from actual current canonical SVG tiles."""
from __future__ import annotations

import json
import subprocess
import tempfile
from pathlib import Path
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
MESSAGE = HERE / '05a-canonical-dialogue.json'
OUT = HERE / '05a-blind-test.png'
TILE, GAP, FRAME_GAP, PAD = 160, 24, 48, 48

message = json.loads(MESSAGE.read_text())
rows = [frame['tokens'] for frame in message['frames']]
width = PAD * 2 + max(len(row) for row in rows) * TILE + (max(len(row) for row in rows) - 1) * GAP
height = PAD * 2 + len(rows) * TILE + (len(rows) - 1) * FRAME_GAP
canvas = Image.new('RGB', (width, height), 'white')

with tempfile.TemporaryDirectory(prefix='pictiq-st05-') as tmp:
    tmp_dir = Path(tmp)
    for frame_i, row in enumerate(rows):
        for token_i, token in enumerate(row):
            if token['type'] != 'icon':
                raise ValueError('05A uses only current ordinary canonical icons')
            source = ROOT / 'icons' / 'svg' / f"{token['id']}.svg"
            rendered_svg = tmp_dir / f"{frame_i}-{token_i}.svg"
            rendered_png = tmp_dir / f"{frame_i}-{token_i}.png"
            rendered_svg.write_text(source.read_text().replace('currentColor', '#000000'))
            subprocess.run(['magick', '-background', 'white', '-density', '192', str(rendered_svg), '-resize', f'{TILE}x{TILE}', str(rendered_png)], check=True)
            tile = Image.open(rendered_png).convert('RGB')
            if token['id'] == 'state_cold':
                # ImageMagick drops SVG strokes; reproduce this source tile's literal line geometry.
                draw = ImageDraw.Draw(tile)
                scale = TILE / 32
                def segment(a, b, width=2.2):
                    a = (round(a[0] * scale), round(a[1] * scale)); b = (round(b[0] * scale), round(b[1] * scale))
                    w = round(width * scale); draw.line((a, b), fill='black', width=w)
                    r = w / 2
                    for px, py in (a, b): draw.ellipse((px-r, py-r, px+r, py+r), fill='black')
                for a, b in [((16,5.5),(16,26.5)), ((6.9,10.8),(25.1,21.2)), ((6.9,21.2),(25.1,10.8)),
                             ((16,9),(13.2,7.2)), ((16,9),(18.8,7.2)), ((16,23),(13.2,24.8)), ((16,23),(18.8,24.8)),
                             ((10,12.6),(9.8,9.3)), ((10,12.6),(7,14.1)), ((22,19.4),(22.2,22.7)), ((22,19.4),(25,17.9)),
                             ((10,19.4),(7,17.9)), ((10,19.4),(9.8,22.7)), ((22,12.6),(25,14.1)), ((22,12.6),(22.2,9.3))]:
                    segment(a, b)
            x = PAD + token_i * (TILE + GAP)
            y = PAD + frame_i * (TILE + FRAME_GAP)
            canvas.paste(tile, (x, y))
            # Exact canonical frame: x/y=1, width/height=30, radius=4.8, stroke=2 on a 32-unit tile.
            inset, radius, stroke = TILE / 32, TILE * 4.8 / 32, TILE * 2 / 32
            ImageDraw.Draw(canvas).rounded_rectangle((x + inset, y + inset, x + TILE - inset, y + TILE - inset), radius=radius, outline='black', width=round(stroke))
canvas.save(OUT, optimize=True)
