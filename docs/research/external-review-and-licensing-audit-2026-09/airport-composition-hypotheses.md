# Airport composition hypotheses from External Review 002

**Status:** `FUTURE CORPUS PRESSURE / NOT TESTED / NOT ACCEPTED TRANSLATIONS`
**Rule:** A source-language word with no matching tile is not automatically a missing Pictiq primitive. Apply current `NEED-BEFORE-VOCABULARY`, communication mode, context, semantic preservation, and task-safety rules first.

## Current identifier check

The current 87-ID ordinary registry contains relevant existing IDs including:

- `place_airport` — airport;
- `move_public` — public transport;
- `media_text` — text / written information;
- `person_generic` — generic person / human participant;
- `punct_question`, `punct_exclaim`, and current relation, time, and logic operators.

It does not contain an exact ID for passport/document, ticket/boarding pass, luggage/bag, plane/flight, lost/missing, wait/queue, gate, entrance/exit, or wheelchair. There is no `move_plane` identifier. Absence is an inventory fact, not a `GAP` determination.

## Owner hypotheses / candidate compositions

| Natural-language intent | Owner hypothesis | Current status and constraints |
|---|---|---|
| Personal document / passport | `media_text + person_generic` | `OWNER HYPOTHESIS / CANDIDATE COMPOSITION`. May support an identity/document reading only in a suitable, already shared identity/document-inspection context. Without that context it may mean person information, text about a person, or another association. Not accepted, not normative, not tested. |
| Ticket | `media_text` | `OWNER HYPOTHESIS / CANDIDATE COMPOSITION`. Could point to or request written information in context, but does not intrinsically distinguish ticket from other text. Context and action must be recorded. |
| Plane ticket | `media_text + [plane concept]` | No plane/flight primitive exists, so no Pictiq sequence is proposed. Do not invent an ID or imply current support. |
| Public-transport ticket | `media_text + move_public` | `OWNER HYPOTHESIS / CANDIDATE COMPOSITION`. Candidate association only; test whether ticket/payment/transport is clear in the target airport context. |
| Bus/taxi to airport | `move_public + place_airport` or `move_taxi + place_airport` | `CANDIDATE COMPOSITION` based on present IDs and Grammar examples; the exact relation and intended action remain context-dependent and have not been human-tested here. |
| Lost object / lost person | No accepted composition | Do not use `person_generic + logic_no` as an assumed solution. A wrong interpretation could change urgent action. Preserve ambiguity and allow `LOSSY`, `GAP`, or human review until a task-specific representation is assessed. |
| Wait, gate, entrance/exit, wheelchair/accessibility | No owner composition supplied | Test as intents in a future corpus. Do not infer that a symbol must exist simply because English has a noun or accessibility is a repository topic. |

These examples are intents for future analysis, not phrase translations, message records, or accepted coverage claims. If later tested, preserve the original task, audience, communication mode, what context supplies, expected receiver action, and observed repairs.

## Future airport corpus

A future, bounded airport corpus may classify each task as `PRESERVED_EXPLICITLY`, `PRESERVED_BY_COMPOSITION`, `CONTEXT-SUFFICIENT`, `EMBODIED-OMITTABLE`, `INTENTIONAL_OMISSION`, `LOSSY`, `GAP`, or `OUT-OF-SCOPE`, using the current semantic-compression and Protocol terminology. Include risk/action ambiguity and whether it is Embodied or Standalone. The 15–20 phrase storyboard suggested by Claude is a candidate corpus size, not an accepted protocol threshold.

This pass did not run that corpus, accept airport translations, add vocabulary, or change the existing Road/Wayfinding test.
