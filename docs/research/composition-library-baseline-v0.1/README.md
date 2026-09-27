# Composition Library Baseline v0.1

**Research-only package.** The Accepted Composition Corpus is a human-reconciled evidence baseline, not normative Grammar. The Public Composition Dictionary is a system-classified candidate and is **not public**; all YES and REVIEW eligibility records await creator eligibility review.

## Frozen inputs and layers

This package was generated from Historical Harvest v0.1 at snapshot `8fae507`, the byte-preserved creator export (SHA-256 `455588e54a561e162d4b8ffdad38ad1b0f59612ccb3fafb889cc6e8ba41b40bc`), and its 2026-09-27 reconciliation addendum. The Harvest and both reconciliation records remain separate and unchanged. The Corpus retains exact historical Messages, current creator replacements, rejections, provenance, tests, failures, compatibility, and lineage.

## Contents

- `accepted-corpus.json` — processed Corpus with 81 historical records plus three separately identified creator replacements.
- `dictionary-candidate.json` — 60 YES entries only; each links to Corpus evidence and a canonical Renderer SVG.
- `dictionary-eligibility.json` — record-level YES / CORPUS_ONLY / REVIEW classifications for 77 current-valid accepted records.
- `reconciliation-accounting.json` — final disposition for all 81 Harvest candidates.
- `lineage.json`, `negative-evidence.json`, `blocked.json` — replacement, rejected/superseded, and blocked-color evidence.
- `explicit-color-modifier-repair.md` — separate implementation requirement; no color mechanism is implemented here.
- `renders/` — canonical Renderer SVGs for 77 valid current accepted Messages.
- `review/corpus.html` — filterable internal Corpus viewer.
- `review/dictionary.html` — dictionary-like YES candidate viewer.
- `review/eligibility-review.html` — the five-entry REVIEW queue.
- `review/replacement-qa.html` — historical-to-replacement visual comparison and the blocked color case.
- `corpus-only-summary.md` — concise rationale and records excluded from the Dictionary.

## Accounting

Of 81 original candidates, creator decisions were 77 ACCEPT, 1 EDIT, 3 REJECT. Post-addendum, 74 are accepted unchanged and current-valid, three exact creator replacements are current-valid, three historical ACCEPT records containing retired `place_hotel` remain accepted historical evidence but are not executable against the current registry, and one hotel/color target is blocked. There are no rejected-without-replacement cases. Corpus size is 84 when the 81 exact historical records and three new replacement records are counted separately.

The current-valid accepted set is 77: 60 Dictionary YES, 12 CORPUS_ONLY, and 5 REVIEW. The 60 YES items produce 60 Dictionary entries. No rejected, superseded, historical-only incompatible, or blocked case enters the Dictionary candidate. Current-valid Messages all validate and render; the three `place_hotel` historical messages are explicitly preserved as `HISTORICAL_ONLY / NOT CURRENTLY VALID` and are not silently rewritten.

Dictionary eligibility is an editorial candidate classification, independent of creator semantic acceptance. The English headword is a lookup label; the evidence-bounded semantic neighbourhood and context remain authoritative. No automated extraction, narrative splitting, or new sub-composition creation occurred. Odyssey and Stress Test 05 whole multi-frame records remain CORPUS_ONLY.

## Human review gate

Review all 60 YES entries in `review/dictionary.html`, the five specific questions in `review/eligibility-review.html`, and the grouped CORPUS_ONLY summary. The next creator step is **eligibility review only**: `KEEP_IN_DICTIONARY`, `MOVE_TO_CORPUS_ONLY`, `REVIEW_LATER`, or `EDIT_ENTRY_METADATA`. Do not re-review semantic correctness of the 81 harvested records.

This is not a deployed Dictionary, website route, public Lexicon update, or new protocol claim.

## Rebuild and validation

From repository root:

```sh
python3 tools/research/build_composition_library_baseline.py
```

The deterministic builder joins frozen inputs, validates current Messages with the repository's schema-shape and registry-aware validators, renders through the canonical Renderer, and regenerates this package's data/viewers. It does not mutate Harvest or creator reconciliation inputs. See `manifest.json`, `render-manifest.json`, and `validation.json` for counts and results.
