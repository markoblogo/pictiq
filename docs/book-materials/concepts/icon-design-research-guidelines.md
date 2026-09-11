# Icon Design Research Guidelines

> Status: research/design method
> Source event: Pictiq Research Foundations — Batch 03
> Scope: future icon QA method only; current filled-silhouette style and existing icons remain accepted.

## Evidence-based correction

Do not adopt the rule: **filled is always better than outline**.

Use this stronger working rule instead:

```text
SILHOUETTE-FIRST
+ DIAGNOSTIC-CUE PRESERVATION
+ SEMANTIC-DISTANCE CONTROL
+ NEIGHBOR DISCRIMINATION
+ ACTUAL-SIZE TESTING
```

Filled silhouettes can work well for Pictiq, but only when the gross shape, negative space, and distinguishing cues survive at the target size.

## Future icon-design template

| Field | Question |
| --- | --- |
| Primary silhouette | What gross shape must survive reduction? |
| Diagnostic cue | Which one or two features distinguish this concept from nearby concepts? |
| Forbidden loss | What simplification would make this icon merge with another concept? |
| Semantic neighbors | Which current/proposed icons are most likely to be confused with it? |
| Size tiers | What changes at 24 px, 64 px, and large print/physical use? |

Do not retroactively rewrite all icon records in this pass.

## Size testing boundary

Use 24 px, 64 px, and large print / physical use as practical QA tiers. Do not claim 24 px is universally readable or 64 px is universally sufficient. Comprehension depends on physical size, display density, distance, visual acuity, lighting, contrast, task, neighboring icons, and familiarity.

## Visual profile hypothesis

The source suggests possible Compact/Scan, Core, and Large Print/Explain visual profiles. Preserve this as a future hypothesis only. Do not create parallel SVG vocabularies until real testing or repeated failures justify them.

## Semantic neighbor testing

Test icons against likely confusions, not only unrelated icons. Future examples may include HOME vs lodging/building, DOCUMENT vs card/screen/book, WATER vs drink/rain/flood, WARNING vs error/danger, and MOVE vs send/go/upload. Use actual current Pictiq concepts when executing tests; do not create missing vocabulary for symmetry.
