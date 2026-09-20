# Stress Test 05 — Zero-Training Cross-Model Visual Comprehension

**Status:** `READY FOR MANUAL CROSS-MODEL EXECUTION` — no external AI run has been made.

This is an exploratory, date-bound protocol. It tests whether particular contemporary consumer AI products can make useful inferences from one unfamiliar Pictiq dialogue image. It is not a benchmark, a model leaderboard, evidence of universal human comprehension, or evidence that any product has a stable underlying model family.

## Fixed 05A artifact

- [Canonical Message JSON](05a-canonical-dialogue.json)
- [Normalized Message JSON](05a-canonical-dialogue.normalized.json)
- [Renderer output](05a-renderer-output.svg)
- [Blind-test PNG](05a-blind-test.png) — the only image supplied in 05A
- [Blind prompt](prompts/05a-blind-decoding.txt)

The PNG uses the fixed canonical Renderer layout and current canonical SVG assets. It has no visible Pictiq name, English text, IDs, glosses, guide, or branding. Do not upload the SVG or JSON in the blind condition.

### Intended dialogue and canonical representation

| Turn | Intended meaning | Canonical sequence | Representation status |
| --- | --- | --- | --- |
| A | Do you have water? | `need_water + punct_question` | Water and availability question are explicit. The addressee is intentionally omitted. |
| B | Yes. Cold water. For sale. | `logic_yes + state_cold + need_water + money_coins` | Yes, cold, and water are explicit. Commercial availability is inferred from water plus money; it is not a dedicated SALE primitive. |
| A | Three bottles, please. Card payment? | `need_water + qty_plus + money_card + punct_question` | A request for more water and card-payment question are preserved. Exact quantity, container, and politeness are intentionally omitted. |
| B | Yes. Six units of local currency. | `logic_yes + money_coins` | Confirmation and money/currency are explicit. Exact price and the local-currency qualifier are intentionally omitted. |

### Intentional omissions

- `QUANTITY_3`: no canonical exact digit `3`; `qty_2 + qty_1` is not accepted arithmetic notation.
- `BOTTLE / UNIT`: no broad bottle/container primitive.
- `PRICE_6`: no canonical exact digit `6`; numeric notation currently implements only `0`, `5`, and the composed `50` rendering.
- `SALE`: represented only through `need_water + money_coins`; a dedicated sale relation is not introduced.
- addressee, politeness, and local qualifier: not decision-critical in this first blind dialogue and not forced into new vocabulary.

These are `INTENTIONAL_OMISSION` / `LOSSY` choices, not vocabulary-change requests. The test must not add symbols or alter grammar to improve this case.

## 05A — blind decoding

Use the exact [blind prompt](prompts/05a-blind-decoding.txt) verbatim with the exact PNG.

For each system, start a **new conversation**, provide no Pictiq name, URL, handbook, prior explanation, or follow-up before saving the first response. Disable or avoid web search where the product permits. Record the visible product/model label and date. If the system identifies Pictiq or appears to know the project, record `POSSIBLE PRIOR-KNOWLEDGE / CONTAMINATION EVENT`; retain the result.

Initial panel:

1. ChatGPT
2. Gemini
3. Claude
4. Microsoft Copilot
5. Mistral Vibe
6. DeepSeek
7. Perplexity — supplementary only, because consumer multi-model orchestration can make model-family attribution less clean.

Do not infer backend model names beyond what the product UI shows.

## 05B — guided production / transfer

Only after capturing the 05A first response in the **same conversation**, provide the fixed [guide artifact](guide-manifest.md), then use [the normative production prompt](prompts/05b-guided-production.txt) verbatim. The selected guide is the unchanged Pictiq Handbook v1.0 PDF. Do not create a model-specific explanation or substitute guide.

## 05C — repair

Reveal the exact intended four-turn dialogue only after 05B. Then use [the repair prompt](prompts/05c-repair.txt) verbatim. Do not automatically evaluate or adopt proposed repairs.

## Recording and analysis

Use the unpopulated [result schema](result-schema.json) once per system/run. Score each 05A semantic slot only as:

- `CORRECT`
- `APPROXIMATE`
- `INFERRED_FROM_CONTEXT`
- `OMITTED`
- `WRONG`
- `HALLUCINATED`

Slots: `WATER`, `QUESTION_AVAILABILITY`, `YES`, `COLD`, `SALE`, `QUANTITY_3`, `BOTTLE_UNIT`, `CARD_PAYMENT`, `YES_CONFIRMATION`, `PRICE_6`, `LOCAL_CURRENCY`.

Also record stated confidence, noted ambiguity, recovered dialogue structure, recovered turn boundaries, contamination/recognition, and repair suggestions. Do not rank systems or create an overall leaderboard.

## Research boundaries

- The panel is diverse but not statistically representative.
- Consumer products and their backends may change.
- Public Pictiq material may create training/web exposure; a new conversation and no guide reduce conversational contamination but cannot prove absence of prior exposure.
- Findings apply only to these specific products/runs on their recorded dates.
- Results cannot prove universal human comprehension.
- Stress Test 05 is not a publication milestone until runs are collected and analyzed.


## Results analysis — supplied five-transcript set

**Status:** `CROSS-MODEL ANALYSIS COMPLETE / READY FOR HUMAN REVIEW`.

Five supplied transcripts (ChatGPT, Claude, Gemini, Mistral, Microsoft Copilot) have been retained and analyzed. DeepSeek remains excluded because no comparable usable run was supplied. This analysis does not make a model ranking, create an aggregate score, alter the frozen prompt/stimulus, or change Pictiq production assets.

### Critical provenance finding

The supplied transcripts and screenshot describe a different visual dialogue from the frozen 05A JSON and PNG in this directory. The supplied runs include `qty_2 + qty_1` and `qty_5 + qty_1`; the frozen 05A uses `qty_plus` and intentionally omits exact quantity and price. See [evidence provenance](evidence/README.md).

The transcripts therefore remain valuable as an **alternate-stimulus exploratory set**, but cannot be presented as a verified result of the published frozen 05A experiment. A future replication must bind each run to the exact PNG hash, prompt, and guide version before more models are added.

### Results artifacts

- [Method](method.md)
- [Primary evidence manifest](evidence/README.md)
- [Blind semantic slots](blind-slot-analysis.json)
- [Visual recognition analysis](visual-recognition-analysis.json)
- [Guided production analysis](guided-production-analysis.json)
- [Repair analysis](repair-analysis.json)
- [Model profiles](model-profiles.md)
- [Cross-model findings](cross-model-findings.md)
- [Limitations](limitations.md)

### Current protocol / handbook finding

Current [`spec/GRAMMAR.md`](../../../spec/GRAMMAR.md) defines additive consecutive quantity tiles, including `qty_1 + qty_2 = 3`. Handbook v1.0, the supplied guide, does not make that rule explicit. This is a **HANDBOOK VERSION GAP / documentation clarification candidate**, not evidence for new numeric notation or new vocabulary. The existing frozen 05A intentionally avoids that mechanism, so the supplied quantity results cannot evaluate its frozen design.
