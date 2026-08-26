#!/usr/bin/env python3
"""Render a luggage-tag communication layout from a content profile."""
from __future__ import annotations
import argparse, json, tempfile
from pathlib import Path
from PIL import Image, ImageDraw
from make_merch_layout import tile_bitmap
from render_png import _detect_backend
from layout_preview import draw_luggage_tag_outline, place_artwork

SIZE=(1800, 2700)
def main() -> int:
    p=argparse.ArgumentParser(); p.add_argument('--profile', required=True); args=p.parse_args()
    repo=Path(__file__).resolve().parents[1]; profile=json.loads((repo/'layouts/profiles'/f'{args.profile}.json').read_text())
    ids=profile['primary'][:8]
    if not 6 <= len(ids) <= 8: raise ValueError('luggage tag needs 6–8 primary icons')
    icons=repo/'icons/svg'; missing=[i for i in ids if not (icons/f'{i}.svg').exists()]
    if missing: raise FileNotFoundError(', '.join(missing))
    out=repo/'layouts/luggage-tag'/args.profile; out.mkdir(parents=True, exist_ok=True); backend=_detect_backend('auto')
    canvas=Image.new('RGB', SIZE, 'white'); d=ImageDraw.Draw(canvas); d.rounded_rectangle((24,24,1775,2675),radius=150,outline='black',width=24); d.ellipse((760,95,1040,375),outline='black',width=24)
    tile=500; gap=70; x0=(SIZE[0]-(2*tile+gap))//2; y0=470
    with tempfile.TemporaryDirectory(prefix='pictiq_tag_') as tmp:
      for n,icon in enumerate(ids):
        image=tile_bitmap(Path(tmp),icons,icon,tile,backend); row,col=divmod(n,2); canvas.paste(image,(x0+col*(tile+gap),y0+row*(tile+gap)))
    canvas.save(out/'artwork.png',dpi=(600,600)); preview=Image.new('RGB',(2200,3000),'white'); printable=draw_luggage_tag_outline(preview,(210,120,1990,2880)); place_artwork(preview,canvas,printable); preview.save(out/'preview.png',dpi=(600,600)); canvas.save(out/f'{args.profile}-luggage-tag.pdf','PDF',resolution=600)
    print(f'Wrote: {out}')
    return 0
if __name__=='__main__': raise SystemExit(main())
