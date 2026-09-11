# AI and Machine Research Backlog

> **Status:** Research backlog  
> **Added:** 2026-09-09  
> **Source:** [Perplexity ideas harvest](perplexity-ideas-harvest-2026-09.md), [text-to-Pictiq RAG prototype](../experiments/text-to-pictiq-rag-prototype.md)

This backlog records possible research directions. It is not an implementation roadmap.

| Item | Status | Research question | Next evidence needed |
|---|---|---|---|
| Text to Pictiq baseline | PROTOTYPE | Can short natural-language input map to existing `icon_id` values through current lexicon metadata? | Keep current baseline record; add tests only when evolving implementation. |
| Semantic Text to Pictiq v2 | PLANNED | Can segmentation plus meaning-aware retrieval reduce multi-clause loss and lexical false positives? | Define dataset, structured intent shape, retrieval method, and GAP threshold. |
| Pictiq to text back-translation | PLANNED | How much meaning survives Pictiq compression? | Define round-trip test cases and independent back-translation method. |
| Machine vision tile recognition | PLANNED | Can models or classifiers identify exact canonical IDs across render and physical transformations? | Build benchmark spec before running. |
| Visual Iconicity Challenge review | DEFERRED | Is this a useful methodological reference for Pictiq visual/VLM benchmarking? | Verify source, metrics, dataset, and publication status. |
| Human-machine shared symbols | HYPOTHESIS | Can one tile be meaningfully human-readable and machine-detectable? | Compare QR/fiducial/classifier baselines and physical conditions. |
| Constrained generation | HYPOTHESIS | Can JSON Schema, function/tool calling, constrained decoding, or grammar-constrained output reduce invalid Pictiq token generation? | Build syntax validator first; measure semantic errors separately. |
| Pictiq translator tool | DEFERRED | Would CLI/library/API/MCP delivery help once translation validity is established? | Wait for a reliable translator baseline and validation suite. |
| AI input safety | HYPOTHESIS | Does validated `icon_id` input reduce selected prompt-injection or malformed-input risks in kiosks/agents? | Threat model, adversarial tests, downstream prompt analysis, comparison with constrained forms/JSON. |
| Token/bandwidth compression | HYPOTHESIS | Are Pictiq ID sequences smaller or cheaper than natural language or structured JSON for specific intents? | Measure serialized size and tokenizer cost across message sets and models. |
| Human-robot / IoT visual states | HYPOTHESIS | Can Pictiq provide a supplementary low-power visible channel for device/robot state? | Define states and compare with text, LEDs, emoji, and icons. |
| AI-to-AI auditable coordination | SPECULATIVE | Can a human-readable symbolic protocol serve as an interpretable coordination layer when auditability matters more than raw bandwidth? | Define a constrained task and compare with text, JSON, and embeddings. |
| Ontology-like concept-ID layer | OBSERVATION | Can `icon_id` plus localized metadata act as a small language-neutral concept registry? | Clarify scope; do not claim formal ontology equivalence. |

## Near-term evidence order

1. Keep the existing text-to-Pictiq baseline as the reproducible starting point.
2. Specify a grammar/phrase validator before constrained generation.
3. Build a small benchmark dataset before changing retrieval methods.
4. Treat security, token savings, and AI-to-AI claims as measured hypotheses only.


## 2026-09-10 methods connection

The [Experimental Methods Backlog](experimental-methods-backlog.md) adds two future tracks that should connect to this file rather than duplicate it: VLM recognition after the visual consistency audit, and Machine Mind comparisons across natural language, compressed natural language, Toki Pona, and Pictiq IDs. Treat Pictiq as a possible inspectable intermediate representation until evidence shows otherwise.
## 2026-09-11 machine experiment program

The [Pictiq AI Experiments harvest](pictiq-ai-experiments-harvest-2026-09.md) refines a supplied experiment catalog into five tracks: Machine Comprehension, Constrained Translation, Signaling Game, Semantic Boundary Corpus, and Machine Interface Experiments. The operational backlog now lives in [Machine Experiments Backlog](machine-experiments-backlog.md), with dedicated plans for [Pictiq Signaling Game](pictiq-signaling-game-plan.md), [Semantic Boundary Corpus](semantic-boundary-corpus-plan.md), and [AI Experiment Verification](ai-experiment-verification-backlog.md).

This update corrects older 52-icon and pre-v1.1.0 examples. Future experiments must use the current audited registry, Message Schema v0.1, Shorthand v0.1, Renderer v0.1 outputs where relevant, and semantic-slot metrics. No experiment is run or accepted as product scope by this backlog.
