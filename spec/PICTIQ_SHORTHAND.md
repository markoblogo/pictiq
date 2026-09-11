# Pictiq Shorthand v0.1

> Status: human authoring format / specification-only  
> Canonical storage: [Pictiq Message Format v0.1](PICTIQ_MESSAGE_SCHEMA.md) JSON  
> Rule: shorthand is parsed and normalized into canonical JSON; it is not the canonical semantic storage format.

## Purpose

Pictiq Shorthand v0.1 is a small deterministic authoring syntax for humans, examples, books, tests, and future Composer text input. It is not natural language and does not introduce aliases beyond the current repository architecture.

## Basic parsing model

- One non-empty content line becomes one frame.
- Multiple whitespace-separated units on a line become the ordered tokens for that frame.
- Blank lines are ignored.
- Leading and trailing whitespace is ignored.
- Consecutive spaces or tabs are treated as one separator.
- Line endings are normalized to LF before parsing.
- A line beginning with `#` is a comment and is ignored.
- Inline comments are not supported in v0.1.

## Directives

Directives are optional and appear before content frames.

```text
!profile standalone
!context narrative
!context odyssey
```

Supported v0.1 directives:

- `!profile VALUE`
- `!context VALUE`

Multiple `!context` lines append contexts in input order, with duplicates removed during normalization. Unknown profile/context values must produce `profile-mismatch` or `context-mismatch` rather than being silently accepted.

Malformed directives produce `malformed-directive`.

## Ordinary icon units

A bare canonical ordinary ID becomes an icon token:

```text
action_conflict
```

Normalizes to:

```json
{ "type": "icon", "id": "action_conflict" }
```

Multiple units form one frame:

```text
action_conflict nature_animal logic_no
```

New normalized JSON must store preferred current IDs. Legacy IDs supported by compatibility metadata are accepted as input but normalized.

Example:

```text
need_bar
```

Normalizes to:

```json
{ "type": "icon", "id": "drink_alcohol" }
```

with a `legacy-id` warning.

## Entity units

Short entity syntax uses `@name` when the declared context makes the resolution unambiguous.

```text
!context odyssey
@poseidon qual_bad power_energy @odysseus
```

In Odyssey context, `@poseidon` resolves to `entity:poseidon@odyssey`. If a short entity name is ambiguous or unknown, the parser must not guess.

Full entity IDs may be written explicitly:

```text
entity:poseidon@odyssey
entity:polyphemus@odyssey
entity:odysseus@literary
```

Examples using current registry IDs:

- `@odysseus` may resolve to `entity:odysseus@literary` when unambiguous in the declared narrative/literary context.
- `@poseidon` may resolve to `entity:poseidon@odyssey` when `!context odyssey` is declared.
- `@polyphemus` may resolve to `entity:polyphemus@odyssey` when `!context odyssey` is declared.

## Number units

A decimal numeric literal becomes a number token:

```text
50
```

Normalizes to:

```json
{ "type": "number", "value": 50 }
```

Numeric literals are not lexical `qty_*` IDs. The current numeric notation layer only implements the digits and composed rendering needed for `50`; other syntactically valid integer literals may still fail registry-aware semantic validation until the digit set expands.

## Parameter units

A parameterized icon uses a compact brace syntax:

```text
nature_cloud{color:#555555}
```

Normalizes to:

```json
{
  "type": "icon",
  "id": "nature_cloud",
  "params": {
    "color": "#555555"
  }
}
```

v0.1 supports only `color` as a six-digit sRGB hex value. Unknown parameters and malformed color values must be rejected explicitly.

## No grouping in v0.1

Shorthand v0.1 has no brackets, nested groups, syntax trees, semantic graphs, causality markers, or 2D semantic layout. Each non-empty content line is one flat frame.

Illegal grouping-like input should produce `illegal-grouping` or a syntax error. Future Odyssey, poetry, UI, or spatial-composition evidence may justify a later extension; it is not part of v0.1.

## Example shorthand document

```text
!profile standalone
!context odyssey

@poseidon qual_bad power_energy @odysseus
@odysseus place_home logic_no
move_watercraft 50 punct_exclaim
nature_cloud{color:#555555}
```

The normalized message contains four frames and explicit typed tokens. Any renderer receives the normalized JSON, not the raw shorthand.
