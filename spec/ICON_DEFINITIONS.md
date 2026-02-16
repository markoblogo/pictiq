# Pictiq Icon Definitions & Design Brief

This document is a designer/developer brief: what each icon means and how it should look.
Important: the repository only accepts SVG icons with no `<text>` elements. If a font is used as a drafting tool for `? ! + - I II IIIII`, it must be converted to curves and manually normalized before committing.

## Icon families & growth rule

- **Family definition:** Every icon belongs to a _family_ (e.g., punctuation, logic, quantity, money, communication, power, needs, safety, places, movement, service).
    
- **Growth rule (strict):** A new lexicon entry MUST be one of:
    
    1. **New primitive (rare)** — allowed only if the concept cannot be expressed by existing icons or a simple compound, and it is highly universal.
        
    2. **Composition** — use existing tiles as BASE + QUALIFIER (preferred).
        
    3. **New object (clear silhouette)** — a distinct real-world object, drawn with minimal detail, not overlapping with existing meanings.
        
    
- **Rejection rule:** If a proposed icon is “almost the same” as an existing one, it MUST be rejected and replaced by:
    
    - better aliases/tags/examples for the existing icon, or
        
    - a compound phrase, not a new icon.
        
    
- **Family consistency:** Within a family:
    
    - silhouette complexity stays comparable,
        
    - proportions and negative space follow the same reading logic,
        
    - no “special styling” is introduced for one icon.
        
    
- **Core vs Context constraint:**
    
    - **Core** accepts only primitives that are globally useful and frequent.
        
    - **Context packs** can add less universal objects and “fixed negations” (object + the same logic_no slash).
        
    
- **Checklist for adding a new icon (must pass):**
    
    - Is there already a synonym in the lexicon?
        
    - Can it be expressed as BASE + QUALIFIER?
        
    - Is the silhouette globally recognizable?
        
    - Does it avoid culture/religion/sexuality-sensitive symbols and brands?
        
    - Can it be rendered cleanly at arm’s length?

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

## Emoji bridge (non-canonical)

Pictiq icons are the canonical representation of meaning. Emoji mappings are provided only as a convenience bridge for typing short messages in environments where custom Pictiq tiles are not available.

**Rule (strict):**
- Each `icon_id` may define **exactly 1 primary emoji** (`primary_emoji`) and **up to 2 alternatives** (`alt_emoji`).
- Do **not** add more than 3 emojis total per icon (1 primary + max 2 alt).
- Emojis are **not normative**: emoji appearance and meaning may vary across platforms and fonts.
- If an emoji is ambiguous, keep the mapping minimal and document the ambiguity in the notes below (do not “fix” ambiguity by adding many alternatives).

**Selection criteria:**
- Prefer globally recognizable, non-branded, non-religious, non-political symbols.
- Prefer the emoji that most closely matches the **core meaning** of the Pictiq tile (not a niche interpretation).
- Avoid emojis that strongly imply culture-specific or sensitive meanings unless the Pictiq meaning itself is explicitly that.
- When in doubt, choose fewer mappings, not more.

### Ambiguity notes (important)

Some concepts are inherently more ambiguous in emoji form:

- `logic_no`: many “no” emojis read as **forbidden/stop** rather than a neutral “not / no / closed / not accepted”. Treat emoji as a shortcut only; the canonical Pictiq meaning remains `X + logic_no`.
- `need_water`: emoji often implies tap water (`🚰`) rather than “bottled water”. Pictiq canonical icon is the bottle silhouette; emoji is only a convenience.
- `comm_wifi`: the best available emoji (`📶`) often reads as “cellular signal” rather than Wi-Fi. Use combinations (e.g., `place_hotel + comm_wifi`) to reduce ambiguity.
- `move_public`: emoji usually encodes a specific vehicle type (bus/train/metro). Pictiq `move_public` is a **class** (“public transport”), not a specific mode.

### Universal Core emoji mapping (finalized, non-canonical)

punct_question — primary: ❓; alt: ❔
punct_exclaim — primary: ❗; alt: ❕
logic_yes — primary: ✅; alt: ✔️
logic_no — primary: 🚫; alt: ❌, ⛔
time — primary: 🕒; alt: ⏰, 🕰️
qty_1 — primary: 1️⃣
qty_2 — primary: 2️⃣
qty_5 — primary: 5️⃣; alt: 🔢
qty_plus — primary: ➕
qty_minus — primary: ➖
money_coins — primary: 🪙; alt: 💰, 💵
money_card — primary: 💳
money_atm_bank — primary: 🏧; alt: 🏦
comm_wifi — primary: 📶; alt: 🌐
comm_phone — primary: 📱; alt: ☎️
power_plug — primary: 🔌
need_toilet — primary: 🚽
need_water — primary: 🚰; alt: 💧
need_food — primary: 🍽️; alt: 🍴
need_bar — primary: 🍷; alt: 🍺, 🥃
safety_medical — primary: 🏥; alt: 🚑, 🩺
safety_police — primary: 👮; alt: 🚓, 🛡️
place_hotel — primary: 🏨; alt: 🛏️
place_shop — primary: 🛒; alt: 🏪, 🛍️
place_landmark_park — primary: 🏞️; alt: 🌳
place_gas — primary: ⛽
service_tools — primary: 🔧; alt: 🛠️
move_feet — primary: 🚶; alt: 👣
move_taxi — primary: 🚕
move_car — primary: 🚗; alt: 🚙
move_public — primary: 🚌; alt: 🚆, 🚇

## 2. Icon definitions (Universal Core)

All icons are framed tiles (rounded-square frame). Inner shapes are filled silhouettes using `currentColor`. No `<text>` elements in final SVGs; even `? ! + - I II IIIII` must be curves/paths.

### punct_question — question
**Visual:** A large question mark `?`, centered.  
**Meaning:** where/how/is there/can I.  
**Avoid:** decorative serif-like endings, tiny dot details.  
**Examples:** `need_toilet + punct_question`, `place_hotel + punct_question`.

### punct_exclaim — urgent / attention / help
**Visual:** A large exclamation mark `!`, centered.  
**Meaning:** urgent / attention / help / insist.  
**Avoid:** double exclamation, stylized marks.  
**Examples:** `safety_medical + punct_exclaim`, `need_water + punct_exclaim`.

### logic_yes — yes / ok / accepted / open
**Visual:** A check mark (tick) centered, simple silhouette.  
**Meaning:** confirmation, acceptance, “works”, “open”.  
**Avoid:** circles, smileys, letters.  
**Examples:** `money_card + logic_yes`, `place_hotel + logic_yes`.

### logic_no — no / not / forbidden / closed
**Visual:** A single diagonal slash `/` inside an otherwise empty tile.  
Direction: top-right → bottom-left. Thickness: 2–3× the frame stroke.  
**Meaning:** negation, prohibition, not accepted, closed.  
**Use:** postfix negation `X + logic_no` or standalone answer `logic_no`.  
**Avoid:** circles, letter X, double-cross (unless introduced later as a separate icon).  
**Examples:** `money_card + logic_no`, `need_food + logic_no`.

### Fixed negations (context packs only)
**Visual:** Any object icon with the same `logic_no` slash over the object (same direction, same character).  
**Meaning:** stable, one-tile restrictions (“no meat”, “no alcohol”, “no nuts”, etc.).  
**Rule:** must reuse the exact slash style of `logic_no`.

---

## Quantity

### qty_1 — one
**Visual:** `I` as a single vertical stroke (curve/path, not text).  
**Meaning:** 1 item.  
**Examples:** `need_water + qty_1`, `need_food + qty_1`.

### qty_2 — two
**Visual:** `II` two vertical strokes, equal spacing and thickness.  
**Examples:** `need_water + qty_2`, `need_food + qty_2`.

### qty_5 — five / many
**Visual:** `IIIII` five vertical strokes.  
**Many rule:** repetition is allowed (`qty_5 + qty_5`). Also allowed: `qty_5 + qty_plus`.  
**Examples:** `need_water + qty_5`, `need_water + qty_5 + qty_5`.

### qty_plus — more / add / another
**Visual:** `+` as a clean geometric plus (curve/path, not text).  
**Important:** must be visibly thinner/lighter than `safety_medical` (medical cross).  
**Examples:** `need_water + qty_plus`, `need_food + qty_plus`.

### qty_minus — less / reduce
**Visual:** `-` as a clean geometric minus (curve/path, not text).  
**Examples:** `need_water + qty_minus`, `need_food + qty_minus`.

---

## Time

### time — time / when / schedule
**Visual:** A simple clock face: a circle + two hands.  
Minute hand: vertical up (12), almost touching the circle but not touching.  
Hour hand: horizontal right (3), about half radius.  
Hands meet at center. No numbers/ticks.  
**Examples:** `move_public + time + punct_question`, `place_shop + time + punct_question`.

---

## Money

### money_coins — cash / money
**Visual:** Two overlapping coins in silhouette; include a simple “edge/layer” cue so it doesn’t resemble card-brand circles.  
**Avoid:** currency symbols, numbers, detailed embossing.  
**Examples:** `need_food + money_coins`, `money_coins + punct_question`.

### money_card — card payment / card
**Visual:** Rounded rectangle card + a single stripe (magnetic stripe).  
**Avoid:** payment logos, numbers, tiny chip details.  
**Examples:** `money_card + punct_question`, `money_card + logic_no`.

### money_atm_bank — ATM / bank
**Visual:** Standalone ATM kiosk: vertical body, screen, 3×3 button grid, cash slot.  
**Avoid:** letters “ATM”, currency symbols.  
**Examples:** `money_atm_bank + punct_question`, `money_atm_bank + time + punct_question`.

---

## Communication & power

### comm_wifi — Wi-Fi
**Visual:** A dot + two arcs (standard Wi-Fi symbol).  
**Avoid:** “WiFi” letters.  
**Examples:** `comm_wifi + punct_question`, `place_hotel + comm_wifi`.

### comm_phone — phone / mobile connection
**Visual:** Simple smartphone silhouette (rounded rectangle). Inside: 4–6 large rounded app tiles (no tiny details).  
**Meaning:** phone/call/mobile services; combines with shop for phone/electronics store.  
**Examples:** `comm_phone + punct_question`, `place_shop + comm_phone`.

### power_plug — power outlet / electricity / charging
**Visual:** A generic plug silhouette. Avoid country-specific plug standards if possible.  
**Examples:** `power_plug + punct_question`, `power_plug + logic_no`.

---

## Needs

### need_toilet — toilet
**Visual:** Prefer a toilet bowl silhouette as the core universal default.  
**Note:** regional variants can exist in context packs (e.g., floor toilet).  
**Avoid:** “WC” letters, gender pictograms.  
**Examples:** `need_toilet + punct_question`, `need_toilet + punct_exclaim`.

### need_water — water / drink
**Visual:** Generic plastic bottle silhouette with cap, no label.  
**Avoid:** brand cues.  
**Examples:** `need_water + qty_2`, `need_water + punct_question`.

### need_food — food / place to eat
**Visual:** Plate + cutlery (fork/knife) as a universal “food/eat” sign.  
**Avoid:** culturally narrow dishes in core.  
**Examples:** `need_food + punct_question`, `need_food + logic_no`.

### need_bar — bar / drinks
**Visual:** A wine glass half-filled (liquid level is the key identifier).  
**Avoid:** cocktail umbrellas/straws, complex cocktails.  
**Examples:** `need_bar + punct_question`, `need_bar + time + punct_question`.

---

## Safety

### safety_medical — medical help
**Visual:** Medical cross silhouette, intentionally heavier than `qty_plus`.  
**Avoid:** letters, snakes/caduceus (too culture-specific).  
**Examples:** `safety_medical + punct_exclaim`, `safety_medical + punct_question`.

### safety_police — police / security / army
**Visual:** A plain shield/badge silhouette without stars or text.  
**Avoid:** national symbols, “POLICE” text.  
**Examples:** `safety_police + punct_question`, `safety_police + punct_exclaim`.

---

## Places & services

### place_hotel — hotel / lodging / overnight stay
**Canonical visual:** A bed (road-sign style) as the universal lodging marker.  
**Examples:** `place_hotel + punct_question`, `place_hotel + comm_wifi`.

### place_shop — shop / store
**Canonical visual:** A supermarket cart silhouette (simple, no brand cues).  
**Compositions:**  
- `place_shop + need_food` = grocery  
- `place_shop + comm_phone` = phone/electronics store  
**Examples:** `place_shop + punct_question`, `place_shop + need_food`.

### place_landmark_park — park / landmark / place to walk
**Visual:** A generic outdoor landmark/park tile (e.g., a simplified monument + trees) that reads as “go see / walk around”.  
**Avoid:** specific famous silhouettes in core.  
**Examples:** `place_landmark_park + punct_question`, `place_landmark_park + time + punct_question`.

### place_gas — gas station / fuel
**Visual:** A fuel pump silhouette.  
**Avoid:** letters, brand station shapes.  
**Examples:** `place_gas + punct_question`, `move_car + place_gas`.

### service_tools — tools / repair / service
**Visual:** A single wrench silhouette (simple, no tiny gear teeth).  
**Composition:** `move_car + service_tools` = car service/repair.  
**Examples:** `service_tools + punct_question`, `move_car + service_tools`.

---

## Movement

### move_feet — walk / on foot
**Visual:** Footprints or a shoe/boot silhouette; footprints preferred for universality.  
**Examples:** `move_feet + punct_question`, `move_feet + time + punct_question`.

### move_taxi — taxi / cab
**Visual:** A car with a small roof sign block (no letters).  
**Avoid:** “TAXI” text.  
**Examples:** `move_taxi + punct_question`, `move_taxi + money_card + punct_question`.

### move_car — car / drive / rental (context-dependent)
**Visual:** A plain car silhouette (no brand/model cues).  
**Examples:** `move_car + punct_question`, `move_car + service_tools`.

### move_public — public transport (generic)
**Visual:** A long vehicle silhouette (bus/coach/wagon) without rails/metro specifics, designed to mean “public transport” broadly.  
**Examples:** `move_public + punct_question`, `move_public + time + punct_question`.

---

## Optional (Universal v1, not Core)

### place_disco — disco / club (optional)
**Visual:** A disco ball (simple sphere with a few large tiles).  
**Avoid:** dense grids and tiny reflections.  
**Examples:** `place_disco + punct_question`, `place_disco + time + punct_question`.
