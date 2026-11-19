# Pictiq Composition Dictionary v0.1 — research baseline freeze

Frozen on **2026-11-19** (Europe/Paris), from clean source Git revision
`a3c74b104849a0c1b709acbb0ed1aec992f0b6e2`.

```text
Research Dictionary baseline: FROZEN
Creator QA: COMPLETE (10/10)
Reconciliation: PASS
Public site/release: NOT RELEASED IN THIS PASS
Browser visual check: NOT VERIFIED
```

This record fixes an identifiable, reproducible research snapshot: **65 entries,
72 variants**, their exact Messages, applicability and canonical renders. FROZEN
does not establish comprehension, independent human validation, public release
or synchronization with a deployed site. Unknown earlier browser history remains
UNKNOWN; the retained final creator export is the evidence checked here.

## Data and evidence

[freeze-manifest.json](freeze-manifest.json) binds the actual files with SHA-256.
Its paths resolve relative to this directory. Its own SHA-256 is
`b07d839d192583f8b1a0ef5a897cc252f5644cdce671a432a57c240b2665bdf0`.

| File | SHA-256 |
| --- | --- |
| [dictionary.json](dictionary.json) | `b640ec220ceed0f4f7111791170d0d2f97389c29c8a4306ae6927fbf01c4cdeb` |
| [variants.json](variants.json) | `0438faff3e7beabc1bfbb9f7216e3f0c18ec32288034b36d071b26535a0a6dbc` |
| [manifest.json](manifest.json) | `c5b64a275993a55eb30593704ffa817f4955e4ca4814bb470e24767a85fb0a48` |

The existing manifest remains the generated-artifact inventory. Its
`artifact_sha256` binds 24 artifacts and its `context_clarifications` binds the
seven immutable application records. [render-manifest.json](render-manifest.json)
defines the 72 current render paths; the freeze manifest supplies byte hashes for
that exact list. It adds only supporting evidence and reproduction dependencies,
without replacing those inventories or rewriting their historical bindings.

The final [creator export](creator-final-qa-2026-11-19/creator-export.json), its
[application table](creator-final-qa-2026-11-19/README.md), the
[reconciliation](creator-final-qa-2026-11-19/RECONCILIATION.md), original QA dataset
and viewer, and active addendum are hash-bound. Seven applications are verified:
`0002` medical context, `0006` communication context, `0009` shopping context,
`0030` parking context, `0028` preferred variant, `0025` Corpus-only, and `0066`
timetable. Their original records and before/after hashes remain unchanged.

- `pcd-v01-0025` is **CORPUS_ONLY**, absent from the Dictionary. Its original
  HERE + NO evidence remains in Corpus `clh-v01-0044`.
- `pcd-v01-0028` retains all three accepted contextual forms; `move_feet` is
  preferred for its **WAYFINDING / road-sign** context, not universally.
- `pcd-v01-0065` asks arrival time: `move_public + time + punct_question`.
- `pcd-v01-0066` is the separate timetable entry:
  `move_public + media_text + time + punct_question`.

## Status chronology and boundaries

The dated reconciliation records the state before S01.18/S01.19. Its known PR1
comm_sound wording discrepancy was resolved in `97da4a6882121a2cb6abba8cd658e99cc3105191`;
PR2 current Viewer wording was resolved in the source revision above. These two
known blockers are absent in this snapshot; this is not a public-release approval.
The current Viewer presents arrival-time and timetable as separate entries and
retains the superseded source note in History. The reader reports the applied
timetable separately from its preserved raw source record.

Generated phase labels such as “awaiting final visual QA” in the package README
and manifest, and “NOT PERFORMED” in earlier receipts/reconciliation, describe
their original stages. They are preserved for exact regeneration; this dated
record states the subsequent freeze and completed reconciliation. The original
creator decision statuses are not rewritten by applying their corrections.

Frozen scope is the identified Dictionary data, its existing artifact inventory,
current renders and supporting evidence. Required Corpus, registries, primitive
assets, profiles and code are pinned as reproduction dependencies; this does not
freeze those entire projects or the repository. No IDs, meanings, Messages,
variants, SVGs, historical QA, creator exports, Corpus or application records
were changed by this pass. Full browser visual inspection and deployment are not
verified. Practical coverage, Color Modifier, Translator/API/MCP, comprehension
testing and publication are outside this freeze.

Future changes require a distinct revision or a new baseline version. Preserve
this source-revision snapshot; do not silently alter its meaning or replace its
hashes. No tag, push or release accompanies this record.

## Reproduce and verify

Use an unmodified checkout of the source revision, retaining these freeze records
separately, or this freeze commit whose underlying data and generator are identical.
Install the existing `requirements.txt` in an isolated Python environment. From
the repository root, the existing reproducibility test builds twice in separate
temporary directories and compares all **95 generated files** byte-for-byte to
each other and to the checked-in artifacts:

```sh
python -m pip install -r requirements.txt
python -m unittest tests.test_composition_dictionary_baseline_v0_1.CompositionDictionaryBaselineTests.test_outputs_are_reproducible -q
```

For a manual build, create a new output directory, copy this package's original
`creator-review-export.json` into it, then run the existing generator:

```sh
python tools/research/build_composition_dictionary_baseline_v0_1.py --output-dir /path/to/new-output
```

At freeze, **79 tests PASS** using the exact command recorded in the machine
manifest: Lexicon/Composer compatibility, Renderer, Dictionary, Messages/SVG,
final QA/snapshot migration, reader, replica-package and actual Viewer JavaScript
in a Node DOM fixture. Two independent builds and an additional audited build
matched all 95 generated files. All 24 artifact hashes and the complete seven-step
application chain passed. The frozen inputs were byte-identical to the source
revision, and `git diff --check` passed. Canonical rendering checks do not replace
author visual QA or a full browser visual check.

To check recorded bytes, compute SHA-256 for each relative file in
`data_sha256`, `canonical_render_inventory.files_sha256`, `provenance_sha256` and
`reproduction.source_files_sha256`, plus the two inventory files. Then verify
the existing manifest's `artifact_sha256` and `context_clarifications`. The render
hash keys must equal the paths in `render-manifest.json` `/renders`; do not infer
replacement assets or update a mismatch automatically.
