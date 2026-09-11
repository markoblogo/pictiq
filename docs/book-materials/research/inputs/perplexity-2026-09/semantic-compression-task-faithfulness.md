Semantic compression is not simply “saying less.” It is a deliberate transformation that retains the distinctions needed for a defined task while reducing or discarding surface wording, redundancy, detail, and sometimes recoverable nuance. For Pictiq, the central question is therefore not whether a message is lossless compared with English or French, but whether it is **sufficiently faithful for the user’s next decision, action, or understanding**.

That aligns well with Pictiq’s existing categories. `CONTEXT-SUFFICIENT` should mean that the compressed representation preserves everything needed in the current shared situation; `INTENTIONAL_OMISSION` should mark details knowingly excluded because they are irrelevant or recoverable; `LOSSY` should mark meaningful detail that has been discarded; and `GAP` should identify meaning the system cannot currently express clearly enough.

## **Semantic compression model**

Classical lossy compression asks how much a signal can be reduced while keeping reconstruction error below a tolerated threshold. Rate–distortion theory formalizes the trade-off between the rate of information transmitted and permitted reconstruction distortion.\[[pmc.ncbi.nlm.nih](https://pmc.ncbi.nlm.nih.gov/articles/PMC12385448/)\]\[[en.wikipedia](https://en.wikipedia.org/wiki/Rate%E2%80%93distortion_theory)\]

Semantic or task-oriented compression changes the fidelity target. Instead of reconstructing the original sentence exactly, the receiver needs enough information to accomplish a task. Research in task-specific semantic compression describes this as transmitting task-relevant semantic information while removing redundancy; acceptable distortion depends on the downstream task and the side information shared by sender and receiver.\[[arxiv](https://arxiv.org/html/2306.02305v1)\]\[[mdpi](https://www.mdpi.com/1099-4300/28/6/593)\]

A useful Pictiq formulation is:

\\text{Adequate Pictiq message}  
\=  
\\text{task-relevant meaning preserved}  
\+  
\\text{shared context available}  
\-  
\\text{unacceptable decision risk}.

Or more explicitly:

\\operatorname{Adequate}(M, T, C)  
\\iff  
\\operatorname{Outcome}(M, T, C)  
\\approx  
\\operatorname{Outcome}(S, T, C),

where:

* `S` is the source utterance or original state.  
* `M` is the Pictiq representation.  
* `T` is the receiver’s task.  
* `C` is available shared context: place, time, prior conversation, interface state, known roles, pack, data source, and social conventions.

The key implication: the same Pictiq sequence can be sufficient in one context and dangerously incomplete in another.

\[WATER\] \[NOW\]

At a café:  
“I would like water now.” — usually sufficient.

During a heat incident:  
“Drink water now.” — may be sufficient as a first instruction,  
but not as a complete emergency message.

In a hospital:  
“Administer water now.” — unsafe and radically under-specified.

In irrigation control:  
“Start water flow now.” — requires target field, quantity,  
duration, source, permissions, and confirmation.

The visible symbols may not change. The acceptable level of compression does.

## **What gets preserved or removed**

Semantic compression does not operate on one single “meaning” layer. It selectively preserves some dimensions and weakens, omits, or loses others.

| Meaning dimension | What it contains | Example in full language | Possible Pictiq treatment | Risk if omitted |
| ----- | ----- | ----- | ----- | ----- |
| Core event or state | What happened, exists, changes, or is needed | “The train is cancelled.” | TRAIN \+ CANCELLED | Usually essential |
| Communicative intent | Ask, inform, command, warn, offer, refuse, confirm | “Could you please…” | ASK, REQUEST, INFORM, WARN, CONFIRM | High; statement vs. request can reverse the action |
| Participants and roles | Who acts, receives, owns, benefits, or is affected | “The driver must call the dispatcher.” | DRIVER \+ MUST \+ CALL \+ DISPATCHER | Often essential |
| Object or topic | What the message concerns | “Deliver the wheat.” | DELIVER \+ WHEAT | Usually essential |
| Time | When, duration, deadline, sequence, recurrence | “Before 16:00 tomorrow.” | BEFORE \+ TIME \+ TOMORROW | Often essential for coordination |
| Place | Location, route, origin, destination, spatial relation | “At silo 3, then to Nantes.” | AT \+ SILO-3 \+ TO \+ NANTES | Essential in logistics, travel, emergency response |
| Quantity and unit | Number, measurement, currency, threshold, range | “40 tonnes at €220/t.” | 40 \+ TONNE \+ PRICE \+ €220/T | Essential for trade, dosage, inventory, billing |
| Polarity | Negation, prohibition, absence, failure | “Do not enter.” | NOT \+ ENTER | Frequently safety-critical |
| Modality | Need, permission, ability, obligation, probability | “You may enter”; “You must stop.” | MAY, MUST, NEED, CAN | High; “can” and “must” are not interchangeable |
| Condition and consequence | If, unless, because, then, exception | “If frost occurs, delay harvest.” | IF \+ FROST \+ THEN \+ DELAY \+ HARVEST | Essential in policies, plans, alerts |
| Status and completion | Planned, active, completed, failed, paused, unknown | “The booking was confirmed.” | BOOKING \+ CONFIRMED | Often essential |
| Evidence and source | Who observed it, data origin, provenance, confidence | “According to sensor A…” | SOURCE \+ SENSOR-A \+ CONFIDENCE | Important for decisions, auditability, trust |
| Uncertainty | Estimate, forecast, confidence range, rumor, possibility | “Rain is likely, not certain.” | MAYBE / LIKELY \+ RAIN | Critical for forecasts and recommendations |
| Causal explanation | Why an event occurred | “Prices rose due to port delays.” | PRICE \+ UP \+ CAUSE \+ PORT \+ DELAY | Often useful, but can be optional |
| Social tone | Courtesy, warmth, deference, irony, formality | “Would you mind terribly…” | Normally omitted | Often low operational risk; high relational effect |
| Rhetorical style | Emphasis, metaphor, humor, cadence, narrative voice | “Prices caught fire.” | PRICE \+ UP / HOT | Usually intentionally omitted |
| Identity and personal detail | Gender, ethnicity, status, intimate facts, individual labels | “A female customer…” | Omit unless functionally necessary | Can protect privacy and reduce bias |
| Cultural reference | Local allusion, idiom, shared media, etiquette | “It’s a Parisian rush-hour nightmare.” | TRAFFIC \+ CROWDED \+ DELAY | Usually omitted, sometimes creates loss of tone |
| Exact wording | Syntax, word order, grammatical tense, lexical choice | “I was hoping you could…” | Normalize to intent and roles | Usually nonessential unless quotation/legal record matters |

A Pictiq message is good semantic compression when it retains the rows that govern the receiver’s correct response and deliberately reduces those that do not.

## **Four outcomes of compression**

Your existing categories can become a rigorous classification system by distinguishing *why* a detail is absent and whether its absence changes the task outcome.

### **`CONTEXT-SUFFICIENT`**

A detail is absent from the symbols but reliably supplied by shared context. The omission is acceptable for the current task.

Pictiq:  
\[COFFEE\] \[PLEASE\]

Spoken source:  
“Could I have one espresso, please?”

Preserved:  
request, desired item, social intent.

Supplied by context:  
the café, one serving, order-taking interaction,  
the person addressed, payment procedure.

Compressed:  
formal politeness wording and syntax.

This is not necessarily lossless, but it is sufficient because the setting supplies the missing roles. The receiver can act correctly without asking a clarification question.

A formal test:

\\operatorname{Context\\text{-}Sufficient}  
\\iff  
P(\\text{correct task outcome} \\mid M, C)  
\\geq \\theta\_T

where `\theta_T` is the task’s required reliability threshold. Ordering coffee permits a lower threshold than authorizing a payment, delivering grain, or administering treatment.

**Pictiq design use:** mark `CONTEXT-SUFFICIENT` when the system intentionally relies on stable visible context—such as screen title, current form, user identity, map location, conversation turn, or a known work procedure.

{  
  "message": \["core:coffee", "core:request"\],  
  "classification": "CONTEXT-SUFFICIENT",  
  "context\_dependencies": \[  
    "venue:coffee-shop",  
    "interaction:ordering",  
    "default\_quantity:1",  
    "speaker:self"  
  \]  
}

The important addition is `context_dependencies`. A message should not be called context-sufficient without recording *which* context makes it sufficient.

### **`INTENTIONAL_OMISSION`**

A detail existed or could have been expressed, but is consciously excluded because it is irrelevant, redundant, private, culturally nonportable, or better left unspecified.

Source:  
“My elderly French neighbour, Madame Leclerc, is worried  
that the parcel may be late again because of the rail strike.”

Pictiq:  
\[PERSON\] \[WORRIED\] \[PARCEL\] \[LATE\]

Intentionally omitted:  
name, nationality, age, honorific, prior recurrence,  
speculative cause, interpersonal framing.

Intentional omission is a design choice, not a failure. It can improve:

* Brevity and scanability.  
* Cross-language portability.  
* Privacy and dignity.  
* Inclusivity, especially when identity labels are not relevant to the request.  
* Robustness against culturally specific idiom.  
* Cognitive load in constrained interfaces.

This fits Pictiq’s stated design direction of representing **facts and needs rather than unnecessary identity categories**. If the person’s identity is not functionally needed, omitting it is often an improvement, not a semantic defect.

However, intentional omission must remain reversible where it matters. A system should be able to preserve excluded details in an optional metadata or expanded text layer even when the visible Pictiq message leaves them out.

Visible:  
\[PERSON\] \[NEED\] \[HELP\] \[STAIRS\]

Expanded semantic record:  
requester: person-123  
mobility context: needs step-free route  
location: station entrance B  
time: now  
spoken-language preference: French

The visual layer omits personal detail; the structured layer retains necessary operational facts.

### **`LOSSY`**

The source meaning contains a task-relevant or potentially relevant distinction that Pictiq does not preserve. The resulting message may still be usable, but it cannot be assumed equivalent.

Source:  
“Please use the gluten-free preparation area because I have  
celiac disease; even trace contamination is unsafe.”

Over-compressed Pictiq:  
\[NO\] \[GLUTEN\]

Lost:  
reason, severity, cross-contamination constraint,  
required operational procedure, health risk.

`LOSSY` should not be a synonym for “short.” It means that a meaningful distinction is irrecoverably absent from the chosen representation.

The loss may be:

* **Benign:** “I’d really love some tea” → WANT \+ TEA. Intensity is lost, but usually harmless.  
* **Functional:** “Send the report before 16:00, not by the end of day” → SEND \+ REPORT \+ TODAY. Deadline precision is lost.  
* **Decision-changing:** “The price increased 3.7% versus yesterday’s close” → PRICE \+ UP. Magnitude and reference period are lost.  
* **Safety-critical:** “Do not give penicillin; prior anaphylaxis” → NO \+ MEDICINE. Drug identity and severe reaction are lost.

In Pictiq’s semantic model, a `LOSSY` mapping should ideally identify both what was dropped and the effect of the loss:

{  
  "classification": "LOSSY",  
  "preserved": \[  
    "allergen:gluten",  
    "polarity:avoid"  
  \],  
  "lost": \[  
    "medical:celiac-disease",  
    "risk:trace-contamination",  
    "required\_procedure:separate-preparation"  
  \],  
  "impact": "high",  
  "safe\_for\_execution": false,  
  "repair\_options": \[  
    "medical:celiac-disease",  
    "food:cross-contamination",  
    "core:must"  
  \]  
}

This turns lossiness into a measurable and repairable property rather than a vague warning.

### **`GAP`**

A `GAP` is not simply omitted information. It is a concept, relation, distinction, or operation that Pictiq cannot currently encode clearly and composably—or cannot encode without overloading a symbol beyond safety or usability.

Source:  
“The futures curve is in backwardation, but the nearby spread  
is narrowing because storage constraints are easing.”

Attempted Pictiq:  
\[FUTURES\] \[PRICE\] \[DOWN?\] \[STORAGE\] \[LESS?\]

Gap:  
No stable representation for:  
\- futures curve versus spot price,  
\- backwardation,  
\- nearby spread,  
\- causal relation,  
\- storage constraints,  
\- easing/narrowing as market-structure changes.

A gap can occur at several levels:

| Gap type | Description | Example |
| ----- | ----- | ----- |
| Lexical gap | Missing domain concept | Backwardation, vestibule, cross-contamination |
| Role gap | Available concepts, but no way to assign who did what to whom | “The broker advised the farmer” |
| Relation gap | Missing causal, temporal, comparative, or conditional relation | “Prices rose because shipping slowed” |
| Scope gap | No reliable way to show what negation, quantity, or modality applies to | “Do not alert every supplier” |
| Precision gap | No representation for exact measurement, unit, threshold, or range | 3.7%, €220/t, 10–15 minutes |
| Context gap | The decoder lacks the required shared background | A venue-specific shorthand outside the venue |
| Cultural gap | Symbol is not consistently recognized across target communities | Gesture/icon whose meaning differs by region |
| Governance gap | A needed concept exists in no approved Context Pack | New agricultural contract type |
| Safety gap | The system can render a simplification, but cannot do so safely | Medication dosage or emergency evacuation exception |

A `GAP` should trigger one of four responses:

1. Add a regular composition using existing core primitives.  
2. Add a domain concept in an appropriate Context Pack.  
3. Add a formal operator, role marker, or type rule to the grammar.  
4. Fall back to text, speech, linked metadata, or a specialist schema.

Do not automatically add a new primitive. In a minimal language, many gaps are better resolved by a reusable relation operator, measurement syntax, or pack-defined frame.

## **A preservation taxonomy**

A practical way to label each source-to-Pictiq transformation is to classify every meaning element into one of six states.

| State | Meaning | Recoverable? | Typical Pictiq handling | Example |
| ----- | ----- | ----- | ----- | ----- |
| `PRESERVED_EXPLICITLY` | Directly encoded in tiles or formal Pictiq structure | Yes | Tile, operator, typed value, relation | NOT \+ ENTER; 40 \+ TONNE |
| `PRESERVED_BY_COMPOSITION` | Not one tile, but recoverable from a regular combination | Yes | Core primitives \+ grammar | WATER \+ GROW \= irrigate |
| `CONTEXT-SUFFICIENT` | Not encoded, but reliably recoverable from declared context | Usually | Message plus known setting/profile | COFFEE \+ REQUEST in a café |
| `INTENTIONAL_OMISSION` | Excluded because it does not affect this task or should remain private | No from visible message; maybe from metadata | Omit; optionally retain in source record | Formal politeness, identity detail |
| `LOSSY` | Excluded despite affecting meaning, nuance, or potentially the task | No | Mark loss; warn or seek clarification | “likely” reduced to a plain weather event |
| `GAP` | Cannot be represented adequately with current vocabulary/grammar/context | No | Add pack/grammar/text fallback | Exact medication contraindication |

This taxonomy prevents a dangerous tendency in minimalist systems: calling every missing detail “context.” Context is legitimate only if the receiver can actually recover the meaning from shared, stable, declared information.

### **A stricter distinction**

CONTEXT-SUFFICIENT:  
The information is absent from the message,  
but the receiver can reliably recover it.

INTENTIONAL\_OMISSION:  
The information is absent because the receiver does not need it.

LOSSY:  
The information is absent even though it could affect interpretation,  
decision, relation, or future reuse.

GAP:  
The information cannot be expressed adequately in the current system.

## **Controlled language and semantic parsing**

Controlled natural languages reduce ambiguity and complexity by restricting vocabulary and grammar. Simplified Technical English, governed by ASD-STE100, uses controlled terminology and rules to support clearer technical documentation for international audiences.\[[ceur-ws](https://ceur-ws.org/Vol-3427/short2.pdf)\]\[[mastertcloc.unistra](https://mastertcloc.unistra.fr/2023/07/06/simplifying-the-complex-asd-ste100-simplified-technical-english/)\]

Its compression is selective:

* It removes lexical variation and stylistic flourish.  
* It reduces grammatical alternatives.  
* It prefers standardized technical terms.  
* It retains procedural actors, actions, conditions, warnings, and equipment references.  
* It intentionally makes text less literary to make it easier to interpret, translate, and execute.

Example:

Uncontrolled:  
“Once you have made sure the panel is properly secured,  
you may proceed to activate the unit.”

Controlled:  
“Make sure that the panel is secure.  
Then activate the unit.”

The reduced form preserves sequence, actor, condition, and action. It removes politeness, hedging, and rhetorical padding.

Pictiq can use the same principle:

Source:  
“After you have verified that the safety panel is secure,  
please start the pump.”

Pictiq:  
\[CHECK\] \[SAFETY\] \[PANEL\] \[SECURE\]  
\[THEN\] \[START\] \[PUMP\]

But to qualify as a robust controlled visual language, Pictiq must preserve:

* Whether the first clause is a **precondition** or merely advice.  
* Whether START is a request, command, permission, or report.  
* Which specific pump and panel are meant.  
* Whether “secure” means locked, closed, powered, intact, or safe-to-use.  
* Whether the operation needs an acknowledgment or verification record.

Semantic parsing makes the same move in software: it converts a natural-language utterance into a machine-understandable logical or structured representation. In task-oriented dialogue, that representation commonly begins as a semantic frame containing an intent plus slots, while more advanced formulations use hierarchical structures for compositional queries.\[[en.wikipedia](https://en.wikipedia.org/wiki/Semantic_parsing)\]\[[ai.meta](https://ai.meta.com/research/publications/semantic-parsing-for-task-oriented-dialog-using-hierarchical-representations/)\]\[[arxiv](https://arxiv.org/abs/1810.07942)\]

For Pictiq, the semantic parse should be the authoritative layer; the visible tiles should render it.

{  
  "intent": "request\_action",  
  "action": "industrial:start",  
  "target": "asset:pump-2",  
  "preconditions": \[  
    {  
      "predicate": "industrial:secure",  
      "target": "asset:safety-panel-2"  
    }  
  \],  
  "sequence": "after-precondition",  
  "actor": "operator:self",  
  "status": "draft"  
}

The Pictiq tiles offer an inspectable compression of that structure. They should not silently erase distinctions merely because they are inconvenient to draw.

## **Emergency communication as a compression benchmark**

Emergency messages are a valuable benchmark because they compress aggressively while preserving a small set of non-negotiable distinctions.

The Common Alerting Protocol, CAP, is a general, all-hazard format for exchanging alerts across networks and alerting systems. It provides categorical and textual descriptions and explicitly models urgency, severity, certainty, geographic targeting, and timing. CAP can also support multilingual and accessible communication across technologies.\[[docs.oasis-open](https://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2-os.html)\]\[[wmo](https://wmo.int/site/wmo-common-alerting-protocol/about-cap)\]

A complete emergency source record may be large:

Forecast source, sensor readings, forecast models, polygon geometry,  
incident command structure, update history, technical hazard details,  
weather history, evacuation logistics, resource allocation, legal authority.

But a public warning must preserve a constrained core:

Hazard:  
  What is happening?

Affected area:  
  Who and where is affected?

Time:  
  When does it apply?

Severity / urgency:  
  How serious and how soon?

Certainty:  
  Is this observed, likely, or possible?

Required action:  
  What should the recipient do?

Authority:  
  Who issued the warning?

A Pictiq emergency rendering might be:

\[WARN\]  
\[FLOOD\] \[PLACE:LOWER-LOIRE\]  
\[TIME:NOW–18:00\]  
\[SEVERE\] \[LIKELY\]  
\[GO\] \[TO\] \[HIGH-GROUND\]

This is effective only if the symbols preserve those distinctions. A short sequence such as `[FLOOD] [GO]` may be emotionally clear but operationally insufficient: go where, who should go, when, how urgent, and under whose authority?

Emergency communication therefore gives Pictiq a useful rule:

> The tighter the time pressure, the more aggressively compress wording—but the less acceptable it is to omit action-changing fields.

In high-risk profiles, Pictiq should label important missing fields as `GAP` or `LOSSY`, not excuse them as minimalism.

## **Minimalist languages and contextual economy**

Toki Pona demonstrates a different type of semantic compression: a very small vocabulary with broad roots and compositional expansion. Its minimal vocabulary makes interpretation heavily dependent on context. Speakers can preserve a broad conceptual direction with a single word, then refine it with additional words only when a distinction matters.\[[griffinbassett](https://griffinbassett.com/wp-content/uploads/2024/11/The-Pragmatics-of-Toki-Pona-Across-Variable-Native-Language-Backgrounds.pdf)\]

For example, an intentionally broad root can remain useful:

WATER

Potential readings:

water as substance  
drink water  
need water  
wet  
watering/irrigation  
water resource

A minimal system succeeds when it lets speakers add structure:

\[PERSON\] \[NEED\] \[WATER\]  
\[PLANT\] \[NEED\] \[WATER\]  
\[WATER\] \[TOO-MUCH\]  
\[START\] \[WATER\] \[FIELD\]  
\[WATER\] \[NOT\] \[SAFE\]

This does not make the broad primitive ambiguous in every case. It makes it **underspecified until composition and context resolve its role**.

The Pictiq implication is that small vocabulary is compatible with high semantic usefulness only if:

* Role grammar is strong.  
* Context Packs supply domain refinements.  
* Users can express distinctions when they become decision-relevant.  
* The system detects when composition is insufficient.  
* It never mistakes “a possible reading” for “a reliable reading.”

## **Human–computer interfaces: compression through progressive disclosure**

Interfaces also practice semantic compression. Progressive disclosure shows the essentials first and postpones advanced or infrequent information until it becomes relevant. The stated purpose is to reduce cognitive overload, improve ease of learning, and make complex systems less error-prone.\[[ixdf](https://ixdf.org/literature/book/the-glossary-of-human-computer-interaction/progressive-disclosure)\]

This is not merely hiding content. It preserves access to the full meaning while reducing what must be processed **now**.

For Pictiq, this suggests three related but distinct forms:

| Interface form | Visible Pictiq message | Hidden or deferred layer | Appropriate use |
| ----- | ----- | ----- | ----- |
| Compact visual summary | Core intent, object, status, action | Exact values, metadata, source, alternatives | Dashboard cards, checklists, messaging |
| Expandable semantic card | Tile sequence plus a short gloss | Roles, time, uncertainty, provenance, validation | Agent reviews, travel planning, field operations |
| Strict execution preview | Pictiq summary plus highlighted mandatory fields | Full JSON/schema record and audit history | Sending, purchasing, editing records, automation |
| Safety escalation | Simple urgent tiles first | Detailed action instructions, authority, map, language variants | Emergency and public alerts |

Example:

Collapsed:  
\[WHEAT\] \[PRICE\] \[UP\] \[ROUEN\] \[TODAY\]

Expanded:  
Wheat spot price increased at Rouen today.  
\+ 3.7% versus previous close  
€221.50/t  
Source: named market feed  
Observed: 12:45 CEST  
Confidence: high  
Action: review basis spread

The compact Pictiq row is not a lossless substitute for the data. It is a navigational summary. The expanded panel makes hidden precision accessible when a decision requires it.

This lets Pictiq stay minimalist at first glance without forcing minimalism on the underlying semantic record.

## **Mapping to Pictiq categories**

The following framework can become a formal annotation model for Pictiq translations, messages, and Context Packs.

| Pictiq category | Formal interpretation | When to use it | Required metadata | Safe for automatic execution? |
| ----- | ----- | ----- | ----- | ----- |
| `PRESERVED_EXPLICITLY` | Source distinction appears directly in tiles or typed semantic fields | Important concepts, negation, quantities, destinations, time, status | Concept IDs, roles, values, units, scope | Potentially, after schema validation |
| `PRESERVED_BY_COMPOSITION` | Meaning is encoded by a defined combination of core primitives | Regular derived concepts such as WATER \+ GROW → irrigation | Composition rule, pack/version, parse tree | Potentially, if grammar is deterministic |
| `CONTEXT-SUFFICIENT` | Omitted distinction is reliably inferable from declared shared context | Current screen, known location, routine interaction, established participant | Context dependencies, task, confidence, expiry/validity | Only in low-risk or validated bounded contexts |
| `INTENTIONAL_OMISSION` | Detail is deliberately excluded as irrelevant, sensitive, redundant, or nonportable | Tone, style, unnecessary identity, background detail, known defaults | Omission rationale, source retention policy, privacy classification | Yes only if omitted detail cannot alter execution |
| `LOSSY` | A source distinction is discarded and cannot be reliably recovered | Hedges, causal nuance, exact temporal/numeric detail, source/provenance, participant distinction | Lost fields, impact level, repair option, warning state | No for medium/high-impact loss |
| `GAP` | Pictiq lacks the lexicon, grammar, type, relation, or contextual basis to represent meaning | New technical domain, complex scope, legal/medical concept, unsupported relation | Gap type, proposed remedy, fallback format | No |

### **Recommended status rule**

Use a conservative status hierarchy:

PRESERVED\_EXPLICITLY  
or PRESERVED\_BY\_COMPOSITION  
    → eligible for structured validation.

CONTEXT-SUFFICIENT  
    → usable when declared context is present and stable.

INTENTIONAL\_OMISSION  
    → usable if omission cannot affect the intended task.

LOSSY  
    → display warning, request clarification, expand to text/data,  
      or block high-stakes actions.

GAP  
    → do not pretend to translate; use fallback text/schema or  
      create a governed grammar/Context Pack extension.

## **A Pictiq “compression ledger”**

For each conversion from text, speech, data, or an agent plan into Pictiq, maintain a machine-readable ledger. This is especially valuable for the RAG/text-to-Pictiq and agent experiments you are exploring.

{  
  "source": {  
    "text": "Please check tomorrow's wheat basis at Rouen and alert me if it widens by more than €3/t.",  
    "locale": "en"  
  },  
  "task": "create\_market\_monitor",  
  "pictiq": {  
    "rendering": \[  
      "core:self",  
      "core:request",  
      "core:check",  
      "agri:wheat",  
      "agri-market:basis",  
      "geo:FR-ROUEN",  
      "core:tomorrow",  
      "core:if",  
      "agri-market:basis",  
      "core:widen",  
      "core:more-than",  
      "currency:EUR",  
      "number:3",  
      "unit:EUR\_PER\_TONNE",  
      "core:then",  
      "core:alert",  
      "core:self"  
    \],  
    "status": "PRESERVED\_EXPLICITLY"  
  },  
  "preserved": \[  
    "request",  
    "monitor action",  
    "commodity",  
    "metric",  
    "location",  
    "time",  
    "change direction",  
    "numeric threshold",  
    "currency",  
    "unit",  
    "notification recipient"  
  \],  
  "context\_sufficient": \[\],  
  "intentional\_omissions": \[  
    "politeness marker"  
  \],  
  "lossy": \[\],  
  "gaps": \[\],  
  "execution\_readiness": "requires\_entity\_resolution\_and\_schema\_validation"  
}

Now compare an over-compressed version:

\[WHEAT\] \[BASIS\] \[WATCH\] \[ROUEN\] \[ALERT\]

Its ledger might say:

{  
  "status": "LOSSY",  
  "lost": \[  
    "observation date",  
    "condition direction",  
    "threshold value",  
    "currency",  
    "unit",  
    "alert recipient"  
  \],  
  "impact": "high",  
  "execution\_readiness": "not executable"  
}

That distinction makes Pictiq much more intellectually honest and operationally useful. The same attractive icon row can be classified as a casual dashboard summary, a valid request, or an unsafe compression depending on what it retains.

## **Decision procedure**

Before rendering or accepting a Pictiq message, apply this sequence.

1. **Define the receiver’s task.**  
   Is the goal recognition, navigation, ordering, logging, analysis, tool invocation, consent, emergency action, or legal record? There is no context-free definition of “enough meaning.”  
2. **Extract the task-critical fields.**  
   Identify intent, actor, target, time, place, quantity, status, polarity, condition, authority, uncertainty, and consequence as relevant.  
3. **Separate defaults from assumptions.**  
   A café’s default quantity of one drink may be context-sufficient. A default medication dose is not.  
4. **Classify every absent field.**  
   Is it context-sufficient, intentionally omitted, lossy, or a gap? Do not call it “context” unless the context is actually available to the receiver.  
5. **Estimate the cost of error.**  
   Consider reversibility, time pressure, financial impact, safety, discrimination risk, privacy, and loss of trust.  
6. **Select an output mode.**  
   Use a minimal tile sequence for low-risk expressive communication; add typed values, labels, metadata, and confirmation for operational tasks; fall back to text or specialist notation when the system has a gap.  
7. **Preserve provenance and expansion paths.**  
   A compact visual message should link to its source, context, exact data, and conversion ledger whenever decisions may be reviewed later.

## **Bottom line**

Pictiq should define success as **task-faithful compression**, not lexical equivalence with natural language. Controlled languages show how reducing vocabulary and grammar can retain operational clarity; semantic parsing shows how to normalize utterances into structured meaning; emergency standards show which fields cannot be omitted under pressure; information theory provides the rate–distortion framing; minimalist languages show how context and composition can carry broad concepts; and progressive disclosure shows how to keep complexity accessible without keeping it constantly visible.\[[pmc.ncbi.nlm.nih](https://pmc.ncbi.nlm.nih.gov/articles/PMC12385448/)\]\[[ceur-ws](https://ceur-ws.org/Vol-3427/short2.pdf)\]\[[ai.meta](https://ai.meta.com/research/publications/semantic-parsing-for-task-oriented-dialog-using-hierarchical-representations/)\]\[[docs.oasis-open](https://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2-os.html)\]\[[griffinbassett](https://griffinbassett.com/wp-content/uploads/2024/11/The-Pragmatics-of-Toki-Pona-Across-Variable-Native-Language-Backgrounds.pdf)\]\[[ixdf](https://ixdf.org/literature/book/the-glossary-of-human-computer-interaction/progressive-disclosure)\]

The most useful Pictiq rule is:

> Preserve what changes the receiver’s correct action, decision, safety, rights, or interpretation; compress what is redundant; intentionally omit what is irrelevant or harmful to expose; mark what was lost; and surface a gap whenever the language cannot carry a needed distinction.

With that rule, the categories become a coherent protocol:

CONTEXT-SUFFICIENT \= recoverable from declared shared context  
INTENTIONAL\_OMISSION \= deliberately unnecessary or inappropriate to include  
LOSSY \= meaningful detail has been dropped  
GAP \= meaningful detail cannot yet be represented safely or clearly

That framework gives Pictiq a principled way to remain minimal without claiming that minimal messages preserve more meaning than they actually do.

