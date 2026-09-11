from __future__ import annotations

import html
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .layout import LayoutOptions, layout_message
from .registry import Registry

XML_DECL_RE = re.compile(r"^\s*<\?xml[^>]*>\s*", re.I)
SVG_OPEN_RE = re.compile(r"^\s*<svg\b([^>]*)>", re.I | re.S)
SVG_CLOSE_RE = re.compile(r"</svg>\s*$", re.I | re.S)
VIEWBOX_RE = re.compile(r'viewBox="([^"]+)"')


@dataclass(frozen=True)
class RenderOptions:
    tile_size: int = 64
    token_gap: int = 8
    frame_gap: int = 16
    padding: int = 16
    direction: str = "ltr"

    def layout_options(self) -> LayoutOptions:
        return LayoutOptions(self.tile_size, self.token_gap, self.frame_gap, self.padding, self.direction)


def _prefix_internal_ids(svg_inner: str, prefix: str) -> str:
    id_map: dict[str, str] = {}

    def remember(match: re.Match[str]) -> str:
        quote = match.group(1)
        value = match.group(2)
        new_value = f"{prefix}{value}"
        id_map[value] = new_value
        return f"id={quote}{new_value}{quote}"

    svg_inner = re.sub(r"id=(\"|')([^\"']+)(\"|')", lambda m: remember(m), svg_inner)
    for old, new in id_map.items():
        svg_inner = svg_inner.replace(f"url(#{old})", f"url(#{new})")
        svg_inner = svg_inner.replace(f"href=\"#{old}\"", f"href=\"#{new}\"")
        svg_inner = svg_inner.replace(f"href='#{old}'", f"href='#{new}'")
        svg_inner = svg_inner.replace(f"xlink:href=\"#{old}\"", f"xlink:href=\"#{new}\"")
        svg_inner = svg_inner.replace(f"xlink:href='#{old}'", f"xlink:href='#{new}'")
    return svg_inner


def _nested_svg(path: Path, x: int, y: int, size: int, color: str = "#000000", prefix: str = "") -> str:
    text = path.read_text(encoding="utf-8")
    text = XML_DECL_RE.sub("", text).strip()
    match = SVG_OPEN_RE.match(text)
    if not match:
        raise ValueError(f"not an SVG file: {path}")
    open_tag = match.group(0)
    viewbox = VIEWBOX_RE.search(open_tag)
    viewbox_value = viewbox.group(1) if viewbox else "0 0 32 32"
    inner = SVG_CLOSE_RE.sub("", text[match.end():]).strip()
    inner = _prefix_internal_ids(inner, prefix) if prefix else inner
    return f'<svg x="{x}" y="{y}" width="{size}" height="{size}" viewBox="{html.escape(viewbox_value)}" color="{html.escape(color)}">{inner}</svg>'


def render_svg(message: dict[str, Any], registry: Registry | None = None, options: RenderOptions | None = None) -> tuple[str, dict[str, int]]:
    registry = registry or Registry()
    options = options or RenderOptions()
    layout = layout_message(message, options.layout_options())
    parts = [
        "<?xml version='1.0' encoding='utf-8'?>",
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {layout["width"]} {layout["height"]}" width="{layout["width"]}" height="{layout["height"]}" role="img" aria-label="Pictiq rendered message">',
        '<g id="pictiq-message" fill="none">',
    ]
    for frame_i, frame in enumerate(layout["frames"]):
        parts.append(f'<g class="pictiq-frame" data-frame="{frame_i}">')
        for token_i, item in enumerate(frame["tokens"]):
            token = item["token"]
            color = token.get("params", {}).get("color", "#000000") if token["type"] == "icon" else "#000000"
            if token["type"] == "icon":
                path = registry.icon_path(token["id"])
            elif token["type"] == "entity":
                path = registry.entity_path(token["id"])
            elif token["type"] == "number":
                path = registry.number_path(token["value"])
            else:  # guarded by validator
                raise ValueError(f"unsupported token type: {token['type']}")
            parts.append(f'<g class="pictiq-token" data-type="{html.escape(token["type"])}" data-id="{html.escape(str(token.get("id", token.get("value"))))}">')
            parts.append(_nested_svg(path, item["x"], item["y"], item["width"], color, f"f{frame_i}_t{token_i}_"))
            parts.append('</g>')
        parts.append('</g>')
    parts.append('</g></svg>')
    return "\n".join(parts) + "\n", {"width": layout["width"], "height": layout["height"]}
