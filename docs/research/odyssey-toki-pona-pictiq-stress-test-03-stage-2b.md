# Pictiq Stress Test 03: Odyssey × Toki Pona × sitelen pona × Pictiq — Stage 2B

> Status: IMPLEMENTED LOCALLY / HUMAN VISUAL ACCEPTANCE PENDING  
> Date: 2026-09-10  
> Scope: integrate five human-accepted scoped Odyssey Entity Symbols. No ordinary lexical primitives, no tag, no release.

## Source reference

The supplied reference sheet is archived at [`../book-materials/experiments/assets/stress-test-03-stage-2b-reference.png`](../book-materials/experiments/assets/stress-test-03-stage-2b-reference.png).

SHA-256: `df459dc55625efc8c279d00bc621f2cbb204fc9ce6e25b000fce4dc7f5bd98f3`

The sheet is treated as the visual source for the accepted silhouettes only. Its associative labels help identify the entities but do not create ordinary lexical primitives.

## Integrated Entity Symbols

| Entity ID | Display name | Namespace | Entity type | Visual association |
| --- | --- | --- | --- | --- |
| `entity:poseidon@odyssey` | Poseidon | odyssey | mythological_entity | trident over waves |
| `entity:zeus@odyssey` | Zeus | odyssey | mythological_entity | cloud and lightning |
| `entity:saturn@odyssey` | Saturn | odyssey | mythological_entity | sickle-like crescent and celestial disc |
| `entity:polyphemus@odyssey` | Polyphemus | odyssey | mythological_entity | cave/mountain mass with one eye |
| `entity:calypso@odyssey` | Calypso | odyssey | mythological_entity | sea cave over waves |

These symbols identify named entities inside the `odyssey` namespace. They are not ordinary lexical vocabulary and do not increase the ordinary canonical icon count.

## Architectural finding

Stage 2B adds the third accepted entity-symbol strategy:

1. self-defined personal symbol, as with Anton;
2. portrait/recognition-based associative identity, as with historical/literary figures;
3. non-portrait associative identity, as with Poseidon, Zeus, Saturn, Polyphemus, and Calypso.

The visual associations are not lexical semantics. Poseidon can use a trident and waves without adding TRIDENT or SEA. Zeus can use cloud and lightning without adding GOD, THUNDER, or STORM. Calypso can use cave/waves without adding CAVE, ISLAND, WOMAN, or SEA.

## Collision checks

- Poseidon is distinct from `surface_wavy` and from any future generic sea/water primitive because the trident/waves composition identifies a named entity only inside the Odyssey namespace.
- Zeus is distinct from `power_energy` and `nature_cloud`; lightning/cloud are entity cues here, not power or weather statements.
- Saturn is distinct from future sickle or astronomy concepts; the crescent/disc identifies the scoped mythological/cultural entity.
- Polyphemus is distinct from `eye_look`; the single eye is embedded in an entity silhouette and does not mean LOOK.
- Calypso is distinct from `move_watercraft`, `surface_wavy`, and any future cave/place symbols; the cave/waves silhouette identifies the named entity.

## QA evidence

Human visual acceptance sheet: [`../../build/qa/stress-test-03-stage-2b-entity-qa.png`](../../build/qa/stress-test-03-stage-2b-entity-qa.png)

The sheet shows reference crop → canonical entity SVG → 64 px → 24 px for all five symbols and a mixed grid with existing Odysseus plus the new Odyssey entities.

## Implementation outcome

- Entity SVGs added under `entities/svg/`.
- Source crops added under `inputs/silhouettes/entity-symbols/`.
- `entities/entity-index.json` updated from 6 to 11 entity-symbol examples.
- `tools/validate_entities.py` updated to allow `mythological_entity` as a scoped entity type.
- Ordinary `icons/svg/`, `lexicon/icon-index.json`, vocabulary classification, packs, and profiles were not changed by this Stage 2B pass.

## Deferred

Stage 2B does not add ordinary primitives for TRIDENT, SICKLE, CYCLOPS, CAVE, ISLAND, WOMAN, MAN, GOD, SEA, THUNDER, or STORM. Those remain future vocabulary questions only if a non-entity context requires them.
