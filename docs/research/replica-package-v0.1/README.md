# Replica package v0.1 — one fixed Dictionary variant

This local research format contains exactly the three generated files `message.json`, `render.svg`, `manifest.json`. It is not a new Message Schema, publishing approval or Composer feature.

## Commands

From the repository root, build into a **new** directory:

```bash
python tools/replica_package.py build --entry-id pcd-v01-0006 --variant-id pcd-v01-0006-preferred --output /tmp/pictiq-less-noise-replica
python tools/replica_package.py verify /tmp/pictiq-less-noise-replica
python tools/replica_package.py verify docs/research/replica-package-v0.1/examples/less-noise
```

The last command checks the committed [example](examples/less-noise/manifest.json). Existing output directories, including empty ones, are refused. Invalid input is rejected before publishing a complete package. Commands return JSON and a nonzero exit code on failure. No external Python package is needed beyond the existing Renderer/validation source and the standard library.

## Exact selected source

- Dictionary entry: `pcd-v01-0006` — Less noise, please.
- Variant: `pcd-v01-0006-preferred`, **not** the alternatives/contextual variants.
- Source: `docs/research/composition-dictionary-baseline-v0.1/dictionary.json`.
- Variant selector: `/entries/5/variants/0`; Message selector: `/entries/5/variants/0/message`.
- Exact token order: `comm_sound + qty_minus`.
- Actual Corpus lineage: `clc-v01-0008-r1`.
- Recorded creator decision: `creator-review-export.json`, `/records/5`, `KEEP_IN_DICTIONARY`; its original notes are preserved. No new approval date is inferred.

The source was inspected with `tools/read_composition.py` (K04) and the explicit variant/creator-review lineage. The builder resolves these IDs uniquely and reads the selected Message once. It does not translate the English label, reconstruct from token_sequence, bundle the other three variants, or use a normalized Message in place of the original.

## Bindings and review boundary

The manifest records package ID and format version, a reference Git revision, source IDs/selectors/data hashes, creator-decision source and exact record, selected variant/context limitations, Corpus lineage, overall Dictionary QA status, active later decisions when linked, artifact hashes, existing render options, and actual implementation/registry/asset hashes.

Git HEAD is informational; hashes come from actual working-tree bytes, including local modifications. The example's reference revision is `34366fc7396f49e40d5235b3a3cc897550b8ea92` (HEAD during assembly), while newly added builder source is independently hashed. Verification does not require current HEAD to equal that revision. No current time or absolute output path is included. Same source bytes and revision produce identical files in different directories.

The manifest retains **AWAITING FINAL VISUAL QA** from the Dictionary. Both `review_status.new_render` and `review_status.final_placement` are **NOT_REVIEWED**. Original creator acceptance does not approve this new render, an illustration/video placement, a speaker, panel, timing, or use in another context. Such fields are not invented.

The SVG embeds canonical artwork and uses internal references; it can be opened after moving the package without fetching icon files from the repository. Reverification still needs the exact source/implementation/registry/asset versions: missing or changed inputs fail explicitly, and the manifest is never automatically rewritten. Verification checks artifact hashes **and** reproduces the selected source Message, canonical SVG and full manifest, so rehashing an inconsistent Message/SVG does not make the package valid. This is an integrity/reproduction check, not creator visual QA.

## Tests

```bash
python -m unittest tests.test_replica_package -q
```

Tests use temporary output directories and copied/memory fixture inputs. They cover reproducibility, exact source/decision binding, frame/token/parameter/profile/context preservation, relocation/self-contained SVG, corruption, rehashed mismatches, unknown variants, invalid Messages, overwrite refusal, real local asset hashes, unavailable input versions, unchanged source bytes and the example/CLI.
