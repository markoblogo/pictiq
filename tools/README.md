# Tools

## validate_lexicon.py

Validates:
- all ids in packs and `layouts/profiles/*.json` exist in `lexicon/icon-index.json`
- profile groups have no duplicates, have matching SVGs, and wallet-card selections fit their capacities
- lexicon ids are unique
- required fields exist and `type` is one of: `icon`, `operator`
- if `lexicon/i18n/` exists: every `strings.<id>` in `*.json` (except `i18n.schema.json`) must exist in lexicon IDs, and each `strings.<id>` value must be an object

Run:

```bash
python3 tools/validate_lexicon.py
```

## make_wallet_card.py

Renders print-resolution, two-sided wallet-card assets from a content profile. The profile can declare documented wallet-only exclusions when a physical card capacity differs from the complete profile.

```bash
python3 tools/make_wallet_card.py --profile paris
```

## make_lighter.py

Renders the two broad faces of a disposable lighter from the optional `lighter` block in a content profile.

```bash
python3 tools/make_lighter.py --profile nightlife
```

## generate_template.py

Generates canonical tile template SVG:
- `templates/tile-template.svg`

Output characteristics:
- `viewBox="0 0 32 32"`
- frame stroke `currentColor`, `stroke-width="2"`, `fill="none"`
- rounded corners `rx=ry=4.8`
- hidden guides group with safe-area and centering lines

Run:

```bash
python3 tools/generate_template.py
```

## build_icon_from_silhouette.py

Builds a canonical tile SVG from a silhouette PNG.

Run:

```bash
python3 tools/build_icon_from_silhouette.py --id <icon_id> --input <silhouette.png> --out <output.svg>
```

Example:

```bash
python3 tools/build_icon_from_silhouette.py --id logic_yes --input inputs/silhouettes/logic_yes.png --out icons/svg/logic_yes.svg
```

Vectorization backend:
- Prefer `potrace` CLI
- Fallback: `inkscape` CLI trace mode
- If neither is installed, the script exits with a clear error

Install recommendations:
- `potrace` (recommended): install via your package manager (for example `brew install potrace`)
- `inkscape` (fallback): install Inkscape and ensure `inkscape` is available in `PATH`

## render_png.py

Renders `icons/svg/{id}.svg` into PNG variants:
- `icons/png/black/{id}.png`
- `icons/png/white/{id}.png`

Default output size preset:
- 2400x3200 (baseline “apparel/classic tote” size)

Run:

```bash
python3 tools/render_png.py
```

Dry run:

```bash
python3 tools/render_png.py --dry-run
```

### Requirements

One of the following renderers must be available:

1) CairoSVG (preferred)
- Install: `pip install cairosvg`
- Note: CairoSVG may require native libraries depending on your OS (for example Cairo/Pango).

2) Inkscape CLI (fallback)
- Install Inkscape and ensure `inkscape` is on your `PATH`.

### Authoring requirement (for black/white variants)

To render black/white variants reliably, SVGs should use `currentColor` for `fill`/`stroke`.
The renderer injects `style=\"color: #000000\"` (black) or `style=\"color: #ffffff\"` (white) onto the root `<svg>`.

## validate_vocabulary_classification.py

Validates `lexicon/vocabulary-classification.json` against the ordinary canonical lexicon and separate entity registry:
- every ordinary canonical ID appears exactly once
- no entity-symbol IDs appear in vocabulary classification
- role, relevance, confidence, and context values come from controlled lists
- required classification fields are present

Run:

```bash
python3 tools/validate_vocabulary_classification.py
```

## validate_numeric_notation.py

Validates `notation/numeric/index.json` and numeric SVG assets:
- implemented digit assets exist and use path geometry, not SVG `<text>`
- composed number renderings match their digit composition
- numeric renderings keep `viewBox="0 0 32 32"` and canonical paint constraints

Run:

```bash
python3 tools/validate_numeric_notation.py
```

## validate_svg.py

Validates canonical icons in `icons/svg/` (ignores `.gitkeep`):
- `viewBox` equivalent to `0 0 32 32`
- no SVG `<text>` elements / no `<text` in canonical SVGs (icons must be curves/paths only)
- no hardcoded colors in `fill`/`stroke` attributes or inline `style`
  Allowed paint values: `currentColor`, `none`, empty
- flags usage of `#...`, `rgb()/rgba()`, and named colors `black`/`white`

Run:

```bash
python3 tools/validate_svg.py
```

## validate_entities.py

Validates scoped entity symbols separately from the ordinary Core lexicon:
- every `entities/entity-index.json` symbol has a namespaced `entity:...@namespace` ID
- accepted entity types currently include `person` and `mythological_entity`
- no entity ID collides with `lexicon/icon-index.json`
- each symbol records namespace, aliases, authority, provenance, status, source crop, and SVG path
- each entity SVG follows the same canonical SVG constraints as ordinary icons

Run:

```bash
python3 tools/validate_entities.py
```

Entity symbols live under `entities/` and are not added to `icons/svg/`, packs, or Core profiles unless a future context/profile explicitly references them.

## make_icon_qa_sheet.py

Prepares a deterministic, self-contained HTML sheet with original canonical SVGs
embedded as isolated images: canonical, small-size and comparison-grid renders,
plus an optional existing PNG/JPEG layout. Python standard library only; open the
result in a browser to render it. Same source bytes/options produce identical HTML;
actual pixels can vary by browser/display. Generated sheets are ignored in `build/qa/`.

```bash
python3 tools/make_icon_qa_sheet.py item_cannabis
python3 tools/make_icon_qa_sheet.py item_cannabis --small-px 16 --neighbors item_cigarette nature_flower
python3 tools/make_icon_qa_sheet.py paris_eiffel_tower --layout docs/merch/paris-shirt-preview-1200x1600.png
python3 -m unittest discover -s tests -v
```

Open `build/qa/<icon_id>.html`. Default grid neighbors are selected deterministically,
favoring the same category; reviewers should supply plausible confusion pairs.
Review size options are illustrative CSS pixels, not normative geometry. Check at
100% zoom and verify physical layouts at actual size/distance separately. The tool
does not alter profile/layout selections or verify that a supplied layout contains
the target icon. Reviewers must check this. Labels are concealed until expanded.

Follow the [Visual QA Protocol](../spec/ICON_SPEC.md#visual-qa-protocol) and record
results in the change/PR. A missing required layout remains pending. Generating a
sheet is neither an automated recognition test nor perceptual acceptance. Run both
structural validators independently before visual QA.

## validate_message_schema.py

Validates Pictiq Message Format v0.1 JSON fixtures against the local schema shape and current registries. It does not implement Shorthand parsing, rendering, Composer, or AI translation.

```bash
python3 tools/validate_message_schema.py
```


## pictiq_render.py

Renders or normalizes Pictiq Message Format v0.1 JSON and Pictiq Shorthand v0.1 inputs. The renderer uses current repository registries and canonical SVG assets; it does not translate natural language, infer missing vocabulary, group tokens, or choose semantic layout.

```bash
python3 tools/pictiq_render.py render examples/renderer/basic-water-question.pictiq --output build/qa/renderer-v0.1/basic-water-question.svg
python3 tools/pictiq_render.py normalize examples/renderer/legacy-normalization.pictiq --output build/qa/renderer-v0.1/legacy-normalization.normalized.json
```

Diagnostics are emitted as JSON lines on stderr. Errors stop rendering; warnings preserve deterministic output.

## read_composition.py — read-only Composition Dictionary / Corpus v0.1

Run from the repository root (the script resolves data relative to its own location):

```bash
python tools/read_composition.py --source dictionary --id pcd-v01-0006
python tools/read_composition.py --source dictionary --id pcd-v01-0025
python tools/read_composition.py --source corpus --id clh-v01-0015
```

Output is JSON: the exact `baseline_record`, package QA status, explicitly linked subsequent creator decisions with application status, linked Corpus records, saved renders, current canonical asset availability, record selectors and SHA-256 of consumed files. No data is normalized or rewritten. Pending decisions are not applied; absence of a pending action does not complete Dictionary QA. Missing historical `place_hotel` stays missing in the current registry even when a saved historical render is available. Its Corpus ID is verified in `accepted-corpus.json`, not inferred from the Harvest ID.

For `pcd-v01-0002`, `pcd-v01-0006`, `pcd-v01-0009` and `pcd-v01-0030`, `applied_creator_decisions` separately reports the [S01.10 medical-context receipt](../docs/research/composition-dictionary-baseline-v0.1/applied-decisions/pcd-v01-0002-context.json), [S01.11 communication-context receipt](../docs/research/composition-dictionary-baseline-v0.1/applied-decisions/pcd-v01-0006-context.json), [S01.12 shopping-context receipt](../docs/research/composition-dictionary-baseline-v0.1/applied-decisions/pcd-v01-0009-context.json) or [S01.13 parking-context receipt](../docs/research/composition-dictionary-baseline-v0.1/applied-decisions/pcd-v01-0030-context.json), with its exact source decision. The ordered receipts verify the current Dictionary back through the unchanged S01.12, S01.11 and S01.10 results to the original Dictionary hash. Each step checks its exact descriptive-field delta and source decision; a missing, reordered or substituted intermediate link fails verification. All three earlier receipts retain their historical before/after-hashes. These are four explicit revisions, not a general snapshot migration. The historical QA export/addendum keep their original bindings; other creator decisions remain pending and package-wide QA is reported independently. K06 packages retain their historical input hashes; verification against changed current inputs reports the required version unavailable rather than rebinding the package.

Exit 0 means the record was read without contradictory links; warnings such as pending QA, historical limitations or missing assets remain in `diagnostics`. It does **not** mean semantic approval. Exit 1 reports unknown IDs/sources, incompatible bindings or ambiguous/contradictory links; no fallback dataset or replacement token is selected. Fatal follow-on link errors preserve the selected raw record when available. Only the fixed active v0.1 files and explicit ID/manifest links are used; archived copies never replace the active addendum. No browser-only QA decisions are inspected or inferred.
