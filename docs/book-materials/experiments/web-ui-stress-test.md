# Web/UI Pictiq Stress Test

> Source artifact: [Web/UI Pictiq Stress Test 2026-09](../../research/web-ui-stress-test-2026-09/README.md)  
> Status: local results for human review  
> Boundary: no vocabulary, grammar, Message Schema, Renderer, Composer, icon, Entity Symbol, Numeric Notation, profile, pack, or Context Pack change.

## Question

How well can current Pictiq represent common modern software/UI meanings without adding vocabulary during the test?

## What the test reveals

Software interfaces are already partial visual languages, but many UI icons are learned conventions rather than direct semantic drawings. The stress test therefore asked whether Pictiq could represent the intent, not whether it could copy conventional UI glyphs such as a floppy disk, gear, cloud arrow, or hamburger menu.

The 24-case frozen corpus produced a mixed result:

- direct or near-direct successes exist for current location, text content, success, and error/attention;
- many cases are possible only with strong UI context;
- several short compositions are technically renderable but too broad for reliable standalone UI meaning;
- three true gaps appeared: loading/processing, save/persistence, and archive/retain-but-hide.

## Main lesson

The cost problem is not mostly long sequences. The harder problem is overloaded short sequences. `logic_no`, `logic_yes`, `rel_here`, `rel_up`, `rel_down`, `rel_greater`, and `rel_lesser` are useful primitives, but UI contexts make them carry too many possible meanings.

## Conventional glyphs vs semantic representation

Pictiq should not add concepts merely to reproduce familiar software glyphs. The useful pressure comes from semantic gaps:

- process / wait / progress;
- persistence / save / record;
- archive / hidden-but-retained state;
- permission and role scope;
- edit/configure as abstract actions.

Upload/download are weaker candidates because the current up/down relation plus content can approximate them in a UI context, though mainly as a learned convention.

## Publication status

Publication milestone verdict: `PUBLICATION_MILESTONE_CANDIDATE`.

Possible editorial angle: **Can 83 Visual Symbols Describe a Modern Software Interface?**

Do not publish from this note directly. First preserve human review of the corpus, classifications, and figure choices.
