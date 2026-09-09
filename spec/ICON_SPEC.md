# Pictiq Icon Spec

Perceptual design and acceptance workflow updated in v1.0.1; Core remains `v1.0.0-core`.

## 1. Purpose
Pictiq icons are designed for short, universal messages where language may be a barrier.
Icons must remain simple, readable, and consistent across print and digital media.

## 2. Format
- Source format: SVG
- Canonical viewBox: `0 0 32 32` (matching the existing SVG validator)
- Color: single color (black or white). No gradients, no shadows, no halftones.
- Canonical lexicon format: a framed "tile" icon (rounded-square frame) is REQUIRED for ALL lexicon icons,
  including punctuation (`?`, `!`) and logic icons (YES/NO).
- Optional export: a "raw" (no-frame) variant MAY be provided for special layouts, but it is not the canonical
  representation in the lexicon.

## 3. The Tile Frame
The rounded-square tile frame is REQUIRED for all lexicon icons.
- Corner radius: consistent across all icons
- Padding: consistent; the pictogram must not touch the frame
- Explicit note: the project logo NEVER uses the tile frame.
- The Pictiq logo is not a tile and must not use the rounded-square frame.

## 4. Stroke / Fill
Pick one approach for the entire lexicon:
- Prefer: filled silhouettes OR consistent stroke icons.
- If stroke is used:
  - define a single stroke width and keep it consistent
  - avoid thin details that break in print
- Negative space must remain open and readable.

## 5. Semantic rule
One icon = one base meaning.
If a concept needs variants, prefer composition (BASE + QUALIFIER) instead of creating many near-duplicates.

## 6. Overlays (operators)
Pictiq separates standalone logic icons from operators that can be applied to any icon.

- `logic_no` (standalone icon): means "no".
  - Definition: NOT a slashed circle. It is the tile frame itself, slashed by a bold diagonal line (no circle).
- Negation slash (visual operation): a diagonal slash across the tile that can be applied to ANY icon.
  - Meaning: no / not / forbidden / without / allergy
  - Supported UX layer: users may also draw this slash manually on printed products (for example on fabric) with a marker.

## 7. No brands / no trademarks
Icons must not include:
- logos, wordmarks, brand mascots
- trademarked shapes or distinctive brand identity elements
- names of places as brands (use generic types: "theme park", "museum", etc.)

Brands may request a dedicated icon only if rights for usage are granted to the project
and the icon still follows the "no logo/wordmark" rule unless explicitly agreed.

## 8. Naming
IDs are lowercase with underscores:
- `category_concept` (examples: `need_toilet`, `move_taxi`, `money_card`)
IDs must be stable over time.

## 9. Metadata requirement
Every icon must appear in `lexicon/icon-index.json` with:
- id
- meaning_en (short)
- aliases_en (list)
- tags_en (list)
- category
- examples (0..N) short example phrases

## 10. Acceptance / moderation
All additions go through maintainer review:
- relevance to the protocol
- style compliance
- originality (must not copy existing icons)


## Perceptual Design Principles

These principles are normative. MUST / MUST NOT indicate requirements; SHOULD indicates a recommendation whose exceptions need a documented reason; MAY indicates an option. They complement existing structural rules and do not change existing canonical geometry or impose new numerical limits in v1.0.1.

### 1. Design for the decision

An icon SHOULD preserve the information necessary for the intended recognition, decision, or action rather than pictorial completeness. Do not optimize an icon for illustration quality. The relevant question is not “Does this depict the object accurately?” but “Can the intended concept be recognized quickly enough for the intended use?”

The intended use MUST also identify whether communication is embodied or standalone. The [protocol distinction](PROTOCOL.md#11-embodied-and-standalone-communication) determines which meaning can be supplied by a present person and which must remain in the artifact.

### 2. Recognition over abstraction

Recognition SHOULD take precedence over geometric purity or stylistic abstraction. When two silhouettes are structurally valid, prefer the one recognized faster and with less ambiguity, even if it is less geometrically regular. Do not simplify a distinctive feature merely to make an icon stylistically uniform.

### 3. Minimum sufficient detail

Canonical icons SHOULD contain the minimum detail necessary for reliable recognition. Remove visual detail until further removal begins to reduce recognition, distinction, or contextual usefulness. “Minimal” does not mean the fewest possible shapes: it means the least visual information that still performs the intended communicative function.

### 4. Relative geometry

Spacing, safe areas, visual proportions, and future geometry constraints SHOULD be defined relative to the canonical tile coordinate system rather than output pixels. Canonical Pictiq SVGs use a 32×32 coordinate system:

`U = canonical tile width / 32`

Thus `1U = 1 viewBox unit` for canonical tiles. U-based measurements SHOULD be used when specifying frame geometry, safe areas, minimum spacing, silhouette margins, visual separation, and future layout constraints.

Raster output dimensions MUST NOT become normative geometry. A 32×32 SVG, 512×512 PNG, printed wallet-card tile, and shirt tile should remain representations of the same relative geometry. This release establishes the relative-unit principle; it introduces no new numerical constraints. Existing frame and safe-area rules, including the `logic_no` exception in [Protocol §2](PROTOCOL.md#2-tiles-and-frame), still apply.

### 5. Contextual validation

A canonical icon MUST NOT be considered perceptually accepted solely because its source SVG is technically valid. Icons SHOULD be evaluated under representative viewing conditions, considering at minimum a canonical render, reduced/small-size render, multi-icon grid, and representative physical or digital layout. Where relevant, also consider viewing distance: for example on a wallet card, lighter, phone screen, shirt, or in signage-like use.

An icon that passes structural validation but becomes ambiguous at its intended size MUST fail perceptual review.

### 6. System consistency over icon uniformity

Pictiq consistency SHOULD primarily come from canonical framing, safe areas, scale relationships, spacing, hierarchy, composition rules, and protocol behavior. Individual silhouettes MAY retain distinctive forms and different levels of internal complexity when those differences improve recognition. Do not force unrelated objects into identical geometric abstraction merely to create stylistic uniformity.

> Consistency is a property of the system before it is a property of the drawing.

## Visual QA Protocol

The review pipeline is:

**canonical render → small-size render → grid render → physical/digital layout render**

### Stage 1 — Canonical render

Inspect the canonical icon independently at normal review scale. Check silhouette integrity, safe area, recognizable concept, and accidental geometry. Apply existing exceptions such as the `logic_no` slash reaching the frame.

### Stage 2 — Small-size render

Render the tile at a representative small physical/digital size. Check collapsed negative spaces, merged details, star/blob effects, and loss of distinctive features. Record the actual display or print size; browser zoom and print scaling can invalidate size assumptions.

### Stage 3 — Grid render

Place the icon among other canonical Pictiq tiles. Check distinguishability, visual weight, scale consistency, and accidental similarity to another icon. Include plausible confusion pairs, not only unrelated neighbors. Evaluate recognition without labels first.

### Stage 4 — Layout render

Place the icon into at least one representative real layout when it is intended for a known profile/use case: wallet card, lighter, phone, shirt, or another approved layout. Test communication under actual context, at intended size and relevant viewing distance. A fit-to-page preview alone does not establish physical-size acceptance.

If no use case is known, record the layout stage as deferred with a reason; do not imply acceptance for untested layouts. A missing required layout leaves that use-case review incomplete.

### Evidence and review record

Use [the QA sheet tool](../tools/README.md#make_icon_qa_sheetpy) or existing renderers to prepare evidence. The tool does not measure semantic recognition or grant acceptance. A short review note in the change/PR is sufficient: icon ID and source revision, reviewer/date, sizes and viewing conditions, grid neighbors, layout (or deferral reason), observations/confusion pairs, and pass/fail/pending per applicable stage. Resolve failures before acceptance. No approval database is required.

## Acceptance status

Pictiq distinguishes **STRUCTURAL VALIDATION** from **PERCEPTUAL ACCEPTANCE**.

Existing automated checks, including `tools/validate_svg.py` and `tools/validate_lexicon.py`, establish structural validity within their checked scope. Passing them does NOT automatically mean an icon is visually accepted.

A new canonical icon MUST follow this lifecycle:

**SOURCE → STRUCTURAL VALIDATION → VISUAL QA → CANONICAL ACCEPTANCE**

Maintainer review under §10 includes the visual evidence and perceptual result, as well as relevance, style, and originality. Failed perceptual review prevents canonical acceptance even when automated checks pass. The v1.0.1 workflow does not retroactively certify the existing icon inventory or replace the historical Core release.

## Reference Systems

**Non-normative.** Pictiq was developed independently. After the initial v1.0 protocol and handbook were completed, the project identified Jock Kinneir and Margaret Calvert’s British road-sign programme (1957–1967) as a particularly relevant historical precedent for its continuing development, not a direct inspiration for Pictiq v1.0.

Their work combined reduction, legibility in real viewing conditions, pictorial recognition, and systematic spacing. Its proportional design rules also illustrate how a visual system can continue to be applied beyond its original designers. These are useful reference points for Pictiq’s future development. See the [Design Museum profile of both designers](https://designmuseum.org/designers/jock-kinneir-and-margaret-calvert).

[MoMA’s Primary route sign for British roadways](https://www.moma.org/collection/works/407908) records the design as 1957–1967 and credits Jock Kinneir, Margaret Calvert, and Simon Morgan for the collection object. This reference does not imply a lineage or collaboration with Pictiq.

The UK Department for Transport’s [Traffic Signs Manual](https://www.gov.uk/government/publications/traffic-signs-manual) provides a further operational reference. [Chapter 1 (2018), §1.3.2 and Table 1-1](https://assets.publishing.service.gov.uk/media/5c419a1240f0b61704aec4d7/traffic-signs-manual-chapter-1.pdf) connects clear, timely understanding with the opportunity to act and describes legibility and viewing distance. [Chapter 7 (2018)](https://assets.publishing.service.gov.uk/media/5c78f8c7e5274a0ebfec719c/traffic-signs-manual-chapter-07.pdf) documents sign-face design and spacing. These references inform the discussion; their road-sign measurements are not Pictiq constraints.
