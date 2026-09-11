from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .diagnostics import Diagnostic
from .parser import parse_shorthand_file, parse_shorthand_text
from .registry import Registry
from .svg_renderer import RenderOptions, render_svg
from .validator import normalize_and_validate_message


def normalize_json(data: Any, registry: Registry | None = None) -> tuple[dict[str, Any] | None, list[Diagnostic]]:
    return normalize_and_validate_message(data, registry)


def parse_shorthand(text: str, registry: Registry | None = None) -> tuple[dict[str, Any] | None, list[Diagnostic]]:
    return parse_shorthand_text(text, registry)


def render_message(message: dict[str, Any], registry: Registry | None = None, options: RenderOptions | None = None) -> dict[str, Any]:
    registry = registry or Registry()
    normalized, diagnostics = normalize_json(message, registry)
    if normalized is None:
        return {"message": None, "diagnostics": [d.to_dict() for d in diagnostics], "render": None}
    svg, meta = render_svg(normalized, registry, options)
    return {"message": normalized, "diagnostics": [d.to_dict() for d in diagnostics], "render": {"format": "svg", **meta, "svg": svg}}


def render_file(path: Path, registry: Registry | None = None, options: RenderOptions | None = None) -> dict[str, Any]:
    registry = registry or Registry()
    if path.suffix == ".pictiq":
        parsed, diagnostics = parse_shorthand_file(path, registry)
        if parsed is None:
            return {"message": None, "diagnostics": [d.to_dict() for d in diagnostics], "render": None}
        normalized, more = normalize_json(parsed, registry)
        diagnostics.extend(more)
        if normalized is None:
            return {"message": None, "diagnostics": [d.to_dict() for d in diagnostics], "render": None}
        svg, meta = render_svg(normalized, registry, options)
        return {"message": normalized, "diagnostics": [d.to_dict() for d in diagnostics], "render": {"format": "svg", **meta, "svg": svg}}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        diagnostic = Diagnostic("error", "malformed-json", f"Malformed JSON: {exc.msg}.", location=f"line {exc.lineno}, column {exc.colno}")
        return {"message": None, "diagnostics": [diagnostic.to_dict()], "render": None}
    return render_message(data, registry, options)
