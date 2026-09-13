# Web/UI Pictiq Stress Test

> Source artifact: [Web/UI Pictiq Stress Test 2026-09](../../research/web-ui-stress-test-2026-09/README.md)
> Status: human semantic reconciliation complete
> Boundary: research/governance only; no Web/UI Context Pack and no new vocabulary beyond accepted `action_change`.

## Main lesson

Domain stress tests should not mechanically generate vocabulary. Human review eliminated several apparent gaps through context, polysemy, and composition.

The reconciled result keeps Pictiq small:

- loading / processing -> `time`;
- save / download -> contextual down + content;
- publish / upload -> contextual up + content;
- settings -> tools;
- empty -> no + relevant content;
- notification -> communication + attention.

The one accepted addition was `action_change`, because Web/UI EDIT pressure exposed a broader universal CHANGE / TRANSFORM / MODIFY primitive.

## Governance lesson

The review formalized **NEED-BEFORE-VOCABULARY**: existing primitive -> composition -> context -> polysemy -> intentional omission -> only then consider a new symbol. “We may need it later” is not enough.

`DEFERRED_UNTIL_NEEDED` is a planning status, not a vocabulary classification. Current deferred concepts are archive, IT/system, and video.

## Reconciled counts

- PRESERVED_EXPLICITLY: 2
- PRESERVED_BY_COMPOSITION: 10
- CONTEXT-SUFFICIENT: 11
- INTENTIONAL_OMISSION: 0
- LOSSY: 1
- GAP: 0

## Publication status

Publication milestone verdict: `PUBLICATION_MILESTONE_CANDIDATE / READY_FOR_EDITORIAL_DEVELOPMENT_AFTER_HUMAN_APPROVAL`.

Possible editorial angle: **What a Visual Language Learns When You Make It Describe Software**.

Do not publish from this note directly; preserve it as book/research material.
