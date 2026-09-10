# Pictiq Architecture & Vocabulary Audit — migrations and compatibility

Status: accepted and implemented in the final audit closeout. Artwork is unchanged for every migration/deprecation below.

## `need_bar` → `drink_alcohol`

- Previous semantics: bar / drinks.
- New preferred active ID: `drink_alcohol`.
- New semantics: ALCOHOL / ALCOHOLIC DRINK.
- Secondary/contextual readings: BAR / DRINKING VENUE / ALCOHOL SERVICE.
- Compatibility treatment: `need_bar` is retained as a legacy alias in the active lexicon entry and as a compatibility mapping in `lexicon/compatibility.json`; its previous SVG is archived under `legacy/svg/need_bar.svg`.
- Effect on users/tools: current public search still finds the concept through `need_bar`, `bar`, and related aliases, while active packs/profiles use `drink_alcohol`.
- Artwork changed: UNCHANGED.

## `place_hotel` → `place_home`

- Previous semantics: hotel / lodging / overnight stay.
- New preferred active ID: `place_home`.
- New semantics: HOME / SHELTER / SLEEPING PLACE / BUILDING; HOMELAND contextually.
- Secondary/contextual readings: HOTEL / ACCOMMODATION / BEDROOM / PLACE TO SLEEP / specific building type when modified.
- Compatibility treatment: `place_hotel` is retained as a legacy alias in the active lexicon entry and as a compatibility mapping in `lexicon/compatibility.json`; its previous SVG is archived under `legacy/svg/place_hotel.svg`.
- Effect on users/tools: current public search still finds the concept through `place_hotel`, `hotel`, and related aliases, while active packs/profiles use `place_home`.
- Artwork changed: UNCHANGED.

Contextual composition examples:

- `place_home + qual_sacred` → sacred building / temple / church contextually.
- `place_home + place_shop` → shop/building contextually.
- `place_home + nature_animal` → animal shelter / zoo-like place contextually.

## `place_fashion_shopping` → `place_shop + item_clothing`

- Previous semantics: fashion shopping.
- New preferred representation: `place_shop + item_clothing`.
- Compatibility treatment: `place_fashion_shopping` is retained as a deprecated legacy identifier in the canonical registry because the current schema does not yet provide a safer inactive-identifier registry for public Pages compatibility. It is removed from active pack/layout recommendations where practical.
- Reason: dedicated compound is no longer needed; composition expresses the useful meaning better.
- Effect on users/tools: existing references can still resolve, while current recommendations should use the composition.
- Artwork changed: UNCHANGED.

## `move_boat` / `move_watercraft`

- `move_watercraft`: preferred broad contextual WATERCRAFT / BOAT / SHIP / GENERIC WATER TRANSPORT concept.
- `move_boat`: retained legacy contextual subtype for narrower historical/recreational/travel boat readings.
- Compatibility treatment: both remain available; final alias/deprecation decision for `move_boat` is deferred to a compatibility audit.
- Effect on users/tools: broad water-transport use should prefer `move_watercraft`; old `move_boat` contexts are not broken.
- Artwork changed: UNCHANGED.
