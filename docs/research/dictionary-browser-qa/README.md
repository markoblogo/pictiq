# S01.21 — frozen Dictionary v0.1: real-browser QA

2026-11-19 (Europe/Paris). Source HEAD: `31cdc4f308f9398d957e2aa101cab8780917aec2`.
The working tree was clean before inspection. This is a read-only browser check,
with evidence recorded outside the frozen package; no fixes were applied.

```text
DICTIONARY BASELINE: FROZEN / PRESERVED
DICTIONARY BROWSER QA: FAIL
COMPOSER BROWSER QA: NOT PERFORMED
PUBLIC RELEASE: NOT PERFORMED
```

## Environment and method

- Browser: **Google Chrome**, the connected desktop browser on macOS (not a DOM
  simulation). Browser build number was not collected.
- Actual Viewer URL: `http://localhost:8000/docs/research/composition-dictionary-baseline-v0.1/review/index.html`.
- Server: the documented repository-root Python HTTP preview, bound to loopback:
  `python3 -m http.server 8000 --bind 127.0.0.1`.
- Tested CSS viewports: **1280 × 900** desktop and **390 × 844** narrow/mobile.
  The temporary size override was reset after inspection. This is responsive
  desktop-browser testing, not a physical mobile-device or Safari check.
- Opened the ordinary Dictionary Viewer. The Final Creator QA viewer, its browser
  decisions, localStorage and Composer were not inspected or changed.

The browser actually loaded the page and SVG images. Search, filters, history
expansion, a Corpus evidence link, browser Back and keyboard Enter were exercised.
Screenshots were visually inspected; read-only browser DOM measurements supplement
those observations. Neither source inspection nor Node tests substitute for this
pass. Detailed measurements are in [observations.json](observations.json).

## Five requested cases

| Case | Actual browser result | Desktop / mobile |
| --- | --- | --- |
| A — `pcd-v01-0006`, Less noise, please. | Search `Less noise` returns one card. All four SVG variants display: `comm_sound + qty_minus`, `comm_sound + rel_down`, `comm_speak + qty_minus`, `comm_speak + rel_down`. Oral/written/social-media communication and human-produced sound are described; natural sounds are excluded; expanded readings remain scoped to the two comm_sound forms. | Content and SVGs PASS on both; mobile text layout FAIL, BQA-01. |
| B — `pcd-v01-0028`, Pedestrian movement | One card; preferred `move_feet` is explicitly road-sign/WAYFINDING scoped. Both contextual forms remain visible: `person_generic + move_feet` and `person_generic + move_feet + rel_here`. The displayed text explicitly separates movement on foot from a crossing-point relation. | Content and three SVGs PASS on both; mobile text layout FAIL, BQA-01. |
| C — `pcd-v01-0025`, CORPUS_ONLY | Searches for its former title `No entry at this location` and its ID return `0 / 65` on both sizes. Clearing search returns all 65 cards; none uses a `pcd-v01-0025` render. It is not offered as an active Dictionary card. | PASS on both. Corpus-only disposition and preserved evidence are not changed. |
| D — `pcd-v01-0065`, arrival-time | Exact title search returns one card, with `move_public + time + punct_question`. Current text names separate arrival-time and timetable entries. There are zero paragraphs outside History containing `which remains unresolved`. Opening History reveals the original note explicitly labelled `Historical source note (superseded)` and the A7 application link. | Current/historical separation and SVG PASS on both; mobile text layout FAIL, BQA-01. |
| E — `pcd-v01-0066`, Public transport schedule / timetable | Exact title search returns its own card. The visible SVG shows transport, text, clock, question, in that order; the displayed sequence is `move_public + media_text + time + punct_question`. It is separate from arrival-time. | Content and four-sign SVG PASS on both; mobile text layout FAIL, BQA-01. |

No new semantic decision was made. These checks concern presentation of already
recorded decisions, not independent comprehension validation.

## Search and navigation

- Initial load and reload: **65 cards, 72 images, zero unloaded/broken SVGs**.
  Inspected case SVGs fit within their image bounds without reordered or clipped
  signs. At 390px their right edges remain within the viewport (e.g. timetable:
  x=16…328px); the defect affects surrounding text, not token order.
- `crossing` finds Pedestrian movement with the visible reason **“Match in related
  materials; title and aliases did not match.”** The headword stays unchanged.
  `comm_sound` finds Less noise, please. with a token-sequence/ID match reason.
- Clearing search restores `65 / 65`; `has variants` gives `4 / 65`,
  `context-dependent` gives `13 / 65`, `known ambiguity` gives `39 / 65`.
  Surface WAYFINDING gives `21 / 65`; Mode EMBODIED gives `1 / 65`.
  Pedestrian movement + BOOK gives zero, then + WAYFINDING gives one.
- Cards are inline; their existing History disclosures open/close by click, and
  keyboard Enter also opens/closes the disclosure. No new card route is assumed.
- From 0006 History, the Corpus link opened
  `http://localhost:8000/docs/research/composition-library-baseline-v0.1/review/corpus.html#clc-v01-0008-r1`.
  The fragment target exists and the corresponding heading landed at about 35px
  from the viewport top. Browser Back returned to the Dictionary with the
  `Less noise` query intact. This was a link check, not a Corpus audit.
- Console capture at initial load, after navigation/mobile scenarios and reload:
  **0 warnings, 0 errors** in the tab's captured warn/error log. No critical
  console error was observed during this run.

## Defects

**BQA-01 — Medium: horizontal overflow clips text at narrow/mobile width.**

Reproduce: open the Viewer at 390 × 844, search `Public transport schedule /
timetable`, then read the meaning, sequence and context without horizontal
scrolling. The document is 654px wide despite a 390px viewport; text extends past
the right edge. All four signs remain visible. Similar overflow is reproducible
for 0006 (662px), 0028 (706px), and 0065 (654px). With all cards shown, document
width is 718px; the empty-results state is 390px.

Desktop case measurements are 1280px document width at 1280px viewport width and
text is readable. On narrow width, horizontal panning is needed to read the
complete descriptions and sequence. This fails the requested mobile-readability
check, so the overall browser QA is **FAIL**, despite working search, navigation
and SVG loading. No Critical/High issue was observed in the tested scenarios.
No issue was corrected in this pass; the frozen research data remain valid and
unchanged.

## Screenshots

- [Desktop 0006 — all four variants](desktop-0006.jpg).
- [Desktop 0028 — preferred and contextual variants](desktop-0028.jpg).
- [Desktop 0065 — current arrival-time wording](desktop-0065.jpg).
- [Mobile 0066 — full document including overflow](mobile-0066.jpg).
- [Mobile 0066 — actual 390 × 844 viewport](mobile-0066-viewport.jpg).

The mobile full-page capture is 654px wide because it includes the overflowed
content. It does not mean a 654px viewport was tested. The separate viewport
capture shows the actual clipping at 390px.

## Preservation and limits

Viewer SHA-256: `a90feffd2f26d713b786bef63e901eac1d168993de27ef95a4dc5595e0944ee9`.
Frozen manifest SHA-256: `b07d839d192583f8b1a0ef5a897cc252f5644cdce671a432a57c240b2665bdf0`.
The frozen package, its generator, Dictionary/variants, all seven application
records, Messages, assets/SVG, creator exports and historical QA remain byte-for-
byte unchanged from the source revision. Only this evidence directory is added.
Recorded SHA-256 references and local evidence links are checked before commit;
`git diff --check` passes. The historical freeze record's `Browser visual check:
NOT VERIFIED` is intentionally not rewritten; this subsequent report records an
actual browser run with a failed mobile layout check.

No Composer QA, code/data fix, full semantic review, browser compatibility matrix,
public-site check, push, tag or release was performed.
