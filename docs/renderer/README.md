# Pictiq Renderer v0.1

> Status: first local implementation
> Scope: deterministic rendering for already-authored Pictiq Message Format v0.1 inputs
> Non-goals: Composer, GUI, browser extension, AI translation, fuzzy matching, semantic inference, poetry generation, arbitrary 2D semantic layout, grouping, and PDF publishing

Pictiq Renderer v0.1 turns a valid Pictiq message into a flat SVG tile row. It accepts canonical JSON messages and the human shorthand syntax, normalizes legacy IDs where the compatibility registry allows migration, validates the tokens against the current registries, and renders only actual canonical Pictiq assets.

The renderer does not choose vocabulary. It does not translate natural language. It renders the message it is given.

## Inputs

Renderer v0.1 supports two input forms:

1. Pictiq Message Format v0.1 JSON, as specified in [`../../spec/PICTIQ_MESSAGE_SCHEMA.md`](../../spec/PICTIQ_MESSAGE_SCHEMA.md).
2. Pictiq Shorthand v0.1, as specified in [`../../spec/PICTIQ_SHORTHAND.md`](../../spec/PICTIQ_SHORTHAND.md).

Shorthand directives are optional:

```pictiq
!profile standalone
!context road-wayfinding-v0.1
surface_wavy punct_exclaim
50
```

The normalized message keeps the same semantic content in JSON form:

```json
{
  "schema": "0.1",
  "pictiq": "1.1",
  "profile": "standalone",
  "contexts": ["road-wayfinding-v0.1"],
  "frames": [
    { "tokens": [
      { "type": "icon", "id": "surface_wavy" },
      { "type": "icon", "id": "punct_exclaim" }
    ]},
    { "tokens": [{ "type": "number", "value": 50 }]}
  ]
}
```

## Supported token types

- `icon` — ordinary canonical IDs from `lexicon/icon-index.json`.
- `entity` — scoped Entity Symbols from `entities/entity-index.json`, either as full IDs such as `entity:poseidon@odyssey` or shorthand aliases such as `@poseidon` when unambiguous.
- `number` — currently implemented numeric notation values from `notation/numeric/index.json`; v0.1 renders `50` and rejects unsupported exact numbers loudly.

The `COLOR` parameter is supported on icon tokens through `params.color`, for example:

```json
{ "type": "icon", "id": "person_generic", "params": { "color": "#555555" } }
```

This recolors `currentColor` artwork at render time. It does not create a new lexical color icon.

## Validation behavior

Renderer validation is registry-aware and fail-loud:

- unknown icon IDs are errors;
- unknown profiles and contexts are errors;
- entity aliases are resolved only when unambiguous;
- profile/context mismatches are warnings, not fatal errors;
- unsupported parameters are errors;
- grouping and arbitrary 2D semantic layout are rejected in v0.1;
- legacy IDs migrate only when `lexicon/compatibility.json` records a semantic migration.

The current legacy migrations are:

- `need_bar` → `drink_alcohol`
- `place_hotel` → `place_home`

`move_boat` remains explicitly deferred as legacy contextual vocabulary; Renderer v0.1 does not silently convert it to `move_watercraft`.

## CLI

Render to SVG:

```bash
python3 tools/pictiq_render.py render examples/renderer/road-wayfinding.pictiq --output build/qa/renderer-v0.1/road-wayfinding.svg
```

Normalize to JSON:

```bash
python3 tools/pictiq_render.py normalize examples/renderer/legacy-normalization.pictiq --output build/qa/renderer-v0.1/legacy-normalization.normalized.json
```

Diagnostics are emitted as one JSON object per line on stderr. The rendered SVG or normalized JSON is written to the requested output path or stdout.

## Python API

```python
from pathlib import Path
from pictiq_renderer import render_file

result = render_file(Path("examples/renderer/basic-water-question.pictiq"))
svg = result["render"]["svg"]
message = result["message"]
diagnostics = result["diagnostics"]
```

## Layout model

Renderer v0.1 uses deterministic linear layout:

- one message contains ordered frames;
- one frame contains a flat ordered token sequence;
- tokens render as framed Pictiq tiles;
- frames are stacked as rows;
- no token grouping, semantic graph, or arbitrary spatial layout is inferred.

Layout options affect visual output only. They do not change the normalized semantic message.

## QA outputs

The first QA collection is generated from real renderer output in [`../../build/qa/renderer-v0.1/`](../../build/qa/renderer-v0.1/):

- `basic-water-question.svg`
- `basic-alcohol-home-no.svg`
- `legacy-normalization.svg`
- `legacy-normalization.normalized.json`
- `road-wayfinding.svg`
- `odyssey-narrative.svg`

The fixtures live in [`../../examples/renderer/`](../../examples/renderer/).

## Browser parity spike

Technical Spike 01 tested a browser-side secondary renderer for future Composer preview. The parity contract is documented in [`browser-renderer-parity.md`](browser-renderer-parity.md). The browser candidate lives in [`browser-renderer.mjs`](browser-renderer.mjs) and consumes the generated canonical asset manifest [`generated/pictiq-browser-assets.mjs`](generated/pictiq-browser-assets.mjs).

The spike verdict is `ACCEPT_WITH_GUARDRAILS`: browser rendering is viable under static GitHub Pages only when canonical data is generated from repository sources and automated parity tests compare it against Python Renderer v0.1. The spike does not implement Composer UI.
