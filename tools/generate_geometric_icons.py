#!/usr/bin/env python3
"""Generate canonical geometric icons that should not use silhouette tracing."""

from __future__ import annotations

import argparse
import math
import xml.etree.ElementTree as ET
from pathlib import Path


SVG_NS = "http://www.w3.org/2000/svg"
ET.register_namespace("", SVG_NS)


def svg_el(tag: str, **attrs: str) -> ET.Element:
    return ET.Element(f"{{{SVG_NS}}}{tag}", attrs)


def logic_no_slash_path() -> str:
    # Center line from top-right to bottom-left.
    x1, y1 = 31.0, 1.0
    x2, y2 = 1.0, 31.0
    thickness = 5.0

    dx = x2 - x1
    dy = y2 - y1
    length = math.hypot(dx, dy)
    nx = -dy / length
    ny = dx / length
    ox = nx * (thickness / 2.0)
    oy = ny * (thickness / 2.0)

    p1 = (x1 + ox, y1 + oy)
    p2 = (x2 + ox, y2 + oy)
    p3 = (x2 - ox, y2 - oy)
    p4 = (x1 - ox, y1 - oy)

    return (
        f"M {p1[0]:.6f} {p1[1]:.6f} "
        f"L {p2[0]:.6f} {p2[1]:.6f} "
        f"L {p3[0]:.6f} {p3[1]:.6f} "
        f"L {p4[0]:.6f} {p4[1]:.6f} Z"
    )


def make_tile_root() -> ET.Element:
    root = svg_el("svg", viewBox="0 0 32 32")

    defs = svg_el("defs")
    clip = svg_el("clipPath", id="icon-clip")
    clip.append(svg_el("rect", x="2", y="2", width="28", height="28", rx="3.8", ry="3.8"))
    defs.append(clip)
    root.append(defs)

    frame_group = svg_el("g", id="frame")
    frame_group.append(
        svg_el(
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
    )
    root.append(frame_group)

    root.append(svg_el("g", id="icon", **{"clip-path": "url(#icon-clip)"}))
    return root


def generate_logic_no(out_path: Path) -> None:
    svg = make_tile_root()
    icon_group = next(el for el in svg if el.tag.endswith("g") and el.attrib.get("id") == "icon")
    slash = svg_el("path", d=logic_no_slash_path(), fill="currentColor", stroke="none")
    icon_group.append(slash)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    ET.ElementTree(svg).write(out_path, encoding="utf-8", xml_declaration=True)


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate canonical geometric icons")
    parser.add_argument("--only", choices=["logic_no"], default="logic_no", help="Icon to generate")
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[1]
    if args.only == "logic_no":
        out = root / "icons" / "svg" / "logic_no.svg"
        generate_logic_no(out)
        print(f"Generated {out}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
