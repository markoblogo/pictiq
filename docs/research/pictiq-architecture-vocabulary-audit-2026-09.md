# Pictiq Architecture & Vocabulary Audit — 2026-09

Status: local reconciliation pass for human review. Nothing has been pushed, tagged, or released from this pass.

This pass reconciles the current audit artifacts with human-accepted architecture decisions. It does not start a new audit, add icons, or redesign SVGs.

## Final counts

- Ordinary canonical primitives: **83**
- Entity Symbols: **11**
- MECHANISM: **16**
- CORE: **26**
- STANDALONE_CORE: **5**
- CONTEXTUAL: **36**
- SPECIALIZED: **0**

Entity Symbols remain separate from ordinary vocabulary. Numeric notation remains separate from pragmatic `qty_*` quantity tiles.

## Disposition counts

Disposition counts overlap where categories are orthogonal.

| Disposition | Count |
| --- | ---: |
| KEEP_CORE | 42 |
| KEEP_CONTEXTUAL | 36 |
| KEEP_STANDALONE_CORE | 5 |
| SEMANTIC_MIGRATION | 2 |
| DEPRECATE_COMPOSABLE | 1 |
| LEGACY_CONTEXTUAL | 1 |
| VISUAL_REDESIGN_CANDIDATE | 12 |
| HUMAN_REVIEW_REQUIRED | 0 |

## Reconciled decisions

- `need_bar`: `SEMANTIC_MIGRATION`; accepted primary field is ALCOHOL / ALCOHOLIC DRINK. BAR, DRINKING VENUE, and ALCOHOL SERVICE are secondary/contextual readings. Recommend a future alcohol-oriented ID while retaining `need_bar` as a legacy alias/deprecated identifier until compatibility infrastructure is formalized.
- `place_hotel`: `SEMANTIC_MIGRATION`; accepted primary field is HOME / SHELTER / SLEEPING PLACE / BUILDING, with HOMELAND contextually. HOTEL, ACCOMMODATION, BEDROOM, and specific building-type readings are contextual. Recommend a future home-oriented ID while retaining `place_hotel` for compatibility.
- `place_fashion_shopping`: `DEPRECATE_COMPOSABLE`; prefer `place_shop + item_clothing`. Preserve legacy/history and do not redesign the old compound merely to keep it active.
- `move_watercraft`: `KEEP_CONTEXTUAL`; preferred broad WATERCRAFT / BOAT / SHIP / GENERIC WATER TRANSPORT concept. `move_boat`: `LEGACY_CONTEXTUAL`; narrower historical/recreational/travel subtype. Final compatibility decision remains deferred, but the semantic hierarchy is no longer unresolved.
- `service_tools`: `KEEP_CORE`; human decision accepted. No `HUMAN_REVIEW_REQUIRED` remains for Core membership.
- Money: `money_coins` is `KEEP_CORE` for MONEY / CURRENCY / PAYMENT VALUE; `money_card` and `money_atm_bank` are `KEEP_CONTEXTUAL`.
- Technology: `comm_wifi`, `comm_phone`, `power_plug`, and `tech_ai` are `KEEP_CONTEXTUAL`; `power_energy` is separate and `KEEP_CORE`.
- Toilet, transport, Paris-specific, tourism/nightlife/city, cigarette/cannabis/beer/condom concepts remain useful canonical contextual vocabulary, not minimal Core.
- Food: `need_food`, `food_produce`, `food_bakery`, and `food_meat` are `KEEP_CORE`; no extra food categories are added for symmetry.
- `nature_flower`, `comm_sound`, `comm_speak`, `media_text`, `media_image`, `qual_sacred`, `action_conflict`, `nature_animal`, `nature_cloud`, `surface_wavy`, `nature_moon`, `rel_here`, `rel_greater`, `rel_lesser`, `rel_up`, and `rel_down` are reconciled to the accepted Core/core-layer decisions while preserving mechanism roles where applicable.

## Methodology principles

- Canonical does not mean Core.
- Complexity belongs to the context that requires it, not to Core.
- Pictiq vocabulary is need-driven, not taxonomically symmetrical.
- Vocabulary growth should follow real communication pressure, composition attempt, semantic compression, context-pack option, actual gap, and only then candidate primitive.
- Semantic migration is distinct from deprecation: a useful concept can survive while its primary meaning and future preferred ID change.
- Deprecate composable compounds when ordinary composition expresses the useful meaning better than a dedicated lexical tile.
- Pictiq preserves the distinction required for the decision, not every distinction present in the source language.
- Semantic migration and deprecate-composable are different outcomes. Migration keeps a useful concept while evolving meaning/ID; deprecate-composable removes a dedicated compound from active recommendations because composition expresses it better.
- Cleanup is part of language development, not evidence that earlier work failed. Early travel bias helped reveal later architecture needs.

## Visual-redesign queue

No SVG redesign is performed in this pass. The following ordinary icons are flagged for a future visual pass after reviewing all 83 current canonical ordinary icons.

| ID | Reason |
| --- | --- |
| `place_fashion_shopping` | Obsolete compound plus visually inconsistent older artwork; do not redesign until future visual-redesign pass decides whether legacy asset remains needed. |
| `place_landmark_park` | Dense older travel/city artwork; 24 px readability and visual mass should be retested. |
| `place_theme_park` | Detailed amusement-park/city artwork; 24 px readability and older generation style should be retested. |
| `place_art_gallery` | Detailed/outlined exhibition-room artwork; visual mass and small-size clarity should be retested. |
| `place_catacombs` | Skull cluster is dense at small size; contextual Paris asset should be retested before broad reuse. |
| `money_atm_bank` | ATM details/keypad create small-size density; contextual finance/travel icon should be retested. |
| `money_card` | Overlapping card/cash forms may be dense at 24 px; contextual payment icon should be retested. |
| `move_public` | Vehicle detail is dense at 24 px; transport contextual icon should be retested. |
| `paris_notre_dame` | Detailed landmark silhouette; Paris contextual icon should be retested at small size. |
| `paris_sacre_coeur` | Detailed landmark silhouette; Paris contextual icon should be retested at small size. |
| `paris_moulin_windmill` | Detailed landmark silhouette; Paris contextual icon should be retested at small size. |
| `paris_arc_de_triomphe` | Landmark form may need mass/readability retest in the Paris context pack. |

## GitHub metadata recommendation

No GitHub repository metadata was changed in this pass. Recommended About text for a future publication/cleanup pass:

> Pictiq: an open visual language and symbolic protocol built from a small vocabulary, compositional grammar, and contextual extensions.

Recommended retained topics: `visual-language`, `visual-communication`, `symbolic-language`, `communication`, `pictograms`, `icons`, `conlang`, `constructed-language`, `hci`, `accessibility`, `open-standard`, `open-source`, `protocol`, `svg`.

Recommended to deprioritize as project-defining topics unless future implementation evidence justifies them: `travel`, `aac`, `computer-vision`.

## Final audit matrix

Machine-readable source: [`pictiq-architecture-vocabulary-audit-2026-09.json`](pictiq-architecture-vocabulary-audit-2026-09.json).

| ID | Final classification | Final dispositions | Semantic field | Visual status | Note |
| --- | --- | --- | --- | --- | --- |
| `punct_question` | MECHANISM | KEEP_CORE | question | NO_REDESIGN_FLAG_IN_THIS_PASS | Accepted classification retained or reconciled to human review decisions. |
| `punct_exclaim` | MECHANISM | KEEP_CORE | urgent | NO_REDESIGN_FLAG_IN_THIS_PASS | Accepted classification retained or reconciled to human review decisions. |
| `logic_yes` | MECHANISM | KEEP_CORE | yes | NO_REDESIGN_FLAG_IN_THIS_PASS | Accepted classification retained or reconciled to human review decisions. |
| `logic_no` | MECHANISM | KEEP_CORE | no | NO_REDESIGN_FLAG_IN_THIS_PASS | Accepted classification retained or reconciled to human review decisions. |
| `qual_good` | MECHANISM | KEEP_CORE | good / positive evaluation | NO_REDESIGN_FLAG_IN_THIS_PASS | Accepted classification retained or reconciled to human review decisions. |
| `qual_bad` | MECHANISM | KEEP_CORE | bad / negative evaluation | NO_REDESIGN_FLAG_IN_THIS_PASS | Accepted classification retained or reconciled to human review decisions. |
| `time` | CORE | KEEP_CORE | time | NO_REDESIGN_FLAG_IN_THIS_PASS | Accepted classification retained or reconciled to human review decisions. |
| `state_hot` | CORE | KEEP_CORE | hot / heat / fire | NO_REDESIGN_FLAG_IN_THIS_PASS | Accepted classification retained or reconciled to human review decisions. |
| `state_cold` | CORE | KEEP_CORE | cold / freezing / refrigeration | NO_REDESIGN_FLAG_IN_THIS_PASS | Accepted classification retained or reconciled to human review decisions. |
| `person_generic` | STANDALONE_CORE | KEEP_STANDALONE_CORE | generic person / human participant | NO_REDESIGN_FLAG_IN_THIS_PASS | Standalone Core because durable messages often need an explicit human participant. |
| `qty_1` | MECHANISM | KEEP_CORE | one | NO_REDESIGN_FLAG_IN_THIS_PASS | Accepted classification retained or reconciled to human review decisions. |
| `qty_2` | MECHANISM | KEEP_CORE | two | NO_REDESIGN_FLAG_IN_THIS_PASS | Accepted classification retained or reconciled to human review decisions. |
| `qty_5` | MECHANISM | KEEP_CORE | five | NO_REDESIGN_FLAG_IN_THIS_PASS | Accepted classification retained or reconciled to human review decisions. |
| `qty_plus` | MECHANISM | KEEP_CORE | more | NO_REDESIGN_FLAG_IN_THIS_PASS | Accepted classification retained or reconciled to human review decisions. |
| `qty_minus` | MECHANISM | KEEP_CORE | less | NO_REDESIGN_FLAG_IN_THIS_PASS | Accepted classification retained or reconciled to human review decisions. |
| `money_coins` | CORE | KEEP_CORE | money / currency / payment value | NO_REDESIGN_FLAG_IN_THIS_PASS | Human decision: KEEP_CORE. Primary field is MONEY / CURRENCY / PAYMENT VALUE. |
| `money_card` | CONTEXTUAL | KEEP_CONTEXTUAL, VISUAL_REDESIGN_CANDIDATE | card payment | VISUAL_REDESIGN_CANDIDATE | Specific card/payment-instrument concept; Finance/Travel/Commerce contextual vocabulary, not Core. |
| `money_atm_bank` | CONTEXTUAL | KEEP_CONTEXTUAL, VISUAL_REDESIGN_CANDIDATE | ATM / bank | VISUAL_REDESIGN_CANDIDATE | Specific ATM/bank infrastructure concept; Finance/Travel/Commerce contextual vocabulary, not Core. |
| `comm_wifi` | CONTEXTUAL | KEEP_CONTEXTUAL | Wi-Fi | NO_REDESIGN_FLAG_IN_THIS_PASS | Technology/travel/modern-everyday contextual concept; not Core. |
| `comm_phone` | CONTEXTUAL | KEEP_CONTEXTUAL | phone | NO_REDESIGN_FLAG_IN_THIS_PASS | Technology/travel/modern-everyday contextual concept; not Core. |
| `power_plug` | CONTEXTUAL | KEEP_CONTEXTUAL | power outlet | NO_REDESIGN_FLAG_IN_THIS_PASS | Technology/travel/infrastructure contextual concept; do not confuse POWER PLUG with ENERGY. |
| `power_energy` | CORE | KEEP_CORE | electrical energy / electricity / power | NO_REDESIGN_FLAG_IN_THIS_PASS | Human decision: broad POWER / ENERGY remains separate and Core; not the same as power plug. |
| `need_toilet` | CONTEXTUAL | KEEP_CONTEXTUAL | toilet | NO_REDESIGN_FLAG_IN_THIS_PASS | Human decision: KEEP_CONTEXTUAL. Everyday/Public Facilities/Travel concept; preserve canonical asset. |
| `need_water` | CORE | KEEP_CORE | water | NO_REDESIGN_FLAG_IN_THIS_PASS | Broad water/basic-need concept. |
| `need_food` | CORE | KEEP_CORE | food | NO_REDESIGN_FLAG_IN_THIS_PASS | Broad food/basic-need concept. |
| `need_bar` | CONTEXTUAL | KEEP_CONTEXTUAL, SEMANTIC_MIGRATION | alcohol / alcoholic drink | NO_REDESIGN_FLAG_IN_THIS_PASS | Future preferred ID should be alcohol-oriented (for example `drink_alcohol` or equivalent accepted naming). Retain `need_bar` as legacy alias/deprecated identifier for... |
| `safety_medical` | CORE | KEEP_CORE | medical help | NO_REDESIGN_FLAG_IN_THIS_PASS | Broad medical/safety concept. |
| `safety_police` | CONTEXTUAL | KEEP_CONTEXTUAL | police | NO_REDESIGN_FLAG_IN_THIS_PASS | Public safety/legal service concept; canonical contextual vocabulary rather than minimal Core. |
| `place_hotel` | CORE | KEEP_CORE, SEMANTIC_MIGRATION | home / shelter / sleeping place / building | NO_REDESIGN_FLAG_IN_THIS_PASS | Future preferred ID should be home-oriented (for example `place_home` or equivalent accepted naming). Retain `place_hotel` as legacy alias/deprecated identifier for co... |
| `place_shop` | CONTEXTUAL | KEEP_CONTEXTUAL | shop | NO_REDESIGN_FLAG_IN_THIS_PASS | Human decision: KEEP_CONTEXTUAL. Commercial/contextual vocabulary, not minimal Core. |
| `place_landmark_park` | CONTEXTUAL | KEEP_CONTEXTUAL, VISUAL_REDESIGN_CANDIDATE | park / landmark | VISUAL_REDESIGN_CANDIDATE | Tourism/nightlife/city contextual vocabulary; not minimal Core after historical travel-bias cleanup. |
| `place_gas` | CONTEXTUAL | KEEP_CONTEXTUAL | gas station | NO_REDESIGN_FLAG_IN_THIS_PASS | Tourism/nightlife/city contextual vocabulary; not minimal Core after historical travel-bias cleanup. |
| `service_tools` | CORE | KEEP_CORE | tools / repair | NO_REDESIGN_FLAG_IN_THIS_PASS | Human decision: KEEP_CORE. Primary field is TOOLS / REPAIR / MAINTENANCE / FIXING; SERVICE is contextual. |
| `move_feet` | CORE | KEEP_CORE | walk / go on foot | NO_REDESIGN_FLAG_IN_THIS_PASS | Broad walking/on-foot movement concept. |
| `move_taxi` | CONTEXTUAL | KEEP_CONTEXTUAL | taxi | NO_REDESIGN_FLAG_IN_THIS_PASS | Transport/Travel/City contextual concept; not minimal Core. |
| `move_car` | CONTEXTUAL | KEEP_CONTEXTUAL | car | NO_REDESIGN_FLAG_IN_THIS_PASS | Transport/Travel/City contextual concept; not minimal Core. |
| `move_public` | CONTEXTUAL | KEEP_CONTEXTUAL, VISUAL_REDESIGN_CANDIDATE | public transport | VISUAL_REDESIGN_CANDIDATE | Transport/Travel/City contextual concept; not minimal Core. |
| `place_disco` | CONTEXTUAL | KEEP_CONTEXTUAL | disco / club | NO_REDESIGN_FLAG_IN_THIS_PASS | Tourism/nightlife/city contextual vocabulary; not minimal Core after historical travel-bias cleanup. |
| `paris_eiffel_tower` | CONTEXTUAL | KEEP_CONTEXTUAL | Eiffel Tower | NO_REDESIGN_FLAG_IN_THIS_PASS | Paris-specific contextual vocabulary; not general Core. |
| `paris_arc_de_triomphe` | CONTEXTUAL | KEEP_CONTEXTUAL, VISUAL_REDESIGN_CANDIDATE | Arc de Triomphe | VISUAL_REDESIGN_CANDIDATE | Paris-specific contextual vocabulary; not general Core. |
| `paris_louvre_pyramid` | CONTEXTUAL | KEEP_CONTEXTUAL | Louvre pyramid | NO_REDESIGN_FLAG_IN_THIS_PASS | Paris-specific contextual vocabulary; not general Core. |
| `paris_notre_dame` | CONTEXTUAL | KEEP_CONTEXTUAL, VISUAL_REDESIGN_CANDIDATE | Notre-Dame cathedral | VISUAL_REDESIGN_CANDIDATE | Paris-specific contextual vocabulary; not general Core. |
| `paris_sacre_coeur` | CONTEXTUAL | KEEP_CONTEXTUAL, VISUAL_REDESIGN_CANDIDATE | Sacre-Coeur basilica | VISUAL_REDESIGN_CANDIDATE | Paris-specific contextual vocabulary; not general Core. |
| `paris_moulin_windmill` | CONTEXTUAL | KEEP_CONTEXTUAL, VISUAL_REDESIGN_CANDIDATE | Paris windmill cabaret landmark | VISUAL_REDESIGN_CANDIDATE | Paris-specific contextual vocabulary; not general Core. |
| `paris_croissant` | CONTEXTUAL | KEEP_CONTEXTUAL | croissant | NO_REDESIGN_FLAG_IN_THIS_PASS | Paris-specific contextual vocabulary; not general Core. |
| `move_boat` | CONTEXTUAL | KEEP_CONTEXTUAL, LEGACY_CONTEXTUAL | boat transport | NO_REDESIGN_FLAG_IN_THIS_PASS | Narrower historical/recreational/travel-oriented subtype under Travel/Maritime; `move_watercraft` is the accepted broad parent. Final deprecation/alias decision is def... |
| `place_catacombs` | CONTEXTUAL | KEEP_CONTEXTUAL, VISUAL_REDESIGN_CANDIDATE | catacombs | VISUAL_REDESIGN_CANDIDATE | Paris-specific contextual vocabulary; not general Core. |
| `place_theme_park` | CONTEXTUAL | KEEP_CONTEXTUAL, VISUAL_REDESIGN_CANDIDATE | theme park | VISUAL_REDESIGN_CANDIDATE | Tourism/nightlife/city contextual vocabulary; not minimal Core after historical travel-bias cleanup. |
| `place_airport` | CONTEXTUAL | KEEP_CONTEXTUAL | airport | NO_REDESIGN_FLAG_IN_THIS_PASS | Transport/Travel/City contextual concept; not minimal Core. |
| `place_art_gallery` | CONTEXTUAL | KEEP_CONTEXTUAL, VISUAL_REDESIGN_CANDIDATE | art gallery | VISUAL_REDESIGN_CANDIDATE | Tourism/nightlife/city contextual vocabulary; not minimal Core after historical travel-bias cleanup. |
| `place_fashion_shopping` | CONTEXTUAL | KEEP_CONTEXTUAL, DEPRECATE_COMPOSABLE, VISUAL_REDESIGN_CANDIDATE | fashion shopping | VISUAL_REDESIGN_CANDIDATE | Prefer `place_shop + item_clothing`; dedicated compound is no longer needed and old artwork diverges from newer morphology. |
| `item_cigarette` | CONTEXTUAL | KEEP_CONTEXTUAL | cigarette / smoking | NO_REDESIGN_FLAG_IN_THIS_PASS | Adult practical communication / Health-Safety / Travel contextual concept; not Core. |
| `item_cannabis` | CONTEXTUAL | KEEP_CONTEXTUAL | cannabis / cannabis-related products | NO_REDESIGN_FLAG_IN_THIS_PASS | Adult practical communication / Health-Safety / Legal / Travel contextual concept; not Core. |
| `drink_beer` | CONTEXTUAL | KEEP_CONTEXTUAL | beer | NO_REDESIGN_FLAG_IN_THIS_PASS | Adult practical communication / Food-Drink contextual concept; not Core. |
| `love_heart` | CONTEXTUAL | KEEP_CONTEXTUAL | love / affection / romance | NO_REDESIGN_FLAG_IN_THIS_PASS | Broad love/affection concept. HEART + PERSON and HEART + PERSON + MANY remain contextual compositions, not new lexical primitives. |
| `item_condom` | CONTEXTUAL | KEEP_CONTEXTUAL | condom / safer-sex protection | NO_REDESIGN_FLAG_IN_THIS_PASS | Health/Safety/adult practical communication contextual concept; not Core. |
| `nature_flower` | CORE | KEEP_CORE | plant / vegetation / flower | NO_REDESIGN_FLAG_IN_THIS_PASS | Primary broad field is PLANT / VEGETATION / FLOWER contextually; do not force botanical precision. |
| `eye_look` | STANDALONE_CORE | KEEP_STANDALONE_CORE | eye / look / see | NO_REDESIGN_FLAG_IN_THIS_PASS | Accepted classification retained or reconciled to human review decisions. |
| `item_clothing` | STANDALONE_CORE | KEEP_STANDALONE_CORE | clothing / garment | NO_REDESIGN_FLAG_IN_THIS_PASS | Accepted classification retained or reconciled to human review decisions. |
| `comm_speak` | CORE | KEEP_CORE | speech / communication / oral or audible communication | NO_REDESIGN_FLAG_IN_THIS_PASS | Primary field is SPEECH / COMMUNICATION / ORAL OR AUDIBLE COMMUNICATION; do not collapse into SOUND + TEXT. |
| `comm_sound` | CORE | KEEP_CORE | sound / audible signal / music / what is heard | NO_REDESIGN_FLAG_IN_THIS_PASS | Primary field is SOUND / AUDIBLE SIGNAL / MUSIC / WHAT IS HEARD. |
| `media_text` | CORE | KEEP_CORE | text / written information | NO_REDESIGN_FLAG_IN_THIS_PASS | Primary field is TEXT / WRITTEN INFORMATION; READ/WRITE/INFORMATION are contextual. |
| `media_image` | CORE | KEEP_CORE | image / picture / photo / drawing / visual representation | NO_REDESIGN_FLAG_IN_THIS_PASS | Primary field is IMAGE / PICTURE / PHOTO / DRAWING / PAINTING / VISUAL REPRESENTATION. |
| `nature_sun` | STANDALONE_CORE | KEEP_STANDALONE_CORE | sun / daylight | NO_REDESIGN_FLAG_IN_THIS_PASS | Accepted classification retained or reconciled to human review decisions. |
| `state_light` | CORE | KEEP_CORE | light / lighting / lamp | NO_REDESIGN_FLAG_IN_THIS_PASS | Broad light/lighting concept. |
| `food_produce` | CORE | KEEP_CORE | fruit / vegetable / fresh produce | NO_REDESIGN_FLAG_IN_THIS_PASS | Primary field is FRUIT / VEGETABLE / FRESH PRODUCE. Not PLANT. |
| `food_bakery` | CORE | KEEP_CORE | bread / baked food / baked goods / pastry | NO_REDESIGN_FLAG_IN_THIS_PASS | Primary field is BREAD / BAKED FOOD / BAKED GOODS / PASTRY. Bakery/place reading is secondary. |
| `food_meat` | CORE | KEEP_CORE | meat / animal food / meat products | NO_REDESIGN_FLAG_IN_THIS_PASS | Human-accepted Architecture & Vocabulary Audit addition. Broad MEAT / ANIMAL FOOD / MEAT PRODUCTS primitive; do not split into steak, chicken, pork, beef, or drumstick... |
| `rel_greater` | MECHANISM | KEEP_CORE | greater / more / comparative relation | NO_REDESIGN_FLAG_IN_THIS_PASS | Comparative GREATER/MORE relation; rightward reading is contextual only, not a global arrow definition. |
| `rel_lesser` | MECHANISM | KEEP_CORE | lesser / less / comparative relation | NO_REDESIGN_FLAG_IN_THIS_PASS | Comparative LESSER/LESS relation; leftward reading is contextual only, not a global arrow definition. |
| `body_mouth` | STANDALONE_CORE | KEEP_STANDALONE_CORE | mouth / oral intake | NO_REDESIGN_FLAG_IN_THIS_PASS | Accepted classification retained or reconciled to human review decisions. |
| `rel_here` | MECHANISM | KEEP_CORE | here / target / this location / reference point | NO_REDESIGN_FLAG_IN_THIS_PASS | Broad here/target/reference-point operator; context determines exact reading. |
| `rel_up` | MECHANISM | KEEP_CORE | up / above / higher / vertical relation | NO_REDESIGN_FLAG_IN_THIS_PASS | UP/DOWN vertical relation family member; not redefined as MORE/LESS for symmetry. |
| `rel_down` | MECHANISM | KEEP_CORE | down / below / lower / vertical relation | NO_REDESIGN_FLAG_IN_THIS_PASS | UP/DOWN vertical relation family member; not redefined as MORE/LESS for symmetry. |
| `nature_moon` | CORE | KEEP_CORE | moon / night / nighttime | NO_REDESIGN_FLAG_IN_THIS_PASS | Primary field is MOON / NIGHT / NIGHTTIME. Do not add DAY merely for symmetry. |
| `surface_wavy` | CORE | KEEP_CORE | wavy / waves / instability / unevenness / slipperiness / irregular surface | NO_REDESIGN_FLAG_IN_THIS_PASS | Broad WAVY / WAVES / INSTABILITY / UNEVENNESS / SLIPPERINESS / IRREGULAR SURFACE concept; water-surface reading is contextual and WATER remains separate. |
| `state_dead` | CONTEXTUAL | KEEP_CONTEXTUAL | dead / death / not alive | NO_REDESIGN_FLAG_IN_THIS_PASS | Accepted from Stress Test 02 as death/not-alive/deadly-contextual; cross-domain potential exists but current evidence does not justify Core. |
| `tech_ai` | CONTEXTUAL | KEEP_CONTEXTUAL | artificial intelligence / AI system | NO_REDESIGN_FLAG_IN_THIS_PASS | AI/Machine/Technology context vocabulary; not Core. |
| `action_conflict` | CORE | KEEP_CORE | conflict / war / aggression / fight / hostile action | NO_REDESIGN_FLAG_IN_THIS_PASS | Human decision: KEEP_CORE. Broad CONFLICT / WAR / AGGRESSION / FIGHT / ATTACK / HOSTILE ACTION / VIOLENCE concept, distinct from BAD evaluation. |
| `move_watercraft` | CONTEXTUAL | KEEP_CONTEXTUAL | boat / ship / generic watercraft transport | NO_REDESIGN_FLAG_IN_THIS_PASS | Human decision: KEEP_CONTEXTUAL. Preferred broad WATERCRAFT / BOAT / SHIP / GENERIC WATER TRANSPORT concept; do not promote to Core solely because broad. |
| `qual_sacred` | CORE | KEEP_CORE | sacred / holy / divine / religious | NO_REDESIGN_FLAG_IN_THIS_PASS | Human decision: KEEP_CORE. Broad SACRED / HOLY / DIVINE / RELIGIOUS / GOD-DIVINITY contextually / SACRED STATUS concept. |
| `nature_animal` | CORE | KEEP_CORE | animal / general land-animal category | NO_REDESIGN_FLAG_IN_THIS_PASS | Human decision: KEEP_CORE. General land-animal category; not scientific taxonomy. Birds/fish/insects may emerge later if needed. |
| `nature_cloud` | CORE | KEEP_CORE | cloud / sky / air / atmospheric space | NO_REDESIGN_FLAG_IN_THIS_PASS | Human decision: KEEP_CORE. Broad CLOUD / SKY / AIR / ATMOSPHERIC SPACE / WEATHER context / OVERHEAD SKY CONTEXT. |
