#!/usr/bin/env python3
"""
Pictiq lexicon validation.

Checks:
- every id in packs/universal-core.json and packs/universal-v1.json exists in lexicon/icon-index.json
- all lexicon ids are unique
- required fields exist and type is valid
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


REQUIRED_FIELDS = ("id", "type", "category", "meaning_en", "aliases_en", "tags_en", "examples")
VALID_TYPES = {"icon", "operator"}


def eprint(msg: str) -> None:
    print(msg, file=sys.stderr)


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise
    except Exception as exc:  # noqa: BLE001 - keep CLI output simple
        raise RuntimeError(f"failed to parse JSON: {path}: {exc}") from exc


def validate_lexicon_index(root: Path) -> tuple[list[dict[str, Any]], list[str]]:
    idx_path = root / "lexicon" / "icon-index.json"
    idx = load_json(idx_path)

    errs: list[str] = []
    if not isinstance(idx, dict):
        return [], [f"{idx_path}: expected object"]

    icons = idx.get("icons")
    if not isinstance(icons, list):
        return [], [f"{idx_path}: missing/invalid 'icons' array"]

    seen: set[str] = set()
    out: list[dict[str, Any]] = []
    for i, entry in enumerate(icons):
        if not isinstance(entry, dict):
            errs.append(f"{idx_path}: icons[{i}]: expected object")
            continue

        missing = [k for k in REQUIRED_FIELDS if k not in entry]
        if missing:
            errs.append(f"{idx_path}: icons[{i}]: missing required fields: {', '.join(missing)}")
            continue

        _id = entry.get("id")
        if not isinstance(_id, str) or not _id:
            errs.append(f"{idx_path}: icons[{i}].id: expected non-empty string")
            continue

        if _id in seen:
            errs.append(f"{idx_path}: duplicate id: {_id}")
        else:
            seen.add(_id)

        _type = entry.get("type")
        if _type not in VALID_TYPES:
            errs.append(f"{idx_path}: {_id}: invalid type '{_type}', expected one of: {', '.join(sorted(VALID_TYPES))}")

        # Basic type checks for required fields (kept minimal, per requirements)
        if not isinstance(entry.get("category"), str):
            errs.append(f"{idx_path}: {_id}.category: expected string")
        if not isinstance(entry.get("meaning_en"), str):
            errs.append(f"{idx_path}: {_id}.meaning_en: expected string")
        if not isinstance(entry.get("aliases_en"), list):
            errs.append(f"{idx_path}: {_id}.aliases_en: expected array")
        if not isinstance(entry.get("tags_en"), list):
            errs.append(f"{idx_path}: {_id}.tags_en: expected array")
        if not isinstance(entry.get("examples"), list):
            errs.append(f"{idx_path}: {_id}.examples: expected array")

        out.append(entry)

    return out, errs


def validate_packs(root: Path, lexicon_ids: set[str]) -> list[str]:
    errs: list[str] = []
    pack_paths = [
        root / "packs" / "universal-core.json",
        root / "packs" / "universal-v1.json",
    ]

    for pack_path in pack_paths:
        try:
            pack = load_json(pack_path)
        except FileNotFoundError:
            errs.append(f"{pack_path}: missing file")
            continue
        except Exception as exc:  # noqa: BLE001
            errs.append(str(exc))
            continue

        if not isinstance(pack, dict):
            errs.append(f"{pack_path}: expected object")
            continue

        icons = pack.get("icons")
        if not isinstance(icons, list):
            errs.append(f"{pack_path}: missing/invalid 'icons' array")
            continue

        missing = [i for i in icons if i not in lexicon_ids]
        if missing:
            errs.append(f"{pack_path}: ids missing from lexicon: {', '.join(missing)}")

    return errs


def main(argv: list[str]) -> int:
    root = Path(__file__).resolve().parents[1]

    _, lex_errs = validate_lexicon_index(root)
    if lex_errs:
        for msg in lex_errs:
            eprint(f"ERROR: {msg}")
        return 1

    idx = load_json(root / "lexicon" / "icon-index.json")
    lexicon_ids = {e["id"] for e in idx["icons"] if isinstance(e, dict) and isinstance(e.get("id"), str)}

    pack_errs = validate_packs(root, lexicon_ids)
    if pack_errs:
        for msg in pack_errs:
            eprint(f"ERROR: {msg}")
        return 1

    print("OK: lexicon and packs validated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

