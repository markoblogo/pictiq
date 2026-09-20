# Supplied result evidence

The five DOCX files in `source-docx/` are byte-for-byte copies of the supplied transcripts. They are the primary evidence for this analysis. `extracted-text/` is a mechanical paragraph extraction for review; it does not replace the DOCX sources.

| System | Source file | SHA-256 |
| --- | --- | --- |
| ChatGPT | `chatgpt.docx` | `196ccc3366e18d9d05802c155e88bd41b3fce58d08c697c75c987771dc2520e4` |
| Claude | `claude.docx` | `2e1909127e6e67867914ed4d8471ecd5be1fce09c57a3bfcccbcb0eb6a75e4fd` |
| Gemini | `gemini.docx` | `89bcf57ff909c0934c16ac961f701b3bb975015b4cfe4e02dfec612cc521e416` |
| Mistral | `mistral.docx` | `68a82d51754a9b60664081b04b5b8b6d6d63051b057cf744633dcd6231bc8bef` |
| Microsoft Copilot | `microsoft-copilot.docx` | `44423badf1f0fcadbb5d4f202d39c684ccaa56ba9cafe0906163e11413afbca6` |

## Provenance limitation

The supplied transcripts and attached screenshot describe an alternate four-turn image containing `qty_2 + qty_1` and `qty_5 + qty_1`. The frozen, published 05A source at `05a-canonical-dialogue.json` instead contains `need_water + qty_plus` in turn three and no exact-quantity tiles in turn four. The published blind PNG confirms that difference.

This directory preserves the frozen protocol and its files unchanged. The transcripts are therefore analyzed as a five-system **alternate-stimulus result set**, not as a verified execution of the frozen published 05A artifact. This is an evidence-provenance issue, not a model-performance finding. No result is discarded or rewritten.
