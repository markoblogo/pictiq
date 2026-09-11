#!/usr/bin/env python3
"""Validate Pictiq Message Format v0.1 fixtures.

This is intentionally small and local: it validates the repository's v0.1
schema shape and registry-aware fixture expectations without implementing a
full shorthand parser or renderer.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "spec" / "pictiq-message.schema.json"
VALID_DIR = ROOT / "examples" / "messages" / "valid"
INVALID_SCHEMA_DIR = ROOT / "examples" / "messages" / "invalid" / "schema"
INVALID_SEMANTIC_DIR = ROOT / "examples" / "messages" / "invalid" / "semantic"

ICON_RE = re.compile(r"^[a-z][a-z0-9]*(?:_[a-z0-9]+)*$")
ENTITY_RE = re.compile(r"^entity:[a-z0-9]+(?:-[a-z0-9]+)*@[a-z0-9]+(?:-[a-z0-9]+)*$")
COLOR_RE = re.compile(r"^#[0-9A-Fa-f]{6}$")
PROFILES = {"embodied", "standalone", "embodied-core-v0.1", "standalone-core-v0.1"}
CONTEXTS = {"universal-core", "universal-v1", "city-paris-v0.1", "road-wayfinding-v0.1", "narrative", "odyssey"}


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001 - CLI validator
        raise AssertionError(f"{path.relative_to(ROOT)}: invalid JSON: {exc}") from exc


def schema_errors(data: Any) -> list[str]:
    errors: list[str] = []
    if not isinstance(data, dict):
        return ["document must be object"]
    allowed_doc = {"schema", "pictiq", "profile", "contexts", "frames"}
    for key in data:
        if key not in allowed_doc:
            errors.append(f"unexpected document property: {key}")
    if data.get("schema") != "0.1":
        errors.append("schema must be 0.1")
    if data.get("pictiq") != "1.1":
        errors.append("pictiq must be 1.1")
    if "profile" in data and data["profile"] not in PROFILES:
        errors.append(f"invalid profile: {data['profile']}")
    if "contexts" in data:
        contexts = data["contexts"]
        if not isinstance(contexts, list):
            errors.append("contexts must be array")
        else:
            if len(contexts) != len(set(contexts)):
                errors.append("contexts must be unique")
            for context in contexts:
                if context not in CONTEXTS:
                    errors.append(f"invalid context: {context}")
    frames = data.get("frames")
    if not isinstance(frames, list) or not frames:
        errors.append("frames must be a non-empty array")
        return errors
    for frame_i, frame in enumerate(frames):
        if not isinstance(frame, dict):
            errors.append(f"frames[{frame_i}] must be object")
            continue
        for key in frame:
            if key != "tokens":
                errors.append(f"frames[{frame_i}] unexpected property: {key}")
        tokens = frame.get("tokens")
        if not isinstance(tokens, list) or not tokens:
            errors.append(f"frames[{frame_i}].tokens must be a non-empty array")
            continue
        for token_i, token in enumerate(tokens):
            loc = f"frames[{frame_i}].tokens[{token_i}]"
            if not isinstance(token, dict):
                errors.append(f"{loc} must be object")
                continue
            t = token.get("type")
            if t == "icon":
                allowed = {"type", "id", "params"}
                for key in token:
                    if key not in allowed:
                        errors.append(f"{loc} unexpected property: {key}")
                if not isinstance(token.get("id"), str) or not ICON_RE.match(token["id"]):
                    errors.append(f"{loc}.id invalid icon id syntax")
                if "params" in token:
                    params = token["params"]
                    if not isinstance(params, dict) or not params:
                        errors.append(f"{loc}.params must be non-empty object")
                    else:
                        for key in params:
                            if key != "color":
                                errors.append(f"{loc}.params unsupported parameter: {key}")
                        if "color" in params and (not isinstance(params["color"], str) or not COLOR_RE.match(params["color"])):
                            errors.append(f"{loc}.params.color malformed")
            elif t == "entity":
                allowed = {"type", "id"}
                for key in token:
                    if key not in allowed:
                        errors.append(f"{loc} unexpected property: {key}")
                if not isinstance(token.get("id"), str) or not ENTITY_RE.match(token["id"]):
                    errors.append(f"{loc}.id invalid entity id syntax")
            elif t == "number":
                allowed = {"type", "value"}
                for key in token:
                    if key not in allowed:
                        errors.append(f"{loc} unexpected property: {key}")
                value = token.get("value")
                if not isinstance(value, int) or value < 0 or value > 9999:
                    errors.append(f"{loc}.value invalid number")
            else:
                errors.append(f"{loc}.type invalid: {t}")
    return errors


def semantic_errors(data: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    icon_ids = {entry["id"] for entry in load_json(ROOT / "lexicon" / "icon-index.json")["icons"]}
    entity_ids = {entry["id"] for entry in load_json(ROOT / "entities" / "entity-index.json")["symbols"]}
    numeric = load_json(ROOT / "notation" / "numeric" / "index.json")
    implemented_numbers = {int(entry["value"]) for entry in numeric.get("implemented_numbers", [])}
    for frame_i, frame in enumerate(data.get("frames", [])):
        for token_i, token in enumerate(frame.get("tokens", [])):
            loc = f"frames[{frame_i}].tokens[{token_i}]"
            if token.get("type") == "icon" and token.get("id") not in icon_ids:
                errors.append(f"{loc}.id unknown icon id: {token.get('id')}")
            if token.get("type") == "entity" and token.get("id") not in entity_ids:
                errors.append(f"{loc}.id unknown entity id: {token.get('id')}")
            if token.get("type") == "number" and token.get("value") not in implemented_numbers:
                errors.append(f"{loc}.value unimplemented numeric notation: {token.get('value')}")
    return errors


def main() -> int:
    load_json(SCHEMA_PATH)
    errors: list[str] = []

    valid_json = sorted(VALID_DIR.glob("*.json"))
    invalid_schema_json = sorted(INVALID_SCHEMA_DIR.glob("*.json"))
    invalid_semantic_json = sorted(INVALID_SEMANTIC_DIR.glob("*.json"))

    if len(valid_json) < 10:
        errors.append("expected at least 10 valid JSON examples")
    if len(invalid_schema_json) < 5:
        errors.append("expected at least 5 schema-invalid JSON examples")

    for path in valid_json:
        data = load_json(path)
        serrs = schema_errors(data)
        if serrs:
            errors.append(f"{path.relative_to(ROOT)} should be schema-valid: {serrs}")
            continue
        semerrs = semantic_errors(data)
        if semerrs:
            errors.append(f"{path.relative_to(ROOT)} should be semantically valid against current registries: {semerrs}")

    for path in invalid_schema_json:
        data = load_json(path)
        serrs = schema_errors(data)
        if not serrs:
            errors.append(f"{path.relative_to(ROOT)} should fail schema validation")

    for path in invalid_semantic_json:
        data = load_json(path)
        serrs = schema_errors(data)
        if serrs:
            errors.append(f"{path.relative_to(ROOT)} should be schema-valid but semantically invalid: {serrs}")
            continue
        semerrs = semantic_errors(data)
        if not semerrs:
            errors.append(f"{path.relative_to(ROOT)} should fail registry-aware semantic validation")

    if errors:
        for err in errors:
            print(f"ERROR: {err}", file=sys.stderr)
        return 1
    shorthand = len(list(VALID_DIR.glob("*.pictiq"))) + len(list(INVALID_SEMANTIC_DIR.glob("*.pictiq")))
    print(f"OK: validated Pictiq Message schema fixtures ({len(valid_json)} valid, {len(invalid_schema_json)} schema-invalid, {len(invalid_semantic_json)} semantic-invalid JSON; {shorthand} shorthand fixtures documented)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
