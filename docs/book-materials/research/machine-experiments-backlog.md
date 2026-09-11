# Machine Experiments Backlog

> Status: research planning backlog
> Source harvest: [Pictiq AI Experiments Harvest 2026-09](pictiq-ai-experiments-harvest-2026-09.md)
> Boundary: future experiments only; no experiment has been run by this document.

This backlog organizes machine-facing Pictiq work after Message Format v0.1 and Renderer v0.1. It should cross-link, not replace, the older [AI and Machine Research Backlog](ai-machine-backlog.md).

## Tracks

| Track | Priority | Timing | Core question | Dependency | Risk to avoid |
| --- | --- | --- | --- | --- | --- |
| A. Machine Comprehension Benchmark | High | Post-Renderer | Can models recognize icons and reconstruct rendered or symbolic Pictiq messages? | Current registry, Renderer output, semantic-slot answer keys. | Treating VLM recognition as proof of human comprehension. |
| B. Constrained Translation Benchmark | Highest | Post-Renderer | What is the simplest architecture that produces valid and semantically useful Pictiq Messages? | Message Schema, registry/context prompts, evaluator. | Assuming RAG or schema-only generation wins without measurement. |
| C. Pictiq Signaling Game | High | Tiny symbolic pilot post-Renderer; larger/visual later | Can independent agents coordinate through valid Pictiq Messages? | Validator, Renderer, rebuilt corpus, judge. | Self-play confound; conflating symbolic IDs with visual reading. |
| D. Semantic Boundary Corpus | Medium/high | Partial early; main track post-Composer | Where do idiom, metaphor, sarcasm, ambiguity, poetry, and indirect intent fail? | Curated corpus, Composer for scale, failure taxonomy. | Blaming Pictiq for source-language ambiguity or translator failure. |
| E. Machine Interface Experiments | Medium | Post-Renderer to long-term | When is Pictiq useful as an interface representation rather than a full language? | Tool/interface definition, corpora, physical artifacts for vision tests. | Overclaiming token savings, security, AAC, or physical recognition. |

## Track A: Machine Comprehension Benchmark

A1. Zero-shot icon recognition: show current canonical icons to multimodal models without lexical context, then with candidate labels, then with the Canonical Registry and relevant Context Pack.

A2. Composition reading: give rendered multi-token Pictiq messages and ask for semantic reconstruction. Compare symbolic JSON/ID input with visual Renderer SVG input.

A3. Cross-model consistency: compare multiple model families on the same corpus and record agreement, recurring ambiguity, and model-specific failures.

Primary metrics: semantic-slot recovery, validation errors, confusion matrix by concept/category, and context-benefit delta.

## Track B: Constrained Translation Benchmark

Input: natural language scenario. Output: Pictiq Message Format v0.1 JSON.

Compare:

- LLM + Message Schema only;
- LLM + Message Schema + Canonical Registry / relevant Context Pack;
- legacy retrieval/RAG baseline;
- later rule-assisted semantic decomposition.

Metrics: schema validity, canonical-ID validity, semantic-slot preservation, incorrect concept selection, unnecessary vocabulary, intentional-omission quality, consistency across repeated runs, and latency/cost where useful.

## Track C: Pictiq Signaling Game

See the dedicated [Pictiq Signaling Game Plan](pictiq-signaling-game-plan.md).

First pilot should be tiny and symbolic. The visual channel is a distinct condition, not a cosmetic variant.

## Track D: Semantic Boundary Corpus

See the dedicated [Semantic Boundary Corpus Plan](semantic-boundary-corpus-plan.md).

This track connects directly to [Pictiq Poetry / Visual Prosody](pictiq-poetry-stress-test-plan.md) and should classify failures across source ambiguity, translator failure, Pictiq structural limit, vocabulary gap, and intentional omission.

## Track E: Machine Interface Experiments

- Compression / communication cost: measure characters, tokenizer tokens, JSON overhead, context overhead, semantic information retained, latency, and cost. Do not assume compression.
- Constrained-input security: compare a concrete closed Pictiq input surface against unrestricted text for a defined tool. Do not claim universal prompt-injection resistance.
- Pictiq -> natural language -> speech: accessibility/travel/interface prototype, not proof of a full AAC system.
- Next-token assistance: long-term/post-Composer; use real usage logs or curated corpora, not the small hand-written examples alone.
- Physical tile recognition: compare Renderer SVG, screen, print, camera conditions, CLIP-style baselines, modern VLMs, and simple CV/fiducial approaches if relevant.

## Logging requirement

Every future machine experiment should archive:

- question and hypothesis;
- Pictiq version;
- Message Schema version;
- Renderer version;
- model/provider/version/date;
- prompts and system instructions;
- corpus and answer key;
- raw outputs;
- normalization diagnostics;
- metrics and failure categories;
- architecture, vocabulary, product, and book/article implications.

Closed model behavior changes over time. Preserve enough provenance to make later results interpretable, not necessarily exactly reproducible.
