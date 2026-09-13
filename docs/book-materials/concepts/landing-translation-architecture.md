# Pictiq Landing Translation Architecture v0.1

> Status: methodology for future implementation. No translation layer is implemented here.
> Source event: English Landing v0.1 creator acceptance, 2026-09-13.
> Source baseline: `ENGLISH_SOURCE_BASELINE_V0_1`.

## Baseline status

`Pictiq English Landing v0.1 — CREATOR ACCEPTANCE PASSED`.

This accepts the English landing as the semantic/source baseline for future Pictiq-mode work. It is not a production custom-domain launch, not Pictiq translation-layer acceptance, and not formal external usability evidence.

Accepted source structure:

1. Header.
2. Hero / About.
3. Book.
4. Composer.
5. Lexicon.
6. Publications.
7. Footer.

Minor English copy/style fixes may still happen, but future Pictiq translation work should not silently rewrite the English source merely to make translation easier.

## Research question

Primary question: **Can Pictiq explain Pictiq?**

Secondary questions:

- What page meanings survive compositionally?
- What depends on context?
- What can be intentionally omitted?
- What requires text fallback?
- What produces genuine vocabulary pressure?
- Can a visitor navigate without first learning Pictiq?

## Translation layers

Every future translation decision should pass through four layers:

A. **Source content** — the accepted English semantic meaning.

B. **Semantic intent** — language-independent intent to preserve.

C. **Pictiq representation** — current canonical Pictiq Message, symbols, frames, composition, or accepted omission.

D. **Rendered UI** — how that representation appears in the landing page.

Do not translate English strings directly into icons without first defining semantic intent.

## Block-by-block order

Future translation should proceed by page block, not by bulk conversion:

1. Header/navigation.
2. Hero statement.
3. Short project description.
4. Book section.
5. Composer section.
6. Lexicon section.
7. Publications section.
8. Footer.

For each block: freeze English meaning, define semantic target, attempt current Pictiq, classify result, review pressure, then integrate only after human review.

## Translation-unit model

Use these unit types as needed:

- `NAV_LABEL`
- `HEADLINE`
- `SHORT_SENTENCE`
- `CTA`
- `STATISTIC`
- `SECTION_TITLE`
- `PARAGRAPH_SUMMARY`
- `PUBLICATION_TITLE`
- `LEGAL_UTILITY_TEXT`

Not all units need the same treatment. Navigation can be compact. Body text can be compressed or summarized. Publication titles and legal/footer text may remain textual metadata with optional Pictiq semantic markers.

## Pressure-log schema

For every attempted translated unit, record:

| Field | Meaning |
| --- | --- |
| `unit_id` | Stable page/block/unit id. |
| `english_source` | Accepted English source text or UI label. |
| `semantic_intent` | Meaning to preserve before selecting icons. |
| `required_slots` | Meanings that must survive. |
| `optional_slots` | Details that may be omitted or moved to text. |
| `pictiq_candidate` | Candidate Message JSON, shorthand, or composition note. |
| `token_count` | Number of Pictiq tokens. |
| `frame_count` | Number of frames. |
| `context_dependency` | LOW / MEDIUM / HIGH. |
| `polysemy_used` | Which broad meanings carry the unit. |
| `intentional_omission` | What is omitted and why. |
| `text_fallback_required` | NONE / ACCESSIBILITY_ONLY / VISIBLE_TEXT / REQUIRED. |
| `compression_classification` | Semantic preservation class. |
| `practical_outcome` | UI-fit class. |
| `zero_training_observation` | Cautious first-encounter judgment. |
| `vocabulary_pressure` | NONE / WEAK / CANDIDATE / BLOCKED. |
| `final_decision` | ACCEPT / REVISE / TEXT_FALLBACK / DEFER / GAP. |
| `notes` | Reviewer notes. |

## Classification model

Semantic-compression classes:

- `PRESERVED_EXPLICITLY`
- `PRESERVED_BY_COMPOSITION`
- `CONTEXT_SUFFICIENT`
- `INTENTIONAL_OMISSION`
- `LOSSY`
- `GAP`

Practical UI outcomes:

- `WORKS_AS_IS`
- `WORKS_WITH_COMPOSITION`
- `WORKS_ONLY_WITH_STRONG_CONTEXT`
- `AMBIGUOUS`
- `POOR_FIT`
- `TEXT_FALLBACK_REQUIRED`
- `GAP`

Zero-training observations are analytical only, not human evidence:

- `LIKELY_TRANSPARENT`
- `CONTEXT_DEPENDENT`
- `LEARNED_CONVENTION_LIKELY_REQUIRED`
- `UNCLEAR`

## NEED-BEFORE-VOCABULARY gate

For every apparent missing concept, ask:

1. Can an existing primitive express it?
2. Can composition express it?
3. Can page/context disambiguate it?
4. Can accepted polysemy express it?
5. Can the detail be intentionally omitted?
6. Can English text fallback handle it?
7. Is the distinction actually necessary for this landing?
8. Only then record a vocabulary-pressure candidate.

A translation problem does not automatically justify a new icon.

## Text fallback policy

English text may remain when precision, accessibility, or identity requires it. Likely fallback cases:

- publication titles;
- author name;
- PDF / EPUB labels;
- URLs;
- copyright;
- legal/privacy/contact text;
- exact version numbers;
- exact technical metadata;
- proper names where Entity Symbol support is not appropriate.

The future Pictiq mode is a semantic translation, not a text-free purity exercise.

## Navigation and EN / PICTIQ switch

The accepted header language presentation is:

`EN | [PICTIQ SYMBOL]`

Future behavior:

- `EN` activates the English semantic presentation.
- The canonical Pictiq logo/symbol activates the Pictiq presentation.
- Route/state should be deterministic.
- Switching should preserve current page position where practical.
- No dropdown.
- No machine-language label is required for the Pictiq option.

Do not implement switching until at least Header/Hero translation has passed human review.

## Pictiq logo boundary

The canonical Pictiq logo is a special proper-name mark and is not a tile. It is not evidence that arbitrary ordinary words can be rendered as custom marks. Do not generalize the logo rule into vocabulary behavior.

## Accessibility policy

Pictiq mode must preserve:

- semantic HTML;
- keyboard navigation;
- focus states;
- accessible labels;
- screen-reader text alternatives;
- explicit destination labels for links;
- visible English fallback where exactness matters.

Visible Pictiq can differ from accessibility text. Icon-only output is not sufficient accessibility.

## Publication titles and footer/legal

Publication titles should not be forced into literal Pictiq translation. Future treatments to test:

- keep English title;
- add Pictiq semantic summary;
- add Pictiq category/meaning marker.

Footer/legal/privacy/contact content should preserve exact wording textually. Pictiq-only legal language is out of scope.

## Future implementation approaches

### Option A — Same DOM / alternate rendered representation

A shared semantic content model drives one DOM. CSS/JS swaps visible English blocks and Pictiq renderings inside the same semantic sections.

Pros: lower duplication, simpler accessibility, deterministic static Pages implementation, less content drift.

Cons: requires careful per-block data structure and reviewer discipline; complex blocks may become harder to read in source HTML.

### Option B — Parallel English and Pictiq render trees from shared data

A shared data file defines source content and Pictiq candidates; the page renders separate English and Pictiq block trees.

Pros: clearer visual separation, easier side-by-side QA, easier block experiments.

Cons: higher duplication risk, more ways for accessibility and link behavior to drift, more tooling required.

Recommendation: begin with **Option A** for Header/Hero because the page is static, link behavior must remain explicit, and avoiding content drift matters more than presentation separation. If later blocks require side-by-side research views, add a review-only artifact rather than changing the public architecture first.

## AI translation status

No automatic LLM translation is implemented. First translation should be human-reviewed, semantic, block-by-block, and constrained to current vocabulary.

A later experiment may compare:

English source -> human Pictiq translation

against:

English source -> model Pictiq translation

Compare semantic preservation, composition cost, vocabulary pressure, clarity, and model-specific additions.

## Immediate roadmap

1. English Landing v0.1 — CREATOR ACCEPTANCE PASSED.
2. EN -> PICTIQ translation architecture/methodology — CURRENT TASK.
3. Translate Header/Hero first.
4. Human review.
5. Translate next block.
6. Continue block-by-block.
7. Integrate EN | PICTIQ switch.
8. Full responsive/accessibility QA.
9. Production/legal/privacy review.
10. Configure `pictiq.abvx.xyz`.
11. Public launch.
12. Observe real use / feedback.

## Publication milestone

Pictiq landing translation/deployment is currently `PUBLICATION MILESTONE CANDIDATE`, not READY.

Possible future angle: `Can a Visual Language Explain Itself?`

Promote only after the Pictiq version produces substantive translation results.

## Deferred vocabulary

These remain `DEFERRED_UNTIL_NEEDED`:

- Archive.
- IT / System / Server.
- Video.

The landing translation may create real need later. Until then, do not implement them.
