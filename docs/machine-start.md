# Machine reading start guide

This is a static navigator for data and local CLI tools in the current checkout. The **Composition Dictionary v0.1 is a research baseline awaiting final creator visual QA**. The reader and replica-package tools exist locally; this guide does not provide a public API/MCP, Translator, or Composer packaging integration. This new document is prepared locally; its public URL is not asserted live before push/deployment.

Paths shown below are relative to the repository root. Markdown links resolve relative to this file in `docs/`.

## Sources and limits

| Source (repository-root path) | Role and limit |
| --- | --- |
| [lexicon/icon-index.json](../lexicon/icon-index.json), [lexicon/icon-index.schema.json](../lexicon/icon-index.schema.json) | Ordinary canonical IDs and primitive/sign metadata; not reusable compositions or proof of comprehension. |
| [entities/entity-index.json](../entities/entity-index.json) | Separate named Entity Symbols; resolve an exact ID through its registry entry and `icon_path`. Do not use the ordinary-icon path template for entities. |
| [spec/pictiq-message.schema.json](../spec/pictiq-message.schema.json), [spec/PICTIQ_MESSAGE_SCHEMA.md](../spec/PICTIQ_MESSAGE_SCHEMA.md) | Message structure and format documentation; valid structure does not certify semantics or placement. |
| [docs/research/composition-dictionary-baseline-v0.1/dictionary.json](research/composition-dictionary-baseline-v0.1/dictionary.json), [docs/research/composition-dictionary-baseline-v0.1/manifest.json](research/composition-dictionary-baseline-v0.1/manifest.json) | Exact reusable semantic units and variants, package QA status and source/hash bindings. The package still awaits final visual QA, even where a variant has `CURRENT_ACCEPTED` metadata. |
| [docs/research/composition-dictionary-baseline-v0.1/final-creator-qa-addendum-v0.2.json](research/composition-dictionary-baseline-v0.1/final-creator-qa-addendum-v0.2.json) | Active later creator decisions, still `PENDING_BASELINE_APPLICATION`. Validate `source_dictionary_baseline` against the exact baseline; never substitute an archived copy or apply decisions during reading. |
| [docs/research/composition-dictionary-baseline-v0.1/creator-review-export.json](research/composition-dictionary-baseline-v0.1/creator-review-export.json) | Recorded source review referenced by the Dictionary manifest/lineage; earlier review and later pending decisions remain separate. |
| [docs/research/composition-library-baseline-v0.1/accepted-corpus.json](research/composition-library-baseline-v0.1/accepted-corpus.json), [docs/research/composition-library-baseline-v0.1/manifest.json](research/composition-library-baseline-v0.1/manifest.json) | Broader evidence, retained historical forms and replacements, with reconciliation/compatibility limitations. Resolve actual `corpus_record_id` through explicit links; do not assume it equals a Harvest ID. |
| [docs/research/composition-dictionary-baseline-v0.1/renders/](research/composition-dictionary-baseline-v0.1/renders/), [docs/research/composition-library-baseline-v0.1/renders/](research/composition-library-baseline-v0.1/renders/), [docs/research/composition-library-historical-harvest-v0.1/renders/](research/composition-library-historical-harvest-v0.1/renders/) | Saved illustrations of messages. Follow the exact record/manifest/review-data render links; a saved historical render does not establish current registry validity. |
| [icons/svg/](../icons/svg/), [entities/entity-index.json](../entities/entity-index.json), [notation/numeric/index.json](../notation/numeric/index.json) | Ordinary icons use `icons/svg/<canonical-id>.svg` after registry lookup. Entities use `icon_path`; implemented numbers use the numeric entry's `svg` path. No common path rule covers every token type. |
| [tools/read_composition.py](../tools/read_composition.py), [tools/README.md](../tools/README.md) (K04 instructions) | Read Dictionary/Corpus by explicit source and ID, with raw records, pending decisions, status boundaries, render/asset references, selectors and actual file hashes. No fallback to another dataset. |
| [tools/replica_package.py](../tools/replica_package.py), [docs/research/replica-package-v0.1/README.md](research/replica-package-v0.1/README.md), [docs/research/replica-package-v0.1/examples/less-noise/manifest.json](research/replica-package-v0.1/examples/less-noise/manifest.json) | Build/verify one explicitly selected Message variant. The package binds exact inputs and canonical render; new render and final placement remain `NOT_REVIEWED`. Follow the existing K06 instructions for commands. |

## Reading rules

- Keep the original baseline, package-wide QA status, entry metadata and subsequent pending creator decisions separate. An absent pending action or reader exit 0 / `ok: true` is not semantic approval or completed QA.
- Prefer K04 for ID lookup. For direct Dictionary JSON reads, also read its **manifest**, the **active addendum and its baseline binding**, the **creator export referenced by manifest/lineage**, and **Corpus data plus its manifest** through explicit lineage. For Corpus reads, retain reconciliation/compatibility status and inspect any linked Dictionary and active addendum. Reject ambiguous or incompatible links rather than guessing.
- Take the exact Message from one explicitly selected variant, retaining frames, token order, parameters, profile/contexts and its context/limitations. Do not reconstruct it from English or token_sequence; acceptance in one context grants no new-context approval.
- Keep an absent historical ID unresolved; do not replace it with a modern token. Check saved render availability separately from current canonical asset availability.
- Use existing canonical assets and Renderer output. Do not redraw canonical signs with a generative image model. Package verification is integrity/reproduction checking, not creator visual QA.

## Three documented reading routes

Run from the repository root:

```bash
python tools/read_composition.py --source dictionary --id pcd-v01-0006
python tools/read_composition.py --source dictionary --id pcd-v01-0025
python tools/read_composition.py --source corpus --id clh-v01-0015
```

- `pcd-v01-0006`: Less noise, please. The source variants are preserved; package-wide final visual QA remains outstanding. Select the exact `variant_id` before using a Message/render.
- `pcd-v01-0025`: the original baseline is still present, alongside subsequent `MOVE_TO_CORPUS_ONLY` pending application. It is not an unconditional current recommendation.
- `clh-v01-0015`: confirmed Corpus record linked to the historical hotel example. Its Message keeps `place_hotel`; the saved historical render exists, but that token is absent from the current canonical registry.

For an exact packaged variant, continue to the [K06 build/verification instructions](research/replica-package-v0.1/README.md). Obtain hashes and selectors at runtime from reader/packager output, not copied values in this guide.

These routes are a **documented reading-route check**, not a blind agent discovery test or an independent AI comprehension test. Local link validation does not prove a new public URL is deployed. Existing usage terms remain in [LICENSE](https://github.com/markoblogo/pictiq/blob/main/LICENSE) and [Commercial License (Draft)](https://github.com/markoblogo/pictiq/blob/main/COMMERCIAL_LICENSE.md); discoverability does not add permissions.
