#!/usr/bin/env python3
"""Validate vocabulary compatibility and migration metadata."""
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]


def load(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    errors: list[str] = []
    lexicon = load(ROOT / "lexicon" / "icon-index.json")
    icons = lexicon.get("icons", [])
    by_id = {entry.get("id"): entry for entry in icons if isinstance(entry, dict)}
    active_ids = set(by_id)

    src = ROOT / "lexicon" / "compatibility.json"
    docs = ROOT / "docs" / "lexicon" / "compatibility.json"
    if not src.is_file():
        errors.append("missing lexicon/compatibility.json")
        compat = {}
    else:
        compat = load(src)
    if not docs.is_file():
        errors.append("missing docs/lexicon/compatibility.json")
    elif src.is_file() and src.read_text(encoding="utf-8") != docs.read_text(encoding="utf-8"):
        errors.append("docs/lexicon/compatibility.json differs from lexicon/compatibility.json")

    entries = compat.get("entries", compat.get("migrations", [])) if isinstance(compat, dict) else []
    if not isinstance(entries, list):
        errors.append("compatibility entries/migrations must be an array")
        entries = []

    expected = {"need_bar", "place_hotel", "place_fashion_shopping", "move_boat"}
    seen = {entry.get("legacy_id") for entry in entries if isinstance(entry, dict)}
    missing = expected - seen
    if missing:
        errors.append(f"missing compatibility entries: {', '.join(sorted(missing))}")

    for entry in entries:
        if not isinstance(entry, dict):
            errors.append("compatibility entry must be an object")
            continue
        legacy = entry.get("legacy_id")
        status = entry.get("status") or entry.get("kind")
        preferred = entry.get("preferred_id")
        replacement = entry.get("replacement") or entry.get("preferred_composition") or []
        legacy_svg = entry.get("legacy_svg") or (f"legacy/svg/{legacy}.svg" if legacy in {"need_bar", "place_hotel"} else None)

        if status == "SEMANTIC_MIGRATION":
            if legacy in active_ids:
                errors.append(f"{legacy}: semantic migration must not remain an active id")
            if preferred not in active_ids:
                errors.append(f"{legacy}: preferred id missing from active lexicon: {preferred}")
            aliases = by_id.get(preferred, {}).get("aliases_en", []) + by_id.get(preferred, {}).get("aliases", [])
            if legacy not in aliases:
                errors.append(f"{preferred}: missing legacy alias {legacy}")
            if legacy_svg and not (ROOT / legacy_svg).is_file():
                errors.append(f"{legacy}: missing legacy svg {legacy_svg}")

        if status == "DEPRECATED_COMPOSABLE":
            if legacy not in active_ids:
                errors.append(f"{legacy}: deprecated composable id must be retained for compatibility")
            for icon_id in replacement:
                if icon_id not in active_ids:
                    errors.append(f"{legacy}: replacement id missing: {icon_id}")
            for folder in (ROOT / "packs", ROOT / "layouts" / "profiles"):
                for path in sorted(folder.glob("*.json")):
                    text = path.read_text(encoding="utf-8")
                    if f'"{legacy}"' in text:
                        errors.append(f"{legacy}: should not be selected by active set {path.relative_to(ROOT)}")

        if status == "LEGACY_CONTEXTUAL":
            if legacy not in active_ids:
                errors.append(f"{legacy}: legacy contextual id missing from active lexicon")
            if preferred not in active_ids:
                errors.append(f"{legacy}: preferred contextual id missing: {preferred}")
            if not entry.get("final_action_deferred"):
                errors.append(f"{legacy}: final action must remain explicitly deferred")

    if errors:
        for err in errors:
            print(f"ERROR: {err}", file=sys.stderr)
        return 1
    print("OK: compatibility migrations, legacy aliases, and deferred contextual hierarchy are consistent")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
