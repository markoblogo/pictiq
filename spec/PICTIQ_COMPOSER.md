# Pictiq Composer v0.1 — Interaction and Architecture Specification

> Status: implementation specification / not implemented
> Target: Pictiq Message Format v0.1, Pictiq Shorthand v0.1, Renderer v0.1
> Rule: this specification does not change Pictiq grammar, Message Schema, Renderer, vocabulary, icons, profiles, packs, Entity Symbols, or numeric notation.

## Purpose

Composer v0.1 is a human authoring interface for constructing valid Pictiq Messages without manually editing JSON, shorthand, SVG, or repository files.

Composer is not a new Pictiq engine, second Renderer, AI translator, illustration tool, vector editor, publishing app, account system, or cloud workspace.

The product loop is:

HUMAN INTENT -> HUMAN TILE SELECTION / COMPOSITION -> PICTIQ MESSAGE JSON -> EXISTING RENDERER -> VISUAL PICTIQ.

The primary success criterion is:

> Can a person construct, edit, understand, and export a valid Pictiq message without knowing Pictiq's internal JSON format or repository structure?

Users may need to learn Pictiq concepts and grammar. They should not need to know internal IDs such as `qual_sacred`, `nature_cloud`, or `entity:poseidon@odyssey` to operate the interface. Internal IDs may appear in advanced/debug views.

## Non-goals for v0.1

Composer v0.1 must not:

- build an AI translator or “describe what you want” box;
- call LLMs, RAG, embeddings, or fuzzy semantic completion;
- infer what the user “really means”;
- silently rewrite selected concepts;
- duplicate or fork the canonical vocabulary;
- duplicate the Renderer as an untested visual approximation;
- introduce nested grouping, syntax trees, semantic graphs, subject/predicate/object fields, or arbitrary spatial semantic positioning;
- add login, cloud storage, synchronization, authentication, sharing networks, marketplace features, PNG/PDF/JPG export, or a tutorial system.

## Minimum user loop

1. Open Composer.
2. Choose or accept a profile/context.
3. Browse or search available concepts.
4. Select a concept.
5. Add it to the current frame.
6. Add more concepts.
7. Reorder concepts.
8. Delete concepts.
9. Create another frame.
10. Edit supported token parameters.
11. See live Renderer preview.
12. Inspect human-readable diagnostics.
13. Copy/export the result.

This loop must work without manual JSON editing.

## Conceptual UI areas

Composer is organized around three conceptual areas:

1. Vocabulary / palette.
2. Message workspace.
3. Renderer preview.

The specification does not prescribe exact pixel layout. Desktop may use simultaneous columns. Narrow/mobile layouts may use panels or tabs: Palette, Message, Preview. The underlying Composer state must be identical across layouts.

## Palette

The palette exposes human-facing concept information:

- actual canonical icon or entity artwork;
- primary label;
- short semantic gloss;
- optional secondary ID/debug details.

The palette should be task-sized, not a dump of all 83 ordinary identifiers plus all Entity Symbols.

Minimum palette groups:

- Core / recommended starter concepts;
- current Context Pack concepts;
- Entity Symbols when relevant;
- Number insertion control;
- search.

Search is deterministic lexical search. It may match current labels, semantic glosses, aliases/synonyms, tags, and optionally internal IDs. v0.1 must not use AI, embeddings, fuzzy semantic inference, or automatic replacement.

## Core, Context Packs, and Profiles

Composer makes the distinction between Canonical Registry, Core, Context Packs, and Profiles operational:

> Context/Profile controls what Composer recommends or exposes in the palette. It does not determine whether Renderer is physically capable of rendering a valid canonical concept.

Profile affects palette recommendations, validation, diagnostics, and authoring guidance. Profile must not silently change token semantics.

Current concrete profile examples are:

- `standalone-core-v0.1`
- `embodied-core-v0.1`

Current concrete context-pack examples are:

- `universal-core`
- `universal-v1`
- `city-paris-v0.1`
- `road-wayfinding-v0.1`

Composer may expose these with human-readable labels such as “Standalone,” “Embodied,” “Universal Core,” “Universal,” “Paris,” and “Road / Wayfinding.” Do not invent packs merely to fill UI mockups.

Message Schema v0.1 supports an ordered `contexts` array, so Composer may allow multiple selected contexts. It must make context switching understandable without requiring users to know package architecture.

## Message workspace

The workspace edits canonical Pictiq Message structure:

DOCUMENT -> FRAMES -> TOKENS.

Each frame contains a flat ordered token sequence. Users must be able to add, reorder, and delete tokens; create and delete frames; and reorder frames if useful.

Composer must preserve Message Schema v0.1. No nested groups, brackets, arbitrary 2D semantic layout, subject/predicate/object fields, or arrows between tiles are permitted. If implementation pressure makes grouping feel necessary, record `FUTURE_LANGUAGE_PRESSURE`; do not solve it secretly in UI state.

Reordering should support drag-and-drop where available, plus keyboard or explicit move-left / move-right controls. Drag-and-drop must not be the only accessible way to reorder.

## Special token: number

Number is not an ordinary vocabulary icon. Composer should expose a simple number insertion/editing interaction:

- Add: Number.
- Inspector: Value.
- Output token: `{ "type": "number", "value": 50 }`.

Only values supported by current Numeric Notation should be accepted as valid. Current Renderer v0.1 supports exact `50`; arbitrary numbers must not be implied until numeric notation expands.

## Special token parameter: color

Color is a token-local parameter, not a separate lexical concept. Composer may expose supported color editing through a small inspector, for example selecting `nature_cloud` and setting `params.color` to `#555555`.

Composer must not become a general design/color editor. It should expose only color behavior supported by Message Schema and Renderer.

## Entity Symbols

Entity Symbols remain separate from ordinary vocabulary. Composer should expose them as human-readable named entities, such as Poseidon, Odysseus, and Polyphemus, rather than requiring typed IDs such as `entity:poseidon@odyssey`.

Entity palette content should be context-aware. Odyssey entities should not clutter unrelated tasks.

If multiple entities eventually share a name, Composer must not guess. It should require explicit namespace/context disambiguation, while avoiding a complex namespace manager in v0.1.

## Live Renderer preview

Composer must use Renderer v0.1 as the source of truth for visual output:

Composer state -> Pictiq Message JSON -> Normalizer / Validator -> Renderer -> SVG preview.

If Composer output differs from CLI Renderer output for the same Message and Render Options, that is a bug.

## Diagnostics

Composer should expose Renderer/Validator diagnostics in human language. Examples:

- unknown concept;
- legacy ID normalized;
- profile mismatch;
- context mismatch;
- unsupported parameter;
- invalid number.

Raw diagnostic JSON is not the primary UX. It may be available later in an advanced/debug view. Warnings should not necessarily block editing or export. Errors that make a message invalid must be clearly distinguishable.

## Import and edit

Composer v0.1 should open/import:

- Pictiq Message JSON;
- `.pictiq` shorthand.

Required loop:

IMPORT -> NORMALIZE -> EDIT -> RENDER -> EXPORT.

Supported legacy IDs must normalize through the existing compatibility layer. For example:

- `need_bar` -> `drink_alcohol`
- `place_hotel` -> `place_home`

Composer should inform the user that normalization occurred and must not preserve legacy IDs in newly exported canonical JSON.

## New, reset, undo

New message defaults should be compatible with the current schema:

- `schema`: `0.1`
- `pictiq`: `1.1`
- optional profile chosen by the user or default environment;
- empty or selected contexts;
- one initially empty editable frame in UI, serialized only when valid/non-empty.

Composer should support clearing the current frame, deleting a frame, and starting a new message. Destructive actions should have obvious recovery or confirmation where appropriate.

Local session undo/redo is a v0.1 SHOULD, not MUST. It is valuable because reorder/delete actions are easy to perform accidentally, but it should remain local/session-only and should not imply cloud history.

## Export

Composer v0.1 should support:

- copy/export canonical Message JSON;
- copy/export `.pictiq` shorthand;
- export SVG.

PNG, PDF, JPG, account storage, cloud sync, and publishing flows are future derivative features, not v0.1 requirements.

## Shorthand serialization requirement

The current repository implements shorthand parsing and normalization, but no deterministic canonical JSON -> shorthand serializer was found. Composer needs shorthand export. Therefore a small deterministic shorthand serializer is an implementation requirement for Composer v0.1.

This requirement does not change Pictiq Shorthand v0.1 in this specification task.

## Accessibility requirements

Composer v0.1 should not be mouse-only. Minimum requirements:

- keyboard navigation;
- visible focus states;
- accessible labels for icons/entities;
- non-drag reorder controls;
- text labels and glosses;
- diagnostics that do not rely only on color.

Do not claim formal accessibility compliance before testing.

## Compact UI principle

Composer is a tool, not a marketing landing page. Prefer compact information density, modest headers, small controls, clear workspace, visible palette, visible composition, and visible preview. Avoid giant hero sections, oversized rounded cards, excessive whitespace, huge buttons, and decorative UI that reduces working area.

This spec does not finalize visual styling.

## First-run experience

Onboarding should be minimal: one short explanation, labels visible by default, a small starter palette, and one example if useful. Do not build a tutorial system in v0.1. Human Authoring Stress Test 04B should reveal where onboarding is actually needed.

## Sample workflows using current Pictiq

| Workflow | Human task | Composer actions | Canonical output sketch |
| --- | --- | --- | --- |
| A — Basic | Ask for water. | Select WATER / `need_water`; select QUESTION / `punct_question`; preview. | `need_water punct_question` |
| B — Negation | Say no alcohol. | Select ALCOHOL / `drink_alcohol`; select NO / `logic_no`; preview. | `drink_alcohol logic_no` |
| C — Home | Indicate home/shelter/sleeping place. | Select HOME / `place_home`; optionally add question or direction. | `place_home` |
| D — Numeric | Show exact 50. | Add Number; set value `50`; preview. | number token `{ "value": 50 }` |
| E — Entity | Compose a small Odyssey message. | Choose Odyssey context; select Poseidon; select BAD / `qual_bad`; preview. | `entity:poseidon@odyssey qual_bad` |
| F — Multi-frame | Ask water, then indicate here. | Frame 1: `need_water punct_question`; Frame 2: `rel_here`. | two frames |
| G — Import legacy | Open old shorthand containing `need_bar` or `place_hotel`. | Import; normalize; show warning; edit/export current IDs. | `drink_alcohol`; `place_home` |

## Implementation architecture note

Current GitHub Pages architecture is a static `/docs` site using HTML, CSS, vanilla JavaScript, and JSON/SVG assets. Current Renderer v0.1 is Python. The Python Renderer cannot run directly in a normal static GitHub Pages browser environment.

Do not silently duplicate SVG composition logic in frontend code. Future implementation must choose an explicit renderer architecture:

| Option | Fit | Tradeoff |
| --- | --- | --- |
| A. Server/API Renderer | Strong Renderer source-of-truth; Composer calls a service. | Requires hosting, API deployment, availability, and possibly CORS/security work; no longer pure GitHub Pages. |
| B. Browser-compatible renderer port with parity tests | Fits static Pages and public no-login Composer. | Creates a second implementation; acceptable only if parity tests compare it against Python Renderer v0.1 golden outputs. |
| C. Shared/generated rendering data plus minimal browser renderer | May reduce drift if geometry/registry data are generated from repository source. | Still needs browser rendering logic and parity tests. |
| D. Pyodide/browser Python bridge | Keeps Python logic closer to source. | Heavy bundle and file-loading complexity; likely too large for a first compact Composer. |

Technical Spike 01 validated the smallest likely public path: a static Composer can use a browser-compatible renderer adapter with generated canonical SVG/data assets, gated by parity tests against Python Renderer v0.1. The accepted architecture is `ACCEPT_WITH_GUARDRAILS`: the browser renderer may be a secondary implementation only when canonical data is generated from repository sources and parity tests remain part of validation.

## Renderer parity requirement

Any future browser-side rendering must have parity tests against Renderer v0.1. “Looks approximately the same” is not sufficient. Same canonical Message plus same render options should produce semantically equivalent output and visually matching tile content, spacing, frame layout, token order, diagnostics, legacy normalization, numeric rendering, entity rendering, and color parameters.

## Single source of truth

Composer must not maintain its own Pictiq vocabulary. Repository canonical data remains the source of truth. Composer consumes:

- `lexicon/icon-index.json`
- `lexicon/vocabulary-classification.json`
- `packs/*.json`
- `profiles/*.json`
- `entities/entity-index.json`
- `notation/numeric/index.json`
- localization metadata

Renderer remains the source of truth for visual output.

## First public surface boundary

Composer v0.1 is intended to become the first broadly usable authoring surface for Pictiq. The first public surface is:

WRITE -> EDIT -> SEE -> EXPORT.

No marketing pages, accounts, community features, sharing networks, marketplace functionality, AI translation, or natural-language translation are part of v0.1.
