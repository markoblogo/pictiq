#!/usr/bin/env python3
"""Validate the Pictiq numeric notation registry and SVG assets."""
from __future__ import annotations

import json
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "notation" / "numeric" / "index.json"
ALLOWED_PAINT = {"", "none", "currentColor"}
HEX_RE = re.compile(r"#(?:[0-9a-fA-F]{3}|[0-9a-fA-F]{4}|[0-9a-fA-F]{6}|[0-9a-fA-F]{8})\b")
RGB_RE = re.compile(r"\brgba?\s*\(", re.IGNORECASE)
NAMED_RE = re.compile(r"\b(black|white)\b", re.IGNORECASE)


def fail(message: str) -> None:
    raise SystemExit(message)


def load_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text())
    except Exception as exc:  # noqa: BLE001
        fail(f"{path.relative_to(ROOT)}: failed to parse JSON: {exc}")


def viewbox_ok(value: str | None) -> bool:
    if not value:
        return False
    parts = [p for p in re.split(r"[\s,]+", value.strip()) if p]
    if len(parts) != 4:
        return False
    try:
        nums = [float(p) for p in parts]
    except ValueError:
        return False
    return nums == [0.0, 0.0, 32.0, 32.0]


def validate_svg(path: Path, framed: bool) -> list[str]:
    errs: list[str] = []
    if not path.is_file() or path.stat().st_size == 0:
        return [f"{path.relative_to(ROOT)}: missing or empty SVG"]
    raw = path.read_text(encoding="utf-8", errors="replace")
    if re.search(r"<\s*(?:[a-zA-Z0-9._-]+:)?text\b", raw, flags=re.IGNORECASE):
        errs.append(f"{path.relative_to(ROOT)}: numeric notation SVG must not use <text>")
    if HEX_RE.search(raw) or RGB_RE.search(raw) or NAMED_RE.search(raw):
        errs.append(f"{path.relative_to(ROOT)}: hardcoded colors are not allowed")
    try:
        root = ET.parse(path).getroot()
    except Exception as exc:  # noqa: BLE001
        return [f"{path.relative_to(ROOT)}: invalid SVG XML: {exc}"]
    if not viewbox_ok(root.attrib.get("viewBox")):
        errs.append(f"{path.relative_to(ROOT)}: expected viewBox 0 0 32 32")
    has_frame = False
    for el in root.iter():
        local = el.tag.split("}", 1)[-1]
        if local == "rect" and el.attrib.get("x") == "1" and el.attrib.get("y") == "1":
            has_frame = True
        for attr in ("fill", "stroke"):
            if attr in el.attrib and (el.attrib.get(attr) or "").strip() not in ALLOWED_PAINT:
                errs.append(f"{path.relative_to(ROOT)}: {attr} must use currentColor/none")
    if framed and not has_frame:
        errs.append(f"{path.relative_to(ROOT)}: framed numeric rendering must include canonical tile frame")
    return errs


def main() -> int:
    registry = load_json(REGISTRY)
    digits = registry.get("implemented_digits", [])
    numbers = registry.get("implemented_numbers", [])
    if not isinstance(digits, list) or not digits:
        fail("implemented_digits must be a non-empty list")
    if not isinstance(numbers, list) or not numbers:
        fail("implemented_numbers must be a non-empty list")
    errs: list[str] = []
    seen_digits: set[str] = set()
    for entry in digits:
        digit = entry.get("digit")
        if digit not in set("0123456789"):
            errs.append(f"invalid digit entry: {digit}")
            continue
        if digit in seen_digits:
            errs.append(f"duplicate digit entry: {digit}")
        seen_digits.add(digit)
        svg = ROOT / entry.get("svg", "")
        source = ROOT / entry.get("source_crop", "")
        if not source.is_file():
            errs.append(f"missing source crop for digit {digit}: {source.relative_to(ROOT)}")
        errs.extend(validate_svg(svg, framed=False))
    for entry in numbers:
        value = entry.get("value")
        if not isinstance(value, str) or not value.isdigit():
            errs.append(f"invalid number value: {value}")
            continue
        composition = entry.get("composition", [])
        expected = [f"digit_{d}" for d in value]
        if composition != expected:
            errs.append(f"number {value}: composition {composition} must match {expected}")
        missing = [d for d in value if d not in seen_digits]
        if missing:
            errs.append(f"number {value}: missing implemented digit assets: {', '.join(missing)}")
        source_ref = ROOT / entry.get("source_reference", "")
        if not source_ref.is_file():
            errs.append(f"number {value}: missing source reference")
        errs.extend(validate_svg(ROOT / entry.get("svg", ""), framed=True))
    if errs:
        for err in errs:
            print(f"ERROR: {err}", file=sys.stderr)
        return 1
    print(f"OK: validated numeric notation ({len(digits)} digit assets, {len(numbers)} number rendering(s))")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
