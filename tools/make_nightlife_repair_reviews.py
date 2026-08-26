#!/usr/bin/env python3
"""Build visual QA sheets for supplied Nightlife icon and lighter references."""
from __future__ import annotations
import argparse, tempfile
from pathlib import Path
from PIL import Image
from make_merch_layout import tile_bitmap
from render_png import _detect_backend

def fit(path: Path, size: tuple[int,int]) -> Image.Image:
    image=Image.open(path).convert('RGB'); image.thumbnail(size,Image.Resampling.LANCZOS); return image

def paste_center(sheet: Image.Image, image: Image.Image, box: tuple[int,int,int,int]):
    x=box[0]+(box[2]-box[0]-image.width)//2; y=box[1]+(box[3]-box[1]-image.height)//2; sheet.paste(image,(x,y))

def main():
    p=argparse.ArgumentParser(); p.add_argument('--cigarette',type=Path,required=True); p.add_argument('--cannabis',type=Path,required=True); p.add_argument('--condom',type=Path,required=True); p.add_argument('--bar',type=Path); p.add_argument('--beer',type=Path); p.add_argument('--lighter',type=Path,required=True); args=p.parse_args()
    repo=Path(__file__).resolve().parents[1]; out=repo/'layouts/overview'; out.mkdir(parents=True,exist_ok=True); backend=_detect_backend('auto')
    refs={'item_cigarette':args.cigarette,'item_cannabis':args.cannabis,'item_condom':args.condom}
    if args.bar: refs['need_bar']=args.bar
    if args.beer: refs['drink_beer']=args.beer
    review=Image.new('RGB',(2400,600*len(refs)),'white')
    with tempfile.TemporaryDirectory(prefix='pictiq_repair_review_') as tmp:
        for row,(icon_id,reference) in enumerate(refs.items()):
            input_path=(repo/'inputs/silhouettes'/f'{icon_id}.png') if icon_id=='need_bar' else (repo/'inputs/silhouettes/reusable'/f'{icon_id}.png')
            images=[fit(reference,(500,500)),fit(input_path,(500,500)),tile_bitmap(Path(tmp),repo/'icons/svg',icon_id,500,backend)]
            for col,image in enumerate(images): paste_center(review,image,(col*800,row*600,(col+1)*800,(row+1)*600))
    review.save(out/'nightlife-icon-repair-review.png')
    lighter=Image.new('RGB',(4000,1800),'white'); paths=[args.lighter,repo/'layouts/lighter/nightlife/preview.png',repo/'layouts/lighter/nightlife/side-a.png',repo/'layouts/lighter/nightlife/side-b.png']
    for col,path in enumerate(paths): paste_center(lighter,fit(path,(900,1650)),(col*1000,0,(col+1)*1000,1800))
    lighter.save(out/'nightlife-lighter-review.png')
    print(f"Wrote: {out/'nightlife-icon-repair-review.png'}")
    print(f"Wrote: {out/'nightlife-lighter-review.png'}")
if __name__=='__main__': main()
