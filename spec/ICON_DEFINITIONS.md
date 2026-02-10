# Pictiq Icon Definitions & Design Brief

This document is a designer/developer brief: what each icon means and how it should look.
Important: the repository only accepts SVG icons with no `<text>` elements. If a font is used as a drafting tool for `? ! + - I II IIIII`, it must be converted to curves and manually normalized before committing.

## 0. Style
- SVG, viewBox `0 0 32 32`.
- Mandatory rounded-square tile frame.
- Inner shapes do not touch the frame, except `logic_no`.
- Monochrome via `currentColor`, no hardcoded colors/gradients.
- Filled silhouettes, no shadows, no halftones.

## 1. Font-as-draft (before converting to curves)
Allowed only as a drafting method for:
`punct_question`, `punct_exclaim`, `qty_plus`, `qty_minus`, `qty_1/2/5`.

Draft font: **Inter Bold**.
Final SVG: curves/paths only, no `<text>`.

Geometry notes:
- `qty_plus` must be visibly thinner/lighter than `safety_medical` (medical cross).
- Roman strokes are equal thickness with equal spacing.
- Punctuation symbols are large and centered.

## 2. Definitions (core examples)
- `punct_question`: a large `?` symbol centered inside the tile.
- `punct_exclaim`: a large `!` symbol centered inside the tile.
- `logic_yes`: a check mark.
- `logic_no`: a single diagonal slash `/` (top-right to bottom-left), 2–3× the frame stroke thickness.
- Fixed negations (context packs only): an object icon with the same `logic_no` slash over it.

(Then list the remaining core icons exactly as in RU brief: time, qty, money, comm, needs, safety, places, movement.)
