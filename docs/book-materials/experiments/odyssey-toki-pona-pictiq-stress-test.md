# Odyssey × Toki Pona × sitelen pona × Pictiq Stress Test

> Source artifact: [Pictiq Stress Test 03 Stage 1](../../research/odyssey-toki-pona-pictiq-stress-test-03-stage-1.md)  
> Status: ARCHITECTURE / BOOK-MATERIALS RECORD  
> Date: 2026-09-10

## Starting question

Can Pictiq carry narrative meaning from the Odyssey while being compared against English, Toki Pona, and sitelen pona without turning every source-language word or grammatical distinction into a new Pictiq tile?

## What Stage 1 records

Stage 1 used six manually reviewed semantic areas: return from war, gods and hostility, ship/sea/dark sky, Arete’s dialogue questions, food/survival/animal/cooking, and the Polyphemus eye-injury/homecoming block.

The main architectural result is that Pictiq should translate semantic and practical function rather than surface form. It should preserve distinctions required for the narrative skeleton and selected reader action, while intentionally omitting details that do not materially affect that representation.

## Book-use value

This experiment is useful book material because it shows Pictiq moving beyond road signs and travel cards into narrative compression. The interesting finding is not that Pictiq can replace Homeric prose. It is that a visual protocol needs a defensible filter for what a narrative representation must preserve.

## Accepted principles preserved

- Pictiq does not encode gender by default.
- Proper names belong to scoped Entity Symbols, not ordinary lexical tiles.
- `INTENTIONAL_OMISSION` is different from `LOSSY` and `GAP`.
- Communication structure can perform some speech acts without separate WHO/ASK/ANSWER tiles.
- Whole semantic frames matter: `ANIMAL + FIRE` is not the same frame as `ANIMAL + FOOD + FIRE`.
- Event order can be preserved by sequence without defining universal causality.

## Stage 2 candidates

Entity-symbol design candidates: Calypso, Poseidon, Zeus, Saturn, and Polyphemus.

Ordinary primitive candidates: CONFLICT, WATERCRAFT, SACRED, ANIMAL, and CLOUD/SKY.

These are design candidates only. No icons, registry entries, or canonical IDs were created in Stage 1.

## Relationship to previous stress tests

Stress Test 01 established Toki Pona and sitelen pona as comparative research systems, not direct ancestors or completion targets.

Stress Test 02 showed that a road context can reuse broad primitives and shared notation, especially `surface_wavy`, `state_dead`, and numeric notation. Stress Test 03 gives `surface_wavy` and `state_dead` independent narrative evidence, while keeping their accepted classification unchanged.

## Future work

Stage 2 can design scoped Odyssey entity symbols and test deferred ordinary primitive candidates. A later visual comparison must use actual canonical Pictiq assets and must not invent fake sitelen pona glyphs or fake Pictiq icons.

## Stage 2A — accepted ordinary primitives

Stage 2A integrated five human-accepted ordinary primitives from the supplied visual reference sheet. The source image is archived at [`assets/stress-test-03-stage-2a-reference.png`](assets/stress-test-03-stage-2a-reference.png) with SHA-256 `8e6c3732336c77330c2ea5b1579e2c7174976b2b7233305e95f1b8eb5bf91883`.

| ID | Classification | Why this general primitive was chosen | Rejected alternatives |
| --- | --- | --- | --- |
| `action_conflict` | CONTEXTUAL | Odyssey pressure separated active hostile action from `qual_bad` negative attitude. | Separate WAR / ATTACK / FIGHT primitives. |
| `move_watercraft` | CONTEXTUAL | Ship/sea narrative required a generic water-transport form, not a literary ship subtype. | Sailboat, yacht, tanker, ferry, cruise ship, military vessel, or immediate cleanup of existing `move_boat`. |
| `qual_sacred` | CONTEXTUAL modifier | Divine/religious pressure can be handled by a broad modifier. | Separate GOD / PRIEST / TEMPLE primitives. |
| `nature_animal` | CORE | Food/survival/cooking pressure exposed a broad animal category with everyday reuse. | Species, subspecies, mammal-only interpretation, or named-animal Entity Symbols. |
| `nature_cloud` | CONTEXTUAL | Dark sky/sea pressure supports cloud/sky plus parametric color. | Separate SKY / DARK / BLACK / GREY primitives. |

The methodological point remains that Odyssey discovers pressure on the vocabulary; it is not copied as a source-language vocabulary template. Stage 2A did not add Calypso, Poseidon, Zeus, Saturn, or Polyphemus entity symbols.

QA evidence: [`../../../build/qa/stress-test-03-stage-2a-primitive-qa.png`](../../../build/qa/stress-test-03-stage-2a-primitive-qa.png).

## Stage 2B — accepted Odyssey Entity Symbols

Stage 2B integrated five human-accepted scoped entity symbols from the supplied mythological-entities reference sheet. The source image is archived at [`assets/stress-test-03-stage-2b-reference.png`](assets/stress-test-03-stage-2b-reference.png) with SHA-256 `df459dc55625efc8c279d00bc621f2cbb204fc9ce6e25b000fce4dc7f5bd98f3`.

| Entity ID | Role | Boundary |
| --- | --- | --- |
| `entity:poseidon@odyssey` | scoped mythological entity | Uses trident/waves as identity cues; does not add TRIDENT or SEA primitives. |
| `entity:zeus@odyssey` | scoped mythological entity | Uses cloud/lightning as identity cues; does not add GOD, THUNDER, or STORM primitives. |
| `entity:saturn@odyssey` | scoped mythological entity | Uses sickle/disc as identity cues; does not add SICKLE or astronomy primitives. |
| `entity:polyphemus@odyssey` | scoped mythological entity | Uses one eye/cave silhouette as identity cues; does not add CYCLOPS or CAVE primitives. |
| `entity:calypso@odyssey` | scoped mythological entity | Uses sea cave/waves as identity cues; does not add ISLAND, WOMAN, CAVE, or SEA primitives. |

The architectural finding is that entity symbols can be non-portrait associative visual proper names. They remain separate from ordinary vocabulary and do not change the 82-icon ordinary canonical registry.

QA evidence: [`../../../build/qa/stress-test-03-stage-2b-entity-qa.png`](../../../build/qa/stress-test-03-stage-2b-entity-qa.png).
