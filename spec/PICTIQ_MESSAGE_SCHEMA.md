# Pictiq Message Format v0.1

> Status: specification-only  
> Message Schema version: `0.1`  
> Target Pictiq language/protocol version: `1.1`  
> Machine schema: [`pictiq-message.schema.json`](pictiq-message.schema.json)

## Purpose

Pictiq Message Format v0.1 defines the stable semantic interchange object that future renderer, generator API, Composer, website, translators, tests, books, research tools, analytics, and back-interpretation tools can share.

The renderer does not translate natural language. It receives an already specified Pictiq message and renders it deterministically.

## Architectural model

AUTHORING / EXTERNAL INPUT

-> Pictiq Shorthand or JSON

-> PARSER / NORMALIZER

-> Canonical Pictiq Message

-> VALIDATOR

-> RENDERER

-> SVG / PNG / HTML / future outputs

Other systems may consume Canonical Pictiq Message directly: Composer, analytics, back-interpretation tools, AI translators, research tooling, generators, and tests.

## Versioning decision

Pictiq v1.1.0 is the current public language milestone. Message Format v0.1 records the target language compatibility as `"pictiq": "1.1"`, meaning the Pictiq 1.1 language/protocol family. The message schema has its own `"schema": "0.1"` value. Future renderer implementations will have their own independent version.

These versions are separate because a schema can gain validation or metadata fields without changing the language, and the language can gain vocabulary or profiles without changing the interchange shape.

## Canonical document shape

```json
{
  "schema": "0.1",
  "pictiq": "1.1",
  "profile": "standalone",
  "contexts": ["narrative"],
  "frames": [
    {
      "tokens": [
        { "type": "entity", "id": "entity:poseidon@odyssey" },
        { "type": "icon", "id": "qual_bad" }
      ]
    }
  ]
}
```

A document contains:

- schema version;
- target Pictiq language/protocol version;
- optional profile declaration;
- optional ordered context declarations;
- ordered frames.

## Frame model

A v0.1 frame is deliberately simple:

```json
{
  "tokens": []
}
```

For valid interchange examples, frames should contain at least one token. A frame is a flat ordered token sequence. v0.1 does not introduce subject, predicate, object, syntax trees, semantic graphs, nested groups, brackets, explicit causality, or arbitrary 2D semantic positioning.

Grouping is `DEFERRED / FUTURE LANGUAGE PRESSURE`. Odyssey and poetry/spatial-composition work may later produce evidence for grouping or 2D semantic layout, but no normative grouping grammar has been accepted.

## Token model

Each token has an explicit `type`. Consumers must not infer every token type solely from ID syntax.

Supported v0.1 token types:

- `icon`
- `entity`
- `number`

### Icon token

```json
{
  "type": "icon",
  "id": "action_conflict"
}
```

The `id` must resolve to an active ordinary canonical Pictiq concept in [`../lexicon/icon-index.json`](../lexicon/icon-index.json). Semantic glosses are not embedded in every message; the Canonical Registry remains the semantic source of truth.

### Entity token

```json
{
  "type": "entity",
  "id": "entity:poseidon@odyssey"
}
```

The `id` must resolve through [`../entities/entity-index.json`](../entities/entity-index.json). Entity Symbols remain semantically distinct from ordinary lexical primitives. Rendering may use similar tile mechanics, but registries must not be merged.

### Number token

```json
{
  "type": "number",
  "value": 50
}
```

Numbers are not ordinary canonical lexical icons. A renderer should use [`NUMERIC_NOTATION.md`](NUMERIC_NOTATION.md) and [`../notation/numeric/index.json`](../notation/numeric/index.json). Do not create `qty_50`, `qty_2026`, or one lexical concept per number.

Schema v0.1 permits non-negative integer values up to 9999 as a syntactic number token. Registry-aware semantic validation is narrower: the current numeric notation layer has implemented digits `0` and `5` and the composed rendering `50`. Values requiring unimplemented digits are future semantic validation errors, not ordinary lexicon gaps.

### Parameterized icon token

```json
{
  "type": "icon",
  "id": "nature_cloud",
  "params": {
    "color": "#555555"
  }
}
```

`params.color` is a token-local COLOR parameter represented as a six-digit sRGB hex string. It applies to the icon token itself. This differs from adding a neighboring lexical color tile. It follows the existing [`PARAMETRIC_COLOR.md`](PARAMETRIC_COLOR.md) prototype and does not create lexical DARK, GREY, RED, or other color tiles.

Unknown parameters must be rejected explicitly.

## Profile treatment

A document may optionally declare a profile such as `"standalone"`, `"embodied"`, `"standalone-core-v0.1"`, or `"embodied-core-v0.1"`.

Profile is useful for validation, Composer palettes, authoring guidance, and interpretation context. Profile membership does not determine whether a valid canonical SVG exists. A renderer should not necessarily refuse to render an otherwise valid canonical concept merely because it falls outside the declared profile. A future validator may report `profile-mismatch` warnings or errors according to policy.

## Context and pack treatment

A document may optionally declare contexts or pack-like environments such as `"narrative"`, `"odyssey"`, `"universal-core"`, `"universal-v1"`, `"city-paris-v0.1"`, or `"road-wayfinding-v0.1"`.

Contexts/packs guide authoring palette, validation, interpretation, provenance, and future translation. They do not embed entire pack definitions into the message.

A Context Pack controls vocabulary availability or recommendation, not the existence of the canonical concept itself.

## Semantic message vs presentation

The canonical Pictiq Message normally does not contain:

- pixel coordinates;
- tile size;
- gaps;
- page dimensions;
- colors of frames/backgrounds;
- output format;
- book layout;
- poster layout.

Those belong to a separate Render Request. One semantic message should be renderable as a compact row, multiple rows, book illustration, mobile UI, poster, SVG, PNG, or HTML without changing the semantic message.

## Render Request v0.1 direction, not implementation

A future render request may wrap a message with output and options:

```json
{
  "message": { "schema": "0.1", "pictiq": "1.1", "frames": [] },
  "output": "svg",
  "options": {
    "tileSize": 64,
    "gap": 8,
    "frameGap": 20,
    "direction": "ltr"
  }
}
```

Likely first output targets are SVG, PNG, HTML, and normalized JSON. PDF may remain future work. This task does not implement any renderer or output generation.

## Determinism

For the same canonical semantic message, Pictiq/registry version, renderer version, and render options, a renderer should produce the same semantic output structure and visually equivalent rendering. Byte-identical output across unrelated rendering engines is not promised unless a future implementation explicitly enforces it.

## Normalization report model

A future parser/normalizer should return a normalized canonical message plus warnings or errors:

```json
{
  "message": {
    "schema": "0.1",
    "pictiq": "1.1",
    "frames": [
      {
        "tokens": [
          { "type": "icon", "id": "drink_alcohol" }
        ]
      }
    ]
  },
  "warnings": [
    {
      "type": "legacy-id",
      "input": "need_bar",
      "normalizedTo": "drink_alcohol"
    }
  ]
}
```

Conservative v0.1 warning/error categories:

- `legacy-id`
- `unknown-id`
- `ambiguous-entity`
- `unsupported-parameter`
- `invalid-number`
- `profile-mismatch`
- `context-mismatch`
- `malformed-directive`
- `illegal-grouping`

Parsing, normalization, validation, and rendering should fail loudly. They must not silently substitute a similar icon for an unknown ID, ambiguous entity, unsupported parameter, or invalid numeric notation. Fuzzy/AI translation belongs upstream of canonical message creation.

## Relationship to AI and poetry

A future AI translator pipeline should be:

natural language -> semantic decomposition -> Pictiq concept selection -> composition -> canonical Pictiq Message JSON -> validation -> renderer

The renderer remains non-fuzzy and deterministic.

Pictiq Poetry / Visual Prosody is a post-Composer research track. Message Schema v0.1 is not distorted to support poetry-specific spatial layout. If poetry later proves that 2D semantic arrangement is required, that becomes evidence for a future schema/language extension.
