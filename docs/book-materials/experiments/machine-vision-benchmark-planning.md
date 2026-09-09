# Machine Vision Benchmark Planning

> **Status:** PLANNED / NOT RUN  
> **Added:** 2026-09-09  
> **Source:** [Perplexity ideas harvest](../research/perplexity-ideas-harvest-2026-09.md), [human-machine shared symbols](../concepts/human-machine-shared-symbols.md)

## Research questions

1. Can multimodal models infer the meaning of a Pictiq tile zero-shot?
2. Can they identify the exact canonical `icon_id` when given the Pictiq lexicon?
3. Can a simpler CV/classification pipeline recognize canonical IDs more reliably than open-ended semantic interpretation?

## Suggested comparison

| Mode | Input | Expected output | What it tests |
|---|---|---|---|
| A | Image only | Natural-language meaning | Open-ended visual/iconic interpretation. |
| B | Image plus lexicon | Exact `icon_id` | Lexicon-grounded symbol recognition. |
| C | Known canonical dataset | Exact `icon_id` classification | Whether a narrow classifier beats a general VLM for canonical IDs. |

## Transformations to test

- canonical SVG;
- raster render;
- 64 px;
- 24 px;
- rotation;
- perspective;
- physical print;
- phone screen;
- shirt/card/luggage-tag surface;
- poor lighting;
- low contrast;
- partial blur or compression.

## Research leads

The supplied PDF mentions the Visual Iconicity Challenge and related VLM/iconicity work. Treat this as a research lead only. Verify the paper, task design, metrics, and citation before using it in publication or in the canonical literature review.

## Guardrails

- Do not call model guesses human comprehension.
- Do not call zero-shot natural-language guesses exact Pictiq recognition.
- Do not treat a rendered image benchmark as proof that physical products are readable.
- Do not run this benchmark until the dataset, expected labels, transformations, and scoring rules are specified.
