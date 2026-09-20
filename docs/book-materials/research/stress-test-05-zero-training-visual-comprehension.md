# Stress Test 05 — Zero-Training Cross-Model Visual Comprehension

> Status: **READY FOR MANUAL CROSS-MODEL EXECUTION**. No external AI calls or results are included.
> Protocol package: [docs/research/stress-test-05-zero-training-cross-model](../../research/stress-test-05-zero-training-cross-model/README.md).

## Purpose

Stress Test 05 tests the zero-training entry hypothesis with a single fixed Pictiq dialogue rendered as an image. It asks what particular contemporary consumer AI products infer before receiving a guide, then whether the same products can author and repair a constrained message after receiving the same fixed guide.

This is exploratory machine evidence. It is not a model leaderboard, a benchmark claim, a vocabulary-change gate by itself, or proof of universal human comprehension.

## Fixed conditions

- **05A Blind decoding:** one canonical four-frame image and one verbatim prompt, with no Pictiq name, guide, URL, source JSON, internal IDs, or follow-up before preserving the first response.
- **05B Guided production / transfer:** the same Pictiq Handbook v1.0 PDF is supplied in the same conversation after 05A; the model encodes a fixed travel-and-payment task using only guide resources.
- **05C Repair:** after 05B, the intended original dialogue is revealed and the model may propose a constrained repair without inventing symbols.

The initial panel is ChatGPT, Gemini, Claude, Microsoft Copilot, Mistral Vibe, and DeepSeek. Perplexity is supplementary because its consumer orchestration can make model-family attribution less clean. Record only the exact visible product/model label; do not assume backend model names.

## Canonical test artifact

The 05A source is a current-vocabulary, four-frame Message v0.1 artifact. It explicitly preserves water, question/availability, confirmation, cold, money/currency context, and card-payment question. It intentionally omits exact `3`, bottle/unit, exact price `6`, and a dedicated sale primitive because current Pictiq does not provide those distinctions cleanly. This follows Meaning-Before-Wording, Priority-First Communication, and Functional Sufficiency without changing vocabulary or grammar.

## Analysis boundaries

The prepared result schema uses semantic slots and only `CORRECT`, `APPROXIMATE`, `INFERRED_FROM_CONTEXT`, `OMITTED`, `WRONG`, and `HALLUCINATED`. It records confidence, ambiguity, dialogue/turn recovery, contamination, and repair suggestions. It does not calculate a scorecard or rank models.

New-chat/no-guide procedure reduces conversational contamination but cannot prove that a system has no web or training exposure to public Pictiq material. Results are evidence about particular systems/runs on a recorded date only.

## Publication relation

Stress Test 05 is **not** a publication milestone at preparation. Re-evaluate only after results are collected and analyzed. The existing `Can a Visual Language Explain Itself? — PUBLICATION MILESTONE READY` status remains unchanged.
