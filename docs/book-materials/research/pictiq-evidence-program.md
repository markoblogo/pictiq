# Pictiq Evidence Program

> Status: central research-planning document
> Source event: Pictiq Research Foundations — Batch 03
> Rule: hypotheses and tests only; no normative language, grammar, vocabulary, Renderer, Composer, pack, profile, Entity Symbol, or release change implied.

## Purpose

Every important Pictiq claim should eventually map to:

```text
CLAIM
→ RISK / COUNTER-HYPOTHESIS
→ EVIDENCE REQUIRED
→ FALSIFICATION CONDITION
→ CHEAPEST USEFUL TEST
→ STRONGER TEST
→ CURRENT STATUS
```

Negative results are valuable. If labels outperform Pictiq, broad primitives create unacceptable disagreement, composition requires too much training, Context Packs duplicate too much vocabulary, Entity Symbols confuse users, or Pictiq adds no value over icons + text + structured data, preserve the result instead of redesigning the experiment after the fact.

## Baseline principle

Do not compare Pictiq only against nothing. Depending on the experiment, useful baselines include natural-language text, translated text, standard icons plus labels, emoji, controlled language, structured forms, and JSON/tool-call previews. Not every test needs every baseline, but benefit claims need a comparator.

## Initial claim registry

| Claim / hypothesis | Risk / counter-hypothesis | Evidence required | Falsification condition | Cheapest useful test | Stronger test | Current status |
| --- | --- | --- | --- | --- | --- | --- |
| Small Core remains usefully expressive. | Core is too small; users need many domain primitives. | Coverage and comprehension across tasks. | Frequent `GAP` for common low-risk tasks. | Composer-built scenario corpus scored with compression ledger. | Multi-domain human production/interpretation study. | PILOT_SUPPORTED |
| Composition is learnable. | Users memorize examples but cannot generalize. | Transfer to unseen compositions. | Learned users fail substitutions or reverse token relations. | Teach 5 rules; test unseen pairs/triples. | Cross-language longitudinal learning test. | UNTESTED |
| Visual symbols can support cross-language communication. | Users rely on labels/context; icons alone diverge. | Independent receiver success across language groups. | Text baseline consistently outperforms without Pictiq value. | Same scenarios with labels hidden/visible. | Cross-cultural comprehension study. | PARTIALLY_SUPPORTED |
| Broad primitives can remain useful without unacceptable ambiguity. | Polysemy produces disagreement. | Context-controlled reading convergence. | Readers choose incompatible actions in target context. | Test `surface_wavy`, `place_home`, `nature_cloud`. | Domain pack studies with real tasks. | PILOT_SUPPORTED |
| Context can safely carry some omitted information. | Context sufficiency collapses when message is forwarded or delayed. | Explicit context-dependency tests. | Receivers fail after context is reduced. | Show same message at location vs screenshot vs delayed. | Field-like study with staged context removal. | UNTESTED |
| Semantic-compression taxonomy is operationally usable. | Annotators disagree on `CONTEXT-SUFFICIENT`, `INTENTIONAL_OMISSION`, `LOSSY`, `GAP`. | Inter-annotator reliability. | Low agreement on common cases. | Two annotators score 04A cases. | Larger annotated corpus with adjudication. | UNTESTED |
| Digital Pictiq is machine-inspectable. | Machine readability is confused with vision. | Parser/Renderer/conformance tests. | Canonical IDs cannot be recovered from digital artifacts. | JSON/SVG round-trip checks. | Conformance suite across runtimes. | PILOT_SUPPORTED |
| Physical Pictiq may become vision-readable. | Human-friendly icons are not camera-robust. | Recognition benchmark and confidence policy. | Camera recovery fails under practical conditions. | Photograph controlled printed tiles. | Scan Profile study with error model. | DEFERRED |
| Context Packs extend Pictiq without destroying interoperability. | Packs fragment meanings or duplicate Core. | Versioned pack tests and compatibility checks. | Same ID means different things across packs. | Pack manifest review and conflict audit. | Multi-pack Composer validation study. | PARTIALLY_SUPPORTED |
| Entity Symbols provide useful scoped recurring reference. | Users confuse identity marks with lexical concepts. | Recognition, collision, and namespace tests. | Entity marks read as concepts or wrong people. | Odyssey entity recall test. | Narrative study with first mention/reinforcement. | PILOT_SUPPORTED |
| Pictiq can support accessibility when alternate channels are included. | Visual layer excludes users or hides meaning. | Keyboard/text/speech/accessibility evaluation. | Meaning inaccessible without vision. | Composer accessibility smoke review. | Formal assistive-tech testing. | SCOPE_LIMITED |
| Pictiq can support bounded low-risk humanitarian/public-service communication. | Users infer unsafe medical/legal meaning. | Professional boundary and escalation tests. | False action in high-risk context. | Low-risk wayfinding/needs test with `PROFESSIONAL_ONLY` labels. | Expert-reviewed field pilot. | DEFERRED |
| Pictiq can be useful as inspectable action representation. | Structured forms/tool previews are clearer. | Action Receipt tests vs JSON/form/text. | Users approve wrong action more often than baseline. | Mock send/delete/publish confirmations. | Real system sandbox with permission checks. | UNTESTED |
| Pictiq supports constrained visual writing/narrative. | It only decorates text and cannot carry story. | Reader reconstruction, memory, and production tests. | Readers cannot track entities/events beyond labels. | Short Odyssey retelling with entity symbols. | Children/adult narrative study. | PILOT_SUPPORTED |
| Pictiq provides measurable value beyond icons + labels + structured data. | It adds complexity with no measurable gain. | Comparator experiments. | No gain in speed, accuracy, confidence calibration, recall, or auditability. | A/B small tasks: labels vs Pictiq vs form. | Domain-specific randomized studies. | UNTESTED |

## Near-term priority after Composer / 04B

1. Grammar intuition / compositional learnability.
2. Cross-cultural Core recognition and interpretation.
3. Polysemy / broad primitive recovery.
4. Context sufficiency under reduced context.
5. Compression taxonomy reliability.

Do not run these experiments as part of this document.
