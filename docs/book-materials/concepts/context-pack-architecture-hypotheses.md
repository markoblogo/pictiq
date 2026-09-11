# Context Pack Architecture Hypotheses

> Status: architecture hypothesis / future implementation note
> Source input: [`../research/inputs/perplexity-2026-09/context-pack-extensibility-architecture.md`](../research/inputs/perplexity-2026-09/context-pack-extensibility-architecture.md)
> Rule: no manifest, governance tier, namespace, vocabulary, or validation behavior is implemented here.

## Layered model

CORE -> CONTEXT PACK -> PROFILE / REFERENCE SET -> LOCALE / PRESENTATION.

Working rule:

> Core defines general composition. Context Packs provide domain vocabulary and conventions. Profiles select or constrain what is appropriate for a specific task. Locales determine labels and presentation without changing semantic identity.

## Layer distinctions

| Layer | Role | Pictiq implication |
| --- | --- | --- |
| Core | Stable general primitives, grammar, Message representation, rendering assumptions, compatibility. | Keep small and interoperable. Promote only when evidence crosses unrelated contexts. |
| Context Pack | Domain vocabulary, conventions, examples, anti-patterns, domain-specific interpretation. | Road, medical, travel, Odyssey, maritime, retail, or education packs can add specificity without redefining Core. |
| Profile / reference set | Task-specific selection or constraint from Core plus packs. | A “tourist emergency card” profile can select a safer subset than a broad travel pack. |
| Locale / presentation | Labels, languages, local conventions, speech output, formatting. | Ukrainian/French/English labels should not create new semantic IDs by themselves. |

## Near-term principle

Complexity belongs to the context that requires it, not to Core.

A concept should generally stay in a Context Pack when it is domain-specific, geographic, institutional, workflow-specific, culturally local, or expressible compositionally but useful as domain shorthand.

A concept becomes a Core candidate only when evidence shows repeated need across unrelated contexts, poor compositional replacement, high combinatorial value, broad cultural usability, stable semantics, and long-term compatibility value.

## Semantic stability

Published semantic IDs should not be silently repurposed. If meaning changes materially:

1. introduce a preferred replacement;
2. preserve compatibility/deprecation metadata;
3. do not silently reinterpret historical messages.

This aligns with existing v1.1.0 compatibility behavior such as `need_bar` -> `drink_alcohol` and `place_hotel` -> `place_home`. This note does not change compatibility behavior.

## Future machine-readable Context Pack manifest

A minimal manifest may become useful later, especially after Composer and public surfaces. Potential fields:

- pack ID;
- version;
- status;
- compatible Pictiq version;
- concepts;
- dependencies;
- locales;
- license.

Do not implement this manifest until there is actual pack complexity and validation pressure.

## Governance boundary

The source proposes sophisticated governance: authority levels, official/certified/community/private tiers, semantic-version dependencies, certification, public registries, and promotion pipelines. Preserve these as future design options. Pictiq is not yet large enough to justify standards-body bureaucracy.
