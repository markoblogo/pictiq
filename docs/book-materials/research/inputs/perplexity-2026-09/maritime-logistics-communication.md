Multilingual maritime, port, warehouse, and logistics work already relies on layered standardization: controlled maritime English, fixed radio phrases, signal flags, hand signals, hazard placards, packaging marks, and safety signage. These systems reduce ambiguity for recurring operational situations, but misunderstandings persist where a message requires exact identity, quantity, authority, timing, condition, or procedural state.

Pictiq could plausibly represent compact operational messages—movement, location, cargo class, visible condition, basic hazard, equipment status, and simple sequence—if it keeps a strict grammar and treats formal cargo documentation, dangerous-goods declarations, navigation orders, and release authority as linked structured data rather than icon-only meaning.

## **Existing language layers**

### **Maritime English and radio procedure**

The International Maritime Organization’s Standard Marine Communication Phrases, or SMCP, exist specifically to reduce language barriers and prevent safety-relevant misunderstandings in ship-to-ship, shore-to-ship, onboard, port-approach, harbor, and berthing communication. Adopted in 2001, the phrases use a simplified version of maritime English and cover routine as well as emergency situations.\[[imo](https://www.imo.org/en/ourwork/safety/pages/standardmarinecommunicationphrases.aspx)\]

SMCP is intentionally restrictive:

* It uses short, standardized wording.  
* It avoids synonyms and contractions.  
* It limits conditional wording such as “might” or “could.”  
* It favors full, explicit answers rather than elliptical “yes/no” replies.\[[mitags](https://www.mitags.org/what-are-standard-marine-communication-phrases/)\]  
* It uses agreed question/answer structures for safety-critical exchanges.  
* It assumes a baseline ability to use maritime English.

A typical operational contrast is revealing:

Unsafe informal wording:  
“Maybe you can come a bit closer after that ship passes?”

Controlled operational wording:  
“Keep clear of vessel ahead.”  
“Proceed to berth number 4.”  
“Stand by on VHF channel 12.”

The second style compresses social niceties and stylistic variation but preserves the command, target, and action.

**Pictiq lesson:** a port/ship visual protocol should not replace SMCP radio communication. It can make the same structure visible as a supplementary confirmation layer:

\[VESSEL\] \[KEEP CLEAR\] \[VESSEL AHEAD\]  
\[THEN\] \[GO\] \[BERTH 4\]  
\[LISTEN\] \[RADIO\] \[CHANNEL 12\]

The visible sequence might support training, noisy environments, handoff boards, checklists, and multilingual crews. The radio exchange, professional judgement, and maritime procedure remain authoritative.

### **International Code of Signals**

The International Code of Signals, ICS, provides internationally standardized communication for situations involving safety of navigation and persons, particularly when language difficulties arise. Each signal or group of signals carries a complete assigned meaning, and the system may use flags, radio, and other means.\[[dco.uscg](https://www.dco.uscg.mil/Portals/9/NMC/pdfs/examinations/Pub102_2020.pdf)\]\[[imo-epublications](https://imo-epublications.org/content/books/9789280117387)\]

The system demonstrates three relevant principles:

1. **A small visual inventory can encode urgent operational meaning.**  
   Signal flags can convey alphabetic content, but individual flags may also have assigned whole-message meanings. For example, Alpha means a diver is down and vessels should keep clear at slow speed; Oscar means “man overboard”; Quebec signals a request for free pratique; Papa calls persons to report aboard.\[[amnautical](https://www.amnautical.com/blogs/the-mariners-blog/international-maritime-signal-flags)\]  
2. **Some messages are lexicalized because speed matters.**  
   “Man overboard” is too important and frequent to reconstruct through a long letter sequence in an emergency.  
3. **Acknowledgment matters.**  
   The Code specifies that a signal group should remain displayed until an answer is received.\[[dco.uscg](https://www.dco.uscg.mil/Portals/9/NMC/pdfs/examinations/Pub102_2020.pdf)\]

For Pictiq, this argues for a distinction between:

Composable operational grammar:  
\[PERSON\] \[IN WATER\] \[NEED HELP\]

Conventional emergency shorthand:  
\[PERSON OVERBOARD\]

The compositional form is teachable and general. The conventional form may be faster where it is standardized, repeatedly trained, and has a single high-priority operational interpretation.

### **Port, warehouse, and dock communication**

Dock work already combines vocal calls, radio, hand signals, visual signs, markings, flashing lights, exclusion zones, PPE rules, and trained procedures. Port safety guidance identifies hand signalling as an essential means of communication between shore workers and between ship and shore, and explicitly notes that signs should be understandable regardless of language or literacy.\[[hsa](https://www.hsa.ie/media/13inxopw/dock-work-cop.pdf)\]

At the same time, operational reality remains difficult:

* Crews, drivers, contractors, terminal staff, surveyors, and vessel personnel may not share a first language.  
* Ambient noise, wind, machinery, radio interference, poor lighting, rain, PPE, distance, and line-of-sight restrictions degrade communication.  
* One person may see the cargo, another controls the crane, another manages vehicle movement, and another owns the release decision.  
* A hand signal can be misunderstood, missed, or applied to the wrong object.  
* A visual sign can identify a hazard but not necessarily the exact handling procedure.  
* The pace of container, breakbulk, bulk, and Ro-Ro operations encourages shorthand.  
* Shift changes create state-loss: “what has been checked, released, moved, damaged, quarantined, or still requires action?”

The ILO maintains a revised code of practice on safety and health in ports, reflecting that port work has substantial occupational-safety demands.\[[imo](https://www.imo.org/en/OurWork/Facilitation/Pages/ILOCode-Default.aspx)\]

**Pictiq lesson:** prioritize messages that are visible, local, and immediately actionable; do not ask a compact visual language to carry hidden operational state or legal authority.

## **Where pictograms already work**

### **Safety signage and mandatory actions**

ISO 7010 defines standardized safety signs used for accident prevention, fire protection, health-hazard information, and emergency evacuation. Its visual grammar uses shape and color as semantic categories:\[[standards.iteh](https://standards.iteh.ai/catalog/standards/iso/85a8f8af-db94-4af2-89c8-da5a8a2dda8b/iso-7010-2019)\]

| Visual form | Typical meaning family | Logistics examples |
| ----- | ----- | ----- |
| Red circle with diagonal bar | Prohibition | No entry, no smoking, no unauthorized personnel |
| Blue circle | Mandatory action | Wear helmet, eye protection, hearing protection |
| Yellow triangle | Warning | Forklift traffic, suspended load, slippery surface |
| Green rectangle/square | Safe condition | Emergency exit, first aid, assembly point |
| Red rectangle/square | Fire equipment | Fire extinguisher, alarm point, hose reel |

For example, safety-sign guidance describes mandatory signs as blue circles with white graphics, and prohibited actions as white circles with a red border and a red diagonal bar.\[[seton](https://www.seton.com/iso-7010-regulations)\]

These signs are strong because they communicate a limited action class:

\[NO ENTRY\]  
\[WEAR HELMET\]  
\[WATCH FOR FORKLIFTS\]  
\[EMERGENCY EXIT\]  
\[FIRST AID\]

They are weak for questions such as:

“Is this zone closed only while crane 3 is working?”  
“Which contractor may enter after induction?”  
“Where should hazardous container ABCD1234567 be staged?”  
“Has this release hold been cleared?”

Those require identity, time, authority, condition, and procedural state.

### **Cargo handling marks and orientation**

Cargo handling uses durable, highly conventional marks: arrows for “this way up,” umbrella-like keep-dry imagery, fragile glass, temperature or handling constraints, and dangerous-goods labels. Orientation arrows are mandated in specified dangerous-goods configurations, including relevant liquid-containing combination packages and certain overpacks; regulations require the arrows on opposite sides and specify dimensions and contrast.\[[thecompliancecenter](https://www.thecompliancecenter.com/help-center/articles/orientation-arrow-requirements/)\]\[[danielstraining](https://danielstraining.com/use-of-package-orientation-arrows-in-the-iata-dangerous-goods-regulations/)\]

These marks encode simple physical constraints:

\[UP\]  
\[KEEP DRY\]  
\[FRAGILE\]  
\[KEEP COLD\]  
\[DO NOT STACK\]  
\[HAZARDOUS\]

They work because:

* The referent is physically present.  
* The action is narrow and immediate.  
* The signal can be repeated on packaging.  
* Meaning must remain visible across language boundaries.  
* The user is usually trained or at least familiar with the handling convention.

They do not substitute for shipping documents, packing certificates, declarations, or cargo-specific instructions.

### **Dangerous-goods labels and placards**

The IMDG Code governs dangerous goods transported by sea, including classification, packaging, marking, documentation, stowage, and segregation. Standard hazard labels provide immediate category recognition—flammable, toxic, corrosive, radioactive, explosive, oxidizing, and environmentally hazardous—while required text and identifiers provide the precise legal/operational identity.\[[shipfinex](https://www.shipfinex.com/blog/imdg-code)\]

For example, dangerous-goods packages typically require a UN number, proper shipping name, and other marks; hazard labels are standardized diamond forms, while cargo transport units require larger placards.\[[shipfinex](https://www.shipfinex.com/blog/imdg-code)\]\[[hseblog](https://www.hseblog.com/imdg-code/)\]

This is a critical model for Pictiq:

Visual layer:  
\[FLAMMABLE\] \[UP\] \[KEEP AWAY\]

Structured/legal layer:  
UN number  
proper shipping name  
hazard class/division  
subsidiary risk  
packing group  
net quantity  
flash point where required  
segregation/stowage rules  
shipper/consignee data  
documentation and declaration

The pictogram rapidly signals **danger class**. It cannot safely encode the full dangerous-goods record.

## **Where misunderstandings persist**

Even with standardized words and signs, ambiguity remains at the boundaries between message, operational state, and responsibility.

| Communication problem | Why a sign or short phrase is insufficient | Example of harmful ambiguity | Pictiq implication |
| ----- | ----- | ----- | ----- |
| Object identity | Generic cargo or equipment icon does not identify the actual unit | “Move container” but which of hundreds? | Use a typed ID, barcode/RFID, container number, or linked record |
| Quantity/unit | A number without unit or basis is dangerous | “20” could be 20 pallets, tonnes, containers, liters, or minutes | Require number \+ unit \+ measured object |
| Location | “Dock,” “bay,” and “yard” may have multiple local meanings | “Take it to bay 4” but there are warehouse and quay bay 4s | Require named/encoded location and map reference |
| Direction | Arrow alone may mean route, orientation, motion, next step, or displacement | “This way up” confused with “move cargo upward” | Declare arrow role: route, object orientation, process sequence, or movement |
| Actor/authority | A worker may see an instruction but not know who is authorized to act | “Open container” without customs/release authority | Separate instruction from authorization and identity |
| Timing | “Later,” “today,” or a clock icon may be insufficient | “Load after inspection” without inspection completion/time | Use status \+ timestamp \+ prerequisite |
| State | Visual color may not show whether a process is planned, active, finished, failed, or paused | Green tag interpreted as safe rather than released | Use explicit lifecycle states |
| Condition | “Damaged” can range from cosmetic scrape to compromised seal or leak | Driver continues with leaking package | Define observed condition and escalation action |
| Hazard detail | Hazard class icon is not the specific substance/procedure | “Flammable” does not tell crew what to do for UN-specific spill response | Keep formal IMDG/DG documentation linked |
| Sequence | A row of icons does not make dependency or exception clear | “Inspect, lift, move” but lift only after permit release | Use THEN, IF, CHECK, CONFIRM, STOP |
| Negation/scope | `NOT` can bind to the wrong tile | “Do not load cargo after check” vs. “do not load unchecked cargo” | Use grouping/scope markers and test them |
| Weather and visibility | Cloud/wind/wave symbols omit thresholds and source | “High wind” without crane wind limit | Pair with measured value, threshold, timestamp, authority |
| Human condition | “Tired,” “injured,” or “unsafe” needs follow-up and confidentiality | Worker’s symptom treated as fit-to-work status | Use as prompt/escalation, not diagnosis/clearance |
| Cross-shift handoff | Static sign cannot represent current evolving facts | “Inspection complete” remains up after a new damage finding | Require live status source, time, owner, and expiry |
| Legal/customs status | Symbols cannot convey hold reason, release condition, or appeal path | Cargo moved before customs release | Do not use pictograms as authoritative legal clearance |

A useful rule is:

> Pictograms are good at **classifying what is visible and directing an immediate action**. They are weak at proving identity, authority, measurement basis, legal status, exceptions, and dynamic operational history.

## **Pictiq scope for logistics**

Pictiq should not compete with IMO communication, IMDG documentation, port operating systems, warehouse management systems, EDI, AIS, cargo manifests, or radio procedure. It can operate between them as a compact human-readable visual layer.

### **Strong candidate message families**

| Message family | Pictiq feasibility | Example |
| ----- | ----- | ----- |
| Direction and route | High | `[TRUCK] [GO] [GATE 3]` |
| Immediate movement control | High with trained use | `[STOP] [FORKLIFT]`, `[WAIT]`, `[GO]`, `[KEEP CLEAR]` |
| Basic cargo class | High | `[CONTAINER]`, `[BULK]`, `[PALLET]`, `[BAG]`, `[TANK]` |
| Visible cargo condition | Moderate–high | `[CARGO] [WET]`, `[BOX] [DAMAGED]`, `[SEAL] [BROKEN]` |
| Handling constraint | High | `[UP]`, `[KEEP DRY]`, `[FRAGILE]`, `[KEEP COLD]`, `[NO STACK]` |
| Equipment state | Moderate | `[CRANE] [WORKING]`, `[FORKLIFT] [NOT AVAILABLE]` |
| PPE and zone safety | High | `[HELMET] [MUST]`, `[NO ENTRY]`, `[DANGER] [SUSPENDED LOAD]` |
| Simple handoff | Moderate | `[TRUCK] [ARRIVED]`, `[CARGO] [READY]`, `[CHECK] [DONE]` |
| Procedure checklist | Moderate–high | `[CHECK SEAL] → [WEIGH] → [LOAD] → [CONFIRM]` |
| Weather status | Moderate | `[WIND] [HIGH]`, `[RAIN]`, `[VISIBILITY] [LOW]` |
| Basic emergency action | High in trained context | `[FIRE] [ALARM] [EXIT]`, `[SPILL] [STOP] [CALL]` |
| Quantified operational status | Moderate with strict typed values | `[PALLET] [24] [READY]`, `[WEIGHT] [18.4] [TONNE]` |
| Conditional operational rule | Moderate only with clear grammar | `[IF] [WIND > LIMIT] [THEN] [STOP] [CRANE]` |

### **Weak or prohibited message families**

| Message family | Why Pictiq alone is inadequate | Proper authoritative layer |
| ----- | ----- | ----- |
| Dangerous-goods declaration | Needs UN number, proper shipping name, class, subsidiary risk, packing group, documents | IMDG/IATA/ADR record and trained DG procedure |
| Cargo release | Requires customs, commercial, security, terminal, and ownership status | Port community system/WMS/TOS plus authorized user |
| Vessel navigation order | Depends on real-time traffic, draft, tide, pilotage, radio confirmation, COLREGs | VTS/pilot/master using SMCP and navigational systems |
| Crane-lift plan | Needs load weight, center of gravity, rigging, wind limit, equipment certification, exclusion zone | Approved lift plan and competent lifting supervisor |
| Container stowage/segregation | Depends on detailed cargo, vessel plan, DG segregation, stability, temperature, access | Stowage planning system and IMDG rules |
| Customs/legal notice | Requires accurate language, rights, deadlines, governing law, confirmation of understanding | Official written translation/interpreter/legal staff |
| Injury assessment or return-to-work clearance | Requires clinical and occupational judgement | First aider, clinician, safety officer |
| Financial/contractual delivery confirmation | Requires parties, Incoterms, quantity/quality basis, timestamp, signatures | ERP/contract/document workflow |
| Weather go/no-go authority | Requires measured conditions, site thresholds, competent authority, active monitoring | Operational control system and supervisor |
| Security incident investigation | Requires identity, chain of custody, witness statement, confidentiality | Security procedure and formal records |

## **Visual grammar for a logistics profile**

A Pictiq port/warehouse pack should use a constrained message template. Avoid free-form “icon poetry” in safety-critical or movement-control contexts.

\[ACTOR / EQUIPMENT\]  
\[ACTION\]  
\[OBJECT / CARGO\]  
\[FROM\]  
\[LOCATION\]  
\[TO\]  
\[LOCATION\]  
\[TIME / STATUS\]  
\[CONDITION / HAZARD\]  
\[REQUIRED CONFIRMATION\]

Examples:

\[FORKLIFT\] \[MOVE\] \[PALLET\] \[FROM\] \[BAY 2\] \[TO\] \[ZONE C\]

\[CRANE\] \[STOP\]  
\[IF\] \[WIND\] \[MORE THAN\] \[LIMIT\]

\[TRUCK\] \[WAIT\] \[GATE 4\]  
\[UNTIL\] \[DOCUMENT\] \[CHECK\] \[DONE\]

\[CONTAINER\] \[SEAL\] \[BROKEN\]  
\[STOP\] \[MOVE\]  
\[CALL\] \[SUPERVISOR\]

### **Required core operators**

A logistics stress test should verify that Pictiq can distinguish these operations without relying only on arrow direction or color:

MOVE  
LOAD  
UNLOAD  
LIFT  
LOWER  
PUSH  
PULL  
OPEN  
CLOSE  
LOCK  
UNLOCK  
CHECK  
WEIGH  
COUNT  
SCAN  
LABEL  
WAIT  
STOP  
START  
FOLLOW  
KEEP CLEAR  
DO NOT ENTER  
CALL  
REPORT  
CONFIRM  
RELEASE  
HOLD  
READY  
DONE  
FAILED  
DAMAGED  
LEAK  
SPILL  
FIRE  
WIND  
RAIN  
LOW VISIBILITY

The grammar also needs non-object concepts:

FROM  
TO  
AT  
IN  
ON  
UNDER  
ABOVE  
BEFORE  
AFTER  
THEN  
IF  
UNTIL  
NOT  
MORE THAN  
LESS THAN  
ALL  
SOME  
ONE  
MANY  
NOW  
TODAY  
TIME  
DATE  
QUANTITY  
WEIGHT  
VOLUME  
TEMPERATURE  
DISTANCE

For Pictiq, `FROM`, `TO`, `IF`, `THEN`, `UNTIL`, `NOT`, and `CONFIRM` may be more operationally valuable than adding many cargo illustrations.

## **Proposed Pictiq logistics stress-test corpus**

This corpus is for research and validation, not direct operational deployment. Every example should be tested in:

* Tile-only form.  
* Tiles plus local-language text.  
* Tiles plus spoken explanation.  
* Tiles shown on paper, handheld device, large sign, and noisy/low-light setting.  
* First-time users, brief-trained users, and experienced logistics workers.  
* Multiple language groups relevant to the intended operating setting.  
* A controlled comprehension setting and a time-pressured simulation.  
* Human interpretation and machine parse from the canonical JSON/grammar form.

Each corpus record should contain:

{  
  "id": "LOG-01",  
  "reference\_text": "Move pallet 24 from bay B2 to staging zone C.",  
  "pictiq\_sequence": \[\],  
  "required\_semantics": \[\],  
  "allowed\_context": \[\],  
  "failure\_modes": \[\],  
  "risk\_level": "low|medium|high|professional-only",  
  "expected\_classification": "PRESERVED\_EXPLICITLY|CONTEXT-SUFFICIENT|LOSSY|GAP"  
}

### **A. Cargo identity, type, and quantity**

| ID | Reference message | Required meaning to preserve | Expected Pictiq classification |
| ----- | ----- | ----- | ----- |
| LOG-01 | Move pallet 24 from bay B2 to staging zone C | Object, ID, movement, origin, destination | `PRESERVED_EXPLICITLY` only with typed ID/location |
| LOG-02 | There are 18 pallets ready for loading | Count, unit, readiness, loading context | `PRESERVED_EXPLICITLY` |
| LOG-03 | Weigh this bulk grain load before unloading | Object, action, procedural order | `PRESERVED_EXPLICITLY` |
| LOG-04 | Net weight is 18.4 tonnes | Measurement basis, number, unit, cargo association | `LOSSY` unless net/gross distinction exists |
| LOG-05 | This container is empty | Container, state | `CONTEXT-SUFFICIENT` |
| LOG-06 | This container is loaded but not released | Loaded state, legal/operational hold | `GAP` / professional-system link required |
| LOG-07 | Count all bags before sealing the truck | Quantifier, object, sequence, next action | `PRESERVED_EXPLICITLY` if ALL and THEN are supported |
| LOG-08 | One bag is missing from pallet 16 | Expected count, missing condition, object identity | `LOSSY` without baseline quantity and pallet ID |
| LOG-09 | Do not mix wheat and soy cargo | Negation, separation, two commodities | `PRESERVED_EXPLICITLY` |
| LOG-10 | Cargo temperature is 6°C and rising | Measurement, unit, direction of change, timestamp/context | `LOSSY` unless trend and time are explicit |

### **B. Direction, place, and movement**

| ID | Reference message | Required meaning to preserve | Expected Pictiq classification |
| ----- | ----- | ----- | ----- |
| LOG-11 | Truck go to gate 3 | Vehicle, imperative, destination | `CONTEXT-SUFFICIENT` in a clearly mapped yard |
| LOG-12 | Forklift reverse slowly | Equipment, reverse direction, speed constraint | `PRESERVED_EXPLICITLY` only if reverse differs from move-back |
| LOG-13 | Keep clear of crane operating area | Prohibition, exclusion zone, equipment, active state | `PRESERVED_EXPLICITLY` |
| LOG-14 | Move the pallet under the covered storage area | Object, move, target spatial relation, shelter | `PRESERVED_EXPLICITLY` |
| LOG-15 | Do not enter lane 4; forklift traffic is active | Prohibition, exact lane, hazard cause, active state | `PRESERVED_EXPLICITLY` |
| LOG-16 | Use the alternate route around the blocked road | Route closure, alternate route, direction | `PRESERVED_EXPLICITLY` with mapped reference |
| LOG-17 | Keep container upright during transfer | Object, orientation, duration/scope | `PRESERVED_EXPLICITLY` |
| LOG-18 | Do not stand under suspended load | Prohibition, person, spatial relation, hazard | `PRESERVED_EXPLICITLY` |
| LOG-19 | Stop vehicle at the weighbridge | Vehicle, stop action, named location | `CONTEXT-SUFFICIENT` if place is visibly identified |
| LOG-20 | Wait outside until called | Wait, location, condition/event | `LOSSY` unless “called by whom/how” is operationally clear |

### **C. Hazard, weather, and condition**

| ID | Reference message | Required meaning to preserve | Expected Pictiq classification |
| ----- | ----- | ----- | ----- |
| LOG-21 | Heavy rain: keep cargo under cover | Weather, intensity, protection action, cargo scope | `PRESERVED_EXPLICITLY` |
| LOG-22 | High wind: stop crane lifting | Measured/threshold wind, stop, crane-lift scope | `LOSSY` unless threshold/authority are linked |
| LOG-23 | Visibility is low: reduce vehicle speed | Visibility, condition, speed reduction, affected actors | `LOSSY` unless speed limit is explicit |
| LOG-24 | Box is damaged; do not load it | Object, condition, prohibition, action | `PRESERVED_EXPLICITLY` |
| LOG-25 | Container seal is broken; report immediately | Specific condition, urgency, reporting destination | `PRESERVED_EXPLICITLY` |
| LOG-26 | Liquid spill: isolate area and call supervisor | Hazard, containment action, escalation | `PRESERVED_EXPLICITLY` |
| LOG-27 | Fire alarm: leave by emergency exit | Alarm/event, evacuation action, route | `PRESERVED_EXPLICITLY` |
| LOG-28 | This is a flammable-goods container | Hazard category, object | `CONTEXT-SUFFICIENT`; not a replacement for IMDG record |
| LOG-29 | Keep this refrigerated cargo between 2°C and 8°C | Product condition, lower/upper threshold, unit, continuous requirement | `GAP` unless range and monitoring scope are explicit |
| LOG-30 | Do not open container: fumigation risk | Prohibition, object, specific hazard, duration/clearance state | `LOSSY` unless clearance authority/time are included |

### **D. Equipment, PPE, and readiness**

| ID | Reference message | Required meaning to preserve | Expected Pictiq classification |
| ----- | ----- | ----- | ----- |
| LOG-31 | Wear helmet and high-visibility vest in this zone | Mandatory PPE, zone scope | `PRESERVED_EXPLICITLY` |
| LOG-32 | Forklift battery is low; charge before next shift | Equipment, state, action, temporal condition | `PRESERVED_EXPLICITLY` |
| LOG-33 | Crane is unavailable for maintenance | Equipment, unavailable state, cause | `PRESERVED_EXPLICITLY` |
| LOG-34 | Inspect sling before lifting | Equipment, inspection, sequence/precondition | `PRESERVED_EXPLICITLY` |
| LOG-35 | Do not use damaged lifting gear | Prohibition, equipment condition, scope | `PRESERVED_EXPLICITLY` |
| LOG-36 | Scanner is offline; record the container number manually | Equipment failure, fallback action, data target | `PRESERVED_EXPLICITLY` if manual-record action exists |
| LOG-37 | Fuel truck is arriving; keep route clear | Vehicle, arrival, future/near-time state, clearance action | `LOSSY` unless timing and route are visible |
| LOG-38 | Only trained operator may use this crane | Permission, role, equipment, authorization | `LOSSY` / requires policy and identity link |
| LOG-39 | Check emergency stop before starting conveyor | Device, check, precondition, action | `PRESERVED_EXPLICITLY` |
| LOG-40 | Machine guard is open; do not start | Safety state, prohibition, target equipment | `PRESERVED_EXPLICITLY` |

### **E. Procedural sequencing and handoff**

| ID | Reference message | Required meaning to preserve | Expected Pictiq classification |
| ----- | ----- | ----- | ----- |
| LOG-41 | Scan container, check seal, then load | Ordered three-step procedure | `PRESERVED_EXPLICITLY` |
| LOG-42 | If seal is broken, stop and call supervisor | Condition, trigger, stop, escalation target | `PRESERVED_EXPLICITLY` |
| LOG-43 | Load only after weight and document checks are complete | Two preconditions, completion state, conditional authorization | `LOSSY` unless scope/grouping is clear |
| LOG-44 | Driver signs after cargo count is confirmed | Actor, sequence, confirmation condition, signature | `PRESERVED_EXPLICITLY` only with defined signature/attestation semantics |
| LOG-45 | Cargo is ready for pickup at dock 7 | Cargo, readiness, action context, location | `CONTEXT-SUFFICIENT` |
| LOG-46 | Cargo hold remains active pending customs release | Hold, condition, external authority, dynamic status | `PROFESSIONAL-SYSTEM-ONLY` |
| LOG-47 | Shift handoff: 12 pallets counted; 2 damaged; inspection pending | Counts, categories, incomplete state, responsibility transfer | `LOSSY` unless record owner/time and object scope are linked |
| LOG-48 | Confirm truck is empty before leaving | Check, state, condition, sequence | `PRESERVED_EXPLICITLY` |
| LOG-49 | Do not close the container until photos are taken | Negation, sequence, evidence requirement | `PRESERVED_EXPLICITLY` if UNTIL is supported |
| LOG-50 | Supervisor approved loading at 13:40 CEST | Authority, action, approval state, time zone, audit evidence | `PROFESSIONAL-SYSTEM-ONLY` as an authoritative claim |

## **Stress-test questions**

For each corpus message, evaluate more than icon recognition.

1. **Object resolution:** Can users identify the relevant cargo, vehicle, zone, container, or equipment—not merely its category?  
2. **Action prediction:** Can users state exactly what they should do next?  
3. **Role clarity:** Can they identify who should act, who should be informed, and who has authority?  
4. **Direction and location:** Can they distinguish `TO`, `FROM`, `AT`, `UNDER`, `AROUND`, `UPRIGHT`, and process-sequence arrows?  
5. **Quantity and units:** Can they accurately distinguish pallet count, gross/net weight, tonne versus kilogram, volume, temperature, time, and distance?  
6. **Negation and scope:** Do they understand what `NOT` prohibits and what condition it applies to?  
7. **State lifecycle:** Can they distinguish planned, ready, active, paused, complete, failed, damaged, held, released, and expired?  
8. **Hazard response:** Does the message cause the correct immediate safety behavior without prompting unsafe improvisation?  
9. **Conditional procedure:** Can users follow `IF`, `THEN`, `UNTIL`, `BEFORE`, `AFTER`, and `CONFIRM` in the correct order?  
10. **Recognition versus compliance:** Does the user recognize a flammable symbol but still know that the detailed IMDG record governs handling?  
11. **Cultural and language variance:** Which symbols are consistently understood, and which are interpreted through local conventions?  
12. **Noise and visibility resilience:** Does comprehension survive PPE, rain, glare, distance, night lighting, motion, loud equipment, and rushed communication?  
13. **Machine parse:** Can a scanner, app, or vision system recover the same canonical Pictiq structure from a printed/displayed sequence?  
14. **Escalation behavior:** When a message is `LOSSY`, `GAP`, or `PROFESSIONAL-SYSTEM-ONLY`, does the user know to stop, check documentation, or call the supervisor?

## **Recommended corpus labels**

Use the semantic-compression categories from your broader Pictiq work, plus a logistics-specific authority label:

PRESERVED\_EXPLICITLY  
  All task-critical elements are visible or formally encoded.

CONTEXT-SUFFICIENT  
  Immediate action is safe because location, equipment, and workflow  
  are physically obvious and stable.

INTENTIONAL\_OMISSION  
  Nonessential detail—such as politeness, shift identity, or repeated  
  context—is excluded without changing the required action.

LOSSY  
  A meaningful operational distinction is missing:  
  exact quantity, condition threshold, actor, timing, or authority.

GAP  
  The grammar or Context Pack cannot yet express required concepts:  
  units, range, sequence scope, legal status, evidence, uncertainty.

PROFESSIONAL-SYSTEM-ONLY  
  The message requires an authoritative operational, legal, safety,  
  customs, or commercial system and qualified personnel.

## **Bottom line**

Maritime and logistics environments show that standardization works when it limits itself to recurring, bounded, high-frequency situations. SMCP provides controlled maritime English for critical ship, shore, and emergency communication; the International Code of Signals supplies standardized visual/message conventions when language is difficult; ISO safety signs and cargo marks communicate immediate hazards and handling constraints; IMDG labels classify danger but rely on formal records for detailed action.\[[imo](https://www.imo.org/en/ourwork/safety/pages/standardmarinecommunicationphrases.aspx)\]\[[imo-epublications](https://imo-epublications.org/content/books/9789280117387)\]\[[standards.iteh](https://standards.iteh.ai/catalog/standards/iso/85a8f8af-db94-4af2-89c8-da5a8a2dda8b/iso-7010-2019)\]\[[shipfinex](https://www.shipfinex.com/blog/imdg-code)\]

For Pictiq, the most defensible stress-test target is a compact visual protocol for:

CARGO \+ CONDITION  
EQUIPMENT \+ STATE  
ACTOR \+ ACTION \+ OBJECT  
FROM \+ LOCATION \+ TO \+ LOCATION  
QUANTITY \+ UNIT  
HAZARD \+ IMMEDIATE ACTION  
IF \+ CONDITION \+ THEN \+ ACTION  
CHECK \+ CONFIRM \+ NEXT STEP

The protocol should deliberately stop at the boundary where identity, release authority, customs status, navigation control, lift engineering, dangerous-goods particulars, exact thresholds, or legal/commercial accountability determine the correct action. In those cases, Pictiq can show an understandable summary and a clear escalation prompt, but the authoritative message must remain in standardized documentation, live operational systems, and trained professional communication.

