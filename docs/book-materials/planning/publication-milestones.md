# Publication Milestones

> Status: editorial planning mechanism, not an automation plan.
> Source event: Research & Deployment Policy pass, 2026-09-11.

## Definition

A publication milestone is a project event that produces at least one of:

- meaningful change in understanding;
- significant research result;
- usable new artifact;
- surprising failure;
- real deployment;
- externally interesting comparison;
- important architectural transition.

Not every commit, tag, or release is a publication milestone.

## Output check

For every significant future milestone, evaluate three possible outputs:

1. Repo artifact.
2. Public post.
3. Book material.

Potential public channels include Medium, Substack, LinkedIn, GitHub, and the project site. This document does not automate publication.

## Future-work prompt

For substantial future work, ask:

**Is this a publication milestone?**

If yes, record:

- possible headline/angle;
- evidence/artifacts;
- screenshots/figures;
- appropriate channels;
- whether publication should happen now or enter backlog.


## Milestone closure workflow

For every substantial future Pictiq result ask: **IS THIS A PUBLICATION MILESTONE?**

If yes, explicitly record:

- milestone;
- possible editorial angle;
- supporting artifacts/data;
- useful illustrations;
- Medium/Substack suitability;
- LinkedIn suitability;
- status: `CANDIDATE`, `READY`, `PUBLISHED`, or `DEFERRED`.

LinkedIn is optional unless a task explicitly requires it. Missing LinkedIn publication should not block milestone closure.

## Seed backlog

| Candidate milestone | Possible angle | Potential outputs | Status |
| --- | --- | --- | --- |
| Architecture & Vocabulary Audit | Why we made a visual language smaller instead of larger. | Repo artifact, public post, book chapter. | Candidate. |
| Odyssey Stress Test | What happens when Homer is translated into a tiny visual language? | Public post, book material, figures. | Candidate. |
| Message / Renderer | How a collection of pictograms became a machine-readable protocol. | Technical post, repo artifact, book architecture chapter. | Candidate. |
| Stress Test 04A | An AI understood the source semantics better than it could express them through a constrained visual protocol. Preserve exact limitations. | Research post, book material. | Candidate. |
| Composer v0.1 | Pictiq Can Now Be Written, Not Just Viewed. | Release `v1.2.0`, Composer public URL, screenshots/article figures, project history. Medium and Substack suitable; LinkedIn optional later. | `PUBLISHED` on Medium and Substack, 2026-09-13. Medium: https://abvcreative.medium.com/pictiq-can-now-be-written-not-just-viewed-bea970f09f00. Substack: https://abvx.substack.com/p/pictiq-can-now-be-written-not-just. |
| Browser Renderer parity | One visual protocol, two rendering runtimes, one conformance contract. | Technical post, repo artifact. | Candidate. |
| Pictiq Games / Human Communication Lab | We turned a visual language into a game to see whether people could communicate without learning it. | Article, session report, figures, book material. | Future candidate after playable prototype, first real session, surprising behavior, repeat-play evidence, or commercial prototype. |
| Web/UI Stress Test | What a Visual Language Learns When You Make It Describe Software | Human-reconciled stress-test report, machine-readable corpus/results, visual QA sheet, book material, and NEED-BEFORE-VOCABULARY rule. Medium/Substack candidate; LinkedIn optional if article exists. | `PUBLICATION_MILESTONE_CANDIDATE / READY_FOR_EDITORIAL_DEVELOPMENT_AFTER_HUMAN_APPROVAL`; do not publish directly from raw report. |
| Stress Test 05 | Can AI read a visual language it has never seen before? | Medium/Substack article, technical appendix, book material, figures. | Likely milestone when run. |
