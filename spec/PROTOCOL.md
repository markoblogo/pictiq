# Pictiq Protocol

Pictiq is a minimal visual protocol for short universal messages across language barriers.
It is meant for pointing, quick signs, stickers, and simple phrases — not for long texts.

## Related systems / inspirations

Pictiq is a minimal visual protocol for short messages. It does not aim to replace existing visual languages,
AAC symbol sets, emoji standards, or writing systems. We treat them as references for *engineering choices*:
how to keep semantics stable, how to scale responsibly, and how to stay usable across cultures and platforms.

We borrow ideas such as: strict control of primitives vs composition (LoCoS), stable meanings with disciplined growth (Blissymbolics),
spec-first standardization and validation mindset (SignWriting), minimal core philosophy (Toki Pona), and parseable token grammar mentality (Lojban).
For interoperability, we also study emoji/Unicode and CLDR keywording, but Pictiq tiles remain canonical.

See the research notes:
- `docs/research/related-systems.md`
- `docs/research/emoji-bridge.md`
- `docs/research/tiny-languages-protocol.md`

## 1. Core principles
- Zero-intent: pointing at an object icon is a valid message by default (“this / need this / where is this”).
- Meaning is amplified by punctuation tiles and context.
- Some nouns may act as actions depending on context (transport = ride, coins = pay).

## 2. Tiles and frame
- Every lexicon word is a framed tile: a rounded-square frame is mandatory.
- Inner shapes must not touch the frame, except `logic_no`, where the slash may reach the frame as part of the canonical look.
- Monochrome: canonical SVG uses `currentColor` to support black/white rendering on any background.

## 3. Punctuation and logic
Punctuation is expressed via dedicated tiles:
- `punct_question` adds “where/how/is there/can I”.
- `punct_exclaim` adds “urgent/attention/help/insist”.

Logic:
- `logic_yes` = confirm/accept/open/ok.
- `logic_no` = negate/forbid/closed/not ok.

Negation form:
- `X + logic_no`
- `logic_no` may be used standalone as an answer.

## 4. Quantity
Quantity follows the object (WHAT then HOW MUCH):
- `qty_1`, `qty_2`, `qty_5`, `qty_plus`, `qty_minus`
“Many” may be expressed by:
- repeating `qty_5` (e.g. `qty_5 + qty_5`)
- combining `qty_5` with `qty_plus`

Note:
- In live interaction, fingers often work better for exact numbers.
- Pictiq is not designed for precise numbers above ~10; plain text outside tiles is allowed (not regulated).

## 5. Compounds
BASE + QUALIFIER is allowed:
- Left tile = base meaning, right tile = qualifier.
Recommended phrase length: 1–3 tiles; maximum: up to 5 tiles.

## 6. Phrases, lines, blocks
- One phrase = one line. No line breaks inside a phrase.
- Left-to-right reading.
- Multiple phrases: each on a new line.
- A vertical grid (one tile per row) is treated as a catalog/keyword list (for pointing).

If both contextual and universal blocks exist:
- contextual block goes on top and is usually larger,
- universal block goes below and is usually smaller,
- blocks may be grouped with a rounded rectangle outline.

## Representations

Pictiq supports two canonical representations of the same lexicon: **Catalog Grid Mode** and **Phrase Line Mode**.
Both representations use the same tile design and token IDs.

### Catalog Grid Mode (pointing)
- Tiles are arranged in a **grid** for pointing at individual concepts.
- A grid is interpreted as a **set of keywords**, not a single sentence.
- Keyword order in a grid is not meaningful unless an explicit layout rule is provided by the pack/template.

Recommended layout for merchandise:
- **Context block** (optional) on top with larger tiles.
- **Core block** below with smaller tiles.
- Blocks MAY be visually separated by spacing or an outer rounded rectangle frame.
- Inside each block, tile size SHOULD be consistent.

### Phrase Line Mode (token sequence)
- A phrase is a **single horizontal line** of tiles.
- Reading order is **left to right**.
- A phrase MUST NOT wrap. No line breaks inside a phrase.
- One phrase MUST occupy exactly one line.
- Multiple phrases are written as multiple lines.

Length constraints:
- A phrase SHOULD be 1–3 tiles.
- A phrase MUST NOT exceed 5 tiles.

### Mixed layouts (grid + phrases)
If both phrases and keyword blocks are present in the same design:
- Phrase lines SHOULD appear first (top).
- Keyword blocks SHOULD appear after phrases.
- Phrase lines MUST NOT be framed as a block (to keep them distinct from keyword sets).

### Negation in representations
- Negation is expressed as `X + logic_no` in Phrase Line Mode.
- In Catalog Grid Mode, the same meaning is achieved by pointing at `X` and then `logic_no`.

### Notes for computer vision / parsing
A recognizer should:
- detect tile boundaries (rounded-square frame)
- detect line grouping vs grid grouping
- reconstruct token order for Phrase Line Mode
- treat grid mode as unordered keywords unless pack-specific rules apply

## 7. Dictionaries and packs
### 7.1 Core protocol
- Core covers universal high-frequency human needs and concepts that are hard to replace with gestures.
- Core does NOT include fixed negations.

### 7.2 Context protocols
Context packs extend vocabulary for a scenario (cities, sports, business events, vegan/allergy packs, etc.).
Context packs may include fixed negations.
Each context pack:
- adds context-specific icons,
- recommends a subset of core icons.

### 7.3 Personal and corporate protocols
Personal/corporate packs are allowed and may include:
- fixed negations,
- interest/needs-specific icons,
- unique icons (if no synonym exists and protocol rules are met),
- proper names.

## 8. Proper names (non-tiles)
- Proper names are not core lexicon words and do not use the tile frame.
- The only globally allowed proper name is the Pictiq logo itself (non-tile).
- Other proper names are allowed only inside context protocols (geo, brands by request, personal/corporate identifiers, etc.).
- A dedicated geo protocol may define types like city/country/river.
- Brand icons are added only by brand initiative and must avoid text/logos.

## 9. Safety & restrictions
- No text/wordmarks/logos.
- Avoid cultural/religious/political sensitive symbols (medical cross is allowed as an international standard).
- No trademarks, brand identity elements, or place names as text.

## 10. Canonical SVG rule
- Canonical icons in the repository must NOT contain SVG `<text>` elements.
- This includes `? ! + - I II IIIII`: they must be vector shapes/paths, not text.
