# Standalone Communication Backlog

Status: **IMPLEMENTATION RECORD** for released v1.0.2; remaining entries are future research.

An item becomes canonical only through the [vocabulary decision tree](PROTOCOL.md#decision-tree), structural validation, the [Visual QA Protocol](ICON_SPEC.md#visual-qa-protocol), and explicit acceptance. Batch A and the accepted Batch B record the implementations that completed that path; remaining entries are non-canonical proposals.

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

**Scope:** planning only. No Batch B icon or ID is implemented by this record. Candidates use existing canonical IDs only when later accepted through the vocabulary decision tree, structural validation, and Visual QA.

#### B1 — essential standalone semantics

Eye/look, communication/speaking, sound, text/writing, and image/picture.

#### B2 — environment and visual context

Sun/day, light, and LARGE/SMALL modifiers.

#### B3 — practical category vocabulary

Clothing, produce, and bakery/bread.

COLOR remains a separate parametric prototype, and entity symbols remain a separate scoped experiment.

#### Batch B accepted implementation

The supplied approved reference sheet produced these accepted IDs: `eye_look`, `item_clothing`, `comm_speak`, `comm_sound`, `media_text`, `media_image`, `nature_sun`, `state_light`, `food_produce`, `food_bakery`, `rel_greater`, and `rel_lesser`. They are **IMPLEMENTED / CANONICAL in v1.0.2** after structural and human visual acceptance.

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
- **Status:** **IMPLEMENTED / CANONICAL** as `food_produce` in v1.0.2.

#### Bakery / bread — lexical-tile candidate

- **Potential scope:** bread, bakery, and baked goods; generic grain remains excluded unless future use establishes it.
- **Visual direction:** a recognizable mix such as baguette, loaf, croissant, pretzel, or pastry.
- **Reference:** existing experience with `paris_croissant` may inform recognition, but the candidate must be universal and not Paris-specific.
- **Status:** **IMPLEMENTED / CANONICAL** as `food_bakery` in v1.0.2.

#### Eye / visual attention — lexical-tile candidate

- **Embodied equivalent:** point to the eyes or direct gaze.
- **Standalone direction:** two eyes or another recognizable visual-attention representation.
- **Status:** **IMPLEMENTED / CANONICAL** as `eye_look` in v1.0.2.

#### Clothing — lexical-tile candidate

- **Embodied equivalent:** point to or pull clothing.
- **Standalone direction:** shirt or T-shirt on a hanger with a clearly recognizable hook.
- **Status:** **IMPLEMENTED / CANONICAL** as `item_clothing` in v1.0.2.

#### Communication / speaking — lexical-tile candidate

- **Embodied equivalent:** actual speech, gesture, and context.
- **Standalone direction:** a head or profile with mouth and outward emission marks.
- **Potential scope:** speak, communication, call out, or voice.
- **Boundary:** shouting and singing must not be assumed equivalent.
- **Status:** **IMPLEMENTED / CANONICAL** as `comm_speak` in v1.0.2.

#### Light — lexical-tile candidate

- **Visual direction:** classic incandescent light bulb with separated radiating marks.
- **Potential scope:** light, lighting, or lamp.
- **Status:** **IMPLEMENTED / CANONICAL** as `state_light` in v1.0.2.

#### Sun / day — lexical-tile candidate

- **Visual direction:** circle with radiating rays.
- **Potential scope:** sun or daylight, and day only in an established context.
- **Boundary:** keep separate from generic light until testing supports a relationship.
- **Status:** **IMPLEMENTED / CANONICAL** as `nature_sun` in v1.0.2.

### Batch C — protocol mechanisms and standalone gaps

#### Batch C local implementation

The supplied approved reference sheet is used as the visual source for five local canonical candidates: `body_mouth`, `rel_here`, `rel_up`, `rel_down`, and `nature_moon`. They are **LOCALLY IMPLEMENTED / PENDING HUMAN VISUAL ACCEPTANCE** and must not be described as released until push, tag, release, and public verification are completed.

Profile treatment:

- `body_mouth` is a Standalone Core candidate. In Embodied Core, a present user can usually indicate the mouth or use eating/drinking context directly.
- `rel_here`, `rel_up`, and `rel_down` are Standalone Core and Embodied Core candidates because they preserve compact reference and orientation relations when pointing alone is not durable enough.
- `nature_moon` is a Standalone Core candidate. In Embodied Core, darkness, timing, or shared context may often supply night; add only where local utility requires it.

#### LARGE / SMALL — modifier research

- **Embodied equivalent:** show scale with hands or body.
- **Standalone direction:** reusable scale modifiers using conventions such as outward/inward arrows, expansion/contraction, or directional size cues.
- **Boundary:** `qty_plus` and `qty_minus` mean more/less and are not physical size.
- **Status:** **IMPLEMENTED / CANONICAL RELATIONAL OPERATORS** as `rel_greater` and `rel_lesser` in v1.0.2.

The supplied morphology is `>` for LARGE/greater and `<` for SMALL/lesser. Batch C extends the same relation/operator family with `rel_up` (`∧`) and `rel_down` (`∨`). The IDs are relational operators, not quantity synonyms.

#### HERE / target — relation operator

- **Embodied equivalent:** point to the actual place, object, body location, or target.
- **Standalone direction:** central target/crosshair mark that identifies “here / this place / target location.”
- **Boundary:** not a generic place tile; use existing place tiles for hotel, shop, gas, etc.
- **Status:** **LOCALLY IMPLEMENTED** as `rel_here`, pending human visual acceptance.

#### Mouth / oral intake — lexical-tile candidate

- **Embodied equivalent:** point to the mouth, eat, drink, or show the relevant action.
- **Standalone direction:** filled lips with white mouth opening from the approved reference sheet.
- **Potential scope:** mouth, eat, drink, or oral intake when context makes the action clear.
- **Boundary:** not speech, language, identity, or emotion; use `comm_speak` for communication.
- **Status:** **LOCALLY IMPLEMENTED** as `body_mouth`, pending human visual acceptance.

#### Moon / night — lexical-tile candidate

- **Embodied equivalent:** use current darkness, time of day, or shared schedule context when reliable.
- **Standalone direction:** filled crescent moon from the approved reference sheet.
- **Potential scope:** moon, night, nighttime, or night context with `time`.
- **Boundary:** not a complete time or calendar mechanism; keep separate from daylight/sun.
- **Status:** **LOCALLY IMPLEMENTED** as `nature_moon`, pending human visual acceptance.

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

## Stress-test and testing guidance

> Stress tests are allowed to expand Pictiq, but they are not allowed to dictate Pictiq.

> A useful stress test should try to break the protocol rather than prove that it already works.

Gaps found through Toki Pona, road signs, literature, websites, narrative, or machine translation still require independent Pictiq utility review. Road Signs × Pictiq is deliberately deferred until the obvious Standalone gaps above are implemented or prototyped, so it tests genuine limitations rather than known omissions.

The next evidence gate is task-based: use a Paris card, understand a road sign, read a narrative fragment, navigate a website, understand a poster/sticker, back-translate a Pictiq text, or use physical merch as an interface. Recognition questions may be local components, but a generic icon-naming exercise is not sufficient. No participants are scheduled here.

Standalone Profile work is also a prerequisite for a future translation laboratory covering an Odyssey fragment, Marcus Aurelius reflections, dialogue, procedural text, a contemporary notice, or poetry. Those translations are not performed in this task.
