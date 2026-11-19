# Composition Dictionary Baseline v0.1

**Status:** creator-reviewed accepted research baseline; awaiting final creator visual QA. Internal research only; not normative Grammar and not deployed.

## Purpose and boundaries

A Dictionary entry is an evidence-backed reusable semantic unit with one or more context-bounded Pictiq representations. It is not an English phrase equated with one universal Pictiq sequence. English headwords are lookup labels; exact current Messages, contexts, and evidence remain authoritative. No comprehension, universal-meaning, or external-validation claim follows from creator review.

The Lexicon remains the primitive registry. The Dictionary organizes reusable words/concepts/short phrases. The Accepted Composition Corpus remains the wider evidence/history archive. This package does not rewrite the Corpus or Candidate predecessor. Historical, rejected, superseded, and blocked lineage remains accessible through Corpus sources and this package's lineage file. Odyssey narrative containers and Stress Test 05 discourse remain outside the Dictionary. The hotel + color case remains blocked because Explicit Color Modifier Mechanism is REQUIRED / NOT IMPLEMENTED.

## Sources and review

Built from Accepted Composition Corpus Baseline v0.1, Dictionary Candidate v0.1, current registries, and the archived owner-supplied creator review. The export is preserved byte-for-byte at `creator-review-export.json` (SHA-256 `3151d779efab99445f3f5b61cd5da41dded979d435cf11226da5d62bbfe9d5ae`). Its source snapshot is `clb-v0.1:33b00632bedb342af8aed35b62824b9b60663474bca556bb69e4ab16ea22d3e0`. All 65 units were decided: `{"EDIT_ENTRY_METADATA": 1, "KEEP_IN_DICTIONARY": 64, "MOVE_TO_CORPUS_ONLY": 0, "REVIEW_LATER": 0}`. Ten records carry non-empty Russian notes; each note is preserved verbatim and separately classified in `creator-review-amendment.json`.

The Candidate's old YES/REVIEW classifications survive only as history. All five former REVIEW records received KEEP_IN_DICTIONARY and are included. Twelve prior CORPUS_ONLY records were not reviewed and remain excluded.

## Variants, context, and unresolved items

Each entry has a preferred current Message and may have evidence-backed ALTERNATIVE or CONTEXTUAL variants. Historical source forms are lineage, not current alternatives. Context warnings remain visible in the viewer. Two note portions remain in `creator-notes-follow-up.json`: the exact scope/token for a proposed UP/AHEAD prohibition and the exact order for a separate schedule/timetable composition. Neither is presented as an accepted Message. The arrival-time entry remains accepted.

`translator-lessons.json` contains **DESIGN EVIDENCE / NOT EXECUTABLE RULE** only. It does not change Grammar, Protocol, Composer, or implement a Translator.

## Review and validation

- Full Dictionary-style viewer: `review/index.html`
- Changed-entry before/after creator QA: `review/final-creator-visual-qa.html`
- Follow-up question view: `creator-notes-follow-up/index.html`
- Exact messages and variants: `dictionary.json`, `variants.json`
- Creator amendment and lineage: `creator-review-amendment.json`, `lineage.json`
- Validation and hashes: `validation.json`, `render-manifest.json`, `manifest.json`

All 71 preferred/accepted variant Messages passed the repository's schema-shape and registry-aware checks and rendered through the canonical Renderer. New research records receive deterministic structural validation; this project has no formal Dictionary schema. These checks are not a human visual acceptance. Run `python3 tools/research/build_composition_dictionary_baseline_v0_1.py` from the repository root to rebuild deterministically from the archived export. Run `pytest -q tests/test_composition_dictionary_baseline_v0_1.py` for the research builder tests.

**Next gate:** creator visually reviews the changed-items QA surface and full viewer; then close/freeze this baseline. Public Dictionary deployment is a later product decision. After visual acceptance, the planned sequence is Color Modifier repair, Practical Coverage Corpus, Composer coverage, Translator Spike, and later retrieval research. Current stage: `FINAL CREATOR VISUAL QA`.
