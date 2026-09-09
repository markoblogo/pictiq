# Numeric Notation

Status: **ACCEPTED MECHANISM / PARTIAL IMPLEMENTATION** after Road & Public Wayfinding Stress Test 02.

Numeric notation solves exact numeric representation. It coexists with the pragmatic quantity tiles `qty_1`, `qty_2`, `qty_5`, `qty_plus`, and `qty_minus`, which remain for small practical quantities and approximate requests such as more/less.

## Architecture

Numeric notation is a shared notation layer, not ordinary lexical vocabulary. It is not a context-pack-owned primitive and it does not create one lexical concept per number.

Current implementation:

- registry: [`../notation/numeric/index.json`](../notation/numeric/index.json)
- digit assets: `notation/numeric/svg/digit_0.svg`, `notation/numeric/svg/digit_5.svg`
- first composed rendering: `notation/numeric/svg/number_50.svg`

The first implementation includes only the digits needed to reproduce the accepted `50` reference. Digits `1`, `2`, `3`, `4`, `6`, `7`, `8`, and `9` remain future work. Mathematical operators such as `%`, `×`, `÷`, `√`, and decimal separators are not implemented.

## Composition

A number is composed from digit assets in left-to-right order inside the numeric notation rendering. For example, `50` is composed as `digit_5 + digit_0` in `number_50.svg`.

This is separate from Pictiq phrase grammar. A Road context can use numeric notation inside an established speed-limit convention, while a retail context can use the same digit layer for prices.

## Relationship to `qty_*`

`qty_1`, `qty_2`, and `qty_5` express simple practical quantities. Consecutive numeric quantity tiles are additive under [Grammar](GRAMMAR.md): `qty_5 + qty_5` means ten, not fifty.

Numeric notation expresses exact written numbers. `50`, `120`, and `2026` should be represented through digit notation when those digits exist. Numeric notation MUST NOT silently replace or redefine the current quantity operators.

## Context-pack rule

Context packs select and reuse notation mechanisms; they do not own them exclusively. Road, accounting, retail, science, measurement, timetable, and time contexts may all reference the same numeric layer.
