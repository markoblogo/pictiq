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
