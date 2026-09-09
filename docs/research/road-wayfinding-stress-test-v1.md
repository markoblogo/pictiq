# Pictiq Stress Test 02: Road & Public Wayfinding

> Status: RESEARCH / STRESS TEST  
> Architecture baseline: `d5e3641` — Formalize vocabulary and phrase architecture  
> Date: 2026-09-10  
> Scope: Phase 1 tests current Pictiq only; Phase 2 simulates DEAD, WAVY, and numeric notation hypotheses. No canonical icons, normative architecture, profiles, packs, tags, or releases are changed.

## Research question

How much of an established public-sign communication system can Pictiq express without being redesigned specifically for it? The test asks what breaks first: vocabulary, composition, spatial relations, domain notation, or contextual interpretation.

The success criterion is practical action, not literal redrawing or exact English back-translation. Pictiq preserves the distinction required for the decision, not every distinction present in the source sign system.

## Sources

- [UNECE consolidated Vienna Convention on Road Signs and Signals](https://unece.org/DAM/trans/conventn/Conv_road_signs_2006v_EN.pdf) — international sign classes; warning/prohibitory/mandatory/information/service categories; road-service signs.
- [GOV.UK Highway Code traffic signs guidance](https://www.gov.uk/guidance/the-highway-code/traffic-signs) — UK public explanation of orders, warnings, direction, information, and road works signs.
- [UK Department for Transport / DVSA Know Your Traffic Signs PDF](https://assets.publishing.service.gov.uk/media/656ef4271104cf0013fa74ef/know-your-traffic-signs-dft.pdf) — common road-user sign meanings and examples.
- [FHWA Manual on Uniform Traffic Control Devices current edition page](https://mutcd.fhwa.dot.gov/) — US standard framing for traffic-control devices that regulate, warn, and guide public travel.
- [Arrêté du 24 novembre 1967 relatif à la signalisation des routes et autoroutes](https://www.legifrance.gouv.fr/loda/id/LEGITEXT000006075080) — French/European examples: no entry, no left/right turn, no parking, pedestrians prohibited, speed limit.
- [Amazon.fr listing B0HJ3WMYKD](https://www.amazon.fr/dp/B0HJ3WMYKD) — related project context only, using the user-supplied public listing excerpt. Title: *Французькі правила й дорожні знаки українською: Практичний довідник для першого знайомства і перенесення водійського досвіду до Франції*. Author: Route Atlas Press. Format: Paperback. Visible positioning: Ukrainian practical guide for understanding French road rules/signs and transferring Ukrainian driving experience to France. Price, stock, and delivery details are volatile and are not used as stable research evidence.

The Amazon listing is treated only as related project context. No Amazon preview/book content was copied, and the listing does not validate Pictiq road communication.

## Method

Each case records official/conventional meaning separately from the Pictiq representation. The first pass uses only current accepted Pictiq primitives. The result class is exactly one of: DIRECT, COMPOSED, CONTEXT-SUFFICIENT, LOSSY, DOMAIN-EXTENSION, GAP, OUT-OF-SCOPE.

Failure modes are secondary labels: VOCABULARY, GRAMMAR, RELATION, LAYOUT, NUMERIC/NOTATION, CONTEXT, SAFETY-PRECISION.

## Overall counts

| Result | Count |
| --- | ---: |
| DIRECT | 7 |
| COMPOSED | 3 |
| CONTEXT-SUFFICIENT | 8 |
| LOSSY | 5 |
| DOMAIN-EXTENSION | 1 |
| GAP | 1 |
| OUT-OF-SCOPE | 0 |

## Case matrix

| Case | Official meaning | Required action | Current Pictiq | Back-interpretation | Result | Failure mode | Action ambiguity | Hypothesis improvement | Architectural consequence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turn/go right | Proceed or turn right according to road/public-wayfinding indication. | Move right / choose the rightward route. | `rel_greater` | rightward / greater-side orientation in navigation context | CONTEXT-SUFFICIENT | RELATION, CONTEXT | No in road-wayfinding context; yes outside it, where `>` may mean comparison. | Road convention could reserve `rel_greater` as rightward inside a Road pack. | Relational morphology can carry direction when context is explicit; do not make RIGHT a Core tile yet. |
| turn/go left | Proceed or turn left according to road/public-wayfinding indication. | Move left / choose the leftward route. | `rel_lesser` | leftward / lesser-side orientation in navigation context | CONTEXT-SUFFICIENT | RELATION, CONTEXT | No in road-wayfinding context; yes outside it, where `<` may mean comparison. | Road convention could reserve `rel_lesser` as leftward inside a Road pack. | Same as right: works contextually, not as universal lexical direction. |
| straight/ahead | Continue straight ahead. | Continue forward on the present route. | `rel_up` | up / above / ahead in navigation context | CONTEXT-SUFFICIENT | RELATION, CONTEXT | Low on a road sign; higher in building maps where up may mean upstairs. | Road layout arrow convention can disambiguate ahead vs physically up. | Unary `rel_up` is usable as ahead only with explicit navigation context. |
| down / lower level | Go down, lower level, or downward route. | Move down or choose the lower-level route. | `rel_down` | down / below / lower | DIRECT | — | No for generic lower/down movement. | None needed for first-pass public wayfinding. | Existing relational operator covers the required distinction. |
| no entry | Entry prohibited / do not enter this road or area. | Do not enter or proceed into the signed way. | `rel_here + logic_no` | not here / this place no / no current reference | GAP | VOCABULARY, RELATION, SAFETY-PRECISION | Yes. It can be read as no current location, not available here, or no place here rather than entry forbidden. | Road-specific access/prohibition convention is stronger than a new Core word. | Candidate Road pack notation for access/entry restriction; avoid Core expansion until cross-domain evidence appears. |
| pedestrian route | Route or path for pedestrians. | Walk here / pedestrians should use this route. | `move_feet` | walking / go on foot | CONTEXT-SUFFICIENT | CONTEXT | Low in pedestrian-wayfinding context. | A Road/Public pack may specify that bare walking in route signage means pedestrian route. | No new pedestrian primitive needed for this case. |
| pedestrians prohibited | Access prohibited to pedestrians. | Do not walk here / pedestrians must not enter. | `move_feet + logic_no` | walking/pedestrian movement prohibited | COMPOSED | — | No material ambiguity for the required action. | No hypothesis needed. | Strong success for current composition and postfix negation. |
| pedestrian crossing | Pedestrian crossing or crossing place. | Expect/use a crossing point; drivers yield/slow where applicable; pedestrians cross here. | `move_feet + rel_here` | walking here / pedestrian movement at this location | LOSSY | RELATION, LAYOUT, SAFETY-PRECISION | Yes. Walking here is not the same as a crossing relation between two sides of a road. | A crossing/path relation or Road pack layout convention could preserve the missing distinction. | Candidate Road/Public relation, not immediate Core. |
| parking | Parking place or parking permitted. | A driver may park here / find parking here. | `rel_here + move_car` | car here / car at this place | CONTEXT-SUFFICIENT | CONTEXT | Low in road context. Outside it, this could mean car location rather than permission to park. | A Road pack could define `rel_here + move_car` as parking-place shorthand. | Parking is not a lexical gap in first pass. |
| no parking | Parking prohibited. | Do not park here. | `rel_here + move_car + logic_no` | car-at-this-place prohibited / no car here | CONTEXT-SUFFICIENT | CONTEXT, SAFETY-PRECISION | Usually acceptable in road context, but can overread as all cars prohibited here. | Road prohibition convention could narrow it to parking rather than vehicle presence. | Works compositionally enough for first pass; review only if legal precision is required. |
| fuel/petrol station | Fuel service or petrol station. | Go here for fuel. | `place_gas` | gas station / fuel place | DIRECT | — | No material ambiguity. | None needed. | Existing contextual tile succeeds as direct service sign. |
| hospital/medical | Hospital or medical service nearby. | Go here for medical help. | `safety_medical` | medical help / medical service | DIRECT | — | No material ambiguity for wayfinding. | None needed. | Existing Core/safety tile succeeds. |
| police | Police service or police post. | Go here for police help or comply with police-point indication. | `safety_police` | police / police help | DIRECT | — | No material ambiguity. | None needed. | Existing Core/safety tile succeeds. |
| food/restaurant | Food service / restaurant available. | Go here for food. | `need_food` | food / need food | CONTEXT-SUFFICIENT | CONTEXT | Low in service-sign context, but it does not distinguish restaurant, grocery, or food need. | Context packs can refine restaurant/grocery if the action differs. | No Core expansion; context may select food subcategory tiles where needed. |
| hotel | Hotel/accommodation available. | Go here for lodging. | `place_hotel` | hotel | DIRECT | — | No material ambiguity. | None needed. | Existing contextual tile succeeds directly in road-service context. |
| information | Information point / tourist or public information. | Go here to obtain information. | `media_text` | text / writing / document | LOSSY | VOCABULARY, CONTEXT | Yes. Written text is not always an information service, and information can be spoken/digital. | `media_text + comm_speak` improves service feel but remains broad. | Potential Public/Wayfinding context primitive, but not automatically Core. |
| warning/caution | General danger warning or caution ahead. | Pay attention, slow, prepare for hazard. | `punct_exclaim` | attention / urgent / caution | DIRECT | — | No for generic caution; yes if the hazard type or severity changes action. | DEAD could represent extreme/deadly danger, not generic warning. | `!` is enough for generic warning, not for all danger severity. |
| road works | Road works or maintenance ahead. | Expect works, slow down, follow temporary routing. | `service_tools + punct_exclaim` | tools/repair/service with caution | CONTEXT-SUFFICIENT | CONTEXT | Low in road context; outside it could mean repair help or tools needed. | Road pack could define this as works/maintenance ahead. | Contextual polysemy is adequate; no road-works tile yet. |
| slippery road | Road surface may be slippery. | Slow down, avoid abrupt steering/braking, increase caution. | `punct_exclaim` | caution / urgent attention | LOSSY | VOCABULARY, SAFETY-PRECISION | Yes. Generic warning does not say surface traction is the issue. | WAVY + `punct_exclaim` preserves problematic/unstable surface more clearly. | Evidence for a surface-irregularity primitive or road/domain notation. |
| uneven/bumpy road | Uneven or rough road surface ahead. | Slow down and expect rough surface/vehicle movement. | `punct_exclaim` | caution / urgent attention | LOSSY | VOCABULARY, SAFETY-PRECISION | Yes. Generic caution loses the surface condition. | WAVY + `punct_exclaim` may compress slippery/uneven into a shared surface-problem warning. | Same WAVY evidence as slippery road. |
| speed bump | Speed hump/bump ahead. | Slow down before a vertical traffic-calming feature. | `rel_up + punct_exclaim` | up/ahead with caution | LOSSY | VOCABULARY, RELATION, SAFETY-PRECISION | Yes. It may mean go up, uphill, upstairs, or caution ahead, not a bump. | WAVY helps only partly; a bump may require road-specific surface/traffic-calming notation. | Most adversarial WAVY case; likely Road-pack refinement if precision matters. |
| dead end | Road has no through continuation. | Do not expect through passage; turn around or choose another route if needed. | `rel_up + logic_no` | no ahead / no upward-forward continuation | COMPOSED | CONTEXT | Low in road navigation context, but not safe outside it. | Do not use DEAD; dead end is a linguistic coincidence. | Current composition is adequate for simple wayfinding. |
| speed limit 50 | Do not exceed 50 in the jurisdiction's speed unit. | Keep speed at or below 50 km/h or mph depending on jurisdiction. | `qty_5 + qty_5` | ten / two fives; not fifty and not speed limit | DOMAIN-EXTENSION | NUMERIC/NOTATION, VOCABULARY, SAFETY-PRECISION | Yes. Current quantity primitives cannot encode exact 50 or maximum-speed rule. | Digits `50` plus established road speed-limit convention solve the case better than Core expansion. | Create a shared numeric notation layer candidate; Road pack can reference it. |
| no left turn | Turning left at the next junction is prohibited. | Do not turn left. | `rel_lesser + logic_no` | left/lesser orientation prohibited | COMPOSED | RELATION, CONTEXT | Low in road context. Adding `move_car` is usually redundant because the sign context supplies vehicle/road use. | Road prohibition convention could make the maneuver restriction explicit. | Existing relation + negation works if Road context is clear. |
| you are here/current location | Current viewer/location reference point on a map or wayfinding board. | Orient from this point. | `rel_here` | here / current reference point / target | DIRECT | — | No material ambiguity in a wayfinding layout. | None needed. | HERE reference semantics are coherent across map/current-location use. |

## Best existing-Pictiq successes

- `move_feet + logic_no` cleanly handles pedestrians prohibited.
- `rel_here` cleanly handles you-are-here/current-location reference.
- `place_gas`, `safety_medical`, `safety_police`, and `place_hotel` work directly for service/facility signs.
- `punct_exclaim` is adequate for generic caution where hazard type does not change the required action.
- `rel_lesser + logic_no` is a plausible no-left-turn representation when road context supplies vehicle/turn interpretation.

## Strongest current failures

- No entry is not honestly captured by `rel_here + logic_no`; entry/access prohibition is missing.
- Pedestrian crossing loses the crossing/path relation. `move_feet + rel_here` says walking here, not crossing here.
- Speed limit 50 exposes the numeric/notation layer gap: current quantity tiles cannot encode exact 50 or maximum speed.
- Slippery/uneven/speed-bump signs show that generic caution loses safety-relevant surface information.
- Information point is only approximated by `media_text`; information service is broader than text/writing.

## Parking result

Parking works compositionally enough in road context as `rel_here + move_car`. No parking as `rel_here + move_car + logic_no` has a plausible “no car here” reading, but in road context that is close enough to “do not park here” for many practical uses. This is CONTEXT-SUFFICIENT, not a lexical gap.

## Information result

`media_text` is lossy. It can imply written information, but it does not reliably express an information point, help desk, visitor information, or spoken/digital information. Recommendation: keep as a Public/Wayfinding contextual candidate, not Core.

## Warning result

`punct_exclaim` is enough for generic warning/caution. It is not enough for hazard type or extreme/deadly danger when that distinction changes behavior.

## DEAD hypothesis

DEAD helps only a narrow subset of this road test: extreme/deadly danger, not generic warning and not dead end. It has plausible cross-domain utility in medical, narrative, and safety contexts, but this experiment alone does not justify canonicalization or Core status.

Recommendation: **DEFER**. If explored later, test it across road/safety, medical, narrative, and general warning cases before assigning a role.

## WAVY hypothesis

WAVY improves slippery road and uneven/bumpy road, and partly improves speed bump. It also has plausible non-road utility for waves/rough water and unstable physical surfaces. The compression is useful, but speed bump remains adversarial: the required action may be more specific than generic surface caution.

Recommendation: **CONTEXTUAL/DEFER**. Treat WAVY as a strong Road/Surface candidate, not Core.

## Slippery / uneven / speed-bump comparison

One broad WAVY primitive can preserve the shared practical action “surface problem ahead; slow down / be careful” for slippery and uneven/rough road. Speed bump is weaker because the driver must prepare for a discrete raised feature, not only a low-friction or rough surface. If legal/traffic-calming precision matters, speed bump may need Road-specific refinement.

## Numeric notation recommendation

Digits should be treated as a shared notation layer candidate, not as ordinary lexical vocabulary and not as replacements for `qty_1`, `qty_2`, and `qty_5`. Exact numeric notation and pragmatic small-quantity communication solve different problems. A future notation registry could be referenced by Road, accounting, retail, science, measurement, and timetable packs.

## Speed-limit-50 result

Current Pictiq fails. `qty_5 + qty_5` means ten under current grammar, not fifty, and it does not encode speed or maximum/limit. The best architecture is DOMAIN-EXTENSION: use ordinary numeric notation `50` inside established Road speed-limit convention, with Pictiq coexisting rather than replacing the domain notation.

## No-left-turn result

`rel_lesser + logic_no` works as COMPOSED when road context is explicit. Adding `move_car` usually adds redundancy because the road sign already supplies vehicle/road use. The remaining weakness is relation/context collision outside Road.

## Dead-end result

`rel_up + logic_no` is adequate in road/navigation context: no continuation ahead. DEAD/DEATH must not be used for dead end; the English word “dead” is accidental and not semantic evidence.

## Pedestrian-crossing result

Current Pictiq is lossy. `move_feet + rel_here` can mean walking here, but crossing requires a relation between pedestrian movement, a crossing path/location, and often driver yielding. This is a relation/layout gap and a Road/Public candidate.

## `< > ∧ ∨` directional result

The relational family is workable as direction only when the Road/Wayfinding context is explicit. It is strongest for no-left-turn and simple directional arrows; weaker for ahead/up ambiguity and for crossing/path relations. This does not require a grammar change, but it does argue for domain conventions when the sign surface is road-specific.

## HERE result

`rel_here` is coherent across you are here, current location, parking here, hotel here, and target/reference. The test supports keeping it as a reference operator rather than turning it into a generic place noun.

## Phrase Architecture result

No accepted Phrase Architecture rule failed materially. The failures are mostly vocabulary, relation/layout, and numeric/domain-notation gaps. Bare adjacency, postfix negation, whole-phrase punctuation, unary contextual relation, and one-proposition-per-line were sufficient for the tested compositions.

## Proposed Road/Public Wayfinding additions

These are recommendations only, not implementation:

- Road access/prohibition notation for no entry.
- Crossing/path relation or layout convention for pedestrian crossing.
- Surface-irregularity candidate, possibly WAVY, for slippery/uneven/rough surface.
- Road-specific refinement for speed bump if practical action requires it.
- Information-point contextual primitive, pending more service-sign cases.
- Shared numeric notation layer, referenced by Road speed-limit conventions.

## Genuine Core evidence

No new concept has enough evidence from this Road-only test to become Core. DEAD has possible cross-domain evidence but remains unproven. WAVY is stronger as contextual. Numeric notation should be a shared notation layer, not Core vocabulary.

## Human Decision Queue

1. Should DEAD enter the candidate backlog, and if so as DEFER pending cross-domain medical/narrative/safety evidence?
2. Should WAVY be accepted as a contextual surface-irregularity candidate, or held until non-road uses are tested?
3. Should Pictiq create a shared numeric notation registry separate from ordinary lexical tiles?
4. Should Road/Public Wayfinding define domain conventions for speed limits instead of trying to express them in pure Pictiq?
5. Is a crossing/path relation needed for pedestrian crossing, or should it remain Road-pack notation?
6. Is `punct_exclaim` sufficient for generic warning while DEAD handles only extreme/deadly danger?
7. Are `< > ∧ ∨` safe as directional operators when a Road/Wayfinding context is explicit?
8. Should `rel_here + move_car` be accepted as parking shorthand in Road context?
9. Does “information point” justify a Public/Wayfinding contextual primitive, or can `media_text` plus context remain enough?
10. Did this test expose any Phrase Architecture rule that needs normative change? Current result: no, only domain notation gaps.

## Visual comparison sheets

The rebuilt sheets compare schematic conventional road/public signs with exact current Pictiq tile sequences rendered from repository SVG assets. They are presentation artifacts only and do not change the analytical classifications. DEAD and WAVY appear only in a separate hypothesis area marked “not canonical.”

## Artifacts

- Machine-readable matrix: [`road-wayfinding-stress-test-v1.json`](road-wayfinding-stress-test-v1.json)
- Full visual comparison sheet: [`../../build/research/road-wayfinding-comparison.png`](../../build/research/road-wayfinding-comparison.png)
- Selected visual comparison sheet: [`../../build/research/road-wayfinding-comparison-selected.png`](../../build/research/road-wayfinding-comparison-selected.png)
- Book-materials note: [`../book-materials/experiments/road-wayfinding-stress-test.md`](../book-materials/experiments/road-wayfinding-stress-test.md)

## Closeout confirmations

- Normative spec unchanged: yes.
- Canonical lexicon remains 75 ordinary IDs: yes.
- Entity symbols remain separate: yes.
- No icons created: yes.
- No tag/release created: yes.
- Nothing pushed: yes.
