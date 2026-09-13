# Web/UI Pictiq Stress Test 2026-09

> Status: HUMAN SEMANTIC RECONCILIATION COMPLETE / LOCAL RESULTS FOR HUMAN REVIEW
> Pictiq release baseline: v1.2.0 plus local `action_change` addition
> Boundary: research/governance reconciliation only. No grammar, Message Schema, Shorthand grammar, Renderer semantics, Composer behavior, Entity Symbol, Numeric Notation, or Web/UI Context Pack changes.

## Research question

How well can current Pictiq represent common modern software/UI meanings without speculative vocabulary growth?

## Method history

The useful sequence was:

1. Initial domain stress test.
2. Automated/structured analysis.
3. Human semantic review.
4. Reconciled result.

The initial pass found 24 intents and reported three GAP cases: loading/processing, save/persistence, and archive/retain-but-hide. Human review found that two of those apparent gaps were recoverable through context/polysemy, and the third is an unresolved composition candidate rather than a reason to create an archive icon now.

## Vocabulary governance conclusion

The accepted rule is **NEED-BEFORE-VOCABULARY**. Pictiq does not add a new primitive merely because a concept is common, useful, conventional, or theoretically desirable. Try existing primitive -> composition -> context -> polysemy -> intentional omission -> only then consider a new symbol.

Rule path: [`../../../spec/VOCABULARY_GOVERNANCE.md`](../../../spec/VOCABULARY_GOVERNANCE.md).

## Reconciled counts

### Semantic compression

| Label | Count |
| --- | ---: |
| `PRESERVED_EXPLICITLY` | 2 |
| `PRESERVED_BY_COMPOSITION` | 10 |
| `CONTEXT-SUFFICIENT` | 11 |
| `INTENTIONAL_OMISSION` | 0 |
| `LOSSY` | 1 |
| `GAP` | 0 |

### Practical outcome

| Label | Count |
| --- | ---: |
| `WORKS_AS_IS` | 2 |
| `WORKS_WITH_COMPOSITION` | 10 |
| `WORKS_ONLY_WITH_STRONG_CONTEXT` | 11 |
| `AMBIGUOUS` | 1 |
| `POOR_FIT` | 0 |
| `GAP` | 0 |

## Reconciled cases

| Case | Intent | Pictiq | Compression | Outcome | Status |
| --- | --- | --- | --- | --- | --- |
| `WEBUI-01` | Back to previous screen or step | `rel_lesser` | CONTEXT-SUFFICIENT | WORKS_ONLY_WITH_STRONG_CONTEXT | CONTEXTUAL_REUSE |
| `WEBUI-02` | Forward / next step | `rel_greater` | CONTEXT-SUFFICIENT | WORKS_ONLY_WITH_STRONG_CONTEXT | CONTEXTUAL_REUSE |
| `WEBUI-03` | Home/start/dashboard | `place_home` | CONTEXT-SUFFICIENT | WORKS_ONLY_WITH_STRONG_CONTEXT | CONTEXTUAL_REUSE |
| `WEBUI-04` | Close/cancel dialog | `logic_no` | CONTEXT-SUFFICIENT | WORKS_ONLY_WITH_STRONG_CONTEXT | CONTEXTUAL_REUSE |
| `WEBUI-05` | Selected item | `logic_yes` | CONTEXT-SUFFICIENT | WORKS_ONLY_WITH_STRONG_CONTEXT | CONTEXTUAL_REUSE |
| `WEBUI-06` | Active/current page | `rel_here` | PRESERVED_EXPLICITLY | WORKS_AS_IS | COMPOSITIONALLY_EXPRESSIBLE |
| `WEBUI-07` | Disabled control | `logic_no` | CONTEXT-SUFFICIENT | WORKS_ONLY_WITH_STRONG_CONTEXT | CONTEXTUAL_REUSE |
| `WEBUI-08` | Loading / processing | `time` | CONTEXT-SUFFICIENT | WORKS_ONLY_WITH_STRONG_CONTEXT | CONTEXTUAL_REUSE |
| `WEBUI-09` | Empty state / no content | `logic_no media_text` | PRESERVED_BY_COMPOSITION | WORKS_WITH_COMPOSITION | COMPOSITIONALLY_EXPRESSIBLE |
| `WEBUI-10` | Success/completed | `logic_yes qual_good` | PRESERVED_BY_COMPOSITION | WORKS_WITH_COMPOSITION | COMPOSITIONALLY_EXPRESSIBLE |
| `WEBUI-11` | Error/failure | `qual_bad punct_exclaim` | PRESERVED_BY_COMPOSITION | WORKS_WITH_COMPOSITION | COMPOSITIONALLY_EXPRESSIBLE |
| `WEBUI-12` | Save changes | `rel_down media_text` | CONTEXT-SUFFICIENT | WORKS_ONLY_WITH_STRONG_CONTEXT | CONTEXTUAL_REUSE |
| `WEBUI-13` | Publish/send message | `rel_up media_text` | CONTEXT-SUFFICIENT | WORKS_ONLY_WITH_STRONG_CONTEXT | CONTEXTUAL_REUSE |
| `WEBUI-14` | Delete item | `logic_no media_text` | PRESERVED_BY_COMPOSITION | WORKS_WITH_COMPOSITION | COMPOSITIONALLY_EXPRESSIBLE |
| `WEBUI-15` | Archive item | `rel_down media_text` | LOSSY | AMBIGUOUS | COMPOSITION_CANDIDATE_NEEDS_VALIDATION |
| `WEBUI-16` | Edit content | `media_text action_change` | PRESERVED_BY_COMPOSITION | WORKS_WITH_COMPOSITION | ACCEPTED_CORE_ADDITION |
| `WEBUI-17` | Undo / restore previous state | `rel_lesser` | CONTEXT-SUFFICIENT | WORKS_ONLY_WITH_STRONG_CONTEXT | CONTEXTUAL_REUSE |
| `WEBUI-18` | Login/access | `person_generic rel_here` | PRESERVED_BY_COMPOSITION | WORKS_WITH_COMPOSITION | COMPOSITIONALLY_EXPRESSIBLE |
| `WEBUI-19` | Permission denied | `logic_no person_generic` | PRESERVED_BY_COMPOSITION | WORKS_WITH_COMPOSITION | COMPOSITIONALLY_EXPRESSIBLE |
| `WEBUI-20` | Settings/preferences | `service_tools` | CONTEXT-SUFFICIENT | WORKS_ONLY_WITH_STRONG_CONTEXT | CONTEXTUAL_REUSE |
| `WEBUI-21` | Download | `rel_down media_text` | PRESERVED_BY_COMPOSITION | WORKS_WITH_COMPOSITION | COMPOSITIONALLY_EXPRESSIBLE |
| `WEBUI-22` | Upload | `rel_up media_text` | PRESERVED_BY_COMPOSITION | WORKS_WITH_COMPOSITION | COMPOSITIONALLY_EXPRESSIBLE |
| `WEBUI-23` | Text content | `media_text` | PRESERVED_EXPLICITLY | WORKS_AS_IS | COMPOSITIONALLY_EXPRESSIBLE |
| `WEBUI-24` | Notification/message alert | `comm_speak punct_exclaim` | PRESERVED_BY_COMPOSITION | WORKS_WITH_COMPOSITION | COMPOSITIONALLY_EXPRESSIBLE |

## Main reconciled decisions

- Loading / processing / wait: `time` is sufficient in context. Not a current GAP.
- Save / download: `rel_down` plus relevant content can mean save/download/move into storage in UI context. This does not make DOWN canonically equal to SAVE.
- Publish / upload / send: `rel_up` plus content is sufficient in UI context; communication can be added when needed.
- Settings / configuration: `service_tools` is sufficient in software context. No gear/settings icon.
- Empty state: express as absence of relevant content, such as `logic_no media_text` or `logic_no media_image`.
- Archive: `rel_down media_text` is a plausible composition, but not fully resolved; any dedicated ARCHIVE concept is `DEFERRED_UNTIL_NEEDED`.
- Edit: the useful addition is not EDIT but the broader Core primitive `action_change`.

## Gap status after reconciliation

Remaining true GAPs: none.

Unresolved composition candidates:

- ARCHIVE / RETAIN BUT HIDE.

`DEFERRED_UNTIL_NEEDED` concepts:

- ARCHIVE / RETAIN BUT HIDE.
- IT / COMPUTER / DIGITAL SYSTEM.
- SERVER / SYSTEM.
- VIDEO.

Accepted Core additions from this cycle:

- `action_change` only.

## Practical next principle

Do not pre-build vocabulary for a hypothetical Web/UI domain. Attempt actual products/interfaces with current Pictiq, observe direct need, and only then reconsider vocabulary. A simple Pictiq landing page does not currently require archive, server/system, or video icons.

## Publication milestone check

Verdict: `PUBLICATION_MILESTONE_CANDIDATE / READY_FOR_EDITORIAL_DEVELOPMENT_AFTER_HUMAN_APPROVAL`.

Suggested editorial angle: **What a Visual Language Learns When You Make It Describe Software**.

Do not publish from this report directly; use it as the accepted reconciled research base.

## Artifacts

- Machine-readable reconciled results: [`web-ui-stress-test-results.json`](web-ui-stress-test-results.json).
- Visual QA sheet: [`web-ui-stress-test-qa.svg`](web-ui-stress-test-qa.svg).
- Message JSON fixtures: [`messages/`](messages/).
- Rendered SVG fixtures: [`rendered/`](rendered/).
