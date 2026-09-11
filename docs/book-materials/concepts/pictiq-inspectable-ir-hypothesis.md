# Pictiq as Inspectable Intermediate Representation

> Status: bounded architecture hypothesis / research note
> Source event: Pictiq Research Foundations — Batch 02
> Scope: future product/research hypothesis only; no Message Schema, grammar, Composer, Renderer, tool-call, or execution binding change implied.

## Bounded hypothesis

Pictiq may function as a **human-auditable / inspectable intermediate representation** for constrained operational communication: short requests, status reports, task descriptions, simple plans, alerts, handoffs, and cross-lingual UI intent.

A plausible future pipeline:

```text
Natural language / UI / AI
→ Pictiq inspectable representation
→ validated domain schema / tool call / workflow
```

The value is inspection: a person can see, correct, teach, compare, or reject the compact semantic layer before a stricter downstream system acts.

## What Pictiq is not replacing

Pictiq is not proposed as a replacement for:

- JSON;
- formal logic;
- AMR;
- PDDL;
- API schemas;
- authentication;
- authorization;
- legal or medical records;
- full natural-language semantics.

Those systems carry precision, authority, execution rules, and audit requirements that Pictiq should expose or summarize rather than replace.

## Action receipt hypothesis

A high-value future product pattern is a **Pictiq Action Receipt**:

```text
AI/system proposes an action
→ formal tool-call candidate exists
→ Pictiq presents a compact human-readable summary
→ human inspects, corrects, or confirms
→ formal schema validation / permissions
→ execution
→ Pictiq + structured execution receipt
```

Possible application classes:

- sending;
- publishing;
- deleting;
- booking;
- monitoring;
- modifying records;
- agent handoffs;
- dashboard alerts.

Pictiq should preview and explain intent; formal systems still enforce identity, permissions, validation, and records.

## Do not import semantic-frame architecture now

The supplied IR research proposes performatives, semantic frames, roles, slot schemas, AGENT/RECIPIENT/TARGET, relations, AST/graph representations, Context Pack ontologies, and typed execution bindings. These are useful comparisons and future language pressure.

They must not be added to Message Schema, Grammar, Composer, Renderer, Canonical Registry, profiles, packs, or Entity Symbols by this research harvest. Current Message v0.1 remains accepted as sufficient for pilots: document → frames → flat ordered tokens.
