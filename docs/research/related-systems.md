# Related Systems & Inspirations (Research Notes)

This document positions **Pictiq** among existing visual / constructed communication systems.
Pictiq is **not** trying to replace them. The goal is to borrow useful design patterns while
keeping Pictiq minimal: short phrases, pointing, framed tiles, and a small core lexicon.

## Quick framing: what Pictiq is / isn’t

- Pictiq is a **minimal visual protocol** for short, universal messages across language barriers.
- Pictiq is **not** a full natural language, not a writing system for speech, and not intended for long texts.
- Pictiq prioritizes:
  - fast recognition at arm’s length
  - minimal grammar (token chaining)
  - stable IDs + searchable metadata
  - strict style constraints (tile frame, monochrome, no SVG `<text>`)

---

## LoCoS (Logographic Communication System)

**Why it matters for Pictiq:** a reference for “small primitives + composition rules” discipline.

**Adopt:**
- Prefer **composition** over new primitives.
- Define “symbol families” and strict rules for introducing new base concepts.

**Avoid:**
- Expanding toward “cover everything” completeness.

Sources:
- https://en.wikipedia.org/wiki/LoCoS

---

## Blissymbolics (Blissymbols)

**Why it matters for Pictiq:** evidence that pictographic systems can be operational, teachable, useful
(AAC contexts), but scaling grammar/coverage has costs.

**Adopt:**
- One symbol = one base meaning.
- Controlled growth via packs/extensions.
- Strong metadata discipline (aliases, tags, use-cases).

**Avoid:**
- Heavy grammar and broad coverage ambitions.

Sources:
- https://en.wikipedia.org/wiki/Blissymbols
- https://www.blissymbolics.org/

---

## SignWriting

**Why it matters for Pictiq:** shows what “spec-first standardization” looks like for non-verbal information.
Pictiq is simpler, but can borrow the engineering mindset: stable forms, validation, documentation, user tests.

**Adopt:**
- Spec-first mindset + validation + user-testing culture.

**Avoid:**
- Movement/gesture encoding complexity.

Sources:
- https://en.wikipedia.org/wiki/SignWriting
- https://signwriting.org/

---

## Toki Pona + sitelen

**Why it matters for Pictiq:** philosophy of minimal core + composition + context.

**Adopt:**
- Keep the core small; grow by composition and context packs.
- Avoid semantic bloat.

**Avoid:**
- Assuming community-specific glyph systems are globally universal.

Sources:
- https://en.wikipedia.org/wiki/Toki_Pona

---

## Lojban

**Why it matters for Pictiq:** reference for machine-readability and unambiguous token grammar.
Pictiq is not a logical language, but can borrow validation mentality.

**Adopt:**
- Keep grammar token-based and parseable (validation-friendly).
- Avoid ambiguous examples and inconsistent notation.

**Avoid:**
- Full logical-language complexity.

Sources:
- https://en.wikipedia.org/wiki/Lojban
- https://lojban.org/

---

## Emoji / Unicode / CLDR (search + interoperability)

**Why it matters for Pictiq:** strongest operational parallel:
stable IDs, versions, multilingual keywords for search/discovery (CLDR annotations).

**Adopt:**
- Stable IDs + releases.
- “Short name + keywords” model for multilingual search.
- Optional “emoji bridge” mapping layer.

**Avoid:**
- Relying on emoji rendering consistency (vendors differ).
- Overloading meaning just because an emoji exists.

Sources:
- https://unicode.org/reports/tr51/
- https://www.unicode.org/cldr/charts/latest/annotations/index.html

---

## Transfer table (what to adopt / avoid)

| System | Adopt for Pictiq | Avoid for Pictiq |
|---|---|---|
| LoCoS | composition discipline, symbol families | completeness ambition |
| Blissymbolics | stable semantics, controlled growth, metadata | heavy grammar |
| SignWriting | spec-first mindset, validation, user testing | gesture/movement encoding |
| Toki Pona | minimal core + composition | assuming global universality of niche glyphs |
| Lojban | parseable token grammar, validation mentality | logical-language complexity |
| Emoji/Unicode/CLDR | stable IDs, releases, multilingual keywords, mapping bridges | vendor rendering dependence |

---

## Immediate action items for Pictiq

1. Add a short section in `spec/PROTOCOL.md`: “Related systems / inspirations”.
2. Add a strict growth rule in `spec/ICON_DEFINITIONS.md`: new symbols must be rare primitives, compositions, or clearly distinct objects.
3. Add a planned “quick user test” to `PHASES.md` for canonical icons (guessability).
4. Add an optional “emoji bridge” file once the first canonical set is stable.
