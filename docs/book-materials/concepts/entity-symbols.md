# Entity symbols

## Core observation

“A person” and “this named person” are different semantic jobs. A named person needs a scoped visual identifier rather than alphabetic spelling or another generic noun.

## Mechanism

A Pictiq entity symbol is a visual proper name. It identifies one specific entity within a namespace, such as `entity:odysseus@literary` or `entity:anton-biletskyi-volokh@personal`.

The symbol does not need to describe the entity completely. It only needs to be stable, distinguishable, learnable, and governed inside its declared context.

## Two authority patterns

1. **Self-defined identity:** a living person supplies an intentional mark or logo, and Pictiq adapts it technically to the protocol. Anton’s personal logo is the first local example.
2. **Associative identity:** a project uses a small number of recognizable attributes for a historical, literary, or public-domain entity. The attributes help identify the entity but do not become the symbol’s lexical semantics.

## Association is not semantics

Odysseus may use waves as an identification cue, but the symbol does not mean sea. Einstein may use distinctive hair, but the symbol does not mean hair. Buddha / Siddhartha Gautama may use calm facial cues, but the symbol does not mean Buddhism, meditation, religion, peace, or teaching.

## Composition

Entity symbols may sit next to ordinary Pictiq concepts. `entity:anton-biletskyi-volokh@personal + comm_speak` can mean Anton speaks, Anton said, or communication associated with Anton. Pictiq does not add a possession operator for this; adjacent entity + concept expresses contextual association unless the distinction changes the required action.

## Evidence

[Protocol entity section](../../../spec/PROTOCOL.md#12-communication-primitive-classes), [proper names rule](../../../spec/PROTOCOL.md#8-proper-names-and-entity-symbols), [entity registry](../../../entities/entity-index.json), and [pilot QA note](../experiments/entity-symbol-pilot.md).

## Current status

**IMPLEMENTED / ACCEPTED.** The six examples are official Pictiq project entity-symbol examples. They are not ordinary Core lexical tiles and do not change the Core/Standalone lexicon count.

## Unresolved questions

Namespace discovery, revision workflow, public reuse policy, and recognition thresholds need further pilots.

## Potential book angle

Visual proper names as governed symbols: a bridge between language, identity, narrative translation, and visual protocol design.
