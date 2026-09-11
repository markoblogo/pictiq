Modern web and mobile interfaces already function as partial visual languages. They communicate action, hierarchy, status, priority, relationships, and interaction possibilities through icons, geometry, placement, color, motion, and state—often before users read a word.

But they are not language-free. Most successful interfaces rely on a **hybrid semantic system**: visual cues provide fast recognition and spatial context, while text supplies precise names, exceptions, instructions, legal meaning, data values, and recovery paths. For Pictiq, a Web/UI stress test should examine where its tile grammar can make existing UI semantics more explicit and portable—and where text, typed data, accessibility metadata, or domain schemas remain necessary.

## **UI as a visual language**

A UI element rarely communicates through a single icon. Meaning comes from a bundle of signals:

\\text{UI meaning}  
\=  
\\text{glyph}  
\+  
\\text{position}  
\+  
\\text{container}  
\+  
\\text{state}  
\+  
\\text{interaction feedback}  
\+  
\\text{surrounding context}.

Consider a magnifying-glass icon:

* In a persistent top bar, it likely means “search.”  
* Inside a product image, it may mean “zoom.”  
* Beside a map, it can mean “inspect this area.”  
* Attached to a data table, it may mean “filter or find.”  
* In an accessibility tool, it may mean “increase magnification.”

The pictogram is recognizable; its operational meaning is assigned by context. Nielsen Norman Group separates **recognizability**—does it look like the thing it depicts?—from **interpretation**—what does the user think it does in this specific UI? Icons can be recognized but still misinterpreted. Because most icons lack universal standardized use, visible labels are especially important for navigation.\[[nngroup](https://www.nngroup.com/articles/how-to-test-digital-icons/)\]\[[nngroup](https://www.nngroup.com/articles/icon-usability/)\]

A Pictiq stress test should therefore never evaluate tiles only as isolated drawings. It should test them:

* In their expected screen position.  
* With or without labels.  
* Before and after interaction.  
* At multiple sizes and contrast levels.  
* Alongside neighboring controls.  
* With keyboard, screen-reader, and touch use.  
* Across languages and familiarity levels.  
* In low-stakes and high-stakes task flows.

## **Taxonomy of UI semantics**

### **Navigation and orientation**

Navigation answers: **Where am I? Where can I go? What level am I at? Can I return?**

| Semantic function | Existing UI signals | Typical conventional forms | Pictiq opportunity | Main ambiguity/risk |
| ----- | ----- | ----- | ----- | ----- |
| Global navigation | Persistent top/bottom/side placement, grouping, active tab | Home, search, menu, profile | PLACE \+ GO; section tiles; current-location marker | Icon-only navigation is frequently ambiguous |
| Back | Left-pointing arrow, position in header, history stack | ←, chevron-left | RETURN / BEFORE / PREVIOUS | Can mean browser history, previous step, or collapse |
| Forward / next | Right arrow, wizard progression, order in form | →, chevron-right | NEXT / AFTER / CONTINUE | Can mean navigation, carousel movement, or submit |
| Up one hierarchy | Up arrow, breadcrumb, parent container | ↑, folder-up | ABOVE / PARENT / OUT | Often confused with scroll-to-top |
| Home | House icon, first tab, logo | House | HOME / START / MAIN | “Home” can mean dashboard, personal profile, or physical home |
| Menu / more options | Three lines, three dots, overflow placement | ☰, ⋮, … | OPTIONS / MORE / CHOOSE | “Hamburger” and kebab menus require learned conventions |
| Hierarchy | Indentation, breadcrumbs, nested cards, tree controls | `A > B > C`, folder tree | PART-OF, INSIDE, LEVEL | Spatial hierarchy becomes hard in linear tiles |
| Current location | Highlighted tab, bold text, filled icon, breadcrumb end | Active state | HERE / CURRENT / SELECTED | Color-only active states exclude some users |
| External destination | Diagonal arrow, link styling, target icon | ↗ | GO OUTSIDE / NEW PLACE | Can be missed without text or tooltip |
| Search scope | Search bar location, placeholder, filters, category chips | Magnifier, filter | FIND \+ \[DOMAIN\] | Search, filter, command palette, and zoom overlap visually |

Spatial position carries enormous meaning. A bottom tab bar usually denotes top-level destinations; an indented row usually denotes a child; a breadcrumb trail shows hierarchical location. Breadcrumbs explicitly represent navigation steps or levels in a hierarchy.\[[panel-material-ui.holoviz](https://panel-material-ui.holoviz.org/reference/menus/Breadcrumbs.html)\]

**Pictiq implication:** distinguish `GO BACK`, `GO NEXT`, `GO UP`, `GO HOME`, `OPEN`, `CLOSE`, `MORE`, and `SEARCH` as separate semantic operators. Do not collapse all arrows into one broad “direction” symbol when an interface action differs.

### **Actions and affordances**

Actions answer: **What can I do here? What will this control change?**

| Semantic function | Existing UI signals | Pictiq primitive / pattern | Notes |
| ----- | ----- | ----- | ----- |
| Create | Plus sign, floating action button, primary placement | ADD / MAKE / NEW | `+` can also mean zoom, expand, attach, or increase quantity |
| Edit | Pencil, inline focus, editable field affordance | CHANGE / EDIT | Pencil may mean annotate, draw, compose, or modify |
| Delete | Trash bin, destructive color, confirmation dialog | REMOVE / DELETE | Must be distinct from close, clear, archive, and cancel |
| Save | Disk icon, checkmark, autosave status | SAVE / KEEP / RECORD | Disk is increasingly a learned legacy metaphor |
| Share | Branch/arrow, system share sheet | SEND / SHARE / GIVE | Sharing may mean publish, invite, export, or copy link |
| Download | Downward arrow to tray | RECEIVE / TAKE / DOWNLOAD | Distinguish download from move-down, collapse, or decrease |
| Upload | Upward arrow to tray | SEND / PUT / UPLOAD | Distinguish upload from move-up or publish |
| Copy | Overlapping documents | COPY / DUPLICATE | Need separate semantics for copy link, duplicate record, or clone project |
| Move | Drag handle, arrows, destination highlight | MOVE / FROM / TO | Requires source, target, and sometimes ordering semantics |
| Undo / redo | Curved arrows, temporal ordering | UNDO / AGAIN | Must be tied to an action history, not only direction |
| Refresh | Circular arrow, pull-to-refresh | UPDATE / AGAIN / NOW | Can imply reload, retry, sync, or recompute |
| Filter | Funnel, chips, applied-filter count | FILTER / ONLY / MATCH | Need scope: what is being filtered? |
| Sort | Directional lines, headers, order indicators | ORDER / UP / DOWN | Sort order needs field and direction |
| Expand / collapse | Chevron, disclosure triangle, accordion state | OPEN / CLOSE; MORE / LESS | Chevron direction is heavily context-dependent |
| Play / pause / stop | Triangle, bars, square, playback timeline | START / WAIT / STOP | Playback, process execution, recording, and automation differ |
| Retry | Circular arrow plus error state | TRY AGAIN | Requires prior failure context |
| Call for help | Question mark, chat bubble, life ring | HELP / ASK / CONTACT | Help, documentation, support chat, and reporting a problem differ |

An icon is strongest when its physical metaphor aligns with a familiar direct action: trash → discard; pencil → edit; plus → add. Even then, labels provide important precision. Material Design treats icons as optional visual communicators for button actions and places them before the label; its own guidance is a reminder that icons normally complement words rather than replace them.\[[m3.material](https://m3.material.io/components/buttons/guidelines)\]\[[m3.material](https://m3.material.io/components/buttons/overview)\]

**Pictiq implication:** define action semantics independently of visual metaphor. A `DELETE` concept should have an explicit consequence model—remove permanently, remove from view, archive, clear input, or revoke access—not merely a bin-shaped glyph.

### **State, status, and feedback**

State answers: **What is true now? What changed? What can or cannot happen?**

WCAG describes state as a dynamic property of a UI component that can change through user action or automated processes. It gives examples including focus, hover, selected, pressed, checked, visited/unvisited, and expanded/collapsed.\[[w3](https://www.w3.org/WAI/WCAG21/Understanding/name-role-value.html)\]

| State family | Common visual encoding | Pictiq semantic form | Why it matters |
| ----- | ----- | ----- | ----- |
| Selected | Fill, highlight, checkmark, border, chip state | SELECTED / THIS / ACTIVE | Distinguish current selection from available option |
| Current / active | Underline, filled tab, bold label, color | HERE / NOW / ACTIVE | Navigation state is often carried mostly by position and color |
| Focused | Outline, ring, caret, elevation | FOCUS / READY | Essential for keyboard and assistive-technology use |
| Hovered / pressed | Color/elevation change, ripple, cursor | TOUCHING / PRESSED | Usually transient; may need no tile in a human message |
| Checked / unchecked | Checkbox mark, toggle position | YES / NO; INCLUDED / EXCLUDED | Boolean state must not depend only on color |
| Enabled / disabled | Opacity, muted color, reduced elevation | CAN / CANNOT / UNAVAILABLE | A disabled state signals non-interactivity; Material uses reduced elevation and color changes. \[[m3.material](https://m3.material.io/foundations/interaction/states/applying-states)\] |
| Available / unavailable | Green/red/gray, badge, inventory cue | AVAILABLE / NOT AVAILABLE | Requires scope: product, person, service, room, or feature |
| Connected / offline | Network glyph, dot color, reconnection cue | CONNECTED / NOT CONNECTED | May mean server, device, account, or collaboration presence |
| Synced / unsynced | Cloud/check, spinner, conflict badge | SYNCED / WAIT / CONFLICT | Needs source and time context |
| Draft / saved / published | Labels, cloud, check, status chips | DRAFT / SAVED / PUBLIC | Crucial when users assume a change is live |
| Processing / loading | Spinner, skeleton, progress bar | WORKING / WAIT / PROGRESS | Duration and cancellation availability may be essential |
| Success | Checkmark, green toast, completion card | DONE / SUCCESS | Should name what succeeded, not merely show a check |
| Warning | Yellow/amber icon, exclamation triangle | WARNING / CARE | Needs cause and required response |
| Error | Red styling, icon, inline message | ERROR / FAILED / FIX | Requires machine-readable error identification and human repair guidance |
| Empty | Illustration, blank state, primary CTA | NONE / EMPTY / ADD | “No data” can mean no results, loading, permission denial, or outage |
| Conflict | Merge symbol, red marker, competing values | CONFLICT / CHOOSE | Relevant for collaboration and sync |
| Stale | Timestamp, faded data, refresh prompt | OLD / UPDATE NEEDED | Important in live information, prices, schedules, alerts |

Status messages need explicit accessibility treatment. WCAG requires status-message changes to be programmatically determinable so assistive technologies can present them without moving focus. A Pictiq UI should similarly not rely only on a green check or red outline: the canonical semantic state must be available to screen readers, APIs, logs, and translations.\[[w3](https://www.w3.org/TR/WCAG22/)\]

### **Error, risk, and recovery**

Errors answer: **What went wrong? What is the consequence? What should I do next?**

| Semantic distinction | Weak visual shorthand | Better semantic structure | Pictiq stress-test requirement |
| ----- | ----- | ----- | ----- |
| Invalid input | Red border | FIELD \+ INVALID \+ REQUIRED FIX | Identify the failing field and error type |
| Missing required input | Asterisk or red text | FIELD \+ MISSING \+ REQUIRED | Distinguish absent from malformed |
| Format error | Red icon | VALUE \+ INVALID FORMAT \+ EXPECTED FORMAT | Include expected pattern or example |
| Permission denial | Lock icon | YOU \+ CANNOT \+ ACTION \+ REASON/POLICY | Distinguish from unavailable, broken, or not found |
| Network failure | Cloud/offline icon | CONNECTION \+ FAILED \+ RETRY | Separate offline, timeout, server error, and auth failure |
| Data conflict | Exclamation/badge | VERSION A ≠ VERSION B \+ CHOOSE/MERGE | Explain whose change conflicts |
| Destructive consequence | Red button, warning triangle | ACTION \+ REMOVE \+ WHAT \+ PERMANENCE | Show what is lost and whether undo exists |
| Irreversible action | Modal confirmation | ACTION \+ PERMANENT \+ CONFIRM | Require explicit confirmation |
| Partial completion | Check plus warning | SOME \+ DONE; SOME \+ FAILED | State scope and recovery path |
| Retryable failure | Circular arrow | FAILED \+ TRY AGAIN | Indicate whether retry is safe |
| System outage | Generic error page | SERVICE \+ UNAVAILABLE \+ STATUS \+ TIME | Do not conflate with user error |
| Security event | Shield/lock | SECURITY \+ EVENT \+ REQUIRED ACTION | Needs precise, accessible wording and verification |

WCAG requires that automatically detected input errors identify the item in error and describe the error in text; when user input is required, labels or instructions must be supplied. This matters for Pictiq because an elegant tile sequence cannot be deemed successful if users cannot discover what to correct.\[[w3](https://www.w3.org/TR/WCAG21/)\]

**Pictiq implication:** make error messages minimally complete:

\[FIELD:EMAIL\] \[ERROR\] \[INVALID-FORMAT\]  
\[FIX\] \[EMAIL-ADDRESS\]

\[PAYMENT\] \[FAILED\]  
\[REASON:AUTHORIZATION\]  
\[TRY-AGAIN\] \[OR\] \[CHANGE-CARD\]

A generic `[ERROR]` tile is only a category marker. It is not an actionable error message.

### **Permission, identity, and trust**

Permission answers: **Who can do what, with which scope, and why?**

| Concept | Common visual language | Why pure iconography struggles | Pictiq requirement |
| ----- | ----- | ----- | ----- |
| Private / public | Lock, globe, people icon | Public to whom? Searchable? Link-accessible? Indexed? | PRIVATE / PUBLIC plus audience scope |
| View / comment / edit / administer | Eye, speech bubble, pencil, gear | Roles are action bundles, not simple objects | CAN \+ VIEW/COMMENT/EDIT/MANAGE |
| Ownership | Avatar, crown, “you” marker | Owner, creator, payer, legal controller differ | OWNER / CREATOR / RESPONSIBLE |
| Authentication | Lock, biometric, key icon | Logged in, verified, reauthenticated, trusted device differ | SIGNED-IN / VERIFY / PROVE-IDENTITY |
| Authorization | Disabled button, lock | Could mean policy, subscription, missing role, or expired access | CANNOT \+ ACTION \+ REASON |
| Sharing scope | Person, group, link, globe | “Anyone with link” differs from public internet | SHARE \+ WHO \+ ACCESS MODE |
| Consent | Checkbox, toggle | Consent must be informed, specific, revocable, recorded | AGREE / DO NOT AGREE \+ PURPOSE \+ CHANGE LATER |
| Security warning | Shield/triangle | Need threat type, affected account, recommended action | WARNING \+ SECURITY \+ ACTION |
| Provenance | Source logo, timestamp, verified badge | “Verified” by whom and under what method? | SOURCE \+ CHECKED \+ TIME \+ AUTHORITY |
| Subscription / entitlement | Crown, star, lock | Trial, paid tier, expired plan, regional restriction differ | HAS / NEEDS PLAN / EXPIRES / UPGRADE |

Permissions remain difficult without language because they encode **normative and legal relationships**, not merely visible state. A lock can mean secure, private, unavailable, paid, restricted, encrypted, archived, or disabled.

For Pictiq, the safe model is:

\[YOU\] \[CAN\] \[VIEW\] \[DOCUMENT\]  
\[YOU\] \[CANNOT\] \[EDIT\] \[DOCUMENT\]  
\[REASON\] \[NEED\] \[PERMISSION\]  
\[ASK\] \[OWNER\]

But a live system still needs canonical policy data—user IDs, role assignments, object IDs, organization, expiry, legal basis, and audit records.

### **Hierarchy, grouping, and information architecture**

Layout itself communicates semantic relationships.

| Visual structure | Meaning normally inferred | Pictiq analogue | Difficulty |
| ----- | ----- | ----- | ----- |
| Containment | This item belongs inside this panel, card, folder, modal, or group | INSIDE / PART-OF / GROUP | Nested scope becomes visually dense |
| Proximity | Items are related | WITH / ABOUT / GROUP | Proximity can be ambiguous without relation markers |
| Alignment | Items have the same role or type | SAME-LEVEL / LIST | Useful but often implicit |
| Repetition | Repeated cards represent repeated records | MANY / LIST / EACH | Need to distinguish instances from categories |
| Order | Sequence, priority, chronology, rank | BEFORE / AFTER / FIRST / NEXT | Reading order changes across locale/layout |
| Size | Importance, quantity, emphasis, hierarchy | MORE / IMPORTANT / BIG | Size can mean content size, popularity, or decoration |
| Whitespace | Separation, grouping, emphasis | BREAK / NEW GROUP | Mostly invisible to machine parsing unless encoded |
| Z-order / overlay | Modal priority, tooltip, temporary interruption | ABOVE / ATTENTION / BLOCKS | Can hide context and confuse assistive tools |
| Card nesting | Parent/child or summary/detail | SUMMARY / DETAILS | Requires explicit expand/collapse semantics |
| Table columns | Shared attribute structure | FIELD / VALUE / RECORD | Difficult to reduce to unlabelled visual tiles |
| Timeline | Time progression and events | TIME \+ BEFORE/AFTER \+ EVENT | Needs date/time values for precision |
| Map layout | Geography, distance, direction, route | PLACE \+ GO \+ FROM/TO | Must separate physical map relation from UI placement |

A future Pictiq grammar should distinguish:

adjacency        \= related or sequential  
containment      \= belongs to / scope applies to  
attachment       \= modifier applies to target  
alignment        \= peer items / same role  
arrow            \= direction, causality, or navigation—never all by default  
overlay          \= temporary priority or dialog state

Without such distinctions, Pictiq may be able to name UI elements but not represent their relationships.

### **Selection, comparison, and choice**

Selection answers: **What is chosen? What is available? Is the choice singular, plural, mandatory, temporary, or final?**

| Selection meaning | UI convention | Pictiq representation | Ambiguity to test |
| ----- | ----- | ----- | ----- |
| Choose one | Radio button, segmented control | CHOOSE ONE \+ OPTION | Must distinguish from a list of actions |
| Choose many | Checkbox, multi-select chips | CHOOSE MANY \+ INCLUDED | Must show whether selection is additive |
| Toggle binary setting | Switch, checkbox | ON / OFF | Switches can represent immediate action or saved setting |
| Current filter | Selected chip, filled pill | FILTER \+ ACTIVE | Needs clear scope and removal mechanism |
| Favorite / saved item | Heart, star, bookmark | KEEP / FAVORITE / SAVE-LATER | Heart/star conventions vary by product |
| Selected rows | Checkboxes, highlighted table rows | SELECTED \+ COUNT | Need distinction between selected and merely focused |
| Range selection | Slider handles, date range | FROM \+ VALUE \+ TO \+ VALUE | Hard to represent without typed values |
| Comparison | Side-by-side cards, check columns | COMPARE \+ A \+ B | Attribute basis must be named |
| Recommended choice | Badge, highlight, placement | RECOMMENDED / BEST-FIT | Recommendation needs reason, source, and personalization context |
| Default | Preselected choice, hint text | DEFAULT / SUGGESTED | Must distinguish default from saved preference |
| Locked choice | Grayed item, lock | UNAVAILABLE / NEEDS ACCESS | Explain why it cannot be selected |

This is an area where UI visual language is very strong for simple interactions, but language becomes essential when the consequences differ:

One radio choice:  
“Choose one delivery method.”

Checkbox group:  
“Choose all preferences that apply.”

Toggle:  
“Automatically renew subscription.”

Button:  
“Renew now.”

All may include a check, switch, or selection marker, but they encode different temporal and legal consequences.

## **Concepts difficult without language**

Some UI meanings can be communicated visually only at a rough level. They require text, typed data, or a detailed Pictiq grammar when users must act precisely.

| Difficult concept | Why icons/layout alone fail | Minimum structured support |
| ----- | ----- | ----- |
| Exact time | Clock icons show “time,” not “Friday 11 September, 13:30 CEST” | Date, time, timezone, recurrence, deadline |
| Price and total cost | Currency and price tags do not express taxes, shipping, subscription renewal, unit price, discounts, exclusions | Amount, currency, unit, tax, billing period, total, conditions |
| Terms and legal rights | A lock or checkmark cannot convey consent scope, withdrawal rights, liability, contract change | Legal text, version, jurisdiction, consent record |
| Permission rationale | Lock cannot say whether access is blocked by role, ownership, payment, geography, age, or policy | Action, subject, object, reason, path to remedy |
| Error cause and repair | Red styling says “problem” but not what broke or how to fix it | Error code/type, affected field/object, proposed correction |
| Uncertainty | Gray, yellow, or dotted line rarely distinguishes likely, estimated, missing, delayed, disputed, or unknown | Confidence, source, freshness, estimate flag |
| Comparison basis | Up arrow does not say “up from what?” | Reference value/time, magnitude, unit, method |
| Scope | A `NOT` symbol may apply to one item, a group, or a condition | Explicit grouping, binding, or syntax |
| Quantification | One/many/all/some/none and ranges have different operational meanings | Number, cardinality, quantifier, unit |
| Conditional logic | “If X, then Y unless Z” is not reliably icon-only | IF, THEN, UNLESS, AND, OR, parentheses/scope |
| Causality | Arrow can mean cause, sequence, direction, transfer, or navigation | CAUSE, LEADS-TO, BECAUSE, AFTER |
| Data provenance | Badge or logo is insufficient to show source, retrieval time, transformation, authority | Source ID, timestamp, method, confidence |
| Identity resolution | Avatar does not identify which person/account/entity | Stable ID, display name, organization context |
| Financial commitment | Cart/checkout imagery does not convey who pays, when, what repeats, and whether action is final | Amount, payer, schedule, cancellation, confirmation |
| Medical or safety instruction | Familiar warning symbols do not capture contraindications, dose, exception, or action sequence | Controlled text, specialist schema, confirmation |
| Privacy choices | Toggle may hide collection purpose, recipients, retention, and consequences | Purpose, data types, sharing recipients, expiry, revocation |
| Abstract concepts | “Sync,” “algorithm,” “privacy,” “AI inference,” “subscription,” “ownership,” “license” are not consistently picturable | Labels, definitions, contextual examples |
| Social tone | A smile or heart does not reliably encode politeness, sarcasm, consent, urgency, or authority | Explicit intent and conventional language |
| Novel domain terms | A user cannot infer a new financial, technical, or administrative concept from a novel icon | Context Pack, label, onboarding, glossary |
| Complex multi-step plans | A linear icon row hides branching, dependencies, resources, and failure paths | Workflow diagram, structured plan, expanded details |

This is not a weakness unique to Pictiq. It is the boundary of visual communication generally. The most effective approach is **progressive semantic disclosure**: show a compact tile summary first, then make exact text, values, provenance, and validation inspectable on demand. Progressive disclosure is specifically intended to reduce cognitive overload by sequencing information and exposing detail when needed.\[[ixdf](https://ixdf.org/literature/book/the-glossary-of-human-computer-interaction/progressive-disclosure)\]

## **Web/UI × Pictiq taxonomy**

A future stress test can treat each UI meaning as a structured Pictiq frame rather than as an isolated icon.

### **Core frame types**

| Pictiq UI frame | Required semantic fields | Optional fields | Example visible summary |
| ----- | ----- | ----- | ----- |
| `NAVIGATE` | actor, destination, navigation mode | origin, hierarchy level, external/internal | `[GO] [HOME]` |
| `OPEN_CLOSE` | target, desired state | current state, scope | `[OPEN] [MENU]` |
| `SEARCH` | search domain or query target | filters, sort, scope, result count | `[FIND] [HOTEL] [NANTES]` |
| `CREATE_EDIT` | action, target type | source, owner, draft state | `[NEW] [NOTE]` |
| `REMOVE` | target, permanence | undo availability, impact count, reason | `[DELETE] [3] [FILES]` |
| `SELECT` | selection mode, target/options | count, default, availability | `[CHOOSE-ONE] [DELIVERY]` |
| `SET_VALUE` | field, value, type/unit | validation, default, source | `[DATE] [12 SEP]` |
| `SUBMIT_CONFIRM` | proposed action, object | consequences, finality, recipient | `[CONFIRM] [PAY] [€24.90]` |
| `STATUS` | entity/process, state | time, source, confidence, next action | `[SYNC] [DONE]` |
| `LOAD_PROGRESS` | process, progress state | percentage, ETA, cancel availability | `[UPLOAD] [WORKING] [63%]` |
| `ERROR_REPAIR` | affected target, error type | reason, repair action, support route | `[EMAIL] [ERROR] [FIX]` |
| `PERMISSION` | subject, capability, resource | authority, reason, expiry, request path | `[YOU] [CANNOT] [EDIT] [FILE]` |
| `ALERT` | event/risk, severity, required action | area, time, authority, certainty | `[WARN] [FLOOD] [GO] [UP]` |
| `COMPARE` | entities, comparison basis | values, source, period, recommendation | `[COMPARE] [A] [B] [PRICE]` |
| `TRANSACTION` | action, payer/recipient, object, amount | currency, tax, renewal, cancellation | `[PAY] [€24.90] [NOW]` |
| `FORM` | field type, expected value | requiredness, format, example, error state | `[ENTER] [EMAIL]` |
| `NOTIFICATION` | event, target, attention level | origin, time, read state, action | `[NEW] [MESSAGE]` |
| `CONTEXT` | current location/domain/task | pack, role, mode, locale | `[TRAVEL] [BOOKING] [NANTES]` |
| `HELP` | topic/problem, help mode | documentation, contact, escalation | `[HELP] [PAYMENT]` |
| `ACCESSIBILITY` | access need or alternative mode | output type, preference, device state | `[SPEAK] [TEXT]`, `[HIGH-CONTRAST] [ON]` |

### **Status modifiers**

Pictiq could use a stable visual/semantic modifier layer for UI state:

ACTIVE  
SELECTED  
FOCUSED  
OPEN  
CLOSED  
AVAILABLE  
UNAVAILABLE  
WORKING  
WAITING  
DONE  
FAILED  
WARNING  
NEW  
READ  
SAVED  
UNSAVED  
SYNCED  
OFFLINE  
LOCKED  
EXPIRED

The important rule: a visible rendering can use color, fill, animation, and position, but the canonical semantic state must not depend on any one of them. WCAG requires programmatically determinable names, roles, values, states, and status-message changes for UI components and assistive technologies.\[[w3](https://www.w3.org/TR/WCAG22/)\]

## **Design rules for a Pictiq UI test**

### **Treat visual cues as grammar**

Define what each visual relation means:

Tile inside container       \= scope / membership  
Tile attached at top-right  \= status modifier  
Tile before another tile    \= temporal or interaction sequence  
Tile under another tile     \= detail / parameter / dependent value  
Arrow                       \= one declared relation per profile  
Filled tile                 \= selected or active, not both unless defined  
Muted tile                  \= unavailable, not merely less important  
Badge count                 \= quantity of notifications/items/errors

A Pictiq Web/UI profile should prevent the same visual treatment from carrying unrelated operational meanings.

### **Separate transient state from persistent meaning**

Some UI cues are only interaction feedback:

* Hover.  
* Pressed state.  
* Focus ring.  
* Ripple animation.  
* Drag preview.  
* Skeleton loader.  
* Snackbar/toast.

They often should not become part of a durable Pictiq message. A screenshot may show them, but a semantic export should distinguish:

{  
  "persistent\_state": "unsaved",  
  "transient\_interaction\_state": "button\_pressed",  
  "announcement": "Saving draft"  
}

Otherwise Pictiq could confuse “currently being pressed” with “requested,” “active,” or “completed.”

### **Make semantics accessible and reversible**

For every icon-only or tile-only control, test whether the system exposes:

* An accessible name.  
* A programmatic role: button, link, checkbox, tab, slider, dialog, menu item, input.  
* A current state: selected, expanded, checked, disabled, invalid, busy.  
* A value where relevant: amount, progress, selected date, slider value.  
* A visible or discoverable explanation.  
* A keyboard-operable equivalent.  
* A text/speech expansion.  
* A way to correct or undo consequential actions.

Focus order must preserve meaning and operability when a page is navigated sequentially. That is an ideal test for Pictiq’s linear grammar: if the tile order is not understandable with keyboard focus alone, the visual sequence is likely underspecified.\[[digitala11y](https://www.digitala11y.com/focus-order-understanding-sc-2-4-3/)\]

### **Separate “recognizable” from “actionable”**

A tile may be easy to name yet poor at communicating what will happen.

Recognizable:  
A heart looks like a heart.

Potential interpretations:  
Like, save, favorite, health, care, donation, emotional content,  
relationship status, or product recommendation.

Actionable only with context:  
\[HEART\] in a product grid may mean “save to favorites.”  
\[HEART\] beside a patient may mean “cardiology.”  
\[HEART\] in a social feed may mean “react positively.”

A Pictiq test should record both:

1. **Recognition rate:** “What do you see?”  
2. **Interpretation rate:** “What happens if you activate this?”  
3. **Outcome rate:** “Can you complete the intended task without help?”  
4. **Confidence:** “How certain are you?”  
5. **Recovery:** “Can you undo or repair a wrong interpretation?”

## **Twenty concrete test cases**

The following cases are designed as a practical Web/UI × Pictiq stress suite. Each has a task, semantic burden, and a failure condition. Test each in at least three render modes: icons/tiles only, tiles plus short labels, and full expanded accessible text.

| \# | Test case | User task | Core semantics Pictiq must express | Failure signal |
| ----- | ----- | ----- | ----- | ----- |
| 1 | Back versus close | Leave a product-detail modal without losing the search-results context | CLOSE MODAL, not GO BACK or DELETE | User exits to wrong page or believes data was discarded |
| 2 | Home versus physical address | Return to application dashboard from a travel itinerary | GO \+ APP HOME, not HOUSE/ACCOMMODATION | House tile is read as lodging/location |
| 3 | Search versus filter | Find wheat records for Rouen, then show only records above a chosen price | SEARCH QUERY versus FILTER CONDITION | User enters a filter as text search or assumes search changes dataset scope |
| 4 | Add versus expand | Add a new shipment record rather than expand a shipment row | CREATE NEW versus OPEN DETAILS | Plus sign opens an accordion or vice versa |
| 5 | Save versus publish | Save a draft article without making it public | SAVE DRAFT versus PUBLISH PUBLIC | User believes saved content is live or publishes accidentally |
| 6 | Delete versus archive | Remove a file permanently versus hide it in an archive | DELETE PERMANENTLY versus ARCHIVE RECOVERABLY | Recovery expectation is wrong |
| 7 | Single versus multiple selection | Select exactly one delivery method, then select all applicable notification channels | CHOOSE ONE versus CHOOSE MANY | User chooses multiple mutually exclusive options |
| 8 | Toggle versus immediate action | Turn automatic price alerts on versus send a test alert now | SETTING ON/OFF versus DO ACTION NOW | User assumes a toggle performs a one-off operation |
| 9 | Active tab versus available tab | Identify current dashboard section and navigate to another | HERE/ACTIVE versus GO TO | Highlight is missed or color-only |
| 10 | Disabled versus unavailable due to permissions | Attempt to edit a shared report without edit rights | CANNOT EDIT \+ REASON \+ ASK OWNER | User reads muted button as broken/loading rather than restricted |
| 11 | Required input and format error | Enter an email address and correct a malformed value | ENTER EMAIL \+ REQUIRED \+ INVALID FORMAT \+ FIX | Only red border appears; user cannot identify or repair error |
| 12 | Loading versus empty result | Search for an uncommon town and distinguish “still loading” from “no results” | WORKING versus NONE FOUND | User retries or abandons during a slow valid search |
| 13 | Progress and cancellation | Upload 50 photos, understand 63% progress, and cancel with known consequence | UPLOAD \+ 63% \+ CANCEL \+ LOST/SAFE | User cannot tell whether cancellation loses completed uploads |
| 14 | Confirmation before payment | Confirm a €24.90 recurring monthly subscription | PAY \+ AMOUNT \+ CURRENCY \+ RECURS MONTHLY \+ CONFIRM | User interprets confirmation as a free trial or one-time purchase |
| 15 | Price comparison basis | Understand that wheat is up 3.7% from the previous close, not simply “high” | PRICE \+ UP \+ 3.7% \+ COMPARED TO \+ PREVIOUS CLOSE | Up-arrow is interpreted as expensive rather than changed |
| 16 | Date, timezone, and deadline | Schedule a report for 16:00 CEST tomorrow | TIME \+ DATE \+ TIMEZONE \+ DEADLINE | A user in another timezone executes at the wrong time |
| 17 | Permission-sharing scope | Share a document with a named team as commenters, not publicly or as editors | SHARE \+ GROUP \+ COMMENT \+ NOT PUBLIC | User exposes a file publicly or grants edit rights |
| 18 | Notification priority | Distinguish an informational update from an urgent failure requiring immediate action | INFORM versus WARN/URGENT \+ REQUIRED ACTION | User ignores an actionable incident or overreacts to routine status |
| 19 | Undo and irreversible effects | Remove five selected records, learn whether undo is available, and restore if possible | REMOVE \+ FIVE \+ UNDO AVAILABLE / PERMANENT | User cannot predict consequences or recover a mistake |
| 20 | Agent action preview | Review an AI-proposed market alert before it is created | MONITOR \+ WHEAT \+ BASIS \+ ROUEN \+ TOMORROW \+ IF WIDEN \> €3/t \+ ALERT SELF | Missing threshold, recipient, market, or time makes the action ambiguous |

A good benchmark result is not merely “participants guessed the icon.” It is:

The participant identified the current state,  
predicted the result of interaction,  
completed the intended action,  
recognized any consequential condition,  
and successfully recovered from a deliberate error.

## **Bottom line**

Web and mobile interfaces already prove that people can read a rich visual grammar: placement conveys hierarchy, containers convey scope, shape implies control type, fill and contrast indicate state, arrows imply movement, badges indicate counts, and motion signals progress or feedback. But these cues work because users bring learned conventions and because text, screen-reader semantics, typed values, and predictable interaction patterns quietly supply the missing precision.\[[nngroup](https://www.nngroup.com/articles/icon-usability/)\]\[[w3](https://www.w3.org/TR/WCAG22/)\]

For Pictiq, the Web/UI stress test should focus on the boundary between:

Visual shorthand that is context-sufficient:  
HOME, BACK, SEARCH, ADD, PLAY, STOP, SELECTED, DONE.

Visual shorthand that needs explicit grammar or data:  
permission, price basis, time zone, consent, error cause,  
scope, irreversible consequence, uncertainty, condition,  
identity, legal status, and multi-step action.

The design goal is not an icon-only interface. It is a Pictiq-enhanced semantic interface where tiles make actions and states quickly legible, while the underlying protocol preserves names, roles, values, consequences, accessibility equivalents, and exact structured meaning.

