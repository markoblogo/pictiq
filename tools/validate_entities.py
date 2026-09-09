#!/usr/bin/env python3
"""Validate scoped Pictiq entity-symbol registry and SVG assets."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

from validate_svg import validate_svg

ROOT = Path(__file__).resolve().parents[1]
ID_RE = re.compile(r"^entity:[a-z0-9]+(?:-[a-z0-9]+)*@[a-z0-9]+(?:-[a-z0-9]+)*$")


def main() -> int:
    errors: list[str] = []
    registry_path = ROOT / "entities" / "entity-index.json"
    if not registry_path.is_file():
        print("No entity registry found; skipping.")
        return 0

    registry = json.loads(registry_path.read_text(encoding="utf-8"))
    symbols = registry.get("symbols")
    if not isinstance(symbols, list):
        errors.append("entities/entity-index.json: symbols must be a list")
        symbols = []

    lexicon_ids = {
        entry["id"]
        for entry in json.loads((ROOT / "lexicon" / "icon-index.json").read_text(encoding="utf-8"))["icons"]
    }
    seen: set[str] = set()

    required = {"id", "namespace", "display_name", "entity_type", "aliases", "authority", "provenance", "icon_path", "status"}
    for index, symbol in enumerate(symbols):
        loc = f"symbols[{index}]"
        missing = sorted(required - set(symbol))
        if missing:
            errors.append(f"{loc}: missing fields: {', '.join(missing)}")
            continue

        entity_id = symbol["id"]
        if not ID_RE.match(entity_id):
            errors.append(f"{loc}: invalid entity id: {entity_id}")
        if entity_id in seen:
            errors.append(f"{loc}: duplicate entity id: {entity_id}")
        seen.add(entity_id)
        if entity_id in lexicon_ids:
            errors.append(f"{loc}: entity id collides with lexical icon id: {entity_id}")

        namespace = entity_id.rsplit("@", 1)[1]
        if symbol.get("namespace") != namespace:
            errors.append(f"{loc}: namespace does not match id suffix")
        if symbol.get("entity_type") != "person":
            errors.append(f"{loc}: first entity-symbol pilot allows person entities only")
        if not symbol.get("aliases"):
            errors.append(f"{loc}: aliases must not be empty")

        provenance = symbol.get("provenance") or {}
        for key in ("source", "source_crop_path", "visual_source"):
            if not provenance.get(key):
                errors.append(f"{loc}: provenance.{key} is required")
        crop = ROOT / str(provenance.get("source_crop_path", ""))
        if not crop.is_file():
            errors.append(f"{loc}: missing source crop: {provenance.get('source_crop_path')}")

        icon_path = str(symbol["icon_path"])
        if not icon_path.startswith("entities/svg/"):
            errors.append(f"{loc}: icon_path must be under entities/svg/")
        svg_path = ROOT / icon_path
        if not svg_path.is_file():
            errors.append(f"{loc}: missing entity SVG: {icon_path}")
        else:
            errors.extend(validate_svg(svg_path))

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print(f"OK: validated {len(symbols)} entity symbol(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
