#!/usr/bin/env python3
"""Validate static SEO and machine-discoverability surfaces for Pictiq Pages."""
from __future__ import annotations
from pathlib import Path
import json
import re
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1] / 'docs'
BASE = 'https://pictiq.abvx.xyz'
IMAGE = f'{BASE}/landing/assets/pictiq-handbook-promo.png'
PAGES = {
    'index.html': (f'{BASE}/', 'Pictiq — A tiny visual language'),
    'composer/index.html': (f'{BASE}/composer/', 'Pictiq Composer v0.1'),
    'lexicon/index.html': (f'{BASE}/lexicon/', 'Pictiq Lexicon'),
    'landing/index.html': (f'{BASE}/', 'Pictiq — A tiny visual language'),
}

def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)

def metadata(name: str, text: str) -> str:
    match = re.search(rf'<meta[^>]+(?:name|property)="{re.escape(name)}"[^>]+content="([^"]+)"', text)
    require(match is not None, f'{name}: missing in {name}')
    return match.group(1)

for path, (canonical, title) in PAGES.items():
    text = (ROOT / path).read_text()
    require(f'<title>{title}</title>' in text, f'{path}: unexpected title')
    require('name="description"' in text, f'{path}: missing description')
    require(f'<link rel="canonical" href="{canonical}" />' in text, f'{path}: wrong canonical')
    require('name="robots" content="index,follow"' in text, f'{path}: missing robots directive')
    require(metadata('og:url', text) == canonical, f'{path}: wrong og:url')
    require(metadata('og:image', text) == IMAGE, f'{path}: wrong og:image')
    require(metadata('twitter:image', text) == IMAGE, f'{path}: wrong twitter:image')
    scripts = re.findall(r'<script type="application/ld\+json">\s*(.*?)\s*</script>', text, flags=re.S)
    require(scripts, f'{path}: missing JSON-LD')
    for script in scripts:
        json.loads(script)

require((ROOT / 'favicon.svg').is_file(), 'missing favicon.svg')
robots = (ROOT / 'robots.txt').read_text()
require(f'Sitemap: {BASE}/sitemap.xml' in robots, 'robots: missing sitemap')
sitemap = ET.parse(ROOT / 'sitemap.xml')
locations = {node.text for node in sitemap.findall('{http://www.sitemaps.org/schemas/sitemap/0.9}url/{http://www.sitemaps.org/schemas/sitemap/0.9}loc')}
expected = {f'{BASE}/', f'{BASE}/composer/', f'{BASE}/lexicon/'}
require(locations == expected, f'sitemap: expected {expected}, got {locations}')
llms = (ROOT / 'llms.txt').read_text()
for url in expected | {f'{BASE}/?mode=pictiq'}:
    require(url in llms, f'llms.txt: missing {url}')
print('OK: canonical metadata, JSON-LD, robots, sitemap, llms.txt, favicon, and Pictiq public routes')
