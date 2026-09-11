At small sizes, the strongest evidence-supported predictors of icon performance are not “solid versus outline” alone. They are **semantic closeness, familiarity, distinctive characteristic cues, low harmful complexity, adequate contrast/negative space, and sufficient physical display size**. Filled silhouettes often have an advantage at very small sizes because their gross shape and visual mass survive reduction, but outlines can outperform fills when the object’s identity depends on interior or edge-defining detail that would disappear in a solid shape.

For Pictiq, the practical rule is: make each tile identifiable from its **largest surviving features** at 24 px; use 64 px as the main semantic-reading size; and reserve fine internal structure, multi-symbol compounds, and expressive illustration for larger print or expandable views.

## **What empirical work supports**

Several recurring variables have been measured in icon and pictogram research:

* **Familiarity:** how often users have encountered the depicted object, convention, or icon.  
* **Semantic distance:** how directly the visual form suggests the intended function or meaning.  
* **Concreteness:** how much the icon resembles a recognizable real-world object rather than an abstract sign.  
* **Visual complexity:** amount of detail, components, lines, enclosed shapes, visual edges, and internal structure.  
* **Meaningfulness/recognizability:** whether people can form an interpretation and distinguish the icon from alternatives.  
* **Size and viewing conditions:** pixel/physical size, contrast, background, viewing distance, and screen/print quality.  
* **Set-level distinctiveness:** whether neighboring icons are visually confusable.

A foundational icon-characteristics dataset explicitly treats concreteness, complexity, meaningfulness, familiarity, and semantic distance as central variables for symbol usability. More recent empirical work similarly identifies familiarity, recognizability, concreteness, simplicity, and close semantic distance as major contributors to perceived icon effectiveness.\[[link.springer](https://link.springer.com/article/10.3758/BF03200730)\]\[[pmc.ncbi.nlm.nih](https://pmc.ncbi.nlm.nih.gov/articles/PMC11371222/)\]

The evidence does **not** support a simple universal ladder such as:

photograph \> illustration \> outline icon \> silhouette

for every user and task. Photos can be more concrete but include distracting backgrounds, viewpoint-specific detail, culturally unfamiliar objects, and visual clutter. A well-designed line drawing on a clean background may be easier to interpret than a poorly chosen photograph. Research on visual-symbol representation explicitly cautions that “photos are easier than line drawings” is an overgeneralization; individual experience, ability to learn, exposure history, and the symbol’s iconicity all matter.\[[talkingmats](https://www.talkingmats.com/the-hierarchy-of-visual-representation/)\]

## **What matters most**

### **1\. Semantic closeness and familiarity**

The single most important conceptual question is:

> Does the picture naturally suggest the meaning you want—not merely depict an object associated with it?

A magnifying glass is visually concrete, but its function can be search, zoom, inspect, investigate, filter, or find. Its **semantic distance** from “search” is lower when it is in a search field or search tab than when it is alone in an unfamiliar control.

Experimental work on vehicle-control icons found that closer semantic distance improved recognition efficiency and search time; cultural background also affected search efficiency and recognition time, with an interaction between culture and semantic distance. That is directly relevant to Pictiq’s cross-language ambitions: a pictogram with a good visual rationale may still be interpreted differently by different user groups.\[[nature](https://www.nature.com/articles/s41598-026-37943-8)\]

Familiarity has robust effects. In experiments involving visual search and semantic recall, users performed significantly better with icons depicting more familiar objects. Other work found familiarity affects performance even in complex cognitive tasks, not just simple icon naming.\[[pmc.ncbi.nlm.nih](https://pmc.ncbi.nlm.nih.gov/articles/PMC6024531/)\]\[[pmc.ncbi.nlm.nih](https://pmc.ncbi.nlm.nih.gov/articles/PMC7059235/)\]

### **Practical implication**

Prefer:

WATER       a simple glass, bottle, or drop only when task context clarifies it  
TOILET      an established facility symbol in a wayfinding context  
PHONE       a universally recognizable handset/device form  
FOOD        a plate/bowl/utensil convention tested with target users  
STOP        a standard stop/prohibition form plus explicit action context

Be cautious with:

SAVE        floppy-disk metaphor  
SYNC        circular arrows/cloud  
PRIVACY     lock/shield/eye-with-slash  
AI          sparkles/brain/chip  
SUBSCRIBE   bell/ribbon/star/crown  
QUALITY     badge/check/diamond  
MARKET      shopfront/chart/coins/handshake

These may be visually recognizable but semantically distant from the intended software, administrative, or financial action.

For Pictiq, use a symbol’s **conceptual core**, not an English word’s many senses. `LOCK` can be a physical object. `PRIVATE`, `SECURE`, `NEEDS AUTHORIZATION`, `PAID FEATURE`, and `READ-ONLY` should not all default to the same lock tile without explicit contextual modifiers.

### **2\. Complexity: simplify until the characteristic cue survives**

Visual complexity is usually operationalized as the amount of visual detail—components, horizontal/vertical/diagonal lines, open/closed figures, letters, and internal edges. Higher icon complexity has been associated with worse visual-search performance, including longer reaction times and more errors for older adults.\[[cronfa.swan.ac](https://cronfa.swan.ac.uk/Record/cronfa60870/Download/60870__25083__05f0eb1ea8da4be591214186344e2f2c.pdf)\]\[[pmc.ncbi.nlm.nih](https://pmc.ncbi.nlm.nih.gov/articles/PMC9026834/)\]

But “simple” must not mean “generic.” An over-simplified icon may lose the very feature that makes it distinctive:

A solid rounded rectangle:  
could be a phone, book, door, package, screen, card, or container.

A simple rectangle with one carefully retained cue:  
phone \= speaker/camera notch  
book \= central spine/open-page form  
package \= top flap/tape seam  
door \= hinge/handle relationship  
screen \= stand or bezel relationship

The design problem is to preserve the **diagnostic cue**—the small visual feature that lets a user distinguish the category—while removing non-diagnostic detail.

A study comparing filled and outline icon variants found an average tendency toward faster recognition for filled icons, but some outlined icons were recognized faster because characteristic cues were more visible in outline form. Narrow internal spacing and closely packed outline lines weakened recognition.\[[digitalcommunications.wp.st-andrews.ac](https://digitalcommunications.wp.st-andrews.ac.uk/2021/09/23/should-icons-be-solid-or-hollow/)\]

### **Practical implication**

For every Pictiq tile, define:

Primary silhouette:  
What should still identify the tile at a glance?

Diagnostic cue:  
What one or two visual features distinguish it from nearby tiles?

Forbidden loss:  
What simplification would make it merge with another concept?

Example:

| Concept | Primary silhouette | Diagnostic cue | Do not remove |
| ----- | ----- | ----- | ----- |
| `PLACE/HOME` | House-like roof \+ base | Door/opening | Roof-to-wall relationship |
| `DOCUMENT` | Sheet/rectangle | Folded corner or text band | Page asymmetry; otherwise resembles card/screen |
| `PACKAGE` | Box/block | Flap, seam, tape, or 3D top plane | Cargo/box identity |
| `PHONE` | Handset/device | Speaker/camera/notch or curved receiver profile | Feature separating it from a generic screen |
| `ALERT` | Triangle/attention mass | Exclamation or radiating signal | Difference from “play,” “arrow,” or “mountain” |
| `WATER` | Drop/glass/bottle | Context-appropriate container/action | Pure droplet may mean weather, flood, moisture, or liquid |
| `MEDICINE` | Pill/bottle/cross | Pill split or bottle cap | Must differ sharply from food and chemical hazard |
| `MOVE` | Directional body/object movement | Clear source/target or arrow role | Avoid generic arrow ambiguity |

### **3\. Visual mass and silhouette**

“Visual mass” is not always measured as a standalone variable in the research literature, but it captures why filled forms often survive reduction: large contiguous regions remain visible after anti-aliasing, scaling, compression, glare, or imperfect printing.

At 24 px, the eye often receives only:

* Overall bounding shape.  
* Major positive/negative regions.  
* One or two high-contrast features.  
* Directionality.  
* Relative weight and symmetry.

Fine strokes, small holes, intricate corners, gradients, and realistic texture collapse first.

The filled-versus-outline evidence points to a conditional conclusion:

| Situation | Likely better treatment | Reason |
| ----- | ----- | ----- |
| Distinct object has a strong silhouette | Filled/solid form | Gross contour and mass remain visible at small size |
| Outline has thin strokes or cramped interior gaps | Filled or simplified outline | Internal structure will blur or merge |
| Object’s identity depends on an interior opening, gap, or edge feature | Open/outline or mixed form | Filling may erase the diagnostic cue |
| Dense icon grid | Consistent low-detail fill/outline system with strong differentiation | Avoid visual noise and neighbor confusion |
| Low contrast / glare / dark mode | Higher mass and contrast; avoid delicate strokes | Thin lines lose visibility |
| Large educational/illustrative use | Outline, mixed, or detailed drawing can work | Users have enough pixels and attention to inspect structure |

The small comparative study found that filled icons were generally recognized faster, while outlined icons could be faster when they made distinctive features clearer. The right Pictiq policy is therefore **silhouette-first, not fill-dogma**.\[[digitalcommunications.wp.st-andrews.ac](https://digitalcommunications.wp.st-andrews.ac.uk/2021/09/23/should-icons-be-solid-or-hollow/)\]

### **4\. Negative space is structural, not decorative**

Negative space is the empty area around and inside a pictogram. At small sizes it does three jobs:

1. Separates the icon from the tile boundary.  
2. Prevents internal strokes/areas from merging.  
3. Preserves diagnostic holes, openings, and direction cues.

An outline icon fails at 24 px when its line gaps become too narrow. A filled icon fails when interior holes close up or when its mass becomes an undifferentiated blob.

Examples:

Good small-scale key:  
large circular bow \+ broad shaft \+ one clear tooth.

Bad small-scale key:  
tiny ring \+ thin shaft \+ three tiny teeth \+ decorative bevels.

Good small-scale speech bubble:  
large rounded mass \+ one obvious tail \+ wide interior void.

Bad small-scale speech bubble:  
thin outline \+ tiny tail \+ small nested quotation marks \+ cramped interior.

A useful geometric heuristic for Pictiq:

At 24 px:  
\- Preserve at least one obvious exterior contour change.  
\- Preserve no more than 1–2 critical interior voids.  
\- Avoid several parallel narrow gaps.  
\- Avoid detail whose only function is realism.  
\- Keep the main icon away from the tile border.

The exact pixel value depends on rasterization and display density, so do not encode a universal minimum stroke width as an aesthetic law. Instead test actual raster exports at target sizes and lighting/background conditions.

### **5\. Scale matters—and age/familiarity moderate it**

In an eye-tracking study of older adults, larger pictogram and text sizes improved icon readability and legibility. When pictograms exceeded 72 × 72 px in the study’s search task, participants tended to fixate text before pictograms, suggesting that size changes how people distribute attention between word and image.\[[pubmed.ncbi.nlm.nih](https://pubmed.ncbi.nlm.nih.gov/34970924/)\]\[[journals.sagepub](https://journals.sagepub.com/doi/abs/10.1177/00187208211061938)\]

Another study using eye-tracking, EEG, and behavioral measures concluded that a 10–20 mm physical icon range was generally effective across tested display contexts, selecting 13 mm and 16 mm as representative points.\[[onlinelibrary.wiley](https://onlinelibrary.wiley.com/doi/full/10.1002/eng2.12577)\]

The research does **not** provide a clean empirical threshold saying that “24 px is universally readable” or “64 px is sufficient for every icon.” Pixel dimensions depend on:

* Device pixel density.  
* CSS pixel versus physical pixel mapping.  
* Viewing distance.  
* Brightness and contrast.  
* Visual acuity and age.  
* Motion, glare, and ambient light.  
* Whether the user must identify, select, compare, or remember the symbol.  
* Whether the symbol appears alone or among similar neighbors.

Still, 24 px, 64 px, and large print are useful Pictiq design tiers.

## **Comparing visual styles**

### **Solid silhouettes**

**Strengths**

* Preserve overall contour and visual mass at small scale.  
* Often support faster rapid recognition when the outer shape is distinctive.  
* Render reliably in low-resolution, monochrome, and imperfect print conditions.  
* Work well in dense UI grids, quick status markers, and small physical labels.  
* Can be detected comparatively well by computer vision because the foreground region is clear.

**Weaknesses**

* May remove internal cues needed to tell one object from another.  
* Can make many icons look like similar blobs if the set shares rounded geometry.  
* Can obscure distinctions between a physical object and an abstract action.  
* May make multi-part concepts difficult without becoming heavy or crowded.

**Best Pictiq use**

24 px controls  
urgent action/status  
navigation anchors  
high-contrast signage  
small tile sequences  
machine-vision/scan profile

### **Outline icons**

**Strengths**

* Preserve internal construction and edge cues.  
* Can distinguish items that would merge as silhouettes.  
* Often work well at medium/large sizes.  
* Can feel less visually heavy in content-dense UI.  
* Support a coherent, calm, editorial visual system.

**Weaknesses**

* Thin strokes, close parallel lines, and cramped internal detail degrade rapidly at small scale.  
* Low-contrast outlines fail on varied or dark backgrounds.  
* Outline style can exaggerate set-level inconsistency when some concepts require many more lines than others.  
* Requires more careful optical correction across sizes.

**Best Pictiq use**

64 px semantic tiles  
learning materials  
reference charts  
medium-scale UI  
concepts where interior geometry is diagnostic

### **Mixed solid-and-outline icons**

**Strengths**

* Can preserve a strong mass while retaining one essential interior cue.  
* Often best for a Pictiq system that needs both fast scanning and compositional semantics.  
* Supports a clear hierarchy: filled primary object, outlined secondary feature, or vice versa.  
* Allows status overlays without destroying the base symbol.

**Weaknesses**

* Easily becomes stylistically inconsistent.  
* Requires firm rules about which layer is solid, which is outline, and what overlays mean.  
* At small size, the secondary outline may still vanish.

**Best Pictiq use**

Core object \+ diagnostic detail  
Object \+ status marker  
Action \+ target relation  
64 px default tile system  
24 px only after testing each compound

A good mixed strategy:

Main concept: filled silhouette  
Diagnostic cue: one negative-space opening or bold outline  
State marker: small fixed-position badge  
Role marker: consistent border/attachment zone

### **Detailed illustrations**

**Strengths**

* Can depict unfamiliar objects, physical procedures, spatial relationships, or culturally specific scenes.  
* Useful for instructional sequences, teaching, medical demonstrations, and long-form documentation.  
* Can show context that a single icon intentionally omits.

**Weaknesses**

* Poor at small scale.  
* High visual complexity slows search and increases errors, particularly for older users.\[[pmc.ncbi.nlm.nih](https://pmc.ncbi.nlm.nih.gov/articles/PMC9026834/)\]  
* More likely to encode unnecessary cultural detail, gender stereotypes, environment, clothing, or misleading specificity.  
* Harder to maintain as a reusable symbol system.  
* Difficult to compose into compact phrases.

**Best Pictiq use**

Large print instructions  
onboarding  
tooltips and expanded descriptions  
training materials  
“explain this tile” views  
not the base tile at 24 px

### **Photographs**

**Strengths**

* High realism for a specific person, object, location, or product.  
* Useful when identity and visual verification matter: actual door, actual medication package, actual meeting point, actual damaged cargo.  
* Can reduce semantic distance for users who need to recognize a real-world referent.

**Weaknesses**

* Usually not a good semantic primitive.  
* Background, lighting, viewpoint, quality, cultural context, and clutter may obscure the intended concept.  
* A photo shows an instance, not necessarily a category or relationship.  
* Poor composability: a photo of a hotel does not cleanly mean lodging, booking, room, destination, or check-in.  
* Difficult to scale consistently and unsuitable for a compact universal lexicon.  
* Can introduce privacy, consent, bias, and localization problems.

**Best Pictiq use**

Reference/example layer  
entity disambiguation  
location confirmation  
product/cargo verification  
photo \+ Pictiq concept, never photo instead of the semantic concept

### **Practical comparison**

| Property | Solid silhouette | Outline icon | Detailed illustration | Photograph | Mixed solid/outline |
| ----- | ----- | ----- | ----- | ----- | ----- |
| 24 px recognizability | High when contour is distinctive | Medium; depends on stroke/gaps | Low | Low–medium | High if controlled |
| 64 px semantic richness | Medium | High | Medium–high | High for instance recognition | High |
| Large-print instruction | Medium | High | High | High | High |
| Fast visual search | High | Medium | Low–medium | Medium | High |
| Abstract/compositional use | High | High | Low–medium | Low | High |
| Physical-object identification | Medium | Medium | High | Very high | Medium–high |
| Cross-cultural portability | Medium–high after testing | Medium–high after testing | Medium | Variable | Medium–high after testing |
| Visual system consistency | High | High | Lower | Low | Medium–high |
| Machine-vision robustness | High | Medium | Medium | Variable | High |
| Main risk | Blobby ambiguity | Vanishing strokes/clutter | Detail overload | Instance/context confusion | Inconsistent visual grammar |

## **Practical rules by size**

### **24 px: recognition and control scale**

At 24 px, a Pictiq tile should behave more like a **traffic sign or interface control** than a miniature illustration. The viewer should identify the broad concept, direction, and state quickly.

Use this tier for:

* Navigation controls.  
* Status chips and badges.  
* Dense message strings.  
* Inline UI actions.  
* Compact mobile toolbars.  
* Small inventory/status labels.  
* Simple machine-vision target profiles.

#### **Rules**

1. **Design for the silhouette first.**  
   Ask whether the icon is distinguishable as a black shape at 24 px. If it only works when users inspect small internal lines, it is not a reliable 24 px primitive.  
2. **Use one dominant visual mass.**  
   Prefer one clear foreground mass rather than several detached fragments.  
3. **Keep one diagnostic feature.**  
   A door opening, bottle cap, speech-bubble tail, page fold, box seam, wheel, arrowhead, or person head may be enough. Do not include five such details.  
4. **Avoid thin parallel strokes and micro-texture.**  
   They alias, merge, or disappear across devices and print.  
5. **Use generous negative space.**  
   Keep the pictogram comfortably inside the square tile. Do not make the tile frame compete with the icon.  
6. **Do not depend on color alone.**  
   State must remain visible in monochrome, low brightness, color-vision variation, and print. Use fill, shape, badge position, or pattern as a second channel.  
7. **Avoid complex compounds.**  
   At 24 px, one tile should normally carry one core concept or one standard operator. Render multi-part Pictiq messages as several separate tiles, not several mini-icons inside one tile.  
8. **Give each operator a non-confusable geometry.**  
   `NOT`, `QUESTION`, `WARNING`, `DONE`, `MORE`, `LESS`, `UP`, `DOWN`, `OPEN`, and `CLOSE` should not be differentiated only by tiny details.  
9. **Prefer fixed status zones.**  
   If a tile needs a state badge, reserve a consistent corner or border strip. Do not float arbitrary overlays over the base concept.  
10. **Test at actual CSS size.**  
    Inspect in a dense row, touch-target context, dark/light mode, reduced contrast, and a low-quality screenshot—not only in a vector editor at 800%.

#### **24 px Pictiq targets**

Strong:  
HOME  
BACK  
SEARCH  
ADD  
REMOVE  
STOP  
PLAY  
PAUSE  
HELP  
WARNING  
DONE  
LOCK  
UNLOCK  
UP  
DOWN  
OPEN  
CLOSE  
WATER  
FOOD  
TOILET  
PHONE  
LOCATION

Needs careful testing:  
SAVE  
SYNC  
SHARE  
FILTER  
SORT  
EDIT  
ARCHIVE  
FAVORITE  
PRIVATE  
PUBLISH  
SCHEDULE  
MEDICINE  
PAYMENT  
PERMISSION  
QUALITY  
MARKET  
ANALYTICS

### **64 px: semantic tile scale**

At 64 px, Pictiq can become a readable semantic unit rather than only a fast control. This is a sensible baseline for:

* Communication boards.  
* Educational material.  
* Agent-action previews.  
* Dashboard cards.  
* Context Pack selectors.  
* Pictiq phrase builders.  
* Accessibility-oriented large controls.  
* Medium-distance signage.  
* Web cards and mobile action sheets.

#### **Rules**

1. **Use a stable primary silhouette plus one or two secondary cues.**  
   This supports both quick scanning and precise distinction.  
2. **Allow controlled outline detail.**  
   A page fold, route line, handle, wheel, drop, pill split, or simple face/body cue can be useful if the gaps remain wide.  
3. **Permit mixed style only under system rules.**  
   Example: primary object filled; semantic relation outlined; status badge fixed in top-right; negation always a diagonal overlay or separate operator tile.  
4. **Express relations through composition, not miniature scenes.**  
   Prefer:  
   \[TRUCK\] \[MOVE\] \[BOX\] \[TO\] \[WAREHOUSE\]  
   rather than a 64 px illustration of a truck, box, arrow, road, warehouse, weather, driver, and clock all fused together.  
5. **Preserve visual grammar across the lexicon.**  
   Similar semantic classes should share controlled structural conventions, but do not make them so visually similar that users confuse them.  
6. **Use labels during learning and for abstract concepts.**  
   Evidence consistently favors familiar, semantically close icons; an unfamiliar or abstract Context Pack tile should launch with a short visible label, glossary, or long-press expansion.\[[nature](https://www.nature.com/articles/s41598-026-37943-8)\]\[[pmc.ncbi.nlm.nih](https://pmc.ncbi.nlm.nih.gov/articles/PMC6024531/)\]  
7. **Test with close neighbors.**  
   Test `HOME` next to `LODGING`, `DOCUMENT` next to `CARD`, `PACKAGE` next to `CONTAINER`, `OPEN` next to `UPLOAD`, `UPLOAD` next to `SEND`, `ERROR` next to `WARNING`, and `MEDICINE` next to `FOOD`.  
8. **Test task interpretation, not only naming.**  
   “What does this mean?” and “What will happen if you choose it?” are different questions. ISO 9186’s symbol-comprehension procedure explicitly asks respondents what they think a symbol means and, where relevant, what action they should take.\[[cdn.standards.iteh](https://cdn.standards.iteh.ai/samples/59226/10ccdf51569a4aeb87e0b42671a6c0e9/ISO-9186-1-2014.pdf)\]

### **Large print: instruction and reference scale**

For large print—roughly a poster, physical card, printed guide, wall sign, or screen tile viewed at distance—you can add meaningful structure, but should still avoid confusing detail with information.

Use this tier for:

* Tourist/transport cards.  
* Field-operation checklists.  
* Warehouse instruction boards.  
* Humanitarian support cards.  
* Educational posters.  
* Pictiq book pages.  
* Large-format signage.  
* Detailed tool/action confirmation panels.

#### **Rules**

1. **Use illustration only when it clarifies a real relationship.**  
   Show a person lifting incorrectly versus correctly, a route through a building, a handwashing sequence, or a cargo orientation—not decorative texture.

**Show procedural sequence spatially.**  
Use numbered panels or stable left-to-right/top-to-bottom order:  
1\. \[CHECK\]  
2\. \[SCAN\]  
3\. \[LOAD\]

2. 4\. \[CONFIRM\]  
3. **Use large clear grouping.**  
   Containers, arrows, whitespace, and numbered stages should show whether the relationship is sequence, condition, alternative, warning, or explanation.  
4. **Pair with short local-language text for public/safety use.**  
   A pictogram can assist recognition, but high-stakes instructions should not depend on pictogram comprehension alone. ISO 9186 exists because comprehensibility must be tested rather than assumed.\[[cdn.standards.iteh](https://cdn.standards.iteh.ai/samples/59226/10ccdf51569a4aeb87e0b42671a6c0e9/ISO-9186-1-2014.pdf)\]\[[iso](https://www.iso.org/obp/ui/)\]  
5. **Use photographs only for instance-specific confirmation.**  
   A photo can help someone identify the actual entrance, correct package, damaged seal, or meeting point. Pair it with a Pictiq category tile and a short text label.  
6. **Maintain distance readability.**  
   Design for the intended viewing distance and lighting; a detailed 300 px illustration is not automatically legible from 3–5 meters.

## **A Pictiq visual grammar**

Rather than choosing “all solid” or “all outline,” define a grammar that uses visual treatment deliberately.

### **Suggested role system**

| Pictiq visual role | Suggested treatment | Why |
| ----- | ----- | ----- |
| Core concrete noun | Strong silhouette; filled or mixed | Fast category recognition |
| Action / verb | Directional silhouette or object-in-action; clear motion cue | Distinguish event from object |
| Relation operator | Small but geometrically distinct sign; fixed placement or separate tile | Avoid ambiguity from ordinary arrows |
| Status/state | Fixed-position badge, border state, or fill pattern | Lets base concept remain stable |
| Negation | Separate `NOT` tile or unambiguous scope overlay | Do not let a decorative slash obscure the object |
| Quantity | Typed numeral plus unit; not a tiny pictorial approximation | Precision belongs to text/numerical layer |
| Time | Clock/calendar class plus actual date/time text when needed | Clock image alone does not encode a deadline |
| Warning/urgency | Shape plus pattern/label, not color alone | Works in monochrome and for color-vision variation |
| Domain Pack specialization | Core tile plus a clear modifier or conventional compound | Keeps the core stable and reduces new-glyph proliferation |
| Entity-specific reference | Photo, name, code, or QR/NFC-linked data alongside Pictiq | A generic icon cannot identify a particular person/container/location |

### **Default style recommendation**

For Pictiq’s intended mix of message tiles, SVG assets, UI use, print, and potential camera parsing:

24 px Scan/Compact Profile:  
  Bold filled or mixed silhouettes,  
  strong outer contour,  
  one diagnostic negative-space feature maximum,  
  stable border and orientation,  
  no intricate internal line art.

64 px Core Profile:  
  Primarily mixed silhouettes:  
  filled main form \+ controlled outline/negative-space cue,  
  consistent stroke system,  
  standard modifier zones,  
  optional short label during learning.

Large Print/Explain Profile:  
  Core tile retained unchanged,  
  expanded with instructional illustration,  
  local-language text,  
  optional photo for concrete instance identification.

This lets the same concept retain a recognizable identity across contexts rather than forcing one overloaded SVG to work at every scale.

## **Test protocol**

Pictiq should evaluate icon candidates with empirical tasks, not designer preference alone.

ISO 9186 provides a relevant baseline: it tests what proportion of people correctly understand a graphical symbol, asking what they think it means and, where relevant, which action they should take.\[[cdn.standards.iteh](https://cdn.standards.iteh.ai/samples/59226/10ccdf51569a4aeb87e0b42671a6c0e9/ISO-9186-1-2014.pdf)\]\[[iso](https://www.iso.org/obp/ui/)\]

### **Test each candidate at three levels**

| Test | Question | Failure indicates |
| ----- | ----- | ----- |
| Recognition | “What do you see?” | Visual form is not concrete or distinctive enough |
| Interpretation | “What does this tile mean here?” | Semantic distance or context dependence is too high |
| Action prediction | “What should you do after seeing/selecting this?” | Operational meaning is missing, ambiguous, or unsafe |
| Discrimination | “Which tile means X among these six?” | Neighbor collision or poor characteristic cue |
| Size robustness | “Can you identify it at 24/64/print distance?” | Detail, contrast, or negative-space failure |
| Memory | “Which tile represented X after delay?” | Weak visual identity/familiarity |
| Cross-cultural comprehension | “What does this mean for each target group?” | Cultural metaphor or convention is not portable |
| Accessibility | “Can the same meaning be accessed through text/speech/high contrast?” | Visual-only semantics are excluding users |
| Machine recognition | “Can parser/vision recover the right tile under distortion?” | Asset geometry lacks robust distinction |

### **Minimum candidate set**

Test a proposed icon against its likely confusions rather than against random unrelated symbols:

HOME         vs LODGING vs BUILDING vs PLACE  
DOCUMENT     vs CARD vs SCREEN vs BOOK  
PACKAGE      vs CONTAINER vs BOX vs CARGO  
MOVE         vs SEND vs UPLOAD vs GO  
OPEN         vs EXPAND vs UNLOCK vs START  
CLOSE        vs DELETE vs STOP vs COLLAPSE  
ALERT        vs WARNING vs ERROR vs DANGER  
CHECK        vs DONE vs APPROVE vs SELECT  
WATER        vs RAIN vs FLOOD vs DRINK  
MEDICINE     vs FOOD vs CHEMICAL vs FIRST AID

A Pictiq primitive should not enter the stable core merely because people can identify it alone. It should be judged on whether users distinguish it from its **semantic neighbors** at the smallest intended size.

## **Bottom line**

The empirical picture is consistent:

* **Familiarity and low semantic distance** are usually more important than fashionable visual style.\[[nature](https://www.nature.com/articles/s41598-026-37943-8)\]\[[pmc.ncbi.nlm.nih](https://pmc.ncbi.nlm.nih.gov/articles/PMC6024531/)\]  
* **Unnecessary visual complexity** harms search and recognition, especially for older users, but simplification must retain the concept’s diagnostic cue.\[[cronfa.swan.ac](https://cronfa.swan.ac.uk/Record/cronfa60870/Download/60870__25083__05f0eb1ea8da4be591214186344e2f2c.pdf)\]\[[pmc.ncbi.nlm.nih](https://pmc.ncbi.nlm.nih.gov/articles/PMC9026834/)\]  
* **Filled silhouettes often help at small sizes**, while outlines can win where an essential edge or interior feature must remain visible.\[[digitalcommunications.wp.st-andrews.ac](https://digitalcommunications.wp.st-andrews.ac.uk/2021/09/23/should-icons-be-solid-or-hollow/)\]  
* **Larger icons improve readability and legibility**, but size requirements depend on physical viewing conditions and user population.\[[pubmed.ncbi.nlm.nih](https://pubmed.ncbi.nlm.nih.gov/34970924/)\]\[[onlinelibrary.wiley](https://onlinelibrary.wiley.com/doi/full/10.1002/eng2.12577)\]  
* **Photos and illustrations are not automatically more comprehensible**; their effectiveness depends on relevance, context, familiarity, and clutter.\[[talkingmats](https://www.talkingmats.com/the-hierarchy-of-visual-representation/)\]  
* **Comprehension must be tested**, ideally by asking both what a symbol means and what action a viewer would take.\[[cdn.standards.iteh](https://cdn.standards.iteh.ai/samples/59226/10ccdf51569a4aeb87e0b42671a6c0e9/ISO-9186-1-2014.pdf)\]

For Pictiq, design tiles as robust, semantically close, highly distinguishable visual units—not as miniature illustrations. At 24 px, preserve the silhouette and one diagnostic cue. At 64 px, add controlled internal structure and compositional clarity. At large print sizes, use illustration, labels, and photographs only to expand the stable core symbol into an instructional or entity-specific layer.

