# Pictiq Grammar (Draft)

Notation:
- `A + B + C` means adjacent icons in a phrase (left to right).

## 1. Default reading (Zero-Intent)
Any object icon is a valid message by default.
Example: `need_toilet` can mean "toilet" / "I need a toilet" depending on context.

## 2. Punctuation operators
- `punct_question` — question / where / how / is there / can I
- `punct_exclaim` — urgent / attention / please help / insist

Examples:
- `need_toilet + punct_question`
- `safety_medical + punct_exclaim`

## 3. Negation (logic_no token)
Negation is expressed with an explicit token:
- `X + logic_no`

`logic_no` can also be used standalone as an answer meaning "no".

Meaning (context dependent): no / not / forbidden / without / allergy.

Physical shortcut: users may also draw the diagonal slash with a marker on printed products (for example on fabric),
but examples in this spec use token form.

Examples:
- `money_card + logic_no` → "no card / card not accepted"
- `need_food + logic_no` → "no food / don't want food"

## 4. Fixed negations (single-tile icons)
Some lexicon icons may encode a negated concept directly as a single tile (for example, a tile that already includes
a bold diagonal slash over an object). These are lexicon items, not operators.

Use cases:
- signage where a single tile is preferred
- fixed phrases that should not be compositional

## 5. Polysemy rule
Some icons may act as actions in context:
- `move_feet` → walk / go on foot
- `move_public` → ride by public transport
- `money_coins` / `money_card` → pay / buy / money operation
- `move_car` → car / drive / car rental (context dependent)

## 6. Quantity
Quantity follows the object: WHAT then HOW MUCH.
Allowed quantity set (core): `qty_1`, `qty_2`, `qty_5`, `qty_plus`, `qty_minus`.
"3" is expressed as `qty_1 + qty_2`.
"Many / more" is better approximated by `qty_5 + qty_plus`; repeating `qty_5` remains available when the intended reading is a concrete total of ten.

Examples:
- `need_water + qty_2`
- `need_food + qty_1`
- `need_water + qty_1 + qty_2` (3)
- `need_water + qty_5 + qty_plus` (many / more)
- `need_water + qty_5 + qty_5` (10)

Quantity and physical scale are distinct. `qty_plus` and `qty_minus` MUST NOT be treated as LARGE and SMALL without an independently defined modifier mechanism.

## 7. Compounds (BASE + QUALIFIER)
Two adjacent icons can form a compound:
Left = base concept, right = qualifier.

Examples:
- `place_shop + comm_phone` → phone/electronics shop
- `place_shop + need_food` → grocery
- `move_car + service_tools` → car repair/service
- `place_hotel + qual_good` → hotel evaluated as good / satisfactory
- `need_food + qual_bad` → food evaluated as bad / unsatisfactory

`qual_good` and `qual_bad` are postfix evaluation modifiers. They qualify a base concept only; they do not encode every emotional or moral meaning of “good” and “bad.” `logic_yes` means confirmation / acceptance / open / yes, while `qual_good` means positive evaluation. `logic_no` means negation / prohibition / closed / no, while `qual_bad` means negative evaluation.

Parametric COLOR and entity-symbol mechanisms are classified in [Protocol §1.2](PROTOCOL.md#12-communication-primitive-classes) but are not current grammar tokens. `rel_greater` (`>`) and `rel_lesser` (`<`) are provisional relational operators described below.

## 7.1 Relational and directional operators (provisional)

`rel_greater` (`>`) and `rel_lesser` (`<`) compare adjacent concepts. In a form such as `OBJECT_A + rel_greater + OBJECT_B`, they can mean that A is larger, greater, or more than B; the interpretation is relational and contextual. They do not mean “give me more,” which remains `qty_plus`, and they do not replace `qty_minus` for reduction.

In a clear navigation context, the same operators MAY indicate rightward (`move_feet + rel_greater`) or leftward (`move_feet + rel_lesser`). This is contextual direction, not a redefinition of LARGE as right or SMALL as left; a dedicated direction mechanism may still be preferable where ambiguity is dangerous.

## 8. Phrase length guidance
- Maximum allowed phrase length: 5 icons.
- Recommended optimal phrase length: up to 3 icons.

## 9. Phrase examples (non-exhaustive)
- `need_toilet + punct_question`
- `safety_medical + punct_exclaim`
- `need_water + qty_2 + money_coins`
- `move_taxi + money_card + punct_question`
- `move_public + time + punct_question`
