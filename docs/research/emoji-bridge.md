
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

### 1) Pictiq → Emoji (primary)
For each Pictiq `id`, store:
- `emoji_candidates`: list of 1..N candidate emoji
- `confidence`: high/medium/low
- `notes`: ambiguity warnings (culture/platform differences)

### 2) Emoji → Pictiq (reverse index)
Maintain a reverse lookup so that typing an emoji can suggest Pictiq concepts.

---

## What maps well vs poorly

### Maps well (often universal)
- comm_wifi → 📶 / 📡 (check ambiguity)
- need_water → 💧 / 🚰 / 🧴 (often ambiguous)
- money_* → 💳 / 💰 / 🪙
- move_public → 🚌 / 🚆 / 🚇 (but Pictiq keeps it “generic”)
- place_shop → 🛒

### Maps poorly (high ambiguity / culture dependent)
- safety_police (emoji may imply specific uniforms/regions)
- logic_no (varies; ❌ is not the same as Pictiq’s slash logic)
- place_hotel (🏨 is “hotel” but also “building”; Pictiq’s bed is clearer)
- punct_question / punct_exclaim (emoji punctuation exists but style varies)

---

## Practical recommendation for Pictiq

- Do NOT try to mirror Pictiq grammar into emoji grammar.
- Use emoji bridge as “approximate shorthand”, not as a canonical writing system.
- Keep Pictiq logic as:
  - stable IDs
  - stable canonical icons
  - stable rules

Emoji bridge is optional and can be versioned as a separate data file later.
