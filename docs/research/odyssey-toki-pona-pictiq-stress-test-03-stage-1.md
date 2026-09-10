# Pictiq Stress Test 03: Odyssey × Toki Pona × sitelen pona × Pictiq — Stage 1

> Status: RESEARCH / ARCHITECTURE STAGE 1  
> Date: 2026-09-10  
> Scope: architecture, documentation, and candidate analysis only. No SVGs, no new canonical lexical IDs, no entity registry entries, no release/tag.

## Research question

How should Pictiq represent literary narrative meaning when the source passes through English, Toki Pona, sitelen pona, and Pictiq without treating surface grammar or source-language lexical categories as mandatory Pictiq vocabulary?

Stage 1 records architectural findings from six manually reviewed semantic areas. It does not create the final comparison artifact and does not claim a finished Odyssey translation.

## Reviewed semantic areas

1. Return from war / Odysseus / Calypso.
2. Gods / Poseidon / hostility / homecoming.
3. Ship / sea / dark sky.
4. Arete dialogue: who are you / where from / clothing.
5. Food / survival / animal / cooking.
6. Poseidon / Polyphemus / eye injury / family relation / blocked homecoming.

No additional Odyssey cases are inferred in this pass.

## Central translation principle

Pictiq translates semantic and practical function, not the surface form of the source language.

Pictiq preserves distinctions required for the intended meaning or action, not distinctions merely because a source language lexicalizes or grammaticalizes them.

For narrative use, Pictiq may preserve characters, actions, important relationships, locations, state changes, event order, and recurring narrative anchors. It may omit literary ornament, redundant metacommunication, grammatical distinctions unnecessary to comprehension, and exact lexical distinctions that do not materially affect the narrative skeleton.

## Analytical categories

Stage 1 adds `INTENTIONAL_OMISSION` as an analysis category.

| Category | Meaning |
| --- | --- |
| `LOSSY` | A relevant distinction was attempted but some of it was lost. |
| `GAP` | The relevant meaning cannot currently be represented honestly enough. |
| `INTENTIONAL_OMISSION` | Source information was deliberately excluded because it does not materially contribute to the selected Pictiq representation. |

`INTENTIONAL_OMISSION` does not mean the omitted information is intrinsically unimportant. It means the information was omitted relative to the chosen Pictiq narrative representation.

Examples from the review include washing hands before preparing food, mast/sail detail when departure by ship matters, literary metacommunication such as “I will answer your questions,” redundant politeness/address formulas, and poetic descriptions of sky/sea when they do not affect the narrative event.

## Structural gender neutrality

Pictiq does not encode gender by default. Generic `person_generic` means human/person, not man or woman.

Do not create Core distinctions for man/woman, he/she, son/daughter, or husband/wife solely because source languages encode them. Entity symbols identify specific entities but do not need to encode gender. Gender may be inferred from known entity identity, narrative context, external knowledge, or a specialized context where the distinction is materially required.

## Relationship composition patterns

These are hypotheses and compositional patterns, not new lexical vocabulary.

| Pattern | Contextual reading | Constraint |
| --- | --- | --- |
| `love_heart + person_generic` | loved person / partner / beloved / close relation | Does not formally mean husband or wife. |
| `love_heart + person_generic + qty_5 + qty_plus` | family / loved group / related group | Quantity indicates many; family reading is contextual. |
| `love_heart + person_generic + rel_lesser` | child / descendant / younger related person | `<` does not globally mean child. No son/daughter encoding. |

## Entity-symbol implications

Odyssey supports the existing Entity Symbols architecture. Narrative needs recurring unique identifiers rather than ordinary lexical tiles for every proper name.

The current accepted example is Odysseus. Stage 1 identifies these candidates as accepted for entity-symbol design in Stage 2, without creating SVGs or registry entries now:

- Calypso
- Poseidon
- Zeus
- Saturn
- Polyphemus

Entity symbols should be scoped, stable inside the narrative/project context, associative where appropriate, visually unique, and distinct from lexical primitives. Poseidon should not become merely a generic trident lexical symbol. Zeus may use lightning association but must not duplicate `power_energy`.

Entity Symbols may identify people, countries, cities, islands, named places, organizations, named objects, fictional locations, and other unique entities. Ukraine, Greece, and Ithaca may eventually have scoped unique entity symbols when required. They are not lexical UKRAINE/GREECE/ITHACA tiles.

## BAD, conflict, and intensity

`qual_bad` remains negative evaluation, attitude, or state. It is not active conflict.

A new ordinary primitive candidate `conflict` is deferred to Stage 2. Its semantic field is conflict / war / aggression / attack / hostile action. The visual direction is two crossed swords. It is not created in Stage 1.

Human-reviewed contrast:

- `POSEIDON + qual_bad + power_energy → ODYSSEUS`: Poseidon has a strongly negative or hostile attitude toward Odysseus.
- `POSEIDON + CONFLICT → ODYSSEUS`: Poseidon acts aggressively or conflicts with Odysseus.
- `POSEIDON + qual_bad + power_energy + CONFLICT → ODYSSEUS`: strong hostility expressed through hostile action.

`power_energy` may potentially act as an intensifier when placed with an evaluative or emotional semantic unit, for example `love_heart + power_energy` or `qual_bad + power_energy`. This is a grammar/semantic hypothesis requiring cross-domain testing because `power_energy` also has literal electricity/power readings.

Repeating symbols such as `love_heart + love_heart + love_heart` is not preferred as formal intensity grammar because repetition may signal intensity, plurality, multiple objects, or decoration.

## Semantic frames

The meaning of a Pictiq composition may emerge from the semantic frame of the whole group, not from simple pairwise dictionary substitution.

`ANIMAL + FIRE` can imply animal exposed to fire, burning animal, sacrifice, or another contextual reading. `ANIMAL + FOOD + FIRE` shifts the frame toward cooking, cooked animal food, or meat preparation. The FOOD tile is semantically important in the cooking composition.

Do not add COOK solely for this Odyssey case.

## Communication structure as meaning

When communication structure already performs a speech act, Pictiq does not necessarily need a lexical tile naming that speech act.

- `person_generic + punct_question` can pragmatically ask “Who are you?”
- A following entity symbol such as `entity:odysseus@literary` can function as the answer.
- `comm_speak + punct_question` or `comm_speak + comm_sound + punct_question` may ask whether to talk, communicate, explain, or begin communication depending on context.

Do not add general lexical primitives for WHO, I, YOU, NAME, ASK, ANSWER, or STRANGER from this passage alone.

## Location, origin, and clothing questions

Do not create FROM or ORIGIN for this pass. The reviewed direction is to reuse `rel_here`, place/home context, and `punct_question`.

Conceptual examples:

- `rel_here + punct_question`: where / here? / current place?
- `rel_here + punct_question` plus a home/place context: where is home? / where are you from? / your place?
- a following named-place entity symbol can serve as the answer.

Clothing questions can be carried by `person_generic + item_clothing + punct_question`, or in clear dialogue context by `item_clothing + punct_question`. The exact English GIVE relation may be intentionally omitted. Do not add GIVE based solely on this case.

## Narrative sequence

Sequential Pictiq frames may preserve event order naturally: A, then B, then C.

This does not make adjacency or visual sequence a strict universal causality operator. A preceding frame may provide causal interpretation through narrative context, but Pictiq does not define `A → B` as “A causes B.” Do not add BECAUSE or CAUSE from this review.

## Stage 2 ordinary primitive candidates

These are accepted as Stage 2 visual-design candidates only. They are not canonical lexical IDs in Stage 1.

| Candidate | Semantic field | Visual direction | Constraint |
| --- | --- | --- | --- |
| CONFLICT | conflict / war / aggression / attack / hostile action | two crossed swords | Distinct from `qual_bad`. |
| WATERCRAFT | boat / ship / generic floating transport | simple neutral boat/ship silhouette | Do not split boat/ship/yacht/ferry/tanker/cargo ship yet. |
| SACRED | sacred / divine / religious / holy | halo-like horizontal ellipse/ring with short rays | Must remain distinct from `nature_sun` and `state_light`. |
| ANIMAL | generic animal category | multiple animal silhouettes of different scales | Do not select one species as universal animal. |
| CLOUD / SKY | cloud / sky / overhead atmospheric/weather context | simple cloud silhouette | `COLOR(dark)` can specialize dark cloud/sky; do not add DARK. |

## Cross-domain evidence from existing additions

`surface_wavy` receives independent evidence beyond Road Stress Test 02. Road uses include slippery / uneven / surface irregularity; narrative/sea uses include waves or sea surface. This supports broad semantic compression as a reusable cross-domain pattern.

Parametric COLOR receives narrative evidence. `surface_wavy + color(dark)` can represent dark sea; future `cloud_sky + color(dark)` could represent dark cloud / dark sky. This is preferable to introducing lexical DARK, BLACK, GREY, and similar palette words when the actual color/value can carry the information.

`state_dead` receives narrative evidence independent of Road/Safety:

- `person_generic + qty_5 + qty_plus + state_dead + logic_no`: people not dead / survival.
- `ENTITY + state_dead + logic_no`: entity does not die / death avoided in context.

`state_dead` must not be used for “dead end,” where the road meaning is no through continuation.

## Generic animal architecture

General Pictiq may need a generic ANIMAL candidate. Specific species belong to contextual Animal/Nature vocabulary. Specialized taxonomy can grow arbitrarily detailed only where a domain requires it. A named individual animal may additionally receive an entity symbol.

Generic animal, species, and individual animal are three different levels and should not be collapsed.

## Physical detail filter

Pictiq narrative does not need to encode every physical object mentioned in literary prose.

Objects such as mast, sail, hand, island, land, and cave remain unjustified as new general primitives in Stage 1 when they occur only as descriptive detail, removing them does not materially damage the narrative skeleton, existing composition approximates the passage sufficiently, or they belong naturally to a future specialized/context pack.

CAVE may sometimes be approximated contextually as `HOME/PLACE + rel_down`, but this is not a universal definition of cave.

## Food and cooking finding

`need_food + ANIMAL + state_hot` may contextually express animal food being cooked, cooked meat, or food preparation. The food tile changes the semantic frame; `ANIMAL + state_hot` alone has different plausible readings.

Do not add COOK, DINNER, STARVATION, or HUNGER based solely on the reviewed fragment.

## Polyphemus eye-injury decomposition

The manually accepted conceptual decomposition is:

```text
ODYSSEUS + CONFLICT → POLYPHEMUS + eye_look + qty_1 + qty_minus
```

Approximate reading: Odysseus attacks/conflicts with Polyphemus, resulting in one eye lost/damaged.

This remains an architecture finding because `CONFLICT`, the Polyphemus entity, and final narrative notation are not implemented in Stage 1.

## Context-pack implications

A future Odyssey or literary-narrative context pack should reuse existing ordinary icons, numeric notation, parametric color, and entity symbols instead of owning them exclusively. It may recommend scoped entity symbols and narrative-specific candidate primitives, but those candidates must pass normal vocabulary review before entering the canonical registry.

A future Road/Public Wayfinding pack may continue reusing `surface_wavy` and numeric notation. The Odyssey review does not change their accepted Stress Test 02 status.

## Stage 1 outcome

- New canonical SVGs: none.
- New ordinary lexical IDs: none.
- Entity registry entries: none.
- Existing icon geometry changed: no.
- Release/tag: none.
- Main architectural addition: narrative translation principles, `INTENTIONAL_OMISSION`, structural gender neutrality, entity-symbol implications, and Stage 2 candidates.
