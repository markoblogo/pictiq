# Standalone Communication Backlog

Status: **PLANNING AND IMPLEMENTATION RECORD** for the unreleased v1.0.2 specification.

An item becomes canonical only through the [vocabulary decision tree](PROTOCOL.md#decision-tree), structural validation, the [Visual QA Protocol](ICON_SPEC.md#visual-qa-protocol), and explicit acceptance. Batch A records the first six implementations to complete that path; all other entries remain non-canonical proposals.

## Architectural priorities

### Batch A — strongest standalone primitives

#### Neutral person — lexical tile

- **Need:** a generic human participant in unattended travel, safety, and accessibility messages.
- **Embodied equivalent:** point to oneself or another person.
- **Visual direction:** familiar public-sign or road-sign-like standing human silhouette.
- **Status:** **IMPLEMENTED / CANONICAL** as `person_generic` in Batch A2.

The concept is generic “person / human participant.” It does not encode a particular individual, pronoun, or gender.

#### GOOD / POSITIVE — modifier

- **Need:** qualify a base concept as good, acceptable, positive, or satisfactory.
- **Examples:** `food + GOOD`; `hotel + GOOD`.
- **Visual direction:** a simple positive or upward smile curve, or another broadly recognizable positive-evaluation mark.
- **Status:** **IMPLEMENTED / CANONICAL MODIFIER** as `qual_good` in Batch A1.

GOOD is not YES and does not overload `logic_yes`. Batch A accepted a thick upward/smiling curve without a face; the historical minimal-curve direction was retained.

#### BAD / NEGATIVE — modifier

- **Need:** qualify a base concept as bad, poor, unpleasant, or unsatisfactory.
- **Example:** `hotel + BAD`.
- **Visual direction:** a simple downward or frowning curve, or another broadly recognizable negative-evaluation mark.
- **Status:** **IMPLEMENTED / CANONICAL MODIFIER** as `qual_bad` in Batch A1.

BAD is not NO and does not overload `logic_no`. YES/NO and GOOD/BAD remain separate semantic axes. Batch A accepted the inverse downward/frowning curve.

#### Hot / fire — lexical-tile candidate

- **Uses to test:** heat, hot, fire, and warning.
- **Visual direction:** conventional flame silhouette familiar from safety signage.
- **Open question:** whether hot and fire can remain one contextual concept.
- **Status:** **IMPLEMENTED / CANONICAL** as `state_hot` in Batch A3.

The accepted tile is a practical contextual cue for hot, heat, or fire. It does not erase the conceptual distinction among those senses or define a specialized hazard class.

#### Cold — lexical-tile candidate

- **Uses to test:** cold, freezing, refrigeration, and comfort/safety.
- **Visual direction:** conventional snowflake associated with refrigeration or freezer use.
- **Status:** **IMPLEMENTED / CANONICAL** as `state_cold` in Batch A3.

#### Energy / electricity — lexical-tile candidate

- **Uses to test:** energy, electricity, and electrical power.
- **Visual direction:** conventional lightning bolt.
- **Boundary:** physical strength is a separate concept and must not be inferred.
- **Status:** **IMPLEMENTED / CANONICAL** as `power_energy` in Batch A3.

The accepted lightning-bolt tile means electricity or electrical power. It remains distinct from `power_plug` and does not encode human physical strength.

### Batch B — practical standalone vocabulary

#### Generic building / home — lexical-tile design research

- **Need:** generic shelter or destination beyond hotel, shop, airport, and landmark tiles.
- **Embodied equivalent:** point toward the visible place.
- **Open question:** one building/shelter concept or separate building and home concepts.
- **Status:** **STRONG CANDIDATE / DESIGN RESEARCH**.

This backlog does not decide the number of concepts or icons.

#### Produce — lexical-tile candidate

- **Potential scope:** fruit, vegetables, or fresh produce for markets, supermarkets, and food preference/context.
- **Visual direction:** a small composition of recognizable produce silhouettes, potentially a pear/apple, banana, and round fruit or vegetable.
- **Boundary:** not automatically vegan; exact objects remain open.
- **Status:** **POSSIBLE**.

#### Bakery / bread — lexical-tile candidate

- **Potential scope:** bread, bakery, and baked goods; generic grain remains excluded unless future use establishes it.
- **Visual direction:** a recognizable mix such as baguette, loaf, croissant, pretzel, or pastry.
- **Reference:** existing experience with `paris_croissant` may inform recognition, but the candidate must be universal and not Paris-specific.
- **Status:** **POSSIBLE**.

#### Eye / visual attention — lexical-tile candidate

- **Embodied equivalent:** point to the eyes or direct gaze.
- **Standalone direction:** two eyes or another recognizable visual-attention representation.
- **Status:** **POSSIBLE**.

#### Clothing — lexical-tile candidate

- **Embodied equivalent:** point to or pull clothing.
- **Standalone direction:** shirt or T-shirt on a hanger with a clearly recognizable hook.
- **Status:** **POSSIBLE**.

#### Communication / speaking — lexical-tile candidate

- **Embodied equivalent:** actual speech, gesture, and context.
- **Standalone direction:** a head or profile with mouth and outward emission marks.
- **Potential scope:** speak, communication, call out, or voice.
- **Boundary:** shouting and singing must not be assumed equivalent.
- **Status:** **POSSIBLE**.

#### Light — lexical-tile candidate

- **Visual direction:** classic incandescent light bulb with separated radiating marks.
- **Potential scope:** light, lighting, or lamp.
- **Status:** **POSSIBLE**.

#### Sun / day — lexical-tile candidate

- **Visual direction:** circle with radiating rays.
- **Potential scope:** sun or daylight, and day only in an established context.
- **Boundary:** keep separate from generic light until testing supports a relationship.
- **Status:** **POSSIBLE**.

### Batch C — protocol mechanisms

#### LARGE / SMALL — modifier research

- **Embodied equivalent:** show scale with hands or body.
- **Standalone direction:** reusable scale modifiers using conventions such as outward/inward arrows, expansion/contraction, or directional size cues.
- **Boundary:** `qty_plus` and `qty_minus` mean more/less and are not physical size.
- **Status:** **MODIFIER RESEARCH**.

#### Parametric COLOR prototype

- **Embodied equivalent:** point to a visible example.
- **Standalone direction:** canonical frame plus a neutral sample shape filled with the actual requested color.
- **Model:** arbitrary values such as `color(#747b72)`, not a finite vocabulary of color words.
- **Status:** **PROPOSED PARAMETRIC MECHANISM — NOT IMPLEMENTED**.

The prototype must test machine representation, contrast, print behavior, accessibility, and the intentional color exception without adding red, yellow, blue, green, or other lexical tiles.

#### Entity-symbol namespace and prototype

- **Need:** identify a named person, fictional character, organization, place, or object without alphabetic spelling.
- **Scope model:** an explicit local namespace such as `entity:odysseus@odyssey-pack`.
- **Governance:** personal authority where practical for real people; project-local canonicity for fictional, historical, or public-domain entities; no universal first-claim ownership.
- **Status:** **ARCHITECTURE PROTOTYPE — NOT IMPLEMENTED**.

The prototype should test local definitions such as symbol A = Odysseus, symbol B = Penelope, and symbol C = Telemachus. An Alice narrative dictionary may likewise identify recurring characters.

#### Emission-mark convention

Repeated short outward marks may act as a reusable visual convention for emitted phenomena:

- mouth/head plus marks → speech, voice, or communication;
- musical symbol plus marks → music or sound;
- light source plus radiating marks → light.

The marks are not a standalone tile. The convention must preserve the distinct semantics of speech, music, and light.

- **Status:** **VISUAL-CONVENTION RESEARCH**.

## Deferred

### Generic container

- **Potential direction:** simple bowl, vessel, or open container.
- **Gate:** a recurring Pictiq use case must demonstrate need.
- **Status:** **DEFERRED**.

### Animal categories

Do not add species broadly to Core. If a future context establishes demand, test generic functional categories first: land animal, bird, insect, or aquatic animal. Specialized packs may then include dolphin, orca, shark, or other needed species.

- **Principle:** generic functional category first; contextual taxonomy only when needed.
- **Status:** **DEFERRED / CONTEXT-PACK DIRECTION**.

### Body-location vocabulary

A generic person may initially cover generic human/body representation. In embodied communication, point directly to the relevant body area. Do not add body-part tiles to Core now.

A future medical or accessibility pack may investigate mouth, eye, head, arm, leg, stomach, or other body locations only when standalone use requires them.

- **Status:** **SPECIALIZED FUTURE PACK**.

## Explicitly rejected directions

Current architecture does not plan to introduce:

- an I / you / he / she lexical pronoun system;
- grammatical gender;
- Toki Pona grammatical particles;
- a broad possession operator solely for lexical completeness;
- an alphabetic spelling system for names;
- individual lexical color vocabulary;
- a large Toki-Pona-shaped abstract vocabulary.

Standalone text and narrative should prefer generic person concepts, scoped entity symbols, context, and composition.

## Interoperability research finding

**Non-normative.** The Toki Pona crosswalk acted as an interoperability stress test and helped reveal that lexical gaps do not imply icon gaps. Some `NONE` mappings are embodied-omittable, some expose standalone needs, some point to modifiers rather than words, colors expose a possible parametric mechanism, proper names expose entity symbols, and grammar remains out of scope.

Toki Pona is not presented as an ancestor of Pictiq. The comparison records a research result about different compression mechanisms.

## Future Handbook revision

A future Handbook revision may explain Embodied versus Standalone Communication, the body as a communication surface, modifiers versus lexical tiles, parametric color, entity symbols, and the Toki Pona crosswalk findings. Handbook v1.0 remains unchanged; this note does not schedule or create Handbook v1.1.
