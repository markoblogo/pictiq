# Semantic Compression Framework

> Status: research framework / book-material seed
> Source event: Pictiq Research Foundations — Batch 02
> Scope: annotation and evaluation method only; no Message Schema, grammar, vocabulary, Renderer, Composer, profile, pack, or Entity Symbol change implied.

## Central question

Pictiq translation quality should not be judged mainly by lexical or sentence-level equivalence. The useful question is:

> Does the Pictiq representation preserve the distinctions needed for the receiver's correct action, decision, understanding, or safe interpretation in the stated task/context?

This makes adequacy task-dependent. The same short Pictiq sequence can be sufficient at a help desk and dangerously underspecified in a medical, legal, financial, or execution context.

## Task-faithful compression

Working book-draft formulation:

> Preserve what changes the receiver's correct action, decision, safety, rights, or interpretation. Compress redundancy. Intentionally omit what is irrelevant or harmful to expose. Mark meaningful loss. Surface a gap when Pictiq cannot carry a necessary distinction.

This is **task-faithful compression**, not lossless translation.

## Six-state preservation taxonomy

These labels are research annotations. They are not grammar operators and do not require Message Schema changes.

| State | Meaning | Typical repair if inadequate |
| --- | --- | --- |
| `PRESERVED_EXPLICITLY` | Meaning is directly represented by current Pictiq tokens or notation. | None. |
| `PRESERVED_BY_COMPOSITION` | Meaning is represented by regular composition of existing concepts rather than by a dedicated primitive. | Document composition; test comprehension. |
| `CONTEXT-SUFFICIENT` | Meaning is absent from the explicit message but reliably recoverable from actual shared context. | Name the context dependency; avoid using this as a vague excuse. |
| `INTENTIONAL_OMISSION` | Meaning is deliberately excluded because it is irrelevant, redundant, private, culturally nonportable, or inappropriate for the task. | Record the omission reason. |
| `LOSSY` | A meaningful distinction is absent and cannot reliably be reconstructed. | Add text, linked data, domain schema, or a richer Pictiq expression. |
| `GAP` | Current Pictiq vocabulary, grammar, notation, or context cannot adequately express a needed distinction. | Consider composition, Context Pack concept, future grammar pressure, or fallback. |

## Four often-confused states

`CONTEXT-SUFFICIENT` means the information is absent but the receiver can recover it from a concrete shared situation.

`INTENTIONAL_OMISSION` means the information is absent because the receiver does not need it or it should not be exposed.

`LOSSY` means the information is absent even though it may affect interpretation, decision, or future reuse.

`GAP` means the needed distinction cannot currently be represented adequately.

## Context dependency checklist

A `CONTEXT-SUFFICIENT` claim should name the context that makes the message sufficient. Examples:

- physical location;
- visible object;
- current UI screen;
- prior conversation;
- known participant;
- established task;
- Context Pack;
- trained procedure;
- current workflow state.

A Context Pack is not the same thing as common ground. It can constrain vocabulary and conventions, but it does not prove that a receiver knows the situation, task, or intended action.

## Pictiq Compression Ledger

A future experiment ledger may record semantic adequacy without changing Message Schema v0.1:

| Field | Purpose |
| --- | --- |
| source | Original sentence, screen, sign, workflow, or scenario. |
| task | What the receiver must decide, do, understand, or avoid. |
| context | Shared environment and assumptions that are explicitly allowed. |
| Pictiq version / Message Schema version | Reproducibility. |
| Pictiq output | Canonical Message JSON, shorthand, or rendered sequence. |
| required semantic slots | What must survive for this task. |
| preserved explicitly | Current tokens/notation that directly carry meaning. |
| preserved by composition | Regular compositions that carry meaning. |
| context-sufficient details | Recoverable details and the context that recovers them. |
| intentional omissions | Omitted details plus reason. |
| lossy details | Missing distinctions that matter. |
| gaps | Missing Pictiq capacity. |
| impact/risk | Consequence of wrong interpretation. |
| repair/fallback | Text, speech, linked data, professional, schema, or future vocabulary path. |
| execution suitability | Whether the representation can preview, support, or authorize an action. |

This connects to the semantic-slot method used in Stress Test 04A while preserving the accepted flat Message model: document → frames → flat ordered tokens.

## Orthogonal safety / authority annotation

Semantic preservation asks: **what meaning was preserved?**

Professional or safety authority asks: **can this visual representation be authoritative for this task?**

Use a separate annotation such as `PROFESSIONAL_ONLY` when a Pictiq representation may communicate a gist but must not carry legal, medical, humanitarian, financial, or destructive authority by itself.

Example: a sequence may express “I agree to treatment,” but it cannot establish informed consent. Consent requires process, comprehension, authority, records, and professional safeguards beyond the visual message.
