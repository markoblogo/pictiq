# Pictiq AI Experiments Harvest 2026-09

> Status: critical research harvest
> Source: archived input [`pictiq-ai-tests-experiments-mvp-catalog-ru.md`](inputs/perplexity-2026-09/pictiq-ai-tests-experiments-mvp-catalog-ru.md)
> Source SHA-256: `df792c5fdd9fd0647a3fe3da87c076a631030f1b76fbd5a9dd35b8bb6da07fbc`
> Rule: this file does not implement experiments and does not change Pictiq vocabulary, grammar, icons, profiles, packs, Entity Symbols, Message Schema, Shorthand, Renderer, tags, or releases.

The supplied catalog is useful because it shifts Pictiq from “can we draw icons?” to “can humans and machines use the same small visual/symbolic protocol?” It is also older than the current repository state: it mentions 52 icons, old examples, `place_hotel`, and pre-v1.1.0 assumptions. Those examples are idea sources only and must be rebuilt from the current audited registry before execution.

## Current-state correction

Current baseline for future execution:

- Pictiq v1.1.0 architecture is closed.
- The ordinary canonical registry currently has 83 retained IDs, with active semantic concepts distinct from legacy identifiers.
- Entity Symbols are separate from ordinary vocabulary.
- Numeric Notation is separate from `qty_*` pragmatic quantity primitives.
- Pictiq Message Format v0.1 and Shorthand v0.1 define the canonical message representation and authoring syntax.
- Renderer v0.1 exists locally and can produce deterministic SVG from valid messages.
- Legacy examples such as `place_hotel` must normalize or be rebuilt from current compatibility decisions before execution.

## Proposal harvest

| Class | Original idea | Source section | Current Pictiq relevance | Dependency | Research value | Product/demo value | Risks/confounds | Recommended timing | Book/article value |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| POST_RENDERER_CANDIDATE | Zero-shot VLM icon recognition, then repeat with labels/lexicon/context. | Level 1 #1; Level 3 #11 | Strong test of visual inferability vs protocol knowledge. Must use current 83 ordinary IDs and separate Entity Symbols intentionally. | Renderer output, current registry, corpus spec, model/version logging. | High: exposes visually ambiguous icons and context dependence. | Medium/high: public benchmark/demo. | Old 52-icon framing is outdated; VLM recognition is not human comprehension. | Early after Renderer, before large public claims. | “Can AI read Pictiq?” with failure examples. |
| STRONG_EXPERIMENT | Constrained generation from natural language to valid Pictiq Message JSON. | Level 1 #2 | Directly tests the value of Message Schema v0.1 and whether RAG is still justified. | Message Schema, registry/context pack prompt variants, evaluator. | Very high: separates syntax validity from semantic usefulness. | High: future translator/API demo. | Schema-only may be valid but semantically wrong; RAG may add or reduce errors. | High-priority post-Renderer pilot. | “What is the simplest architecture that writes valid Pictiq?” |
| POST_RENDERER_CANDIDATE | Reverse reading: model reconstructs meaning from tile sequence. | Level 1 #3 | Now runnable using Renderer v0.1 visual outputs and canonical JSON. | Rendered fixtures, symbolic fixtures, semantic-slot answer key. | High: tests compression and grammar readability. | Medium: clear article examples. | Literal wording similarity is the wrong metric; use semantic slots. | Early symbolic pilot; visual condition after QA corpus. | Shows what survives Pictiq compression. |
| POST_RENDERER_CANDIDATE | Cross-model consistency. | Level 1 #4 | Useful across both generation and reconstruction. | Fixed corpus, model/provider/version logs. | High: identifies stable vs model-specific ambiguities. | Medium. | Can become a leaderboard instead of architecture evidence. | Pair with Tracks A/B, not standalone first. | Good comparative tables for Machine Mind material. |
| POST_COMPOSER_CANDIDATE | Idioms, metaphor, sarcasm, double negation. | Level 1 #5 | Belongs in semantic boundary corpus and poetry/visual prosody track. | Curated source corpus, explicit failure taxonomy, Composer for larger runs. | High: finds source ambiguity, translator failure, structural limit, or vocabulary gap. | Medium. | Easy to overclaim “Pictiq fails” when source itself is ambiguous. | Some JSON cases early; main work post-Composer. | Strong chapter on useful failures. |
| TOO_STRONG | Public web demo of old RAG prototype with feedback button. | Level 2 #6 | The old TF-IDF/RAG prototype is useful baseline evidence, not current product architecture. | Reliable translator benchmark, validation, public surface. | Medium if instrumented; low if launched as demo too early. | Medium/high later. | Would collect noisy invalid data and present outdated examples. | Defer until translator baseline and Composer/public surface. | Useful as “prototype vs evidence” case. |
| POST_COMPOSER_CANDIDATE | MCP/agent tool “Pictiq translator”. | Level 2 #7 | Useful once translation validity is established. | Renderer/API, constrained generation benchmark, validation suite. | Medium/high. | High integration value. | A tool wrapper can hide weak semantic selection. | Post-translator benchmark; not now. | Agent-tool article after evidence exists. |
| POST_RENDERER_CANDIDATE | CLIP-style physical tile classifier. | Level 2 #8 | Better framed as physical tile recognition benchmark. | Renderer SVG, print/screen transforms, physical/camera corpus. | High for human-machine shared symbols. | Medium/high for physical products. | CLIP may be wrong baseline; 52-icon count outdated. | After Renderer and physical artifact plan. | “Machine-readable vs human-readable” section. |
| POST_COMPOSER_CANDIDATE | Pictiq -> natural language -> speech. | Level 2 #9 | Accessibility/interface prototype, not proof of a full AAC system. | Renderer/message inputs, reconstruction layer, TTS, safety/usability framing. | Medium. | High demo value for travel/interface scenarios. | AAC claims require specialist/user research; hallucinated reconstruction risk. | After basic reconstruction benchmark; stronger post-Composer. | Good product demo with careful boundary. |
| LONG_TERM | Next tile predictor from `icon-index.json` examples. | Level 2 #10 | Relevant only after real Composer usage logs or curated corpora. | Corpus with real sequences, user intents, context labels. | Medium/high later. | Medium in Composer. | Current hand-written examples are too small and biased. | Long-term/post-Composer. | “Prediction without pretending to know intent.” |
| POST_RENDERER_CANDIDATE | Open benchmark of model Pictiq understanding. | Level 3 #11 | Umbrella over Track A. | Dataset, renderer, evaluator, reproducible logs. | High. | Medium/high. | Needs versioned model/date provenance because APIs change. | After small pilot proves metrics. | Publishable methods/results piece. |
| STRONG_EXPERIMENT | Two AI agents communicate only through valid Pictiq. | Level 3 #12 and dedicated section | One of the strongest Machine Mind experiments if symbolic and visual channels are separated. | Message validator, Renderer, corpus, judge, cross-model pairs. | Very high: tests interpretable constrained communication. | High demo/blog value. | Self-play/shared-model confound; invalid messages; wrong metric. | Tiny symbolic pilot post-Renderer; visual pilot after QA corpus. | Strong Machine Mind chapter. |
| VERIFICATION_REQUIRED | Prompt/token compression measurement. | Level 3 #13 | Valid research question but not a claim. Must measure JSON overhead and semantic retention. | Message corpus, tokenizer/accounting method, baseline text variants. | Medium/high. | Medium for IoT/API claims if positive. | Pictiq may be longer once JSON/schema/context overhead is counted. Negative result is valid. | Post-Renderer after corpus exists. | Good cautionary article about measured compression. |
| VERIFICATION_REQUIRED | Prompt-injection resistance test. | Level 3 #14 | Reframe as constrained-interface security, not a universal language property. | Threat model, interface definition, adversarial corpus, downstream prompt design. | Medium/high for interface safety. | Medium for kiosk/agent interfaces. | “Closed vocabulary = safe” is too strong; output prompts can still be vulnerable. | After a concrete tool/interface exists. | Useful if written as bounded security evidence. |
| OUTDATED_EXAMPLE | Scenario cards using 52 icons, `place_hotel`, and older examples. | Signaling game examples | Good methodological pattern, but not executable current fixtures. | Rebuild from current registry and Message Schema. | Medium as method seed. | Low as-is. | Importing them would reintroduce deprecated examples. | Rebuild before any pilot. | Good before/after example of archive discipline. |
| DEFER | Emergent/convention-building mode in first pilot. | Signaling game arms | Interesting control later, but can muddy the first result. | Stable baseline task, maybe non-Pictiq symbolic baseline. | Medium later. | Low early. | Conflates Pictiq comprehension with convention invention. | Not in first pilot unless the baseline is already stable. | Later comparison to emergent-language literature. |

## Five main experiment tracks

1. **Machine Comprehension Benchmark**: icon recognition, composition reading, and cross-model consistency.
2. **Constrained Translation Benchmark**: natural language -> Pictiq Message JSON under schema-only, schema+registry/context, and RAG/rule-assisted variants.
3. **Pictiq Signaling Game**: Sender/Receiver/Judge tasks over symbolic and visual channels.
4. **Semantic Boundary Corpus**: idiom, metaphor, sarcasm, double negation, indirect request, euphemism, ambiguity, and poetry.
5. **Machine Interface Experiments**: compression/cost, constrained-input security, Pictiq-to-speech, next-token assistance, and physical tile recognition.

## Highest-priority post-Renderer experiments

1. Constrained Message-Schema generation from natural language.
2. Symbolic Pictiq -> semantic-slot reconstruction.
3. Tiny Sender/Receiver symbolic pilot with a rebuilt current-registry corpus.

These should be small, versioned, and diagnostic. They should not delay Composer unless they expose a real architecture problem.

## Deferred until Composer or public surface

- crowdsourced translation challenge;
- next-token assistance;
- large human/machine comparison;
- Semantic Boundary corpus at scale;
- public RAG/translator demo;
- Pictiq -> speech demo with usability framing.

## Book connections

For `Toki Pona and the Machine Mind`, this catalog supports themes around constrained symbolic interfaces, small vocabularies vs large models, symbolic vs visual channels, and two AIs forced to communicate through a human-readable protocol.

For the main Pictiq book or later edition, it supports chapters or sections on whether AI can read Pictiq, whether AI can write valid Pictiq, where failed translations are useful, and what “machine-readable” should mean.
