# Pictiq Machine / Agent Access — architecture concept

> **Status:** future architecture / not implemented. No API, MCP server, manifest, search service, or additional registry is created here.

## Purpose and authority

An unfamiliar machine should be able to discover Pictiq's authoritative records from one future official entry point, without scraping the whole repository, guessing IDs, treating English glosses as translations, or drawing substitute glyphs. Human and machine views must derive from or reference one authoritative data layer.

| Concern | Authority | Machine layer responsibility |
|---|---|---|
| Primitive IDs and meanings | [canonical Lexicon data](../../../lexicon/icon-index.json), vocabulary classification, and Entity registry | Find/return current canonical record and status; do not duplicate meanings |
| Valid message structure | [Message Schema](../../../spec/pictiq-message.schema.json) | Reuse exact schema and validation behavior |
| Valid language behavior | [Grammar](../../../spec/GRAMMAR.md) and [Protocol](../../../spec/PROTOCOL.md) | Link relevant rules; do not reinterpret them |
| Reusable public compositions | Future Composition Dictionary | Retrieve reusable, human-reviewed exact Messages with separate Dictionary eligibility and evidence |
| Broader evidence-bearing compositions | Future internal Composition Corpus | Retrieve exact Messages and source evidence, including narrative, experimental, historical, rejected, and failure records; do not imply Dictionary eligibility |
| Visual output | Canonical SVG assets and deterministic Renderer | Resolve original assets or request the existing Renderer; do not synthesize canonical art |
| Human authoring | Composer | Remain the authoring/review surface; future exports may carry provenance |

Machine discoverability does not confer permission to reuse assets commercially. Licensing terms remain governed by the existing license records and separate commercial terms.

## Conceptual retrieval contract

Future access may support these conceptual operations; names are descriptive, not an API specification:

- `search_primitives(query, context?)` and `get_primitive(canonical_id)` return canonical ID, meaning, aliases/search terms, vocabulary class, status, compatibility, canonical SVG reference, stable address, related Library records, and Grammar/Protocol references. Lexicon remains the only semantic registry.
- `search_compositions(intent, communication_mode, surface, context)` and `get_composition(composition_id)` return exact Message JSON, linked intent/neighborhood, rendered-preview reference, mode/surface compatibility, context requirements and `context_supplies`, lifecycle, preservation assessment, origin/uses/tests/failures, ambiguity, and validity.
- `validate_message(message_json)` and `render_message(message_json)` reuse existing Schema, validators, and Renderer. No parallel validator or renderer.
- `report_gap(intent, context, mode, surface, attempted_candidates)` may record pressure for human review under existing NEED-BEFORE-VOCABULARY governance. It does not create vocabulary.

The Composition Library model is one exact message per record with extensible communication surface and existing `EMBODIED` / `STANDALONE` mode. Shared intent/neighborhood references can link different records; they do not imply a universal phrase translation. Context supplies must be evidence-backed. Coverage is assessed per mode/surface/context, not just per intent. Composition Dictionary eligibility (`YES`, `CORPUS_ONLY`, or `REVIEW`) is separate from semantic disposition and lifecycle; the public Library view should primarily expose the Dictionary. Translator retrieval may use Dictionary first and Corpus as broader evidence, while making authority/status explicit.

## Stable addressing and entry point

A future single official machine-entry URL should link to the Lexicon, canonical SVG assets, Composition Library, Message Schema, Grammar/Protocol, validation and rendering contracts, and known gaps/limitations. Stable addresses should resolve to canonical records/assets or versioned references, not scraped prose. `llms.txt` may later point to a machine manifest; neither it nor `llms.txt` is changed in this pass. Exact production URL design remains open until the repository's source-of-truth and publishing architecture are selected.

Human-facing HTML, machine-readable data, Translator retrieval, Composer references, and any later API should be generated from or reference the same authority. Do not manually maintain parallel semantic copies. The current Lexicon/index schema mismatch (extra Lexicon fields ignored by the current validator) is separate technical debt; document and repair it in a small dedicated validation pass, not as a prerequisite or silent exception here.

## Forward and reverse use

**Forward:** source/dialogue/structured intent → semantic intent → resolve mode + surface + context → Composition Dictionary retrieval → Composition Corpus evidence/context → Lexicon + Grammar fallback → candidate Message JSON → existing validation → canonical Renderer preview → human decision. The Translator can stop with `LOSSY`, `GAP`, or `NEEDS_HUMAN_REVIEW`; it is not required to emit a message.

**Reverse/reference:** prefer (1) exact Message JSON or provenance sidecar, (2) Composer/Renderer structured export, (3) canonical IDs and hashes, (4) visual matching against canonical assets, then (5) unconstrained vision only as candidate inference. Resolve IDs through the Lexicon, retrieve original SVGs, inspect known compositions/evidence, and report ambiguity. If structured provenance is absent, visual matching does not become canonical identification without review.

## Canonical assets and production evidence

AI may reason about or propose semantics. When a canonical asset exists, AI must not synthesize or redraw canonical Pictiq glyph artwork. Canonical visual output must come from canonical SVGs, deterministic Renderer output, or preserved immutable Composer/Renderer exports. This applies to image generation, comics, books, presentations, mockups, and diagrams. The documented editorial production issue is that generative image workflows can imitate or redraw symbols; the remedy is semantic decision → canonical IDs → canonical assets/Renderer → immutable Pictiq layer → illustration/layout integration, not teaching an image model to imitate the glyphs.

A future Composer sidecar such as `dialogue-03.pictiq.json` could accompany an image and reference existing Message JSON plus stable composition/block/frame/source-turn IDs, canonical token/asset references, semantic source, speaker, mode, surface, context, placement/panel, version, and hashes. Avoid duplicating the Message itself. Case 002 has semantic dialogue and source sheets but unresolved exact per-turn Composer block mapping; flattened artwork is not enough to reconstruct it.

## Future acceptance target and research

Design target, not proven capability: an unfamiliar AI given one official entry point can locate a primitive, its canonical SVG and meaning, relevant known compositions, context/evidence, and a valid Message representation without reading the entire repository or synthesizing replacement glyphs.

The separate [Agent Retrieval Stress Test plan](../../research/pictiq-agent-retrieval-stress-test-plan.md) is `PLANNED / NOT RUN`. It will compare current repository discovery with a future structured machine layer using identical fixed tasks. Retrieval accuracy, mode/surface matching, false coverage, ignored failures, invented IDs/glyphs, and honest GAP are distinct measures; it is not a comprehension or superiority claim.
