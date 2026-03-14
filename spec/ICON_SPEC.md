# Pictiq Icon Spec (Draft)

## 1. Purpose
Pictiq icons are designed for short, universal messages where language may be a barrier.
Icons must remain simple, readable, and consistent across print and digital media.

## 2. Format
- Source format: SVG
- ViewBox: 32x32 (preferred) or 24x24 (allowed, but be consistent)
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
