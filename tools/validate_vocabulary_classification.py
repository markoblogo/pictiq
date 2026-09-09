#!/usr/bin/env python3
"""Validate Pictiq vocabulary role classification against canonical registries."""
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CLASSIFICATION_PATH = ROOT / "lexicon" / "vocabulary-classification.json"
LEXICON_PATH = ROOT / "lexicon" / "icon-index.json"
ENTITY_PATH = ROOT / "entities" / "entity-index.json"

REQUIRED_FIELDS = {
    "id",
    "primary_role",
    "secondary_contexts",
    "embodied_relevance",
    "standalone_relevance",
    "confidence",
}


def load_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text())
    except FileNotFoundError as exc:
        raise SystemExit(f"missing required file: {path.relative_to(ROOT)}") from exc
    except json.JSONDecodeError as exc:
        raise SystemExit(f"invalid JSON in {path.relative_to(ROOT)}: {exc}") from exc


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)


def main() -> None:
    lexicon = load_json(LEXICON_PATH)
    classification = load_json(CLASSIFICATION_PATH)
    entities = load_json(ENTITY_PATH) if ENTITY_PATH.exists() else {"symbols": []}

    canonical_ids = [entry.get("id") for entry in lexicon.get("icons", [])]
    require(all(isinstance(icon_id, str) for icon_id in canonical_ids), "lexicon contains an icon without string id")
    require(len(canonical_ids) == len(set(canonical_ids)), "lexicon contains duplicate ids")

    entity_ids = {entry.get("id") for entry in entities.get("symbols", []) if isinstance(entry.get("id"), str)}

    controlled = classification.get("controlled_values", {})
    allowed_roles = set(controlled.get("primary_role", []))
    allowed_relevance = set(controlled.get("relevance", []))
    allowed_confidence = set(controlled.get("confidence", []))
    allowed_contexts = set(controlled.get("secondary_contexts", []))

    require(allowed_roles, "controlled_values.primary_role must be non-empty")
    require(allowed_relevance, "controlled_values.relevance must be non-empty")
    require(allowed_confidence, "controlled_values.confidence must be non-empty")
    require(allowed_contexts, "controlled_values.secondary_contexts must be non-empty")
    require(classification.get("canonical_lexicon") == "lexicon/icon-index.json", "invalid canonical_lexicon pointer")
    require(classification.get("entity_registry") == "entities/entity-index.json", "invalid entity_registry pointer")
    require(
        classification.get("ordinary_canonical_icon_count") == len(canonical_ids),
        "ordinary_canonical_icon_count must match lexicon icon count",
    )

    entries = classification.get("entries")
    require(isinstance(entries, list), "entries must be a list")
    ids = [entry.get("id") for entry in entries if isinstance(entry, dict)]
    require(len(entries) == len(ids), "each classification entry must be an object with string id")
    require(len(ids) == len(set(ids)), "classification contains duplicate ids")

    missing = sorted(set(canonical_ids) - set(ids))
    extra = sorted(set(ids) - set(canonical_ids))
    entity_overlap = sorted(set(ids) & entity_ids)
    require(not missing, "classification missing canonical ids: " + ", ".join(missing))
    require(not extra, "classification has ids outside ordinary lexicon: " + ", ".join(extra))
    require(not entity_overlap, "entity ids must not be in ordinary classification: " + ", ".join(entity_overlap))

    for entry in entries:
        icon_id = entry["id"]
        missing_fields = sorted(REQUIRED_FIELDS - set(entry))
        require(not missing_fields, f"{icon_id}: missing fields: {', '.join(missing_fields)}")
        require(entry["primary_role"] in allowed_roles, f"{icon_id}: invalid primary_role")
        require(entry["embodied_relevance"] in allowed_relevance, f"{icon_id}: invalid embodied_relevance")
        require(entry["standalone_relevance"] in allowed_relevance, f"{icon_id}: invalid standalone_relevance")
        require(entry["confidence"] in allowed_confidence, f"{icon_id}: invalid confidence")
        contexts = entry["secondary_contexts"]
        require(isinstance(contexts, list) and contexts, f"{icon_id}: secondary_contexts must be a non-empty list")
        require(len(contexts) == len(set(contexts)), f"{icon_id}: duplicate secondary_contexts")
        invalid_contexts = sorted(set(contexts) - allowed_contexts)
        require(not invalid_contexts, f"{icon_id}: invalid secondary_contexts: {', '.join(invalid_contexts)}")

    role_counts = Counter(entry["primary_role"] for entry in entries)
    count_text = ", ".join(f"{role}={role_counts[role]}" for role in sorted(role_counts))
    print(f"OK: validated {len(entries)} ordinary vocabulary classifications ({count_text}); {len(entity_ids)} entity symbols excluded")


if __name__ == "__main__":
    main()
