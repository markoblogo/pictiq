# Pictiq Grammar (Draft)

## 1. Default reading (Zero-Intent)
Any object icon is a valid message by default.
Example: `need_toilet` can mean "toilet?" / "I need a toilet" depending on context.

## 2. Punctuation operators
- `punct_question` (`?`) — question / where / how / is there / can I
- `punct_exclaim` (`!`) — urgent / attention / please help / insist

Examples:
- `need_toilet + punct_question`
- `safety_medical + punct_exclaim`

## 3. Negation
Negation is expressed by a diagonal slash overlay on an icon.
Meaning: no / not / forbidden / without / allergy.
Users may also draw the slash manually on printed products.

Examples:
- (slashed) `money_card` → "no card / card not accepted"
- (slashed) `need_food` → "no food / don't want food"

## 4. Polysemy rule
Some icons may act as actions in context:
- `move_feet` → walk / go on foot
- `move_public` → ride by public transport
- `money_coins` / `money_card` → pay / buy / money operation
- `move_car` → car / drive / car rental (context dependent)

## 5. Quantity
Quantity follows the object: WHAT then HOW MUCH.
Allowed quantity set (core): `qty_1`, `qty_2`, `qty_5`, `qty_plus`, `qty_minus`.
"Many" may be expressed by repeating `qty_5`.

Examples:
- `need_water + qty_2`
- `need_food + qty_1`
- `need_water + qty_5 + qty_5` (many)

## 6. Compounds (BASE + QUALIFIER)
Two adjacent icons can form a compound:
Left = base concept, right = qualifier.

Examples:
- `place_shop + comm_phone` → phone/electronics shop
- `place_shop + need_food` → grocery
- `move_car + service_tools` → car repair/service

## 7. Phrase examples (non-exhaustive)
- `need_toilet ?`
- `safety_medical !`
- `need_water II money_coins`
- `move_taxi ? money_card`
- `move_public ? time`
