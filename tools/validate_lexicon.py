#!/usr/bin/env python3
"""
Pictiq lexicon validation.

Checks:
- every pack and content-profile id exists in lexicon/icon-index.json
- all lexicon ids are unique
- declared JSON Schema validates the complete lexicon structure
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


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
    root = root.resolve()
    idx_path = root / "lexicon" / "icon-index.json"
    schema_path = root / "lexicon" / "icon-index.schema.json"
    try:
        from jsonschema.validators import validator_for
    except ImportError as exc:
        return [], [f"{idx_path}: JSON Schema validation unavailable: {exc}; "
                    "install dependencies with python -m pip install -r requirements.txt"]

    try:
        schema = load_json(schema_path)
        validator_class = validator_for(schema, default=None) if isinstance(schema, dict) else None
        if validator_class is None:
            return [], [f"{schema_path}: schema $: missing or unsupported $schema dialect"]
        validator_class.check_schema(schema)
    except Exception as exc:  # Invalid/unreadable schemas must fail closed.
        path = getattr(exc, "json_path", "$")
        message = getattr(exc, "message", str(exc))
        return [], [f"{schema_path}: schema {path}: {message}"]

    try:
        idx = load_json(idx_path)
    except (OSError, RuntimeError) as exc:
        return [], [f"{idx_path}: $: {exc}"]

    try:
        validation_errors = sorted(validator_class(schema).iter_errors(idx),
                                   key=lambda error: tuple(map(str, error.absolute_path)))
    except Exception as exc:  # Includes an unavailable schema reference.
        return [], [f"{schema_path}: JSON Schema validation failed: {exc}"]
    if validation_errors:
        return [], [f"{idx_path}: {error.json_path}: {error.message}"
                    for error in validation_errors]

    # Uniqueness is a project invariant beyond the declared structural schema.
    icons = idx["icons"]
    seen: set[str] = set()
    errs: list[str] = []
    for i, entry in enumerate(icons):
        icon_id = entry["id"]
        if icon_id in seen:
            errs.append(f"{idx_path}: $.icons[{i}].id: duplicate id: {icon_id}")
        seen.add(icon_id)
    return icons, errs


def validate_packs(root: Path, lexicon_ids: set[str]) -> list[str]:
    errs: list[str] = []
    pack_paths = sorted((root / "packs").glob("*.json"))
    if not pack_paths:
        errs.append(f"{root / 'packs'}: no pack JSON files found")
        return errs

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


def validate_i18n(root: Path, lexicon_ids: set[str]) -> list[str]:
    errs: list[str] = []
    i18n_dir = root / "lexicon" / "i18n"

    # Backward compatible: i18n directory is optional.
    if not i18n_dir.is_dir():
        return errs

    for i18n_file in sorted(i18n_dir.glob("*.json")):
        if i18n_file.name == "i18n.schema.json":
            continue

        try:
            data = load_json(i18n_file)
        except FileNotFoundError:
            continue
        except Exception as exc:  # noqa: BLE001
            errs.append(str(exc))
            continue

        if not isinstance(data, dict):
            errs.append(f"{i18n_file}: expected object")
            continue

        strings = data.get("strings", {})
        if strings is None:
            strings = {}
        if not isinstance(strings, dict):
            errs.append(f"{i18n_file}: 'strings' must be an object")
            continue

        for key, value in strings.items():
            if key not in lexicon_ids:
                errs.append(f"i18n file {i18n_file.name} contains unknown id: {key}")
            if not isinstance(value, dict):
                errs.append(f"i18n file {i18n_file.name} has non-object value for id: {key}")

    return errs


def validate_profiles(root: Path, lexicon_ids: set[str]) -> list[str]:
    errs: list[str] = []
    profiles_dir = root / "layouts" / "profiles"
    if not profiles_dir.is_dir():
        return errs

    for path in sorted(profiles_dir.glob("*.json")):
        try:
            profile = load_json(path)
        except Exception as exc:  # noqa: BLE001
            errs.append(str(exc))
            continue
        if not isinstance(profile, dict):
            errs.append(f"{path}: expected object")
            continue
        if not isinstance(profile.get("id"), str) or not profile["id"]:
            errs.append(f"{path}: missing/invalid profile id")
        if not isinstance(profile.get("title"), str) or not profile["title"]:
            errs.append(f"{path}: missing/invalid profile title")
        for group in ("primary", "secondary"):
            values = profile.get(group)
            if not isinstance(values, list) or not all(isinstance(value, str) and value for value in values):
                errs.append(f"{path}: {group} must be an array of non-empty ids")
                continue
            if len(values) != len(set(values)):
                errs.append(f"{path}: duplicate ids in {group}")
            unknown = [value for value in values if value not in lexicon_ids]
            if unknown:
                errs.append(f"{path}: {group} ids missing from lexicon: {', '.join(unknown)}")
            missing_svg = [value for value in values if not (root / 'icons' / 'svg' / f'{value}.svg').exists()]
            if missing_svg:
                errs.append(f"{path}: {group} ids missing SVG: {', '.join(missing_svg)}")

        primary = profile.get("primary", [])
        secondary = profile.get("secondary", [])
        if isinstance(primary, list) and isinstance(secondary, list):
            overlap = sorted(set(primary) & set(secondary))
            if overlap:
                errs.append(f"{path}: ids duplicated between primary and secondary: {', '.join(overlap)}")

        wallet = profile.get("wallet_card", {})
        if wallet is not None and not isinstance(wallet, dict):
            errs.append(f"{path}: wallet_card must be an object")
            continue
        wallet = wallet or {}
        selected: dict[str, list[str]] = {}
        for group, limit in (("primary", 12), ("secondary", 20)):
            excluded = wallet.get(f"exclude_{group}", [])
            if not isinstance(excluded, list) or not all(isinstance(value, str) for value in excluded):
                errs.append(f"{path}: wallet_card.exclude_{group} must be an array of ids")
                continue
            if len(excluded) != len(set(excluded)):
                errs.append(f"{path}: duplicate wallet_card.exclude_{group} ids")
            source = profile.get(group, [])
            unknown_exclusions = [value for value in excluded if value not in source]
            if unknown_exclusions:
                errs.append(f"{path}: wallet_card excludes ids outside {group}: {', '.join(unknown_exclusions)}")
            selected[group] = [value for value in source if value not in set(excluded)]
            if len(selected[group]) > limit:
                errs.append(f"{path}: wallet card {group} capacity exceeded: {len(selected[group])}/{limit}")

        lighter = profile.get("lighter")
        if lighter is not None:
            if not isinstance(lighter, dict):
                errs.append(f"{path}: lighter must be an object")
                continue
            for side in ("side_a", "side_b"):
                icon_ids = lighter.get(side)
                if not isinstance(icon_ids, list) or len(icon_ids) != 3 or not all(isinstance(value, str) for value in icon_ids):
                    errs.append(f"{path}: lighter.{side} must contain exactly 3 icon ids")
                    continue
                unknown = [value for value in icon_ids if value not in lexicon_ids]
                if unknown:
                    errs.append(f"{path}: lighter.{side} ids missing from lexicon: {', '.join(unknown)}")
                missing_svg = [value for value in icon_ids if not (root / 'icons' / 'svg' / f'{value}.svg').exists()]
                if missing_svg:
                    errs.append(f"{path}: lighter.{side} ids missing SVG: {', '.join(missing_svg)}")

    return errs


def main(argv: list[str]) -> int:
    root = Path(__file__).resolve().parents[1]

    entries, lex_errs = validate_lexicon_index(root)
    if lex_errs:
        for msg in lex_errs:
            eprint(f"ERROR: {msg}")
        return 1

    lexicon_ids = {entry["id"] for entry in entries}

    pack_errs = validate_packs(root, lexicon_ids)
    if pack_errs:
        for msg in pack_errs:
            eprint(f"ERROR: {msg}")
        return 1

    i18n_errs = validate_i18n(root, lexicon_ids)
    if i18n_errs:
        for msg in i18n_errs:
            eprint(f"ERROR: {msg}")
        return 1

    profile_errs = validate_profiles(root, lexicon_ids)
    if profile_errs:
        for msg in profile_errs:
            eprint(f"ERROR: {msg}")
        return 1

    print("OK: lexicon, packs, profiles, and i18n validated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
