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
## English Landing v0.1 implementation pass — 2026-09-13

Status: IMPLEMENTED LOCALLY / HUMAN ACCEPTANCE PENDING.

Scope implemented: a static English landing candidate at `docs/landing/`, leaving the existing lexicon homepage unchanged until acceptance. No Pictiq translation layer, domain configuration, vocabulary, icon, grammar, Renderer, Message Schema, Composer, or Context Pack change was made.

Actual assets used:

- Book cover: `books/handbook-v1/cover.png`, served on the landing through the existing raw GitHub asset URL for Pages compatibility.
- Free book PDF: `https://raw.githubusercontent.com/markoblogo/pictiq/main/books/handbook-v1/pictiq-handbook-v1.0.pdf`.
- Free book EPUB: `https://raw.githubusercontent.com/markoblogo/pictiq/main/books/handbook-v1/pictiq-handbook-v1.0.epub`.
- Example composition: current validated `need_water + punct_question` Renderer fixture, displayed with canonical SVG assets from `docs/lexicon/svg/`.

Actual links used:

- GitHub: `https://github.com/markoblogo/pictiq`.
- Composer: `../composer/` from the candidate route; public equivalent `https://markoblogo.github.io/pictiq/composer/`.
- Lexicon: `../` from the candidate route.
- Specification: `https://github.com/markoblogo/pictiq/tree/main/spec`.
- Publications: the two already-published Medium/Substack milestones only.

Pressure observed:

| intent | current_pictiq_expression | composition | context_dependency | problem | workaround | vocabulary_pressure | final_decision |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Explain “visual language/protocol” to a first-time visitor | None used as primary content | Not attempted in v0.1 | High: this is explanatory English copy | Current symbols are not meant to replace the conceptual landing pitch before the user understands Pictiq | Use plain English; show one authentic composition as evidence | None | No vocabulary change |
| Link to Composer / authoring | Existing interface text; possible `media_text`, `comm_speak`, `action_change` analogies are imprecise | Not attempted | Medium: web navigation makes text/action clear | Forcing a Pictiq icon would reduce clarity and accessibility | Use textual nav link “Composer ↗” | None | Defer Pictiq translation layer |
| Show a readable sample message | `need_water + punct_question` | Two-token frame | Low: the pair is legible with short context | This demonstrates Pictiq without requiring new UI vocabulary | Use canonical SVGs and explain briefly | None | Keep as authentic example |
| Represent “publications” / writing | `media_text` could be relevant but too broad for section navigation | Not attempted | Medium: section heading carries meaning | A publications icon is not required for the English landing | Use plain heading “Writing & experiments” | None | No new symbol |

Deferred issues:

- Pictiq translation layer remains a later experiment after human acceptance.
- Custom domain `pictiq.abvx.xyz` remains unconfigured.
- Archive, IT/System/Server, and Video remain deferred and unimplemented.
- Replacing the existing public homepage remains a later acceptance decision.

Human acceptance status: PENDING.

## English Landing v0.1 acceptance fix pass 1 — 2026-09-13

Status: IMPLEMENTED LOCALLY / HUMAN ACCEPTANCE PENDING.

Human acceptance result for the first local implementation: REJECTED / REQUIRES STRUCTURAL REDESIGN. The landing looked too close to the technical Lexicon/Pages surface and did not yet read as a public project landing page.

Revised implementation: `docs/landing/` remains a candidate route. The existing public lexicon homepage remains unchanged until human acceptance.

Canonical identity asset used:

- `branding/logo.svg`, copied unchanged to `docs/landing/assets/pictiq-logo.svg` for GitHub Pages/static serving. The logo remains an unframed proper-name mark, not a Pictiq tile.

Rejected v0.1 elements removed:

- search-first / Lexicon-like hierarchy;
- dark Lexicon styling and green accent assumptions;
- dashboard/card-heavy presentation;
- oversized startup-style hero;
- homepage treatment that implied the Lexicon grid was the product homepage.

Replacement structure:

1. Header with canonical Pictiq logo/symbol, conventional section navigation, GitHub link, and future `EN | Pictiq symbol` language-mode placement.
2. Hero/About with concise English positioning and book-cover visual anchor.
3. Book section with exact current handbook title and PDF/EPUB/GitHub links.
4. Composer section with a small authentic composition sample and Composer link.
5. Lexicon section explaining small-vocabulary semantics without embedding the 84-icon grid.
6. Publications section listing only the two already-published Medium/Substack milestones.
7. Footer with project links, copyright, and pre-production privacy/legal/contact note.

Actual assets and links preserved:

- Book cover: `books/handbook-v1/cover.png` via raw GitHub URL for Pages compatibility.
- Free book PDF: `https://raw.githubusercontent.com/markoblogo/pictiq/main/books/handbook-v1/pictiq-handbook-v1.0.pdf`.
- Free book EPUB: `https://raw.githubusercontent.com/markoblogo/pictiq/main/books/handbook-v1/pictiq-handbook-v1.0.epub`.
- Composer: `../composer/` locally, public equivalent `https://markoblogo.github.io/pictiq/composer/`.
- Lexicon: `../` from the candidate route.
- GitHub: `https://github.com/markoblogo/pictiq`.

Language-mode decision:

- `EN` is visible and active.
- Pictiq mode is visually represented by the canonical Pictiq logo/symbol as planned future placement only.
- No Pictiq translation layer, language dropdown, parallel DOM, or automatic translation was implemented.

Privacy/legal/domain status:

- The current static landing implementation has no accounts, forms, first-party analytics, or first-party tracking code.
- Privacy/legal/contact review remains PENDING before any custom-domain production launch.
- No `pictiq.abvx.xyz`, DNS, Pages custom domain, CNAME, redirect, tag, release, or deployment change was made.

Pressure observed during fix pass 1:

| intent | current_pictiq_expression | composition | context_dependency | problem | workaround | vocabulary_pressure | final_decision |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Represent the project name in navigation | Canonical Pictiq logo/symbol | Proper-name mark outside tile vocabulary | Low | Normal text wordmark was explicitly disallowed when canonical asset exists | Use `branding/logo.svg` asset | None | No vocabulary change |
| Prepare future EN/Pictiq language mode | Canonical Pictiq logo/symbol | UI mode marker, not translated content | High: future site state | Pictiq translation is not implemented yet | Show `EN` active and logo/symbol as planned inactive future mode | None | Translation layer deferred |
| Communicate public project sections | Plain English section labels | Not attempted | Medium | Icon-only navigation would hurt zero-training entry and accessibility | Use text navigation | None | No new UI vocabulary |
| Explain Composer without embedding Composer | `need_water + punct_question` | Two-token authentic sample | Low | Full Composer embed would dominate the landing | Show small Composer-like sample and link | None | No vocabulary change |

Deferred concepts remain unchanged:

- Archive: `DEFERRED_UNTIL_NEEDED`.
- IT/System/Server: `DEFERRED_UNTIL_NEEDED`.
- Video: `DEFERRED_UNTIL_NEEDED`.

Human acceptance status: PENDING.
