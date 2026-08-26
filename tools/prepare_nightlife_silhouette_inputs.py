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
    p=argparse.ArgumentParser(); p.add_argument('--cigarette',type=Path,required=True); p.add_argument('--cannabis',type=Path,required=True); p.add_argument('--condom',type=Path,required=True); p.add_argument('--out-dir',type=Path,required=True); args=p.parse_args()
    prepare(args.cigarette,args.out_dir/'item_cigarette.png',460)
    prepare(args.cannabis,args.out_dir/'item_cannabis.png',460)
    prepare(args.condom,args.out_dir/'item_condom.png',360)
if __name__=='__main__': main()
