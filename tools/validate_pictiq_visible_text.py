#!/usr/bin/env python3
"""Prevent visible natural-language text from returning to Pictiq landing mode."""
from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LANDING = ROOT / "docs" / "landing" / "index.html"
ROOT_LANDING = ROOT / "docs" / "index.html"
STYLE = ROOT / "docs" / "landing" / "style.css"
SCRIPT = ROOT / "docs" / "landing" / "landing.js"


class PictiqTextAudit(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.depth = 0
        self.visible_text: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if dict(attrs).get("id") == "pictiq-view":
            self.depth = 1
        elif self.depth:
            self.depth += 1

    def handle_endtag(self, tag: str) -> None:
        if self.depth:
            self.depth -= 1

    def handle_data(self, data: str) -> None:
        if self.depth and data.strip():
            self.visible_text.append(data.strip())


def main() -> int:
    errors = []
    for landing in (ROOT_LANDING, LANDING):
        parser = PictiqTextAudit()
        parser.feed(landing.read_text(encoding="utf-8"))
        if parser.visible_text:
            errors.append(
                f"{landing.relative_to(ROOT)} Pictiq mode contains visible text nodes: "
                + ", ".join(repr(item) for item in parser.visible_text)
            )

    style = STYLE.read_text(encoding="utf-8")
    script = SCRIPT.read_text(encoding="utf-8")
    required = (
        'html[data-mode="pictiq"] .mode-en-label { display:none; }',
        'html[data-mode="pictiq"] .mode-english img { display:block; }',
        'html[data-mode="pictiq"] #english-view, html[data-mode="pictiq"] .nav { display:none !important; }',
        '.nav[hidden], .pictiq-nav[hidden] { display:none !important; }',
        "if (nav) nav.hidden = pictiq;",
        "if (pictiqNav) pictiqNav.hidden = !pictiq;",
    )
    for item in required:
        if item not in (style + script):
            errors.append(f"missing Pictiq-mode visibility guard: {item}")

    if errors:
        raise SystemExit("\n".join(f"ERROR: {error}" for error in errors))
    print("OK: root and legacy Pictiq landing modes have zero visible natural-language text nodes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
