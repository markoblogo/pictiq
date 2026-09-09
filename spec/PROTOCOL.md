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

### 1.1 Embodied and Standalone Communication

This section is normative. **Embodied Communication** is a live exchange in which a person can use their body, voice, gaze, pointing, a visible object, and the shared physical situation together with Pictiq. **Standalone Communication** is a durable or remote artifact—such as a sign, printed card, sticker, screen, or unattended instruction—that must remain understandable when the author is absent.

Pictiq MUST evaluate vocabulary and composition against the communication mode in which a message must work. A concept supplied reliably by the embodied channel SHOULD be omitted from the tile sequence. The same concept MAY require explicit representation when the message must survive without the person, object, or situation that supplied it.

> Design only what the communication surface cannot already provide.

In practice: use the body for what the body can express, and use the icon for what must remain after the body is gone. Before expanding the vocabulary, check the body, gesture, physical object, environment, pointing, neighboring tiles, existing protocol operators, and shared contextual knowledge.

This rule complements [Design for the decision](ICON_SPEC.md#1-design-for-the-decision): the minimum sufficient message includes all available channels, not only the drawing.

#### Decision tree

For each proposed concept or message:

1. Ask whether the concept is independently useful to Pictiq outside a particular translation or crosswalk. If not, do not add it.
2. Identify the intended mode. If body, gesture, pointing, environment, carrier object, or existing tiles supply the concept reliably in embodied use, an embodied-specific tile is usually unnecessary; continue only if standalone use creates a genuine need.
3. Remove the person and transient context. If the standalone artifact remains clear, prefer context or composition. If it becomes ambiguous, continue.
4. Test whether an existing tile, composition, modifier, or parameter can preserve the concept before proposing a new lexical tile.
5. If a new canonical concept is still justified, apply the Perceptual Design Principles and Visual QA Protocol before acceptance.

> A missing lexical equivalent is not automatically a missing Pictiq concept.

Examples:

- **Person / participant:** pointing to oneself or another person may supply the participant in an embodied exchange. An unattended medical card or evacuation sign may need a neutral person concept.
- **Direction / location:** a pointing arm, gaze, or placement can carry direction in a live exchange. A standalone route sign needs direction encoded in the artifact.
- **Color / object identification:** pointing to a visible red object can make a color tile redundant. A remote instruction such as “use the red container” needs color to remain explicit.
- **Communication / message:** speaking, showing a phone, or indicating a written note can supply the channel live. A standalone interface may need a channel-neutral message concept.
- **Hot / cold:** live physical context may help but is often unreliable. Standalone safety or comfort messages may need conventional heat/fire or cold cues; no asset is defined here.
- **Light:** ambient light can be indicated live. An unattended lighting, visibility, or access instruction may need the concept encoded; no asset is defined here.

#### Absence states

An absent lexical equivalent MUST NOT be treated automatically as a protocol defect. Gap analysis SHOULD classify the intended use with one or more of these states:

- **EMBODIED-OMITTABLE:** the embodied channel can supply the concept reliably enough that no tile is needed for that use.
- **STANDALONE-GAP:** the concept is necessary when the message must work without the communicator or transient context, and existing tiles or composition do not preserve it honestly.
- **OUT-OF-SCOPE:** explicit encoding would add language-specific grammar, excessive lexical breadth, or a concept without demonstrated independent Pictiq utility.

The states are analytical and may overlap. For example, visual attention can be EMBODIED-OMITTABLE when gaze or pointing is visible and still be a STANDALONE-GAP for an unattended accessibility cue.

#### Parametric visual modifiers

A compact color system is a candidate for future standalone communication because color can distinguish an object after the communicator is gone. In embodied use, pointing at an existing color remains preferred when reliable.

The standalone research direction is a parametric visual modifier: the canonical Pictiq frame plus a neutral internal color sample whose actual value carries the meaning. Conceptual forms include `color(#ff0000)`, `color(#264653)`, and `color(#747b72)`; the palette is not lexically bounded. A machine-readable form could be `{ "type": "color", "value": "#747b72" }`.

This may become the first parametric Pictiq tile or operator. Because color itself is the semantic payload, it would be an intentional exception to the normal monochrome visual system. This is a non-canonical proposal: it defines no icon, ID, sample geometry, palette, syntax, implementation, or acceptance status, and it does not introduce hardcoded color tiles.

#### Relationship to Toki Pona

**Non-normative.** Toki Pona and Pictiq both use context to reduce explicit vocabulary, but they do so through different media. A Toki Pona lexical absence in Pictiq may be supplied by embodiment, may expose a real standalone requirement, or may fall outside Pictiq’s intended scope. Crosswalk coverage is therefore evidence for analysis, not a completeness target.

## 2. Tiles and frame
- Every lexicon word is a framed tile: a rounded-square frame is mandatory.
- Inner shapes must not touch the frame, except `logic_no`, where the slash may reach the frame as part of the canonical look.
- Monochrome: canonical SVG uses `currentColor` to support black/white rendering on any background.
- The Pictiq logo is not a tile and must not use the rounded-square frame.

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
