# Perplexity ↔ Claude external review comparison

Both reviews are external repository impressions. They do not constitute protocol validation, human evidence, comprehension testing, or adoption evidence. Perplexity is preserved in [review 001](perplexity-review.md); Claude is preserved in [review 002](claude-review-002.md). Claude observations are reconciled in the [findings map](claude-findings-map.md).

| Pressure | Perplexity | Claude | Reconciliation |
|---|---|---|---|
| Composition comprehension | Individual glyph recognition may not transfer to shared sequence meaning. | Unfamiliar recipients may not reliably interpret composed messages; asks for human testing. | Independently raised; already explicit in 05–07 research. Neither reviewer supplies human results. |
| First-use positioning | One concrete scenario and three messages should precede broad positioning. | Narrow scenario; put Composer/demo closer to first screen and add an interaction video. | Independently raised discovery pressure, with distinct proposed fixes. Current site has broad hero; Composer appears later. Not a conversion test. |
| Licensing terminology | “Open”/“open-source” conflicts with CC BY-NC and separate commercial terms. | CC BY-NC may deter integrations; consider separate open protocol/spec license. | Independent convergence on licensing friction. Existing audit says `Open source` is inconsistent with NC terms in the OSI sense; no license change accepted. |
| Vocabulary size / coverage | Avoid expanding vocabulary before testing; test a small scenario corpus. | 87 tiles spread over multiple domains; complete one niche and add airport concepts. | Shared pressure to test coverage before expansion; Claude’s “complete niche” framing and airport priorities are unsupported. Core and canonical registry must not be conflated. |
| External validation | Test 10–15 unfamiliar people on compositions, errors, time, and effect of brief learning. | Test 10–20 people guessing isolated icons; publish percentages. | Both call for human evidence; task-based message comprehension is distinct from isolated icon recognition. No such study executed here. |
| Adoption | Narrow scenario and comprehensible value may improve newcomer orientation. | Network effect is decisive; community posting/first users needed. | Claude raises stronger adoption claim, not independently established. Repository stars/forks are only a time-bound public snapshot. |
| Related-system differentiation | Architecture and tools are strengths; no strong comparison claim. | Suggests open licensing key to Emoji/Bliss success and presents standard-level ambition. | Divergent: Perplexity praises internal architecture; Claude adds a causal historical claim not supported by repository evidence. Existing comparison notes favor neutral differentiation. |
| Machine readability | JSON, Renderer, Composer, validators and CI are a project strength. | Asks for LLM/CV integration and photo/text-to-tile tool. | Complementary but not contradictory. The machine-readable message pipeline is real; Translator/CV integrations remain research/prototype, not production features. |
| Registry/schema | No specific registry flaw identified. | Points to extra lexicon fields beyond strict schema. | Claude reveals a concrete conformance mismatch: data has extra fields, CI validator ignores them despite schema rejecting them. Recorded as new pressure; not fixed in this pass. |
| Airport/travel coverage | Travel card is one possible focused entry case; no airport gap corpus. | Proposes nine airport/accessibility primitives and sample mappings. | Claude-specific pressure. No primitive is added. Missing word matches are not automatically Pictiq gaps; proposed pairs remain candidates pending context-aware assessment. |

## Independently repeated pressures

1. **Composition comprehension requires evidence beyond symbol recognition.** Both distinguish a readable tile from a shared message meaning.
2. **A newcomer needs a concrete first-use path.** Both ask to reduce the distance between the broad protocol description and trying a useful message.
3. **License language and reuse permission need to be clear.** Both notice tension between openness language and noncommercial terms.
4. **Vocabulary expansion should follow demonstrated communication need.** Perplexity recommends testing messages before adding symbols; Claude’s airport proposal provides a test case, although its implied additions are not accepted.

These common themes are pressure signals for research and documentation. They do not override the active controlled experiment: Stress Test 07.1 remains prepared and unexecuted. Composition Library and Translator are parallel knowledge/product architecture tracks, not substitutes for that study or production-case evidence.
