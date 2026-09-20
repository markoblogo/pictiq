# Model-by-model profiles

These profiles describe the five supplied transcripts. They are not ranks.

## ChatGPT

- **Blind visual recognition:** Strong for bottle/product, check, snowflake, money, card, and quantity function.
- **Structure:** Recovered all four turns and the question → answer → question → answer pattern.
- **Semantics/numbers:** Recovered a retail exchange but left `2 + 1` and `5 + 1` undecoded.
- **Guided production:** Conservative and mostly protocol-valid; omitted unsupported passengers, bags, and exact count.
- **Repair:** Correctly identifies an additive-quantity documentation issue.
- **Notable failure:** Treats the first question as possibly price rather than availability.

## Claude

- **Blind visual recognition:** Strong except ambiguity between `qty_5` and barcode/scan.
- **Structure:** Recovered a four-turn transaction and recurring bottle.
- **Semantics/numbers:** Recovered cold product and payment; rendered quantity sequences as 2.10/two-one and scan/one/cash.
- **Guided production:** Uses documented IDs and reports omissions; passenger interpretation of `qty_2` remains contextual.
- **Repair:** Supports a documentation clarification for quantity composition.
- **Notable failure:** Visual ambiguity of the five-stroke tile changes the final turn.

## Gemini

- **Blind visual recognition:** Identified the visible glyphs and both quantities accurately.
- **Structure:** Recovered the retail dialogue and four alternating turns.
- **Semantics/numbers:** Recovered three bottles, card payment, and six currency units; currency/payment nuance remains acknowledged as ambiguous.
- **Guided production:** Uses documented IDs but extends `move_feet` and `qty_plus` into passenger/luggage meaning.
- **Repair:** Proposes visual repetition and order changes as hypotheses.
- **Notable failure:** Treats context-dependent proxies as more definite than the guide supports.

## Mistral

- **Blind visual recognition:** Misreads the water glyph as a pencil and quantity glyphs as pause/separators.
- **Structure:** Does not recover the four-turn transaction.
- **Semantics/numbers:** Later semantic mismatches originate before Pictiq semantics can be assessed.
- **Guided production:** Mixes valid concepts with invented `need_taxi`, `person`, `qty_3`, and `bag`.
- **Repair:** Contains unsupported replacements.
- **Notable failure:** Visual-object error followed by vocabulary hallucination.

## Microsoft Copilot

- **Blind visual recognition:** Reports pencil, barcode, pause/barrier, and a rearranged apparent sequence; recognizes question, check, money, and card.
- **Structure:** Does not recover the dialogue structure.
- **Semantics/numbers:** Cannot be assessed independently of the visual mismatch.
- **Guided production:** Uses existing IDs but asserts undocumented quantity and luggage readings.
- **Repair:** Reassigns quantity and punctuation semantics in unsupported ways.
- **Notable failure:** Visual misrecognition combined with unacknowledged protocol extension.
