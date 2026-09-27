# Human Reconciliation Viewer v0.1

This static local tool presents all 81 exact candidates from the frozen Historical Composition Harvest v0.1 (`8fae507`). It reads the Harvest manifest and review dataset without modifying them. Creator decisions, optional reason tags, and notes are a separate overlay stored in this browser’s `localStorage` and exported/imported as JSON.

Open `index.html` through a local HTTP server from the repository root. For example:

```sh
python3 -m http.server 8765
```

Then open:

```text
http://localhost:8765/docs/research/composition-library-historical-harvest-v0.1/reconciliation/
```

The viewer checks the Harvest ID, snapshot, counts, and SHA-256 hashes of the frozen manifest and review dataset. If any check fails, it disables reconciliation controls and displays a warning. It starts with every decision as `UNREVIEWED` when no local overlay exists. Local decisions persist across reloads on the same browser/origin; export JSON to move review to another browser or keep an external copy. Import checks version, snapshot, IDs, decisions, and reason tags, and rejects unknown or duplicate IDs.

Exports contain all 81 overlay rows, the decision counts, and references to each record’s Harvest identity/source. Partial exports are allowed and explicitly marked. Comparison selections are temporary and are not included in the overlay. `Clear local reconciliation` requires confirmation and affects only this browser’s overlay.

This is a decision-capture tool only. It does not recommend decisions, alter Messages, interpret notes, accept a baseline, or begin the Practical Coverage Corpus. The excluded-evidence review remains separate at `../review/exclusions.html`.
