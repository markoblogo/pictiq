# Emoji Bridge (Research Notes)

This document proposes an optional “bridge” between **Pictiq concepts** and **Unicode emoji**
to enable lightweight messaging where emoji are available (chat apps, notes, quick UI).

Pictiq remains the canonical visual standard (framed tiles). Emoji are a convenience layer.

## Why do this?

- Many users already have emoji keyboards.
- Emoji can approximate some Pictiq concepts for quick messages.
- Emoji have multilingual search support via CLDR annotations/keywords.

Key constraint: emoji appearance varies across vendors/platforms. Pictiq icons must remain the source of truth.

Sources:
- https://unicode.org/reports/tr51/
- https://www.unicode.org/cldr/charts/latest/annotations/index.html

---

## Proposed mapping model

### Pictiq → Emoji
For each Pictiq `id`, store:
- `emoji_candidates`: list of 1..N candidates (single emoji or sequences)
- `confidence`: high / medium / low
- `notes`: ambiguity warnings (culture/platform differences)

### Emoji → Pictiq (reverse index)
Maintain a reverse lookup so that typing an emoji can suggest Pictiq concepts.

---

## What maps well vs poorly

### Maps well (often universal)
- comm_wifi → 📶 / 📡 (check ambiguity)
- money_* → 💳 / 💰 / 🪙
- place_shop → 🛒

### Maps poorly (high ambiguity / culture dependent)
- safety_police (uniform/region associations)
- logic_no (❌ is not the same as Pictiq’s slash logic)
- punct_* (punctuation emoji style varies)

---

## Recommendation for Pictiq

- Do NOT mirror Pictiq grammar into emoji grammar.
- Use emoji bridge as approximate shorthand only.
- Keep Pictiq tiles as canonical, controlled visuals.
