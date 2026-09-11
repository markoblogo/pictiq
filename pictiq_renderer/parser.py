from __future__ import annotations

import re
from pathlib import Path
from typing import Any

from .diagnostics import Diagnostic
from .registry import Registry

PARAM_RE = re.compile(r"^([a-z][a-z0-9]*(?:_[a-z0-9]+)*)\{([^{}]+)\}$")
NUMBER_RE = re.compile(r"^[0-9]+$")
FULL_ENTITY_RE = re.compile(r"^entity:[a-z0-9]+(?:-[a-z0-9]+)*@[a-z0-9]+(?:-[a-z0-9]+)*$")


def parse_shorthand_text(text: str, registry: Registry | None = None) -> tuple[dict[str, Any] | None, list[Diagnostic]]:
    registry = registry or Registry()
    diagnostics: list[Diagnostic] = []
    profile: str | None = None
    contexts: list[str] = []
    frames: list[dict[str, Any]] = []

    for line_no, raw in enumerate(text.replace("\r\n", "\n").replace("\r", "\n").split("\n"), start=1):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        loc = f"line {line_no}"
        if line.startswith("!"):
            parts = line.split()
            if len(parts) != 2 or parts[0] not in {"!profile", "!context"}:
                diagnostics.append(Diagnostic("error", "malformed-directive", f"Malformed directive: {line}", line, None, loc))
                continue
            if parts[0] == "!profile":
                profile = parts[1]
            else:
                if parts[1] not in contexts:
                    contexts.append(parts[1])
            continue
        tokens: list[dict[str, Any]] = []
        for col, unit in enumerate(line.split(), start=1):
            token_loc = f"line {line_no}, token {col}"
            if any(ch in unit for ch in "[]()"):
                diagnostics.append(Diagnostic("error", "illegal-grouping", f"Grouping syntax is not supported in v0.1: {unit}", unit, None, token_loc))
                continue
            if NUMBER_RE.match(unit):
                tokens.append({"type": "number", "value": int(unit)})
                continue
            if FULL_ENTITY_RE.match(unit):
                tokens.append({"type": "entity", "id": unit})
                continue
            if unit.startswith("@"):
                resolved, diags = registry.resolve_entity_alias(unit, contexts, token_loc)
                diagnostics.extend(diags)
                if resolved:
                    tokens.append({"type": "entity", "id": resolved})
                continue
            match = PARAM_RE.match(unit)
            if match:
                icon_id, params_text = match.groups()
                params: dict[str, str] = {}
                for piece in params_text.split(","):
                    if ":" not in piece:
                        diagnostics.append(Diagnostic("error", "unsupported-parameter", f"Malformed parameter: {piece}", piece, None, token_loc))
                        continue
                    key, value = [x.strip() for x in piece.split(":", 1)]
                    params[key] = value
                token: dict[str, Any] = {"type": "icon", "id": icon_id}
                if params:
                    token["params"] = params
                tokens.append(token)
                continue
            tokens.append({"type": "icon", "id": unit})
        if tokens:
            frames.append({"tokens": tokens})
    message: dict[str, Any] = {"schema": "0.1", "pictiq": "1.1", "frames": frames}
    if profile:
        message["profile"] = profile
    if contexts:
        message["contexts"] = contexts
    return (None if any(d.level == "error" for d in diagnostics) else message), diagnostics


def parse_shorthand_file(path: Path, registry: Registry | None = None) -> tuple[dict[str, Any] | None, list[Diagnostic]]:
    return parse_shorthand_text(path.read_text(encoding="utf-8"), registry)
