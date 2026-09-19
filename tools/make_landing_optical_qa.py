#!/usr/bin/env python3
"""Create source-linked HTML QA for imported Pictiq icons without rasterization."""
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'docs/research/landing-translation-v0.1/imported-icon-human-correction-qa.html'
ITEMS = [
 ('Approved source', 'action-combine-approved-source.png', 'Supplied complete reference crop'),
 ('Canonical foreground', 'forensic/action-combine-canonical-foreground.svg', 'Normalized canonical path, no frame'),
 ('Final framed tile', '../../lexicon/svg/action_combine.svg', 'Exact Pages lexicon asset'),
 ('Final landing render', '../../lexicon/svg/action_combine.svg', 'Exact landing img asset at landing scale'),
]
def main():
    cards = []
    for name, path, detail in ITEMS:
        extra = ' landing' if name == 'Final landing render' else ''
        cards.append(f'<section class="card"><div class="label">{name}</div><div class="tile{extra}"><img src="{path}" alt="{name}"></div><div class="detail">{detail}</div></section>')
    OUT.write_text('''<!doctype html><meta charset="utf-8"><title>Pictiq imported icon QA</title><style>
body{margin:0;padding:48px;background:#f7f7f5;color:#101114;font:16px/1.4 system-ui,sans-serif}h1{margin:0 0 8px;font-size:30px}.note{max-width:920px;color:#505866}.grid{display:grid;grid-template-columns:repeat(4,minmax(180px,1fr));gap:18px;margin-top:32px}.card{background:#fff;border:1px solid #d6d9de;border-radius:12px;padding:18px}.tile{aspect-ratio:1;display:grid;place-items:center;margin:12px 0;border:1px solid #e1e3e6;border-radius:8px;background:white}.tile img{width:100%;height:100%;object-fit:contain}.landing{width:96px;height:96px;border:0}.label{font-weight:750}.detail{color:#5c6470;font-size:14px}@media(max-width:800px){.grid{grid-template-columns:1fr 1fr}}</style><main><h1>Imported icon QA — complete silhouette check</h1><p class="note">The four views use direct SVG/PNG assets. This sheet intentionally does not rasterize SVG through ImageMagick: that legacy path omitted the frame stroke and was removed from acceptance evidence.</p><div class="grid">''' + ''.join(cards) + '''</div><p class="note">For the complete A–G diagnostic and pixel-edge record, see <a href="forensic/action-combine-pipeline-forensic.html">pipeline forensic</a>.</p></main>''')
    print(f'OK: wrote {OUT.relative_to(ROOT)}')
if __name__ == '__main__': main()
