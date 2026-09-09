#!/usr/bin/env python3
"""Validate vocabulary profiles against the single canonical lexicon."""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
data = json.loads((root / "lexicon/icon-index.json").read_text())
ids = {entry["id"] for entry in data["icons"]}
profiles = sorted((root / "profiles").glob("*-core-v*.json"))
if not profiles:
    raise SystemExit("no vocabulary profiles found")
for path in profiles:
    profile = json.loads(path.read_text())
    included = profile.get("included_ids")
    if not isinstance(included, list) or not included or len(included) != len(set(included)):
        raise SystemExit(f"{path}: included_ids must be a non-empty unique list")
    unknown = sorted(set(included) - ids)
    if unknown:
        raise SystemExit(f"{path}: unknown canonical IDs: {', '.join(unknown)}")
    if profile.get("canonical_lexicon") != "lexicon/icon-index.json":
        raise SystemExit(f"{path}: invalid canonical_lexicon")
print(f"OK: validated {len(profiles)} vocabulary profiles against {len(ids)} canonical icons")
