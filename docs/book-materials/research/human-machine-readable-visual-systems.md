# Human + Machine Readable Visual Systems — Comparative Note

> Status: comparative research note
> Source event: Pictiq Research Foundations — Batch 02
> Rule: external precedent notes require primary-source verification before public claims.

## Main lesson

Human readability and machine reliability usually come from **layering + stable identifiers + constrained structure + redundancy + validation**, not from expecting one visible layer to do everything.

## Precedent map

| Precedent | Useful lesson for Pictiq | Boundary |
| --- | --- | --- |
| AprilTag / ArUco | Robust physical recognition often uses machine-oriented geometry and an error model. | Pictiq human icons are not automatically camera-robust tags. |
| GS1 DataMatrix | Exact identity and records can ride alongside human-readable labels. | Pictiq should not become a barcode; linked data is a separate route. |
| BPMN | A diagram can be visual while still having formal machine semantics. | BPMN requires constrained notation and tooling; Pictiq v0.1 is flatter. |
| SysML | Multiple views can synchronize around a formal model. | Too heavy for current Pictiq; useful as long-term model/view comparison. |
| Ontologies / semantic markup | Concept identity can be separate from image and wording. | Ontologies are not human-first icons. |
| Tactical symbology | A visual grammar can pair with encoded identifiers. | Operational authority and training matter. |
| ISA / P&ID | Symbols, tags, and relationships work together. | Domain-specific diagrams are not general language. |
| Public pictograms + accessibility metadata | Human comprehension and digital accessibility need different channels. | A visible icon alone is not accessibility. |

## Pictiq implication

Pictiq's strongest current machine-readable path is **semantic-native**, not vision-native: Message JSON, canonical IDs, registries, SVG metadata, Renderer output, and browser parity. Physical machine recognition should be treated as a separate future research track with its own scan profile, constraints, and tests.
