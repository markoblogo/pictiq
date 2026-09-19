#!/usr/bin/env python3
"""Measure canonical visible geometry against the Pictiq fitting standard.

The probe renders icon geometry without the presentation frame at 256 px,
thresholds it, and converts the tight raster bbox back to 32-unit coordinates.
It is intentionally a validator/report, never an icon generator.
"""
from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SAFE = (4.0, 4.0, 28.0, 28.0)
FIT = (5.0, 5.0, 27.0, 27.0)
DEFAULT_IDS = ("action_combine", "action_learn", "action_write")
GEOMETRY_RE = re.compile(r"^(\d+) (\d+) ([+-]?\d+) ([+-]?\d+)$")


def probe(path: Path) -> tuple[float, float, float, float]:
    if shutil.which("magick") is None:
        raise RuntimeError("magick is required for fitting validation")
    raw = path.read_text(encoding="utf-8")
    # Remove only the canonical presentation frame; preserve all approved paths
    # and transforms. ImageMagick does not resolve currentColor, so the probe
    # substitutes black in its temporary copy.
    raw = re.sub(r'<g id="frame">.*?</g>', '', raw, count=1, flags=re.S)
    raw = raw.replace("currentColor", "black")
    with tempfile.TemporaryDirectory(prefix="pictiq-fit-") as td:
        svg = Path(td) / path.name
        svg.write_text(raw, encoding="utf-8")
        cmd = ["magick", "-background", "white", str(svg), "-resize", "256x256!",
               "-alpha", "off", "-threshold", "50%", "-trim", "-format", "%w %h %X %Y\\n", "info:"]
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
    match = GEOMETRY_RE.match(result.stdout.strip().replace("+", ""))
    if not match:
        raise RuntimeError(f"unable to measure visible geometry in {path}")
    w, h, x, y = (float(v) for v in match.groups())
    # Raster probe is 32 viewBox units represented by 256 pixels.
    unit = 256.0 / 32.0
    return x / unit, y / unit, w / unit, h / unit


def validate(icon_id: str) -> tuple[bool, str]:
    path = ROOT / "icons" / "svg" / f"{icon_id}.svg"
    x, y, w, h = probe(path)
    x2, y2 = x + w, y + h
    cx, cy = x + w / 2.0, y + h / 2.0
    dx, dy = cx - 16.0, cy - 16.0
    inside = x >= SAFE[0] and y >= SAFE[1] and x2 <= SAFE[2] and y2 <= SAFE[3]
    # Safe-area containment is a hard gate. Bbox centering is reported for
    # diagnosis only: the final framed render and human review decide optical
    # balance for asymmetric imported artwork.
    ok = inside
    status = "PASS" if ok else "FAIL"
    return ok, (f"{status} {icon_id}: bbox=({x:.2f},{y:.2f},{w:.2f},{h:.2f}) "
                f"bbox_center_delta=({dx:+.2f},{dy:+.2f}) "
                f"edge_clearance=({x:.2f},{y:.2f},{32-x2:.2f},{32-y2:.2f}) "
                f"safe_area=({FIT[0]:.0f},{FIT[1]:.0f})..({FIT[2]:.0f},{FIT[3]:.0f})")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("ids", nargs="*", default=list(DEFAULT_IDS))
    args = parser.parse_args()
    failures = 0
    for icon_id in args.ids:
        try:
            ok, line = validate(icon_id)
        except (OSError, RuntimeError, subprocess.CalledProcessError) as exc:
            print(f"FAIL {icon_id}: {exc}")
            failures += 1
            continue
        print(line)
        failures += not ok
    return int(bool(failures))


if __name__ == "__main__":
    raise SystemExit(main())
