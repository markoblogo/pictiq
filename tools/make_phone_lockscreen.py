#!/usr/bin/env python3
"""Render a phone lock-screen communication wallpaper from a content profile."""
from __future__ import annotations
import argparse, json, tempfile
from pathlib import Path
from PIL import Image
from make_merch_layout import tile_bitmap
from render_png import _detect_backend

SIZE=(1440,3200); TOP_SAFE=420; BOTTOM_SAFE=520
def main() -> int:
    p=argparse.ArgumentParser(); p.add_argument('--profile',required=True); args=p.parse_args()
    repo=Path(__file__).resolve().parents[1]; profile=json.loads((repo/'layouts/profiles'/f'{args.profile}.json').read_text())
    ids=profile['primary']+profile['secondary']
    if not 12 <= len(ids) <= 16: raise ValueError('lock screen needs 12–16 icons')
    icons=repo/'icons/svg'; missing=[i for i in ids if not (icons/f'{i}.svg').exists()]
    if missing: raise FileNotFoundError(', '.join(missing))
    out=repo/'layouts/phone-lockscreen'/args.profile; out.mkdir(parents=True,exist_ok=True); backend=_detect_backend('auto')
    image=Image.new('RGB',SIZE,'white'); tile=250; cols=4; rows=4; gap=55; block_h=rows*tile+(rows-1)*gap; x0=(SIZE[0]-(cols*tile+(cols-1)*gap))//2; y0=TOP_SAFE+((SIZE[1]-TOP_SAFE-BOTTOM_SAFE-block_h)//2)
    with tempfile.TemporaryDirectory(prefix='pictiq_phone_') as tmp:
      for n,icon in enumerate(ids):
        tile_image=tile_bitmap(Path(tmp),icons,icon,tile,backend); row,col=divmod(n,cols); image.paste(tile_image,(x0+col*(tile+gap),y0+row*(tile+gap)))
    image.save(out/'wallpaper.png',dpi=(400,400)); image.save(out/'preview.png',dpi=(400,400)); print(f'Wrote: {out}'); return 0
if __name__=='__main__': raise SystemExit(main())
