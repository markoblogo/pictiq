# Identity-neutral substrate

> Status: book-material concept note  
> Source: Perplexity inclusive-design inputs archived under `../research/inputs/perplexity-2026-09/`  
> Rule: this note records an architectural interpretation. It is not a normative protocol change.

## Core idea

Pictiq does not encode identity categories by default. It encodes useful facts, needs, relationships, entities, and actions, then preserves additional distinctions only when they are materially required for the intended meaning, decision, or action.

This is stronger and safer than saying Pictiq must never represent gender, age, disability, nationality, relationship status, or other identity-linked categories. Some medical, demographic, legal, educational, narrative, or accessibility contexts may genuinely require such distinctions. The architectural point is that those distinctions should belong to the context that requires them, not to general Core by default.

## Already-supported architecture

The current repository already supports this direction independently of the supplied manifesto material:

- `person_generic` is a neutral human participant, not a man/woman split.
- [Structural gender neutrality](../../../spec/PROTOCOL.md#structural-gender-neutrality) rejects default Core distinctions for man/woman, he/she, son/daughter, and husband/wife solely because a source language encodes them.
- [Entity Symbols](entity-symbols.md) identify named people, narrative figures, and other scoped entities without making their identity attributes lexical semantics.
- [Vocabulary architecture](vocabulary-architecture.md) separates Core, Standalone Core, contextual vocabulary, specialized vocabulary, mechanisms, and the entity registry.
- [Numeric notation](../../../spec/NUMERIC_NOTATION.md) can express exact numbers where needed; it is separate from pragmatic quantity tiles.
- [Odyssey Stress Test 03 Stage 1](../../research/odyssey-toki-pona-pictiq-stress-test-03-stage-1.md) records structural gender neutrality, relationship composition, entity-symbol pressure, and intentional omission as narrative architecture findings.

## Fact vs identity distinction

| Area | Current classification | Careful treatment |
| --- | --- | --- |
| Gender | Already supported for general Pictiq. | General `person_generic` stays neutral. Specialized contexts may encode gender only when the distinction changes the required meaning, decision, or action. |
| Marital / relationship status | Useful design hypothesis with partial support. | `love_heart + person_generic` can express a loved person in context, but it is not a universal replacement for legal spouse, parent, kinship, custody, emergency-contact, or inheritance semantics. |
| Family | Strong concept, domain-dependent. | Prefer composition over one fixed nuclear-family pictogram. Exact kinship may matter in legal, medical, school, or family-services contexts. |
| Race / ethnicity | Strong omission hypothesis, verification required. | Do not add broad visual race/ethnicity icons to Core. Do not claim Pictiq has solved race representation. Some demographic or anti-discrimination contexts may require carefully governed textual or structured metadata outside ordinary icons. |
| Nationality / citizenship | Useful design hypothesis, not fully implemented. | Citizenship, birthplace, language, residence, and cultural origin are different facts. Pictiq currently has no complete formal model for all of them; named countries/places may use Entity Symbols where appropriate. |
| Disability | Strong concept, domain-dependent. | Functional-need-first is promising. Do not claim disability identity language is invalid. Accessibility, medical, legal, and community contexts may need identity-aware distinctions. |
| Age | Useful hypothesis, domain-dependent. | Exact age can be represented through numeric notation when implemented broadly. Qualitative age concepts such as child, adult, older person, or senior may still be useful in specific safety, legal, medical, or service contexts. |

## Inclusive design as an emergent property

Pictiq's inclusive-design value is not an extra feature layered on top of the protocol. It can emerge from the existing engineering pattern:

- small Core vocabulary;
- composition rather than categorical icon proliferation;
- context-sensitive precision;
- scoped Entity Symbols;
- separation between general vocabulary and specialized packs.

This combination can reduce the number of assumptions the protocol makes about the user. That is a book-material finding, not a marketing proof.

## Boundaries

Do not turn this note into an absolute rule. Pictiq should avoid default identity categories where they are not needed, while preserving the ability to encode precise distinctions in the context that genuinely requires them.

Do not import competitive claims such as “the only visual language without identity categories” without a dedicated comparative verification pass.
