#!/usr/bin/env python3
"""
Validate canonical SVG icons in icons/svg/.

Checks for each *.svg (excluding .gitkeep):
- viewBox must be equivalent to 0 0 32 32
- disallow hardcoded colors in fill/stroke attributes and inline styles
  Allowed values: currentColor, none, and empty.
- flag any usage of:
  - hex colors (#...)
  - rgb()/rgba()
  - named colors black/white
"""

from __future__ import annotations

import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path


ALLOWED_PAINT = {"", "none", "currentColor"}


HEX_RE = re.compile(r"#(?:[0-9a-fA-F]{3}|[0-9a-fA-F]{4}|[0-9a-fA-F]{6}|[0-9a-fA-F]{8})\b")
RGB_RE = re.compile(r"\brgba?\s*\(", re.IGNORECASE)
NAMED_RE = re.compile(r"\b(black|white)\b", re.IGNORECASE)


def eprint(msg: str) -> None:
    print(msg, file=sys.stderr)


def parse_viewbox(v: str) -> list[float] | None:
    # viewBox syntax allows commas and/or whitespace separators.
    parts = [p for p in re.split(r"[\s,]+", (v or "").strip()) if p]
    if len(parts) != 4:
        return None
    try:
        return [float(x) for x in parts]
    except ValueError:
        return None


def viewbox_ok(v: str) -> bool:
    nums = parse_viewbox(v)
    if not nums:
        return False
    target = [0.0, 0.0, 32.0, 32.0]
    return all(abs(a - b) < 1e-9 for a, b in zip(nums, target))


def iter_elements(root: ET.Element):
    yield root
    yield from root.iter()


def normalize_paint(v: str | None) -> str:
    return (v or "").strip()


def parse_style(style: str) -> dict[str, str]:
    out: dict[str, str] = {}
    for chunk in (style or "").split(";"):
        if ":" not in chunk:
            continue
        k, val = chunk.split(":", 1)
        k = k.strip().lower()
        val = val.strip()
        if k:
            out[k] = val
    return out


def validate_svg(path: Path) -> list[str]:
    errs: list[str] = []
    try:
        tree = ET.parse(path)
        root = tree.getroot()
    except Exception as exc:  # noqa: BLE001
        return [f"{path}: failed to parse XML: {exc}"]

    vb = root.attrib.get("viewBox")
    if not vb or not viewbox_ok(vb):
        errs.append(f"{path}: invalid viewBox '{vb}', expected equivalent to '0 0 32 32'")

    # Scan for forbidden color patterns in fill/stroke attrs and inline styles.
    for el in iter_elements(root):
        for attr in ("fill", "stroke"):
            if attr in el.attrib:
                val = normalize_paint(el.attrib.get(attr))
                if val not in ALLOWED_PAINT:
                    errs.append(f"{path}: <{el.tag}> {attr}='{val}' is not allowed (use currentColor/none)")
                if HEX_RE.search(val) or RGB_RE.search(val) or NAMED_RE.search(val):
                    errs.append(f"{path}: <{el.tag}> {attr}='{val}' uses a hardcoded color")

        if "style" in el.attrib:
            style = el.attrib.get("style") or ""
            # Fast pattern flags.
            if HEX_RE.search(style) or RGB_RE.search(style) or NAMED_RE.search(style):
                errs.append(f"{path}: <{el.tag}> style contains a hardcoded color")

            kv = parse_style(style)
            for prop in ("fill", "stroke"):
                if prop in kv:
                    val = normalize_paint(kv[prop])
                    if val not in ALLOWED_PAINT:
                        errs.append(f"{path}: <{el.tag}> style {prop}:{val} is not allowed (use currentColor/none)")

    return errs


def main() -> int:
    repo = Path(__file__).resolve().parents[1]
    in_dir = repo / "icons" / "svg"
    svgs = sorted(p for p in in_dir.glob("*.svg") if p.name != ".gitkeep")

    if not svgs:
        print(f"No SVGs found in {in_dir} (skipping).")
        return 0

    all_errs: list[str] = []
    for p in svgs:
        all_errs.extend(validate_svg(p))

    if all_errs:
        for msg in all_errs:
            eprint(f"ERROR: {msg}")
        return 1

    print(f"OK: validated {len(svgs)} SVG(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
