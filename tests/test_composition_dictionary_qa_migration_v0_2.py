"""Exercise the actual generated viewer's single K01a transition with isolated storage."""
import json
import re
import subprocess
import unittest
from unittest import mock
import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / 'docs/research/composition-dictionary-baseline-v0.1/review'
HTML = REVIEW / 'final-creator-qa-v0.2.html'


class SnapshotMigrationTests(unittest.TestCase):
    def run_js(self, body):
        html = HTML.read_text()
        data = json.loads((REVIEW / 'final-creator-qa-v0.2.json').read_text())
        runtime = html[html.index('// K01a: exactly'):html.index('// K01A_RUNTIME_END')]
        preamble = 'const DATA=' + json.dumps(data) + ';\n' + '''
const assert=require('node:assert/strict');
const DECISIONS=['ACCEPT_AS_SHOWN','NEEDS_CORRECTION','MOVE_TO_CORPUS_ONLY','KEEP_ENTRY_CHANGE_PREFERRED','UNRESOLVED'];
const KEY='pictiq.final-creator-qa.v0.2:'+DATA.qa_dataset_sha256;
const crypto=require('node:crypto').webcrypto;
const fs=require('node:fs'),path=require('node:path');
const elements={};const $=id=>elements[id]||(elements[id]={hidden:true,textContent:''});
let migrationLineage=null,storageLoadError=null;
class Storage{constructor(){this.map=new Map()}getItem(k){return this.map.get(k)??null}setItem(k,v){this.map.set(k,v)}}
const localStorage=new Storage();
'''
        fixtures = '''
const unlocked=MIGRATION.dataset.entries.filter(r=>!r.recorded_decision);
const originalOverlay={
 [unlocked[0].dictionary_entry_id]:{decision:'NEEDS_CORRECTION',note:'Owner note — retain exactly',reviewed_at:'2026-09-28T12:03:04Z'},
 [unlocked[1].dictionary_entry_id]:{note:'Unreviewed note',updated_at:'2026-09-28T12:04:05Z'}
};
const raw=JSON.stringify(originalOverlay);localStorage.setItem(OLD_KEY,raw);
const oldExport=oldOverlayExport(raw),sourceHash='a'.repeat(64),at='2026-11-18T12:00:00Z';
'''
        script = preamble + runtime + fixtures + '\n(async()=>{\n' + body + '\n})().catch(e=>{console.error(e);process.exit(1)});'
        result = subprocess.run(['node', '-e', script], cwd=ROOT, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_partial_progress_notes_timestamps_and_locked_choices(self):
        self.run_js('''
const before=stable(oldExport),result=installMigration(localStorage,oldExport,sourceHash,at,{raw});
assert.equal(result.status,'MIGRATED');assert.equal(result.output.reviewed_count,3);
assert.equal(stable(result.output.records),stable(oldExport.records));
assert.equal(result.output.records.find(r=>r.dictionary_entry_id===unlocked[1].dictionary_entry_id).decision,null);
assert.equal(result.output.records.find(r=>r.dictionary_entry_id===unlocked[0].dictionary_entry_id).reviewed_at,'2026-09-28T12:03:04Z');
assert.equal(validateSnapshotExport(result.output,DATA),true);
assert.equal(stable(oldExport),before);assert.equal(localStorage.getItem(OLD_KEY),raw);
assert.equal(result.envelope.original_source.raw,raw);
assert.equal(result.output.technical_migration.from_dataset_sha256,MIGRATION.old_dataset_sha256);
assert.throws(()=>validateSnapshotExport(oldExport,DATA),/snapshot mismatch/);
''')

    def test_rejects_wrong_snapshot_duplicate_unknown_ids_and_counters(self):
        self.run_js('''
for(const mutate of [
 x=>x.qa_dataset_sha256='bad',x=>x.pending_addendum.sha256='bad',
 x=>x.records[0].dictionary_entry_id='unknown',
 x=>x.records[1]=clone(x.records[0]),x=>x.entry_ids[1]=x.entry_ids[0],
 x=>x.records.pop(),x=>x.reviewed_count++,x=>x.unresolved_decision_count++,
 x=>x.records[0].decision='BAD',x=>x.records[0].corpus_record_id='wrong',
 x=>x.records.find(r=>r.decision_source==='PENDING_ADDENDUM').decision=null,
 x=>x.records.find(r=>r.decision==='NEEDS_CORRECTION').creator_note=''
]){const x=clone(oldExport);mutate(x);assert.throws(()=>migrateKnownExport(x,sourceHash,at))}
assert.equal(localStorage.getItem(OLD_KEY),raw);assert.equal(localStorage.getItem(KEY),null);
''')

    def test_changed_card_preview_locked_decision_or_baseline_stops_transfer(self):
        self.run_js('''
for(const mutate of [x=>x.entries[0].headword='changed',
 x=>x.entries[0].current_baseline.preferred_message.frames[0].tokens.pop(),
 x=>x.entries[0].current_baseline.preferred_render='wrong.svg',
 x=>x.entries.find(r=>r.recorded_decision).recorded_decision='UNRESOLVED',
 x=>x.source_baseline.dictionary_json_sha256='bad']){
 const changed=clone(DATA);mutate(changed);assert.throws(()=>assertKnownPair(MIGRATION.dataset,changed),/changed/)
}
''')

    def test_conflict_and_repeat_never_overwrite_or_merge(self):
        self.run_js('''
for(const target of ['not JSON',JSON.stringify({ownerWork:'keep'}),JSON.stringify({qa_overlay:{unrelated:'keep'}})]){
 localStorage.setItem(KEY,target);assert.throws(()=>installMigration(localStorage,oldExport,sourceHash,at,{raw}),/CONFLICT/);
 assert.equal(localStorage.getItem(KEY),target);assert.equal(localStorage.getItem(OLD_KEY),raw)
}
localStorage.map.delete(KEY);
installMigration(localStorage,oldExport,sourceHash,at,{raw});const installed=localStorage.getItem(KEY);
assert.equal(installMigration(localStorage,oldExport,sourceHash,at,{raw}).status,'ALREADY_MIGRATED');
assert.equal(localStorage.getItem(KEY),installed);assert.equal(localStorage.getItem(OLD_KEY),raw);
const changed=clone(oldExport);changed.records.find(r=>r.decision==='NEEDS_CORRECTION').creator_note='new note';
assert.throws(()=>installMigration(localStorage,changed,'b'.repeat(64),at,{raw}),/CONFLICT/);
assert.equal(localStorage.getItem(KEY),installed);
''')

    def test_write_failure_and_corrupt_source_preserve_original(self):
        self.run_js('''
localStorage.setItem=(k,v)=>{throw Error('quota exceeded')};
assert.throws(()=>installMigration(localStorage,oldExport,sourceHash,at,{raw}),/quota/);
assert.equal(localStorage.getItem(OLD_KEY),raw);assert.equal(localStorage.getItem(KEY),null);
assert.throws(()=>oldOverlayExport('broken JSON'));
assert.throws(()=>oldOverlayExport(JSON.stringify({unknown:{decision:'ACCEPT_AS_SHOWN'}})),/unknown/);
''')

    def test_old_progress_notice_and_runtime_preview_integrity(self):
        self.run_js('''
refreshMigrationNotice();assert.match(elements['migration-status'].textContent,/Saved work found.*3 \\/ 10/);
assert.equal(elements['migrate-local'].hidden,false);
const base=''' + json.dumps(str(REVIEW)) + ''';
global.fetch=async relative=>{const b=fs.readFileSync(path.resolve(base,relative));return {ok:true,arrayBuffer:async()=>b.buffer.slice(b.byteOffset,b.byteOffset+b.byteLength)}};
await verifyMigrationAssets();
global.fetch=async()=>({ok:true,arrayBuffer:async()=>new Uint8Array([1,2,3]).buffer});
await assert.rejects(verifyMigrationAssets(),/Preview changed/);
assert.equal(localStorage.getItem(OLD_KEY),raw);assert.equal(localStorage.getItem(KEY),null);
''')

    def test_generator_refuses_content_drift_before_writing_outputs(self):
        from tools.research import build_composition_dictionary_final_qa_v0_2 as builder
        outputs = [builder.ADDENDUM, builder.OUT_DATA, builder.HTML, builder.README,
                   builder.REVIEW / "previews/qa-new-public-transport-timetable.svg"]
        before = {str(p): hashlib.sha256(p.read_bytes()).hexdigest() for p in outputs}
        read = builder.read
        # Exercise drift in the complete historical QA input, not the smaller
        # active projection. Reversal verifies every intervening application.
        from tools.research.communication_context_clarification import receipt_refs, verify_sequence
        refs = receipt_refs(read(builder.PKG / 'manifest.json'))
        original, _, _ = verify_sequence((builder.PKG / 'dictionary.json').read_bytes(),
                                         [read(builder.PKG / r['path']) for r in refs], builder.ROOT)
        def changed(path):
            value = json.loads(json.dumps(original)) if path == builder.PKG / 'dictionary.json' else read(path)
            if path == builder.PKG / "dictionary.json":
                next(e for e in value["entries"] if "clh-v01-0022" in e["corpus_refs"])["headword"] += " unexpected"
            return value
        with mock.patch.object(builder, "read", side_effect=changed):
            with self.assertRaisesRegex(ValueError, "unexpected target snapshot"):
                builder.build()
        self.assertEqual(before, {str(p): hashlib.sha256(p.read_bytes()).hexdigest() for p in outputs})

    def test_full_generated_script_initializes_and_exports_migrated_progress(self):
        # Test the actual HTML script, not a second implementation of UI handlers.
        html = HTML.read_text()
        script = re.search(r'<script>(.*?)</script>', html, re.S).group(1)
        harness = '''
const vm=require('node:vm'),assert=require('node:assert/strict'),fs=require('node:fs'),path=require('node:path');
const old=JSON.parse(fs.readFileSync('docs/research/composition-dictionary-baseline-v0.1/repairs/K01-timetable-media-text/migration-source.json')).dataset;
const id=old.entries.find(r=>!r.recorded_decision).dictionary_entry_id;
const raw=JSON.stringify({[id]:{decision:'ACCEPT_AS_SHOWN',note:'realistic fixture',timestamp:'2026-09-28'}});
const oldKey='pictiq.final-creator-qa.v0.2:'+old.qa_dataset_sha256;
const store=new Map([[oldKey,raw]]),elements={},downloads=[];
function el(){return {value:'',checked:false,options:[{}],hidden:true,append(){this.options.push({})},addEventListener(){},click(){downloads.push(this.download)}}}
const document={getElementById:id=>elements[id]||(elements[id]=el()),createElement:()=>el(),querySelectorAll:()=>[]};
const base=''' + json.dumps(str(REVIEW)) + ''';
const context=vm.createContext({document,localStorage:{getItem:k=>store.get(k)??null,setItem:(k,v)=>store.set(k,v),removeItem:k=>store.delete(k)},
 console,TextEncoder,Blob,crypto:require('node:crypto').webcrypto,URL:{createObjectURL:()=>'',revokeObjectURL(){}},
 alert:message=>{throw Error(message)},confirm:()=>false,
 fetch:async relative=>{const b=fs.readFileSync(path.resolve(base,relative));return {ok:true,arrayBuffer:async()=>b.buffer.slice(b.byteOffset,b.byteOffset+b.byteLength)}}});
'''
        harness += 'vm.runInContext(' + json.dumps(script) + ',context);\n'
        harness += '''
(async()=>{
assert.match(elements['migration-status'].textContent,/Saved work found/);
await elements['migrate-local'].onclick();
assert.match(elements['migration-status'].textContent,/MIGRATED/);
assert.match(elements.progress.textContent,/3 \\/ 10/);
elements.export.onclick();assert.equal(downloads.length,2);
assert.equal(store.get(oldKey),raw);
vm.runInContext('validateImport({...snapshotExport(exportRecords()),technical_migration:migrationLineage})',context);
const output=vm.runInContext('exportRecords()',context);
assert.equal(output.find(r=>r.dictionary_entry_id===id).timestamp,'2026-09-28');
})().catch(e=>{console.error(e);process.exit(1)});
'''
        result = subprocess.run(['node','-e',harness],cwd=ROOT,capture_output=True,text=True)
        self.assertEqual(result.returncode,0,result.stderr)


if __name__ == '__main__':
    unittest.main()
