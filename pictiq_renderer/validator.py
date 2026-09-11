from __future__ import annotations

import re
from typing import Any

from .diagnostics import Diagnostic
from .registry import Registry

ICON_RE = re.compile(r"^[a-z][a-z0-9]*(?:_[a-z0-9]+)*$")
ENTITY_RE = re.compile(r"^entity:[a-z0-9]+(?:-[a-z0-9]+)*@[a-z0-9]+(?:-[a-z0-9]+)*$")
COLOR_RE = re.compile(r"^#[0-9A-Fa-f]{6}$")
PROFILES = {"embodied", "standalone", "embodied-core-v0.1", "standalone-core-v0.1"}
CONTEXTS = {"universal-core", "universal-v1", "city-paris-v0.1", "road-wayfinding-v0.1", "narrative", "odyssey"}


def normalize_and_validate_message(data: Any, registry: Registry | None = None) -> tuple[dict[str, Any] | None, list[Diagnostic]]:
    registry = registry or Registry()
    diagnostics: list[Diagnostic] = []
    if not isinstance(data, dict):
        return None, [Diagnostic("error", "unknown-id", "Message must be a JSON object.")]
    allowed_doc = {"schema", "pictiq", "profile", "contexts", "frames"}
    for key in data:
        if key not in allowed_doc:
            diagnostics.append(Diagnostic("error", "unknown-id", f"Unexpected document property: {key}", key))
    if data.get("schema") != "0.1":
        diagnostics.append(Diagnostic("error", "unknown-id", "schema must be 0.1", str(data.get("schema"))))
    if data.get("pictiq") != "1.1":
        diagnostics.append(Diagnostic("error", "unknown-id", "pictiq must be 1.1", str(data.get("pictiq"))))

    profile = data.get("profile")
    if profile is not None and profile not in PROFILES:
        diagnostics.append(Diagnostic("error", "profile-mismatch", f"Invalid profile '{profile}'.", str(profile)))
    contexts = data.get("contexts", [])
    if contexts is None:
        contexts = []
    if not isinstance(contexts, list) or any(not isinstance(x, str) for x in contexts):
        diagnostics.append(Diagnostic("error", "context-mismatch", "contexts must be an array of strings."))
        contexts = []
    else:
        for context in contexts:
            if context not in CONTEXTS:
                diagnostics.append(Diagnostic("error", "context-mismatch", f"Invalid context '{context}'.", context))

    frames = data.get("frames")
    if not isinstance(frames, list) or not frames:
        diagnostics.append(Diagnostic("error", "unknown-id", "frames must be a non-empty array."))
        return None, diagnostics

    normalized: dict[str, Any] = {"schema": "0.1", "pictiq": "1.1"}
    if isinstance(profile, str):
        normalized["profile"] = profile
    if contexts:
        normalized["contexts"] = list(dict.fromkeys(contexts))
    normalized_frames: list[dict[str, Any]] = []

    for frame_i, frame in enumerate(frames):
        if not isinstance(frame, dict):
            diagnostics.append(Diagnostic("error", "illegal-grouping", "Frame must be an object.", location=f"frames[{frame_i}]"))
            continue
        for key in frame:
            if key != "tokens":
                diagnostics.append(Diagnostic("error", "illegal-grouping", f"Frame property '{key}' is not allowed in v0.1.", key, None, f"frames[{frame_i}]"))
        tokens = frame.get("tokens")
        if not isinstance(tokens, list) or not tokens:
            diagnostics.append(Diagnostic("error", "unknown-id", "Frame tokens must be a non-empty array.", location=f"frames[{frame_i}].tokens"))
            continue
        out_tokens: list[dict[str, Any]] = []
        for token_i, token in enumerate(tokens):
            loc = f"frames[{frame_i}].tokens[{token_i}]"
            if not isinstance(token, dict):
                diagnostics.append(Diagnostic("error", "illegal-grouping", "Token must be an object; grouping is not supported.", location=loc))
                continue
            token_type = token.get("type")
            if token_type == "icon":
                icon_id = token.get("id")
                if not isinstance(icon_id, str) or not ICON_RE.match(icon_id):
                    diagnostics.append(Diagnostic("error", "unknown-id", "Invalid icon id syntax.", str(icon_id), None, loc))
                    continue
                icon_id, diags = registry.normalize_icon_id(icon_id, loc)
                diagnostics.extend(diags)
                if icon_id not in registry.icon_entries:
                    diagnostics.append(Diagnostic("error", "unknown-id", f"Unknown icon id '{icon_id}'.", icon_id, None, loc))
                    continue
                out: dict[str, Any] = {"type": "icon", "id": icon_id}
                params = token.get("params")
                if params is not None:
                    if not isinstance(params, dict) or not params:
                        diagnostics.append(Diagnostic("error", "unsupported-parameter", "params must be a non-empty object.", location=loc))
                        continue
                    for key, value in params.items():
                        if key != "color" or not isinstance(value, str) or not COLOR_RE.match(value):
                            diagnostics.append(Diagnostic("error", "unsupported-parameter", f"Unsupported or malformed parameter '{key}'.", str(value), None, loc))
                    if any(d.level == "error" and d.location == loc and d.type == "unsupported-parameter" for d in diagnostics):
                        continue
                    out["params"] = {"color": params["color"]}
                out_tokens.append(out)
                if profile in PROFILES and registry.profile_ids(profile) and icon_id not in registry.profile_ids(profile):
                    diagnostics.append(Diagnostic("warning", "profile-mismatch", f"Icon '{icon_id}' is outside declared profile '{profile}'.", icon_id, None, loc))
                pack_contexts = [c for c in contexts if registry.context_ids(c)]
                if pack_contexts and not any(icon_id in registry.context_ids(c) for c in pack_contexts):
                    diagnostics.append(Diagnostic("warning", "context-mismatch", f"Icon '{icon_id}' is outside declared context pack(s).", icon_id, None, loc))
            elif token_type == "entity":
                entity_id = token.get("id")
                if not isinstance(entity_id, str) or not ENTITY_RE.match(entity_id):
                    diagnostics.append(Diagnostic("error", "unknown-id", "Invalid entity id syntax.", str(entity_id), None, loc))
                    continue
                if entity_id not in registry.entity_entries:
                    diagnostics.append(Diagnostic("error", "unknown-id", f"Unknown entity id '{entity_id}'.", entity_id, None, loc))
                    continue
                out_tokens.append({"type": "entity", "id": entity_id})
            elif token_type == "number":
                value = token.get("value")
                if not isinstance(value, int) or value < 0 or value > 9999 or value not in registry.implemented_numbers:
                    diagnostics.append(Diagnostic("error", "invalid-number", f"Unsupported numeric notation value '{value}'.", str(value), None, loc))
                    continue
                out_tokens.append({"type": "number", "value": value})
            else:
                diagnostics.append(Diagnostic("error", "unknown-id", f"Unsupported token type '{token_type}'.", str(token_type), None, loc))
        if out_tokens:
            normalized_frames.append({"tokens": out_tokens})
    normalized["frames"] = normalized_frames
    if any(d.level == "error" for d in diagnostics):
        return None, diagnostics
    return normalized, diagnostics
