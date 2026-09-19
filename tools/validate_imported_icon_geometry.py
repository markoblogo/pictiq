#!/usr/bin/env python3
"""Audit rendered imported artwork separately from its tile frame."""
from __future__ import annotations
import re, shutil, subprocess, tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ASSETS = {
    "action_combine": "icons/svg/action_combine.svg",
    "action_learn": "icons/svg/action_learn.svg",
    "action_write": "icons/svg/action_write.svg",
    "github": "entities/svg/github__platform.svg",
    "english": "entities/svg/english__language.svg",
    "pdf": "entities/svg/pdf__format.svg",
    "medium": "entities/svg/medium__platform.svg",
    "substack": "entities/svg/substack__platform.svg",
}
PAGES = {"github": "docs/landing/assets/entity/github__platform.svg", "english": "docs/landing/assets/entity/english__language.svg", "pdf": "docs/landing/assets/entity/pdf__format.svg", "medium": "docs/landing/assets/entity/medium__platform.svg", "substack": "docs/landing/assets/entity/substack__platform.svg"}
RE = re.compile(r"^(\d+) (\d+) ([+-]?\d+) ([+-]?\d+)$")

def bbox(path: Path, unclipped: bool = False):
    raw = path.read_text()
    raw = re.sub(r'<g id="frame">.*?</g>', '', raw, flags=re.S, count=1).replace('currentColor', 'black')
    if unclipped:
        raw = re.sub(r'\sclip-path="url\(#icon-clip\)"', '', raw)
    with tempfile.TemporaryDirectory() as temp:
        probe = Path(temp) / path.name
        probe.write_text(raw)
        out = subprocess.run(['magick', '-background', 'white', f'svg:{probe}', '-resize', '1024x1024!', '-alpha', 'off', '-threshold', '50%', '-trim', '-format', '%w %h %X %Y\\n', 'info:'], capture_output=True, text=True, check=True).stdout.strip().replace('+','')
    m = RE.match(out)
    if not m: raise RuntimeError(f'cannot measure {path}')
    w,h,x,y = (float(v)/32 for v in m.groups())
    return x,y,w,h

def main():
    if not shutil.which('magick'): raise SystemExit('magick required')
    failures=[]
    for name, rel in ASSETS.items():
        src = ROOT / rel
        x,y,w,h = bbox(src)
        ux,uy,uw,uh = bbox(src, True)
        cx,cy=x+w/2,y+h/2
        clipped = any(abs(a-b) > .04 for a,b in zip((x,y,w,h),(ux,uy,uw,uh)))
        ok=not clipped and x>=4 and y>=4 and x+w<=28 and y+h<=28 and abs(cx-16)<=.5 and abs(cy-16)<=.5
        print(f"{'PASS' if ok else 'FAIL'} {name}: foreground=({x:.2f},{y:.2f},{w:.2f},{h:.2f}) center=({cx-16:+.2f},{cy-16:+.2f}) clip={'yes' if clipped else 'no'}")
        if not ok: failures.append(name)
        if name in PAGES and (ROOT / PAGES[name]).read_bytes() != src.read_bytes(): failures.append(f'{name} Pages mirror differs')
    if failures: raise SystemExit('FAIL: ' + ', '.join(failures))
    print('OK: audited rendered foreground geometry and Pages mirrors')
if __name__ == '__main__': main()
