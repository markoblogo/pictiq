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
