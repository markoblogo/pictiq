# Pictiq Landing Page Deployment / Stress Test Plan

> Status: NEXT planning artifact. Do not implement in this pass.
> Source: Web/UI publication pass and human semantic reconciliation, 2026-09-13.
> Vocabulary boundary: current 84 ordinary canonical primitives, 11 Entity Symbols, no new Web/UI vocabulary.

## Research question

Can a simple useful landing page be represented and navigated using current Pictiq without pre-building a Web/UI vocabulary?

Secondary questions:

- Which existing primitives work naturally?
- Which meanings require composition?
- Which depend strongly on web context?
- Which concepts can be omitted?
- Which apparent gaps disappear during actual implementation?
- Does any concrete requirement genuinely justify new vocabulary?

## Principle

The next Web/UI work should test Pictiq against a concrete artifact: a simple landing page. It should not be another abstract vocabulary corpus. This operationalizes [NEED-BEFORE-VOCABULARY](../../../spec/VOCABULARY_GOVERNANCE.md).

Current vocabulary is frozen for the first pass:

- 84 ordinary canonical primitives;
- 11 Entity Symbols;
- no Archive icon;
- no IT/System/Server icon;
- no Video icon;
- no new navigation icons;
- no Web/UI Context Pack.

`action_change` is the only Core primitive produced by the Web/UI Stress Test cycle. Use it only where semantically appropriate; do not force it into the page as a demo.

## NEED-BEFORE-VOCABULARY gate

If a missing concept appears during implementation:

1. Can an existing primitive express it?
2. Can composition express it?
3. Can interface context disambiguate it?
4. Can accepted polysemy express it?
5. Can the information be intentionally omitted?
6. Is the distinction actually required for the landing page?
7. Only then record a vocabulary-pressure candidate.

Do not add a symbol during the same step in which pressure is first observed. Pressure must be reviewed separately.

## Deliberately simple scope

The landing page should contain enough real interface semantics to create pressure, but should not become a full website project. Potential sections/functions:

- identity/title;
- short explanation;
- visual example;
- primary action;
- secondary action;
- navigation;
- information/help;
- external/project link;
- Composer link;
- download/export/resource action only where genuinely useful.

Do not force features merely to exercise vocabulary.

## Two language layers

Distinguish content language from interface language.

Content language: what the page says about Pictiq.

Interface language: how the user navigates or acts.

A concept may be difficult as page content but unnecessary as a UI control, or vice versa.

## Conditions to preserve

Plan at least two possible conditions:

A. **Pictiq-heavy** — Pictiq carries substantial interface/content meaning with minimal textual support.

B. **Pictiq + text fallback** — Pictiq provides the visual semantic layer while text remains available for precision and accessibility.

The first implementation may choose one condition, but preserve the comparison as research material.

## Zero-training boundary

The page should be consistent with the [Zero-Training Entry Principle](../concepts/zero-training-entry.md). A visitor should not need to study Pictiq before interacting with the page. Do not use internal IDs as user-facing labels. Do not require knowledge of formal grammar.

## Accessibility boundary

Do not treat icon-only UI as inherently accessible. Preserve appropriate text alternatives, semantic HTML, labels, keyboard access, and fallback information. Pictiq is an additional visual semantic layer, not a reason to remove accessibility information.

## Pressure-log format

For every meaningful UI/content decision record:

| Field | Meaning |
| --- | --- |
| `intent` | What the page needs to communicate or let the user do. |
| `current_pictiq_expression` | Existing primitive(s) used. |
| `composition` | How tokens combine. |
| `context_dependency` | What the web/page context supplies. |
| `token_cost` | Number of tokens/tiles. |
| `zero_training_observation` | Likely first-encounter readability. |
| `problem` | Ambiguity, overload, or failure. |
| `workaround` | Text fallback, layout, omission, composition, or context. |
| `vocabulary_pressure` | None / weak / candidate / blocked. |
| `final_decision` | Use as-is, compose, omit, defer, or review separately. |

Use statuses compatible with the existing semantic-compression framework: `PRESERVED_EXPLICITLY`, `PRESERVED_BY_COMPOSITION`, `CONTEXT-SUFFICIENT`, `INTENTIONAL_OMISSION`, `LOSSY`, and `GAP`.

## Deferred concepts

These remain `DEFERRED_UNTIL_NEEDED`:

- Archive.
- IT/System/Server.
- Video.

For video, a future visual direction may be a simple conventional video-camera symbol, but no canonical icon should exist until a concrete use requires it.

## Expected artifacts from the future experiment

- Working landing-page prototype.
- Pressure log.
- Screenshots.
- Representative Pictiq compositions.
- Book-material note.
- Potential public demo.

This planning pass does not implement these artifacts.

## Publication relation

The landing-page experiment may become a later publication milestone candidate only if it produces a substantive result. It may strengthen the existing Web/UI article, become a separate later story, or simply become supporting evidence. Decide after results exist.

## Linked references

- [Web/UI Stress Test](../../../docs/research/web-ui-stress-test-2026-09/README.md)
- [Vocabulary Governance](../../../spec/VOCABULARY_GOVERNANCE.md)
- [Zero-Training Entry Principle](../concepts/zero-training-entry.md)
- [Deployment Roadmap](../planning/deployment-roadmap.md)
- [Publication Milestones](../planning/publication-milestones.md)
