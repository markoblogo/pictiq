# Pictiq Architecture & Vocabulary Audit — 2026-09

Status: **CLOSED** after human semantic and visual review.

The audit completed the post-Stress-Test architecture cleanup. It separates Canonical Registry, Core Vocabulary, Standalone Core, Context Packs, Specialized Vocabulary, Entity Symbols, and Legacy/Deprecated compatibility records.

## Final counts

- Active ordinary semantic concepts: **82**
- Retained ordinary canonical identifiers: **83**
- Retained legacy/deprecated identifiers: **4**
- Entity Symbols: **11**
- MECHANISM: **16**
- CORE: **26**
- STANDALONE_CORE: **5**
- CONTEXTUAL: **36**
- SPECIALIZED: **0**

Numeric notation remains separate from pragmatic `qty_*` quantity tiles. Entity Symbols remain separate from ordinary vocabulary.

## Final decisions

- `drink_alcohol` is the preferred active ID for ALCOHOL / ALCOHOLIC DRINK. Historical `need_bar` is retained as a compatibility alias and legacy SVG only; artwork unchanged.
- `place_home` is the preferred active ID for HOME / SHELTER / SLEEPING PLACE / BUILDING. Historical `place_hotel` is retained as a compatibility alias and legacy SVG only; artwork unchanged.
- `place_fashion_shopping` remains a retained deprecated identifier; active representation is `place_shop + item_clothing`; artwork unchanged and not redesigned.
- `move_watercraft` is the preferred broad contextual water-transport concept. `move_boat` remains a legacy contextual subtype; final compatibility action is deferred, but the semantic hierarchy is accepted.
- `food_meat` remains Core with MEAT / ANIMAL FOOD / MEAT PRODUCTS semantics. No further food categories were added for symmetry.
- The 12 visual-audit candidates remain accepted as-is except `place_fashion_shopping`, which is not redrawn because it is compositionally obsolete.

## Visual governance lesson

> Visual consistency is a constraint, not a goal in itself. A working icon should be redesigned only when there is a concrete semantic, recognizability, technical, size-survival, or architectural problem.

Old-generation style alone is not a redesign trigger.

## Migration and compatibility

See [`pictiq-architecture-vocabulary-audit-2026-09-migrations.md`](pictiq-architecture-vocabulary-audit-2026-09-migrations.md).

## Book-material findings

- Historical travel bias inflated the apparent Core.
- Canonical Registry and Core are different layers.
- Contextual vocabulary can remain canonical without being universal.
- Broad primitives are preferred where context can specialize meaning.
- Composition can eliminate obsolete compound icons.
- Semantic migration differs from deprecation.
- Legacy subtype differs from semantic migration.
- Core is need-driven and intentionally asymmetric.
- The audit produced only one clear new primitive: MEAT.
- Visual diversity by itself did not justify redesign.
- Cleanup corrected architecture without pretending earlier development was a failure.

## Final audit matrix

| ID | Final classification | Final dispositions | Semantic field | Visual final decision | Note |
| --- | --- | --- | --- | --- | --- |
| `punct_question` | MECHANISM | KEEP_CORE | question | ACCEPTED_AS_IS | No visual redesign requested or required in final closure. |
| `punct_exclaim` | MECHANISM | KEEP_CORE | urgent | ACCEPTED_AS_IS | No visual redesign requested or required in final closure. |
| `logic_yes` | MECHANISM | KEEP_CORE | yes | ACCEPTED_AS_IS | No visual redesign requested or required in final closure. |
| `logic_no` | MECHANISM | KEEP_CORE | no | ACCEPTED_AS_IS | No visual redesign requested or required in final closure. |
| `qual_good` | MECHANISM | KEEP_CORE | good / positive evaluation | ACCEPTED_AS_IS | No visual redesign requested or required in final closure. |
| `qual_bad` | MECHANISM | KEEP_CORE | bad / negative evaluation | ACCEPTED_AS_IS | No visual redesign requested or required in final closure. |
| `time` | CORE | KEEP_CORE | time | ACCEPTED_AS_IS | No visual redesign requested or required in final closure. |
| `state_hot` | CORE | KEEP_CORE | hot / heat / fire | ACCEPTED_AS_IS | No visual redesign requested or required in final closure. |
| `state_cold` | CORE | KEEP_CORE | cold / freezing / refrigeration | ACCEPTED_AS_IS | No visual redesign requested or required in final closure. |
| `person_generic` | STANDALONE_CORE | KEEP_STANDALONE_CORE | generic person / human participant | ACCEPTED_AS_IS | Standalone Core because durable messages often need an explicit human participant. |
| `qty_1` | MECHANISM | KEEP_CORE | one | ACCEPTED_AS_IS | No visual redesign requested or required in final closure. |
| `qty_2` | MECHANISM | KEEP_CORE | two | ACCEPTED_AS_IS | No visual redesign requested or required in final closure. |
| `qty_5` | MECHANISM | KEEP_CORE | five | ACCEPTED_AS_IS | No visual redesign requested or required in final closure. |
| `qty_plus` | MECHANISM | KEEP_CORE | more | ACCEPTED_AS_IS | No visual redesign requested or required in final closure. |
| `qty_minus` | MECHANISM | KEEP_CORE | less | ACCEPTED_AS_IS | No visual redesign requested or required in final closure. |
| `money_coins` | CORE | KEEP_CORE | money / currency / payment value | ACCEPTED_AS_IS | Human decision: KEEP_CORE. Primary field is MONEY / CURRENCY / PAYMENT VALUE. |
| `money_card` | CONTEXTUAL | KEEP_CONTEXTUAL | card payment | KEEP AS IS | Specific card/payment-instrument concept; Finance/Travel/Commerce contextual vocabulary, not Core. |
| `money_atm_bank` | CONTEXTUAL | KEEP_CONTEXTUAL | ATM / bank | KEEP AS IS | Specific ATM/bank infrastructure concept; Finance/Travel/Commerce contextual vocabulary, not Core. |
| `comm_wifi` | CONTEXTUAL | KEEP_CONTEXTUAL | Wi-Fi | ACCEPTED_AS_IS | Technology/travel/modern-everyday contextual concept; not Core. |
| `comm_phone` | CONTEXTUAL | KEEP_CONTEXTUAL | phone | ACCEPTED_AS_IS | Technology/travel/modern-everyday contextual concept; not Core. |
| `power_plug` | CONTEXTUAL | KEEP_CONTEXTUAL | power outlet | ACCEPTED_AS_IS | Technology/travel/infrastructure contextual concept; do not confuse POWER PLUG with ENERGY. |
| `power_energy` | CORE | KEEP_CORE | electrical energy / electricity / power | ACCEPTED_AS_IS | Human decision: broad POWER / ENERGY remains separate and Core; not the same as power plug. |
| `need_toilet` | CONTEXTUAL | KEEP_CONTEXTUAL | toilet | ACCEPTED_AS_IS | Human decision: KEEP_CONTEXTUAL. Everyday/Public Facilities/Travel concept; preserve canonical asset. |
| `need_water` | CORE | KEEP_CORE | water | ACCEPTED_AS_IS | Broad water/basic-need concept. |
| `need_food` | CORE | KEEP_CORE | food | ACCEPTED_AS_IS | Broad food/basic-need concept. |
| `drink_alcohol` | CONTEXTUAL | KEEP_CONTEXTUAL, SEMANTIC_MIGRATION | alcohol / alcoholic drink | ACCEPTED_AS_IS | Implemented semantic migration from historical `need_bar`; legacy alias retained. |
| `safety_medical` | CORE | KEEP_CORE | medical help | ACCEPTED_AS_IS | Broad medical/safety concept. |
| `safety_police` | CONTEXTUAL | KEEP_CONTEXTUAL | police | ACCEPTED_AS_IS | Public safety/legal service concept; canonical contextual vocabulary rather than minimal Core. |
| `place_home` | CORE | KEEP_CORE, SEMANTIC_MIGRATION | home / shelter / sleeping place / building | ACCEPTED_AS_IS | Implemented semantic migration from historical `place_hotel`; legacy alias retained. |
| `place_shop` | CONTEXTUAL | KEEP_CONTEXTUAL | shop | ACCEPTED_AS_IS | Human decision: KEEP_CONTEXTUAL. Commercial/contextual vocabulary, not minimal Core. |
| `place_landmark_park` | CONTEXTUAL | KEEP_CONTEXTUAL | park / landmark | KEEP AS IS | Tourism/nightlife/city contextual vocabulary; not minimal Core after historical travel-bias cleanup. |
| `place_gas` | CONTEXTUAL | KEEP_CONTEXTUAL | gas station | ACCEPTED_AS_IS | Tourism/nightlife/city contextual vocabulary; not minimal Core after historical travel-bias cleanup. |
| `service_tools` | CORE | KEEP_CORE | tools / repair | ACCEPTED_AS_IS | Human decision: KEEP_CORE. Primary field is TOOLS / REPAIR / MAINTENANCE / FIXING; SERVICE is contextual. |
| `move_feet` | CORE | KEEP_CORE | walk / go on foot | ACCEPTED_AS_IS | Broad walking/on-foot movement concept. |
| `move_taxi` | CONTEXTUAL | KEEP_CONTEXTUAL | taxi | ACCEPTED_AS_IS | Transport/Travel/City contextual concept; not minimal Core. |
| `move_car` | CONTEXTUAL | KEEP_CONTEXTUAL | car | ACCEPTED_AS_IS | Transport/Travel/City contextual concept; not minimal Core. |
| `move_public` | CONTEXTUAL | KEEP_CONTEXTUAL | public transport | KEEP AS IS | Transport/Travel/City contextual concept; not minimal Core. |
| `place_disco` | CONTEXTUAL | KEEP_CONTEXTUAL | disco / club | ACCEPTED_AS_IS | Tourism/nightlife/city contextual vocabulary; not minimal Core after historical travel-bias cleanup. |
| `paris_eiffel_tower` | CONTEXTUAL | KEEP_CONTEXTUAL | Eiffel Tower | ACCEPTED_AS_IS | Paris-specific contextual vocabulary; not general Core. |
| `paris_arc_de_triomphe` | CONTEXTUAL | KEEP_CONTEXTUAL | Arc de Triomphe | KEEP AS IS | Paris-specific contextual vocabulary; not general Core. |
| `paris_louvre_pyramid` | CONTEXTUAL | KEEP_CONTEXTUAL | Louvre pyramid | ACCEPTED_AS_IS | Paris-specific contextual vocabulary; not general Core. |
| `paris_notre_dame` | CONTEXTUAL | KEEP_CONTEXTUAL | Notre-Dame cathedral | KEEP AS IS | Paris-specific contextual vocabulary; not general Core. |
| `paris_sacre_coeur` | CONTEXTUAL | KEEP_CONTEXTUAL | Sacre-Coeur basilica | KEEP AS IS | Paris-specific contextual vocabulary; not general Core. |
| `paris_moulin_windmill` | CONTEXTUAL | KEEP_CONTEXTUAL | Paris windmill cabaret landmark | KEEP AS IS | Paris-specific contextual vocabulary; not general Core. |
| `paris_croissant` | CONTEXTUAL | KEEP_CONTEXTUAL | croissant | ACCEPTED_AS_IS | Paris-specific contextual vocabulary; not general Core. |
| `move_boat` | CONTEXTUAL | KEEP_CONTEXTUAL, LEGACY_CONTEXTUAL | boat transport | ACCEPTED_AS_IS | Narrower historical/recreational/travel-oriented subtype under Travel/Maritime; broad concept is `move_watercraft`; final compatibility action deferred. |
| `place_catacombs` | CONTEXTUAL | KEEP_CONTEXTUAL | catacombs | KEEP AS IS | Paris-specific contextual vocabulary; not general Core. |
| `place_theme_park` | CONTEXTUAL | KEEP_CONTEXTUAL | theme park | KEEP AS IS | Tourism/nightlife/city contextual vocabulary; not minimal Core after historical travel-bias cleanup. |
| `place_airport` | CONTEXTUAL | KEEP_CONTEXTUAL | airport | ACCEPTED_AS_IS | Transport/Travel/City contextual concept; not minimal Core. |
| `place_art_gallery` | CONTEXTUAL | KEEP_CONTEXTUAL | art gallery | KEEP AS IS | Tourism/nightlife/city contextual vocabulary; not minimal Core after historical travel-bias cleanup. |
| `place_fashion_shopping` | CONTEXTUAL | KEEP_CONTEXTUAL, DEPRECATE_COMPOSABLE | fashion shopping (deprecated composable legacy concept) | DO NOT REDRAW / DEPRECATE | Prefer `place_shop + item_clothing`; retained deprecated legacy identifier because active schema does not yet split inactive IDs safely. |
| `item_cigarette` | CONTEXTUAL | KEEP_CONTEXTUAL | cigarette / smoking | ACCEPTED_AS_IS | Adult practical communication / Health-Safety / Travel contextual concept; not Core. |
| `item_cannabis` | CONTEXTUAL | KEEP_CONTEXTUAL | cannabis / cannabis-related products | ACCEPTED_AS_IS | Adult practical communication / Health-Safety / Legal / Travel contextual concept; not Core. |
| `drink_beer` | CONTEXTUAL | KEEP_CONTEXTUAL | beer | ACCEPTED_AS_IS | Adult practical communication / Food-Drink contextual concept; not Core. |
| `love_heart` | CONTEXTUAL | KEEP_CONTEXTUAL | love / affection / romance | ACCEPTED_AS_IS | Broad love/affection concept. HEART + PERSON and HEART + PERSON + MANY remain contextual compositions, not new lexical primitives. |
| `item_condom` | CONTEXTUAL | KEEP_CONTEXTUAL | condom / safer-sex protection | ACCEPTED_AS_IS | Health/Safety/adult practical communication contextual concept; not Core. |
| `nature_flower` | CORE | KEEP_CORE | plant / vegetation / flower | ACCEPTED_AS_IS | Primary broad field is PLANT / VEGETATION / FLOWER contextually; do not force botanical precision. |
| `eye_look` | STANDALONE_CORE | KEEP_STANDALONE_CORE | eye / look / see | ACCEPTED_AS_IS | No visual redesign requested or required in final closure. |
| `item_clothing` | STANDALONE_CORE | KEEP_STANDALONE_CORE | clothing / garment | ACCEPTED_AS_IS | No visual redesign requested or required in final closure. |
| `comm_speak` | CORE | KEEP_CORE | speech / communication / oral or audible communication | ACCEPTED_AS_IS | Primary field is SPEECH / COMMUNICATION / ORAL OR AUDIBLE COMMUNICATION; do not collapse into SOUND + TEXT. |
| `comm_sound` | CORE | KEEP_CORE | sound / audible signal / music / what is heard | ACCEPTED_AS_IS | Primary field is SOUND / AUDIBLE SIGNAL / MUSIC / WHAT IS HEARD. |
| `media_text` | CORE | KEEP_CORE | text / written information | ACCEPTED_AS_IS | Primary field is TEXT / WRITTEN INFORMATION; READ/WRITE/INFORMATION are contextual. |
| `media_image` | CORE | KEEP_CORE | image / picture / photo / drawing / visual representation | ACCEPTED_AS_IS | Primary field is IMAGE / PICTURE / PHOTO / DRAWING / PAINTING / VISUAL REPRESENTATION. |
| `nature_sun` | STANDALONE_CORE | KEEP_STANDALONE_CORE | sun / daylight | ACCEPTED_AS_IS | No visual redesign requested or required in final closure. |
| `state_light` | CORE | KEEP_CORE | light / lighting / lamp | ACCEPTED_AS_IS | Broad light/lighting concept. |
| `food_produce` | CORE | KEEP_CORE | fruit / vegetable / fresh produce | ACCEPTED_AS_IS | Primary field is FRUIT / VEGETABLE / FRESH PRODUCE. Not PLANT. |
| `food_bakery` | CORE | KEEP_CORE | bread / baked food / baked goods / pastry | ACCEPTED_AS_IS | Primary field is BREAD / BAKED FOOD / BAKED GOODS / PASTRY. Bakery/place reading is secondary. |
| `food_meat` | CORE | KEEP_CORE | meat / animal food / meat products | ACCEPTED_AS_IS | Human-accepted Architecture & Vocabulary Audit addition. Broad MEAT / ANIMAL FOOD / MEAT PRODUCTS primitive; do not split into steak, chicken, pork, beef, or drumstick... |
| `rel_greater` | MECHANISM | KEEP_CORE | greater / more / comparative relation | ACCEPTED_AS_IS | Comparative GREATER/MORE relation; rightward reading is contextual only, not a global arrow definition. |
| `rel_lesser` | MECHANISM | KEEP_CORE | lesser / less / comparative relation | ACCEPTED_AS_IS | Comparative LESSER/LESS relation; leftward reading is contextual only, not a global arrow definition. |
| `body_mouth` | STANDALONE_CORE | KEEP_STANDALONE_CORE | mouth / oral intake | ACCEPTED_AS_IS | No visual redesign requested or required in final closure. |
| `rel_here` | MECHANISM | KEEP_CORE | here / target / this location / reference point | ACCEPTED_AS_IS | Broad here/target/reference-point operator; context determines exact reading. |
| `rel_up` | MECHANISM | KEEP_CORE | up / above / higher / vertical relation | ACCEPTED_AS_IS | UP/DOWN vertical relation family member; not redefined as MORE/LESS for symmetry. |
| `rel_down` | MECHANISM | KEEP_CORE | down / below / lower / vertical relation | ACCEPTED_AS_IS | UP/DOWN vertical relation family member; not redefined as MORE/LESS for symmetry. |
| `nature_moon` | CORE | KEEP_CORE | moon / night / nighttime | ACCEPTED_AS_IS | Primary field is MOON / NIGHT / NIGHTTIME. Do not add DAY merely for symmetry. |
| `surface_wavy` | CORE | KEEP_CORE | wavy / waves / instability / unevenness / slipperiness / irregular surface | ACCEPTED_AS_IS | Broad WAVY / WAVES / INSTABILITY / UNEVENNESS / SLIPPERINESS / IRREGULAR SURFACE concept; water-surface reading is contextual and WATER remains separate. |
| `state_dead` | CONTEXTUAL | KEEP_CONTEXTUAL | dead / death / not alive | ACCEPTED_AS_IS | Accepted from Stress Test 02 as death/not-alive/deadly-contextual; cross-domain potential exists but current evidence does not justify Core. |
| `tech_ai` | CONTEXTUAL | KEEP_CONTEXTUAL | artificial intelligence / AI system | ACCEPTED_AS_IS | AI/Machine/Technology context vocabulary; not Core. |
| `action_conflict` | CORE | KEEP_CORE | conflict / war / aggression / fight / hostile action | ACCEPTED_AS_IS | Human decision: KEEP_CORE. Broad CONFLICT / WAR / AGGRESSION / FIGHT / ATTACK / HOSTILE ACTION / VIOLENCE concept, distinct from BAD evaluation. |
| `move_watercraft` | CONTEXTUAL | KEEP_CONTEXTUAL | boat / ship / generic watercraft transport | ACCEPTED_AS_IS | Human decision: KEEP_CONTEXTUAL. Preferred broad WATERCRAFT / BOAT / SHIP / GENERIC WATER TRANSPORT concept; do not promote to Core solely because broad. |
| `qual_sacred` | CORE | KEEP_CORE | sacred / holy / divine / religious | ACCEPTED_AS_IS | Human decision: KEEP_CORE. Broad SACRED / HOLY / DIVINE / RELIGIOUS / GOD-DIVINITY contextually / SACRED STATUS concept. |
| `nature_animal` | CORE | KEEP_CORE | animal / general land-animal category | ACCEPTED_AS_IS | Human decision: KEEP_CORE. General land-animal category; not scientific taxonomy. Birds/fish/insects may emerge later if needed. |
| `nature_cloud` | CORE | KEEP_CORE | cloud / sky / air / atmospheric space | ACCEPTED_AS_IS | Human decision: KEEP_CORE. Broad CLOUD / SKY / AIR / ATMOSPHERIC SPACE / WEATHER context / OVERHEAD SKY CONTEXT. |
