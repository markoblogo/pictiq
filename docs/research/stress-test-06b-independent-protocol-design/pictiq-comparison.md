# Pictiq comparison — after independent analysis

This compares independently supported themes against current Pictiq specifications. It does not adopt the models’ Phase D claims without checking the repository.

## Strong independent convergence

- A restricted visual protocol can optimize practical meaning rather than reproduce full natural-language sentences.
- Vocabulary growth should be controlled; composition should be tried before routine lexical expansion.
- Questions, affirmation, negation, small practical quantities and exact-number notation deserve separate treatment.
- Named entities should not inflate ordinary general vocabulary.
- Machines benefit from deterministic canonical representation.
- Context can narrow a visual token’s reading.

## Main divergence

Pictiq intentionally keeps phrases flat and bounded: bare tiles and adjacency are contextual semantic association, not typed subject–predicate–object syntax. The independent designs repeatedly made intent, roles, scope and relations explicit through frames, slots, containment, connectors or ASTs.

Pictiq’s alternative source of efficiency is explicit in the protocol: zero-intent, embodied versus standalone surfaces, action-relevant polysemy, repair dialogue, and functional sufficiency. The independent designs generally assumed a self-contained artifact and consequently placed more burden on grammar.

## Repository-grounded boundaries

- `spec/PICTIQ_MESSAGE_SCHEMA.md` v0.1 uses flat ordered token sequences and deliberately defers syntax trees, nested groups, semantic graphs and arbitrary 2D semantic placement.
- `spec/GRAMMAR.md` supplies terminal `punct_question`, standalone `logic_yes`/`logic_no`, pragmatic `qty_1`/`qty_2`/`qty_5`, and a separate exact numeric notation mechanism.
- `spec/PROTOCOL.md` makes embodiment, standalone communication, intentional omission, LOSSY/GAP distinctions, context packs and scoped Entity Symbols normative.

The comparison yields experimental alternatives, not architecture changes.

