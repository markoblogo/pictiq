# Tools

## validate_lexicon.py

Validates:
- all ids in `packs/universal-core.json` and `packs/universal-v1.json` exist in `lexicon/icon-index.json`
- lexicon ids are unique
- required fields exist and `type` is one of: `icon`, `operator`
- if `lexicon/i18n/` exists: every `strings.<id>` in `*.json` (except `i18n.schema.json`) must exist in lexicon IDs, and each `strings.<id>` value must be an object

Run:

```bash
python3 tools/validate_lexicon.py
```

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
