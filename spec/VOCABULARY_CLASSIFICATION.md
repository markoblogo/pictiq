# Vocabulary Classification

This document formalizes the accepted Pictiq vocabulary architecture. The machine-readable source of truth is [`../lexicon/vocabulary-classification.json`](../lexicon/vocabulary-classification.json). Semantic meanings remain in [`../lexicon/icon-index.json`](../lexicon/icon-index.json); this file classifies architectural role only.

## Core distinctions

Pictiq separates five registries and selection layers:

**Canonical Registry != Core Vocabulary != Standalone Core != Context Packs != Entity Registry.**

1. **Canonical Registry** — every accepted ordinary reusable tile in `lexicon/icon-index.json`; currently 83 IDs.
2. **Core Vocabulary** — broad everyday primitives inside the canonical registry.
3. **Standalone Core** — concepts that must often be explicit when the body, object, or live situation disappears.
4. **Context Packs** — scenario-specific selections and additions such as Paris, nightlife, travel, retail, health, food, or infrastructure.
5. **Entity Registry** — scoped visual proper names under `entities/`; these are not ordinary lexical icons and do not increase the Core count.

Two principles control classification:

- **Canonical does not mean Core.**
- **Complexity belongs to the context that requires it, not to Core.**
- **Pictiq vocabulary is need-driven, not taxonomically symmetrical.**
- **Vocabulary growth should follow real communication pressure, composition attempt, semantic compression, context-pack option, actual gap, and only then candidate primitive.**

## Two independent axes

Vocabulary generality and communication surface are separate axes.

| Axis | Values | Purpose |
| --- | --- | --- |
| Vocabulary generality | MECHANISM, CORE, STANDALONE_CORE, CONTEXTUAL, SPECIALIZED | Classifies why a canonical tile belongs in the system. |
| Communication surface | EMBODIED, STANDALONE | Classifies where the tile is useful or necessary. |

A tile can be contextual and still useful in both embodied and standalone communication. A tile can be Standalone Core without becoming ordinary Core. Profiles select tiles for a communication surface; they do not redefine canonical meaning.

## Counts

| Role | Count |
| --- | ---: |
| MECHANISM | 16 |
| CORE | 18 |
| STANDALONE_CORE | 10 |
| CONTEXTUAL | 38 |
| SPECIALIZED | 1 |
| Total ordinary canonical IDs | 83 |

Entity symbols and numeric notation assets are excluded from these counts.

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
| `money_coins` | CORE | EVERYDAY, PAYMENT, RETAIL | HIGH | HIGH | HIGH | Primary semantic field is MONEY / CURRENCY / PAYMENT VALUE. Cash/coins remain visual and contextual readings. |
| `money_card` | CONTEXTUAL | PAYMENT, RETAIL, TRAVEL | MEDIUM | MEDIUM | HIGH | Specific payment instrument; useful canonical contextual vocabulary, not minimal Core. |
| `money_atm_bank` | CONTEXTUAL | PAYMENT, TRAVEL, INFRASTRUCTURE | MEDIUM | MEDIUM | HIGH | Specific finance/infrastructure service, not minimal Core. |
| `comm_wifi` | CONTEXTUAL | TECH, COMMUNICATION, TRAVEL, INFRASTRUCTURE | MEDIUM | MEDIUM | HIGH | Technology/infrastructure/travel concept; not minimal general Core. |
| `comm_phone` | CONTEXTUAL | TECH, COMMUNICATION, EVERYDAY, TRAVEL | MEDIUM | MEDIUM | HIGH | Modern communication device/service; useful contextual vocabulary, not minimal Core. |
| `power_plug` | CONTEXTUAL | TECH, TRAVEL, INFRASTRUCTURE, EVERYDAY | MEDIUM | MEDIUM | HIGH | Specific charging/outlet concept; distinct from power_energy and not minimal Core. |
| `power_energy` | CORE | EVERYDAY, TECH, SAFETY, INFRASTRUCTURE | HIGH | HIGH | HIGH | Broad energy/electricity/power concept; not equivalent to power_plug. |
| `need_toilet` | CONTEXTUAL | EVERYDAY, TRAVEL, INFRASTRUCTURE | MEDIUM | HIGH | HIGH | Everyday/public-facility/travel concept; useful canonical vocabulary but outside minimal Core. |
| `need_water` | CORE | EVERYDAY, WATER, SAFETY | HIGH | HIGH | HIGH | Broad water/basic-need concept. |
| `need_food` | CORE | EVERYDAY, FOOD, SAFETY | HIGH | HIGH | HIGH | Broad food/basic-need concept. |
| `need_bar` | CONTEXTUAL | NIGHTLIFE, FOOD, LEGAL, TRAVEL | MEDIUM | MEDIUM | HIGH | SEMANTIC_MIGRATION: compatibility ID. Accepted primary semantics are ALCOHOL / ALCOHOLIC DRINK; BAR/venue is secondary. Preferred future ID candidate: drink_alcohol. Do not create a duplicate active concept. |
| `safety_medical` | CORE | SAFETY, HEALTH, EVERYDAY | HIGH | HIGH | HIGH | Broad medical/safety concept. |
| `safety_police` | CONTEXTUAL | SAFETY, LEGAL, CITY, TRAVEL | MEDIUM | HIGH | HIGH | Public safety/legal service concept; canonical contextual vocabulary rather than minimal Core. |
| `place_hotel` | CORE | EVERYDAY, STANDALONE, TRAVEL, CITY | HIGH | HIGH | HIGH | SEMANTIC_MIGRATION: compatibility ID. Accepted primary semantics are HOME / SHELTER / SLEEPING PLACE / BUILDING; HOTEL/accommodation is secondary. Preferred future ID candidate: place_home. Do not create a duplicate active concept. |
| `place_shop` | CONTEXTUAL | RETAIL, EVERYDAY, TRAVEL | MEDIUM | MEDIUM | HIGH | Generic shop remains useful commercial contextual vocabulary; not minimal Core merely because many compounds can use it. |
| `place_landmark_park` | CONTEXTUAL | CITY, TRAVEL, LEISURE | MEDIUM | MEDIUM | HIGH |  |
| `place_gas` | CONTEXTUAL | TRANSPORT, TRAVEL | MEDIUM | MEDIUM | HIGH |  |
| `service_tools` | CORE | EVERYDAY, INFRASTRUCTURE | HIGH | HIGH | MEDIUM | Kept in Core for now; repair/help contexts are broad but should be reviewed with use evidence. |
| `move_feet` | CORE | EVERYDAY, TRANSPORT, NAVIGATION | HIGH | HIGH | HIGH | Broad walking/on-foot movement concept. |
| `move_taxi` | CONTEXTUAL | TRANSPORT, TRAVEL, CITY | MEDIUM | MEDIUM | HIGH | Transport-specific concept outside minimal Core. |
| `move_car` | CONTEXTUAL | TRANSPORT, TRAVEL, EVERYDAY | MEDIUM | MEDIUM | HIGH | Transport-specific concept outside minimal Core after removal of historical travel bias. |
| `move_public` | CONTEXTUAL | TRANSPORT, CITY, TRAVEL | MEDIUM | MEDIUM | HIGH | Transport/city/travel concept outside minimal Core. |
| `place_disco` | CONTEXTUAL | NIGHTLIFE, LEISURE | MEDIUM | MEDIUM | HIGH |  |
| `paris_eiffel_tower` | CONTEXTUAL | PARIS, CITY, TRAVEL, CULTURE | MEDIUM | MEDIUM | HIGH |  |
| `paris_arc_de_triomphe` | CONTEXTUAL | PARIS, CITY, TRAVEL, CULTURE | MEDIUM | MEDIUM | HIGH |  |
| `paris_louvre_pyramid` | CONTEXTUAL | PARIS, CITY, TRAVEL, CULTURE | MEDIUM | MEDIUM | HIGH |  |
| `paris_notre_dame` | CONTEXTUAL | PARIS, CITY, TRAVEL, CULTURE | MEDIUM | MEDIUM | HIGH |  |
| `paris_sacre_coeur` | CONTEXTUAL | PARIS, CITY, TRAVEL, CULTURE | MEDIUM | MEDIUM | HIGH |  |
| `paris_moulin_windmill` | CONTEXTUAL | PARIS, NIGHTLIFE, CULTURE | MEDIUM | MEDIUM | HIGH |  |
| `paris_croissant` | CONTEXTUAL | PARIS, FOOD, CULTURE | MEDIUM | MEDIUM | HIGH | Paris-specific food/culture symbol in the Paris context, not generic food Core. |
| `move_boat` | CONTEXTUAL | TRANSPORT, TRAVEL, WATER | MEDIUM | MEDIUM | HIGH | LEGACY_CONTEXTUAL: narrower/historical boat concept. move_watercraft is the preferred broad water-transport concept; preserve until future compatibility review. |
| `place_catacombs` | CONTEXTUAL | CITY, TRAVEL, LEISURE | MEDIUM | MEDIUM | HIGH |  |
| `place_theme_park` | CONTEXTUAL | LEISURE, TRAVEL | MEDIUM | MEDIUM | HIGH |  |
| `place_airport` | CONTEXTUAL | TRANSPORT, TRAVEL | MEDIUM | MEDIUM | HIGH |  |
| `place_art_gallery` | CONTEXTUAL | CULTURE, LEISURE, TRAVEL | MEDIUM | MEDIUM | HIGH |  |
| `place_fashion_shopping` | CONTEXTUAL | RETAIL, CULTURE, TRAVEL | LOW | LOW | MEDIUM | DEPRECATE_COMPOSABLE / VISUAL_REDESIGN_CANDIDATE: prefer place_shop + item_clothing. Preserve historical evidence and compatibility; do not redesign unnecessary compound primitive now. |
| `item_cigarette` | CONTEXTUAL | NIGHTLIFE, RETAIL, HEALTH, LEGAL | MEDIUM | MEDIUM | HIGH | Contextual nightlife/retail/health/legal item, not a specialized technical concept. |
| `item_cannabis` | CONTEXTUAL | NIGHTLIFE, RETAIL, HEALTH, LEGAL | MEDIUM | MEDIUM | HIGH | Contextual nightlife/retail/health/legal item, not a specialized technical concept. |
| `drink_beer` | CONTEXTUAL | NIGHTLIFE, FOOD, LEGAL | MEDIUM | MEDIUM | HIGH | Specific alcoholic-drink subtype; remains contextual and separate from migrated broad alcohol concept. |
| `love_heart` | CONTEXTUAL | SOCIAL, EVERYDAY, NARRATIVE | MEDIUM | HIGH | HIGH | Broad love/affection concept. HEART + PERSON and HEART + PERSON + MANY remain contextual compositions, not new lexical primitives. |
| `item_condom` | CONTEXTUAL | HEALTH, SAFETY, NIGHTLIFE, TRAVEL | MEDIUM | MEDIUM | MEDIUM | Contextual for now; safety/health/nightlife/travel use needs future evidence before Core. |
| `nature_flower` | CONTEXTUAL | NATURE, SOCIAL, LEISURE, EVERYDAY | MEDIUM | MEDIUM | HIGH | Broad plant/vegetation/flower concept; do not force botanical precision or taxonomy completion. |
| `eye_look` | STANDALONE_CORE | STANDALONE, PERCEPTION | LOW | HIGH | HIGH |  |
| `item_clothing` | STANDALONE_CORE | STANDALONE, EVERYDAY | LOW | HIGH | HIGH |  |
| `comm_speak` | STANDALONE_CORE | STANDALONE, COMMUNICATION | LOW | HIGH | HIGH |  |
| `comm_sound` | STANDALONE_CORE | STANDALONE, COMMUNICATION | LOW | HIGH | HIGH |  |
| `media_text` | STANDALONE_CORE | STANDALONE, MEDIA | LOW | HIGH | HIGH |  |
| `media_image` | STANDALONE_CORE | STANDALONE, MEDIA | LOW | HIGH | HIGH |  |
| `nature_sun` | STANDALONE_CORE | STANDALONE, NATURE, TIME | LOW | HIGH | HIGH |  |
| `state_light` | CORE | EVERYDAY, INFRASTRUCTURE, SAFETY | HIGH | HIGH | HIGH | Broad light/lighting concept. |
| `food_produce` | CONTEXTUAL | FOOD, RETAIL, EVERYDAY | MEDIUM | MEDIUM | HIGH | Primary field is FRUIT / VEGETABLE / FRESH PRODUCE. Do not expand to PLANT. |
| `food_bakery` | CORE | FOOD, EVERYDAY, RETAIL | HIGH | HIGH | HIGH | Primary field is BREAD / BAKED FOOD / BAKED GOODS / PASTRY. Bakery/place reading is secondary. |
| `food_meat` | CORE | FOOD, EVERYDAY, RETAIL | HIGH | HIGH | HIGH | Human-accepted Architecture & Vocabulary Audit addition. Broad MEAT / ANIMAL FOOD / MEAT PRODUCTS primitive; do not split into steak, chicken, pork, beef, or drumstick without future context evidence. |
| `rel_greater` | MECHANISM | NAVIGATION, RELATION | HIGH | HIGH | HIGH | Comparative GREATER/MORE relation; rightward reading is contextual only, not a global arrow definition. |
| `rel_lesser` | MECHANISM | NAVIGATION, RELATION | HIGH | HIGH | HIGH | Comparative LESSER/LESS relation; leftward reading is contextual only, not a global arrow definition. |
| `body_mouth` | STANDALONE_CORE | STANDALONE, BODY, FOOD | LOW | HIGH | HIGH |  |
| `rel_here` | MECHANISM | NAVIGATION, RELATION | HIGH | HIGH | HIGH | Broad here/target/reference-point operator; context determines exact reading. |
| `rel_up` | MECHANISM | NAVIGATION, RELATION | HIGH | HIGH | HIGH | UP/DOWN vertical relation family member; not redefined as MORE/LESS for symmetry. |
| `rel_down` | MECHANISM | NAVIGATION, RELATION | HIGH | HIGH | HIGH | UP/DOWN vertical relation family member; not redefined as MORE/LESS for symmetry. |
| `nature_moon` | STANDALONE_CORE | STANDALONE, NATURE, TIME | LOW | HIGH | HIGH |  |
| `surface_wavy` | CONTEXTUAL | ROAD, SURFACE, SAFETY, WATER | MEDIUM | HIGH | HIGH | Broad wavy/waves/unstable/uneven/slippery/irregular-surface concept supported by Road and Odyssey; not collapsed into WATER. |
| `state_dead` | CONTEXTUAL | SAFETY, HEALTH, NARRATIVE, ROAD, INDUSTRIAL | MEDIUM | HIGH | MEDIUM | Accepted from Stress Test 02 as death/not-alive/deadly-contextual; cross-domain potential exists but current evidence does not justify Core. |
| `tech_ai` | SPECIALIZED | TECH, SPECIALIZED, MACHINE_INTERFACE | LOW | LOW | HIGH | AI/Machine/Technology context vocabulary; not minimal Core. |
| `action_conflict` | CORE | NARRATIVE, SAFETY, CULTURE, SOCIAL | HIGH | HIGH | MEDIUM | Broad conflict/war/aggression/fight/hostile action concept; distinct from qual_bad evaluation. |
| `move_watercraft` | CONTEXTUAL | TRANSPORT, TRAVEL, WATER, NARRATIVE | MEDIUM | HIGH | MEDIUM | Preferred broad watercraft / boat / ship / generic water transport concept; not minimal Core. Existing move_boat remains legacy contextual pending future compatibility review. |
| `qual_sacred` | CORE | CULTURE, NARRATIVE, SOCIAL | HIGH | HIGH | MEDIUM | Broad sacred/holy/divine/religious concept; avoids separate GOD/PRIEST/TEMPLE primitives unless future contexts require them. |
| `nature_animal` | CORE | EVERYDAY, NATURE, FOOD, NARRATIVE | HIGH | HIGH | MEDIUM | General land-animal category; not rigorous taxonomy. Birds/fish/insects may emerge separately if real use creates pressure. |
| `nature_cloud` | CORE | NATURE, WATER, NARRATIVE, TRAVEL | HIGH | HIGH | MEDIUM | Broad cloud/sky/air/atmospheric-space concept; do not add AIR/SKY/WEATHER merely for taxonomy. |

## Review queue

- `move_boat` remains a legacy contextual subtype while `move_watercraft` is the preferred broad water-transport primitive. A later compatibility audit should decide whether to deprecate, alias, or retain both.
- `place_fashion_shopping` is preserved for compatibility but should be removed from active recommendations in favor of `place_shop + item_clothing`; its artwork remains a visual redesign candidate if kept in any legacy context.
- `service_tools` stays in Core for now with medium confidence; repair/help/service should be retested with use evidence before any future demotion.
- No unresolved Stress Test 03 Stage 1 hypothesis is promoted here to normative grammar. The audit changes vocabulary classification and semantics only.
