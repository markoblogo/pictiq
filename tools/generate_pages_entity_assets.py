#!/usr/bin/env python3
"""Publish the canonical Entity Symbol registry and assets to GitHub Pages."""
from __future__ import annotations

import json
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "entities"
DESTINATION = ROOT / "docs" / "entities"


def main() -> int:
    registry_path = SOURCE / "entity-index.json"
    registry = json.loads(registry_path.read_text(encoding="utf-8"))
    symbols = registry.get("symbols", [])
    if not isinstance(symbols, list):
        raise SystemExit("entity registry symbols must be a list")

    DESTINATION.mkdir(parents=True, exist_ok=True)
    shutil.copy2(registry_path, DESTINATION / "entity-index.json")
    for symbol in symbols:
        source = ROOT / symbol["icon_path"]
        destination = ROOT / "docs" / symbol["icon_path"]
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)

    print(f"OK: published {len(symbols)} Entity Symbols to docs/entities")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
