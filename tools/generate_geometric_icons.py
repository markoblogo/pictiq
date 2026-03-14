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


def icon_group(root: ET.Element) -> ET.Element:
    return next(el for el in root if el.tag.endswith("g") and el.attrib.get("id") == "icon")


def rect(x: float, y: float, w: float, h: float) -> ET.Element:
    return svg_el(
        "rect",
        x=f"{x:.6f}",
        y=f"{y:.6f}",
        width=f"{w:.6f}",
        height=f"{h:.6f}",
        fill="currentColor",
        stroke="none",
    )


def generate_logic_no(out_path: Path) -> None:
    svg = make_tile_root()
    ig = icon_group(svg)
    slash = svg_el("path", d=logic_no_slash_path(), fill="currentColor", stroke="none")
    ig.append(slash)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    ET.ElementTree(svg).write(out_path, encoding="utf-8", xml_declaration=True)


def _line_intersection(
    p1: tuple[float, float],
    p2: tuple[float, float],
    p3: tuple[float, float],
    p4: tuple[float, float],
) -> tuple[float, float] | None:
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    x4, y4 = p4
    den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if abs(den) < 1e-9:
        return None
    px = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / den
    py = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / den
    return (px, py)


def polyline_miter_fill_path(points: list[tuple[float, float]], thickness: float) -> str:
    if len(points) != 3:
        raise ValueError("Expected exactly 3 points for checkmark polyline")

    a, b, c = points
    half = thickness / 2.0

    def norm(vx: float, vy: float) -> tuple[float, float]:
        l = math.hypot(vx, vy)
        return (vx / l, vy / l)

    def left_normal(p0: tuple[float, float], p1: tuple[float, float]) -> tuple[float, float]:
        dx, dy = p1[0] - p0[0], p1[1] - p0[1]
        ux, uy = norm(dx, dy)
        return (-uy, ux)

    n1 = left_normal(a, b)
    n2 = left_normal(b, c)

    a_l = (a[0] + n1[0] * half, a[1] + n1[1] * half)
    a_r = (a[0] - n1[0] * half, a[1] - n1[1] * half)

    # Offset lines for miter join at B.
    l1a = (a[0] + n1[0] * half, a[1] + n1[1] * half)
    l1b = (b[0] + n1[0] * half, b[1] + n1[1] * half)
    l2a = (b[0] + n2[0] * half, b[1] + n2[1] * half)
    l2b = (c[0] + n2[0] * half, c[1] + n2[1] * half)
    r1a = (a[0] - n1[0] * half, a[1] - n1[1] * half)
    r1b = (b[0] - n1[0] * half, b[1] - n1[1] * half)
    r2a = (b[0] - n2[0] * half, b[1] - n2[1] * half)
    r2b = (c[0] - n2[0] * half, c[1] - n2[1] * half)

    m_left = _line_intersection(l1a, l1b, l2a, l2b) or l1b
    m_right = _line_intersection(r1a, r1b, r2a, r2b) or r1b

    c_l = (c[0] + n2[0] * half, c[1] + n2[1] * half)
    c_r = (c[0] - n2[0] * half, c[1] - n2[1] * half)

    outline = [a_l, m_left, c_l, c_r, m_right, a_r]
    d = "M " + " L ".join(f"{x:.6f} {y:.6f}" for x, y in outline) + " Z"
    return d


def generate_logic_yes(out_path: Path) -> None:
    svg = make_tile_root()
    ig = icon_group(svg)
    d = polyline_miter_fill_path([(9.0, 19.0), (15.0, 24.0), (26.0, 10.0)], thickness=4.0)
    ig.append(svg_el("path", d=d, fill="currentColor", stroke="none"))
    out_path.parent.mkdir(parents=True, exist_ok=True)
    ET.ElementTree(svg).write(out_path, encoding="utf-8", xml_declaration=True)


def generate_qty_minus(out_path: Path) -> None:
    svg = make_tile_root()
    ig = icon_group(svg)
    ig.append(rect(10, 14.5, 12, 3))
    out_path.parent.mkdir(parents=True, exist_ok=True)
    ET.ElementTree(svg).write(out_path, encoding="utf-8", xml_declaration=True)


def generate_qty_bars(out_path: Path, count: int) -> None:
    svg = make_tile_root()
    ig = icon_group(svg)
    if count == 1:
        bar_w, gap = 3.0, 0.0
    elif count == 2:
        bar_w, gap = 3.0, 3.0
    else:
        # Keep qty_5 visually similar to existing look.
        bar_w, gap = 2.0, 2.0
    bar_h = 16.0
    total_w = count * bar_w + (count - 1) * gap
    start_x = 16.0 - total_w / 2.0
    y = 8.0
    for i in range(count):
        ig.append(rect(start_x + i * (bar_w + gap), y, bar_w, bar_h))
    out_path.parent.mkdir(parents=True, exist_ok=True)
    ET.ElementTree(svg).write(out_path, encoding="utf-8", xml_declaration=True)


def generate_punct_exclaim(out_path: Path) -> None:
    svg = make_tile_root()
    ig = icon_group(svg)
    ig.append(rect(14, 7, 4, 14))
    ig.append(rect(14, 24, 4, 4))
    out_path.parent.mkdir(parents=True, exist_ok=True)
    ET.ElementTree(svg).write(out_path, encoding="utf-8", xml_declaration=True)


def generate_punct_question(out_path: Path) -> None:
    svg = make_tile_root()
    ig = icon_group(svg)
    # Block-based approximation of a question mark silhouette.
    ig.append(rect(10, 6, 12, 4))   # top cap
    ig.append(rect(18, 10, 4, 6))   # right stem
    ig.append(rect(14, 14, 8, 4))   # mid bridge
    ig.append(rect(14, 18, 4, 4))   # lower connector
    ig.append(rect(14, 24, 4, 4))   # dot
    out_path.parent.mkdir(parents=True, exist_ok=True)
    ET.ElementTree(svg).write(out_path, encoding="utf-8", xml_declaration=True)


def generate_time(out_path: Path) -> None:
    svg = make_tile_root()
    ig = icon_group(svg)
    # Donut ring: outer r=10, inner r=8, evenodd fill.
    ring_d = (
        "M 26 16 "
        "A 10 10 0 1 1 6 16 "
        "A 10 10 0 1 1 26 16 Z "
        "M 24 16 "
        "A 8 8 0 1 0 8 16 "
        "A 8 8 0 1 0 24 16 Z"
    )
    ring = svg_el("path", d=ring_d, fill="currentColor", stroke="none", **{"fill-rule": "evenodd"})
    ig.append(ring)
    # Hands as filled silhouettes, overlap by 1px at center to avoid gaps.
    ig.append(rect(15, 8, 2, 9))   # minute hand (width 2)
    ig.append(rect(15, 14.5, 8, 3))  # hour hand (width 3)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    ET.ElementTree(svg).write(out_path, encoding="utf-8", xml_declaration=True)


def main() -> int:
    available = [
        "logic_yes",
        "logic_no",
        "qty_minus",
        "qty_1",
        "qty_2",
        "qty_5",
        "punct_question",
        "punct_exclaim",
        "time",
    ]
    parser = argparse.ArgumentParser(description="Generate canonical geometric icons")
    parser.add_argument("--only", nargs="+", choices=available, default=available, help="Icon(s) to generate")
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[1]
    for icon_id in args.only:
        out = root / "icons" / "svg" / f"{icon_id}.svg"
        if icon_id == "logic_yes":
            generate_logic_yes(out)
        elif icon_id == "logic_no":
            generate_logic_no(out)
        elif icon_id == "qty_minus":
            generate_qty_minus(out)
        elif icon_id == "qty_1":
            generate_qty_bars(out, 1)
        elif icon_id == "qty_2":
            generate_qty_bars(out, 2)
        elif icon_id == "qty_5":
            generate_qty_bars(out, 5)
        elif icon_id == "punct_question":
            generate_punct_question(out)
        elif icon_id == "punct_exclaim":
            generate_punct_exclaim(out)
        elif icon_id == "time":
            generate_time(out)
        print(f"Generated {out}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
