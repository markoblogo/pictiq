# Vocabulary Classification

This document formalizes the accepted Pictiq vocabulary architecture. The machine-readable source of truth is [`../lexicon/vocabulary-classification.json`](../lexicon/vocabulary-classification.json). Semantic meanings remain in [`../lexicon/icon-index.json`](../lexicon/icon-index.json); this file classifies architectural role only.

## Core distinctions

Pictiq separates five registries and selection layers:

**Canonical Registry != Core Vocabulary != Standalone Core != Context Packs != Entity Registry.**


1. **Canonical Registry** — every accepted ordinary reusable tile in `lexicon/icon-index.json`; currently 75 IDs.
2. **Core Vocabulary** — broad everyday primitives inside the canonical registry.
3. **Standalone Core** — concepts that must often be explicit when the body, object, or live situation disappears.
4. **Context Packs** — scenario-specific selections and additions such as Paris, nightlife, travel, retail, health, or infrastructure.
5. **Entity Registry** — scoped visual proper names under `entities/`; these are not ordinary lexical icons and do not increase the Core count.

Two principles control classification:

- **Canonical does not mean Core.** A tile can be accepted and canonical without being universal Core.
- **Complexity belongs to the context that requires it, not to Core.** Domain-specific needs should move to context packs, profiles, entity registries, or future parameter mechanisms before expanding Core.

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
| CORE | 15 |
| STANDALONE_CORE | 11 |
| CONTEXTUAL | 32 |
| SPECIALIZED | 1 |

| Total ordinary canonical IDs | 75 |

Entity symbols are excluded from these counts.

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
| `money_coins` | CORE | EVERYDAY, PAYMENT | HIGH | HIGH | HIGH |  |
| `money_card` | CORE | EVERYDAY, PAYMENT | HIGH | HIGH | HIGH |  |
| `money_atm_bank` | CONTEXTUAL | PAYMENT, TRAVEL | MEDIUM | MEDIUM | HIGH |  |
| `comm_wifi` | CONTEXTUAL | COMMUNICATION, TRAVEL | MEDIUM | MEDIUM | HIGH |  |
| `comm_phone` | CORE | COMMUNICATION, EVERYDAY | HIGH | HIGH | HIGH |  |
| `power_plug` | CONTEXTUAL | TECH, TRAVEL, INFRASTRUCTURE, EVERYDAY | MEDIUM | MEDIUM | HIGH | Contextual infrastructure/charging concept; not universal Core. |
| `power_energy` | CONTEXTUAL | TECH, SAFETY, INFRASTRUCTURE, EVERYDAY | MEDIUM | MEDIUM | HIGH | Contextual electricity/energy concept; not ordinary Core and not narrow specialized jargon. |
| `need_toilet` | CORE | EVERYDAY, TRAVEL | HIGH | HIGH | HIGH |  |
| `need_water` | CORE | EVERYDAY, TRAVEL | HIGH | HIGH | HIGH |  |
| `need_food` | CORE | EVERYDAY, TRAVEL | HIGH | HIGH | HIGH |  |
| `need_bar` | CONTEXTUAL | NIGHTLIFE, TRAVEL | MEDIUM | MEDIUM | HIGH |  |
| `safety_medical` | CORE | SAFETY, HEALTH, TRAVEL | HIGH | HIGH | HIGH |  |
| `safety_police` | CORE | SAFETY, TRAVEL | HIGH | HIGH | HIGH |  |
| `place_hotel` | CONTEXTUAL | TRAVEL, CITY | MEDIUM | MEDIUM | HIGH |  |
| `place_shop` | CORE | EVERYDAY, RETAIL, TRAVEL | HIGH | HIGH | HIGH | Accepted as Core because shopping is a broad everyday/travel need. |
| `place_landmark_park` | CONTEXTUAL | CITY, TRAVEL, LEISURE | MEDIUM | MEDIUM | HIGH |  |
| `place_gas` | CONTEXTUAL | TRANSPORT, TRAVEL | MEDIUM | MEDIUM | HIGH |  |
| `service_tools` | CORE | EVERYDAY, INFRASTRUCTURE | HIGH | HIGH | MEDIUM | Kept in Core for now; repair/help contexts are broad but should be reviewed with use evidence. |
| `move_feet` | CORE | EVERYDAY, TRANSPORT | HIGH | HIGH | HIGH |  |
| `move_taxi` | CONTEXTUAL | TRANSPORT, TRAVEL | MEDIUM | MEDIUM | HIGH |  |
| `move_car` | CORE | EVERYDAY, TRANSPORT | HIGH | HIGH | HIGH | Accepted as Core because car access and driving/riding are broad practical needs. |
| `move_public` | CONTEXTUAL | TRANSPORT, CITY, TRAVEL | MEDIUM | MEDIUM | HIGH | Contextual transport/city/travel concept. |
| `place_disco` | CONTEXTUAL | NIGHTLIFE, LEISURE | MEDIUM | MEDIUM | HIGH |  |
| `paris_eiffel_tower` | CONTEXTUAL | PARIS, CITY, TRAVEL, CULTURE | MEDIUM | MEDIUM | HIGH |  |
| `paris_arc_de_triomphe` | CONTEXTUAL | PARIS, CITY, TRAVEL, CULTURE | MEDIUM | MEDIUM | HIGH |  |
| `paris_louvre_pyramid` | CONTEXTUAL | PARIS, CITY, TRAVEL, CULTURE | MEDIUM | MEDIUM | HIGH |  |
| `paris_notre_dame` | CONTEXTUAL | PARIS, CITY, TRAVEL, CULTURE | MEDIUM | MEDIUM | HIGH |  |
| `paris_sacre_coeur` | CONTEXTUAL | PARIS, CITY, TRAVEL, CULTURE | MEDIUM | MEDIUM | HIGH |  |
| `paris_moulin_windmill` | CONTEXTUAL | PARIS, NIGHTLIFE, CULTURE | MEDIUM | MEDIUM | HIGH |  |
| `paris_croissant` | CONTEXTUAL | PARIS, FOOD, CULTURE | MEDIUM | MEDIUM | HIGH | Paris-specific food/culture symbol in the Paris context, not generic food Core. |
| `move_boat` | CONTEXTUAL | TRANSPORT, TRAVEL | MEDIUM | MEDIUM | HIGH |  |
| `place_catacombs` | CONTEXTUAL | CITY, TRAVEL, LEISURE | MEDIUM | MEDIUM | HIGH |  |
| `place_theme_park` | CONTEXTUAL | LEISURE, TRAVEL | MEDIUM | MEDIUM | HIGH |  |
| `place_airport` | CONTEXTUAL | TRANSPORT, TRAVEL | MEDIUM | MEDIUM | HIGH |  |
| `place_art_gallery` | CONTEXTUAL | CULTURE, LEISURE, TRAVEL | MEDIUM | MEDIUM | HIGH |  |
| `place_fashion_shopping` | CONTEXTUAL | RETAIL, CULTURE, TRAVEL | MEDIUM | MEDIUM | HIGH |  |
| `item_cigarette` | CONTEXTUAL | NIGHTLIFE, RETAIL, HEALTH, LEGAL | MEDIUM | MEDIUM | HIGH | Contextual nightlife/retail/health/legal item, not a specialized technical concept. |
| `item_cannabis` | CONTEXTUAL | NIGHTLIFE, RETAIL, HEALTH, LEGAL | MEDIUM | MEDIUM | HIGH | Contextual nightlife/retail/health/legal item, not a specialized technical concept. |
| `drink_beer` | CONTEXTUAL | NIGHTLIFE, FOOD, LEGAL | MEDIUM | MEDIUM | HIGH |  |
| `love_heart` | CONTEXTUAL | SOCIAL, EVERYDAY | MEDIUM | MEDIUM | HIGH |  |
| `item_condom` | CONTEXTUAL | HEALTH, SAFETY, NIGHTLIFE, TRAVEL | MEDIUM | MEDIUM | MEDIUM | Contextual for now; safety/health/nightlife/travel use needs future evidence before Core. |
| `nature_flower` | CONTEXTUAL | NATURE, SOCIAL, LEISURE | MEDIUM | MEDIUM | HIGH |  |
| `eye_look` | STANDALONE_CORE | STANDALONE, PERCEPTION | LOW | HIGH | HIGH |  |
| `item_clothing` | STANDALONE_CORE | STANDALONE, EVERYDAY | LOW | HIGH | HIGH |  |
| `comm_speak` | STANDALONE_CORE | STANDALONE, COMMUNICATION | LOW | HIGH | HIGH |  |
| `comm_sound` | STANDALONE_CORE | STANDALONE, COMMUNICATION | LOW | HIGH | HIGH |  |
| `media_text` | STANDALONE_CORE | STANDALONE, MEDIA | LOW | HIGH | HIGH |  |
| `media_image` | STANDALONE_CORE | STANDALONE, MEDIA | LOW | HIGH | HIGH |  |
| `nature_sun` | STANDALONE_CORE | STANDALONE, NATURE, TIME | LOW | HIGH | HIGH |  |
| `state_light` | STANDALONE_CORE | STANDALONE, INFRASTRUCTURE | LOW | HIGH | HIGH |  |
| `food_produce` | CONTEXTUAL | FOOD, RETAIL, EVERYDAY | MEDIUM | MEDIUM | MEDIUM | Food/retail subcategory; useful in standalone contexts but narrower than food Core. |
| `food_bakery` | CONTEXTUAL | FOOD, RETAIL, EVERYDAY | MEDIUM | MEDIUM | MEDIUM | Food/retail subcategory; useful in standalone contexts but narrower than food Core. |
| `rel_greater` | MECHANISM | NAVIGATION, RELATION | HIGH | HIGH | HIGH |  |
| `rel_lesser` | MECHANISM | NAVIGATION, RELATION | HIGH | HIGH | HIGH |  |
| `body_mouth` | STANDALONE_CORE | STANDALONE, BODY, FOOD | LOW | HIGH | HIGH |  |
| `rel_here` | MECHANISM | NAVIGATION, RELATION | HIGH | HIGH | HIGH |  |
| `rel_up` | MECHANISM | NAVIGATION, RELATION | HIGH | HIGH | HIGH |  |
| `rel_down` | MECHANISM | NAVIGATION, RELATION | HIGH | HIGH | HIGH |  |
| `nature_moon` | STANDALONE_CORE | STANDALONE, NATURE, TIME | LOW | HIGH | HIGH |  |
| `tech_ai` | SPECIALIZED | TECH, SPECIALIZED, MACHINE_INTERFACE | LOW | LOW | HIGH | Specialized machine-interface concept. |

## Review queue

The current accepted classification keeps `service_tools` in Core with medium confidence, and keeps `item_condom`, `food_produce`, and `food_bakery` contextual with medium confidence. Future changes should be evidence-led and should update the JSON source of truth, this document, and validation in the same change.
