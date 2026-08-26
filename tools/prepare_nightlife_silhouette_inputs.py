#!/usr/bin/env python3
"""Normalize supplied Nightlife references to reviewable 512px silhouettes."""
from __future__ import annotations
import argparse
from pathlib import Path
from PIL import Image

def prepare(source: Path, output: Path, max_size: int):
    image=Image.open(source).convert('L'); image.thumbnail((max_size,max_size),Image.Resampling.LANCZOS)
    canvas=Image.new('L',(512,512),255); canvas.paste(image,((512-image.width)//2,(512-image.height)//2)); output.parent.mkdir(parents=True,exist_ok=True); canvas.save(output)

def main():
    p=argparse.ArgumentParser()
    for name in ('cigarette','cannabis','condom','bar','beer'): p.add_argument(f'--{name}',type=Path)
    p.add_argument('--out-dir',type=Path,required=True); args=p.parse_args()
    jobs=((args.cigarette,'item_cigarette.png',460),(args.cannabis,'item_cannabis.png',460),(args.condom,'item_condom.png',360),(args.bar,'need_bar.png',460),(args.beer,'drink_beer.png',460))
    for source,name,size in jobs:
        if source: prepare(source,args.out_dir/name,size)
if __name__=='__main__': main()
