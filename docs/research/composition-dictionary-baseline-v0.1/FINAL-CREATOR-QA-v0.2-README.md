# Final Creator QA v0.2

**Status:** prepared; creator review is open. Dictionary Baseline v0.1 is unchanged and not frozen.

The v0.1 QA sheet grouped records under change categories, causing the same semantic entry to appear repeatedly (16 category events). That duplication invalidated it as a single-decision final gate; it does not by itself indicate a defect in the baseline. v0.2 aggregates all category memberships, variants, context, and pending questions into **10 unique entry cards**. Each entry gets one decision.

Open `review/final-creator-qa-v0.2.html` (local server URL: `http://localhost:8765/docs/research/composition-dictionary-baseline-v0.1/review/final-creator-qa-v0.2.html`). Actions are ACCEPT_AS_SHOWN, NEEDS_CORRECTION, MOVE_TO_CORPUS_ONLY, KEEP_ENTRY_CHANGE_PREFERRED, and UNRESOLVED. The two decisions already supplied in this task are shown as read-only evidence and counted reviewed; remaining cards start UNREVIEWED.

Editable decisions and notes live only in browser `localStorage`, keyed to the dataset snapshot. EXPORT / IMPORT uses JSON bound to baseline, dataset, and pending-addendum hashes; import rejects mismatched snapshots, unknown/duplicate IDs, missing entry records, invalid actions, and changed locked decisions. RESET LOCAL QA asks for confirmation and clears only the local overlay; it cannot remove the repository addendum.

K01a adds a fixed, explicit old→corrected snapshot transfer in this same viewer. It detects old local work, checks all unchanged card content and preview bytes, preserves the old key/export, and refuses to overwrite a nonempty target. Ordinary import still rejects old snapshots. Use **Transfer saved work from previous snapshot** or **Explicit old-export transfer**; the original export downloads before any target write. See [K01a verification](repairs/K01-timetable-media-text/K01a-REPORT.md).

`final-creator-qa-addendum-v0.2.json` records the new creator decisions with status `PENDING_BASELINE_APPLICATION`. The timetable preview uses the canonical renderer and lives under `review/previews/`; neither it nor the addendum is baseline data. No review decision is automatically applied.

After creator completes v0.2, a separate processing pass should apply the QA export and addendum, validate the resulting baseline, and freeze v0.1. Only after that research arc is complete should it be pushed; Color Modifier repair comes next. This task does not start that pass.

Dataset SHA-256: `45c041165ad17f2f8114dddd454ba42f74e9e635eb44606133f291348626f413`. Pending addendum SHA-256: `8c5cfda80ee90dea0e185d142249a03e6be83b7ec40f1523f07e74dcd5ed0b51`. Old v0.1 QA remains at `review/final-creator-visual-qa.html` unchanged.
