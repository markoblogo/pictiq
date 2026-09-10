# Vocabulary Classification

This document formalizes the accepted Pictiq vocabulary architecture. The machine-readable source of truth is [`../lexicon/vocabulary-classification.json`](../lexicon/vocabulary-classification.json). Semantic meanings remain in [`../lexicon/icon-index.json`](../lexicon/icon-index.json); this file classifies architectural role only.

## Core distinctions

Pictiq separates seven layers:

**Canonical Registry != Core Vocabulary != Standalone Core != Context Packs != Specialized Vocabulary != Entity Registry != Legacy/Deprecated compatibility.**

1. **Canonical Registry** — every accepted ordinary reusable tile in `lexicon/icon-index.json`; currently 83 active/retained ordinary identifiers.
2. **Core Vocabulary** — broad everyday primitives inside the canonical registry.
3. **Standalone Core** — concepts that must often be explicit when the body, object, or live situation disappears.
4. **Context Packs** — scenario-specific selections such as Paris, nightlife, travel, retail, health, food, technology, or infrastructure.
5. **Specialized Vocabulary** — domain-specific ordinary symbols when needed; currently 0 active IDs in this role.
6. **Entity Registry** — scoped visual proper names under `entities/`; these are not ordinary lexical icons and do not increase the Core count.
7. **Legacy/Deprecated compatibility** — historical IDs, aliases, retained deprecated identifiers, and migration records that preserve older references without creating duplicate active concepts.

Two principles control classification:

- **Canonical does not mean Core.**
- **Complexity belongs to the context that requires it, not to Core.**
- **Pictiq vocabulary is need-driven, not taxonomically symmetrical.**
- **Vocabulary growth should follow real communication pressure, composition attempt, semantic compression, context-pack option, actual gap, and only then candidate primitive.**
- **Semantic migration is distinct from deprecation: a useful concept can survive while its primary meaning and future preferred ID change.**
- **Deprecate composable compounds when ordinary composition expresses the useful meaning better than a dedicated lexical tile.**

## Counts

| Role | Count |
| --- | ---: |
| MECHANISM | 16 |
| CORE | 26 |
| STANDALONE_CORE | 5 |
| CONTEXTUAL | 36 |
| SPECIALIZED | 0 |
| Active ordinary semantic concepts | 82 |
| Retained ordinary identifiers in canonical registry | 83 |

Entity symbols and numeric notation assets are excluded from these counts. `place_fashion_shopping` is retained as a deprecated compatibility identifier, so the active semantic concept count and retained ordinary identifier count differ by one.

## Reconciled disposition summary

Disposition counts can overlap.

| Disposition | Count |
| --- | ---: |
| KEEP_CORE | 42 |
| KEEP_CONTEXTUAL | 36 |
| KEEP_STANDALONE_CORE | 5 |
| SEMANTIC_MIGRATION | 2 |
| DEPRECATE_COMPOSABLE | 1 |
| LEGACY_CONTEXTUAL | 1 |
| VISUAL_REDESIGN_CANDIDATE | 0 |
| HUMAN_REVIEW_REQUIRED | 0 |

## Classification table

| ID | Primary role | Secondary contexts | Embodied relevance | Standalone relevance | Confidence | Note |
| --- | --- | --- | --- | --- | --- | --- |
| `punct_question` | MECHANISM | EVERYDAY, COMMUNICATION | HIGH | HIGH | HIGH |  |
| `punct_exclaim` | MECHANISM | EVERYDAY, SAFETY | HIGH | HIGH | HIGH |  |
| `logic_yes` | MECHANISM | EVERYDAY, COMMUNICATION | HIGH | HIGH | HIGH |  |
| `logic_no` | MECHANISM | EVERYDAY, SAFETY, COMMUNICATION | HIGH | HIGH | HIGH |  |
| `qual_good` | MECHANISM | EVERYDAY, EVALUATION | HIGH | HIGH | HIGH |  |
| `qual_bad` | MECHANISM | EVERYDAY, EVALUATION | HIGH | HIGH | HIGH |  |
| `time` | CORE | EVERYDAY, TRAVEL | HIGH | HIGH | HIGH |  |
| `state_hot` | CORE | EVERYDAY, SAFETY | HIGH | HIGH | HIGH |  |
| `state_cold` | CORE | EVERYDAY, SAFETY | HIGH | HIGH | HIGH |  |
| `person_generic` | STANDALONE_CORE | STANDALONE, PEOPLE | LOW | HIGH | HIGH | Standalone Core because durable messages often need an explicit human participant. |
| `qty_1` | MECHANISM | EVERYDAY, QUANTITY | HIGH | HIGH | HIGH |  |
| `qty_2` | MECHANISM | EVERYDAY, QUANTITY | HIGH | HIGH | HIGH |  |
| `qty_5` | MECHANISM | EVERYDAY, QUANTITY | HIGH | HIGH | HIGH |  |
| `qty_plus` | MECHANISM | EVERYDAY, QUANTITY | HIGH | HIGH | HIGH |  |
| `qty_minus` | MECHANISM | EVERYDAY, QUANTITY | HIGH | HIGH | HIGH |  |
| `money_coins` | CORE | EVERYDAY, PAYMENT, RETAIL | HIGH | HIGH | HIGH | Human decision: KEEP_CORE. Primary field is MONEY / CURRENCY / PAYMENT VALUE. |
| `money_card` | CONTEXTUAL | PAYMENT, RETAIL, TRAVEL | MEDIUM | MEDIUM | HIGH | Specific card/payment-instrument concept; Finance/Travel/Commerce contextual vocabulary, not Core. |
| `money_atm_bank` | CONTEXTUAL | PAYMENT, TRAVEL, INFRASTRUCTURE | MEDIUM | MEDIUM | HIGH | Specific ATM/bank infrastructure concept; Finance/Travel/Commerce contextual vocabulary, not Core. |
| `comm_wifi` | CONTEXTUAL | TECH, COMMUNICATION, TRAVEL | MEDIUM | MEDIUM | HIGH | Technology/travel/modern-everyday contextual concept; not Core. |
| `comm_phone` | CONTEXTUAL | TECH, COMMUNICATION, EVERYDAY, TRAVEL | MEDIUM | MEDIUM | HIGH | Technology/travel/modern-everyday contextual concept; not Core. |
| `power_plug` | CONTEXTUAL | TECH, TRAVEL, INFRASTRUCTURE, EVERYDAY | MEDIUM | MEDIUM | HIGH | Technology/travel/infrastructure contextual concept; do not confuse POWER PLUG with ENERGY. |
| `power_energy` | CORE | SAFETY, INFRASTRUCTURE, EVERYDAY, TECH | HIGH | HIGH | HIGH | Human decision: broad POWER / ENERGY remains separate and Core; not the same as power plug. |
| `need_toilet` | CONTEXTUAL | EVERYDAY, TRAVEL, INFRASTRUCTURE | MEDIUM | HIGH | HIGH | Human decision: KEEP_CONTEXTUAL. Everyday/Public Facilities/Travel concept; preserve canonical asset. |
| `need_water` | CORE | EVERYDAY, WATER, SAFETY | HIGH | HIGH | HIGH | Broad water/basic-need concept. |
| `need_food` | CORE | EVERYDAY, FOOD, SAFETY | HIGH | HIGH | HIGH | Broad food/basic-need concept. |
| `drink_alcohol` | CONTEXTUAL | NIGHTLIFE, TRAVEL, FOOD | MEDIUM | MEDIUM | HIGH | SEMANTIC_MIGRATION complete: preferred active ID for ALCOHOL / ALCOHOLIC DRINK. Historical need_bar is retained as compatibility alias; artwork unchanged. |
| `safety_medical` | CORE | SAFETY, HEALTH, EVERYDAY | HIGH | HIGH | HIGH | Broad medical/safety concept. |
| `safety_police` | CONTEXTUAL | SAFETY, LEGAL, CITY, TRAVEL | MEDIUM | HIGH | HIGH | Public safety/legal service concept; canonical contextual vocabulary rather than minimal Core. |
| `place_home` | CORE | EVERYDAY, TRAVEL, CITY | HIGH | HIGH | HIGH | SEMANTIC_MIGRATION complete: preferred active ID for HOME / SHELTER / SLEEPING PLACE / BUILDING, HOMELAND contextually. Historical place_hotel is retained as compatibility alias; artwork unchanged. |
| `place_shop` | CONTEXTUAL | RETAIL, EVERYDAY, TRAVEL | MEDIUM | MEDIUM | HIGH | Human decision: KEEP_CONTEXTUAL. Commercial/contextual vocabulary, not minimal Core. |
| `place_landmark_park` | CONTEXTUAL | CITY, TRAVEL, LEISURE | MEDIUM | MEDIUM | HIGH | Tourism/nightlife/city contextual vocabulary; not minimal Core after historical travel-bias cleanup. |
| `place_gas` | CONTEXTUAL | CITY, TRAVEL, LEISURE | MEDIUM | MEDIUM | HIGH | Tourism/nightlife/city contextual vocabulary; not minimal Core after historical travel-bias cleanup. |
| `service_tools` | CORE | EVERYDAY, INFRASTRUCTURE, INDUSTRIAL | HIGH | HIGH | HIGH | Human decision: KEEP_CORE. Primary field is TOOLS / REPAIR / MAINTENANCE / FIXING; SERVICE is contextual. |
| `move_feet` | CORE | EVERYDAY, TRANSPORT, NAVIGATION | HIGH | HIGH | HIGH | Broad walking/on-foot movement concept. |
| `move_taxi` | CONTEXTUAL | TRANSPORT, TRAVEL, CITY | MEDIUM | MEDIUM | HIGH | Transport/Travel/City contextual concept; not minimal Core. |
| `move_car` | CONTEXTUAL | TRANSPORT, TRAVEL, EVERYDAY | MEDIUM | MEDIUM | HIGH | Transport/Travel/City contextual concept; not minimal Core. |
| `move_public` | CONTEXTUAL | TRANSPORT, CITY, TRAVEL | MEDIUM | MEDIUM | HIGH | Transport/Travel/City contextual concept; not minimal Core. |
| `place_disco` | CONTEXTUAL | CITY, TRAVEL, LEISURE | MEDIUM | MEDIUM | HIGH | Tourism/nightlife/city contextual vocabulary; not minimal Core after historical travel-bias cleanup. |
| `paris_eiffel_tower` | CONTEXTUAL | PARIS, CITY, TRAVEL | LOW | MEDIUM | HIGH | Paris-specific contextual vocabulary; not general Core. |
| `paris_arc_de_triomphe` | CONTEXTUAL | PARIS, CITY, TRAVEL | LOW | MEDIUM | HIGH | Paris-specific contextual vocabulary; not general Core. |
| `paris_louvre_pyramid` | CONTEXTUAL | PARIS, CITY, TRAVEL | LOW | MEDIUM | HIGH | Paris-specific contextual vocabulary; not general Core. |
| `paris_notre_dame` | CONTEXTUAL | PARIS, CITY, TRAVEL | LOW | MEDIUM | HIGH | Paris-specific contextual vocabulary; not general Core. |
| `paris_sacre_coeur` | CONTEXTUAL | PARIS, CITY, TRAVEL | LOW | MEDIUM | HIGH | Paris-specific contextual vocabulary; not general Core. |
| `paris_moulin_windmill` | CONTEXTUAL | PARIS, CITY, TRAVEL | LOW | MEDIUM | HIGH | Paris-specific contextual vocabulary; not general Core. |
| `paris_croissant` | CONTEXTUAL | PARIS, CITY, TRAVEL | LOW | MEDIUM | HIGH | Paris-specific contextual vocabulary; not general Core. |
| `move_boat` | CONTEXTUAL | TRANSPORT, TRAVEL, WATER | MEDIUM | MEDIUM | HIGH | LEGACY_CONTEXTUAL: narrower historical/recreational/travel-oriented boat subtype. move_watercraft is accepted as the broad hierarchy parent; final compatibility decision deferred. |
| `place_catacombs` | CONTEXTUAL | PARIS, CITY, TRAVEL | LOW | MEDIUM | HIGH | Paris-specific contextual vocabulary; not general Core. |
| `place_theme_park` | CONTEXTUAL | CITY, TRAVEL, LEISURE | MEDIUM | MEDIUM | HIGH | Tourism/nightlife/city contextual vocabulary; not minimal Core after historical travel-bias cleanup. |
| `place_airport` | CONTEXTUAL | TRANSPORT, TRAVEL, CITY | MEDIUM | MEDIUM | HIGH | Transport/Travel/City contextual concept; not minimal Core. |
| `place_art_gallery` | CONTEXTUAL | CITY, TRAVEL, LEISURE | MEDIUM | MEDIUM | HIGH | Tourism/nightlife/city contextual vocabulary; not minimal Core after historical travel-bias cleanup. |
| `place_fashion_shopping` | CONTEXTUAL | RETAIL, CITY, TRAVEL | LOW | LOW | HIGH | DEPRECATE_COMPOSABLE: retained legacy/deprecated identifier; active recommendation is place_shop + item_clothing. Do not redesign by default. |
| `item_cigarette` | CONTEXTUAL | NIGHTLIFE, HEALTH, TRAVEL | MEDIUM | MEDIUM | HIGH | Adult practical communication / Health-Safety / Travel contextual concept; not Core. |
| `item_cannabis` | CONTEXTUAL | NIGHTLIFE, HEALTH, LEGAL, TRAVEL | LOW | LOW | HIGH | Adult practical communication / Health-Safety / Legal / Travel contextual concept; not Core. |
| `drink_beer` | CONTEXTUAL | NIGHTLIFE, FOOD, TRAVEL | MEDIUM | MEDIUM | HIGH | Adult practical communication / Food-Drink contextual concept; not Core. |
| `love_heart` | CONTEXTUAL | SOCIAL, EVERYDAY, NARRATIVE | MEDIUM | HIGH | HIGH | Broad love/affection concept. HEART + PERSON and HEART + PERSON + MANY remain contextual compositions, not new lexical primitives. |
| `item_condom` | CONTEXTUAL | HEALTH, SAFETY, TRAVEL | MEDIUM | MEDIUM | HIGH | Health/Safety/adult practical communication contextual concept; not Core. |
| `nature_flower` | CORE | NATURE, EVERYDAY, SOCIAL | HIGH | HIGH | HIGH | Primary broad field is PLANT / VEGETATION / FLOWER contextually; do not force botanical precision. |
| `eye_look` | STANDALONE_CORE | STANDALONE, PERCEPTION | LOW | HIGH | HIGH |  |
| `item_clothing` | STANDALONE_CORE | STANDALONE, EVERYDAY | LOW | HIGH | HIGH |  |
| `comm_speak` | CORE | COMMUNICATION, PEOPLE, PERCEPTION | MEDIUM | HIGH | HIGH | Primary field is SPEECH / COMMUNICATION / ORAL OR AUDIBLE COMMUNICATION; do not collapse into SOUND + TEXT. |
| `comm_sound` | CORE | COMMUNICATION, PERCEPTION, MEDIA | MEDIUM | HIGH | HIGH | Primary field is SOUND / AUDIBLE SIGNAL / MUSIC / WHAT IS HEARD. |
| `media_text` | CORE | COMMUNICATION, MEDIA, EVERYDAY | MEDIUM | HIGH | HIGH | Primary field is TEXT / WRITTEN INFORMATION; READ/WRITE/INFORMATION are contextual. |
| `media_image` | CORE | COMMUNICATION, MEDIA, EVERYDAY | MEDIUM | HIGH | HIGH | Primary field is IMAGE / PICTURE / PHOTO / DRAWING / PAINTING / VISUAL REPRESENTATION. |
| `nature_sun` | STANDALONE_CORE | STANDALONE, NATURE, TIME | LOW | HIGH | HIGH |  |
| `state_light` | CORE | EVERYDAY, INFRASTRUCTURE, SAFETY | HIGH | HIGH | HIGH | Broad light/lighting concept. |
| `food_produce` | CORE | FOOD, EVERYDAY, RETAIL | HIGH | HIGH | HIGH | Primary field is FRUIT / VEGETABLE / FRESH PRODUCE. Not PLANT. |
| `food_bakery` | CORE | FOOD, EVERYDAY, RETAIL | HIGH | HIGH | HIGH | Primary field is BREAD / BAKED FOOD / BAKED GOODS / PASTRY. Bakery/place reading is secondary. |
| `food_meat` | CORE | FOOD, EVERYDAY, RETAIL | HIGH | HIGH | HIGH | Human-accepted Architecture & Vocabulary Audit addition. Broad MEAT / ANIMAL FOOD / MEAT PRODUCTS primitive; do not split into steak, chicken, pork, beef, or drumstick without future context evidence. |
| `rel_greater` | MECHANISM | NAVIGATION, RELATION | HIGH | HIGH | HIGH | Comparative GREATER/MORE relation; rightward reading is contextual only, not a global arrow definition. |
| `rel_lesser` | MECHANISM | NAVIGATION, RELATION | HIGH | HIGH | HIGH | Comparative LESSER/LESS relation; leftward reading is contextual only, not a global arrow definition. |
| `body_mouth` | STANDALONE_CORE | STANDALONE, BODY, FOOD | LOW | HIGH | HIGH |  |
| `rel_here` | MECHANISM | NAVIGATION, RELATION | HIGH | HIGH | HIGH | Broad here/target/reference-point operator; context determines exact reading. |
| `rel_up` | MECHANISM | NAVIGATION, RELATION | HIGH | HIGH | HIGH | UP/DOWN vertical relation family member; not redefined as MORE/LESS for symmetry. |
| `rel_down` | MECHANISM | NAVIGATION, RELATION | HIGH | HIGH | HIGH | UP/DOWN vertical relation family member; not redefined as MORE/LESS for symmetry. |
| `nature_moon` | CORE | NATURE, TIME, EVERYDAY | HIGH | HIGH | HIGH | Primary field is MOON / NIGHT / NIGHTTIME. Do not add DAY merely for symmetry. |
| `surface_wavy` | CORE | SURFACE, SAFETY, WATER, ROAD | HIGH | HIGH | HIGH | Broad WAVY / WAVES / INSTABILITY / UNEVENNESS / SLIPPERINESS / IRREGULAR SURFACE concept; water-surface reading is contextual and WATER remains separate. |
| `state_dead` | CONTEXTUAL | SAFETY, HEALTH, NARRATIVE, ROAD, INDUSTRIAL | MEDIUM | HIGH | MEDIUM | Accepted from Stress Test 02 as death/not-alive/deadly-contextual; cross-domain potential exists but current evidence does not justify Core. |
| `tech_ai` | CONTEXTUAL | TECH, MACHINE_INTERFACE, COMMUNICATION | LOW | MEDIUM | HIGH | AI/Machine/Technology context vocabulary; not Core. |
| `action_conflict` | CORE | NARRATIVE, SAFETY, CULTURE, SOCIAL | HIGH | HIGH | HIGH | Human decision: KEEP_CORE. Broad CONFLICT / WAR / AGGRESSION / FIGHT / ATTACK / HOSTILE ACTION / VIOLENCE concept, distinct from BAD evaluation. |
| `move_watercraft` | CONTEXTUAL | TRANSPORT, TRAVEL, WATER, NARRATIVE | MEDIUM | MEDIUM | HIGH | Human decision: KEEP_CONTEXTUAL. Preferred broad WATERCRAFT / BOAT / SHIP / GENERIC WATER TRANSPORT concept; do not promote to Core solely because broad. |
| `qual_sacred` | CORE | CULTURE, NARRATIVE, SOCIAL | HIGH | HIGH | HIGH | Human decision: KEEP_CORE. Broad SACRED / HOLY / DIVINE / RELIGIOUS / GOD-DIVINITY contextually / SACRED STATUS concept. |
| `nature_animal` | CORE | NATURE, EVERYDAY, FOOD, NARRATIVE | HIGH | HIGH | HIGH | Human decision: KEEP_CORE. General land-animal category; not scientific taxonomy. Birds/fish/insects may emerge later if needed. |
| `nature_cloud` | CORE | NATURE, WATER, TRAVEL, NARRATIVE | HIGH | HIGH | HIGH | Human decision: KEEP_CORE. Broad CLOUD / SKY / AIR / ATMOSPHERIC SPACE / WEATHER context / OVERHEAD SKY CONTEXT. |
