# Pictiq Tooling Architecture

> Status: post-audit engineering direction  
> Source harvest: [Perplexity book/kids/experiment harvest](../research/perplexity-book-kids-and-experiment-harvest-2026-09.md)  
> Rule: No API or tool is implemented by this note.

## Direction

Do not build each future surface with independent rendering logic. Prefer one shared renderer/generator layer that consumes the same canonical data and serves Composer, website, books, physical layouts, AI tools, and browser/site translation experiments.

## Conceptual stack

Canonical Registry + Vocabulary Classification + Context Packs + Grammar / Composition + Entity Symbols + Parametric Notation

-> Renderer / Generator API

-> Composer

-> Website / Browser translator / Books / Physical layouts / AI tools

## Possible API input

- Ordered ordinary icon IDs.
- Entity Symbol IDs.
- Context/profile selection.
- Parametric values such as numbers and future color parameters.
- Layout/output options: tile size, grid, phrase line, card, poster, PDF region.

## Possible output

- SVG.
- PNG.
- PDF/layout data.
- Validation report: invalid ID, missing asset, profile violation, unknown entity, unsupported parametric value, or semantic GAP marker.

## Translator lesson

The previous text-to-Pictiq RAG prototype showed that nearest-icon retrieval is not sufficient. A serious translator should likely follow:

natural language -> semantic decomposition -> omission decision -> Pictiq concepts -> composition -> context pack -> rendering -> back-interpretation / validation.

Cross-links: [text-to-Pictiq prototype](../experiments/text-to-pictiq-rag-prototype.md), [AI and machine backlog](../research/ai-machine-backlog.md), [human-machine shared symbols](human-machine-shared-symbols.md), [experimental methods backlog](../research/experimental-methods-backlog.md).
