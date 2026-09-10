# Pictiq Architecture & Vocabulary Audit — 2026-09

Status: local audit implementation for human review.

This audit applies accepted post-Stress-Test architecture decisions while preserving the difference between canonical registry, Core vocabulary, Standalone Core, context packs, specialized vocabulary, numeric notation, and Entity Symbols.

## Counts after this pass

- Ordinary canonical icons: **83**
- Entity Symbols: **11**
- CONTEXTUAL: **38**
- CORE: **18**
- MECHANISM: **16**
- SPECIALIZED: **1**
- STANDALONE_CORE: **10**

Entity Symbols remain separate from ordinary vocabulary. Numeric notation remains a separate notation layer and does not create ordinary lexical concepts such as `num_50`.

## Accepted changes implemented

- `food_meat` added as a human-accepted ordinary Core primitive for MEAT / ANIMAL FOOD / MEAT PRODUCTS contextually. It fills a real vocabulary gap between broad food categories and does not create separate steak, chicken, pork, beef, or drumstick primitives.
- `money_coins` now primarily means MONEY / CURRENCY / PAYMENT VALUE. Card and ATM/bank concepts are contextual payment/infrastructure vocabulary.
- `need_bar` is treated as a semantic migration toward ALCOHOL / ALCOHOLIC DRINK, preserving the existing compatibility ID.
- `place_hotel` is treated as a semantic migration toward HOME / SHELTER / SLEEPING PLACE / BUILDING, preserving the existing compatibility ID.
- `place_fashion_shopping` is preserved as legacy contextual vocabulary but removed from active Paris recommendations in favor of `place_shop + item_clothing`.
- `move_boat` remains a legacy contextual subtype. `move_watercraft` is the preferred broad water-transport primitive. The compatibility decision is explicitly deferred.
- `service_tools` stays Core with medium confidence and remains in the human-review queue rather than being silently demoted.

## Principles preserved

- Canonical does not mean Core.
- Complexity belongs to the context that requires it, not to Core.
- Pictiq vocabulary is need-driven, not taxonomically symmetrical.
- Vocabulary growth should follow real communication pressure, composition attempt, semantic compression, context-pack option, actual gap, and only then candidate primitive.
- Pictiq preserves the distinction required for the decision, not every distinction present in the source language.
- Core asymmetry is intentional: vocabulary grows from actual communication pressure, not from taxonomy symmetry.

## Audit matrix

Full machine-readable rows are in [`pictiq-architecture-vocabulary-audit-2026-09.json`](pictiq-architecture-vocabulary-audit-2026-09.json).

| ID | Start role | Proposed role | Disposition | Human status | Note |
| --- | --- | --- | --- | --- | --- |
| `punct_question` | MECHANISM | MECHANISM | KEEP | HUMAN_ACCEPTED | Accepted classification retained. |
| `punct_exclaim` | MECHANISM | MECHANISM | KEEP | HUMAN_ACCEPTED | Accepted classification retained. |
| `logic_yes` | MECHANISM | MECHANISM | KEEP | HUMAN_ACCEPTED | Accepted classification retained. |
| `logic_no` | MECHANISM | MECHANISM | KEEP | HUMAN_ACCEPTED | Accepted classification retained. |
| `qual_good` | MECHANISM | MECHANISM | KEEP | HUMAN_ACCEPTED | Accepted classification retained. |
| `qual_bad` | MECHANISM | MECHANISM | KEEP | HUMAN_ACCEPTED | Accepted classification retained. |
| `time` | CORE | CORE | KEEP | HUMAN_ACCEPTED | Accepted classification retained. |
| `state_hot` | CORE | CORE | KEEP | HUMAN_ACCEPTED | Accepted classification retained. |
| `state_cold` | CORE | CORE | KEEP | HUMAN_ACCEPTED | Accepted classification retained. |
| `person_generic` | STANDALONE_CORE | STANDALONE_CORE | KEEP | HUMAN_ACCEPTED | Standalone Core because durable messages often need an explicit human participant. |
| `qty_1` | MECHANISM | MECHANISM | KEEP | HUMAN_ACCEPTED | Accepted classification retained. |
| `qty_2` | MECHANISM | MECHANISM | KEEP | HUMAN_ACCEPTED | Accepted classification retained. |
| `qty_5` | MECHANISM | MECHANISM | KEEP | HUMAN_ACCEPTED | Accepted classification retained. |
| `qty_plus` | MECHANISM | MECHANISM | KEEP | HUMAN_ACCEPTED | Accepted classification retained. |
| `qty_minus` | MECHANISM | MECHANISM | KEEP | HUMAN_ACCEPTED | Accepted classification retained. |
| `money_coins` | CORE | CORE | KEEP | HUMAN_ACCEPTED | Primary semantic field is MONEY / CURRENCY / PAYMENT VALUE. Cash/coins remain visual and contextual readings. |
| `money_card` | CORE | CONTEXTUAL | RECLASSIFY | HUMAN_ACCEPTED | Specific payment instrument; useful canonical contextual vocabulary, not minimal Core. |
| `money_atm_bank` | CONTEXTUAL | CONTEXTUAL | KEEP | HUMAN_ACCEPTED | Specific finance/infrastructure service, not minimal Core. |
| `comm_wifi` | CONTEXTUAL | CONTEXTUAL | KEEP | HUMAN_ACCEPTED | Technology/infrastructure/travel concept; not minimal general Core. |
| `comm_phone` | CORE | CONTEXTUAL | RECLASSIFY | HUMAN_ACCEPTED | Modern communication device/service; useful contextual vocabulary, not minimal Core. |
| `power_plug` | CONTEXTUAL | CONTEXTUAL | KEEP | HUMAN_ACCEPTED | Specific charging/outlet concept; distinct from power_energy and not minimal Core. |
| `power_energy` | CONTEXTUAL | CORE | RECLASSIFY | HUMAN_ACCEPTED | Broad energy/electricity/power concept; not equivalent to power_plug. |
| `need_toilet` | CORE | CONTEXTUAL | RECLASSIFY | HUMAN_ACCEPTED | Everyday/public-facility/travel concept; useful canonical vocabulary but outside minimal Core. |
| `need_water` | CORE | CORE | KEEP | HUMAN_ACCEPTED | Broad water/basic-need concept. |
| `need_food` | CORE | CORE | KEEP | HUMAN_ACCEPTED | Broad food/basic-need concept. |
| `need_bar` | CONTEXTUAL | CONTEXTUAL | SEMANTIC_MIGRATION | HUMAN_ACCEPTED | SEMANTIC_MIGRATION: compatibility ID. Accepted primary semantics are ALCOHOL / ALCOHOLIC DRINK; BAR/venue is secondary. Preferred future ID candidate: drink_... |
| `safety_medical` | CORE | CORE | KEEP | HUMAN_ACCEPTED | Broad medical/safety concept. |
| `safety_police` | CORE | CONTEXTUAL | RECLASSIFY | HUMAN_ACCEPTED | Public safety/legal service concept; canonical contextual vocabulary rather than minimal Core. |
| `place_hotel` | CONTEXTUAL | CORE | RECLASSIFY, SEMANTIC_MIGRATION | HUMAN_ACCEPTED | SEMANTIC_MIGRATION: compatibility ID. Accepted primary semantics are HOME / SHELTER / SLEEPING PLACE / BUILDING; HOTEL/accommodation is secondary. Preferred ... |
| `place_shop` | CORE | CONTEXTUAL | RECLASSIFY | HUMAN_ACCEPTED | Generic shop remains useful commercial contextual vocabulary; not minimal Core merely because many compounds can use it. |
| `place_landmark_park` | CONTEXTUAL | CONTEXTUAL | KEEP | HUMAN_ACCEPTED | Accepted classification retained. |
| `place_gas` | CONTEXTUAL | CONTEXTUAL | KEEP | HUMAN_ACCEPTED | Accepted classification retained. |
| `service_tools` | CORE | CORE | HUMAN_REVIEW_REQUIRED | HUMAN_REVIEW_REQUIRED | Kept in Core for now; repair/help contexts are broad but should be reviewed with use evidence. |
| `move_feet` | CORE | CORE | KEEP | HUMAN_ACCEPTED | Broad walking/on-foot movement concept. |
| `move_taxi` | CONTEXTUAL | CONTEXTUAL | KEEP | HUMAN_ACCEPTED | Transport-specific concept outside minimal Core. |
| `move_car` | CORE | CONTEXTUAL | RECLASSIFY | HUMAN_ACCEPTED | Transport-specific concept outside minimal Core after removal of historical travel bias. |
| `move_public` | CONTEXTUAL | CONTEXTUAL | KEEP | HUMAN_ACCEPTED | Transport/city/travel concept outside minimal Core. |
| `place_disco` | CONTEXTUAL | CONTEXTUAL | KEEP | HUMAN_ACCEPTED | Accepted classification retained. |
| `paris_eiffel_tower` | CONTEXTUAL | CONTEXTUAL | KEEP | HUMAN_ACCEPTED | Accepted classification retained. |
| `paris_arc_de_triomphe` | CONTEXTUAL | CONTEXTUAL | KEEP | HUMAN_ACCEPTED | Accepted classification retained. |
| `paris_louvre_pyramid` | CONTEXTUAL | CONTEXTUAL | KEEP | HUMAN_ACCEPTED | Accepted classification retained. |
| `paris_notre_dame` | CONTEXTUAL | CONTEXTUAL | KEEP | HUMAN_ACCEPTED | Accepted classification retained. |
| `paris_sacre_coeur` | CONTEXTUAL | CONTEXTUAL | KEEP | HUMAN_ACCEPTED | Accepted classification retained. |
| `paris_moulin_windmill` | CONTEXTUAL | CONTEXTUAL | KEEP | HUMAN_ACCEPTED | Accepted classification retained. |
| `paris_croissant` | CONTEXTUAL | CONTEXTUAL | KEEP | HUMAN_ACCEPTED | Paris-specific food/culture symbol in the Paris context, not generic food Core. |
| `move_boat` | CONTEXTUAL | CONTEXTUAL | LEGACY_CONTEXTUAL | DEFERRED_TO_COMPATIBILITY_AUDIT | Keep as legacy contextual subtype; defer compatibility decision. |
| `place_catacombs` | CONTEXTUAL | CONTEXTUAL | KEEP | HUMAN_ACCEPTED | Accepted classification retained. |
| `place_theme_park` | CONTEXTUAL | CONTEXTUAL | KEEP | HUMAN_ACCEPTED | Accepted classification retained. |
| `place_airport` | CONTEXTUAL | CONTEXTUAL | KEEP | HUMAN_ACCEPTED | Accepted classification retained. |
| `place_art_gallery` | CONTEXTUAL | CONTEXTUAL | KEEP | HUMAN_ACCEPTED | Accepted classification retained. |
| `place_fashion_shopping` | CONTEXTUAL | CONTEXTUAL | DEPRECATE_COMPOSABLE, VISUAL_REDESIGN_CANDIDATE | HUMAN_ACCEPTED | Preserve legacy asset, remove from active recommendations, prefer composition. |
| `item_cigarette` | CONTEXTUAL | CONTEXTUAL | KEEP | HUMAN_ACCEPTED | Contextual nightlife/retail/health/legal item, not a specialized technical concept. |
| `item_cannabis` | CONTEXTUAL | CONTEXTUAL | KEEP | HUMAN_ACCEPTED | Contextual nightlife/retail/health/legal item, not a specialized technical concept. |
| `drink_beer` | CONTEXTUAL | CONTEXTUAL | KEEP | HUMAN_ACCEPTED | Specific alcoholic-drink subtype; remains contextual and separate from migrated broad alcohol concept. |
| `love_heart` | CONTEXTUAL | CONTEXTUAL | KEEP | HUMAN_ACCEPTED | Broad love/affection concept. HEART + PERSON and HEART + PERSON + MANY remain contextual compositions, not new lexical primitives. |
| `item_condom` | CONTEXTUAL | CONTEXTUAL | KEEP | HUMAN_ACCEPTED | Contextual for now; safety/health/nightlife/travel use needs future evidence before Core. |
| `nature_flower` | CONTEXTUAL | CONTEXTUAL | KEEP | HUMAN_ACCEPTED | Broad plant/vegetation/flower concept; do not force botanical precision or taxonomy completion. |
| `eye_look` | STANDALONE_CORE | STANDALONE_CORE | KEEP | HUMAN_ACCEPTED | Accepted classification retained. |
| `item_clothing` | STANDALONE_CORE | STANDALONE_CORE | KEEP | HUMAN_ACCEPTED | Accepted classification retained. |
| `comm_speak` | STANDALONE_CORE | STANDALONE_CORE | KEEP | HUMAN_ACCEPTED | Accepted classification retained. |
| `comm_sound` | STANDALONE_CORE | STANDALONE_CORE | KEEP | HUMAN_ACCEPTED | Accepted classification retained. |
| `media_text` | STANDALONE_CORE | STANDALONE_CORE | KEEP | HUMAN_ACCEPTED | Accepted classification retained. |
| `media_image` | STANDALONE_CORE | STANDALONE_CORE | KEEP | HUMAN_ACCEPTED | Accepted classification retained. |
| `nature_sun` | STANDALONE_CORE | STANDALONE_CORE | KEEP | HUMAN_ACCEPTED | Accepted classification retained. |
| `state_light` | CORE | CORE | KEEP | HUMAN_ACCEPTED | Broad light/lighting concept. |
| `food_produce` | CONTEXTUAL | CONTEXTUAL | KEEP | HUMAN_ACCEPTED | Primary field is FRUIT / VEGETABLE / FRESH PRODUCE. Do not expand to PLANT. |
| `food_bakery` | CONTEXTUAL | CORE | RECLASSIFY | HUMAN_ACCEPTED | Primary field is BREAD / BAKED FOOD / BAKED GOODS / PASTRY. Bakery/place reading is secondary. |
| `food_meat` | NOT_PRESENT | CORE | KEEP | HUMAN_ACCEPTED_NEW_PRIMITIVE | Human-accepted vocabulary gap: broad animal-food category analogous to produce and bakery; no narrower meat taxonomy added. |
| `rel_greater` | MECHANISM | MECHANISM | KEEP | HUMAN_ACCEPTED | Comparative GREATER/MORE relation; rightward reading is contextual only, not a global arrow definition. |
| `rel_lesser` | MECHANISM | MECHANISM | KEEP | HUMAN_ACCEPTED | Comparative LESSER/LESS relation; leftward reading is contextual only, not a global arrow definition. |
| `body_mouth` | STANDALONE_CORE | STANDALONE_CORE | KEEP | HUMAN_ACCEPTED | Accepted classification retained. |
| `rel_here` | MECHANISM | MECHANISM | KEEP | HUMAN_ACCEPTED | Broad here/target/reference-point operator; context determines exact reading. |
| `rel_up` | MECHANISM | MECHANISM | KEEP | HUMAN_ACCEPTED | UP/DOWN vertical relation family member; not redefined as MORE/LESS for symmetry. |
| `rel_down` | MECHANISM | MECHANISM | KEEP | HUMAN_ACCEPTED | UP/DOWN vertical relation family member; not redefined as MORE/LESS for symmetry. |
| `nature_moon` | STANDALONE_CORE | STANDALONE_CORE | KEEP | HUMAN_ACCEPTED | Accepted classification retained. |
| `surface_wavy` | CONTEXTUAL | CONTEXTUAL | KEEP | HUMAN_ACCEPTED | Broad wavy/waves/unstable/uneven/slippery/irregular-surface concept supported by Road and Odyssey; not collapsed into WATER. |
| `state_dead` | CONTEXTUAL | CONTEXTUAL | KEEP | HUMAN_ACCEPTED | Accepted from Stress Test 02 as death/not-alive/deadly-contextual; cross-domain potential exists but current evidence does not justify Core. |
| `tech_ai` | SPECIALIZED | SPECIALIZED | KEEP | HUMAN_ACCEPTED | AI/Machine/Technology context vocabulary; not minimal Core. |
| `action_conflict` | CORE | CORE | KEEP | HUMAN_ACCEPTED | Broad conflict/war/aggression/fight/hostile action concept; distinct from qual_bad evaluation. |
| `move_watercraft` | CONTEXTUAL | CONTEXTUAL | KEEP | HUMAN_ACCEPTED | Preferred broad watercraft / boat / ship / generic water transport concept; not minimal Core. Existing move_boat remains legacy contextual pending future com... |
| `qual_sacred` | CORE | CORE | KEEP | HUMAN_ACCEPTED | Broad sacred/holy/divine/religious concept; avoids separate GOD/PRIEST/TEMPLE primitives unless future contexts require them. |
| `nature_animal` | CORE | CORE | KEEP | HUMAN_ACCEPTED | General land-animal category; not rigorous taxonomy. Birds/fish/insects may emerge separately if real use creates pressure. |
| `nature_cloud` | CORE | CORE | KEEP | HUMAN_ACCEPTED | Broad cloud/sky/air/atmospheric-space concept; do not add AIR/SKY/WEATHER merely for taxonomy. |

## QA

- `food_meat` visual QA sheet: `build/qa/food_meat.html` (local generated evidence; build output is intentionally not versioned).
- Source reference archived at [`../book-materials/experiments/assets/architecture-vocabulary-audit-food-meat-reference.png`](../book-materials/experiments/assets/architecture-vocabulary-audit-food-meat-reference.png).
- Canonical SVG: [`../../icons/svg/food_meat.svg`](../../icons/svg/food_meat.svg).
