# Perplexity inclusive-design and use-cases harvest — 2026-09

> Status: critical research harvest  
> Inputs: archived under [`inputs/perplexity-2026-09/`](inputs/perplexity-2026-09/)  
> Rule: the supplied Perplexity materials are idea sources, not authoritative Pictiq specification.

## Input archive

| Archived input | SHA-256 |
| --- | --- |
| [`where-pictiq-is-especially-useful-ru.md`](inputs/perplexity-2026-09/where-pictiq-is-especially-useful-ru.md) | `acf69cb5ce910d826019c9eca08041a00411896611479d7ea75ec2a7601e8b46` |
| [`inclusive-design-manifesto-ru.md`](inputs/perplexity-2026-09/inclusive-design-manifesto-ru.md) | `4555b37637891b64ce826a307d947f6fc3e616e90576580d567ea186410c8492` |
| [`inclusive-design-manifesto-en.md`](inputs/perplexity-2026-09/inclusive-design-manifesto-en.md) | `90d6fd1dff08761c31fb362af9876773cb9d2eb9aad88448c549de5a68100f2c` |

## Critical harvest table

| Idea | Class | Source file | Relation to current architecture | Repository evidence | External verification | Recommended treatment | Future book/article use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Pictiq encodes useful facts, needs, relationships, actions, and scoped entities rather than default identity categories. | STRONG CONCEPT | all three | Matches structural gender neutrality, Entity Symbols, context packs, and “distinction required for the decision.” | `spec/PROTOCOL.md`, Odyssey Stage 1, `entity-symbols.md`, `vocabulary-architecture.md` | Needed before broad historical/social claims. | Preserve as `identity-neutral-substrate.md`; do not make a new normative rule here. | Strong architecture/book chapter. |
| Inclusive design can emerge from small Core + composition + contextual extension. | STRONG CONCEPT | manifestos | Fits current vocabulary architecture without adding icons. | `spec/VOCABULARY_CLASSIFICATION.md`, `lexicon/vocabulary-classification.json` | No external claim required for internal architecture; external impact claims need testing. | Use as book-material framing. | Good essay thesis. |
| Gender-neutral `person_generic` is preferable to default man/woman in general Pictiq. | ALREADY SUPPORTED | manifestos/use-case doc | Already normative for general Pictiq. | `spec/PROTOCOL.md#structural-gender-neutrality`, Odyssey Stage 1 | External signage debate claims need verification. | Keep as supported principle, with domain-dependent caveat. | Strong example. |
| Loved-person composition can avoid default spouse/status assumptions. | EXPERIMENT CANDIDATE | use-case doc/manifestos | Partially aligned with composition, but current grammar does not formalize every relationship role. | `love_heart`, grammar adjacency, Odyssey Stage 1 | Relationship/legal/family use cases need domain review. | Treat as contextual composition, not universal replacement. | Useful cautionary example. |
| Family should be composed rather than represented by a fixed nuclear-family pictogram. | STRONG CONCEPT | use-case doc/manifestos | Consistent with composition and avoiding category proliferation. | Grammar and vocabulary architecture | Family-pictogram exclusion claims need sources. | Preserve as design hypothesis. | Strong public-facing idea with verification. |
| Race/ethnicity should not be ordinary visual Core categories. | STRONG CONCEPT | use-case doc/manifestos | Fits identity-neutral substrate. | No current race/ethnicity icons; context-pack principle. | Emoji/Unicode and signage claims need verification. | Keep as omission hypothesis; allow specialized contexts. | Use only with careful citations. |
| Citizenship, birthplace, origin, nationality, language, and residence are different facts. | EXPERIMENT CANDIDATE | use-case doc/manifestos | Entity Symbols may support named places/countries, but Pictiq lacks a formal fact model here. | Entity Symbols, numeric/context mechanisms | Legal/public-service semantics need verification. | Add to future Core/profile audit questions. | Good systems-design section. |
| Functional need may be better than a broad disability label in situational communication. | STRONG CONCEPT | manifestos/use-case doc | Fits practical-need design and Standalone/Embodied decision logic. | `need_*`, `safety_*`, protocol decision tree | Accessible Icon Project and AAC ethics claims need verification. | Treat as experiment direction, not anti-disability-language claim. | Strong but sensitive book material. |
| Exact age can use numeric notation instead of old/young labels. | EXPERIMENT CANDIDATE | manifestos/use-case doc | Numeric notation exists partially; broad digits are not complete. | `spec/NUMERIC_NOTATION.md` | Age-label/ageism claims need verification. | Preserve as hypothesis; do not ban age-category vocabulary. | Good mechanism example. |
| Humanitarian / crisis response pack. | EXPERIMENT CANDIDATE | use-case doc | Context-pack architecture can support it. | Road stress test, packs model | ICOON/OCHA claims need verification. | Candidate stress test, not roadmap. | Strong application case study. |
| Situational/out-of-home AAC support. | EXPERIMENT CANDIDATE | use-case doc | Fits short practical messages better than full everyday AAC. | Standalone profile, needs/safety icons, text-to-Pictiq prototype note | ARASAAC, PECS, Stroke Association, regulation, ethics need verification. | Explore with specialist input. | Strong ethical-boundary section. |
| Multilingual workplace safety training, not replacement of ISO/GHS signage. | STRONG CONCEPT | use-case doc | Fits context pack around existing standards, not replacement. | Road stress test; “design for decision” | ISO/GHS/training claims need verification. | Research candidate; avoid compliance claims. | Good practical example. |
| Maritime/logistics language-barrier support. | EXPERIMENT CANDIDATE | use-case doc | Fits emergency/bilingual operational instruction stress test. | `move_watercraft`, road/narrative stress-test evidence | Maritime literature and existing signal systems need verification. | Research lead; potentially valuable stress test. | Interesting niche chapter. |
| Pictiq is the first/only visual language with real grammar. | REJECT / DO NOT IMPORT | use-case doc | Too broad and competitive. | Current repo proves Pictiq has grammar, not uniqueness. | Dedicated comparative pass required. | Do not use as claim. | Maybe research question only. |
| All existing pictographic systems are static flat dictionaries. | REJECT / DO NOT IMPORT | use-case doc | Overbroad; PECS has a formal interaction protocol and other systems may have syntax-like behavior. | Prior precedent harvest already cautions against this. | Comparative verification required. | Replace with narrower wording. | Use as “too-strong draft” example. |
| Market-size and “worldwide/de facto standard” claims. | VERIFICATION REQUIRED | use-case doc | Commercial evidence does not affect current architecture. | None in repo. | Primary/strong independent sources required. | Keep in verification backlog only. | Not book-safe now. |

## Strongest harvested finding

The strongest idea is the identity-neutral substrate: Pictiq's current architecture already tends to encode action-relevant facts and needs rather than identity categories by default. This connects directly to Odyssey Stage 1 gender neutrality and the Entity Symbol strategy.

## Major cautions

- Do not rewrite `PROTOCOL.md` from manifesto prose.
- Do not add identity-category bans.
- Do not use “first,” “only,” “all competitors,” or market-size claims without verification.
- Do not position Pictiq as a replacement for mature AAC systems.
- Do not imply Pictiq can replace regulated signs, interpreters, or legal accommodations.

## Connection to Odyssey

Odyssey Stress Test 03 already supplied independent evidence for structural gender neutrality, intentional omission, entity symbols, relationship composition, and context-specific vocabulary growth. The Perplexity material is useful because it names a broader pattern behind those decisions, not because it proves them.

## Connection to future Core audit

The future Core/Profile audit should ask whether candidate identity-linked concepts are genuinely required for general Core, or whether they belong to context packs, Entity Symbols, numeric notation, labels, or external metadata.
