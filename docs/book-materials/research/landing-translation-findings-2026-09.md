# Landing translation findings — 2026-09

> Status: accepted research and book-material record; the Pictiq landing translation itself remains unimplemented.

## Source and pressure

The first complete manual semantic pass over the accepted English landing established `ENGLISH_SOURCE_BASELINE_V0_1`. It tested the question: **Can Pictiq explain Pictiq?** The review found that many explanatory phrases are rhetorical, redundant, or recoverable from context. A Pictiq mode should therefore be substantially shorter than English mode and preserve communicative intent rather than source wording.

Three concepts created genuine Core pressure across the landing rather than a website-only gap:

- `action_combine` — combine, join, compose, assemble;
- `action_learn` — learn, study, practice, train;
- `action_write` — the action of creating written information, distinct from `media_text` as the text object or result.

They passed NEED-BEFORE-VOCABULARY after existing composition, context, polysemy, and omission were insufficient. No other landing pressure justified a new primitive in this pass. Machine/Computer, Browser, Workspace, Project, System, Symbol, New, Archive, Video, and IT/Server remain deferred. Protocol can be handled contextually through INFORMATION where appropriate; Experiment can use existing CHANGE/cycle semantics where useful.

## Communication principles

The normative protocol now records:

1. **MEANING-BEFORE-WORDING** — preserve communicative meaning, not every source word or rhetorical layer.
2. **PRIORITY-FIRST COMMUNICATION** — lead with the highest-priority actionable intent; add background only when needed.
3. **FUNCTIONAL SUFFICIENCY** — stop when the receiver has enough meaning to respond or act appropriately.

Their compact relationship is: `Meaning before wording. Priority before background. Sufficiency before completeness.` These principles connect to the existing semantic-compression states. `INTENTIONAL_OMISSION` can preserve functional sufficiency and is not automatically `LOSSY`; `LOSSY` marks a meaningful missing distinction, while `GAP` marks a currently inadequate representational capacity.

Practical examples retained for future writing:

- `TOILET + punct_question` can be enough to get directions; apology, travel history, and politeness need not be encoded first.
- Start with `NEED + WATER`. Add identity, quantity, payment, reason, or other context only if the receiver asks or the task requires it.

This is progressive practical communication, not a claim that literary translation should discard narrative structure. Literary and poetic translation remains a separate boundary research track. In an Odyssey-like narrative, source order may remain relevant; in a live help request, `NEED WATER` may be the right first message.

Shorter goal-first messages may reduce decoding burden for a receiver with no prior Pictiq training. That is a design hypothesis, not human evidence.

## Deferred hypotheses and candidates

The short/long/high/low arrow notation idea remains a `DEFERRED NOTATION HYPOTHESIS`; current landing work can use `SMALL + COMMUNICATION` for short messages. Entity-symbol pressure was observed for Composer, GitHub, English/England, PDF, EPUB, Medium, and Substack. These are candidates for a dedicated Entity Symbol pass, not additions here.

The landing translation/deployment remains `PUBLICATION MILESTONE CANDIDATE`, with the possible angle **Can a Visual Language Explain Itself?** It is not READY and no translation layer is implemented.

