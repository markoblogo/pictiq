# Changelog

All notable changes to this repository will be documented in this file.

This project uses milestone-style tags. The `-infra` suffix indicates a pre-icons infrastructure release.

## Unreleased

### Odyssey Stress Test 03 findings
- Formalized Stage 1 narrative architecture for Odyssey × Toki Pona × sitelen pona × Pictiq: semantic/practical translation, `INTENTIONAL_OMISSION`, structural gender neutrality, semantic frames, and deferred entity-symbol work.
- Integrated the five human-accepted Stage 2A ordinary primitives from the supplied reference sheet: `action_conflict`, `move_watercraft`, `qual_sacred`, `nature_animal`, and `nature_cloud`.
- Bumped ordinary canonical lexicon metadata to `0.7.0`; the ordinary lexicon now has 82 icons. Entity symbols remain counted separately.
- Added five human-accepted Stage 2B Odyssey Entity Symbols: `entity:poseidon@odyssey`, `entity:zeus@odyssey`, `entity:saturn@odyssey`, `entity:polyphemus@odyssey`, and `entity:calypso@odyssey`.

### Road & Public Wayfinding findings
- Accepted `surface_wavy` and `state_dead` as contextual ordinary canonical primitives emerging from Stress Test 02; ordinary canonical lexicon metadata is now `0.6.0` with 77 icons.
- Added partial shared numeric notation under `notation/numeric/`, demonstrating `50` through digit assets rather than a lexical `num_50`.
- Added numeric notation validation and QA evidence for WAVY, DEAD, and numeric `50`.

### Vocabulary and phrase architecture
- Added `lexicon/vocabulary-classification.json` as the machine-readable source of truth for architectural role classification across all accepted ordinary canonical IDs, explicitly excluding the 11 entity-symbol examples.
- Added `spec/VOCABULARY_CLASSIFICATION.md` and validation for the accepted distinction between Canonical Registry, Core Vocabulary, Standalone Core, Context Packs, Specialized vocabulary, Mechanisms, and Entity Registry.
- Formalized phrase architecture in `spec/GRAMMAR.md`: bare tile / zero-intent, bare adjacency as contextual association, postfix scope for qualifiers/quantities/negation, additive numeric quantity expressions, relational-orientation operators, `rel_here` as reference, and one proposition per phrase line.

### Accepted canonical lexicon work
- Accepted Standalone Batch C as canonical: `body_mouth`, `rel_here`, `rel_up`, `rel_down`, and `nature_moon`.
- Bumped ordinary canonical lexicon metadata to `0.5.0`; the ordinary lexicon now has 75 icons.
- Recorded Batch C architecture decisions for contextual polysemy, action-relevant ambiguity, standalone externalization of embodiment, spatial reference, the `< > ∧ ∨` relation/orientation family, and `time + nature_sun` / `time + nature_moon` day/night composition.

### Entity symbols
- Accepted the first six official Pictiq project entity-symbol examples: `entity:anton-biletskyi-volokh@personal`, `entity:odysseus@literary`, `entity:william-shakespeare@historical`, `entity:albert-einstein@historical`, `entity:leonardo-da-vinci@historical`, and `entity:siddhartha-gautama-buddha@historical`.
- Added `entities/entity-index.json`, `entities/svg/`, entity-source crops, QA generation, and entity-registry validation.
- Clarified that entity symbols are visual proper names in scoped namespaces, not ordinary lexical icons; the entity registry count is 11 and must not be combined into ordinary Core or canonical icon counts.
- Formalized self-defined personal symbols, project-scoped historical/literary examples, narrative/context namespaces, contextual association without a possession operator, and the Buddha / Siddhartha Gautama semantic boundary.

## v1.0.2 — 2026-09-09

### Architecture
- Added recommended Embodied and Standalone vocabulary profiles over the single canonical lexicon; context packs may layer on either profile.
- Replaced the generic classroom-style usability gate with task-based real-context testing guidance and staged Batch B planning.
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
- Added approved Batch B concepts: `eye_look`, `item_clothing`, `comm_speak`, `comm_sound`, `media_text`, `media_image`, `nature_sun`, `state_light`, `food_produce`, `food_bakery`, `rel_greater`, and `rel_lesser`.
- Bumped canonical lexicon metadata to `0.4.0` (70 icons) and preserved the supplied reference morphology through the trace and visual-QA workflow.

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
