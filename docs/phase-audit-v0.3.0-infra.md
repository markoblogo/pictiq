# Phase Audit — v0.3.0-infra (Infrastructure & Docs, pre-icons)

Audit date: 2026-02-10

## Summary
This audit closes the “infra + docs (pre-icons)” phase. The repository structure, protocol/spec docs, lexicon registry, packs, tooling, and GitHub Pages static dictionary site are in place. No canonical SVG icons have been added yet under `icons/svg/`, and the SVG validator correctly skips when none exist.

## Repo Tree (max depth 3)
```text
.
├── .github
│   └── workflows
│       └── ci.yml
├── docs
│   ├── README.md
│   ├── app.js
│   ├── index.html
│   └── style.css
├── icons
│   ├── png
│   │   ├── black
│   │   └── white
│   └── svg
│       └── .gitkeep
├── lexicon
│   ├── icon-index.json
│   └── icon-index.schema.json
├── packs
│   ├── universal-core.json
│   └── universal-v1.json
├── releases
│   ├── README.md
│   └── v0.3.0-infra.md
├── spec
│   ├── GRAMMAR.md
│   ├── ICON_DEFINITIONS.md
│   ├── ICON_DEFINITIONS.ru.md
│   ├── ICON_SPEC.md
│   ├── PROTOCOL.md
│   └── PROTOCOL.ru.md
├── templates
│   ├── README.md
│   └── tile-template.svg
├── tools
│   ├── README.md
│   ├── render_png.py
│   ├── validate_lexicon.py
│   └── validate_svg.py
├── CHANGELOG.md
├── COMMERCIAL_LICENSE.md
├── CONTRIBUTING.md
├── LICENSE
├── PHASES.md
└── README.md
```

## Required Paths Check
Verified present:
- `spec/` (`ICON_SPEC.md`, `GRAMMAR.md`, `PROTOCOL.md`, `PROTOCOL.ru.md`, `ICON_DEFINITIONS.md`, `ICON_DEFINITIONS.ru.md`)
- `lexicon/` (`icon-index.json`, `icon-index.schema.json`)
- `packs/` (`universal-core.json`, `universal-v1.json`)
- `icons/svg/`, `icons/png/black/`, `icons/png/white/`
- `tools/` (`validate_lexicon.py`, `validate_svg.py`, `render_png.py`, `README.md`)
- `docs/` (`index.html`, `app.js`, `style.css`, `README.md`)
- `.github/workflows/ci.yml`

## Checks Run
```bash
python3 tools/validate_lexicon.py
python3 tools/validate_svg.py
```

## Results
Lexicon validation:
```text
OK: lexicon and packs validated
```

SVG validation:
```text
No SVGs found in /Users/antonbiletskiy-volokh/Downloads/Projects/pictiq/icons/svg (skipping).
```

## Deprecated Tokens / Sanity Grep
- `overlay\_slash`: OK (not found)
- `\(slashed\)`: OK (not found)
- `<text` usage expectation:
  - `icons/svg/`: no SVG icons yet (only `.gitkeep`)
  - The string `<text>` appears in documentation and tooling docs (expected). The canonical SVG validator enforces “no `<text>` elements” once real icons are added.

## Docs Site Basics (GitHub Pages)
- Data load path: `docs/app.js` loads `../lexicon/icon-index.json` (works when serving repo root and visiting `/docs/`).
- Search fields: search text includes `id`, `meaning_en`, `aliases_en`, `tags_en`.
- Fully static: plain HTML/CSS/JS, no build step.
- Optional i18n: language selector attempts to load `../lexicon/i18n/{lang}.json` if present.

## Action Items (Next Phase)
- Add the first canonical SVG icons into `icons/svg/` (starting with the first reference tiles), ensuring:
  - `viewBox="0 0 32 32"`
  - `currentColor`/`none` paint only (no hardcoded colors)
  - no SVG `<text>` elements
- Once icons exist, enable SVG→PNG generation outputs (and decide how to store or regenerate them).
