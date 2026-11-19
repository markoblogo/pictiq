import hashlib
import json
import re
import subprocess
import sys
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PKG = ROOT / "docs/research/composition-dictionary-baseline-v0.1"
VIEWER = PKG / "review/final-creator-qa-v0.2.html"
DATA_PATH = PKG / "review/final-creator-qa-v0.2.json"


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


def migration_runtime(html):
    return html[html.index("// K01a: exactly"):html.index("// K01A_RUNTIME_END")]


class FinalCreatorQATests(unittest.TestCase):
    def test_unique_scope_badges_and_recorded_decisions(self):
        data = load(DATA_PATH)
        entries = data["entries"]
        ids = [x["dictionary_entry_id"] for x in entries]
        self.assertEqual(len(entries), 10)
        self.assertEqual(len(ids), len(set(ids)))
        self.assertEqual(data["old_category_event_count"], 16)
        self.assertEqual(data["already_recorded_decisions_count"], 2)
        self.assertEqual(sum(len(x["badges"]) > 1 for x in entries), 6)
        mapping = data["old_category_memberships"]
        for entry in entries:
            for category in entry["legacy_category_memberships"]:
                self.assertIn(mapping[category], entry["badges"])
        by_corpus = {x["corpus_record_id"]: x for x in entries}
        self.assertEqual(by_corpus["clh-v01-0044"]["recorded_decision"], "MOVE_TO_CORPUS_ONLY")
        self.assertEqual(by_corpus["clh-v01-0044"]["pending_addendum"]["replacement"], None)
        self.assertEqual(by_corpus["clh-v01-0022"]["recorded_decision"], "ACCEPT_AS_SHOWN")
        self.assertEqual(by_corpus["clh-v01-0022"]["related_pending_entry"]["temporary_qa_id"], "qa-new-public-transport-timetable")
        self.assertEqual(by_corpus["clh-v01-0022"]["related_pending_entry"]["token_sequence"], "move_public + media_text + time + punct_question")
        self.assertEqual(data["remaining_unresolved_follow_up_count"], 0)
        self.assertEqual(len(by_corpus["clh-v01-0044"]["proposed_unaccepted"]), 5)
        self.assertTrue(all(x["exact_message"] is None and x["render"] is None for x in by_corpus["clh-v01-0044"]["proposed_unaccepted"]))

    def test_variant_visibility_scope_warnings_and_visual_pairs(self):
        data = load(DATA_PATH)
        html = VIEWER.read_text(encoding="utf-8")
        # This viewer is intentionally frozen. Reconstruct its exact bound
        # baseline through verified receipts, rather than treating it as live QA.
        from tools.research.communication_context_clarification import receipt_refs, verify_sequence
        refs = receipt_refs(load(PKG / 'manifest.json'))
        original, _, _ = verify_sequence((PKG / 'dictionary.json').read_bytes(),
                                         [load(PKG / r['path']) for r in refs], ROOT)
        self.assertEqual(hashlib.sha256((json.dumps(original, ensure_ascii=False, indent=2) + '\n').encode()).hexdigest(),
                         data['source_baseline']['dictionary_json_sha256'])
        entries = original['entries']
        for card in data["entries"]:
            source = next(x for x in entries if x["dictionary_entry_id"] == card["dictionary_entry_id"])
            self.assertEqual(len(card["accepted_variants"]), len(source["variants"]))
            for variant, source_variant in zip(card["accepted_variants"], source["variants"]):
                self.assertEqual(variant["message"], source_variant["message"])
                self.assertEqual(variant["type"], source_variant["variant_type"])
                self.assertTrue(variant["visible_in_viewer"])
                self.assertTrue((PKG / source_variant["render"]).is_file())
                sequence = " + ".join(t["id"] for f in variant["message"]["frames"] for t in f["tokens"] if t["type"] == "icon")
                self.assertEqual(sequence, variant["token_sequence"])
            if card["previous_state"]["message"]:
                self.assertNotEqual(card["previous_state"]["token_sequence"], card["current_baseline"]["preferred_token_sequence"])
        by_corpus = {x["corpus_record_id"]: x for x in data["entries"]}
        self.assertIn("MODE / CONTEXT MAY BE OVERSTATED", " ".join(by_corpus["clh-v01-0003"]["scope_warnings"]))
        self.assertEqual(by_corpus["clh-v01-0003"]["current_baseline"]["mode"], ["STANDALONE"])
        self.assertIn("SOURCE TASK ≠ CURRENT DICTIONARY SCOPE", " ".join(by_corpus["clh-v01-0047"]["scope_warnings"]))
        self.assertIn("LOCAL_ORDER_CORRECTION", by_corpus["clh-v01-0049"]["badges"])
        self.assertIn("DIRECT_PRIMITIVE_PREFERRED", by_corpus["clh-v01-0006"]["badges"])
        self.assertIn("RESET LOCAL QA", html)
        self.assertIn("localStorage.removeItem(KEY)", html)
        self.assertIn("EXPORT FINAL QA JSON", html)
        self.assertIn("validateImport(x)", html)
        self.assertIn("Show unreviewed only", html)

    def test_browser_overlay_export_import_validation_round_trip(self):
        data = load(DATA_PATH)
        html = VIEWER.read_text(encoding="utf-8")
        script = re.search(r"<script>(.*?)</script>", html, re.S).group(1)
        funcs = script[script.index("function exportRecords()") : script.index("function download(")]
        harness = f'''const DATA={json.dumps(data,ensure_ascii=False)};
const DECISIONS=["ACCEPT_AS_SHOWN","NEEDS_CORRECTION","MOVE_TO_CORPUS_ONLY","KEEP_ENTRY_CHANGE_PREFERRED","UNRESOLVED"];
let state={{}};let preservedExport=null;const KEY="fixture-key";
function locked(r){{return !!r.recorded_decision}}
function decision(r){{return locked(r)?r.recorded_decision:(state[r.dictionary_entry_id]?.decision||"UNREVIEWED")}}
function reviewed(r){{return locked(r)||!!state[r.dictionary_entry_id]?.decision}}
{funcs}
{migration_runtime(html)}
const records=exportRecords();
const payload={{qa_type:DATA.qa_type,version:DATA.version,source_baseline:DATA.source_baseline,qa_dataset_sha256:DATA.qa_dataset_sha256,pending_addendum:DATA.pending_addendum,unique_primary_entry_count:DATA.unique_primary_entry_count,entry_ids:DATA.entries.map(r=>r.dictionary_entry_id),reviewed_count:2,unresolved_follow_up_count:0,unresolved_decision_count:0,records}};
if(records.length!==DATA.unique_primary_entry_count)throw Error("record count");
if(DATA.entries.filter(reviewed).length!==2)throw Error("initial progress");
validateImport(payload);
state[DATA.entries.find(x=>!locked(x)).dictionary_entry_id]={{decision:"ACCEPT_AS_SHOWN",note:""}};
if(DATA.entries.filter(reviewed).length!==3)throw Error("progress after decision");
const updated={{...payload,reviewed_count:3,records:exportRecords()}};validateImport(updated);
for(const bad of [{{...updated,qa_dataset_sha256:"wrong"}},{{...updated,records:[...updated.records,updated.records[0]]}},{{...updated,records:updated.records.slice(1)}}]){{let rejected=false;try{{validateImport(bad)}}catch{{rejected=true}}if(!rejected)throw Error("invalid import accepted")}}
'''
        result = subprocess.run(["node", "-e", harness], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_pending_timetable_matches_explicit_creator_sequence(self):
        # Independent oracle: a three-token arrival Message is not a timetable.
        expected = ["move_public", "media_text", "time", "punct_question"]
        addendum = load(PKG / "final-creator-qa-addendum-v0.2.json")
        decision = next(d for d in addendum["decisions"]
                        if d.get("new_related_entry", {}).get("temporary_qa_id")
                        == "qa-new-public-transport-timetable")
        pending = decision["new_related_entry"]
        data = load(DATA_PATH)
        card = next(e for e in data["entries"]
                    if e["corpus_record_id"] == decision["corpus_record_id"])
        for name, record in [("addendum", pending),
                             ("viewer dataset", card["related_pending_entry"])]:
            with self.subTest(record=name):
                self.assertEqual([t["id"] for f in record["message"]["frames"]
                                  for t in f["tokens"]], expected)
                self.assertEqual(record["token_sequence"].split(" + "), expected)
                from tools.validate_message_schema import schema_errors, semantic_errors
                self.assertEqual(schema_errors(record["message"]), [])
                self.assertEqual(semantic_errors(record["message"]), [])
        preview = PKG / pending["preview_render"]
        self.assertEqual([el.attrib["data-id"] for el in ET.parse(preview).iter()
                          if "data-id" in el.attrib], expected)
        from tools.research.build_composition_dictionary_final_qa_v0_2 import make_addendum
        from tools.research.communication_context_clarification import receipt_refs, verify_sequence
        refs = receipt_refs(load(PKG / 'manifest.json'))
        dictionary, _, _ = verify_sequence((PKG / 'dictionary.json').read_bytes(),
                                           [load(PKG / r['path']) for r in refs], ROOT)
        by_corpus = {cid: e for e in dictionary["entries"] for cid in e["corpus_refs"]}
        generated = make_addendum(by_corpus, dictionary, pending["preview_render_sha256"])
        generated_pending = next(d["new_related_entry"] for d in generated["decisions"]
                                 if d.get("new_related_entry", {}).get("temporary_qa_id")
                                 == pending["temporary_qa_id"])
        self.assertEqual([t["id"] for f in generated_pending["message"]["frames"]
                          for t in f["tokens"]], expected)
        self.assertEqual([t["id"] for f in by_corpus[decision["corpus_record_id"]]
                          ["preferred_variant"]["message"]["frames"]
                          for t in f["tokens"]], ["move_public", "time", "punct_question"])
        self.assertEqual(addendum["status"], "PENDING_BASELINE_APPLICATION")
        self.assertEqual(hashlib.sha256(preview.read_bytes()).hexdigest(),
                         pending["preview_render_sha256"])
        self.assertEqual(hashlib.sha256((PKG / data["pending_addendum"]["path"]).read_bytes()).hexdigest(),
                         data["pending_addendum"]["sha256"])

    def test_k01_rejects_old_snapshot_without_migrating_decisions(self):
        revision = "f9be7228bf1b4a64ab52dd157e2663add3298d5a"
        relative = "docs/research/composition-dictionary-baseline-v0.1/review/final-creator-qa-v0.2.json"
        old = json.loads(subprocess.check_output(["git", "show", f"{revision}:{relative}"], cwd=ROOT))
        data = load(DATA_PATH)
        self.assertEqual(data["entries"], old["entries"])
        self.assertEqual(data["source_baseline"], old["source_baseline"])
        self.assertNotEqual(data["qa_dataset_sha256"], old["qa_dataset_sha256"])
        self.assertNotEqual(data["pending_addendum"]["sha256"], old["pending_addendum"]["sha256"])
        script = re.search(r"<script>(.*?)</script>", VIEWER.read_text(), re.S).group(1)
        funcs = script[script.index("function exportRecords()") : script.index("function download(")]
        # A historical export must still fail the snapshot guard, even with valid records.
        old_export = {**old, "entry_ids": [e["dictionary_entry_id"] for e in old["entries"]],
                      "records": [{"dictionary_entry_id": e["dictionary_entry_id"],
                                   "decision": e["recorded_decision"]} for e in old["entries"]]}
        harness = f"const DATA={json.dumps(data)};const oldExport={json.dumps(old_export)};const KEY=\"fixture-key\";" + funcs + migration_runtime(VIEWER.read_text()) + """
let rejected=false;try{validateImport(oldExport)}catch(e){
 if(e.message!=='QA dataset/addendum snapshot mismatch')throw e;rejected=true;}
if(!rejected)throw Error('old decisions silently rebound');
"""
        result = subprocess.run(["node", "-e", harness], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_preview_render_and_frozen_inputs_unchanged(self):
        data = load(DATA_PATH)
        preview = data["timetable_preview"]
        path = PKG / "review" / preview["path"]
        self.assertEqual(preview["token_sequence"], "move_public + media_text + time + punct_question")
        self.assertTrue(preview["valid"])
        self.assertIn("<svg", path.read_text(encoding="utf-8"))
        self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(), preview["sha256"])
        for repo_path in [
            "docs/research/composition-dictionary-baseline-v0.1/dictionary.json",
            "docs/research/composition-library-baseline-v0.1/accepted-corpus.json",
            "docs/research/composition-dictionary-baseline-v0.1/review/final-creator-visual-qa.html",
        ]:
            actual = (ROOT / repo_path).read_bytes()
            frozen = subprocess.run(["git", "show", f"59e23b2:{repo_path}"], cwd=ROOT, capture_output=True, check=True).stdout
            if repo_path.endswith('/dictionary.json'):
                # The original QA stays bound to these exact bytes. Verify the
                # explicit authorized description sequence back to that frozen input.
                from tools.research.communication_context_clarification import receipt_refs, verify_sequence, encode
                refs = receipt_refs(load(PKG / 'manifest.json'))
                predecessor, _, _ = verify_sequence(actual, [load(PKG / r['path']) for r in refs], ROOT)
                actual = encode(predecessor)
            self.assertEqual(actual, frozen, repo_path)


if __name__ == "__main__":
    unittest.main()
