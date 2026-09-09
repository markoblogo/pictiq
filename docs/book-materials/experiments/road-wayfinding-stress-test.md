# Road & Public Wayfinding Stress Test

> Status: RESEARCH NOTE + ACCEPTED FOLLOW-UP / NOT SPEC
> Source artifact: [Pictiq Stress Test 02](../../research/road-wayfinding-stress-test-v1.md)  
> Date: 2026-09-10

## Human-accepted final visual representation

The authoritative visual result is [`assets/road-wayfinding-pictiq-representation.png`](assets/road-wayfinding-pictiq-representation.png). The supplied image is preserved exactly as supplied and should be treated as the human-accepted final comparison for Stress Test 02.

It incorporates later human semantic review. It was not regenerated from the original v1 JSON and should not be treated as an official legal road-sign source.

## Starting question

Can current Pictiq communicate established road and public-wayfinding meanings without being redesigned for road signs?

## Methodology

The experiment used 25 common road/public-wayfinding cases. Each case separated official/conventional meaning from current Pictiq representation, neutral back-interpretation, practical action, result class, failure mode, and action ambiguity. Phase 1 used only current accepted Pictiq primitives. Phase 2 simulated three hypotheses: DEAD, WAVY, and numeric notation. A later acceptance pass converted two hypotheses into contextual canonical primitives and converted numeric `50` into the first partial shared numeric-notation rendering.

## Surprising successes

- Pedestrians prohibited works cleanly as `person_generic + move_feet + logic_no`; pedestrian meaning needs PERSON plus FEET/WALKING.
- Parking works better than expected as `rel_here + move_car` in road context.
- No left turn is plausible as `rel_lesser + logic_no` without adding `move_car`.
- `rel_here` held together across current location, target, parking here, and hotel here.

## Failures

No entry, pedestrian crossing, speed limit 50, and information point exposed real gaps. Slippery road and uneven road are not honest with generic `punct_exclaim` alone because surface hazard information is lost.

## Rejected approaches

- Do not redraw road signs literally as Pictiq icons.
- Do not turn every conventional sign into Core vocabulary.
- Do not use DEAD for dead end; that is an English-language coincidence.
- Do not solve speed limit 50 by adding `50` as a Core lexical word.

## DEAD / WAVY hypotheses

The acceptance pass added `surface_wavy` and `state_dead` as contextual ordinary canonical primitives. `surface_wavy` keeps the broad WAVY / UNEVEN / UNSTABLE / SLIPPERY / WAVES / SURFACE IRREGULARITY field and must not be narrowed to “slippery road.” `state_dead` remains contextual rather than Core: it is useful for death/not-alive/deadly-context messages, but current evidence still says complexity belongs to the contexts that require it.

## Numerical notation question

Speed limit 50 produced a partial shared notation layer under `notation/numeric/`. The pass implemented the referenced `5` and `0` digit assets plus a canonical `50` rendering. It did not create `num_50`, and it did not replace `qty_1`, `qty_2`, `qty_5`, `qty_plus`, or `qty_minus`. Context packs may reference numeric notation; they do not own it exclusively.

## Final displayed result counts

The human-accepted image displays these 25-case counts and they should not be silently recalculated from older rejected mappings:

- DIRECT: 7
- COMPOSED: 3
- CONTEXT-SUFFICIENT: 8
- LOSSY: 5
- DOMAIN-EXTENSION: 1
- GAP: 1
- OUT-OF-SCOPE: 0

## Architectural lessons

The test supports the current architecture: Core should stay small, Road-specific complexity should live in a context pack or notation layer, and Pictiq can coexist with established domain conventions. The phrase grammar did not need immediate normative changes; the failures were mostly vocabulary, relation/layout, and numeric notation issues.

## Methodological lesson

Future Pictiq stress tests should validate source meaning, validate Pictiq semantic mapping, obtain human acceptance, and only then create the final visual comparison. Polished visual output must not substitute for semantic validation.

## Book/publication connection

The related road-sign publication is the Ukrainian-language paperback *Французькі правила й дорожні знаки українською: Практичний довідник для першого знайомства і перенесення водійського досвіду до Франції*, credited to Route Atlas Press on the user-supplied Amazon listing excerpt. Its positioning around French signs, Ukrainian driver experience transfer, and practical action makes road signage a natural real-world field for testing Pictiq architecture. It does not validate Pictiq. The experiment may later support essays, future Pictiq book chapters, or public-communication research notes.

## Visual comparison sheets

The experiment now has one human-accepted final visual representation. Earlier Codex-generated comparison sheets are rejected as final outputs because human review found source-sign and Pictiq-mapping problems. They are retained only as intermediate history.

- [Human-accepted final visual representation](assets/road-wayfinding-pictiq-representation.png)
- Rejected intermediate full sheet: `build/research/road-wayfinding-comparison.png`
- Rejected intermediate selected sheet: `build/research/road-wayfinding-comparison-selected.png`
