#!/usr/bin/env python3
"""Render a non-canonical handbook overview of portable Pictiq layouts."""
from pathlib import Path
from PIL import Image
def fit(path, size):
    image=Image.open(path).convert('RGB'); image.thumbnail(size,Image.Resampling.LANCZOS); return image
def main():
    repo=Path(__file__).resolve().parents[1]; sheet=Image.new('RGB',(4200,3000),'white')
    items=[
      (repo/'docs/merch/paris-shirt-preview-1200x1600.png',(380,120),(650,1100)),
      (repo/'layouts/wallet-card/paris/preview.png',(1450,350),(1200,520)),
      (repo/'layouts/wallet-card/nightlife/preview.png',(2850,350),(1200,520)),
      (repo/'layouts/lighter/nightlife/preview.png',(200,1650),(1050,1150)),
      (repo/'layouts/luggage-tag/travel-transit/preview.png',(1650,1650),(700,1150)),
      (repo/'layouts/phone-lockscreen/personal-demo/preview.png',(3050,1500),(700,1350)),
    ]
    for path,point,size in items: sheet.paste(fit(path,size),point)
    out=repo/'layouts/overview/portable-layouts.png'; out.parent.mkdir(parents=True,exist_ok=True); sheet.save(out); print(f'Wrote: {out}')
if __name__=='__main__': main()
