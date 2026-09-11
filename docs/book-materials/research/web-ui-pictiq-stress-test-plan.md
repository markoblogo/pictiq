# Web/UI Pictiq Stress Test Plan

> Status: future stress-test plan
> Source event: Pictiq Research Foundations — Batch 02
> Rule: source cases are candidates, not accepted Pictiq translations or vocabulary.

## Premise

Modern web and mobile interfaces already act as partial visual languages. Meaning comes from glyph, position, container, state, interaction, neighboring controls, text, and accessibility semantics.

Preserve the key distinction: **recognizable is not actionable**. A user may name an icon but still misunderstand what will happen when they activate it.

## Candidate test families

- Back vs Close;
- Home vs physical HOME;
- Search vs Filter;
- Add vs Expand;
- Save vs Publish;
- Delete vs Archive;
- choose-one vs choose-many;
- toggle vs immediate action;
- active vs available;
- disabled vs permission-denied;
- required input vs format error;
- Loading vs Empty;
- progress/cancel;
- payment confirmation;
- price comparison basis;
- timezone/deadline;
- permission scope;
- notification priority;
- Undo vs irreversible action;
- agent action preview.

## Evaluation questions

Each case should be rebuilt later against the then-current registry and classified as existing primitive, composition, context-sufficient, lossy, gap, or future language pressure.

Record possible pressure around containment, attachment, grouping, scope, selection state, transient vs persistent state, hierarchy, relations, and typed values. Do not adopt these mechanisms until tests show current flat Message v0.1 is insufficient.

## Accessibility boundary

Visual Pictiq must not be the only semantic channel in digital UI. Future interfaces should consider accessible names, roles, states, values, keyboard operation, text/speech expansion, diagnostics, and reversible actions.

Do not claim WCAG compliance from this research plan.
