# Creator reconciliation — Historical Composition Harvest v0.1

**Review status:** `CREATOR REVIEW COMPLETE / BASELINE BLOCKED ON EDIT`
**Harvest snapshot:** `8fae507`
**Exported:** `2026-09-27T17:42:11.509Z`
**Source:** creator-supplied browser export, originally provided as `pictiq-human-reconciliation-v0.1-8fae507.json`
**Archived export:** [`creator-export-2026-09-27.json`](creator-export-2026-09-27.json)
**Archived export SHA-256:** `455588e54a561e162d4b8ffdad38ad1b0f59612ccb3fafb889cc6e8ba41b40bc`

## Reconciliation result

All 81 exported composition IDs map one-to-one to the frozen 81-record review dataset. The export reports 81 reviewed and 0 unreviewed; counting its row decisions gives the same result:

| Decision | Count |
|---|---:|
| `ACCEPT` | 77 |
| `ACCEPT_CONTEXTUAL` | 0 |
| `EDIT` | 1 |
| `REJECT` | 3 |
| `EVIDENCE_ONLY` | 0 |
| `UNREVIEWED` | 0 |

The export contains no reason tags or human notes on any row. Its `harvest_snapshot` is `8fae507`, and `harvest_version` is `0.1`.

## Decisions needing follow-up

- `clh-v01-0008` — “Less noise, please.” — `EDIT`. The review contains no note explaining the required correction and no replacement sequence. Keep it out of an accepted baseline until the creator supplies the intended correction or changes the disposition.
- `clh-v01-0070` — “Loading / processing” — `REJECT`.
- `clh-v01-0010` — “A beautiful blue hotel near the old city center.” — `REJECT`.
- `clh-v01-0012` — “This place is a battlefield.” — `REJECT`.

The `REJECT` entries record the creator’s disposition of these harvested candidates. They do not establish that related messages are invalid in every use or context.

## Interpretation and preservation boundary

This artifact records a creator review overlay over historical source-paired candidates. `ACCEPT` is not evidence of external comprehension, universal validity, a protocol change, or a separate product-level acceptance. No accepted Composition Library baseline is created by this report. The frozen manifest, review dataset, individual harvest records, renders, grammar, vocabulary, and protocol remain unchanged. The Practical Coverage Corpus remains not started.

**Next gate:** resolve the unannotated `EDIT` for `clh-v01-0008`; then decide whether to create a baseline from accepted dispositions while preserving source provenance and the three exclusions.

### Subsequent creator addendum

The creator later supplied explicit replacements for all four non-`ACCEPT` records and clarified that the `EDIT` is resolved by `comm_sound + qty_minus`. See [Creator Reconciliation Addendum — 2026-09-27](creator-reconciliation-addendum-2026-09-27.md). That later addendum supersedes the pending-EDIT statement above; the initial export and this first-pass report remain as historical evidence. Baseline processing is still a separate, not-yet-started stage.
