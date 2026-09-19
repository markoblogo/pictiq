#!/usr/bin/env python3
"""Generate a rendered-size comparison sheet for landing icon optical review."""
from __future__ import annotations
import base64
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'docs/research/landing-translation-v0.1/optical-fit-qa.svg'
AUDITED=[('action_combine','icons/svg/action_combine.svg'),('action_learn','icons/svg/action_learn.svg'),('action_write','icons/svg/action_write.svg'),('github','entities/svg/github__platform.svg'),('english','entities/svg/english__language.svg'),('pdf','entities/svg/pdf__format.svg'),('medium','entities/svg/medium__platform.svg'),('substack','entities/svg/substack__platform.svg'),('Pictiq glyph','docs/landing/assets/pictiq-logo.svg')]
REFERENCES=[('question','icons/svg/punct_question.svg'),('water','icons/svg/need_water.svg'),('speak','icons/svg/comm_speak.svg'),('yes','icons/svg/logic_yes.svg')]
def uri(rel): return 'data:image/svg+xml;base64,'+base64.b64encode((ROOT/rel).read_bytes()).decode()
def main():
 p=['<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="980" viewBox="0 0 1200 980"><rect width="100%" height="100%" fill="white"/>','<style>text{font-family:Arial,sans-serif;fill:#101114}.small{font-size:13px;fill:#5f6670}.head{font-size:28px;font-weight:700}</style>','<text x="40" y="50" class="head">Pictiq Landing optical-fit QA</text><text x="40" y="76" class="small">Foreground compared at landing hierarchy sizes; references remain unchanged.</text>']
 p.append('<text x="400" y="114" class="small">primary 96 px</text><text x="580" y="114" class="small">secondary 64 px</text><text x="720" y="114" class="small">navigation 40 px</text><text x="910" y="114" class="small">reference set 40 px</text>')
 for i,(name,rel) in enumerate(AUDITED):
  y=150+i*88; p.append(f'<text x="40" y="{y+38}" font-size="16">{name}</text>')
  for x,size in ((410,96),(600,64),(740,40)):
   p.append(f'<image x="{x}" y="{y+(96-size)/2}" width="{size}" height="{size}" href="{uri(rel)}"/>')
  for j,(_,ref) in enumerate(REFERENCES): p.append(f'<image x="{900+j*56}" y="{y+24}" width="40" height="40" href="{uri(ref)}"/>')
  p.append(f'<line x1="40" y1="{y+82}" x2="1160" y2="{y+82}" stroke="#d7dce2"/>')
 p.append('</svg>'); OUT.write_text(''.join(p)); print(f'OK: wrote {OUT.relative_to(ROOT)}')
if __name__=='__main__': main()
