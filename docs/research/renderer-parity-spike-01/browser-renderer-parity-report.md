# Browser Renderer Parity Report — Spike 01

- Status: **PASS**
- Architecture verdict: **ACCEPT_WITH_GUARDRAILS**
- Comparison level: functional/structural parity; byte equality recorded but not required
- Generated asset manifest: `docs/renderer/generated/pictiq-browser-assets.mjs` (347366 bytes)
- QA sheet: `docs/research/renderer-parity-spike-01/browser-renderer-parity-qa.svg`

| Fixture | Dimensions | Tokens/layout | Assets/byte | Color | Numeric | Entity | Result |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `01-ordinary-icon` | True | True | byte=True | True | True | True | **PASS** |
| `02-water-question` | True | True | byte=True | True | True | True | **PASS** |
| `03-alcohol-home-no` | True | True | byte=True | True | True | True | **PASS** |
| `04-multi-frame` | True | True | byte=True | True | True | True | **PASS** |
| `05-legacy-normalized` | True | True | byte=True | True | True | True | **PASS** |
| `06-number-50` | True | True | byte=True | True | True | True | **PASS** |
| `07-color-cloud` | True | True | byte=True | True | True | True | **PASS** |
| `08-entity-symbols-three` | True | True | byte=True | True | True | True | **PASS** |
| `09-road-wayfinding` | True | True | byte=True | True | True | True | **PASS** |
| `10-odyssey-narrative` | True | True | byte=True | True | True | True | **PASS** |

Performance snapshot:

- Browser total render time for fixture corpus: 5.32 ms under Node.
- Python total render time for fixture corpus: 8.107 ms.
- Measurements are a spike smoke check, not a benchmark.
