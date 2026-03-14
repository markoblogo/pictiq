#!/usr/bin/env python3
"""Generate canonical tile template SVG."""

from __future__ import annotations

from pathlib import Path
import xml.etree.ElementTree as ET


SVG_NS = "http://www.w3.org/2000/svg"
ET.register_namespace("", SVG_NS)


def svg_el(tag: str, **attrs: str) -> ET.Element:
    return ET.Element(f"{{{SVG_NS}}}{tag}", attrs)


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    out_path = root / "templates" / "tile-template.svg"
    out_path.parent.mkdir(parents=True, exist_ok=True)

    svg = svg_el("svg", viewBox="0 0 32 32")

    defs = svg_el("defs")
    clip = svg_el("clipPath", id="icon-clip")
    # Inner frame area for clipping: outer rect inset by half the frame stroke.
    clip_rect = svg_el("rect", x="2", y="2", width="28", height="28", rx="3.8", ry="3.8")
    clip.append(clip_rect)
    defs.append(clip)
    svg.append(defs)

    frame_group = svg_el("g", id="frame")
    frame = svg_el(
        "rect",
        x="1",
        y="1",
        width="30",
        height="30",
        rx="4.8",
        ry="4.8",
        stroke="currentColor",
        **{"stroke-width": "2"},
        fill="none",
    )
    frame_group.append(frame)
    svg.append(frame_group)

    icon_group = svg_el("g", id="icon", **{"clip-path": "url(#icon-clip)"})
    svg.append(icon_group)

    guides = svg_el("g", id="guides", style="display:none")
    safe_rect = svg_el(
        "rect",
        x="4",
        y="4",
        width="24",
        height="24",
        stroke="currentColor",
        **{"stroke-width": "1"},
        fill="none",
    )
    vline = svg_el("line", x1="16", y1="0", x2="16", y2="32", stroke="currentColor", **{"stroke-width": "1"})
    hline = svg_el("line", x1="0", y1="16", x2="32", y2="16", stroke="currentColor", **{"stroke-width": "1"})
    guides.extend([safe_rect, vline, hline])
    svg.append(guides)

    ET.ElementTree(svg).write(out_path, encoding="utf-8", xml_declaration=True)
    print(f"Generated {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
