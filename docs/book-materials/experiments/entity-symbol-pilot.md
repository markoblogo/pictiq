# Entity-symbol pilot

## Starting question

How can Pictiq represent names without alphabetic spelling?

## Hypothesis

A named entity can be represented by one stable visual identifier inside a declared namespace. Pictiq does not translate a proper name; it assigns or reuses a visual identifier for the entity.

## Mechanisms tested

1. **Self-defined identity:** Anton Biletskyi-Volokh uses a supplied personal logo adapted into the Pictiq frame.
2. **Portrait/recognition-based associative identity:** Odysseus, William Shakespeare, Albert Einstein, Leonardo da Vinci, and Buddha / Siddhartha Gautama use approved associative visual identifiers.
3. **Non-portrait associative identity:** Poseidon, Zeus, Saturn, Polyphemus, and Calypso use scoped Odyssey symbols built from associative attributes rather than portrait likeness.

## Local registry

The pilot registry is `entities/entity-index.json`. It stores each entity ID, namespace, display name, aliases, entity type, authority, provenance, icon path, status, governance note, and visual cues.

Entity symbols are stored under `entities/svg/` and are intentionally separate from `icons/svg/` and `lexicon/icon-index.json`.

## Pilot set

| Entity ID | Display name | Namespace | Authority pattern | Provenance |
| --- | --- | --- | --- | --- |
| `entity:anton-biletskyi-volokh@personal` | Anton Biletskyi-Volokh | personal | self-defined | self-supplied personal logo |
| `entity:odysseus@literary` | Odysseus | literary | project-scoped associative | approved generated reference symbol |
| `entity:william-shakespeare@historical` | William Shakespeare | historical | project-scoped associative | approved generated reference symbol |
| `entity:albert-einstein@historical` | Albert Einstein | historical | project-scoped associative | approved generated reference symbol |
| `entity:leonardo-da-vinci@historical` | Leonardo da Vinci | historical | project-scoped associative | approved generated reference symbol |
| `entity:siddhartha-gautama-buddha@historical` | Buddha / Siddhartha Gautama | historical | project-scoped associative | approved generated reference symbol |
| `entity:poseidon@odyssey` | Poseidon | odyssey | project-scoped associative | accepted Odyssey Stage 2B reference symbol |
| `entity:zeus@odyssey` | Zeus | odyssey | project-scoped associative | accepted Odyssey Stage 2B reference symbol |
| `entity:saturn@odyssey` | Saturn | odyssey | project-scoped associative | accepted Odyssey Stage 2B reference symbol |
| `entity:polyphemus@odyssey` | Polyphemus | odyssey | project-scoped associative | accepted Odyssey Stage 2B reference symbol |
| `entity:calypso@odyssey` | Calypso | odyssey | project-scoped associative | accepted Odyssey Stage 2B reference symbol |

## Conceptual finding

Entity symbols behave like visual proper names. Their internal visual cues are recognition aids, not lexical components. One symbol identifies one entity within a namespace, and natural-language aliases may resolve to the same entity ID. The Odyssey additions show that a stable entity symbol can be associative without being portrait-like: a trident can identify Poseidon in the Odyssey namespace without creating a generic TRIDENT primitive.

## QA artifact

Local visual review sheets: `build/qa/entity-symbols-demo.png` and `build/qa/stress-test-03-stage-2b-entity-qa.png`.

The sheet compares each source crop with the framed canonical symbol plus 64 px and 24 px renders. The expected test is distinguishability and learnability after introduction, not unaided universal name recognition.

## Future book relevance

This pilot supports future material on visual proper names, narrative translation, identity governance, scoped canonicity, and the difference between a symbol’s associative features and its semantic identity.

## Current status

Implemented locally as official Pictiq project entity-symbol examples after human acceptance of the supplied reference imagery. No tag, release, or ordinary Core lexicon count change is implied.
