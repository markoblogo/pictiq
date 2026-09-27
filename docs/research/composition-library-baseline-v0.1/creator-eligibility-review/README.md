# Dictionary Creator Eligibility Review Viewer v0.1

This local, static viewer lets the creator review whether already accepted compositions belong in a future public Composition Dictionary and whether their entry metadata is suitable. It does not reopen semantic acceptance.

## Frozen source and binding

Source baseline: `../` — Accepted Composition Corpus Baseline v0.1 and Dictionary Candidate v0.1. The viewer contains 65 review units: 60 system-classified YES candidates and 5 system-classified REVIEW records. The 12 CORPUS_ONLY records are excluded from individual review and linked as a read-only summary.

The import/export binding is `clb-v0.1:33b00632bedb342af8aed35b62824b9b60663474bca556bb69e4ab16ea22d3e0`. It is derived from baseline version `0.1` and the manifest SHA-256 values for `accepted-corpus.json`, `dictionary-candidate.json`, and `dictionary-eligibility.json`. Any changed source snapshot requires a matching viewer/export.

## Decisions

- `KEEP_IN_DICTIONARY` — include the accepted composition in the future public Dictionary.
- `MOVE_TO_CORPUS_ONLY` — retain it in the research corpus, outside the Dictionary.
- `REVIEW_LATER` — defer the creator decision.
- `EDIT_ENTRY_METADATA` — request a headword, alias, context, or presentation correction. Notes record the request; this viewer does not apply it.

Blank entries start as `UNREVIEWED`; system eligibility is displayed separately and never preselected as the creator's decision. The five REVIEW questions are shown as supplied and remain unanswered here.

## Local progress and files

The display payload is embedded in the HTML from the frozen source files for static use. Progress and notes persist in this browser's `localStorage`; they are not written to repository datasets. Export downloads the complete 65-record review JSON. Import checks review type/version, baseline and candidate binding, stable IDs, duplicate/missing records, eligibility/reference binding, and decision values before replacing local progress. Reset clears only local state for this snapshot after confirmation.

## Next step

After completing review, export the JSON and run the designated creator-reconciliation step. That result should then be reconciled and reviewed before any final Composition Dictionary Baseline is created.
