# Changelog

All notable changes to this repository will be documented in this file.

This project uses milestone-style tags. The `-infra` suffix indicates a pre-icons infrastructure release.

## v0.3.0-infra — Infrastructure & Docs (pre-icons)

### Added
- Repo scaffolding for the Pictiq protocol: `spec/`, `lexicon/`, `packs/`, `icons/`, `tools/`, `docs/`.
- Static dictionary site under `docs/` (GitHub Pages-ready) with search across `id`, `meaning`, `aliases`, and `tags`.
- CI workflow to run lexicon and SVG validations on pushes and pull requests.
- Lexicon validator: ensures pack IDs exist in the lexicon, unique IDs, required fields, and valid enums.
- SVG validator: enforces `viewBox` consistency and prohibits hardcoded colors (expects `currentColor`/`none`).
- Icon creation template: `templates/tile-template.svg` + usage notes.

### Changed
- Grammar and examples normalized to the token format: `token + token`.
- Negation standardized to `X + logic_no`; `logic_no` allowed as standalone answer.
- Protocol docs clarified around core vs context packs and fixed negations (context-only).

### Fixed
- Removed legacy / deprecated negation operator token usage from lexicon and docs.

### Notes
- No canonical SVG icons are included yet in `icons/svg/` (pre-icons milestone).
- Next milestone focuses on producing the first canonical icon set and enabling stable SVG→PNG generation outputs.

