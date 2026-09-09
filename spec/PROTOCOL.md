# Pictiq Protocol

Pictiq is a minimal visual protocol for short universal messages across language barriers.
It is meant for pointing, quick signs, stickers, and simple phrases — not for long texts.

## Related systems / inspirations

Pictiq is a minimal visual protocol for short messages. It does not aim to replace existing visual languages,
AAC symbol sets, emoji standards, or writing systems. We treat them as references for *engineering choices*:
how to keep semantics stable, how to scale responsibly, and how to stay usable across cultures and platforms.

We study engineering patterns found in systems such as LoCoS, Blissymbolics, SignWriting, Lojban, emoji/Unicode, and Toki Pona with sitelen pona. These systems are references for comparison, interoperability, and design analysis rather than direct ancestors of Pictiq.

Relevant patterns include control of primitives versus composition, stable semantics, spec-first standardization, constrained vocabularies, parseable grammar, visual writing, and cross-system interoperability. Pictiq tiles remain canonical.

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
3. Remove the person and transient context. Ask whether the concept must survive in standalone communication. If not, prefer embodiment or context.
4. Test whether an existing lexical tile expresses the concept honestly.
5. Test whether composition with existing tiles expresses it.
6. Ask whether it qualifies another tile and is therefore a modifier or operator.
7. Ask whether it is a semantic type with a dynamic value and is therefore better represented as a parameter.
8. Ask whether it identifies one named entity within a defined context and is therefore an entity symbol.

Only after these alternatives fail should a new lexical tile be considered. Any proposed canonical rendering MUST then pass the Perceptual Design Principles and Visual QA Protocol before acceptance.

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

#### Relationship to Toki Pona

**Non-normative.** Toki Pona and sitelen pona became a comparative research system for Pictiq after the initial protocol was developed. The crosswalk is used to study how a minimal lexical language differs from an embodied visual protocol; it is not presented as a direct design reference or source of Pictiq's original architecture.

Toki Pona and Pictiq both use context to reduce explicit vocabulary, but they do so through different media. A Toki Pona lexical absence in Pictiq may be supplied by embodiment, may expose a real standalone requirement, or may fall outside Pictiq’s intended scope. Crosswalk coverage is therefore evidence for analysis, not a completeness target.

### 1.2 Communication primitive classes

Pictiq uses five architectural classes. The class describes how meaning enters a message; it does not grant canonical status.

#### Lexical tiles

Lexical tiles represent reusable concepts that genuinely require explicit visual representation. Current examples include water, food, a neutral person, heat/fire, cold, electrical energy, taxi, hotel, airport, medical help, and bar.

A lexical tile SHOULD be created only when the concept has independent Pictiq utility, embodiment and context do not replace it reliably in all required modes, composition or modification is insufficient, and it survives the vocabulary decision tree. A word in Toki Pona or another source language, or a translation gap by itself, MUST NOT justify a lexical tile.

#### Modifiers and operators

Modifiers qualify another tile; operators alter how another tile or phrase is interpreted. Existing punctuation, yes/no logic, quantities, plus, and minus are the current examples. Their exact behavior remains defined in §§3–5 and [Grammar](GRAMMAR.md).

> Do not create a word when a modifier will do.

Evaluation and truth are distinct axes. `logic_yes` and `logic_no` MUST NOT be overloaded as generic GOOD and BAD. Canonical `qual_good` and `qual_bad` modifiers may qualify food, hotel, or another base concept as positively or negatively evaluated; they do not encode every emotional or moral sense of “good” and “bad.” Likewise, physical LARGE/SMALL must not be equated with `qty_plus`/`qty_minus`; embodied users can show scale with their hands, while standalone use should investigate reusable scale modifiers.

The provisional relational operators `rel_greater` (`>`) and `rel_lesser` (`<`) compare larger/greater with smaller/lesser. They remain distinct from `qty_plus` and `qty_minus`, which request additional quantity or reduction. In a clearly navigational context they MAY also carry rightward or leftward direction; this contextual reading does not redefine either operator as a permanent direction token.

As a research example, Toki Pona `mute` is better approximated compositionally as `qty_5 + qty_plus` than by `qty_5` alone. This observation defines no new mechanism.

#### Parametric tiles

A parametric tile represents a semantic type whose value is supplied dynamically rather than selected from a finite lexical vocabulary. COLOR is the first proposed Pictiq parametric type.

In embodied use, point to an actual visible color where reliable. In standalone use, the proposed representation is the canonical Pictiq frame containing a neutral color-sample shape, preferably a circle, filled with the requested value. Conceptual forms include `color(#ff0000)`, `color(#264653)`, and `color(#747b72)`. A machine-readable form could be `{ "type": "color", "value": "#747b72" }`.

The palette is not lexically bounded; arbitrary colors are permitted. The actual color is the semantic payload, making COLOR an intentional exception to normal monochrome rendering while the frame remains canonical Pictiq structure. Separate red, yellow, blue, green, or other lexical color tiles MUST NOT be created merely to enumerate a palette.

COLOR is a **PROPOSED PARAMETRIC MECHANISM**. It defines no canonical icon, ID, sample geometry, syntax, implementation, or acceptance status. Future parametric types MAY be considered only through the same decision tree.

#### Entity symbols

An entity symbol is a unique visual identifier for a specific person, fictional character, organization, place, object, or other named entity within an explicit context. It differs from a generic lexical concept: a neutral person tile means “person / human participant,” while an entity symbol means “this specific identified entity.”

> Do not spell an identity when a symbol can identify it.

Entity symbols are not automatically part of the Core lexicon. They MAY belong to context packs, narrative dictionaries, personal profiles, or future entity registries. A narrative may locally define symbols for Odysseus, Penelope, and Telemachus just as an Alice narrative pack may identify a recurring character. A conceptual namespace such as `entity:odysseus@odyssey-pack` expresses the required scope; it is not implemented syntax.

Governance requirements:

- **Real people:** the represented person SHOULD be able to define or revise their personal symbol where practical. A third-party context MAY use a local identifier but MUST NOT claim ownership of a universal identity.
- **Fictional, historical, and public-domain entities:** a project, translation, pack, or narrative MAY define a symbol canonical within that named context and version until explicitly revised.
- **Scope:** identity MUST have an explicit namespace or context. No global first-claim registry is implied.
- **Recognition:** a symbol SHOULD use distinctive, recognizable associations rather than an arbitrary abstract mark where practical. A tile rendering MUST pass normal perceptual QA.

#### Embodied references

An embodied reference deliberately leaves meaning on the human communication surface. A person can point to self or another person, indicate eyes or direct gaze, pull clothing, point to a body location or mouth, show physical size with hands, indicate a visible color, point toward a direction or place, and use facial expression, voice, or gesture for emotion.

These are intentional protocol behaviors, not missing features. A standalone requirement may still move the same concept into another class.

> Embodiment is part of the protocol, not a workaround for the protocol.

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
“Many / more” is best approximated by combining `qty_5` with `qty_plus`. Repeating `qty_5` represents a concrete total of ten.

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

## 8. Proper names and entity symbols
- Proper names are not Core lexical words. Plain text used as a name remains outside the tile system.
- An entity symbol MAY identify a named entity inside an explicitly scoped context under §1.2; it does not become a global Core word.
- The Pictiq logo remains the only globally defined proper-name mark and is not a tile.
- Context protocols may define geographic, narrative, personal, or organizational entity symbols. Brand identifiers require appropriate authority and remain subject to §9.

## 9. Safety & restrictions
- No text/wordmarks/logos.
- Avoid cultural/religious/political sensitive symbols (medical cross is allowed as an international standard).
- No trademarks, brand identity elements, or place names as text.

## 10. Canonical SVG rule
- Canonical icons in the repository must NOT contain SVG `<text>` elements.
- This includes `? ! + - I II IIIII`: they must be vector shapes/paths, not text.
