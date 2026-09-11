# Experimenter-Only Semantic Targets

> Do not show this file to participants. Score communicated meaning, not exact string identity.

## T0 — Training: I need water

- Source intent: I need water.
- Required semantic slots: water/drink need.
- Optional slots: person/self if participant chooses it.
- Intentionally omittable: tense, quantity, politeness.
- Known acceptable compositions: `need_water`; `person_generic + need_water` if used as self/person need.
- Clearly unjustified concepts: alcohol/bar, food-only, money, place.
- Expected profile/context: default/core is sufficient.

## T1 — Ask for water

- Source intent: Ask for water.
- Required semantic slots: water/drink need/request; question/request marker.
- Optional slots: person/self.
- Intentionally omittable: exact quantity, tense, please.
- Known acceptable compositions: `need_water + punct_question`; `person_generic + need_water + punct_question`.
- Clearly unjustified concepts: alcohol/bar, no, unrelated place/entity.
- Expected profile/context: default/core is sufficient.

## T2 — No alcohol / no bar/drinking here

- Source intent: No alcohol or no drinking/bar here.
- Required semantic slots: alcohol/bar/drink-alcohol concept; negation/prohibition.
- Optional slots: here/place marker.
- Intentionally omittable: legal authority, exact venue, tense.
- Known acceptable compositions: `drink_alcohol + logic_no`; `rel_here + drink_alcohol + logic_no`; `logic_no + drink_alcohol` if meaning is clear.
- Clearly unjustified concepts: water-only, food-only, medical cross, Entity Symbols.
- Expected profile/context: default/core is sufficient; Search may help.

## T3 — I want food

- Source intent: I want food.
- Required semantic slots: person/self or need/want; food.
- Optional slots: question/request marker.
- Intentionally omittable: exact food category, tense, quantity.
- Known acceptable compositions: `person_generic + need_food`; `need_food`; `need_food + punct_question` if expressed as request.
- Clearly unjustified concepts: water-only, alcohol-only, no, unrelated entity.
- Expected profile/context: default/core is sufficient.

## T4 — Two Frames: I need water. Thank you / good.

- Source intent: Two-part message: first water need/request, second positive thanks/good.
- Required semantic slots: Frame 1 contains water need/request; Frame 2 contains positive/good/yes/accepted meaning.
- Optional slots: question/request marker; person/self.
- Intentionally omittable: literal word "thank you" if no exact current primitive exists.
- Known acceptable compositions: Frame 1 `need_water`; Frame 2 `qual_good`; Frame 1 `need_water + punct_question`; Frame 2 `logic_yes` or `qual_good`.
- Clearly unjustified concepts: one single overloaded Frame if participant never creates two parts; unrelated Entity Symbols.
- Expected profile/context: default/core is sufficient.

## T5 — Warning about slippery or uneven surface

- Source intent: Surface problem / slippery or uneven surface warning.
- Required semantic slots: wavy/uneven/slippery surface; warning/caution.
- Optional slots: road context; exclamation/caution marker.
- Intentionally omittable: distinction between slippery, rough, speed bump, and waves; Pictiq intentionally keeps broad surface irregularity here.
- Known acceptable compositions: `surface_wavy + punct_exclaim`; `surface_wavy` in road context if warning is otherwise clear.
- Clearly unjustified concepts: water-only unless used as wave context without warning; unrelated weather/entity.
- Expected profile/context: road-wayfinding context recommended; Search for surface/slippery/wavy acceptable.

## T6 — Exact number 50

- Source intent: Communicate the exact number 50.
- Required semantic slots: numeric token 50.
- Optional slots: context such as speed/road if participant adds it, but not required.
- Intentionally omittable: percent, units, speed limit circle.
- Known acceptable compositions: number token `50`.
- Clearly unjustified concepts: `qty_5` plus an invented zero-style quantity, arbitrary unsupported numbers, plus/minus.
- Expected profile/context: default/core is sufficient; Special `50` button is expected.

## T7 — Poseidon and water/sea

- Source intent: Compose a message about Poseidon and water/sea.
- Required semantic slots: Poseidon Entity Symbol; water/sea/ocean concept.
- Optional slots: sacred/divine, person/entity context, relation/order.
- Intentionally omittable: mythology details, trident, exact Greek/Roman distinction.
- Known acceptable compositions: `entity:poseidon@odyssey + need_water`; `entity:poseidon@odyssey + surface_wavy`; `entity:poseidon@odyssey + move_watercraft` if participant frames sea travel.
- Clearly unjustified concepts: other Odyssey entities as replacement for Poseidon, no entity selected, unrelated food/money.
- Expected profile/context: Odyssey context should be selected or search should reveal entities.

## T8 — Edit/correct/export: ask for food instead of water

- Source intent: Start with water request and correct it to food request; export SVG.
- Required semantic slots: final message asks/requests food, not water; export succeeds.
- Optional slots: person/self; question marker.
- Intentionally omittable: exact food category unless participant chooses produce/bakery/meat as food subcategory.
- Known acceptable compositions: final `need_food + punct_question`; `person_generic + need_food + punct_question`; equivalent clear food request.
- Clearly unjustified concepts: water remains as main requested item; no export; JSON-only export if task asked SVG and participant could have used SVG.
- Expected profile/context: default/core is sufficient.
