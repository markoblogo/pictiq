#!/usr/bin/env python3
"""Check that the checked-in GitHub Pages artifact has all local runtime assets."""
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1] / "docs"

def require(path: str) -> Path:
    p = ROOT / path
    if not p.is_file() or p.stat().st_size == 0:
        raise SystemExit(f"missing Pages asset: {path}")
    return p

require("index.html")
require("app.js")
require("style.css")
compatibility = require("lexicon/compatibility.json")
data = json.loads(require("lexicon/icon-index.json").read_text())
ids = [entry["id"] for entry in data["icons"]]
for icon_id in ids:
    require(f"lexicon/svg/{icon_id}.svg")
for lang in ("fr", "es"):
    require(f"lexicon/i18n/{lang}.json")

html = (ROOT / "index.html").read_text()
for ref in re.findall(r'(?:href|src)="([^"]+)"', html):
    if ref.startswith(("http://", "https://", "#")):
        continue
    require(ref.split("?", 1)[0].lstrip("./"))
app = (ROOT / "app.js").read_text()
for ref in ("./lexicon/icon-index.json", "./lexicon/i18n/", "./lexicon/svg/" ):
    if ref not in app:
        raise SystemExit(f"missing runtime reference: {ref}")
print(f"OK: Pages artifact contains {len(ids)} icons, compatibility metadata, i18n en/es/fr, and local app assets")
