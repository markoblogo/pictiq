# Pictiq Composition Library — Historical Composition Harvest v0.1

**Status:** `HARVEST COMPLETE / AWAITING HUMAN RECONCILIATION`
**Repository snapshot:** `8fae507`
**Harvested:** 2026-09-27

This is a research harvest of exact, source-paired Pictiq messages. It is not a public Composition Library, a translation table, a comprehension result, or automatic acceptance of any record. Record IDs (`clh-v01-NNNN`) are local harvest IDs only. Human reconciliation is the next gate. No vocabulary, grammar, numeric notation, production behavior, or research conclusion is changed here.

## Review package

- [`review/index.html`](review/index.html) — static review of the 81 unique exact candidate records, with compact/evidence modes and filters for source family, lifecycle, mode, surface, preservation, compatibility, tests, failures, and text. Decision and notes fields are local and are not saved.
- [`review/exclusions.html`](review/exclusions.html) — evidence-only and unsafe-to-harvest findings with reason and recovery requirements.
- [`review-dataset.json`](review-dataset.json) — structured review copy with current-renderer previews and source mapping.
- [`manifest.json`](manifest.json), [`source-coverage.json`](source-coverage.json), [`inventory.json`](inventory.json), [`harvest-counts.json`](harvest-counts.json), [`evidence-only.json`](evidence-only.json), [`unsafe-to-harvest.json`](unsafe-to-harvest.json).
- [`records/`](records/) — one exact Message per record; [`renders/`](renders/) are previews generated from those exact Message JSONs by the current repository renderer.

## Inclusion and preservation rules

An exact-harvestable finding required a source that explicitly pairs communicative intent with an exact ordered message and establishes a concrete `EMBODIED` or `STANDALONE` mode. Findings were deduplicated only within the same source family, exact Message, mode, and surface; separate intent/context evidence is retained as neighborhoods. No phrase was translated into Pictiq, no flattened artwork was decoded, no source message was repaired, and no grammar example was expanded combinatorially.

`lifecycle_status` retains the source’s evidence status: `EXPERIMENTAL` is not human acceptance; `CANDIDATE` is an illustrative Handbook example; `HUMAN_ACCEPTED` records creator acceptance of landing copy only, not external comprehension. Road and Web/UI findings remain scoped to their documented reconciliation. Stress Test 05 is the frozen canonical message without a verified matching run; its mismatched transcript sets remain unsafe. Stress Test 07.1 remains paused and preserved; its stimuli are inventory evidence only and were not decoded.

Where historical ID arrays were explicit but not stored as Message JSON, a transparent v0.1 research encoding was rendered and separately marked as such. Compatibility is source-specific; the harvest does not claim that historical records validate against the current schema unless checks say so. Handbook source references are minimal glosses only; no substantial book text is copied.

## Coverage and counts

See [`source-coverage-ledger.md`](source-coverage-ledger.md) and [`source-coverage.json`](source-coverage.json) for every inspected source family, paths, counts, and unresolved retrieval/provenance issues. In this snapshot, 182 candidate findings were inventoried: 89 exact-harvestable source findings collapsed to 81 unique records, 86 evidence-only findings, and 7 unsafe findings. All 81 exact records rendered with the current canonical renderer. These are repository-retrieval counts, **not** vocabulary coverage, user-frequency, comprehension, or product-success measures. Corpus summaries use only these 81 unique messages and are descriptive of this biased historical sample.

The proposal schema is discussion-only and no formal Composition Library JSON Schema validator is implemented. Harvest structural checks and existing Message Schema fixture-validator checks are reported separately; neither makes a candidate accepted. Current registry/message validation is independently recorded per record. Three records preserve the historical `place_hotel` ID, which is absent from the current icon registry; those are marked `HISTORICAL` and were not rewritten.

## Source families inspected

Protocol/Grammar/Handbook; Message/Renderer/Composer; portable layouts; Road/Wayfinding; Odyssey; Web/UI; Landing; constrained Translation Pilot 04A; Stress Tests 05, 06, 06B, 07 and 07.1; editorial cases 001/002; and Toki Pona crosswalk/history references. Full paths and scope are listed in the ledger.

## Next step and protected work

**NEXT:** human reconciliation of this harvest, including candidate semantics, lifecycle labels, provenance, and any record-schema gaps. Do not start the Practical Coverage Corpus until that reconciliation is complete. Later order remains: Practical Coverage Corpus → Composer coverage → Frequency/Semantic Coverage → Translator Spike → Agent Retrieval Stress Test → return to 07.1.

The 07.1 frozen SVG/PNG stimuli, hashes, manifests, prompts, hypotheses, randomization, and protocol were not changed. Production icons, lexicon, entities, grammar, protocol, Numeric Notation, Message Schema, Renderer, Composer, landing, Handbook, and licenses were not changed.
