#!/usr/bin/env python3
"""Small CLI for Pictiq Renderer v0.1."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from pictiq_renderer import RenderOptions, render_file  # noqa: E402


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Render or normalize Pictiq Message v0.1 input.")
    sub = parser.add_subparsers(dest="command", required=True)
    for name in ("render", "normalize"):
        p = sub.add_parser(name)
        p.add_argument("input", type=Path)
        p.add_argument("--output", type=Path)
        p.add_argument("--tile-size", type=int, default=64)
        p.add_argument("--token-gap", type=int, default=8)
        p.add_argument("--frame-gap", type=int, default=16)
        p.add_argument("--padding", type=int, default=16)
        p.add_argument("--direction", choices=("ltr", "rtl"), default="ltr")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    options = RenderOptions(args.tile_size, args.token_gap, args.frame_gap, args.padding, args.direction)
    result = render_file(args.input, options=options)
    diagnostics = result.get("diagnostics", [])
    for diag in diagnostics:
        print(json.dumps(diag, ensure_ascii=False, sort_keys=True), file=sys.stderr)
    if any(d.get("level") == "error" for d in diagnostics):
        return 1
    if args.command == "normalize":
        text = json.dumps(result["message"], ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    else:
        text = result["render"]["svg"]
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
