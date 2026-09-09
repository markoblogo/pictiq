# Text to Pictiq RAG Prototype

> **Status:** PROTOTYPE / BASELINE
> **Input source:** [archived Python prototype](../research/inputs/pictiq-text-to-tile-rag-prototype.py)
> **Reviewed against:** then-current `main`, Pictiq v1.0.2-era 70-icon lexicon
> **Rule:** This is not production code and not an accepted translator architecture.

## Research question

Can arbitrary short natural-language input be mapped to existing Pictiq IDs using the current lexicon without training a dedicated model?

## Architectural proposal

The supplied source describes four stages:

| Stage | Proposed role |
|---|---|
| Stage A - Normalize / Segment | Convert free text into a structured concept plus quantity, negation, urgency, and question markers. |
| Stage B - Retrieve | Find candidate content tiles from the lexicon. |
| Stage C - Compose | Assemble content tile plus operators into a Pictiq sequence. |
| Stage D - Validate / Fallback | Avoid forced matches when confidence is low; route gaps to vocabulary/protocol review. |

## What the Python prototype actually implements

Stage A is not a production multilingual LLM/JSON-Schema segmenter. It is a lightweight baseline using regexes, English/Russian keyword lists, and a small demo-only RU-to-EN gloss table.

Stage B is implemented as lexical TF-IDF retrieval:

- loads `lexicon/icon-index.json`;
- removes operator categories `quantity`, `logic`, and `punctuation`;
- builds one document per content icon from `id`, `meaning_en`, weighted `aliases_en`, and `tags_en`;
- uses `TfidfVectorizer(analyzer="char_wb", ngram_range=(3, 5), sublinear_tf=True)`;
- ranks candidates by cosine similarity.

This is a lexical string baseline. It is not semantic embeddings and not true multilingual semantic retrieval.

Stage C composes:

- retrieved content tile;
- quantity tiles;
- `logic_no` for negation;
- `punct_exclaim` for urgency or `punct_question` for questions.

This broadly follows [GRAMMAR.md](../../../spec/GRAMMAR.md): object first, quantity after object, negation as `X + logic_no`, and punctuation at the end. The prototype does not run a full grammar validator or semantic validator.

Stage D applies a confidence threshold of `0.18`. If the top retrieval score is below threshold, the content tile is not forced. The result includes a low-confidence flag and refers to the standalone backlog decision tree.

## Reproduced small demonstration set

Reproduced locally on 2026-09-09 with a temporary Python environment containing `scikit-learn` and `numpy`, using the current repository `lexicon/icon-index.json`.

| Input | Tiles | Top match | Score | Flags |
|---|---|---|---:|---|
| Where can I find a toilet? | `need_toilet + punct_question` | `need_toilet` | 0.266 | none |
| I need two beers, please | `drink_beer + qty_2` | `drink_beer` | 0.315 | none |
| No card, cash only | `money_coins + logic_no` | `money_coins` | 0.401 | none |
| I need medical help urgently! | `safety_medical + punct_exclaim` | `safety_medical` | 0.484 | none |
| Мне нужна вода, срочно | `need_water + punct_exclaim` | `need_water` | 0.495 | none |
| Where is the nearest hotel? | `place_hotel + punct_question` | `place_hotel` | 0.341 | none |
| I need sunscreen | `need_bar` | `need_bar` | 0.219 | none |
| Такси, пожалуйста? | `move_taxi + punct_question` | `move_taxi` | 0.593 | none |

This is a small demonstration set, not a benchmark.

## Observed failure 1 - multi-clause compression

Input:

`No card, cash only`

One-shot output:

`money_coins + logic_no`

The one-shot output loses the two-clause structure. It negates the cash concept instead of preserving the likely intended contrast between no card and cash only.

Pre-split demonstration:

| Clause | Prototype output |
|---|---|
| no card | `money_card + logic_no` |
| cash | `money_coins` |

Implication: natural-language to Pictiq requires clause/intent segmentation before retrieval. The possible target `money_card + logic_no` and `money_coins` is a research example, not an accepted final translation.

## Observed failure 2 - lexical false positive

Input:

`I need sunscreen`

Observed output:

`need_bar`

The score `0.219` exceeded the current threshold even though sunscreen is not represented by `need_bar`. This is a lexical-similarity failure: character n-gram TF-IDF measures string overlap, not semantic equivalence.

Implication: production retrieval should use meaning-aware retrieval, a stronger fallback policy, a semantic mapping layer, or a validated intent representation. A syntactically valid tile sequence may still be semantically wrong.

## Future v2 hypothesis

Illustrative architecture only:

```json
{
  "clauses": [
    {
      "concept": "payment card",
      "quantity": null,
      "negation": true,
      "evaluation": null,
      "relation": null,
      "urgent": false,
      "question": false
    }
  ]
}
```

Potential pipeline:

Natural language -> LLM semantic segmentation -> structured intent representation -> semantic retrieval against Pictiq lexicon -> Pictiq composition -> protocol/grammar validator -> Pictiq phrase or explicit GAP.

The intermediate representation is not a frozen protocol schema.

## Pictiq to text back-translation candidate

Status: PLANNED / NOT RUN.

Research question: how much meaning survives Pictiq compression?

Pipeline:

natural language -> Pictiq -> independent back-translation -> compare original meaning with reconstructed meaning.

This may become useful for literary translation, signage, website navigation, travel communication, and AI translation evaluation.

## Protocol consistency audit note

The prototype provides evidence for a future protocol audit:

- multi-clause input exposes phrase segmentation issues;
- simple object -> operator ordering is insufficient for richer text;
- low-confidence retrieval requires explicit GAP behavior;
- translation needs a distinction between lexical retrieval and grammatical composition;
- syntactically valid output may still be semantically wrong.

No grammar change is made by this experiment record.
