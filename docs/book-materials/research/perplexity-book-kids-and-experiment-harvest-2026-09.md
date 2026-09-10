# Perplexity Book, Kids, and Experiment Harvest — 2026-09

> Status: critical research/planning harvest  
> Inputs: [book structure](inputs/perplexity-2026-09/pictiq-book-structure-ru.md), [kids book concept](inputs/perplexity-2026-09/pictiq-kids-book-series-concept-ru.md), [topics and mini-project catalog](inputs/perplexity-2026-09/pictiq-topics-research-mini-projects-catalog-ru.md)  
> Rule: These notes are not accepted roadmap, not normative specification, and not product commitments.

## Core working principle

Future Pictiq products, publications, and tools should whenever practical also function as experiments that return evidence to the language itself. A book can test narrative composition; a browser translator can test Web semantics; a renderer can test formal grammar; a card or sticker can test Embodied use; a VLM benchmark can test machine recognizability; a translation challenge can expose vocabulary gaps.

This does not require every commercial or content artifact to become an academic study. It means substantial work should end with a recorded question, method, result, failure/ambiguity, and architectural implication. Success, failure, ambiguity, and negative results are all useful outputs.

## Harvest table

| Class | Source file | Concise idea | Current evidence in Pictiq | Relation to roadmap | Experiment value | Product/content value | Risks / assumptions | Recommended treatment |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ALREADY SUPPORTED | Book structure | Pictiq book can explain history, architecture, grammar, omission, applications, and AI future. | Handbook, protocol docs, crosswalk, road stress test, Odyssey stress test, inclusive-design archive. | Fits book-materials archive. | Low direct experiment value unless each chapter ties to a stress test. | High book value. | The proposed outline may overstate finality. | Preserve as hypothesis, not TOC. |
| STRONG DIRECTION | Book structure + catalog | Tell Pictiq as a language developed through attempts to break it. | Stress Tests 01, 02, and 03 already changed or clarified architecture. | Strong fit before Book 1. | High: makes failures part of method. | High: stronger narrative than static spec tour. | Requires honest treatment of unresolved gaps. | Use as leading Book 1 structure candidate. |
| BOOK MATERIAL | Book structure | Chapter on deliberate omissions / identity-neutral substrate. | `person_generic`, `love_heart`, Entity Symbols, Odyssey intentional omission. | Fits existing concepts archive. | Medium: can be tested through cases. | High: clear intellectual position. | Must avoid unsupported market or pedagogy claims. | Keep as book chapter material. |
| VERIFICATION REQUIRED | Book structure | Claim that no comparable systems have grammar. | Pictiq has explicit grammar; precedent research warns against broad competitive claims. | Requires comparative research. | Medium. | Tempting marketing line, unsafe now. | PECS, Blissymbolics, SignWriting, LoCoS, Lojban-adjacent systems complicate it. | Reject strong form; keep as research question only. |
| EXPERIMENT CANDIDATE | Kids concept | Staged children's learning path from single icon to compositions to narrative/comic use. | Existing canonical assets and Odyssey narrative findings. | Future kids/narrative track after audit. | High. | Medium/high future content value. | No evidence yet of child comprehension or pedagogy. | Preserve as future track, not product line. |
| VERIFICATION REQUIRED | Kids concept | Frith/logographic reading model supports Pictiq learning. | No repository verification. | Related to kids track only. | Medium if verified. | Medium book/marketing value. | Scribd-like source is insufficient; analogy may be shallow. | Mark as pedagogical analogy requiring sources. |
| EXPERIMENT CANDIDATE | Kids concept | Need emotions and routines: sleep, play, fear, joy, sadness, hug, comfort. | Current vocabulary intentionally avoids many mental/emotional open classes. | Could feed future specialized pack only through evidence. | High vocabulary-pressure test. | High for child narrative if gaps recur. | Risk of creating a kids pack from imagination. | Use Odyssey method: scene -> current Pictiq -> compression -> gap -> candidate. |
| STRONG DIRECTION | Catalog | Grammar intuition test without showing `GRAMMAR.md`. | Current grammar is internally coherent but human intuition is untested. | Good post-audit experiment. | High. | Medium article value. | Must distinguish intuitive ordering from learned convention. | Prioritize as strong future experiment. |
| EXPERIMENT CANDIDATE | Catalog | Compare photos, conventional illustrations, and Pictiq silhouettes. | Existing visual QA and precedent research. | Useful after visual audit. | High for design evidence. | High article/book visual material. | Should not be framed as Pictiq must win. | Preserve as visual-mode comparison. |
| TOOLING CANDIDATE | Catalog | Shared renderer/generator API. | Existing scripts generate cards, sheets, QA, and site assets. | Post-audit engineering direction before Composer. | High: exposes grammar/layout assumptions. | High platform value. | Fragmented renderers would create inconsistency. | Record shared renderer layer; do not implement now. |
| TOOLING CANDIDATE | Catalog | Composer / translator / MCP-like tool. | RAG prototype showed lexical retrieval failures. | After renderer and reliable translator architecture. | High if it captures failed translations. | High demo value later. | Nearest-icon retrieval is not sufficient. | Defer until semantic pipeline exists. |
| EXPERIMENT CANDIDATE | Catalog | VLM recognition benchmark. | Machine-vision planning and human-machine symbol hypothesis already exist. | After visual consistency audit. | High. | High research/publicity value. | Model leaderboard changes; recognition is not comprehension. | Defer execution; cross-link existing backlog. |
| EXPERIMENT CANDIDATE | Catalog | Crowdsourced translation challenge. | Current GitHub repo and docs can host issues; Composer does not exist. | Post-Composer. | High for real vocabulary pressure. | Medium community value. | Without Composer, friction/noise is high. | Defer until users can construct valid sequences. |
| VERIFICATION REQUIRED | Catalog | ISO 9186-inspired tests. | Current project prefers context-rich task tests over isolated guessing. | Methodology reference. | Medium/high if adapted carefully. | Medium credibility value. | Standards details and licensing/citation must be verified. | Keep as reference, not immediate priority. |
| EXPERIMENT CANDIDATE | Catalog | Specialist AAC/safety feedback. | Application-domain radar flags AAC/safety as serious domains. | Domain-specific work only. | Medium/high. | Medium credibility value. | Specialist feedback does not prove general comprehensibility. | Use for relevant packs, not global claims. |
| PREMATURE PRODUCT IDEA | Catalog | Landing pages, waitlists, merch, AR prototype. | Physical layouts exist; product demand untested. | Later product validation. | Medium if tied to real context. | Potentially high. | Could distract from architecture cleanup. | Keep as later experiments with product/research split. |
| BOOK MATERIAL | Catalog | Dev-diary topics: Toki Pona, road failures, `50 != qty_5 + qty_5`, pedestrian composition, Odyssey omission, Entity Symbols. | All have repo evidence. | Strong content pipeline. | Low/medium. | High. | Do not generate articles before choosing publication cadence. | Preserve as content candidates. |
| REJECT / DO NOT IMPORT | Kids concept + catalog | Children's series is already pedagogically validated / ready to launch. | No child testing yet. | Conflicts with evidence-first workflow. | N/A. | Premature. | Could create false education claims. | Retain as future experimental track only. |

## Strongest future research ideas

1. Grammar intuition test: intended meaning plus unordered existing tiles; participant arranges the sequence without seeing `GRAMMAR.md`.
2. Visual-mode comparison: photographs vs conventional illustrations vs abstract Pictiq silhouettes.
3. Kids/narrative staged-complexity track, treated as evidence gathering rather than accepted product line.
4. Shared renderer/generator layer before Composer and public tools.
5. Crowdsourced translation challenge after Composer, with explicit “I cannot express this” failure capture.

## Claims not accepted

- “None of Point It / Kwikpoint / ICOON / PECS has grammar.”
- “Pictiq is the first or only visual language with compositional grammar.”
- “Frith’s reading model validates Pictiq for children.”
- “Children’s-book experiments are required before the first substantial Pictiq book.”
- “Nearest-icon retrieval is enough for a Pictiq translator.”

## Book timing decision

A first substantial Pictiq book may be published before children’s-book experiments are complete. Children’s experiments can feed a revised edition, Book 2, later chapters, follow-up articles, or specialized publications. They are not a prerequisite for Book 1.
