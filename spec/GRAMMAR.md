# Pictiq Grammar (Draft)

Notation:
- `A + B + C` means adjacent icons in a phrase (left to right).
- `ICON (overlay_slash)` means the icon with the negation slash overlay applied.

## 1. Default reading (Zero-Intent)
Any object icon is a valid message by default.
Example: `need_toilet` can mean "toilet?" / "I need a toilet" depending on context.

## 2. Punctuation operators
- `punct_question` (`?`) — question / where / how / is there / can I
- `punct_exclaim` (`!`) — urgent / attention / please help / insist

Examples:
- `need_toilet + punct_question`
- `safety_medical + punct_exclaim`

## 3. overlay_slash (operator)
`overlay_slash` is an operator that can be applied to ANY icon.
Meaning: no / not / forbidden / without / allergy.

Supported UX layer: users may also manually slash an icon with a marker on printed products (for example on fabric).

Examples:
- `money_card (overlay_slash)` → "no card / card not accepted"
- `need_food (overlay_slash)` → "no food / don't want food"

## 4. logic_no vs overlay_slash
- `logic_no` is a standalone icon meaning "no".
- `overlay_slash` is a negation operator applied on top of an icon.

Examples:
- `money_card + logic_no` → "no card"
- `money_card (overlay_slash)` → "card not accepted / no card"

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
"Many" may be expressed by repeating `qty_5`.

Examples:
- `need_water + qty_2`
- `need_food + qty_1`
- `need_water + qty_1 + qty_2` (3)
- `need_water + qty_5 + qty_5` (many)

## 7. Compounds (BASE + QUALIFIER)
Two adjacent icons can form a compound:
Left = base concept, right = qualifier.

Examples:
- `place_shop + comm_phone` → phone/electronics shop
- `place_shop + need_food` → grocery
- `move_car + service_tools` → car repair/service

## 8. Phrase length guidance
- Maximum allowed phrase length: 5 icons.
- Recommended optimal phrase length: up to 3 icons.

## 9. Phrase examples (non-exhaustive)
- `need_toilet + punct_question`
- `safety_medical + punct_exclaim`
- `need_water + qty_2 + money_coins`
- `move_taxi + money_card + punct_question`
- `move_public + time + punct_question`
