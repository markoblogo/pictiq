# Cross-model findings

## Evidence status first

The five transcripts are primary evidence, but they do not correspond to the frozen published 05A PNG/JSON. They describe an alternate visual dialogue with additive quantity tiles. The findings below are therefore limited to that supplied result set.

## Observed across all five

- Question mark, check/affirmation, money, and card were recognized as broad visual concepts.
- Each transcript treated the image as an ordered sequence rather than unrelated icons.

## Observed in most (3/5)

- ChatGPT, Claude, and Gemini recovered a retail/service context, cold drink/product, recurring object, and question → answer → question → answer structure.
- ChatGPT, Claude, and Gemini recognized tally-like glyphs as quantities, though only Gemini assigned both intended sums.

## Observed in one or two

- Gemini alone recovered both `2 + 1 = 3` and `5 + 1 = 6` from the blind image.
- Claude alone made the explicit barcode-versus-five visual ambiguity central to its account.
- Mistral and Microsoft Copilot treated the water glyph as writing/pencil-like, which blocks semantic composition assessment.

## Cross-model interpretation

The evidence separates visual recognition from Pictiq semantics. A model can infer transaction structure after recognizing bottle, cold, card, and money without knowing Pictiq. Conversely, a water-glyph or tally-glyph recognition error prevents a meaningful claim that the model failed Pictiq composition.

The clearest protocol pressure is not a new primitive. The current grammar makes pragmatic quantity tiles additive, while the supplied Handbook v1.0 does not state that rule. The exact-number task is additionally invalid as evidence about frozen 05A because frozen 05A deliberately omitted exact quantities.

## Action classification

| Pressure | Classification | Reason |
| --- | --- | --- |
| Additive practical quantity rule in Handbook | HANDBOOK UPDATE CANDIDATE | Current normative grammar is more explicit than the guide used. |
| Canonical stimulus fingerprinting | DOCUMENTATION CLARIFICATION | Record PNG hash/visual manifest before future runs. |
| Water glyph recognition | VISUAL ICON REVIEW CANDIDATE | Two supplied transcripts describe it as pencil-like; separate controlled visual testing is needed. |
| Quantity glyph recognition | VISUAL ICON REVIEW CANDIDATE | One transcript saw barcode and two did not recover quantities. |
| Re-run with frozen 05A image | FUTURE EXPERIMENT | Needed before claiming an outcome for published Stress Test 05. |
| New water, bottle, bag, person, sale, or numeric primitives | NO ACTION | This five-run evidence has visual, documentation, and provenance alternatives; NEED-BEFORE-VOCABULARY is not met. |

## More-model verdict

**METHODOLOGY NEEDS REVISION BEFORE MORE RUNS.** A larger panel would not repair the mismatch between the published frozen stimulus and the image described in the transcripts. First bind the run to one hashed PNG and a recorded prompt/guide version; then decide whether a replication set is useful.

## Publication milestone verdict

**NOT A PUBLICATION MILESTONE.** The dataset is small and exploratory, has unknown/changeable consumer backends, and has a frozen-stimulus provenance mismatch. It is useful research material, not evidence for a public claim about zero-training comprehension.
