Pictiq can plausibly serve as an **inspectable intermediate representation** for a constrained band of communication: short requests, status reports, task descriptions, simple plans, alerts, handoffs, and cross-lingual UI intent. It should not be treated as a general replacement for natural language, formal logic, tool schemas, or planning languages; its value is a readable semantic layer between them.

The most realistic architecture is:

\\text{Natural language / speech / UI input}  
\\rightarrow  
\\text{Pictiq semantic IR}  
\\rightarrow  
\\text{validated domain schema, plan, or tool call}

Pictiq would be the layer a human can see, correct, teach, and audit—while JSON, ontologies, schemas, and execution engines carry the precision necessary for reliable automation.

## **What “intermediate representation” means**

An intermediate representation, or IR, is a form designed to sit between a messy or user-friendly input and a stricter downstream system. It usually makes structure explicit while omitting details irrelevant to the next step.

For example:

Natural language:  
“Please check tomorrow’s wheat basis at Rouen and alert me if it widens.”

Inspectable Pictiq layer:  
\[ME\] \[ASK\] \[CHECK\] \[WHEAT\] \[BASIS\] \[ROUEN\] \[TOMORROW\]  
\[IF\] \[BASIS\] \[WIDEN\] \[THEN\] \[ALERT\] \[ME\]

Executable representation:  
{  
  "intent": "monitor\_market\_metric",  
  "commodity": "wheat",  
  "metric": "basis",  
  "location": "FR-ROUEN",  
  "time": {"relative\_date": "tomorrow"},  
  "condition": {"operator": "increase", "direction": "widen"},  
  "on\_true": {"action": "notify", "recipient": "self"}  
}

The Pictiq layer is not necessarily the final execution format. It provides a compact, human-checkable bridge that exposes the proposed interpretation before an agent queries data or performs an action.

That makes it closer to an **auditable intent representation** than to an icon-based replacement for JSON.

## **Comparison with existing IRs**

| System | Typical representation | What it makes explicit | Human readability | Machine executability | Where Pictiq resembles it | Crucial difference |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| Semantic frames / FrameNet | Event or situation frame plus participant roles | Event type, core roles, peripheral roles, relations | Medium | Medium | Pictiq can use role-bearing visual frames such as BUYER–GOODS–SELLER | FrameNet is a very large linguistic resource, not a compact operational language |
| AMR | Rooted directed graph of concepts and relations | Predicate–argument structure, modifiers, core semantic relations | Low–medium | Medium–high | Pictiq could render a compact, selected subset of an AMR-like graph | AMR is broad, abstract, and generally unsuitable as a direct execution contract |
| Intent \+ slots | Intent label plus named parameter values | Requested task and required variables | High for developers | High in bounded domains | Very close to a Pictiq request/status pattern | Flat slot records become inadequate for complex scope, logic, and multi-step plans |
| Controlled natural language | Restricted natural-language syntax and lexicon | Unambiguous or limited interpretations | High | High when grammar is formal | Pictiq can be a visual controlled language with fixed grammar | Pictiq has lower expressive coverage and needs spatial/visual parsing rules |
| PDDL | Typed predicates, states, actions, preconditions, effects, goals | World state and action consequences | Medium for specialists | High for planners | Pictiq can present a human-facing plan summary | Pictiq cannot safely encode full formal planning semantics without a logic layer |
| Tool-call schemas / JSON Schema | Function name plus typed, validated arguments | Exact API operation, argument types, constraints | Medium | Very high | Pictiq can display the intended action and key arguments before execution | A pictogram sequence should never be the sole authorization/execution payload |
| KQML / FIPA-ACL | Performatives, content, ontology, conversation metadata | Communicative intent, protocol, payload, context | Low–medium | Medium–high | Pictiq can visibly encode ASK, INFORM, CONFIRM, REQUEST, REFUSE, etc. | Agent protocols require routing, identity, correlation, commitments, and error semantics |
| Constrained DSL | Formal domain-specific syntax | Domain objects, operators, conditions, actions | Medium–high for trained users | High | A strict Pictiq Context Pack can serve as a visual DSL front end | DSLs normally privilege precision over broad public readability |

The unifying pattern is that each system separates at least some of these layers:

Communicative act:  
  What is the sender doing?  
  ask, report, request, confirm, warn, refuse, propose

Semantic content:  
  What entities, events, values, relations, and conditions are involved?

Domain model:  
  What does “basis,” “check-in,” “dose,” or “evacuate” formally mean?

Execution contract:  
  What tool, endpoint, permissions, parameters, and validations are required?

Presentation:  
  How is the message shown to a person?

Pictiq is strongest in the first, second, and fifth layers. It can assist with the third through Context Packs. It should delegate the fourth to a validated schema and execution system.

## **Semantic frames: Pictiq’s best conceptual fit**

Frame semantics models meaning as structured situations. FrameNet treats a frame as a situation, event, relation, or entity with participant roles, called frame elements. Its core elements are essential to that frame’s meaning; non-core elements add information such as time, place, and manner.\[[en.wikipedia](https://en.wikipedia.org/wiki/FrameNet)\]\[[academiccommons.columbia](https://academiccommons.columbia.edu/doi/10.7916/D81261XT/download)\]

A commerce frame illustrates the idea:

COMMERCE\_SELL  
  Seller  
  Buyer  
  Goods  
  Money  
  Place  
  Time

A Pictiq Context Pack can express the same concept with explicit, visible role composition:

\[SELLER\] — \[SELL\] — \[GOODS\] — \[BUYER\]  
                       \[PRICE\]  
                       \[PLACE\]  
                       \[TIME\]

Or in a linear compact form:

\[PERSON:A\] \[SELL\] \[GRAIN\] \[TO\] \[PERSON:B\]  
\[FOR\] \[PRICE\] \[AT\] \[PLACE\] \[ON\] \[TIME\]

The critical design decision is that `SELL`, `GRAIN`, `PRICE`, and `PLACE` cannot be merely adjacent decorative icons. Their semantic roles must be encoded or deterministically inferred:

* Who is the actor?  
* What is being sold?  
* Who receives it?  
* Is PRICE an amount, a target, a comparison baseline, or an alert threshold?  
* Does TIME apply to the sale, delivery, observation, or payment?

### **What Pictiq can borrow**

Pictiq should adopt a **small reusable role inventory** rather than build hundreds of ad hoc visual templates:

| Role family | Core roles for Pictiq | Examples |
| ----- | ----- | ----- |
| Agency | AGENT, RECIPIENT, OWNER, SOURCE | Farmer sends a report; traveler requests help |
| Event | ACTION, EVENT, STATE, CHANGE | Deliver, inspect, unavailable, increase |
| Entity | OBJECT, PERSON, PLACE, RESOURCE | Grain, package, staff member, accommodation |
| Relation | TARGET, FROM, TO, WITH, ABOUT | Deliver goods to depot; ask staff about a room |
| Context | TIME, LOCATION, QUANTITY, VALUE, UNIT | Tomorrow, Nantes, 5 tonnes, €220/t |
| Modality | NEED, WANT, CAN, MUST, MAY | Need water; must stop; can enter |
| Dialogue act | ASK, INFORM, REQUEST, CONFIRM, REFUSE | Ask for route; report damage; confirm booking |
| Logic | NOT, IF, THEN, OR, AND, COMPARE | If rain then delay; no nuts; price above threshold |
| Operational state | START, STOP, DONE, WAIT, ERROR, URGENT | Start pump; task complete; fault; urgent evacuation |

FrameNet’s distinction between core and peripheral elements is useful for Pictiq UI and Context Packs. A pack can define a minimal valid message and then allow optional contextual refinements:

Core “delivery” frame:  
  ACTOR \+ MOVE/DELIVER \+ GOODS \+ DESTINATION

Optional:  
  quantity, quality, deadline, vehicle, route,  
  price, condition, receiver confirmation

This keeps common messages compact without making the grammar unable to express richer cases.

## **AMR: Pictiq can be a legible projection, not an AMR replacement**

Abstract Meaning Representation represents sentence meaning as a graph: nodes correspond to concepts and edges specify relationships. AMR is commonly described as a rooted directed acyclic graph that captures “who is doing what to whom.” In contrast to surface text, it aims to abstract away from many syntactic variations.\[[arxiv](https://arxiv.org/html/2505.03229v1)\]

A sentence such as:

“The cooperative will deliver 40 tonnes of wheat to Nantes tomorrow.”

could conceptually become:

deliver-01  
  :ARG0 cooperative  
  :ARG1 wheat  
      :quant 40  
      :unit tonne  
  :destination Nantes  
  :time tomorrow

A Pictiq equivalent could render the same structure as:

\[COOPERATIVE\] \[DELIVER\] \[WHEAT\] \[40\] \[TONNES\]  
\[TO\] \[NANTES\] \[TOMORROW\]

But a visually linear tile row does not inherently expose the underlying graph. Its parser needs declared attachment rules or an internal graph:

{  
  "event": "agri-logistics:deliver",  
  "agent": "org:cooperative",  
  "goods": {  
    "concept": "agri:wheat",  
    "quantity": 40,  
    "unit": "t"  
  },  
  "destination": "geo:Nantes",  
  "time": "2026-09-12"  
}

### **Where the AMR analogy works**

Pictiq can behave like a constrained visual semantic graph when it:

* Normalizes multiple wordings into the same concept structure.  
* Represents entities, events, properties, quantities, and relations explicitly.  
* Uses canonical identifiers rather than relying only on French or English labels.  
* Separates visible rendering from semantic data.  
* Supports localized generation in multiple languages.  
* Lets an AI or user inspect the interpreted structure before acting.

For example, these can normalize to one Pictiq representation:

“Book me a room in Nantes for Friday.”  
“Je voudrais réserver une chambre à Nantes vendredi.”  
“Find accommodation in Nantes this Friday.”  
\[ME\] \[REQUEST\] \[RESERVE\] \[ROOM\] \[AT\] \[NANTES\] \[FRIDAY\]

### **Where it breaks**

AMR is already difficult to annotate consistently, and it handles many phenomena that Pictiq should not try to encode in a minimal icon grammar:

* Fine-grained lexical sense distinctions.  
* Negation scope across complex clauses.  
* Quantifier scope: “Every supplier did not deliver.”  
* Modality and counterfactuals.  
* Coreference across long discourse.  
* Ellipsis, irony, metaphor, presupposition, humor, and rhetorical intent.  
* Nested propositional attitudes: “Anna believes that Boris suspects…”  
* Detailed temporal, causal, and evidential relations.  
* Ambiguity that must remain unresolved rather than being forced into one parse.

Pictiq should therefore operate as a **task-semantic subset**. It can preserve an `unresolved` or `needs-confirmation` state instead of pretending that every natural-language sentence maps cleanly to tiles.

## **Intent–slot representations: the closest operational analogy**

Task-oriented dialogue systems often reduce an utterance to two pieces:

1. An **intent**: what the user wants the system to do.  
2. **Slots**: the values required to carry out that intent.

The resulting semantic frame is typically extracted through intent classification and slot filling. For example:\[[aclanthology](https://aclanthology.org/2020.coling-main.42.pdf)\]

{  
  "intent": "book\_hotel",  
  "city": "Nantes",  
  "check\_in": "2026-09-11",  
  "nights": 1,  
  "guests": 1  
}

Pictiq maps naturally onto this:

\[ME\] \[REQUEST\] \[BOOK\] \[HOTEL\]  
\[PLACE:NANTES\] \[DATE:FRIDAY\] \[1\] \[1\]

This is a good fit because:

* The vocabulary can remain small.  
* Domain-specific slots belong naturally in Context Packs.  
* The user can visually inspect missing values.  
* Each pack can publish valid templates and required fields.  
* The representation can compile to JSON Schema, SQL filters, API calls, or workflow steps.  
* Human correction can occur before execution.

### **Pictiq as visual intent schema**

A Context Pack can define a compact template:

Intent:  
  agri-market:monitor-basis

Required slots:  
  commodity  
  location  
  observation\_time  
  threshold\_or\_change\_condition

Optional slots:  
  delivery\_period  
  grade  
  currency  
  notification\_channel

Pictiq rendering:

\[MONITOR\] \[BASIS\]  
\[COMMODITY:WHEAT\]  
\[LOCATION:ROUEN\]  
\[TIME:TOMORROW\]  
\[CONDITION:WIDEN\]  
\[ALERT:ME\]

Machine representation:

{  
  "intent": "agri-market:monitor-basis",  
  "slots": {  
    "commodity": "agri:wheat",  
    "location": "geo:FR-ROUEN",  
    "observation\_time": "2026-09-12",  
    "condition": {  
      "operator": "change",  
      "direction": "widen"  
    },  
    "notify": "self"  
  }  
}

This is exactly where a Pictiq IR could be unusually useful: a user or supervising agent sees not a hidden JSON object, but a standardized visual “receipt” of the intent.

### **Limit of the intent–slot approach**

Intent-and-slot systems work well for bounded transactional tasks but degrade when a request becomes a plan, an argument, a negotiation, a diagnosis, a creative brief, or a multi-party conversation.

For example:

“Compare the last three harvests, account for the drought effect,  
show uncertainty, and recommend a hedging strategy only if the  
confidence interval justifies it.”

This includes analysis specification, causal assumptions, data selection, uncertainty representation, decision policy, and conditional recommendation. An intent plus a few slots is insufficient. Pictiq may represent an inspectable summary, but the formal computational representation needs richer query, statistical, and policy languages.

## **Controlled natural languages: the human-readable formal-language model**

Attempto Controlled English, or ACE, is a precisely defined subset of English that can be automatically and unambiguously translated into first-order logic. It is intended to remain natural-looking to domain specialists while functioning as a formal language.\[[research.vu](https://research.vu.nl/en/publications/attempto-controlled-english-for-knowledge-representation/)\]\[[attempto.ifi.uzh](https://attempto.ifi.uzh.ch/)\]

ACE can be used to formulate requirements, translate them into discourse representation structures and optionally Prolog, add them to a knowledge base, and query or execute them for simulation, prototyping, and validation.\[[arxiv](https://arxiv.org/abs/cmp-lg/9603003)\]

That gives Pictiq an important aspiration:

Natural language:  
“Every shipment with a failed quality check must be held.”

Controlled Pictiq:  
\[ALL\] \[SHIPMENT\]  
\[IF\] \[QUALITY-CHECK\] \[FAIL\]  
\[THEN\] \[MUST\] \[HOLD\]

Formal policy:  
∀x (shipment(x) ∧ failed\_quality\_check(x) → must\_hold(x))

Pictiq could become a controlled visual language if it has:

* A closed or carefully governed vocabulary.  
* A formal grammar.  
* Explicit role and scope rules.  
* Deterministic mappings to a semantic model.  
* Defined treatment for negation, modality, quantity, reference, conditionals, and tense/aspect.  
* A parser that rejects invalid or under-specified forms rather than silently guessing.  
* Authoring support that prevents users from constructing structurally invalid messages.

### **The necessary caution**

Controlled languages usually give up part of natural language’s convenience, nuance, and broad coverage in exchange for formal interpretability. Pictiq would face the same trade-off, more sharply:

* A visual language has fewer low-friction ways to express abstract relations.  
* Icons are more culturally variable than words.  
* Spatial syntax adds rendering and accessibility complexity.  
* Precise logical markers can quickly make tiles dense and intimidating.  
* A “simple” visual sequence may conceal complicated semantic decisions.

Therefore, Pictiq should offer controlled expressiveness in layers:

| Pictiq mode | Goal | Example use |
| ----- | ----- | ----- |
| Expressive / informal | Fast human communication; ambiguity acceptable | Travel cards, chat, simple personal notes |
| Structured / inspectable | Clear intent, named roles, visible scope, parseable JSON | Forms, dashboards, workflows, agent handoffs |
| Strict / executable | A constrained grammar with validation and unambiguous data types | Tool invocation preview, checklists, safety procedures, policy rules |
| Linked / authoritative | Visual message points to or is generated from signed structured data | Medical, emergency, transactional, regulatory, inventory uses |

A visual sequence should only be executable in the strict mode—and even then the canonical data object, validation result, authentication state, and user authorization determine execution.

## **Planning languages: Pictiq can show plans, not replace planning semantics**

PDDL, the Planning Domain Definition Language, standardizes a way to express automated planning tasks. A domain describes possible states and actions; a problem describes a specific initial state and desired goal. Actions have parameters, preconditions, and effects, including conditional effects.\[[en.wikipedia](https://en.wikipedia.org/wiki/Planning_Domain_Definition_Language)\]\[[users.cecs.anu.edu](https://users.cecs.anu.edu.au/~patrik/pddlman/writing.html)\]

A simple PDDL-like action has logic absent from ordinary intent schemas:

Action: deliver(goods, source, destination)  
Preconditions:  
  goods are at source  
  vehicle is available  
  route is open  
Effects:  
  goods are at destination  
  goods are no longer at source

Pictiq can render this clearly for supervision:

\[DELIVER\] \[GOODS\] \[FROM\] \[SOURCE\] \[TO\] \[DESTINATION\]

\[REQUIRES\]  
\[GOODS\] \[AT\] \[SOURCE\]  
\[AND\] \[VEHICLE\] \[AVAILABLE\]  
\[AND\] \[ROUTE\] \[OPEN\]

\[RESULTS\]  
\[GOODS\] \[AT\] \[DESTINATION\]  
\[NOT\] \[GOODS\] \[AT\] \[SOURCE\]

But the execution engine should use formal PDDL, a workflow engine, state machine, or typed API—not a pictogram parse alone.

### **Why the analogy breaks**

Planning requires a formally defined world model:

* State predicates and object types.  
* Closed/open-world assumptions.  
* Preconditions and effects.  
* Resources, costs, duration, concurrency, and temporal constraints.  
* Uncertainty and observability.  
* Action failures and recovery policies.  
* Goal conflicts and preference ordering.

A Pictiq tile sequence can represent these notions at a high level, but it cannot safely supply all their formal semantics unless Pictiq grows into a visual syntax for PDDL-like logic. That may be appropriate for an advanced expert pack, but it conflicts with the project’s minimal, broadly readable core.

The better division is:

Pictiq:  
  “This plan intends to deliver wheat from silo A to port B tomorrow.”

Planning DSL:  
  Exact resources, capacity, route constraints, calendars,  
  inventory state, safety rules, cost objective, failure branches.

Pictiq functions as the plan’s human-readable **explanation and approval surface**.

## **Tool-call schemas: Pictiq as a pre-execution receipt**

Modern LLM tool use relies on structured schemas. A tool is uniquely identified by a name and publishes an `inputSchema` that defines expected parameters under JSON Schema rules. Model Context Protocol, for example, standardizes integration between LLM applications and external tools/data sources, with the authoritative specification defined through typed schemas and broader JSON Schema availability.\[[modelcontextprotocol](https://modelcontextprotocol.io/specification/draft/server/tools)\]\[[modelcontextprotocol](https://modelcontextprotocol.io/specification/2025-06-18)\]\[[github](https://github.com/modelcontextprotocol/modelcontextprotocol)\]

Structured-output systems similarly use JSON Schema to constrain an LLM’s response to a required data contract.\[[developers.openai](https://developers.openai.com/api/docs/guides/structured-outputs)\]

Example:

{  
  "tool": "search\_market\_prices",  
  "arguments": {  
    "commodity": "wheat",  
    "market": "Rouen",  
    "date": "2026-09-12"  
  }  
}

Pictiq can act as an inspection layer:

\[SEARCH\] \[PRICE\]  
\[WHEAT\] \[MARKET:ROUEN\] \[DATE:TOMORROW\]

Before execution, a UI can show both:

| User-facing view | System-facing view |
| ----- | ----- |
| `[SEARCH] [PRICE] [WHEAT] [ROUEN] [TOMORROW]` | `search_market_prices({commodity:"wheat", market:"FR-ROUEN", date:"2026-09-12"})` |

This reduces a common AI-agent problem: users cannot easily verify opaque tool arguments, especially identifiers, dates, filters, account scopes, recipient identities, or irreversible side effects.

### **Where Pictiq is especially useful**

* Tool invocation previews before sending messages, buying items, changing records, publishing content, or deleting data.  
* Internal agent handoffs, where one agent proposes a task and another executes it.  
* Multilingual interfaces, where a stable visual rendering accompanies local-language explanations.  
* Dashboards that summarize jobs, status, exceptions, inputs, outputs, and pending approvals.  
* Physical or low-literacy workflows where an icon grammar can be easier to inspect than raw JSON.  
* User correction interfaces: tap a tile to alter the corresponding validated field.

### **Where it must not be authoritative**

Pictiq must not substitute for:

* Authentication and authorization.  
* User consent to irreversible actions.  
* Exact numeric, financial, legal, medical, or safety constraints.  
* API type validation.  
* Entity disambiguation: which “Anton,” which account, which field, which market, which document?  
* Security-sensitive secrets, tokens, signatures, or policy decisions.  
* Full provenance, evidence, uncertainty, or audit logs.

The visual layer may say `[SEND] [INVOICE] [CLIENT]`; the formal layer must still carry recipient ID, invoice ID, organization, payment terms, currency, permissions, and confirmation state.

## **Symbolic agents: communicative act plus content plus ontology**

KQML and FIPA-style agent communication languages clarify a design distinction Pictiq should preserve. KQML defines performatives—such as assertions, queries, commands, and replies—and attaches a communicative act to the message content. It can also declare the content language, assumed ontology, and topic descriptors.\[[cdn.aaai](https://cdn.aaai.org/Workshops/1994/WS-94-02/WS94-02-007.pdf)\]

FIPA-ACL follows the same layered model. Its required performative says what speech act is being attempted; optional fields can specify sender/receiver, conversation identifier, protocol, content language, and ontology. The content language provides syntax; the ontology provides vocabulary.\[[site.ieee](https://site.ieee.org/pes-mas/agent-technology/standards-and-interoperability/)\]

A Pictiq-like agent packet should therefore not be merely:

\[WHEAT\] \[PRICE\] \[UP\]

It should be structured conceptually as:

{  
  "performative": "inform",  
  "sender": "agent:market-monitor",  
  "recipient": "agent:portfolio-manager",  
  "conversation\_id": "market-alert-2026-09-11-001",  
  "protocol": "pictiq-agent-1",  
  "ontology": "org.pictiq.agri-market@1.2",  
  "content": {  
    "event": "agri-market:price-change",  
    "commodity": "agri:wheat",  
    "direction": "core:up",  
    "observation\_time": "2026-09-11T13:00:00+02:00"  
  },  
  "rendering": {  
    "pictiq": "\[INFORM\] \[WHEAT\] \[PRICE\] \[UP\] \[NOW\]"  
  }  
}

The Pictiq rendering can give a person an immediate understanding. But the agent protocol needs the message envelope because autonomous coordination depends on metadata that has no reason to be visible in every human-facing tile string.

### **A useful Pictiq split**

| Layer | Pictiq role | Example |
| ----- | ----- | ----- |
| Speech act | Visible or structured operator | ASK, INFORM, REQUEST, CONFIRM, WARN, DECLINE |
| Content frame | Tile sequence and canonical graph | WHEAT \+ PRICE \+ INCREASE \+ ROUEN \+ TODAY |
| Ontology/context pack | Declares the vocabulary and interpretation | `agri-market@1.2` |
| Conversation state | Usually metadata, optionally summarized visually | `conversation_id`, turn, proposal, accepted/rejected |
| Routing and trust | Metadata only | sender, recipient, signatures, authorization, provenance |
| Tool execution | Typed payload generated after validation | API/function call with resolved IDs and arguments |

This directly supports your Context Pack model. A pack becomes the declared ontology or vocabulary profile an agent needs to interpret a Pictiq message correctly.

## **Where Pictiq is plausible**

Pictiq is most credible as an IR where four conditions hold:

1. **The domain has recurring frames.**  
   Travel, hospitality, agriculture, logistics, home tasks, field observation, basic customer service, inventory, accessibility requests, and incident reporting have repeated actors, actions, objects, places, times, states, and requests.  
2. **The message can use a constrained vocabulary.**  
   A small stable core plus a domain Context Pack is adequate. The user does not need unrestricted philosophical, literary, legal, or scientific discourse.  
3. **A human should inspect the parsed intent.**  
   The visual form provides a practical advantage over raw JSON, hidden model reasoning, or technical schema fields.  
4. **The final action has a separate validation contract.**  
   Pictiq expresses intention; a schema, typed tool call, query plan, or workflow engine verifies and executes it.

### **Strong application areas**

| Application | Pictiq IR role | Downstream representation |
| ----- | ----- | ----- |
| Travel assistance | Request/clarification form: need, place, time, mobility, booking status | Reservation/search API schema |
| Agrimarket dashboards | Compact alerts, threshold definitions, data-query summaries, report handoffs | Query object, alert rule, data pipeline parameters |
| Field operations | Observations, tasks, status, quantities, hazards, proof-of-completion | Work-order, GIS, inventory, maintenance schema |
| Tourism content | Structured itinerary fragments, accessibility markers, visitor preferences | CMS metadata, map POIs, booking links |
| AAC-supportive workflows | Expressive or task-forming messages that users can inspect and correct | Speech output, communication log, optional workflow request |
| Agent supervision | Proposed plan/action summary before tool use | JSON Schema tool call, API payload, approval record |
| Logistics | Shipment condition, location, quantity, handoff, delay, required action | Event stream, EDI-like record, workflow state |
| Education | Teaching semantic roles, logic, data structures, and agent action semantics | Interactive AST/JSON view |

For a Pictiq-powered agrimarket tool, the sweet spot is not “replace analyst prose.” It is a reproducible visual brief such as:

\[INFORM\] \[WHEAT\] \[PRICE\] \[UP\]  
\[PLACE:ROUEN\] \[TIME:TODAY\]  
\[CAUSE?\] \[PORT\] \[DELAY\]  
\[ACTION\] \[CHECK\] \[BASIS\]

Each tile group can link to the exact data series, observation timestamp, source, uncertainty, and recommended next tool query. That is inspectable and compositional without pretending the icons themselves contain a complete market model.

## **Where the analogy breaks down**

Pictiq is not a universal semantic IR. Its limitations are structural, not merely unfinished implementation work.

### **Full natural-language meaning**

Natural language carries implicit assumptions, discourse context, social relationships, rhetorical force, connotation, metaphor, humor, politeness, uncertainty, and underspecified reference. A minimal pictographic vocabulary necessarily discards or forces explicit choices about much of this.

The sentence:

“I suppose we might consider delaying the shipment,  
unless the buyer is already relying on it.”

does not map honestly to a simple `DELAY SHIPMENT` tile sequence. It includes tentative stance, proposal rather than command, conditional dependency, epistemic uncertainty, temporal assumptions, and a model of another party’s expectations.

Pictiq can render a simplified operational version only after a user or model makes those decisions explicit:

\[PROPOSE\] \[MAYBE\] \[DELAY\] \[SHIPMENT\]  
\[UNLESS\] \[BUYER\] \[NEED\] \[SHIPMENT\]

But it must preserve that this is a constrained reformulation, not lossless translation.

### **Open-world knowledge and reasoning**

A Pictiq message can identify `WHEAT`, `PRICE`, `ROUEN`, and `INCREASE`; it does not define the data source, market methodology, units, series revision policy, currency conversion, delivery basis, statistical uncertainty, or causal mechanism.

For factual claims and recommendations, Pictiq needs linked provenance:

{  
  "claim": "agri-market:price-increase",  
  "commodity": "agri:wheat",  
  "market": "geo:FR-ROUEN",  
  "comparison": "previous\_close",  
  "value": 4.25,  
  "unit": "EUR/tonne",  
  "source": "source:…",  
  "observed\_at": "…",  
  "confidence": 0.93  
}

The icons can summarize this record; they should not replace it.

### **Logic, scope, and quantification**

Basic IF/THEN/NOT/AND/OR tiles can cover useful operational cases. But natural and formal logic rapidly become difficult:

* “Do not alert every trader who has not opted out.”  
* “Alert a trader only if no approved alternative alert was sent.”  
* “For each shipment, choose the cheapest route that still meets the delivery deadline.”  
* “The price may rise unless the policy changes, but only in the northern region.”

These require precise scope, variables, quantifiers, optimization, exceptions, nested conditions, and temporal logic. A Pictiq representation could display an explanation of the rule, but a formal DSL or policy language should own the actual semantics.

### **Numeric and typed data**

A tile can show `NUMBER`, `PRICE`, `MORE`, `LESS`, `TIME`, and `MEASURE`. Yet execution depends on exact values, units, precision, currencies, time zones, rounding, thresholds, ranges, and missing-data policy.

For example, these differ materially:

€220/t  
€220 per metric tonne  
€220 per short ton  
€220/t excluding VAT  
€220/t delivered Rouen, Oct–Dec  
€220/t indicative, not executable

Pictiq should visually expose key numbers and units but preserve formal typed values underneath.

### **High-stakes execution**

In medical, legal, financial, emergency, identity, and irreversible operational contexts, a pictorial IR may improve review but cannot be the authoritative specification. The risk is “semantic laundering”: a complex, uncertain, or unsafe action looks reassuringly simple once rendered as friendly tiles.

The safe pattern is:

Pictiq summary  
  ↓  
Human confirmation / correction  
  ↓  
Resolved entities \+ typed schema validation  
  ↓  
Permissions and policy enforcement  
  ↓  
Execution  
  ↓  
Auditable structured log \+ Pictiq receipt

## **Recommended Pictiq IR model**

Build Pictiq as a family of representations rather than a single flat icon string.

### **1\. Visual surface syntax**

This is what humans see:

\[ME\] \[REQUEST\] \[BOOK\] \[ROOM\]  
\[PLACE:NANTES\] \[TIME:FRIDAY\] \[1\]

It prioritizes scanability, correction, multilingual support, and compactness.

### **2\. Canonical semantic frame**

This is the stable internal form:

{  
  "performative": "request",  
  "frame": "travel:lodging-reservation",  
  "roles": {  
    "requester": {"ref": "self"},  
    "lodging\_type": "travel:room",  
    "place": {"id": "geo:FR-NANTES"},  
    "start\_date": "2026-09-11",  
    "duration": {"value": 1, "unit": "night"}  
  },  
  "ontology": "org.pictiq.travel@1.0",  
  "status": "draft",  
  "confidence": "confirmed-by-user"  
}

The canonical frame should use fixed roles and typed fields defined by the Context Pack, rather than depend on the visual order alone.

### **3\. Execution binding**

This converts the semantic frame into a specific tool/API payload:

{  
  "tool": "search\_lodging",  
  "arguments": {  
    "city\_id": "geo:FR-NANTES",  
    "check\_in": "2026-09-11",  
    "nights": 1,  
    "guests": 1  
  },  
  "validation": {  
    "schema": "travel.search\_lodging.v2",  
    "resolved\_entities": true,  
    "requires\_confirmation": false  
  }  
}

The binding should be explicit and reversible:

Pictiq → semantic frame → candidate tools → schema-valid payload

The reverse direction should also work:

Tool call / event → semantic frame → Pictiq visual receipt

That round trip is central. It means a person can inspect not only what an AI proposes to do, but also what a system actually did.

## **Design requirements for Context Packs**

A Context Pack intended for inspectable IR use needs more than a symbol set. It needs a mini ontology and a constrained semantic schema.

Each pack should define:

* **Frames:** recurring events, requests, reports, states, and workflows.  
* **Required roles:** the minimum arguments that make a frame meaningful.  
* **Optional roles:** context such as time, place, quantity, source, method, confidence, or reason.  
* **Permitted core primitives:** which Pictiq roots are valid in the pack.  
* **Domain concepts:** namespaced terms and their stable definitions.  
* **Type system:** person, organization, physical object, location, date/time, quantity, currency, document, dataset, alert, action, policy, etc.  
* **Relations:** actor-of, target-of, source, destination, temporal scope, condition, cause, comparison, evidence, authority.  
* **Cardinality:** whether a role takes zero, one, or multiple values.  
* **Constraints:** required combinations, forbidden combinations, unit requirements, date formats, safety limits.  
* **Mappings:** transformations to and from APIs, JSON Schemas, SQL/query systems, event formats, or external ontologies.  
* **Rendering rules:** canonical visual order, grouping, relation markers, local labels, accessible text.  
* **Validation tests:** valid examples, invalid examples, ambiguous examples, and expected recovery behavior.  
* **Versioning and deprecation policy:** required for durable agent and software interoperability.

For example, an `agri-market:price-alert` frame might require:

Required:  
  commodity  
  market/location  
  metric  
  observation time  
  direction or threshold

Optional:  
  delivery period  
  quality grade  
  currency and unit  
  source  
  confidence  
  cause hypothesis  
  recommended follow-up

The Pictiq sequence stays short, but the Context Pack determines whether it is sufficiently specified to become an executable alert.

## **Bottom line**

Pictiq is most promising not as a universal replacement for semantic parsing, JSON, PDDL, AMR, or agent protocols, but as a **human-auditable, multilingual, compositional semantic IR** for bounded operational domains.

Its closest analogues are:

* Semantic frames, because both organize meaning around recurring situations and participant roles.\[[en.wikipedia](https://en.wikipedia.org/wiki/FrameNet)\]\[[academiccommons.columbia](https://academiccommons.columbia.edu/doi/10.7916/D81261XT/download)\]  
* Intent-and-slot systems, because both are well suited to constrained task interpretation.\[[aclanthology](https://aclanthology.org/2020.coling-main.42.pdf)\]  
* Controlled natural languages such as ACE, because both can trade unconstrained expression for inspectable, machine-processable structure.\[[research.vu](https://research.vu.nl/en/publications/attempto-controlled-english-for-knowledge-representation/)\]\[[arxiv](https://arxiv.org/abs/cmp-lg/9603003)\]  
* Tool-call schemas, because Pictiq can expose and validate a proposed action before execution.\[[modelcontextprotocol](https://modelcontextprotocol.io/specification/draft/server/tools)\]\[[developers.openai](https://developers.openai.com/api/docs/guides/structured-outputs)\]  
* FIPA/KQML-style agent protocols, because Pictiq can separate visible communicative acts from domain content, ontology declarations, and hidden routing metadata.\[[cdn.aaai](https://cdn.aaai.org/Workshops/1994/WS-94-02/WS94-02-007.pdf)\]\[[site.ieee](https://site.ieee.org/pes-mas/agent-technology/standards-and-interoperability/)\]

The analogy fails whenever the system needs lossless natural-language meaning, formal planning, open-world reasoning, subtle pragmatic intent, dense quantification, exact numerical/legal/medical specification, security, or autonomous high-stakes execution. In those cases, Pictiq should be the **inspectable front layer** of a more rigorous representation—not the layer that bears all semantic and operational responsibility.

