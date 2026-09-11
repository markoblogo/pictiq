# IR Comparator Note for Pictiq

> Status: comparative research note
> Source event: Pictiq Research Foundations — Batch 02
> Rule: comparisons only; not accepted Pictiq architecture.

| System | Problem it solves | Human readability | Machine precision | Useful Pictiq analogy | Where analogy breaks |
| --- | --- | --- | --- | --- | --- |
| Semantic frames / FrameNet | Represents recurring situations and participant roles. | Moderate when labels are explained. | Strong when frames/roles are formalized. | Useful for future stress-test ledgers and domain schemas. | Pictiq v0.1 has flat frames, not role graphs. |
| AMR | Encodes sentence meaning as a graph for NLP. | Low for ordinary users. | Strong for computational semantics. | Useful as a warning that meaning graphs need strict conventions. | Pictiq is visual and user-facing; it should not claim full sentence semantics. |
| Intent + slots | Captures operational user intent and required values. | Moderate; often explainable in UI. | Strong inside bounded domains. | Closest analogy for action preview / Action Receipt. | Slots are domain-specific; Pictiq should not hide missing required values. |
| Controlled natural language | Reduces ambiguity while remaining text-readable. | High for trained readers. | Medium to strong depending on parser. | Good model for constrained authoring and repair prompts. | Pictiq is not text; visual ambiguity and icon recognition add different risks. |
| PDDL / planning languages | Represents states, actions, preconditions, effects. | Low outside technical users. | Strong for planning engines. | Useful for “show plan, do not execute plan” boundaries. | Pictiq should not become an execution planner. |
| Tool-call schemas | Defines exact function, arguments, validation, execution contract. | Low to moderate; usually needs UI summary. | Strong. | Pictiq can summarize the intended action before confirmation. | The schema, not Pictiq, owns execution authority. |
| KQML / FIPA-style agent communication | Structures communicative acts between agents. | Low for non-specialists. | Strong in agent systems. | Reminds Pictiq that “ask/tell/confirm/warn” may matter in future interfaces. | Current grammar has no performative layer. |
| Constrained DSLs | Makes a narrow task precise and executable. | Varies. | Strong inside domain. | Context Packs may eventually resemble small constrained DSLs. | This is future pressure, not a reason to redesign Core now. |
