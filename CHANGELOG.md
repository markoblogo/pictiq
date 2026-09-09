# Changelog

All notable changes to this repository will be documented in this file.

This project uses milestone-style tags. The `-infra` suffix indicates a pre-icons infrastructure release.

## v1.0.2 (unreleased)

### Architecture
- Distinguished Embodied Communication from Standalone Communication in the normative protocol.
- Added a decision tree for deciding when the body, live context, composition, or an explicit concept must carry meaning.
- Defined EMBODIED-OMITTABLE, STANDALONE-GAP, and OUT-OF-SCOPE absence states for vocabulary research.
- Classified communication primitives as lexical tiles, modifiers/operators, parametric tiles, entity symbols, and embodied references.
- Separated YES/NO logic from GOOD/BAD evaluation and quantity from proposed LARGE/SMALL scale modifiers.
- Recorded a non-canonical parametric color direction for future standalone use.
- Defined scoped entity-symbol governance without implementing a namespace or registry.

### Implementation
- Added `qual_good` and `qual_bad` evaluation modifiers with explicit `BASE + QUALIFIER` grammar.
- Added `person_generic` for a neutral human participant in standalone messages.
- Added `state_hot` as a practical contextual heat/fire tile and `state_cold` for cold/freezing/refrigeration.
- Added `power_energy` for electricity and electrical power, distinct from `power_plug` and physical strength.
- Expanded the canonical lexicon metadata to `0.3.0`, from 52 to 58 icons, and regenerated the overview grid.

### Research
- Recorded the Toki Pona interoperability findings as evidence about lexical gaps versus standalone needs, not as a translation target or historical influence.
- Preserved the distinction between embodied omissions, standalone gaps, modifiers, parametric color, scoped entity symbols, and grammar that intentionally remains outside Pictiq.
- Updated the standalone backlog with Batch A implementation outcomes while retaining its original rationale and open questions.

Handbook v1.0, existing packs, profiles, layouts, and pre-existing icon geometry remain unchanged.

## v1.0.1

### Perceptual design
- Added six perceptual design principles.
- Formalized recognition-over-abstraction and minimum-sufficient-detail rules.
- Added relative geometry based on canonical tile units, without new numerical constraints.
- Added visual QA pipeline: canonical → small → grid → layout.
- Distinguished structural validation from perceptual acceptance.
- Added Kinneir–Calvert British road signage as a non-normative historical reference system identified after Pictiq v1.0.
- Added a dependency-free, deterministic HTML visual QA sheet tool and automated tooling checks; sheets prepare human review evidence, not semantic acceptance.

This is a standards/documentation and QA workflow evolution, not a Core replacement. No canonical IDs, existing icon geometry, or pack/profile/layout composition changed. Handbook v1.0 remains unchanged. Historical tags `v1.0.0-core` and `handbook-v1.0.0` remain unchanged.

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
