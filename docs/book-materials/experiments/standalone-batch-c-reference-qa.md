# Standalone Batch C reference QA

## Starting question

Can the next five standalone candidates be implemented from the approved reference image without changing existing icons or expanding the protocol into unrelated future concepts?

## Local candidate IDs

| ID | Class | Primary semantics | Standalone profile | Embodied profile |
| --- | --- | --- | --- | --- |
| `body_mouth` | lexical tile | mouth / eat / drink / oral intake | yes | omitted by default |
| `rel_here` | relation operator | here / target / reference location | yes | yes |
| `rel_up` | relation operator | up / above / higher | yes | yes |
| `rel_down` | relation operator | down / below / lower | yes | yes |
| `nature_moon` | lexical tile | moon / night / nighttime | yes | omitted by default |

## Architecture notes

Batch C reinforces contextual polysemy: an icon may cover related action meanings when the decision remains clear. `body_mouth` can mean mouth, eating, drinking, or oral intake in context, but it is not a speech or emotion tile.

The relation family now has horizontal and vertical operators: `rel_greater` (`>`), `rel_lesser` (`<`), `rel_up` (`∧`), and `rel_down` (`∨`). These remain distinct from `qty_plus` and `qty_minus`, which request quantity change.

`rel_here` is a target/reference operator, not a generic place tile. It is useful when the body or layout cannot reliably preserve the intended reference.

`nature_sun` and `nature_moon` may combine with `time` to indicate daylight and nighttime contexts. They do not define a complete calendar system.

## QA artifacts

Local visual sheets:

- `build/qa/batch-c.png`
- `build/qa/batch-c-compositions.png`

Both sheets are local review artifacts. Batch C remains pending human visual acceptance and is not released, tagged, or pushed by this local implementation task.
