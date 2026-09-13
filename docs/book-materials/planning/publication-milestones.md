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

## Status model

Publication significance and publication timing are separate.

Significance status:

- `CANDIDATE` — may become an article/post after more review or stronger framing.
- `READY` — substantial enough for public editorial work.
- `NOT_PUBLICATION_WORTHY` — useful internally but not a distinct public story.

Editorial status:

- `BACKLOG` — keep as a publishable story, but do not publish now.
- `SCHEDULED` — assigned to a future publication window.
- `PUBLISHED` — already published.
- `DEFERRED` — intentionally postponed.

A result becoming `PUBLICATION MILESTONE: READY` does not mean it must be published immediately.

## Default editorial cadence

Pictiq milestone posts should normally be published no more frequently than once per 7 days.

Purpose: avoid spamming the audience, give each substantial result time to circulate, maintain editorial quality, prevent rapid project progress from producing excessive public posting, and allow several READY milestones to accumulate in a publication backlog.

This is a default editorial cadence, not an absolute prohibition. Exceptions may be made for genuinely time-sensitive developments, external events, major releases, or publication opportunities where delay would materially reduce relevance. Do not automatically schedule anything.

Medium + Substack versions of the same milestone count as one publication event for cadence purposes. Optional LinkedIn adaptation of the same milestone also belongs to the same publication event, not a separate weekly slot. The cadence applies to distinct substantive Pictiq stories or milestones.

## Future publication signal

At closure of every substantial future milestone explicitly report:

`PUBLICATION MILESTONE: <status>`

If the significance status is `READY`, also record: editorial angle, supporting artifacts, useful illustrations, Medium/Substack suitability, LinkedIn suitability, earliest sensible publication window based on cadence, and whether it should outrank existing backlog items. Do not automatically publish.

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

## Ordered publication backlog / chronology

| # | Milestone | Significance status | Editorial status | Public title / angle | Channels / notes |
| ---: | --- | --- | --- | --- | --- |
| 01 | Pictiq Public Introduction | READY | PUBLISHED | `I Built a Tiny Visual Protocol for When Words Are Too Much` | Medium + Substack. Substack: https://abvx.substack.com/p/i-built-a-tiny-visual-protocol-for. Medium: https://abvcreative.medium.com/i-built-a-tiny-visual-protocol-for-when-words-are-too-much-9c86ac61bd73. |
| 02 | Composer / Public Authoring | READY | PUBLISHED | `Pictiq Can Now Be Written, Not Just Viewed` | Medium + Substack. Medium: https://abvcreative.medium.com/pictiq-can-now-be-written-not-just-viewed-bea970f09f00. Substack: https://abvx.substack.com/p/pictiq-can-now-be-written-not-just. |
| 03 | Web/UI Stress Test | READY | BACKLOG | `What a Visual Language Learns When You Make It Describe Software` or `Can 84 Visual Symbols Describe a Modern Software Interface?` | Human-reconciled report, machine-readable corpus/results, visual QA sheet, NEED-BEFORE-VOCABULARY rule. Do not publish now merely because it is READY. |
| 04 | Pictiq Landing Translation / Deployment | CANDIDATE | BACKLOG | `Can a Visual Language Explain Itself?` | Candidate only until the Pictiq version produces substantive translation results. English Landing v0.1 is creator-accepted as `ENGLISH_SOURCE_BASELINE_V0_1`; no public article yet. |

The public-introduction article is a completed historical publication milestone. It is not treated here as new research evidence and does not retroactively change project conclusions.

## Seed backlog

| Candidate milestone | Possible angle | Potential outputs | Status |
| --- | --- | --- | --- |
| Pictiq Public Introduction | I Built a Tiny Visual Protocol for When Words Are Too Much. | Historical public introduction article. Medium and Substack publication records only; article contents are not copied into the repository. | `PUBLISHED` on Medium and Substack. Substack: https://abvx.substack.com/p/i-built-a-tiny-visual-protocol-for. Medium: https://abvcreative.medium.com/i-built-a-tiny-visual-protocol-for-when-words-are-too-much-9c86ac61bd73. |
| Architecture & Vocabulary Audit | Why we made a visual language smaller instead of larger. | Repo artifact, public post, book chapter. | Candidate. |
| Odyssey Stress Test | What happens when Homer is translated into a tiny visual language? | Public post, book material, figures. | Candidate. |
| Message / Renderer | How a collection of pictograms became a machine-readable protocol. | Technical post, repo artifact, book architecture chapter. | Candidate. |
| Stress Test 04A | An AI understood the source semantics better than it could express them through a constrained visual protocol. Preserve exact limitations. | Research post, book material. | Candidate. |
| Composer v0.1 | Pictiq Can Now Be Written, Not Just Viewed. | Release `v1.2.0`, Composer public URL, screenshots/article figures, project history. Medium and Substack suitable; LinkedIn optional later. | `PUBLISHED` on Medium and Substack, 2026-09-13. Medium: https://abvcreative.medium.com/pictiq-can-now-be-written-not-just-viewed-bea970f09f00. Substack: https://abvx.substack.com/p/pictiq-can-now-be-written-not-just. |
| Browser Renderer parity | One visual protocol, two rendering runtimes, one conformance contract. | Technical post, repo artifact. | Candidate. |
| Pictiq Games / Human Communication Lab | We turned a visual language into a game to see whether people could communicate without learning it. | Article, session report, figures, book material. | Future candidate after playable prototype, first real session, surprising behavior, repeat-play evidence, or commercial prototype. |
| Web/UI Stress Test | What a Visual Language Learns When You Make It Describe Software | Human-reconciled stress-test report, machine-readable corpus/results, visual QA sheet, book material, and NEED-BEFORE-VOCABULARY rule. Medium/Substack suitable; LinkedIn optional if article exists. | Significance `READY`; editorial `BACKLOG`. Do not publish now merely because it is ready. |
| Landing translation / deployment | Can a Visual Language Explain Itself? | Accepted English baseline, future block-by-block Pictiq translation, pressure log, before/after site screenshots, vocabulary-pressure findings. | `CANDIDATE`; not READY until the Pictiq version produces substantive results. |
| Stress Test 05 | Can AI read a visual language it has never seen before? | Medium/Substack article, technical appendix, book material, figures. | Likely milestone when run. |
