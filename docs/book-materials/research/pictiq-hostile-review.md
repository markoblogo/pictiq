# Pictiq Hostile Review — Research Design Checks

> Status: critical research note
> Source event: Pictiq Research Foundations — Batch 03
> Rule: designed to make weak claims falsifiable, not to defend Pictiq.

## Five cross-cutting risks

| Risk | Meaning | Research-design check |
| --- | --- | --- |
| `AUTHOR_CONTEXT_BIAS` | The creator knows the intended meaning and sees information an independent reader cannot recover. | Use independent encoders, independent receivers, hidden targets, fixed corpora, and predeclared scoring. |
| `RECOGNITION_INTERPRETATION_CONFUSION` | Naming an icon is mistaken for knowing what action/message it implies. | Measure recognition, interpretation, action choice, confidence, and repair separately. |
| `HUMAN_MACHINE_READABILITY_CONFLATION` | Digital semantic-native parsing is confused with camera recognition of physical icons. | Separate Level 1 visual, Level 2 semantic-native, and Level 3 vision-robust claims. |
| `SCOPE_INFLATION` | Success in low-risk scenarios is generalized to medical, legal, logistics, identity, or safety authority. | Mark `PROFESSIONAL_ONLY`, linked-data needs, and authoritative-system boundaries. |
| `GOVERNANCE_OPTIMISM` | Context Packs, Entity Symbols, aliases, and compatibility are assumed to stay clean without tests. | Add collision checks, versioning rules, deprecation tests, and pack conflict audits. |

## Falsification posture

The project should welcome negative results. Evidence that Pictiq fails in a domain can still improve the system by narrowing claims, defining fallback paths, or showing that text, labels, forms, or professional mediation are better.

## Immediate experiment pressure

After Composer v0.1 and Stress Test 04B, the first high-value tests should check whether humans can build and read unseen compositions, whether broad primitives converge in context, whether context sufficiency survives forwarding/delay, and whether Pictiq outperforms or complements icons plus labels.
