# Experimental Methods Backlog

> Status: methods backlog  
> Source harvest: [Perplexity book/kids/experiment harvest](perplexity-book-kids-and-experiment-harvest-2026-09.md)  
> Rule: Methods are future options. They do not override the current preference for context-rich task testing.

Every substantial experiment should record both product value and research value. A project can be commercially useful but weak as evidence, or scientifically useful but not immediately monetizable. At this stage, prefer experiments that also improve Pictiq architecture.

| Method | Status | Core question | Product value | Research value | Timing / dependency | Boundary |
| --- | --- | --- | --- | --- | --- | --- |
| Grammar intuition test | STRONG FUTURE EXPERIMENT | Given an intended meaning plus unordered existing tiles, do people arrange a natural sequence without seeing `GRAMMAR.md`? | Medium: article/demo. | High: tests whether composition is intuitive or only internally familiar. | After Architecture & Vocabulary Audit. | Does not prove full language comprehension. |
| Visual-mode comparison | EXPERIMENT CANDIDATE | How do photos, conventional illustrations, and abstract Pictiq silhouettes differ for recognition, ambiguity, speed, composability, precision, and small-size readability? | High: strong visual article/book material. | High: informs icon design and visual QA. | After visual audit. | Do not frame as a contest Pictiq must win. |
| VLM recognition benchmark | DEFER UNTIL AFTER VISUAL CONSISTENCY AUDIT | Can multimodal models identify canonical IDs zero-shot, with candidate meanings, with full lexicon context, and in compositions? | Medium/high: public benchmark. | High: machine-readability evidence and redesign candidates. | After visual audit and benchmark spec. | Recognition is not semantic comprehension. |
| Crowdsourced translation challenge | POST-COMPOSER EXPERIMENT | Given a target phrase/scenario, can users construct Pictiq or explicitly report “I cannot express this”? | Medium: community engagement. | High: real vocabulary/grammar pressure. | After Composer exists. | GitHub Issues alone may produce noisy invalid sequences. |
| ISO 9186-inspired comprehension work | FUTURE METHODOLOGY REFERENCE | Which ISO-style judged comprehensibility/comprehension methods can be adapted without losing context-rich testing? | Medium credibility value. | Medium/high if adapted. | Not immediate priority. | Do not silently reverse the project’s task-based testing preference. |
| Specialist feedback | DOMAIN-SPECIFIC FUTURE METHOD | What do AAC, safety, education, logistics, or other specialists see in a specific domain pack/use case? | Medium credibility/product fit. | Medium/high for domains. | When a concrete domain pack exists. | Specialist interviews are not proof of general comprehensibility. |
| Physical-format experiments | FUTURE EMBODIED EXPERIMENTS | How do cards, stickers, posters, shirts, lighters/wrappers, emergency cards, service cards, and travel cards work in real environments? | Medium/high. | High for Embodied mode. | After cleaned assets and selected use case. | Do not start merchandise production from this backlog alone. |
| Human-machine / Machine Mind experiments | FUTURE RESEARCH TRACK | Does Pictiq work best as final user language, inspectable intermediate representation, or both? | Medium. | High. | After renderer/composer and datasets. | Do not assume Pictiq beats natural language. |
| Pictiq Poetry / Visual Prosody | POST-COMPOSER RESEARCH TRACK | What survives when poetic language is subjected to Pictiq semantic compression, and what native formal conventions emerge without sound? | Medium/high: strong essay/book/demo material if failures are reported honestly. | High: tests expressivity under ambiguity and formal constraint. | After Renderer / Generator and Composer. | Do not add poetry-specific grammar or icons; negative results are first-class. |

## Tiny Language Protocol × Pictiq

Experiment/book direction only:

Natural language -> Toki Pona reduction -> Lojban structural clarification -> Pictiq semantic externalization -> reconstructed natural language.

Conceptual frame: Reduce -> Structure -> Visualize -> Reconstruct.

Do not claim this works until tested.

## Machine Mind × Pictiq

Potential comparison:

- natural-language instruction;
- compressed natural language;
- Toki Pona;
- Pictiq IDs.

Possible measures: token count, semantic preservation, ambiguity, deterministic parsing, reconstruction quality, cross-model consistency. A useful result may be that Pictiq works better as an inspectable intermediate representation, not as a replacement for natural language.

## Pictiq Poetry / Visual Prosody

Experiment/book direction only: test original Pictiq compositions and translations of short poetic forms after Composer exists. Compare SOURCE -> PICTIQ -> BACK-INTERPRETATION, recording `SURVIVED`, `COMPRESSED`, `INTENTIONAL_OMISSION`, `LOSSY`, `GAP`, and `UNTRANSLATABLE/STRUCTURALLY_INCOMPATIBLE`. Do not treat repeated tiles as automatic rhyme, and do not claim that tile-count forms reproduce natural-language meter.

## Post-Renderer machine experiment program

The [Machine Experiments Backlog](machine-experiments-backlog.md) turns the earlier Machine Mind row into five concrete research tracks after Renderer v0.1: Machine Comprehension, Constrained Translation, Signaling Game, Semantic Boundary Corpus, and Machine Interface Experiments. Early pilots may test constrained JSON generation, symbolic reconstruction, and a tiny signaling game; broad public/human/composer-dependent work remains post-Composer.
