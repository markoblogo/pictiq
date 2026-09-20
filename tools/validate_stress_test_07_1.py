#!/usr/bin/env python3
"""Validate the non-participant-facing integrity properties of Stress Test 07.1."""
from __future__ import annotations

import hashlib
import json
import struct
import sys
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
EXPERIMENT = ROOT / "docs/research/stress-test-07-explicit-grammar-vs-context"
PACKAGE = EXPERIMENT / "07.1"
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
ALLOWED_CHUNKS = {b"IHDR", b"IDAT", b"IEND"}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def chunks(path: Path) -> set[bytes]:
    data = path.read_bytes()
    if not data.startswith(PNG_SIGNATURE):
        raise ValueError(f"{path}: not PNG")
    offset, found = len(PNG_SIGNATURE), set()
    while offset < len(data):
        length = struct.unpack(">I", data[offset:offset + 4])[0]
        name = data[offset + 4:offset + 8]
        found.add(name)
        offset += 12 + length
    return found


def validate(records: list[dict], expected_count: int) -> None:
    assert len(records) == expected_count
    names = set()
    for record in records:
        output = PACKAGE / record["delivery_png"]
        source = EXPERIMENT / record["source_svg"]
        assert output.exists() and source.exists()
        assert output.name == record["delivery_filename"]
        assert output.name.startswith(("stimulus-", "transfer-"))
        assert record["delivery_filename"] not in names
        names.add(record["delivery_filename"])
        assert sha256(output) == record["delivery_png_sha256"]
        assert sha256(source) == record["source_svg_sha256"]
        with Image.open(output) as image:
            assert image.size == (1872, 768) and image.mode == "RGBA"
        assert chunks(output) <= ALLOWED_CHUNKS, f"{output}: PNG metadata chunks present: {chunks(output) - ALLOWED_CHUNKS}"


def main() -> int:
    manifest = json.loads((PACKAGE / "delivery-manifest.json").read_text())
    assert manifest["status"] == "PREPARED_NOT_EXECUTED"
    assert manifest["dimensions"] == {"width": 1872, "height": 768}
    validate(manifest["primary"], 6)
    validate(manifest["transfer"], 6)
    for entry in manifest["frozen_inputs"]:
        assert sha256(EXPERIMENT / entry["source"]) == entry["sha256"]
        assert sha256(PACKAGE / entry["delivery"]) == entry["delivery_sha256"]
    guide = manifest["micro_learning_guide"]
    assert sha256(EXPERIMENT / guide["source"]) == guide["source_sha256"]
    assert sha256(PACKAGE / guide["delivery"]) == guide["delivery_sha256"]
    assignments = json.loads((PACKAGE / "rerun-assignments.json").read_text())
    assert len(assignments["panel"]) == 5
    assert all(run["status"] == "UNRUN" for run in assignments["panel"])
    json.loads((PACKAGE / "delivery-log.schema.json").read_text())
    print("OK: Stress Test 07.1 has 6 primary and 6 transfer metadata-free 1872x768 PNGs; hashes and frozen inputs match")
    return 0


if __name__ == "__main__":
    sys.exit(main())
