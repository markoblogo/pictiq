# Web/UI Pictiq Stress Test 2026-09
> Status: LOCAL RESULTS FOR HUMAN REVIEW  
> Pictiq release: v1.2.0  
> Boundary: original language pressure test only; no vocabulary, grammar, Message Schema, Renderer, Composer, icon, Entity Symbol, Numeric Notation, profile, pack, or Context Pack changes were made during the test.
> Post-review update: `action_change` was later accepted as a broader Core CHANGE primitive exposed by `WEBUI-16`, without reconciling the remaining Web/UI concepts.
## Research question

How well can current Pictiq represent common modern software/UI meanings without adding vocabulary during the test?
## Method

The corpus was frozen before Pictiq encoding. Each case records source intent, minimal target, required semantic slots, optional information, and context. Encoding then used only current Pictiq v1.2.0 tokens and Message Schema v0.1. Difficult cases were retained as lossy or gap results rather than repaired by adding vocabulary.
This is an analytical stress test, not a human-comprehension study. Zero-training observations are hypotheses about likely transparency, not evidence from participants.
## Frozen corpus

| Case | Category | Source intent | Required slots | Context |
| --- | --- | --- | --- | --- |
| `WEBUI-01` | NAVIGATION | Back to previous screen or step | PREVIOUS_OR_BACK, NAVIGATION | Header/back-control context |
| `WEBUI-02` | NAVIGATION | Forward / next step | NEXT_OR_FORWARD, NAVIGATION | Wizard/header context |
| `WEBUI-03` | NAVIGATION | Home/start/dashboard | MAIN_DESTINATION | App navigation bar |
| `WEBUI-04` | NAVIGATION | Close/cancel dialog | DISMISS_OR_CANCEL, CURRENT_SURFACE | Dialog/modal context |
| `WEBUI-05` | STATE | Selected item | THIS_OPTION, SELECTED | Choice list context |
| `WEBUI-06` | STATE | Active/current page | CURRENT_LOCATION, ACTIVE_STATE | Navigation tab context |
| `WEBUI-07` | STATE | Disabled control | CANNOT_USE, CONTROL | Button/control context |
| `WEBUI-08` | STATE | Loading / processing | PROCESSING, WAIT | Loading indicator context |
| `WEBUI-09` | STATE | Empty state / no content | NONE_OR_EMPTY, CONTENT_SCOPE | Blank state or list context |
| `WEBUI-10` | STATE | Success/completed | SUCCESS_OR_DONE | Toast/result context |
| `WEBUI-11` | STATE | Error/failure | FAILURE_OR_ERROR, ATTENTION | Error state context |
| `WEBUI-12` | ACTION | Save changes | PERSIST_OR_KEEP, CURRENT_WORK | Editor/form context |
| `WEBUI-13` | ACTION | Publish/send message | SEND_OR_PUBLISH, CONTENT | Composer/editor context |
| `WEBUI-14` | ACTION | Delete item | REMOVE, ITEM | Item/action menu context |
| `WEBUI-15` | ACTION | Archive item | REMOVE_FROM_ACTIVE_VIEW, RETAIN | Mail/task/list context |
| `WEBUI-16` | ACTION | Edit content | CHANGE_OR_MODIFY, CONTENT | Text/image editor context |
| `WEBUI-17` | ACTION | Undo / restore previous state | REVERSE_LAST_ACTION, PREVIOUS_STATE | Editor history context |
| `WEBUI-18` | ACCESS_SYSTEM | Login/access | PERSON, ACCESS_ALLOWED | Login or account context |
| `WEBUI-19` | ACCESS_SYSTEM | Permission denied | PERSON, CANNOT, PERMISSION_OR_ACCESS | Restricted action context |
| `WEBUI-20` | ACCESS_SYSTEM | Settings/preferences | CONFIGURE_OR_SETTINGS | App toolbar/menu context |
| `WEBUI-21` | ACCESS_SYSTEM | Download | RECEIVE_OR_MOVE_DOWN, FILE_OR_CONTENT | File/action toolbar context |
| `WEBUI-22` | ACCESS_SYSTEM | Upload | SEND_OR_MOVE_UP, FILE_OR_CONTENT | File/action toolbar context |
| `WEBUI-23` | CONTENT_COMM | Text content | TEXT_CONTENT | Content-type picker |
| `WEBUI-24` | CONTENT_COMM | Notification/message alert | MESSAGE_OR_COMMUNICATION, ATTENTION | Notification center context |

## Results summary

- Corpus size: 24 cases.
- Rendered current-Pictiq messages: 21 cases.
- True GAP cases: 3.
- Token cost, message cases only: min 1, max 2, average 1.57.
- Frame cost: all non-gap attempts use one flat Message frame.

### Semantic-compression classification

| Label | Count |
| --- | ---: |
| `CONTEXT-SUFFICIENT` | 2 |
| `LOSSY` | 10 |
| `PRESERVED_BY_COMPOSITION` | 7 |
| `PRESERVED_EXPLICITLY` | 2 |
| `GAP` | 3 |

### Practical outcome

| Label | Count |
| --- | ---: |
| `WORKS_ONLY_WITH_STRONG_CONTEXT` | 6 |
| `AMBIGUOUS` | 5 |
| `WORKS_WITH_COMPOSITION` | 5 |
| `WORKS_AS_IS` | 2 |
| `GAP` | 3 |
| `POOR_FIT` | 3 |

### Zero-training analytical observation

| Label | Count |
| --- | ---: |
| `LEARNED_CONVENTION_LIKELY_REQUIRED` | 6 |
| `CONTEXT_DEPENDENT` | 10 |
| `LIKELY_TRANSPARENT` | 4 |
| `UNCLEAR` | 4 |

### Gap/status discipline

| Label | Count |
| --- | ---: |
| `UI_SPECIFIC_CONVENTION` | 5 |
| `CONTEXTUAL_PRESSURE` | 11 |
| `COMPOSITIONALLY_EXPRESSIBLE` | 5 |
| `GAP` | 3 |

## Results table

| Case | Intent | Pictiq | Compression | Practical outcome | Zero-training observation | Pressure |
| --- | --- | --- | --- | --- | --- | --- |
| `WEBUI-01` | Back to previous screen or step | `rel_lesser` | `CONTEXT-SUFFICIENT` | `WORKS_ONLY_WITH_STRONG_CONTEXT` | `LEARNED_CONVENTION_LIKELY_REQUIRED` | direction/navigation ambiguity |
| `WEBUI-02` | Forward / next step | `rel_greater` | `CONTEXT-SUFFICIENT` | `WORKS_ONLY_WITH_STRONG_CONTEXT` | `LEARNED_CONVENTION_LIKELY_REQUIRED` | direction/navigation ambiguity |
| `WEBUI-03` | Home/start/dashboard | `place_home` | `LOSSY` | `AMBIGUOUS` | `CONTEXT_DEPENDENT` | home physical vs UI-start |
| `WEBUI-04` | Close/cancel dialog | `logic_no` | `LOSSY` | `AMBIGUOUS` | `CONTEXT_DEPENDENT` | cancel vs no vs denied |
| `WEBUI-05` | Selected item | `rel_here logic_yes` | `PRESERVED_BY_COMPOSITION` | `WORKS_WITH_COMPOSITION` | `CONTEXT_DEPENDENT` | selection state |
| `WEBUI-06` | Active/current page | `rel_here` | `PRESERVED_EXPLICITLY` | `WORKS_AS_IS` | `LIKELY_TRANSPARENT` | current state |
| `WEBUI-07` | Disabled control | `logic_no` | `LOSSY` | `WORKS_ONLY_WITH_STRONG_CONTEXT` | `CONTEXT_DEPENDENT` | disabled vs permission denied vs unavailable |
| `WEBUI-08` | Loading / processing | `—` | `GAP` | `GAP` | `UNCLEAR` | process/wait state |
| `WEBUI-09` | Empty state / no content | `qty_minus` | `LOSSY` | `POOR_FIT` | `UNCLEAR` | none/empty state |
| `WEBUI-10` | Success/completed | `logic_yes qual_good` | `PRESERVED_BY_COMPOSITION` | `WORKS_WITH_COMPOSITION` | `LIKELY_TRANSPARENT` | success vs selected yes |
| `WEBUI-11` | Error/failure | `qual_bad punct_exclaim` | `PRESERVED_BY_COMPOSITION` | `WORKS_WITH_COMPOSITION` | `LIKELY_TRANSPARENT` | error cause missing |
| `WEBUI-12` | Save changes | `—` | `GAP` | `GAP` | `UNCLEAR` | persistence/storage action |
| `WEBUI-13` | Publish/send message | `media_text comm_speak` | `LOSSY` | `AMBIGUOUS` | `CONTEXT_DEPENDENT` | send vs publish vs speak |
| `WEBUI-14` | Delete item | `logic_no state_dead` | `PRESERVED_BY_COMPOSITION` | `WORKS_WITH_COMPOSITION` | `CONTEXT_DEPENDENT` | delete vs archive vs close |
| `WEBUI-15` | Archive item | `—` | `GAP` | `GAP` | `UNCLEAR` | archive/retain hidden state |
| `WEBUI-16` | Edit content | `media_text service_tools` | `LOSSY` | `POOR_FIT` | `CONTEXT_DEPENDENT` | edit/change action |
| `WEBUI-17` | Undo / restore previous state | `rel_lesser time` | `LOSSY` | `POOR_FIT` | `LEARNED_CONVENTION_LIKELY_REQUIRED` | temporal/action history |
| `WEBUI-18` | Login/access | `person_generic logic_yes` | `LOSSY` | `AMBIGUOUS` | `CONTEXT_DEPENDENT` | identity/access |
| `WEBUI-19` | Permission denied | `person_generic logic_no` | `LOSSY` | `WORKS_ONLY_WITH_STRONG_CONTEXT` | `CONTEXT_DEPENDENT` | permission denied vs no |
| `WEBUI-20` | Settings/preferences | `service_tools` | `LOSSY` | `AMBIGUOUS` | `LEARNED_CONVENTION_LIKELY_REQUIRED` | gear/settings convention |
| `WEBUI-21` | Download | `rel_down media_text` | `PRESERVED_BY_COMPOSITION` | `WORKS_ONLY_WITH_STRONG_CONTEXT` | `LEARNED_CONVENTION_LIKELY_REQUIRED` | download arrow convention |
| `WEBUI-22` | Upload | `rel_up media_text` | `PRESERVED_BY_COMPOSITION` | `WORKS_ONLY_WITH_STRONG_CONTEXT` | `LEARNED_CONVENTION_LIKELY_REQUIRED` | upload arrow convention |
| `WEBUI-23` | Text content | `media_text` | `PRESERVED_EXPLICITLY` | `WORKS_AS_IS` | `LIKELY_TRANSPARENT` | direct content primitive |
| `WEBUI-24` | Notification/message alert | `comm_speak punct_exclaim` | `PRESERVED_BY_COMPOSITION` | `WORKS_WITH_COMPOSITION` | `CONTEXT_DEPENDENT` | message vs alert vs speech |

## Representative successes

- `WEBUI-06` — Active/current page: `rel_here`. rel_here is a strong current-location marker in UI context.
- `WEBUI-10` — Success/completed: `logic_yes qual_good`. YES + GOOD gives positive completion but needs context for operation scope.
- `WEBUI-11` — Error/failure: `qual_bad punct_exclaim`. Bad + urgent marks problem, but not machine error type.
- `WEBUI-23` — Text content: `media_text`. Direct hit.

## Representative ambiguous / lossy / poor-fit cases

- `WEBUI-03` — Home/start/dashboard: `place_home` -> `AMBIGUOUS`. Existing HOME is broad and context can recover app-start, but without UI context it reads as shelter/home.
- `WEBUI-04` — Close/cancel dialog: `logic_no` -> `AMBIGUOUS`. NO can express refusal/cancel only with strong UI context; close/dismiss is not explicit.
- `WEBUI-09` — Empty state / no content: `qty_minus` -> `POOR_FIT`. Minus/less can suggest absence but does not clearly mean empty content.
- `WEBUI-16` — Edit content: `media_text service_tools` -> `POOR_FIT`. Text + tools suggests work on text but does not clearly mean edit.
- `WEBUI-17` — Undo / restore previous state: `rel_lesser time` -> `POOR_FIT`. Previous + time approximates past, not undo/restore.
- `WEBUI-20` — Settings/preferences: `service_tools` -> `AMBIGUOUS`. Tools is close to maintenance/repair, not abstract preferences/configuration.

## True gaps

- `WEBUI-08` — Loading / processing: process/wait state. Current vocabulary lacks wait/loading/process/progress. time alone would be misleading.
- `WEBUI-12` — Save changes: persistence/storage action. No current primitive for save/keep/record/storage; checkmark would overstate completion.
- `WEBUI-15` — Archive item: archive/retain hidden state. Current vocabulary cannot preserve remove-from-view + keep distinction.

## Composition-cost observations

Current Pictiq can express several broad UI meanings with one or two tokens, but UI concepts with process, persistence, authorization, or workflow-state semantics become lossy quickly. The stress point is not long expressions; it is that many short expressions are too broad. `logic_no`, `logic_yes`, `rel_here`, `rel_up`, `rel_down`, `rel_greater`, and `rel_lesser` are useful but become overloaded in UI contexts.

## Recurring language-pressure categories

- state/status vocabulary.
- process/wait/progress concepts.
- persistence/storage/save.
- archive/retain-hidden distinction.
- permission/access/role scope.
- abstract edit/configuration actions.
- UI direction convention vs semantic navigation.
- content object vs action distinction.

## Potential vocabulary/context implications

| Pressure | Recommendation status | Rationale |
| --- | --- | --- |
| WAIT / LOADING / PROCESSING | `WEB_UI_CONTEXT_CANDIDATE` | True gap in this corpus; likely useful beyond UI, but needs more domain evidence before Core. |
| SAVE / KEEP / RECORD | `WEB_UI_CONTEXT_CANDIDATE` | True gap for software persistence; could overlap with documents, storage, memory, records. |
| ARCHIVE / RETAIN BUT HIDE | `WEB_UI_CONTEXT_CANDIDATE` | True gap but strongly software/workflow-specific. |
| SETTINGS / CONFIGURATION | `WEB_UI_CONTEXT_CANDIDATE` | Conventional gear is not semantic; current tools icon is too concrete. |
| SELECTED / ACTIVE / CURRENT distinction | `COMPOSITION_ONLY` | rel_here + logic_yes works analytically; test comprehension before adding. |
| UPLOAD / DOWNLOAD | `NOT_WORTH_ADDING_YET` | Current up/down + content works only by UI convention; better studied in real product context. |
| DELETE | `NEEDS_MORE_EVIDENCE` | Expressible by composition but risky; distinguish delete/archive/close before adding. |

## UI convention vs general meaning

Several failures are not failures to copy a conventional glyph. Pictiq does not need to reproduce floppy-disk save, gear settings, cloud-arrow upload/download, or hamburger-menu conventions. The question is whether it can express the semantic intent. In this corpus, the hardest cases are genuine semantic gaps around persistence, processing, archive, and configuration, not merely missing familiar UI drawings.

## Post-review vocabulary outcome

Human semantic review of `WEBUI-16` found that the missing concept was broader than a Web/UI-specific EDIT icon. `action_change` is accepted as a Core primitive for change / transform / modify / become different. Edit, recycle, exchange, and replacement remain contextual readings. This update does not reconcile loading, save, archive, settings, IT/system, video, upload/download, notification, or permission/access.

## Limitations

- No human participants.
- No external AI/model run.
- No live UI screenshots or product flows.
- No new Context Pack.
- No changes to Pictiq vocabulary or grammar.
- Zero-training observations are analytical only.

## Publication milestone check

`IS WEB/UI STRESS TEST A PUBLICATION MILESTONE?`

Verdict: `PUBLICATION_MILESTONE_CANDIDATE`.

Suggested editorial angle: **Can 83 Visual Symbols Describe a Modern Software Interface?**

Reason: the results are balanced and explainable, with clear successes, true gaps, and a useful distinction between semantic representation and conventional UI glyphs. A later article should wait for human review of the findings and possibly a cleaner figure set.

## Artifacts

- Machine-readable results: [`web-ui-stress-test-results.json`](web-ui-stress-test-results.json).
- Rendered examples: [`rendered/`](rendered/).
- Visual QA sheet: [`web-ui-stress-test-qa.svg`](web-ui-stress-test-qa.svg).
