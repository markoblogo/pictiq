# Polysemy Decision Framework

> Status: concept note / future audit aid
> Source input: [`../research/inputs/perplexity-2026-09/intentional-polysemy-in-visual-language.md`](../research/inputs/perplexity-2026-09/intentional-polysemy-in-visual-language.md)
> Rule: explanatory framework only; do not reopen the vocabulary audit from this note.

## Core principle

Polysemy is a compression tool; unmarked ambiguity is a decoding cost.

A broad primitive is useful when it gives users a stable conceptual center and the intended reading can be recovered from grammar, composition, situation, or interface context. It becomes harmful when users must distinguish meanings that have different consequences but lack reliable contextual cues.

## Decision factors

Evaluate a broad primitive against:

- conceptual kinship;
- stable visual anchor;
- contextual recoverability;
- action equivalence;
- stakes of error;
- frequency;
- compositional repair;
- learnability;
- cultural robustness;
- accessibility/confusion risk.

## Keep broad when

- meanings form a coherent semantic family;
- there is an identifiable invariant core;
- context or composition reliably selects the intended reading;
- mistakes are low-cost or reversible;
- specificity can be expressed regularly;
- the primitive has broad combinatorial value.

## Split or contextualize when

- meanings are unrelated;
- multiple readings remain plausible in the same use case;
- users must distinguish them before context becomes available;
- the distinction changes consequential action;
- misunderstanding creates safety, legal, financial, medical, or operational risk;
- compositional repair is awkward or too slow for the context.

## Retrospective examples, not new audit decisions

| Existing concept | Why broadness may be useful | Where caution begins |
| --- | --- | --- |
| `nature_cloud` | Cloud / sky / air / atmospheric context share an overhead-atmosphere anchor. | Aviation, weather warnings, or pollution contexts may need stricter domain terms. |
| `surface_wavy` | Waves / uneven / slippery / unstable surface share a repeated undulating-surface anchor and often require similar caution. | Safety-critical road, industrial, or marine contexts may need context-pack precision. |
| `place_home` | Home / shelter / sleeping place / building-context readings support practical travel communication. | Legal residence, hotel booking, emergency shelter, and family home are not always interchangeable. |
| `qual_sacred` | Sacred / divine / religious / holy / ritual modifier is useful as a broad cultural/religious marker. | Specific religions, institutions, and legal restrictions should remain contextual or entity-specific. |
| `safety_medical` | Broad medical/safety icon is useful for urgent aid seeking. | Diagnosis, medication, allergies, dosage, and emergency triage require precise domain context. |

## Do not import speculative operators yet

The source proposes possible contextual operators and semantic types such as physical/digital/social/institutional distinctions, role markers, and additional state/viewpoint systems. Preserve them as speculative design ideas only. They require independent future stress-test pressure before any Pictiq implementation.
