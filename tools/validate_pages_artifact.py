#!/usr/bin/env python3
"""Check that the checked-in GitHub Pages artifact has all local runtime assets."""
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1] / "docs"

def require(path: str) -> Path:
    p = ROOT / path
    if p.is_dir():
        p = p / "index.html"
    if not p.is_file() or p.stat().st_size == 0:
        raise SystemExit(f"missing Pages asset: {path}")
    return p

require("index.html")
require("app.js")
require("style.css")
require("landing/index.html")
require("landing/landing.js")
require("landing/style.css")
require("lexicon/index.html")
require("CNAME")
if require("CNAME").read_text().strip() != "pictiq.abvx.xyz":
    raise SystemExit("unexpected Pages custom domain")
require("entities/entity-index.json")
require("composer/index.html")
require("composer/app.mjs")
require("composer/composer-core.mjs")
require("composer/style.css")
require("composer/generated/pictiq-composer-data.mjs")
require("renderer/browser-renderer.mjs")
require("renderer/generated/pictiq-browser-assets.mjs")
compatibility = require("lexicon/compatibility.json")
data = json.loads(require("lexicon/icon-index.json").read_text())
ids = [entry["id"] for entry in data["icons"]]
for icon_id in ids:
    page_icon = require(f"lexicon/svg/{icon_id}.svg")
    canonical_icon = ROOT.parent / "icons" / "svg" / f"{icon_id}.svg"
    if not canonical_icon.is_file() or page_icon.read_bytes() != canonical_icon.read_bytes():
        raise SystemExit(f"stale Pages lexicon SVG: {icon_id}")
entities = json.loads(require("entities/entity-index.json").read_text())
for entity in entities.get("symbols", []):
    page_entity = require(entity["icon_path"])
    canonical_entity = ROOT.parent / entity["icon_path"]
    if not canonical_entity.is_file() or page_entity.read_bytes() != canonical_entity.read_bytes():
        raise SystemExit(f"stale Pages Entity SVG: {entity['id']}")
for lang in ("fr", "es"):
    require(f"lexicon/i18n/{lang}.json")

html = (ROOT / "index.html").read_text()
for ref in re.findall(r'(?:href|src)="([^"]+)"', html):
    if ref.startswith(("http://", "https://", "#")):
        continue
    require(ref.split("?", 1)[0].lstrip("./"))
app = (ROOT / "app.js").read_text()
for ref in ("lexicon/icon-index.json", "entities/entity-index.json", "lexicon/i18n/", "lexicon/svg/"):
    if ref not in app:
        raise SystemExit(f"missing runtime reference: {ref}")
composer = (ROOT / "composer" / "app.mjs").read_text()
for ref in ("../renderer/browser-renderer.mjs", "./composer-core.mjs", "../renderer/generated/pictiq-browser-assets.mjs"):
    if ref not in composer:
        raise SystemExit(f"missing Composer runtime reference: {ref}")
composer_core = (ROOT / "composer" / "composer-core.mjs").read_text()
if "semantic" in composer_core.lower() and "embedding" in composer_core.lower():
    raise SystemExit("Composer core appears to include forbidden AI/semantic-search language")
print(f"OK: Pages artifact contains {len(ids)} icons, {len(entities.get('symbols', []))} Entity Symbols, Composer static app, root landing, /lexicon route, custom-domain configuration, compatibility metadata, i18n en/es/fr, and local app assets")
