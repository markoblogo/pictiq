# **Trace: a small visual protocol**

*"Trace" is a working name. The capitalized labels below (WATER, HAVE…) are only shorthand for you, the reader. In the language itself they are pictures, never words or letters.*

---

## **1\. Fundamental design principles**

1. **Picture what can be pictured.** Otherwise use a form that performs its meaning, such as an arrow (toward), a gap (unknown), a slash (not) or a spike (harm). This uses body, physics and geometry that every person shares, not conventions that vary by culture.  
2. **Grammar lives in geometry, not in the vocabulary.** Cell outline shape gives word class, contact gives modification, and position gives role. A learner picks up about six spatial rules, not a lexicon of function words.  
3. **Small closed core, open composition.** Most meanings are built from visible parts. A composed symbol can be understood by reading its parts, and a machine can always expand it into primitives.  
4. **One form, one meaning.** There are no homonyms and no hidden metaphors. Figurative extension must be written out as composition.  
5. **Declare intent first.** Every message starts with a mood marker (statement, question, request or warning), so how to take the message is known before its content is read.  
6. **Fail softly.** Each cell is meaningful on its own, and there are no long-distance dependencies. A receiver who understands 60% of the cells still gets about 60% of the meaning.  
7. **Ask, don't guess.** Clarification is built into the grammar (empty slots, pick-one, echo-back), so ambiguity is settled by a reply and not by silent inference.  
8. **Robust to poor conditions.** Everything works in one color, at small sizes and hand-drawn. Color, motion and sound are only ever redundant.  
9. **One structure, two renderings.** Every message is a small tree. Humans see it as a drawing and machines see it as typed nodes, and the two are convertible in both directions.

---

## **2\. Grammar**

**Message frame.** A filled dot at the left edge marks the head, and the message ends with a thin closing bar. Reading goes from the dot toward the bar, so no script direction is assumed. Every message consists of one mood tab followed by 1–7 cells.

**Moods (the tab at the head):**

* STATE: a flat bar.  
* ASK: an open ring.  
* REQUEST: a cupped palm.  
* WARN: a spiky burst outline around the whole message.

**Cell shape gives word class:**

* ○ **round cell**: an entity (person, thing, substance, place).  
* ▷ **chevron cell**: an action or relation. Its point faces the object, so it also shows the reading direction.  
* □ **square cell**: a measure or quality (a level bar, a number).

**Slot order:** Actor ○, then Action ▷, then Object ○, then optional extras. Extra roles are introduced with an arrow (for example, an arrow followed by an entity marks a recipient or destination).

**Omitted actor.** The actor may be left out only where it is unambiguous. In REQUEST it is the speaker, and in WARN it is whoever reads the message. In STATE and ASK the actor is always drawn.

---

## **3\. How symbols combine**

Seven spatial operators cover all composition:

| Operator | Drawn as | Meaning |
| ----- | ----- | ----- |
| Sequence | cells in a row with gaps | roles by slot |
| Top contact | a small cell touching the top of another | attribute (quantity, quality, "of this place") |
| Bottom contact | a small cell touching the bottom | means or instrument ("by way of") |
| Containment | one shape drawn inside another | the outer cell is the head, the inner cell is its specifier (a vessel containing water is a bottle of water) |
| Slash | a diagonal bar through a cell or group | negation of whatever it crosses |
| Link bar | a bar between two cells | equals or is (a match) |
| Twin arrows | two opposed arrows between two cells | exchange |

Grouping uses a rounded outline, which lets a slash or a number apply to several cells. Nesting is limited to two levels, because deeper nesting is hard for humans to read.

---

## **4\. Questions, affirmation, negation, quantity, direction, quality, actions**

* **Yes/no questions.** The message ends with an answer pair: MATCH beside slashed-MATCH. This is self-explaining ("choose one"), and in a digital interface the two are simply buttons.  
* **Open questions.** An empty ring drawn in the slot of the unknown. **The ring takes the shape of the expected answer class**: a round ring asks which thing, who or where, a chevron ring asks which action, and a square ring with empty digit frames asks how much or how many. The reply repeats the message with the slot filled.  
* **Asking a price:** ASK, then \[thing ⇄ VALUE with empty digit frames\].  
* **Affirmation:** MATCH. **Negation:** SLASH. A slash over one cell means "not that one", and the reply "no, the other one" is a slashed cell followed by the correct one.  
* **Don't know or unclear:** the ASK ring alone, or attached to a cell ("what do you mean by this?").  
* **Quantity:** dots attached above a cell (see section 6). "Some" or "many" is dots plus a level bar, and "none" is a slashed entity.  
* **Direction:** an arrow.  
  * In a plain message, up means forward, down means back, and left and right mean left and right, as drawn from the reader's point of view.  
  * Placed in a ring with a person figure at its center, it becomes a map frame with a fixed orientation. Machines may add an explicit bearing.  
  * A length or level bar on the arrow shows near or far.  
  * An arrow dangling off the frame edge points at something in the real world ("that one over there").  
* **Quality:** a square cell holding a dimension icon (heat, size…) plus a three-segment level bar. Zero segments filled is "none", one is low, two is middle, and three is high. Attach it to an entity. On an action, it means intensity.  
* **Comparison:** a level bar with a small up or down arrow ("cheaper" is VALUE with a down arrow).  
* **Actions:** a chevron cell. Its point marks the direction of effect from actor to object. Actions can carry levels: WANT at full level means NEED.

---

## **5\. Context and ambiguity**

* **One idea per message.** Long ideas are sent as several short messages.  
* **No pronouns.** Use HERE, the pointing arrow, or simply repeat the symbol.  
* **Topic tab (optional).** An entity cell in the head tab sets the domain (VALUE for a shop, VEHICLE for transport, BODY for health). It narrows readings of ambiguous glyphs and is recommended for machines and interfaces.  
* **Pick-one.** For real ambiguity, a sender or machine offers 2–3 candidate readings in a row, each with a small circle. The reply fills one circle.  
* **Echo-back for critical content.** For money, safety and identity, the receiver repeats the message with an answer pair and the sender confirms. Machines must do this. Humans do it when they doubt they understood.  
* **Rule of visible uncertainty.** If a sender is unsure of a symbol, it wobbles the outline (see section 9).

---

## **6\. Numbers**

* **1 to 5:** plain dots, attached above the counted thing. Small groups are recognized at a glance.  
* **Any number:** digit frames, meaning boxes of ten slots in two rows of five, in which the number of filled dots is the digit. A zero is an empty box.  
  * Digits go left to right, most significant first.  
  * Position labels itself. The units frame has a heavy baseline, the tens frame has one tick above it, the hundreds frame has two ticks, and so on.  
  * Six is therefore a full top row plus one dot below, and twenty-six is two frames: a tick-marked frame with two dots, and a baseline frame with six.  
* **Decimals:** a small filled pin between frames.  
* **Fractions:** a partially shaded disc. A half-filled circle is a half.  
* **Approximate amounts:** dots with a level bar and no frame.  
* **Machines:** exact integer or decimal fields.

---

## **7\. Proper names and concepts outside the core**

**Names.** A name is a hang-tag shape holding two parts.

1. A category glyph: PERSON, ENCLOSURE for a place or business, VEHICLE for a line or route, and so on.  
2. An opaque payload, drawn inside a hatched box that means "copy this, do not interpret it". The payload can be original-script text, a picture or logo, a map position, or a digit-frame string such as a room or phone number.

Humans can copy or show it, and machines pass it through verbatim.

**Other concepts.** Try in this order:

1. **Compose** from primitives ("a place where..." is ENCLOSURE plus specifier).  
2. **Depict.** Draw or show a real picture in a double frame, which marks it as a literal picture and not a symbol.  
3. **Point.** Use the dangling arrow toward the actual object.

---

## **8\. Controlled vocabulary growth**

Three tiers:

| Tier | Contents | Rules |
| ----- | ----- | ----- |
| **Core** | about 40 primitives, hard cap 64 | Frozen per version. A new primitive is admitted only if it cannot be composed from existing ones with acceptable guess-accuracy. Each admission must be paid for by retiring or merging another primitive. |
| **Registry** | frozen compounds such as TOILET, TAXI and BUY | Each entry has a canonical decomposition into Core primitives (always expandable). It must pass a guess-the-meaning test across language groups and show real demand. Entries expire when unused. |
| **Ad hoc** | anything else | Drawn in a dashed "improvised" outline so the receiver knows it is unregistered. It is never silently promoted. |

Testing is done with people who have never seen the system. Each candidate gets a meaning-guess test, and a candidate is rejected if it is confused with an existing symbol.

---

## **9\. Meaning the system cannot express exactly**

* **Wobble.** A dashed or wavering outline on any cell means "roughly this, not exactly".  
* **Gap declaration.** An empty dashed cell of the right class means "the meaning belongs here but I cannot say it". The receiver may answer with a pick-one of guesses.  
* **Fallbacks, in order:** wobbled nearest composition, then a picture in a double frame, then a name-tag payload, then pointing at the real thing.  
* **Machines** send an explicit node with an *unmapped* flag, a confidence value and an optional payload.

The system never fills a gap by pretending to be exact.

---

## **10\. Humans and machines**

**Shared:** one tree, one grammar and one vocabulary.

**For humans:**

* Rendering is redundant (class-shaped cells, chevrons that point, gaps, large glyphs).  
* Messages stay short and shallow.  
* Interfaces are slot-based palettes, so ill-formed messages cannot be assembled and empty rings show what is still missing.  
* Hand-drawn input is recognized approximately and confirmed by echo.

**For machines:**

* Each cell is a node: `{class, id, modifiers, number}`. An id is 6 bits, a class is 2 bits, and a mood is 3 bits per message.  
* Parsing is strict, there is a canonical form, and no judgment of similarity is used.  
* Machines additionally carry precise numbers, name payloads, confidence and bearings.

**Parity rules:**

* Every machine message must have a faithful human rendering (no hidden fields).  
* Every human message must be parsable, with ambiguity returned as pick-one and not resolved silently.  
* Machines that speak to humans keep messages short (roughly 5 cells or fewer) and always offer an answer pair.

---

## **Core vocabulary (about 40\)**

**A. Structure and operators**

| Primitive | Meaning | Visual metaphor | Why it may be guessable |
| ----- | ----- | ----- | ----- |
| HEAD | start of the message, reading direction | filled dot on the left of a line ending in a thin bar | a start point plus a path is a universal "begin here, go there" shape |
| STATE | plain statement | a flat bar | flat, calm, "just laying it down" |
| ASK | question, unknown | an open ring | a hole to be filled is a natural picture of a missing piece |
| REQUEST | I want you to do or give (please) | cupped open palm | the "please give" gesture is widely understood |
| WARN | danger, attend | a spiky burst outline | sharp points read as hurtful to nearly everyone |
| MATCH | same, is, yes | two identical shapes joined by a bar | equal shapes look "in agreement" |
| SLASH | not | a diagonal bar across something | crossing something out means cancelling it |
| ARROW | toward, direction, recipient | a shaft with a point | the arrow shows where something is heading |
| AT | location, place | a dot inside a ring | a spot with a marked area around it |
| DOT | one unit, counting | a small filled dot | counting units by marks is the earliest and most universal counting |
| DIGIT FRAME | a digit (count of dots in a ten-slot box) | two rows of five slots, filled dots \= value | it can be read by counting alone |
| LEVEL | degree (none, low, mid, high) | a three-segment bar filling from the base | a filled bar suggests "how much" |
| WOBBLE | approximately | a dashed or wavering outline | a shaky line signals imprecision |

**B. People, body and things**

| Primitive | Meaning | Visual metaphor | Why it may be guessable |
| ----- | ----- | ----- | ----- |
| ME | the speaker | a figure with a dot on its chest | pointing to the chest to say "me" is common across cultures |
| YOU | the addressee | the same figure facing out with an outstretched hand toward the reader | a hand held toward someone means "you" |
| PERSON | someone, people | a plain standing figure | a human silhouette |
| BODY | body, physical needs | a torso outline | a torso is a reliable picture of a person's body |
| HAND | manipulate, give, hold | an open hand | a hand is an obvious picture of a hand |
| MOUTH | eat, drink, speak | an open mouth | a mouth is a straightforward picture |
| EYE | see, look | an eye | an eye is a straightforward picture |
| WATER | water, liquid | a drop | drops of water are seen everywhere |
| FOOD | food | a bowl with a mound | a bowl with a heap is common to many diets |
| VALUE | money, price, worth | a disc with an inner ring | a round coin |
| CARD | card payment | a rounded rectangle with a stripe and a small chip square | a picture of the object (learned by use rather than guessed) |
| BLOCK | generic item, unit | a solid cube | a plain object stands in for "one thing" |
| VESSEL | container | an open-topped cup shape | a cup is used almost everywhere |
| ENCLOSURE | building, room, indoors | walls and a roof with a door gap | a shelter is a universal picture, and the gap suggests entering |
| VEHICLE | vehicle, transport | a body on two wheels | wheels mean rolling transport |

**C. Dimensions (used with LEVEL)**

| Primitive | Meaning | Visual metaphor | Why it may be guessable |
| ----- | ----- | ----- | ----- |
| HEAT | temperature | a flame | fire is the classic image of heat |
| SIZE | big or small | a small square nested inside a bigger one | relative extent |
| SPEED | fast or slow | an arrow with trailing streak lines | streaks indicate motion |
| HARM | dangerous or safe | the spiky burst (same as WARN) | pointed shapes mean hurt |

**D. Actions**

| Primitive | Meaning | Visual metaphor | Why it may be guessable |
| ----- | ----- | ----- | ----- |
| HAVE | possess, hold | a fist around a block | holding is possessing |
| GIVE | give, hand over | a hand with a block leaving it along an arrow | handing over an object |
| WANT | want (NEED at full level) | a reaching hand with an arrow toward an object | reaching means desiring |
| GO | move, enter, leave | footprints with an arrow | footprints trace a path of movement |

Everything else (DRINK, BUY, SELL, TOILET, TAXI, PAIN, BUS, HELP…) is a Registry compound built from these.

---

## **Demonstration**

Notation used only here:

* ○ marks an entity cell, ▷ an action cell and □ a quality cell.  
* `+` means top contact.  
* `⊃` means containment.

**1\. "Do you have water?"**  
 `STATE→ASK` ○YOU ▷HAVE ○WATER `[MATCH | ⁄MATCH]`  
 An open-ring mood tab, then the outward-facing figure, a fist around a block, and a drop. The message ends with the answer pair "equal / not-equal".

**2\. "Yes. Cold water. For sale."**  
 Message A: STATE, then MATCH alone.  
 Message B: STATE, ○ME ▷GIVE ○WATER, with a square cell (HEAT flame plus one of three level segments filled) touching the top of WATER, followed by the twin-arrow exchange to ○VALUE with no number.  
 Reading: I give cold water, exchangeable for value.

**3\. "Three bottles, please. Card payment?"**  
 Message A: REQUEST, then ▷WANT, then ○\[VESSEL ⊃ WATER\], with three dots on top.  
 The actor is omitted because it is the speaker, and the cupped-palm mood carries "please".  
 Message B: ASK, ○ME ▷GIVE ○VALUE, with CARD touching the bottom of ▷GIVE (means: by card). It ends with `[MATCH | ⁄MATCH]`.

**4\. "Yes. Six units of local currency."**  
 Message A: STATE, MATCH.  
 Message B: STATE, ○VALUE with a digit frame of six dots on top (five in the top row, one below), all inside an AT ring. The ring means "of this place".

**5\. "Where is the toilet?"**  
 ASK, ○TOILET, ▷AT, ○◌ (an empty round ring in the slot, showing that a place is expected).  
 TOILET is a Registry compound: ENCLOSURE ⊃ \[BODY with a down arrow ending in small dots\].  
 A possible reply: STATE ○TOILET ▷AT ○\[ARROW pointing up-left with two of three level segments filled\]. It means: forward-left, moderately near.

**6\. "I need a taxi."**  
 REQUEST, ▷WANT with a three-of-three LEVEL on top (intensity, meaning NEED), ○TAXI.  
 The actor is omitted because it is the speaker. TAXI is a Registry compound: VEHICLE ⊃ \[PERSON \+ VALUE\].

**7\. "This is dangerous. Do not enter."**  
 Message A: WARN frame, ○AT-ring-with-figure-inside (HERE), MATCH, □\[HARM spike plus three-of-three LEVEL\].  
 Message B: WARN frame, SLASH across the group \[▷GO with an arrow pointing into ○ENCLOSURE through its door gap\].  
 The actor is omitted because in WARN it is whoever reads. On a sign the two messages share a single spiky frame.

---

## **Honest weak points**

* **TOILET, TAXI and CARD are the least guessable symbols.** They need testing, and they are the most likely to be replaced by a better composition.  
* **The bottom-contact "instrument" rule and the direction-frame convention** are learned rules, not guessable ones. They need prominent demonstration in any interface.  
* **Time is deliberately absent from the Core.** A Registry compound (a line with a "now" pin and an arrow along the reading direction) would be the first addition.

I can draw this as a rendered visual sheet (the primitives and the seven messages as actual SVG glyphs) if that would help you test it.

# **Stress test of Trace**

I'm treating the guessability claims in my first answer as hypotheses, since none were tested. Confidence levels below are my own estimates.

---

## **1\. Symbols likely to be understood immediately**

**High confidence (as an object, not always as the intended concept):**

* **PERSON**, **HAND**, **EYE**, **MOUTH**, and the **DOT** as a count of one.  
* **HEAT** (flame) as "fire or hot", **ARROW** as direction, and **SLASH** as "not".  
* **ENCLOSURE** as "a building".  
* **DIGIT FRAME** for numbers 1-4, where dots are subitized at a glance.

**Medium confidence:**

* **WATER**: a drop reads as "liquid" or "wet", but also as a tear, blood, oil, sweat or a leak.  
* **WARN**: the spiky burst reads as "attention", but also as an explosion, a star, a celebration, a comic "pow" or a **sale badge**.  
* **VALUE**: a coin is guessable, but a disc with an inner ring also reads as a target, button, plate, wheel or record.  
* **MATCH | slashed-MATCH**: readers with math exposure see "= / ≠", but many won't.  
* **VESSEL**: could be a cup, glass, bucket or bin.

## **2\. Symbols that require learning**

* **All three cell outline classes**: circle, chevron and square meaning entity, action and measure. Nothing in the shapes hints at this.  
* **Every operator except sequence**: top contact, bottom contact, containment, twin arrows and the link bar are all conventions.  
* **Mood tabs**: the flat bar for STATE has no natural meaning, and the open ring for ASK is a guess.  
* **HEAD/closing bar**: it looks like a progress bar or a route line, not a reading direction.  
* **CARD, GO, HAVE, GIVE and WANT**: these are depictions of objects or gestures that stand in for abstractions, not concepts that can be guessed.  
* **Level bar semantics**: which end is the base, and that zero means "none" and not "unknown".  
* **Digit frames and place-value ticks**: this is a full positional numeral system.  
* **Wobble, dashed outline, hatched box and double frame**: these are all meta-marks (approximate, improvised, opaque copy, literal picture).

## **3\. Dangerous ambiguities**

Ranked by consequence, worst first:

1. **GIVE vs WANT vs TAKE.** They differ mainly by arrow direction on a hand-and-block. At small size, or mirrored, "I give" and "I want" look alike. In commerce that swaps the buyer and seller roles.  
2. **ME vs YOU.** The difference is a chest dot versus an outstretched hand. On any screen, a figure with a dot reads as "this is you" (a profile icon), which is the opposite of the intended meaning. Whose "me" it is also flips every time the speaker changes.  
3. **Prohibition, inability and description are collapsed.** SLASH over GO can mean "must not enter", "cannot enter", "nobody enters" or "didn't enter". Nothing separates rule from fact from physical impossibility. Warnings depend on exactly this distinction.  
4. **HARM has a zero pole.** A spike with zero filled segments means "safe", but it is nearly identical to a spike with no bar at all, or with a lost or misjudged bar (2 of 3 vs 3 of 3). A missing or poorly rendered level bar flips the warning.  
5. **No hazard type.** WARN says "danger" but not fire, electricity, poison, flood, fall or contaminated water. "Is this water safe?" (\[WATER \+ HARM\]) could read as a flood warning.  
6. **Zero and "unknown" look the same.** An empty digit frame is zero, but an empty digit frame also asks "how much?". A free item and a price question are drawn the same way.  
7. **Missing currency.** "Six units" says nothing about which currency. "Local" is relative to the speaker, the shop or the tourist.  
8. **Slash scope.** A slash across a cell versus a group is hard to tell apart in drawings. "Not cold water" and "cold, not water" are visually near-identical.  
9. **HAVE.** A fist around a block means possession, holding, availability, existing, containing and "in stock". "Do you have water?" could be read as "are you physically holding water?". The answer "yes" (MATCH) then confirms the wrong sense.  
10. **REQUEST \+ WANT.** In my own demonstration, this is either redundant ("I request that I want") or has an unintended reading ("I want you to want").

## **4\. Overloaded concepts**

* **Ring**: ASK mood, empty entity slot, AT (dot inside a ring), the outer body of VALUE, pick-one circles, and the circle cell outline itself. A ring can be any of these.  
* **Dot**: count of one, HEAD marker, chest of ME, AT centre, decimal pin, the marks inside digit frames and level segments, and the hatched-box payload marker.  
* **Arrow**: direction, recipient, destination, GIVE trajectory, "by way of", comparison (up/down), the excretion mark in TOILET, "point at real thing", and reading direction. No "from", "via", "with" or "for" exists.  
* **Top contact**: quantity, quality, "of this place", and action intensity.  
* **Level bar**: quality, near/far, intensity, comparison, and "some/many" (bar plus dots).  
* **Containment**: container of substance (bottle of water), passengers in a vehicle (TAXI), a person at a place (HERE), an action into a place (GO into ENCLOSURE), and a component inside a compound (TOILET).  
* **Dashed or wobbly line**: approximate, improvised (registry tier), unsayable (gap), and in UIs, disabled or optional.  
* **Hand-based glyphs**: HAND, REQUEST, GIVE, WANT, HAVE (fist) and YOU (outstretched hand). Six symbols share one visual family.  
* **Spike**: WARN (mood), HARM (dimension), and the "danger" end of a level bar. The same glyph plays three grammatical roles.  
* **Twin arrows**: exchange, but also sync, refresh, swap and currency conversion in UIs. The last is especially unfortunate next to VALUE.

## **5\. Grammar that may be too abstract**

* **The "six spatial rules" claim was optimistic.** Counting rules a learner must know: three cell classes, four moods, seven operators, group outlines, slot order, actor omission per mood, answer pairs, shape-of-answer rings, pick-one, echo-back, topic tab, wobble, gap, name tags with payload boxes, double frames, and three registry-status outlines. That is more than twenty.  
* **Class-by-outline is inconsistent in my own vocabulary.** AT is called a chevron relation in a sentence but appears as a round entity ("HERE"). MATCH is a bar, not a cell. WARN is a mood and HARM is a measure, with the same glyph. ARROW belongs to no class.  
* **Actor-omission rules break in my own demos.** The rule says STATE always draws the actor, but "Yes" is a lone MATCH. Demo 1 also used a muddled "STATE→ASK" notation.  
* **Reference frames are undefined.** "Up is forward" conflicts with screen and map conventions (up \= north, up \= upstairs). "Left and right from the reader's point of view" collides with ME and YOU figures that face the reader, so the figure's left is the reader's right.  
* **No coordination.** Two entity cells in a row read as actor and object or as an error, never as "water and food". No "or", "and", "with" or "because".  
* **No tense, no time.** Everything is present tense. "When does it leave?" and "the water was contaminated" can't be said.  
* **Meta-symbols must be understood before clarification works.** A person who doesn't read the ASK ring can't benefit from pick-one or echo-back. The repair mechanism has the same bootstrapping problem as the base language.  
* **Comprehension is easier than production.** A novice with a pen must draw a fist around a block, a door gap, footprints, and place ticks. Only a palette interface makes production practical.

## **6\. Numerical notation problems**

* **Two systems.** Plain dots for 1-5 and digit frames for everything else. A frame with five dots in the units row and five plain dots above a cell look almost the same.  
* **Counting beyond 4 is slow and error-prone.** The 5+4 layout for 9 requires counting or pattern memorization. This matters most for money.  
* **Place value depends on tick marks.** Ticks above a baseline scale poorly: a million needs six. Phone numbers and IDs shouldn't carry place value, but they use the same frames.  
* **Width blow-up.** 26 takes two 10-slot frames, and a price like 12.50 takes about four frame widths, larger than the object being priced.  
* **The decimal pin is a dot.** At small sizes it looks like a filled slot or a stray mark.  
* **Zero vs missing digit vs unknown** (see section 3, item 6).  
* **Fractions.** A partial disc collides with the coin glyph, battery and progress icons, and moon phases. "Half full" and "half empty" are also the same picture.  
* **No negatives, ranges, percentages, ordinals or units.** "Minus 3 degrees", "5-10 minutes", "second bus", "2 km" all lack notation.  
* **Dot-count collisions.** Three level segments and three count dots both sit at "top contact". "I need a taxi" (three-of-three LEVEL) can be read as "I need three taxis".

## **7\. Cases where composition becomes too long**

* **TAXI** \= VEHICLE ⊃ \[PERSON \+ VALUE\] and **TOILET** \= ENCLOSURE ⊃ \[BODY \+ arrow \+ dots\]. These are the most common practical concepts, and they are the longest. In practice they'd need redrawing as single glyphs, which loses the "expandable by parts" property.  
* **The Core excludes the most frequent needs.** DRINK, BUY, SELL, PAY, TOILET, TAXI, HELP, PAIN, BUS, HOSPITAL and POLICE all live in the Registry. The real working vocabulary is Core plus 100+ registry items, so "small Core" undersells the learning load.  
* **"Cold water. For sale."** takes two messages. The second has five parts (ME, GIVE, WATER, HEAT with partial level, exchange to VALUE) and is still ambiguous.  
* **"Six units of local currency"** stacks four devices (VALUE, digit frame, AT ring, top contact) and still fails to say which currency.  
* **Nesting limit of two** is quickly hit: a bottle of water (containment) with a count (top contact) inside a negation (group).

## **8\. Cultural assumptions**

* **Left-to-right start.** A filled dot at the left edge and a bar at the right assumes LTR, even though the design claims neutrality. Right-to-left readers, mirrored signage, and selfie-camera mirroring all reverse it.  
* **Gestures aren't universal.** Pointing at the chest for "me" varies (some cultures point to the nose). An outstretched hand can read as "stop", "beg" or "give me". A cupped palm can be a beggar's gesture. A fist can read as aggression or protest. Showing the left hand is offensive in some contexts.  
* **Objects.** A bowl with a mound is a rice bowl. A bank card with a chip is Western and payment-app dependent. Two wheels reads as a bicycle or scooter, not a bus, train or boat. A pitched-roof house isn't every culture's "indoors".  
* **Toilet depiction.** A body with an excretion arrow may be considered vulgar or shocking in some places, and toilet practices differ (squat, sit, water, paper).  
* **Fire as heat** and **footprints as movement** assume particular experiences (footprints suggest walking, not driving).  
* **Symmetry of "up \= forward"** presumes a spatial metaphor not shared everywhere.  
* **Base 10 and abacus-like frames** match school systems in many places but not everywhere.  
* **Silent assumption of commerce**: fixed prices, coins and cards, and a shop-versus-buyer role split.

## **9\. Problems for machine vision**

* **2D layout parsing.** Roles depend on contact, containment, position and outline, so a machine must reconstruct a graph from an image. That is harder than tokenizing a line of text.  
* **Contact vs near-contact.** A 1-pixel gap separates "sequence" from "attribute". Anti-aliasing, scaling and hand-drawing make this unstable.  
* **Occlusion by SLASH.** The slash overlays the glyph it negates, which hides exactly the features needed to identify it.  
* **Perspective and rotation.** Photos of signs are skewed and rotated, and top/bottom contact, arrow directions and left/right all break under rotation or mirroring.  
* **Wobble is indistinguishable from noise.** "Approximate" is encoded by a hand-drawn quality that also appears in any rough sketch, low-resolution photo or compressed image.  
* **Line-style classification** (solid, dashed, double, hatched, wobbly) is fragile at small size and under compression. Hatching produces moiré.  
* **Counting.** Digit frames require counting small dots and ticks, which is a known weakness of vision models, and errors here mean wrong money.  
* **Similar glyph families** (six hand glyphs, three ring uses) will collide in recognition even before ambiguity.  
* **The binary encoding is underspecified.** A 6-bit id and 2-bit class don't cover contact type, containment, slash scope or group boundaries, so the claimed machine efficiency is unproven.  
* **Accessibility.** Blind and low-vision users depend on the machine layer being rendered to speech, but nothing here defines that.

## **10\. Problems at 24-32 px**

* **ME vs YOU vs PERSON** lose distinguishing details (a chest dot is \~2 px).  
* **CARD** shrinks to a plain rounded rectangle, which is indistinguishable from the group outline, a phone or a ticket.  
* **VALUE** (coin with inner ring) becomes a gray disc or a ring, which is the ASK ring.  
* **HAVE, GIVE, WANT** (hand plus block plus arrow) turn into blobs. Three subparts don't fit.  
* **ENCLOSURE** loses the door gap, and **SIZE** (nested squares) merges into a thick square.  
* **FOOD** (bowl with a mound) becomes a hat or a hill.  
* **AT** (dot in ring) looks like a selected radio button, a target or a record button.  
* **DIGIT FRAME**: 10 slots in about 30 px gives \~5 px cells and \~2 px dots, so filled versus empty is one or two pixels of difference.  
* **Dashed, double and hatched lines** either vanish or become solid or gray.  
* **Contact vs 1 px gap** (see section 9).  
* **Slash** thickness must be about 2 px to be seen, which then covers most of a 24 px glyph.  
* **Nested compounds** (TOILET, TAXI) have inner parts under 10 px, which are unreadable.  
* **Mood tab**: the STATE bar is the thinnest element and the ASK ring can be mistaken for the AT glyph or a dot, though mood is the most important element in the message.  
* **Whole-message width.** With a tab, 5-7 cells and bar at 32 px each, a message is 250-320 px wide, before any digit frames.

---

## **Overall assessment**

The strongest parts are the small number of depictive nouns and the idea that grammar comes from geometry. The weakest points are:

1. Symbols that share the same visual material (rings, dots, arrows, hands, spikes).  
2. Safety-critical distinctions (give/want, me/you, prohibition/description, safe/danger levels) that depend on small details.  
3. A numeral system too heavy for its use (prices).  
4. A grammar much larger than advertised.  
5. An unverified assumption that composition stays legible when small.

# **Trace v0.2**

Every change below cites the section of my stress test that it answers. Capitalized names are still reader shorthand for pictures.

---

## **1\. What I changed**

| \# | Change | Problem it answers |
| ----- | ----- | ----- |
| 1 | **Header strip replaces the HEAD dot and mood tabs.** Every message opens with a small strip: a solid figure (sender), a line, and a hollow figure (receiver). The form of the line is the mood. A plain arrow means STATE. An arrow carrying an open ring means ASK. An arrow pointing back at the sender means REQUEST. A spiky burst around the whole message means WARN (receiver figure only). Optional in the strip: a topic glyph, and a LEVEL on the line for urgency (REQUEST/WARN only). The closing bar stays as a bold end cap. | §2 (HEAD looks like a progress bar; STATE bar has no natural meaning); §4 (cupped palm joins the six-glyph hand family); §8 (begging gesture); §9 (no orientation reference); §10 (mood was the thinnest element) |
| 2 | **ME/YOU/PERSON distinguished by fill, not detail.** Same silhouette. Solid \= sender, hollow \= receiver, split-fill \= anyone else. The header figures teach this by repetition. The chest dot and outstretched hand are gone. | §3.2 (ME/YOU flip); §8 (pointing gestures); §10 (2 px chest dot); §9 (mirroring) |
| 3 | **WANT and HAVE deleted.** GIVE is redrawn as one silhouette (palm plus block, no arrow). Direction comes from slot, and the default recipient is "the other party". "Have" becomes AT: WATER AT YOU. | §3.1 (GIVE/WANT swap); §3.9 (HAVE overloaded); §3.10 (REQUEST \+ WANT redundant); §4 (hand family); §10 (three-part blobs) |
| 4 | **HARM changes from a bipolar measure to an action** (chevron, jagged edge). "Safe" is HARM with a slash. Hazard type comes from composition: HEAT HARM BODY, WATER HARM MOUTH. | §3.4 (zero pole flips a warning); §3.5 (no hazard type); §4 (spike overloaded) |
| 5 | **LEVEL redrawn as three ascending steps, values 1–3 only.** Zero is never drawn. "None" is a slash. A bare LEVEL never attaches to a cell. It always sits inside a quality tile with a dimension icon, or on the header line. | §3.4; §6 (level segments vs count dots) |
| 6 | **Slash rewritten.** It protrudes past the outline of what it negates, sits on a halo so the glyph stays legible, and crosses exactly one outline (cell or group). Its meaning depends on mood: "is not" in STATE/ASK, "must not" in REQUEST/WARN. | §3.3 (prohibition vs description); §3.8 (scope); §9 (occlusion) |
| 7 | **One number system.** A digit is a single tile holding at most one bar (five) plus 0–4 dots. Plain dots, 10-slot frames and place-value ticks are removed. Digits sit left to right, most significant first, in one rounded numeral group. Decimals are reduced-height tiles after the whole part (no decimal pin). Zero is an empty tile with a slash, and unknown is an empty tile with a ring. A missing numeral means "unspecified", not "free". Inside a literal tile, digits are labels with no place value. Vague quantity becomes a wobbled numeral. | §6 (two systems, counting past 4, ticks, width, pin, zero/unknown, dot collisions); §3.6; §10 (5 px cells) |
| 8 | **Currency is mandatory.** A VALUE amount needs a currency name-tag (VALUE plus a literal tile showing the note or coin). "Local" is dropped. Without a tag the receiver asks. Machines must carry a currency field. | §3.7 |
| 9 | **Ring overload reduced.** VALUE becomes a stack of edge-on coins. AT becomes a dot inside four corner brackets. Pick-one circles are removed (candidates are separated by dividers). A gap declaration is now just an empty ring outside ASK. A ring now means only "unknown/unspecified". | §4 (ring); §10 (VALUE \= ASK ring, AT \= radio button) |
| 10 | **Top contact, containment and direction narrowed.** Top contact means attribute only. Intensity moves to the header line and "of this place" is gone. Containment means "whole ⊃ content/part" only. Location uses AT and movement uses ARROW. A bare ARROW means "toward the adjacent cell". Compass directions exist only in a *bearing frame*: a top-down figure with a wedge pointing up, which defines forward. The up \= forward rule for plain messages is removed. | §4 (top contact, containment, arrow); §5 (reference frames) |
| 11 | **Actor rules made structural, and replies defined.** The actor may be omitted only in REQUEST/WARN when the body begins with a chevron (the actor is then the receiver). A REQUEST whose body is a single entity phrase means "give or bring this to me". After an ASK, a reply may be a lone MATCH/slashed-MATCH or the fragment that fills the ring. Every Core primitive has one fixed class (§3 below). | §5 (rules broken by my own demos; inconsistent classes) |
| 12 | **Line styles removed.** Dashed, double and hatched outlines are gone. WOBBLE is a discrete mark at a cell's top-right corner, never a property of the outline. Unregistered compositions must carry it. Picture, name payload and digit labels all share one *literal tile* (cut corner). | §9 (line-style classification, wobble vs noise); §4 (dashed overloaded); §2 (meta-marks) |
| 13 | **Contact is overlap.** Attached tiles overlap their parent by at least 15% of their own height, and sequence gaps are at least 25% of tile size. There are no near-touches. | §9 (1 px contact/gap); §10 |
| 14 | **Orientation is fixed.** Messages read left to right and are never mirrored. A right-pointing header arrow is the orientation check, so mirrored or rotated messages are invalid. | §8 and §9. This is a stated decision, not neutrality. |
| 15 | **Glyph redraws for small size:** CARD is a landscape rectangle with a thick band (no chip). ENCLOSURE has a filled door instead of a gap. SIZE is two squares side by side instead of nested. | §10 |
| 16 | **TOILET recomposed** as ENCLOSURE ⊃ \[BODY \+ WATER\] (excretion mark removed). TAXI is unchanged. Registry compounds may be rendered as one flattened glyph below 32 px, with the decomposition kept in the table. | §8 (vulgarity); §7 and §10 (long compounds, unreadable inner parts) |
| 17 | **Machine wire format specified.** Header: 1 byte (mood 2 b, urgency 2 b, reply 1 b, sender-present 1 b, receiver-present 1 b, spare 1 b). Node: 16 bits (id 6, relation to parent 2 \[sequence/attribute/instrument/contained\], negation 1, approximate 1, value 4 \[digit 0–9 or level 1–3\], group open/close 2). Payloads are length-prefixed. An unmapped node is an ASK-ring id plus payload and confidence. | §9 (encoding underspecified) |
| 18 | **Disclosure rule.** Any quoted Core size must be stated together with the Registry size. | §7 (Core undersells the learning load) |

---

## **2\. What I deliberately did not change**

* **Untested glyphs I have no evidence to improve:** WATER (drop vs tear/blood), VESSEL, FOOD (rice-bowl bias, hat at small size), GO (footprints), HAND, EYE, MOUTH, BLOCK, HEAT, SPEED. Redrawing without testing would be guessing.  
* **WARN as a spiky burst.** HARM is now a chevron with a jagged edge, so the two share a motif but no longer a role. Spike overload is reduced, not eliminated.  
* **MATCH / slashed-MATCH** as the yes/no pair, and **twin arrows** for exchange (the sync/refresh clash is untouched).  
* **Bottom contact \= instrument.** It is still a learned rule, and the demonstrations must teach it.  
* **Base 10, coin-and-card commerce, fire \= heat.** These cultural assumptions remain.  
* **No time, no coordination (and/or/because), no negatives, ranges, percentages, ordinals or units.** None are needed by the required scenarios, and adding them would grow the vocabulary. Fractions remain a partial disc.  
* **Nesting limit of two, one idea per message, and "cold water for sale" taking two messages.**  
* **Bootstrapping.** A person must still recognize the ring on the header line before ASK-based repair helps them.  
* **Pen-production burden.** It is still solved only by palette interfaces.  
* **Accessibility and speech rendering.** These need per-locale label tables, which are outside the protocol.  
* **Guessability claims.** They are still hypotheses, and v0.2 has not been tested with anyone.  
* **Core cap of 64** and the admit-one/retire-one rule.  
* **TAXI decomposition** (VEHICLE ⊃ \[PERSON \+ VALUE\]).  
* **Noticed while re-encoding, not in the critique:** "cold" is still expressed as a low HEAT level. A flame with one step may read as "slightly warm", so this is a likely v0.3 issue.

---

## **3\. Final Core vocabulary: 32 primitives**

v0.1 actually had 36, not the "about 40" I claimed. Removed: HEAD, DOT, WANT, HAVE. DIGIT FRAME became DIGIT. HARM moved class. Nothing was added.

* **Moods (4):** STATE, ASK, REQUEST, WARN  
* **Marks (5):** SLASH, WOBBLE, LEVEL (3 states), DIGIT (10 states), ARROW  
* **Chevron cells (5):** MATCH, AT, GIVE, GO, HARM  
* **Round cells (15):** ME, YOU, PERSON, BODY, HAND, MOUTH, EYE, WATER, FOOD, VALUE, CARD, BLOCK, VESSEL, ENCLOSURE, VEHICLE  
* **Dimensions (3):** HEAT, SIZE, SPEED

Counting every digit and level state as its own form, there are 32 − 2 \+ 13 \= 43\. **Registry: 2 entries** (TOILET, TAXI), both used only in the demonstrations.

---

## **4\. Final grammar rules: 22, plus 3 rendering rules**

I did not meaningfully reduce the rule count. I traded some rules for others, so "grammar too abstract" is only partly addressed. What improved is consistency and fewer shared visual forms.

**Frame**

1. A message is a header strip, a body of 1–7 cells, and a bold end cap. It reads left to right and is never mirrored or rotated.  
2. The header line gives the mood: arrow (STATE), arrow with ring (ASK), arrow pointing back at the sender (REQUEST), spiky burst around everything (WARN).  
3. The header may carry a topic glyph, and a LEVEL for urgency (REQUEST/WARN only).

**Roles**  
 4\. Body cells are round (entity) or chevron (action/relation), with one fixed class per primitive. Slot order is actor, action, object, then optional ARROW \+ entity for other roles.  
 5\. The actor may be omitted only in REQUEST/WARN when the body begins with a chevron, and it is then the receiver.  
 6\. A REQUEST body that is a single entity phrase means "give or bring this to me".  
 7\. GIVE without a recipient gives to the other party.

**Combination**  
 8\. Top contact means attribute (numeral or quality tile).  
 9\. Bottom contact means instrument ("by way of").  
 10\. Containment means whole ⊃ content/part.  
 11\. Two opposed arrows between two entities mean exchange.  
 12\. A rounded group outline lets a slash, numeral or attribute apply to several cells. Nesting is at most two levels.  
 13\. Contact is overlap of at least 15%, and sequence gaps are at least 25%.

**Logic and questions**  
 14\. A slash crosses exactly one outline, protrudes past it, and sits on a halo. It means "is not" in STATE/ASK and "must not" in REQUEST/WARN. "None" is a slashed entity, and "safe" is slashed HARM.  
 15\. An empty ring is "unknown/unspecified". In ASK it is a question, and elsewhere it is a declared gap. Its shape gives the expected class: round for a thing, chevron for an action, numeral tile for a quantity.  
 16\. Yes/no questions end with \[MATCH | slashed-MATCH\]. After an ASK, a reply may be a lone answer token or the fragment that fills the ring. Nothing else may omit the actor.  
 17\. For real ambiguity, candidate groups are separated by dividers and the reply repeats the chosen one. Money, hazards and identity must be echoed back, and machines always echo.

**Numbers**  
 18\. A numeral group holds digit tiles (0–1 bar plus 0–4 dots) from most to least significant. Zero is a slashed empty tile, unknown is a ringed empty tile, and decimals are reduced-height tiles. Digits inside literal tiles are labels.  
 19\. VALUE with a numeral needs a currency name-tag. VALUE without a numeral means "unspecified", never "free".

**Direction**  
 20\. A bare ARROW means "toward the adjacent cell". Compass directions exist only inside a bearing frame (top-down figure, wedge up \= forward), and LEVEL on the arrow means near/far.

**Names and uncertainty**  
 21\. A literal tile (cut corner) holds names, pictures and digit labels. Category glyph \+ literal tile \= name tag. Anything else outside the Core is composed, pictured in a literal tile, or pointed at with a dangling arrow.  
 22\. WOBBLE is a corner mark meaning "roughly this". Unregistered or improvised compositions must carry it.

**Rendering (not grammar)**

* R1. Tiles are at least 32 px, and numeral tiles at least 32 px with dots at least 4 px.  
* R2. Strokes and gaps are at least 2 px, and no Core glyph relies on a feature smaller than 1/6 of its tile or uses more than three strokes.  
* R3. Registry compounds may be flattened below 32 px, with the decomposition kept in the registry.

---

## **Regression check of the seven messages**

This is a consistency check, not a redesign.

| \# | Encoding (header → body) |
| ----- | ----- |
| 1 | ASK: WATER ▷AT YOU, \[MATCH | ⁄MATCH\] |
| 2 | Reply: MATCH. Then STATE: ME ▷GIVE WATER (top: HEAT \+ LEVEL 1\) ⇄ VALUE (no numeral) |
| 3 | REQUEST: \[VESSEL ⊃ WATER\] (top: 3). Then ASK: ME ▷GIVE (bottom: CARD) VALUE, \[MATCH | ⁄MATCH\] |
| 4 | Reply: MATCH. Then STATE: YOU ▷GIVE VALUE-tag (literal tile: local note/coin; top: 6\) |
| 5 | ASK: TOILET ▷AT ○(empty ring). Reply fragment: bearing frame with arrow forward-left, LEVEL 2 |
| 6 | REQUEST (header LEVEL 3): TAXI |
| 7 | WARN: THIS (dangling arrow at the real thing) ▷HARM YOU. Then WARN: ⁄\[▷GO ARROW ENCLOSURE\] |

Registry: TOILET \= ENCLOSURE ⊃ \[BODY \+ WATER\]. TAXI \= VEHICLE ⊃ \[PERSON \+ VALUE\].

The test in message 4 changed: v0.1 had a bare noun phrase with no actor, which broke its own rule. v0.2 uses "YOU GIVE" instead. Message 6 no longer carries a level on the action, so it can't be read as "three taxis".

I only have the URL, not the documentation, so I'll fetch the repository before comparing anything.The README gives an overview but not the grammar details, so I'll fetch the linked protocol spec too.The protocol spec links to the grammar, numeric notation and governance documents. I'll fetch those three so the comparison rests on the actual rules.\# Trace v0.2 vs Pictiq: structural comparison

**Sources read:** the README, `spec/PROTOCOL.md`, `spec/GRAMMAR.md` and `spec/NUMERIC_NOTATION.md`. I did not read the vocabulary governance file, the message schema, the profiles or the handbook. I also could not inspect the icon SVGs, so visual-metaphor claims rest on icon IDs and prose only. Where I say Pictiq lacks something, I mean "not in the documents I read".

Similarity labels: **\[N\]** near-identical solution, **\[P\]** same principle, different implementation, **\[S\]** superficial similarity.

---

## **1\. Design goals**

* **\[P\]** Both target short practical messages across language barriers, and neither claims to replace natural language.  
* **Difference:** Pictiq targets physical carriers (stickers, cards, shirts, signs, pointing) and treats the live human body as part of the channel. Trace treats the message as a self-contained artifact for humans and machines. Trade-off: Pictiq spends fewer symbols because gesture supplies context, but a message can be underspecified once the sender leaves. Trace stays complete in isolation but pays in grammar size.  
* Pictiq also states meaning-before-wording, priority-first and "functional sufficiency". Trace aims at faithful structure and has no explicit sufficiency principle.

## **2\. Core vocabulary strategy**

* **\[P\]** Both use a small base, composition first, and tiers or layers for the rest. Trace has Core, Registry and Ad hoc. Pictiq has Canonical Registry, Core, Standalone Core, Context Packs and Entity Registry.  
* **Difference:** Pictiq gives everyday concepts like taxi, toilet and hotel their own tiles (its registry has 87 ordinary icons). Trace forced TOILET and TAXI to be Registry compounds. Trade-off: single tiles are faster and more legible at small size, while compounds keep the vocabulary provably composable but are long.  
* Pictiq's "Canonical ≠ Core" separation lets the registry grow without inflating Core. Trace's Core is defined by a count (32).

## **3\. Visual metaphors**

* **\[P\]** Both prefer depiction of objects and body parts, monochrome vector rendering, and no text as a symbol. Pictiq forbids `<text>` in canonical SVGs and uses `currentColor`.  
* **Difference:** Trace also uses performative forms (slash, spike, ring, arrow) as grammar. Pictiq's few operators are drawn as vector paths (`?`, `!`, `+`, `-`, `>`, `<`) and depend on convention. Trade-off: geometric operators are compact but learned. Familiar punctuation shapes are quicker to recognize for literate users, but they carry cultural baggage.  
* Pictiq has explicit perceptual QA at multiple scales. My equivalent was three rendering rules (R1–R3) derived from a paper critique.

## **4\. Composition**

* **\[P\]** Both compose BASE \+ QUALIFIER, and both keep qualifiers attached to what they qualify. My top-contact attribute corresponds to Pictiq's postfix qualifier.  
* **Difference:** Pictiq is strictly one-dimensional: adjacency in a line. Trace uses 2D operators (top and bottom contact, containment, group outlines). Trade-off: 1D is easy to lay out and parse and survives cropping and resizing. 2D gives more distinct relations per symbol but needs contact detection, which I identified as fragile.  
* **\[S\]** Both discourage long strings, but Pictiq caps a phrase at 5 tiles (3 recommended) and Trace at 7 cells.

## **5\. Grammar**

* **\[N\]** Left-to-right reading, and one idea per phrase or message.  
* **Difference:** Pictiq has no roles. Bare adjacency means contextual association, with no subject, object or word-order rule. Trace has typed slots (actor, action, object), class-coded outlines and mood-dependent omission rules. Trade-off: Pictiq has minimal training cost and little to get wrong structurally, but relations like "A gives B" or "A must not X" are left to context. Trace makes roles explicit and machine-checkable, at the cost of about twenty rules.  
* Pictiq's grammar is honest about being a draft and lists many "do not add X" decisions (no AND, BECAUSE, I/YOU).

## **6\. Questions**

* **\[P\]** Both use an explicit interrogative marker. Pictiq uses terminal `punct_question` applying to the whole phrase. Trace uses an ASK mood in the header plus an empty ring in the unknown slot.  
* **Difference and trade-off:** a terminal mark mimics written language and is recognizable, but it is overloaded (where, how, is there, can I) and arrives after the content. A header mood tells the receiver how to read before reading, and the class-shaped ring says what kind of answer is expected. This costs a header and a rule.

## **7\. Yes/no**

* **\[P\]** Both allow a single-token answer. Pictiq: `logic_yes`, `logic_no` stand alone. Trace: MATCH / slashed MATCH.  
* **Difference:** Trace appends an answer pair to yes/no questions, which makes a question self-explaining in interfaces but adds two cells. Pictiq keeps questions short and relies on the responder knowing the convention.  
* Pictiq's yes/no is deliberately polysemous (confirm, accept, open, ok / negate, forbid, closed, not ok), and it keeps evaluation (`qual_good/bad`) separate from truth.

## **8\. Negation**

* **\[N\]** The idea is the same: an explicit operator applies to the adjacent unit, and prohibition and negation share one form. Pictiq states it as `X + logic_no`, with scope of the immediately preceding unit.  
* **Implementation difference:** Trace overlays a slash on the crossed outline. Pictiq places a postfix token and mentions a physical slash only as a marker shortcut for printed goods. Trade-off: an overlay occludes the negated glyph and depends on precise drawing. A postfix token is easy to detect but its scope becomes ambiguous as phrases grow, and Pictiq handles this by splitting or reformulating.  
* **Difference:** Pictiq allows fixed negations as single lexicon tiles for signage. Trace composes negation and separates "is not" from "must not" by mood. Pictiq's `logic_no` covers both readings and leaves them to context.

## **9\. Quantity and numbers**

* **\[P\]** Both use an additive tally with a "five" unit: Pictiq's `qty_1`, `qty_2`, `qty_5` (`qty_1 + qty_2` \= 3, `qty_5 + qty_5` \= 10\) and my digit tile (one bar for five plus 0–4 dots). Both also have a positional digit layer for exact numbers, in which digits run left to right.  
* **Difference:** Pictiq keeps four things separate: small counts, "more/less" (`qty_plus`, `qty_minus`), exact numerals, and approximate quantity by composition (`qty_5 + qty_plus` \= many). Trace uses one system, with a wobbled numeral for vague amounts. Trade-off: separating practical quantity from exact numerals prevents `5+5 = 10` from being confused with `50`, and it keeps small orders simple. One system is more uniform but makes every quantity a numeral.  
* Pictiq's numeric layer is only partly implemented (digits 0 and 5), and it says it is not designed for precision above about 10\. I found no currency mechanism in what I read. Trace mandates a currency tag, distinguishes zero from unknown, and has no equivalent of `qty_plus/minus`.

## **10\. Direction and relations**

* **\[P\]** Both use geometric relation marks, and both have a deictic "here": Pictiq's `rel_here`, my dangling arrow or AT.  
* **Difference:** Pictiq has four comparison/orientation operators (`rel_greater`, `rel_lesser`, `rel_up`, `rel_down`). In a navigation context they read as right, left, up and down, and the spec says they do not solve navigation. Trace has an ARROW with an adjacent-cell rule and a bearing frame with a defined forward. Trade-off: Pictiq's dual use (compare and orient) saves symbols but leaves the reference frame to context. Trace's frame is more explicit but is a learned convention.  
* Pictiq deliberately leaves direction to pointing in embodied use.

## **11\. Context and polysemy**

* **\[P\]** Both narrow meaning by domain: Pictiq's context packs and my topic glyph. Both use clarification and repair dialogue.  
* **Difference (philosophical):** Pictiq embraces polysemy where it is action-relevant (`body_mouth` \= eat/drink, `money_coins` \= pay, `move_public` \= ride). Trace's rule is one form, one meaning, plus pick-one, echo-back and a topic glyph. Trade-off: polysemy reduces vocabulary and matches how people interpret objects, but risks an uncorrected wrong reading. Trace's rule avoids silent misreadings, but it needs more symbols and more turns.

## **12\. Proper names and entities**

* **\[P\]** Both keep names out of the ordinary vocabulary and count them separately. Pictiq uses namespaced entity symbols, and Trace uses a category glyph plus a literal tile.  
* **Difference:** Pictiq mints a stable visual identifier per entity, with provenance, authority, aliases and self-defined marks, and it forbids text inside tiles. Trace carries an opaque payload verbatim (original script, logo, digits, position). Trade-off: minted symbols are recognizable, memorable and governed, but need a registry and scope. Payload tags work immediately with no registry, but are not visual identities and reintroduce script.

## **13\. Missing meaning**

* **\[P\]** Both refuse to fake exactness.  
* **Difference:** Pictiq classifies absence at design time: EMBODIED-OMITTABLE, STANDALONE-GAP, OUT-OF-SCOPE, INTENTIONAL\_OMISSION (also LOSSY versus GAP). Trace marks it at run time: WOBBLE, an empty ring, a fallback ladder, and a machine "unmapped" flag with confidence. Trade-off: Pictiq's taxonomy guides vocabulary decisions and avoids treating every gap as a defect. Trace's marks tell a receiver in the moment that a symbol is approximate. The two answer different questions.

## **14\. Vocabulary-growth governance**

* **\[N\]** In principle: compose before adding, and require demonstrated need (Pictiq's NEED-BEFORE-VOCABULARY and DEFERRED\_UNTIL\_NEEDED, my demand test).  
* **Implementation difference:** Pictiq uses an ordered decision tree (embodiment, existing tile, composition, modifier, parameter, entity) plus classification metadata and perceptual QA before acceptance. Trace uses a numeric cap with admit-one/retire-one and registry expiry. Trade-off: a cap forces prioritisation but may block a needed concept. A procedural gate is more flexible but relies on discipline, since the registry has no ceiling. Pictiq's Core boundary is a classification, so I cannot verify a Core count.

## **15\. Human readability**

* **\[S\]** Both stress recognizability and short messages.  
* **Difference:** Pictiq uses one uniform rounded-square frame, and its zero-intent rule means a single tile can be a message. It has a pointing-oriented Catalog Grid mode. Trace needs a header and shape classes before a message parses. Trade-off: Pictiq has lower training and higher underspecification. Trace has a stricter reading but a higher entry cost.

## **16\. Machine readability**

* **\[P\]** Both aim for a machine-parsable form of the same message.  
* **Difference:** Pictiq has working artifacts: canonical SVGs, a JSON schema, a renderer, validators, CI, and notes that a recognizer should detect tile boundaries and distinguish grid from line. My wire format is only a paper spec. The uniform tile frame makes segmentation easy, whereas my overlap-based contact and outline classes were the CV weaknesses I flagged. Trade-off: a flat token stream is easy to encode but carries less structure. My tree carries roles and negation scope but needs harder image parsing.

---

## **Independently invented, already in Pictiq**

* Small base, composition first, need-gated growth \[N\]  
* One proposition per message, with short length caps \[N\]  
* Left-to-right reading \[N\]  
* Explicit negation operator applying to the adjacent unit \[N\]  
* Attribute and quantity attached to the thing counted \[P\]  
* A five-unit additive tally \[P\]  
* Positional digits for exact numbers \[P\]  
* Standalone yes/no answer tokens \[P\]  
* A deictic "here" \[P\]  
* Names kept separate from ordinary vocabulary \[P\]  
* Domain hint to narrow readings \[P\]  
* Repair by clarification \[P\]  
* Monochrome, text-free glyphs \[P\]  
* An urgency marker (my header LEVEL versus `punct_exclaim`) \[P\]  
* Everyday concepts like toilet and taxi as reusable units, though I made them compounds

## **Pictiq ideas my design did not discover**

* **Zero-intent:** a bare tile is a valid message.  
* **Embodied versus Standalone communication:** designing symbols only for what the body cannot supply, and profiles built on that.  
* **Uniform tile frame** as segmentation unit, and **Catalog Grid mode** for pointing at unordered keywords.  
* **Action-relevant polysemy** as a deliberate principle, with nouns doubling as actions.  
* **Canonical ≠ Core ≠ Packs** layering, and the ordered vocabulary decision tree.  
* **Meaning-before-wording, priority-first and functional sufficiency**, including INTENTIONAL\_OMISSION versus LOSSY versus GAP.  
* **Scoped entity symbols** with provenance, authority and self-defined personal marks.  
* **Parametric tiles** (COLOR) and separate **evaluation modifiers** (`qual_good/bad`).  
* **Structural gender neutrality**, fixed negations for signage, and comparison operators (`rel_greater/lesser`).  
* **Perceptual QA and CI validation** as part of the standard, plus SVG-first tooling.

## **Trace ideas Pictiq does not currently use**

* Header strip with sender/receiver figures and a mood (statement, question, request, warning)  
* Typed slots (actor, action, object) and class-coded outlines  
* Answer pair on yes/no questions, and class-shaped empty rings for open questions  
* Echo-back for money, safety and identity, and a pick-one disambiguation format  
* Mandatory currency tag, plus the distinction between zero, unknown, unspecified and free  
* "Must not" versus "is not" by mood, a dedicated hazard mood, and hazard type by composition  
* LEVEL scale with dimension tiles, and a bearing frame with a defined forward  
* In-message WOBBLE, gap mark, fallback ladder, and machine unmapped flag with confidence  
* Verbatim literal tile for original-script payloads  
* Bit-level wire format  
* Hard vocabulary cap with admit-one/retire-one and registry expiry  
* Orientation check to reject mirrored or rotated messages

## **Differences worth testing experimentally**

1. **Bare tile vs framed message:** compare intent recovery for "water?" as a bare tile versus a headed, moded message.  
2. **Terminal `?` vs header ASK ring:** measure the correct-question rate and the "what kind of answer" rate.  
3. **Postfix `logic_no` vs overlay slash:** measure scope errors, small-size legibility and recognizer accuracy.  
4. **Prohibition vs description:** test "do not enter" versus "closed" or "not ok" under polysemous `logic_no` versus mood-separated negation.  
5. **Price entry:** compare additive `qty_*`, bar-and-dot digits and positional digits on prices like 6 and 12.50, for both error rate and time.  
6. **Single tile vs compound:** test guessability of a drawn toilet or taxi tile against a composed one, at 24–32 px.  
7. **Uniform frame vs class-coded outlines:** compare CV segmentation accuracy and human reading speed.  
8. **Polysemy vs one-form-one-meaning:** measure how often `money_coins` \= "pay" is misread as "price" or "cash only", and the cost of wrong readings.  
9. **Embodied vs standalone:** run the same messages with and without the communicator present, and test whether ME/YOU-type tiles are ever needed.  
10. **Entity symbols vs literal payload tags:** compare recognition and reuse for names.  
11. **Echo-back on money and safety:** measure the error reduction against added friction.  
12. **Length cap:** compare 5 versus 7 cells for completion of the seven scenario messages.

