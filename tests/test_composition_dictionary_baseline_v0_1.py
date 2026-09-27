import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "docs/research/composition-dictionary-baseline-v0.1"
BUILDER = ROOT / "tools/research/build_composition_dictionary_baseline_v0_1.py"


class CompositionDictionaryBaselineTests(unittest.TestCase):
    def test_creator_dispositions_and_protected_decisions(self):
        manifest = json.loads((PACKAGE / "manifest.json").read_text())
        self.assertEqual(manifest["validation"], "PASS")
        self.assertEqual(manifest["counts"]["dictionary_entries"], 65)
        self.assertEqual(manifest["counts"]["render_count"], 70)
        amendment = json.loads((PACKAGE / "creator-review-amendment.json").read_text())
        records = amendment["records"]
        self.assertEqual(len(records), 65)
        self.assertEqual(sum(bool(x["creator_notes"].strip()) for x in records), 10)
        dictionary = json.loads((PACKAGE / "dictionary.json").read_text())
        entries = dictionary["entries"]
        self.assertEqual(len({x["dictionary_entry_id"] for x in entries}), 65)
        self.assertTrue(all(x.get("lineage", {}).get("source_provenance") is not None for x in entries))
        self.assertFalse(any("semantic_examples" in x for x in entries))
        former_review_ids = {"clh-v01-0002", "clh-v01-0007", "clh-v01-0011", "clh-v01-0017", "clh-v01-0022"}
        self.assertTrue(former_review_ids.issubset({x["corpus_refs"][0] for x in entries}))
        for entry in entries:
            for variant in entry["variants"]:
                self.assertTrue((PACKAGE / variant["render"]).is_file())
        followups = json.loads((PACKAGE / "creator-notes-follow-up.json").read_text())
        self.assertEqual(len(followups), 2)

    def test_outputs_are_reproducible(self):
        with tempfile.TemporaryDirectory() as td:
            outputs = []
            for name in ("first", "second"):
                out = Path(td) / name
                out.mkdir()
                shutil.copyfile(PACKAGE / "creator-review-export.json", out / "creator-review-export.json")
                subprocess.run([sys.executable, str(BUILDER), "--output-dir", str(out)], check=True, capture_output=True, text=True)
                outputs.append({p.relative_to(out): hashlib.sha256(p.read_bytes()).hexdigest() for p in out.rglob("*") if p.is_file()})
            self.assertEqual(outputs[0], outputs[1])


if __name__ == "__main__":
    unittest.main()
