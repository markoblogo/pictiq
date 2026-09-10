# Pictiq Poetry Stress Test Plan

> Status: future research plan  
> Track: POST-COMPOSER RESEARCH TRACK  
> Source harvest: [Pictiq Poetry Harvest 2026-09](pictiq-poetry-harvest-2026-09.md)  
> Rule: do not execute this plan until the shared Renderer / Generator and Composer make composition reproducible.

## Purpose

Test expressivity under ambiguity and formal constraint. Poetry is deliberately difficult for Pictiq because it often depends on connotation, atmosphere, sound, rhythm, metaphor, grammar nuance, and under-specification. Negative results are valid results.

## Experiment workflow

question -> corpus/formal constraint -> Pictiq attempt -> artifacts -> back-interpretation -> failures -> findings -> architectural implications -> book/publication material

Each experiment should record:

- source or theme;
- selected vocabulary/profile/context;
- formal constraint;
- Pictiq composition;
- rendered artifact;
- back-interpretation;
- what survived;
- what compressed;
- what was intentionally omitted;
- what became lossy, gap-like, or structurally incompatible;
- vocabulary, grammar, tooling, and book implications.

## Original Pictiq corpus

Plan a small corpus of native Pictiq works after Composer exists:

- 8-10 short Pictiq poems;
- one palindrome;
- one spatial composition;
- one longer sonnet-like experiment.

The purpose is to discover native Pictiq artistic conventions rather than force natural-language poetry onto Pictiq.

## Translation corpus

Plan a separate small corpus of about 5-10 short works/forms selected for different pressures:

- imagist poem;
- haiku;
- epigram;
- aphoristic poem;
- highly metaphorical lyric;
- concrete/visual poem;
- short formal/rhymed poem.

For each case compare:

SOURCE -> PICTIQ -> BACK-INTERPRETATION

Use outcome labels:

- `SURVIVED`
- `COMPRESSED`
- `INTENTIONAL_OMISSION`
- `LOSSY`
- `GAP`
- `UNTRANSLATABLE/STRUCTURALLY_INCOMPATIBLE`

## Formal experiment candidates

### Tile-count form

Fixed number of tiles per line. A 5-7-5 structure may be tested as an Oulipo-like constraint. Do not claim that 5-7-5 Pictiq tiles equal Japanese haiku meter.

### Exact visual rhyme

The same tile appears at structurally corresponding positions, such as the end of multiple lines. Treat this as an experimental convention, not grammar.

### Category rhyme

Different tiles from the same semantic or visual category appear in corresponding positions. This may create a weak formal echo without exact repetition.

### Visual pulse

Alternate content tiles and operator/relation tiles to create a repeated visual or semantic beat.

### Palindrome

Create a tile sequence symmetrical in reading order. Test whether the symmetry adds meaning or only decorative structure.

### Spatial poem

Use 2D arrangement as part of interpretation. This requires layout tooling because manual SVG assembly would make comparisons hard to reproduce.

### Sonnet-like constraint

Fourteen Pictiq lines/compositions with repeated structural patterns and a visual or semantic turn. Do not claim equivalence to traditional sonnet prosody.

### Collaborative/renga-like experiment

Each participant adds a Pictiq line while preserving or transforming at least one tile, category, or structural element from the previous line. This could become a future community experiment once the public composition surface exists.

## Tooling dependency

This track comes after:

1. Architecture & Vocabulary Audit.
2. Architecture release.
3. Shared Renderer / Generator layer.
4. Composer.
5. Public usable Pictiq surface.

Composer makes it possible to construct, render, revise, and compare many formal Pictiq compositions without manually assembling SVGs.
