# Pictiq Poetry Harvest 2026-09

> Status: research harvest / book-material seed  
> Source input: [`inputs/perplexity-2026-09/pictiq-poetry-ru.md`](inputs/perplexity-2026-09/pictiq-poetry-ru.md)  
> Source SHA-256: `f2c1987dd79c851c5e5c491bfe3f6ed48ac9dedf43ef1f85906eadc914f61118`  
> Rule: this harvest does not change Pictiq grammar, lexicon, icons, profiles, packs, notation, Entity Symbols, or release state.

## Source handling

The supplied Perplexity artifact is archived byte-for-byte as a research input. It is treated as an idea source, not an authoritative source and not an accepted Pictiq translation corpus. Examples in the source may use older vocabulary assumptions and must be rebuilt from the current audited Canonical Registry and grammar before any future experiment.

## Critical harvest matrix

| Class | Idea | Useful Pictiq-specific finding | Risk / boundary | Treatment |
|---|---|---|---|---|
| ALREADY_SUPPORTED | Pictiq can form expressive compositions through repetition, negation, quantity, relation, context, and semantic compression. | Existing grammar already supports tile sequence, adjacency, modifiers/operators, and context-sensitive interpretation. | Artistic use must not be confused with normative grammar. | Preserve as a research direction layered on existing Pictiq. |
| STRONG_CONCEPT | VISUAL PROSODY: formal poetic structure without phonetic rhyme or spoken meter. | Gives Pictiq a native artistic question: what happens when rhythm/rhyme become visual and semantic patterning? | A repeated tile is not automatically rhyme. The term is a working research label. | Record in `concepts/visual-prosody.md`. |
| STRONG_CONCEPT | Poetry as a negative test for semantic compression. | Poetry stresses connotation, ambiguity, atmosphere, rhythm, metaphor, and under-specification: exactly the properties Pictiq often compresses. | The experiment should not be framed as proving universal expressiveness. | Treat failures and lossy results as first-class findings. |
| EXPERIMENT_CANDIDATE | Original Pictiq poetry. | Creates works for Pictiq's own affordances: tile repetition, symmetry, spatial layout, compression, negation, and quantity. | Do not imitate natural-language forms too literally. | Defer until Composer exists. |
| EXPERIMENT_CANDIDATE | Translation of existing short poems/forms into Pictiq. | Boundary test for what survives, compresses, disappears, or becomes structurally incompatible. | Not a proof that Pictiq preserves poetry perfectly. | Plan a small diverse corpus; do not execute now. |
| EXPERIMENT_CANDIDATE | Fixed tile-count forms such as 5-7-5. | Useful as an Oulipo-like constraint over tiles. | 5-7-5 Pictiq tiles are not Japanese haiku meter. | Test as formal constraint only. |
| EXPERIMENT_CANDIDATE | Exact visual rhyme / category rhyme / terminal-tile repetition. | Corresponding positions can be patterned by exact tile, semantic class, visual family, or terminal tile. | These are experimental conventions, not grammar. | Include in stress-test plan. |
| EXPERIMENT_CANDIDATE | Palindromic Pictiq sequences. | Discrete visual symbols make reversible structures easy to construct and inspect. | Palindrome may become visual trick rather than meaningful poem. | Test with back-interpretation and failure notes. |
| EXPERIMENT_CANDIDATE | Spatial poem. | 2D layout can carry meaning beyond reading order. | Requires Composer/layout tooling; manual SVG assembly will be brittle. | Post-Composer track. |
| EXPERIMENT_CANDIDATE | Collaborative/renga-like sequence. | A low-friction community exercise could require each line to preserve or transform one tile/category from the previous line. | Requires clear constraints and a valid composition surface, otherwise noisy. | Future community experiment after Composer/public surface. |
| VERIFICATION_REQUIRED | ASL poetry and handshape/movement/location rhyme. | Potentially useful comparative precedent for non-phonetic formal patterning. | Do not claim icon repetition is the same phenomenon as ASL handshape rhyme. | Add to verification backlog. |
| VERIFICATION_REQUIRED | Apollinaire / Calligrammes and concrete/visual poetry. | Potentially useful precedent for spatial arrangement carrying meaning. | Historical/artistic analogy needs sourced detail before book use. | Add to verification backlog. |
| VERIFICATION_REQUIRED | Oulipo and constrained writing. | Strong analogy for finite vocabulary plus formal constraints. | Do not imply direct design ancestry or exact equivalence. | Add to verification backlog. |
| VERIFICATION_REQUIRED | Renga/linking conventions. | Useful precedent for collaborative line-linking by repeated element. | Needs source-grounded description; avoid superficial analogy. | Add to verification backlog. |
| VERIFICATION_REQUIRED | Ezra Pound / imagism / ideogram-related claims. | The source's Pound example is useful as a translation-pressure idea. | Literary-historical claims and the example translation must not be accepted without verification. | Preserve as source idea only. |
| SPECULATIVE | Pictiq chapbook / public poetry challenge. | Could become strong book/publication material after tooling exists. | Product value unknown; do not schedule before architecture/tooling sequence. | Keep as future product/content hypothesis. |
| DO_NOT_IMPORT | Poetry-specific icons or grammar rules. | None at this stage. | Would bloat vocabulary and violate the current audit discipline. | Do not add. |
| DO_NOT_IMPORT | Source-provided Pictiq sequences as accepted translations. | None at this stage. | The source may reflect older vocabulary and unvalidated interpretation. | Archive only; future experiments must rebuild from current assets. |

## Original Pictiq poetry vs translation

Original Pictiq poetry should create compositions specifically for Pictiq's own expressive affordances and constraints. It may exploit repetition, symmetry, composition, negation, quantity, spatial layout, and semantic compression.

Poetry translation is a separate boundary experiment. Existing short poetic forms can be translated into Pictiq to measure what survives and what disappears. The purpose is not to prove that Pictiq can preserve poetry perfectly. The purpose is to record `SURVIVED`, `COMPRESSED`, `INTENTIONAL_OMISSION`, `LOSSY`, `GAP`, and `UNTRANSLATABLE/STRUCTURALLY_INCOMPATIBLE` outcomes with the same discipline used in Odyssey Stress Test 03.

## Negative-test value

The value of the poetry experiment is not proving that Pictiq can express everything. It is testing what remains when poetic language is subjected to Pictiq's semantic compression.

Poetry is useful because it deliberately depends on properties that Pictiq often compresses: connotation, ambiguity, atmosphere, metaphor, sound, rhythm, grammatical nuance, and deliberate under-specification. A failed or extremely lossy translation may be the strongest result because it clarifies the boundary between practical visual protocol and literary language.

## Tooling connection

Pictiq Poetry should not interrupt the current architecture cleanup/tooling sequence. It becomes cheaper and more reproducible after the shared Renderer / Generator and Composer exist.

Conceptual stack:

Canonical Registry + Grammar + Context Packs + Entity Symbols

-> Renderer / Generator

-> Composer

-> constrained-writing tools

A future Pictiq constrained-writing assistant might accept a theme, vocabulary/profile, number of lines, tiles per line, repetition constraint, terminal-tile constraint, palindrome constraint, or semantic-category constraint, then output candidate Pictiq compositions. This harvest does not implement that assistant.

## Book value

Possible future book themes include:

- Can a language without sound have poetry?
- Visual prosody.
- What semantic compression destroys.
- What new expressive forms appear when rhyme becomes repetition.
- A language discovering its artistic constraints.

The strongest book value is double-sided: the experiment can show unexpected expressive possibilities and hard limits. That is stronger than presenting Pictiq as universally expressive.
