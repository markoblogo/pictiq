# Related Systems & Inspirations (Research Notes)

This document positions **Pictiq** among existing visual / constructed communication systems.
Pictiq is **not** trying to replace them. The goal is to borrow useful design patterns while
keeping Pictiq minimal: short phrases, pointing, framed tiles, and a small core lexicon.

## Quick comparison (what Pictiq is / isn’t)

- Pictiq is a **minimal visual protocol** for short, universal messages across language barriers.
- Pictiq is **not** a full natural language, not a writing system for speech, and not intended for long texts.
- Pictiq prioritizes:
  - fast recognition at arm’s length
  - minimal grammar (token chaining)
  - stable IDs + searchable metadata
  - strict style constraints (tile frame, monochrome, no SVG `<text>`)

---

## LoCoS (Logographic Communication System)

**What it is:** A minimalist logographic system aimed at communication through composable symbols.

**Why it matters for Pictiq:** LoCoS is a strong reference for “small primitives + composition rules”.
Even if Pictiq uses more globally recognizable pictograms, the **discipline of composition**
helps prevent uncontrolled growth.

**Takeaways to adopt:**
- Prefer **composition** over introducing new primitives.
- Define “symbol families” and rules for introducing new base concepts.

**Do NOT adopt:**
- Expanding toward “cover everything” language completeness.

Sources:
- https://en.wikipedia.org/wiki/LoCoS

---

## Blissymbolics (Blissymbols)

**What it is:** An ideographic symbol system used in AAC contexts.

**Why it matters for Pictiq:** Blissymbolics is real-world evidence that pictographic systems can be
operational, teachable, and useful — but also shows the cost of scaling grammar/coverage.

**Takeaways to adopt:**
- One symbol = one base meaning (avoid near-duplicates).
- Treat the lexicon as a stable “standard” with controlled extensions.
- Strong metadata: synonyms/aliases/use-cases.

**Do NOT adopt:**
- Heavy grammar and full-language ambitions (Pictiq wins by staying minimal).

Sources:
- https://en.wikipedia.org/wiki/Blissymbols
- https://www.blissymbolics.org/

---

## SignWriting (writing systems for sign languages)

**What it is:** A writing system for sign languages that encodes hand shapes, movement, facial expression, etc.

**Why it matters for Pictiq:** SignWriting shows what formalization looks like when representing
complex non-verbal information. Pictiq is simpler, but can borrow the engineering mindset:
spec-first, stable forms, validation, and user testing.

**Takeaways to adopt:**
- Treat the spec as a true standard: clear rules, examples, validation.
- Consider future tooling (parsing, generation, recognition).

**Do NOT adopt:**
- Movement/gesture encoding complexity.

Sources:
- https://en.wikipedia.org/wiki/SignWriting
- https://signwriting.org/

---

## Toki Pona + sitelen

**What it is:** A minimalist constructed language with a small vocabulary; has writing systems such as sitelen pona.

**Why it matters for Pictiq:** The key inspiration is the philosophy: minimal set + context + composition.
Pictiq can apply the same strategy to pictograms (few core tiles, many combinations).

**Takeaways to adopt:**
- Minimize the core and grow by composition.
- Use strict rules to prevent vocabulary bloat.

**Do NOT adopt:**
- Treating community-specific glyphs as globally universal.

Sources:
- https://en.wikipedia.org/wiki/Toki_Pona

---

## Lojban

**What it is:** A constructed language designed for unambiguous grammar and logical structure.

**Why it matters for Pictiq:** Pictiq is not a logical language, but Lojban is a useful reference
for **machine-readability**: explicit tokens, unambiguous parsing, formal validation.

**Takeaways to adopt:**
- Keep the grammar token-based and parseable (validation-friendly).
- Avoid ambiguous syntax in examples and docs.

**Do NOT adopt:**
- Full logical-language complexity.

Sources:
- https://en.wikipedia.org/wiki/Lojban
- https://lojban.org/

---

## Emoji / Unicode / CLDR (search + interoperability)

**What it is:** Unicode standardizes emoji characters and sequences; CLDR provides names and keywords (annotations)
in many languages for search/discovery.

**Why it matters for Pictiq:** This is the strongest operational parallel:
Pictiq also needs stable IDs, searchable keywords, and multilingual annotations.

**Takeaways to adopt:**
- Stable IDs + versions/releases.
- “Short name + keywords” model for multilingual search (like CLDR annotations).
- An “emoji bridge” mapping: Pictiq concept → best matching emoji set, where feasible.

**Do NOT adopt:**
- Relying on emoji rendering consistency (vendors differ widely).
- Overloading meaning just because an emoji exists.

Sources:
- https://unicode.org/reports/tr51/
- https://www.unicode.org/cldr/charts/latest/annotations/index.html
- https://www.unicode.org/faq/emoji_dingbats.html

---

## Transfer table (what to adopt / avoid)

| System | Adopt for Pictiq | Avoid for Pictiq |
|---|---|---|
| LoCoS | “primitives + composition discipline”, symbol families | full-language completeness |
| Blissymbolics | stable semantics, controlled growth, metadata discipline | heavy grammar, broad coverage ambitions |
| SignWriting | spec-first mindset, validation, user testing culture | movement/gesture encoding complexity |
| Toki Pona | minimal core + composition + context | community-specific glyph universality assumptions |
| Lojban | machine-parseable token grammar, validation mentality | logical-language complexity |
| Emoji/Unicode/CLDR | stable IDs, releases, multilingual keywords, mapping bridges | vendor rendering dependence, meaning overload |

---

## Immediate action items for Pictiq (from this research)

1. Add a short section in `spec/PROTOCOL.md`: “Related systems / inspirations”.
2. Add a rule in `spec/ICON_DEFINITIONS.md`: new symbols should be:
   - a new primitive (rare), or
   - a composition of existing symbols, or
   - a clearly distinct object with minimal details.
3. Add a planned “quick user test” to `PHASES.md` for the first canonical icons:
   - 5–10 people, mixed languages/cultures, measure guessability and confusion cases.
1. Plan an “emoji bridge” file (see `emoji-bridge.md`) once core icons are canonical.
