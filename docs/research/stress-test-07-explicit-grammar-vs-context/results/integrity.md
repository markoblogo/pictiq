# Result-integrity record

## Collection scope

Five supplied model transcripts were archived byte-for-byte on 2026-09-20. They contain the six blind interpretations and practical responses in their assigned order, except Mistral, which ends before `07C-B` after a service-limit message. No supplied transcript contains the pre-registered micro-learning or learned-transfer phases.

| Transcript | Order | Primary stimuli observed | Blindness status | Use in analysis |
|---|---|---|---|---|
| Claude | 2 | 6/6 | `SOURCE_EXPOSED` | interface/format diagnostic only |
| Copilot | 2 | 6/6 | `SOURCE_EXPOSED` | interface/format diagnostic only |
| Gemini | 1 | 6/6 | `BLIND_CANDIDATE` | exploratory visual evidence |
| ChatGPT | 1 | 6/6 | `BLIND_CANDIDATE`; `07C-A` reported content mismatches frozen visual | exploratory except `07C-A` |
| Mistral | 1 | 5/6 | `SOURCE_EXPOSED`; incomplete | interface/format diagnostic only |

`BLIND_CANDIDATE` means the transcript does not disclose source/metadata access. It does not independently prove that the participant received the intended pixels.

## Source hashes

| Archive file | SHA-256 |
|---|---|
| `raw/claude-07.md` | `b580ffe584a416a17ff93f736d36bc586bc249f71b16620c4f764d7f79fcf443` |
| `raw/copilot-07.md` | `7d36dee56355515b0fb010aedcd8ae06380ab0b90e4be9da5f435a7268182e05` |
| `raw/gemini-07.md` | `a1ac355793f5f00ef4739df584f9dd3145539cd9c4360c408cd2901fae48a383` |
| `raw/gpt-07.md` | `4f58df9792cad46ff10c80235ea2b99ac240cb839b9b6591bb870c06a2cb2cfe` |
| `raw/mistral-07.md` | `0c15d91de57b15a017e271366538f9d072cdea27670fa5b61399b3a1f1e531ff` |

## Critical delivery finding

Claude, Copilot and Mistral explicitly accessed semantic SVG internals such as `data-id="need_water"`, `data-id="need_toilet"` and `punct_question`. They are not blind visual-comprehension observations. This is a delivery-channel failure: participant-facing SVG source exposes labels even when the rendered artwork has no English legend.

The frozen primary SVGs and prompts remain unchanged. Any repeat must use a separately versioned, rasterized or metadata-sanitized delivery derivative, with new provenance, rather than changing this experiment's frozen stimuli.
