# Perplexity Ideas Harvest 2026-09

> **Status:** Research harvest  
> **Inputs:** [PDF research input](inputs/perplexity-pictiq-ideas-2026-09.pdf), [text-to-tile RAG prototype source](inputs/pictiq-text-to-tile-rag-prototype.py)  
> **Rule:** Extracted ideas are evidence, hypotheses, prototypes, or experiment candidates. They are not accepted Pictiq protocol changes.

## Superseded precedent material

The PDF contains an earlier comparison of Point It, Kwikpoint, ICOON, and related products. That material should not overwrite the later [portable visual communication precedent study](portable-visual-communication-precedents.md) or [verification matrix](portable-visual-communication-verification-matrix.md).

Specific older claims now require the verified repository wording:

| Supplied PDF claim | Current archive handling |
|---|---|
| Point It sold 2.5 million copies. | Keep as UNVERIFIED. Use only the weaker "over 2 million" claim with publisher/retail attribution. |
| Kwikpoint had universal military adoption / standard issue. | Do not use absolute wording. Current status is REPORTED/SUPPORTED only through first-party and secondary sources. |
| None of the analogues have grammar. | Use narrower wording: no published formal visual grammar was found for the tourist pointing products; PECS has a formal interaction protocol. |
| Pictiq is simply ahead because it has grammar. | Do not use superiority framing. Pictiq has distinct architecture; other systems may outperform it in adoption, specificity, validation, or distribution. |

## Extracted ideas

| Item | Class | Harvested value | Status in Pictiq |
|---|---|---|---|
| Pictiq as a constrained symbolic protocol / DSL-like representation | OBSERVATION | Stable IDs, grammar, profiles, packs, JSON metadata, and canonical SVGs make software operations possible at the `icon_id` level. | Conceptual framing only; Pictiq is not a programming language. |
| Human + machine shared symbols | HYPOTHESIS / EXPERIMENT CANDIDATE | A tile may be human-readable as a symbol and machine-detectable as a framed canonical shape resolving to `icon_id`. | Captured in [human-machine-shared-symbols](../concepts/human-machine-shared-symbols.md). |
| Text to Pictiq baseline translator | PROTOTYPE | Supplied Python implements a runnable offline TF-IDF baseline over `lexicon/icon-index.json`. | Archived as research input and documented in [text-to-pictiq-rag-prototype](../experiments/text-to-pictiq-rag-prototype.md). |
| Low-confidence fallback | OBSERVATION / PROTOTYPE | The prototype does not force a tile below threshold and records a GAP-like signal. | Strong future translator requirement; consistent with current gap philosophy. |
| Multi-clause segmentation requirement | OBSERVED FAILURE | "No card, cash only" loses a clause in one-shot composition. | Evidence for future protocol-consistency audit; no grammar change made. |
| Lexical false positive risk | OBSERVED FAILURE | "I need sunscreen" retrieved `need_bar` above threshold in the then-current 70-icon lexicon run. | Evidence that TF-IDF char n-grams are a lexical baseline, not semantic retrieval. |
| Text to Pictiq v2 | EXPERIMENT CANDIDATE | Natural language -> semantic segmentation -> structured intent -> retrieval -> composition -> validator -> phrase or GAP. | Planned idea only. |
| Pictiq to text back-translation | EXPERIMENT CANDIDATE | Evaluate how much meaning survives Pictiq compression by independent reconstruction. | Planned / not run. |
| Machine vision benchmark | EXPERIMENT CANDIDATE | Compare image-only meaning inference, image+lexicon `icon_id` matching, and canonical dataset classification. | Planned in [machine-vision-benchmark-planning](../experiments/machine-vision-benchmark-planning.md). |
| Visual Iconicity Challenge | SPECULATIVE / RESEARCH LEAD | Possible methodology source for VLM/iconicity evaluation. | Must be verified before citation in publication. |
| Constrained generation | HYPOTHESIS | JSON Schema, function/tool calling, constrained decoding, or grammar-constrained output may reduce nonexistent-token hallucination. | Syntax validity does not guarantee correct translation. |
| Pictiq translator tool | PRODUCT/SCENARIO IDEA | Possible CLI/library/API/MCP adapter for text -> Pictiq, Pictiq -> text, validation, lookup, render, and GAP reports. | Do not implement until translator validity is established. |
| AI input safety | SPECULATIVE / HYPOTHESIS | Restricting input to validated Pictiq IDs may reduce some malformed-input or prompt-injection classes. | Requires threat model and adversarial tests; no safety claim accepted. |
| Token/bandwidth compression | HYPOTHESIS | Pictiq ID sequences may serialize more compactly than natural language in some contexts. | Requires measurement across messages/tokenizers/models. |
| Human-robot / IoT display channel | PRODUCT/SCENARIO IDEA | Small e-ink/LED/device state signs: power, waiting, error, confirmation, movement, attention. | Supplementary visible channel only. |
| AI-to-AI coordination | SPECULATIVE | Human-readable symbolic layer might support auditable agent coordination when interpretability matters. | Do not claim better than embeddings or emergent languages. |
| Language-neutral concept-ID layer | OBSERVATION | `icon_id` plus localized metadata resembles a small ontology-like registry. | Do not claim equivalence to Wikidata or a formal ontology. |

## Most useful new material

The strongest new contribution is not the older precedent comparison. It is the combination of:

1. A runnable text-to-Pictiq baseline.
2. Two observed prototype failures.
3. A clearer software framing: Pictiq can be treated computationally as a constrained symbolic protocol where software acts on IDs rather than image pixels.
4. A future evaluation direction: back-translation and machine-vision benchmarks.

## Not accepted

- No AI roadmap is accepted.
- No MCP tool is prioritized.
- No protocol grammar changed.
- No canonical icons, IDs, packs, or profiles changed.
- No commercial product hypothesis is treated as market proof.
