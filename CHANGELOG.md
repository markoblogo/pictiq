# Changelog

All notable changes to this repository will be documented in this file.

This project uses milestone-style tags. The `-infra` suffix indicates a pre-icons infrastructure release.

## handbook-v1.0.0 — Pictiq Handbook v1.0

### Added
- First public Pictiq Handbook: a 95-page illustrated field guide in PDF and reflowable EPUB formats.
- Protocol rules, Core lexicon, phrase patterns, and the Paris context-pack case.
- Portable layout system with shirt, wallet-card, Nightlife lighter, luggage-tag, and phone-lockscreen examples.
- Alice comic, poetry/semantic-compression, computer-vision, and LLM experiments.
- Canonical handbook cover, promotional artwork, repository download links, and GitHub Pages handbook entry point.

### Repository updates included in the handbook cycle
- Canonical SVG icon set and reusable silhouette pipeline.
- Paris, Nightlife, travel-transit, and personal-demo content profiles.
- Landscape wallet-card geometry and reusable physical-layout renderers.
- `nature_flower` and the finalized Nightlife icon/preview work.

## v1.0.0-core — Core Protocol

### Added
- First stable Core protocol release and printable Core overview.
- Canonical framed SVG icons, Core lexicon, curated packs, and validation tooling.
- Paris context pack and canonical merchandise layout.

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
