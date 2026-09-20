# Stress Test 07 Pilot

**Status:** `EXECUTION INTEGRITY FAILURE / PARTIAL DATA`

The first manual pilot is invalid for primary Stress Test 07 A/B inference. It remains useful methodological evidence.

- Claude — `SVG SOURCE EXPOSED / BLIND VISUAL CONDITION INVALID`
- Copilot — `SVG SOURCE EXPOSED / BLIND VISUAL CONDITION INVALID`
- Mistral — `SVG SOURCE EXPOSED / BLIND VISUAL CONDITION INVALID`; incomplete before `07C-B`
- ChatGPT — visually usable candidate except `07C-A`, whose reported no-smoking visual is incompatible with the frozen toilet-question stimulus
- Gemini — visually usable candidate subject to the existing integrity note

The raw evidence and prior coding are preserved unchanged in [results/raw](../results/raw/), [integrity record](../results/integrity.md), [analysis](../results/analysis.md), and [coded observations](../results/blind-phase-coding.json). Pilot observations do not enter 07.1 primary inference.

## Method finding

SVG is not a neutral visual stimulus for multimodal AI testing. It can expose element IDs, semantic labels, filenames, XML structure, accessibility metadata, source geometry, and other text. When the question is visual comprehension, participants must receive metadata-free raster images. This is a delivery-method finding, not a Pictiq grammar or protocol finding.
