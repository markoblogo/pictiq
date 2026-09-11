# Stress Test 04B — Human Authoring / Composer Usability Plan

> Status: future exploratory study plan
> Dependency: Composer v0.1 implementation accepted
> Boundary: this document does not run the study and does not finalize the corpus.

## Purpose

Test whether users can construct valid Pictiq messages using Composer without manual JSON, shorthand, SVG, or repository editing.

## Research question

Can a person use Composer to construct, edit, preview, and export a valid Pictiq Message for a simple intent while relying on human-facing labels, icons, palette grouping, diagnostics, and Renderer preview?

## Initial task categories

Plan approximately 10 tasks, using already understood Pictiq semantics rather than new vocabulary:

| Category | Example task shape | Notes |
| --- | --- | --- |
| Basic need | Ask for water. | `need_water + punct_question` candidate. |
| Question | Ask where something is. | Tests `punct_question` and frame order. |
| Negation | Express a simple no/forbidden message. | Avoid deprecated compounds where current composition is preferred. |
| Direction / movement | Use current relation or movement icons. | Tests palette search and semantic labels. |
| Number | Insert exact `50`. | Tests special number token, not ordinary vocabulary. |
| Contextual concept | Use `surface_wavy` or similar broad contextual icon. | Tests broad semantic gloss and context guidance. |
| Entity Symbol | Compose a small Odyssey entity message. | Requires context-aware entity palette. |
| Multi-frame | Build two short frames. | Tests frame model and preview. |
| Deprecated composition | Import or build a preferred composition instead of deprecated old concept. | Example: `place_shop + item_clothing` instead of historical `place_fashion_shopping`. |
| Edit/import | Import existing JSON or `.pictiq`, normalize legacy ID, edit, export. | Example legacy input: `need_bar` or `place_hotel`. |

Do not finalize exact task wording until the Composer implementation exists, because UI affordances will affect task difficulty.

## Candidate metrics

- task completion;
- time to first valid message;
- number of palette searches;
- wrong concept selections;
- corrections/deletions;
- diagnostics encountered;
- frame/reorder errors;
- export success;
- participant interpretation of resulting message;
- qualitative confusion.

This is exploratory. Do not present it as a formal usability benchmark until methods, participants, and corpus are fixed.

## Future research connection

Composer enables later human experiments:

- icon recognition;
- icon comprehension;
- composition comprehension;
- human Sender -> Receiver signaling;
- grammar intuition;
- crowdsourced translation;
- Poetry / Visual Prosody;
- Kids/Narrative experiments.

Composer-generated Message JSON should use the same canonical representation as AI-generated Message JSON. That enables future HUMAN AUTHORING vs AI GENERATION comparisons without changing Renderer or Message representation.
## Composer v0.1 implementation readiness note

Composer v0.1 has passed creator/software acceptance after the initial implementation, Acceptance Fix Pass 1, Acceptance Fix Pass 2, Acceptance Fix Pass 3, and manual Safari/local-HTTP use. The accepted implementation includes a compact Palette, direct-manipulation Message Workspace, tile and Frame drag/reorder, cross-Frame tile movement, contextual delete controls, bottom `+` Frame creation, compact header, visual COLOR controls, native color picker, EyeDropper where supported, HEX precision input, live Browser Renderer preview, import/export, and Browser/Python Renderer parity.

Stress Test 04B is still **not run**. The next step is to prepare the 04B experiment kit for a tiny external human-authoring pilot. Do not manufacture usability results from creator acceptance or automated tests.


## Experiment kit status

The first reproducible 04B experiment kit is prepared at [`../../research/composer-human-authoring-04b/README.md`](../../research/composer-human-authoring-04b/README.md). It fixes the initial pilot at one unscored training task, eight scored tasks, a participant script, experimenter guide, observer sheet, semantic targets, debrief questions, and a machine-readable results template.

The kit contains no participant data. Stress Test 04B remains **NOT RUN** until real participants use Composer.
