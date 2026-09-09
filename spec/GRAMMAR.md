# Pictiq Grammar (Draft)

Notation: `A + B + C` means adjacent icons in a phrase, read left to right. A phrase line carries one semantic proposition or intention. Multiple propositions are written as multiple phrase lines.

## 1. Bare tile and zero-intent

Any object icon is a valid message by itself. The bare-tile reading is intentionally underspecified: “this”, “I need this”, “where is this”, “use this”, or another action-relevant reading may be supplied by embodied context, layout, carrier object, or repair dialogue.

Example: `need_toilet` can mean “toilet” or “I need a toilet” depending on context.

## 2. Bare adjacency

Bare adjacency means contextual semantic association. It does not define a fixed grammatical relation such as possession, subject/object, adjective/noun, or English word order.

Examples:

- `place_shop + comm_phone` → phone/electronics shop, where that context is clear.
- `move_car + service_tools` → car repair/service.
- `entity:odysseus@literary + move_boat` → Odysseus associated with a boat/ship in a narrative context.

Where adjacency creates dangerous ambiguity, split the message, add context, specialize the pack, or record a gap.

## 3. Punctuation operators

- `punct_question` — question / where / how / is there / can I
- `punct_exclaim` — urgent / attention / please help / insist

Terminal punctuation is the outer-scope exception: when `punct_question` or `punct_exclaim` appears at the end of a phrase, it applies to the whole phrase line, not only to the immediately preceding tile.

Examples:

- `need_toilet + punct_question`
- `safety_medical + punct_exclaim`

## 4. Postfix operators and scope

Qualifiers, quantities, and negation are postfix by default. They apply to the immediately preceding semantic unit. That unit may be a single tile or a compound already formed by adjacency.

Examples:

- `place_hotel + qual_good` → hotel evaluated as good/satisfactory.
- `need_food + qual_bad` → food evaluated as bad/unsatisfactory.
- `need_water + qty_2` → two waters / two units of water.
- `place_shop + need_food + qual_good` → a food shop/grocery evaluated as good, where the compound is established by context.

`qual_good` and `qual_bad` are evaluation modifiers. `logic_yes` and `logic_no` are logic operators; they MUST NOT be overloaded as generic GOOD/BAD.

## 5. Negation

Negation is expressed with an explicit token: `X + logic_no`. `logic_no` can also stand alone as an answer meaning “no”.

Meaning is context-dependent: no / not / forbidden / without / allergy.

Examples:

- `money_card + logic_no` → no card / card not accepted.
- `need_food + logic_no` → no food / do not want food.

`logic_no` negates the immediately preceding semantic unit. If the intended scope cannot be made safe, reformulate as multiple lines, add context, use a context-specific tile, or record a gap.

Physical shortcut: users may draw a diagonal slash with a marker on printed products, but examples in this spec use token form.

## 6. Fixed negations

Some lexicon icons may encode a negated concept directly as a single tile. These are lexicon items, not operators. They are allowed for signage or fixed phrases where a single tile is preferred and compositional meaning would be worse.

## 7. Polysemy rule

Some icons may act as actions in context:

- `move_feet` → walk / go on foot
- `move_public` → ride by public transport
- `money_coins` / `money_card` → pay / buy / money operation
- `move_car` → car / drive / car rental
- `body_mouth` → mouth / eat / drink / oral intake, when the phrase and situation make the action clear

Polysemy is acceptable only when it remains action-relevant. A tile may cover related practical readings, but it MUST NOT become a general dictionary substitute when the message would mislead.

## 8. Quantity

Quantity follows the object: WHAT then HOW MUCH. Allowed quantity set: `qty_1`, `qty_2`, `qty_5`, `qty_plus`, `qty_minus`.

Consecutive numeric quantity tiles form one additive quantity expression:

- `qty_1 + qty_2` → 3
- `qty_5 + qty_5` → 10

Examples:

- `need_water + qty_2`
- `need_food + qty_1`
- `need_water + qty_1 + qty_2` → three waters
- `need_water + qty_5 + qty_5` → ten waters

`qty_plus` is not mathematical addition. It means more / extra / additional. `qty_minus` means less / fewer / reduce / remove, according to context. `qty_plus` and `qty_minus` MUST NOT be treated as LARGE and SMALL without an independently defined scale-modifier mechanism.

Exact written numbers belong to the separate [Numeric Notation](NUMERIC_NOTATION.md) mechanism. `qty_5 + qty_5` means ten under phrase grammar; it does not mean `50`.

## 9. Relational and orientation operators

The relational-orientation family contains `rel_greater` (`>`), `rel_lesser` (`<`), `rel_up` (`∧`), and `rel_down` (`∨`). These are horizontal/vertical relation operators, not quantity, size, or movement tokens.

Binary form: `A + REL + B`.

- `OBJECT_A + rel_greater + OBJECT_B` → A is greater/larger/more than B, where the comparison is clear.
- `OBJECT_A + rel_lesser + OBJECT_B` → A is less/smaller than B, where the comparison is clear.

Unary/contextual form: `A + REL`. In a clear navigation context, this may indicate orientation from A or from the current reference frame:

- `place_hotel + rel_greater` → hotel/rightward in navigation context.
- `place_hotel + rel_up` → hotel/upstairs/above in navigation context.

Do NOT claim these operators solve all navigation. Where ambiguity is dangerous, context-specific notation may be preferable.

## 10. Here/reference operator

`rel_here` is a reference operator, distinct from the four relational-orientation operators. It marks a selected point, here, current location, target, or reference.

Examples:

- `rel_here + place_hotel`
- `rel_here + time`

`rel_here + time` may contextually mean now / this time / current moment. Do NOT add a separate NOW tile.

## 11. Time and day/night

`nature_sun` and `nature_moon` can combine with `time` to distinguish daylight and nighttime contexts: `time + nature_sun`, `time + nature_moon`. They are not a complete calendar or clock system.

## 12. Multi-clause messages

One semantic proposition or intention belongs on one phrase line. Natural-language multi-clause input SHOULD normally be decomposed into multiple Pictiq phrase lines.

Do NOT introduce AND, BUT, semicolon, or a generic clause-separator tile unless future evidence demonstrates independent need.

Example:

Natural language: “No card, cash only.”

Pictiq:

- line 1: `money_card + logic_no`
- line 2: `money_coins + logic_yes`

Each line is a complete semantic unit.

## 13. Phrase length guidance

- Maximum allowed phrase length: 5 icons.
- Recommended optimal phrase length: up to 3 icons.

## 14. Phrase examples

- `need_toilet + punct_question`
- `safety_medical + punct_exclaim`
- `need_water + qty_2 + money_coins`
- `move_taxi + money_card + punct_question`
- `move_public + time + punct_question`
