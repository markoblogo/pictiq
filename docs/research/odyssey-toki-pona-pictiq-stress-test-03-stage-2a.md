# Pictiq Stress Test 03: Odyssey × Toki Pona × sitelen pona × Pictiq — Stage 2A

> Status: IMPLEMENTED LOCALLY / HUMAN VISUAL ACCEPTANCE PENDING  
> Date: 2026-09-10  
> Scope: integrate five human-accepted ordinary primitive candidates from the supplied reference sheet. No entity symbols, no tag, no release.

## Source reference

The supplied reference sheet is archived at [`../book-materials/experiments/assets/stress-test-03-stage-2a-reference.png`](../book-materials/experiments/assets/stress-test-03-stage-2a-reference.png).

SHA-256: `8e6c3732336c77330c2ea5b1579e2c7174976b2b7233305e95f1b8eb5bf91883`

The sheet is treated as a visual source for the accepted silhouettes only. Its labels and descriptive prose are not treated as normative where Stage 1 or the Stage 2A implementation brief gives more precise semantics.

## Starting state

Stage 1 was already present locally as commit `0a2f714`. The ordinary canonical registry started this pass at 77 icons.

## Integrated ordinary primitives

| ID | Classification | Semantic field | Visual source / morphology |
| --- | --- | --- | --- |
| `action_conflict` | CONTEXTUAL | conflict / war / aggression / attack / hostile action / fight | two filled crossed swords |
| `move_watercraft` | CONTEXTUAL | boat / ship / watercraft / generic water transport | filled generic hull, minimal upper structure, waves below |
| `qual_sacred` | CONTEXTUAL modifier | sacred / divine / religious / holy / ritual | heavy horizontal halo/ring with short rays |
| `nature_animal` | CORE | animal / general animal category | overlapping filled animal silhouettes of different scales, facing left |
| `nature_cloud` | CONTEXTUAL | cloud / sky / overhead atmospheric context | simple filled cloud silhouette |

The resulting ordinary canonical registry has 82 icons. Entity Symbols remain separate and still have six current project examples.

## Classification rationale

`action_conflict` is contextual because active conflict is broadly reusable across narrative, safety, culture, history/news-like writing, and migration contexts, but it is not a minimal everyday Core need. It remains distinct from `qual_bad`, which is negative evaluation, attitude, or state.

`move_watercraft` is contextual transport vocabulary. The repository already had `move_boat`; it remains unchanged to preserve existing assets and compatibility. `move_watercraft` records the accepted generic watercraft morphology from this stress test. A later compatibility cleanup may decide whether to consolidate names.

`qual_sacred` is a contextual modifier rather than a Core primitive. It allows religious/divine/ritual readings without adding separate GOD, PRIEST, or TEMPLE primitives from one narrative case.

`nature_animal` is Core with medium confidence because animal is a broad everyday/nature/food/narrative category. It deliberately stays generic: species, subspecies, and named individual animals belong to contextual/specialized taxonomy or Entity Symbols.

`nature_cloud` is contextual nature/weather/narrative vocabulary. It covers cloud, sky, and overhead atmospheric context without adding separate SKY or DARK primitives. Dark or stormy readings should prefer parametric COLOR where needed.

## Odyssey pressure points

- War/conflict and Poseidon hostility exposed the need to separate negative attitude (`qual_bad`) from active hostile action (`action_conflict`).
- Ship/sea passages supplied pressure for a generic water transport primitive and independent evidence for `surface_wavy` as water/sea surface.
- Divine actors supplied pressure for a broad sacred/divine/religious modifier instead of separate GOD/PRIEST/TEMPLE tiles.
- Food/survival/cooking passages supplied pressure for a generic animal category without creating a species taxonomy.
- Dark sky/sea descriptions supplied pressure for cloud/sky and parametric color reuse instead of lexical DARK/BLACK/GREY.

## Rejected alternatives

Stage 2A does not add WAR, ATTACK, FIGHT, GOD, PRIEST, TEMPLE, SKY, DARK, BLACK, GREY, DEER, species/subspecies tiles, or entity symbols for Calypso, Poseidon, Zeus, Saturn, or Polyphemus.

Stage 1 hypotheses remain hypotheses: ENERGY-as-intensifier is not made normative, sequence is not made causality, and relationship compositions remain contextual.

## QA evidence

Human visual acceptance sheet: [`../../build/qa/stress-test-03-stage-2a-primitive-qa.png`](../../build/qa/stress-test-03-stage-2a-primitive-qa.png)

The QA sheet shows reference crop → canonical SVG → 64 px → 24 px for all five icons, a mixed-grid comparison, and representative compositions built from actual repository assets.

## Implementation outcome

- Canonical SVGs added under `icons/svg/`.
- Pages SVG copies added under `docs/lexicon/svg/`.
- `lexicon/icon-index.json` and `docs/lexicon/icon-index.json` updated to metadata version `0.7.0`.
- `lexicon/vocabulary-classification.json` updated to 82 ordinary canonical IDs.
- `nature_animal` added to universal packs as the only new Core item from this pass.
- No entity registry entries added.
- Existing icon geometry not redesigned.
- No push, tag, or release in this pass.
