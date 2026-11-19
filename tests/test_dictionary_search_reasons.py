"""Run the real generated viewer script and its original predecessor in a small DOM fixture."""
import hashlib
import json
import re
import subprocess
import unittest
from pathlib import Path

from tools.research.build_composition_dictionary_baseline_v0_1 import make_dictionary_viewer

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / 'docs/research/composition-dictionary-baseline-v0.1'
REVISION = '58d622eacc5357bdecddf7e52cd1f8c83eefe4fd'


class DictionarySearchReasonTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.html = (PACKAGE / 'review/index.html').read_text()
        old = subprocess.check_output(['git','show',REVISION+':docs/research/composition-dictionary-baseline-v0.1/review/index.html'],cwd=ROOT,text=True)
        cls.script = re.search(r'<script>(.*?)</script>',cls.html,re.S).group(1)
        cls.old_script = re.search(r'<script>(.*?)</script>',old,re.S).group(1)

    def run_js(self, body):
        harness = '''
const vm=require('node:vm'),assert=require('node:assert/strict');
const plain=x=>JSON.parse(JSON.stringify(x));
function viewer(script){
 const elements={};const el=()=>({value:'',checked:false,hidden:true,append(){},addEventListener(){}});
 const context=vm.createContext({document:{getElementById:id=>elements[id]||(elements[id]=el()),createElement:el}});
 vm.runInContext(script,context);return {elements,context};
}
function results(view,q,filters={}){
 for(const id of ['mode','surface'])view.elements[id].value=filters[id]||'';
 for(const id of ['variants','contextual','ambiguity'])view.elements[id].checked=!!filters[id];
 view.elements.q.value=q;vm.runInContext('draw()',view.context);
 return {headings:[...view.elements.entries.innerHTML.matchAll(/<h2>(.*?)<\\/h2>/g)].map(m=>m[1]),
         html:view.elements.entries.innerHTML,count:view.elements.count.textContent};
}
'''
        harness += 'const current=viewer('+json.dumps(self.script)+');const original=viewer('+json.dumps(self.old_script)+');\n'
        # Compare the two real algorithms on the same current data. Authorized
        # applications may legitimately change variants, fields and matches.
        harness += "vm.runInContext('D.splice(0,D.length,...'+JSON.stringify(plain(vm.runInContext('D',current.context)))+')',original.context);\n" + body
        result = subprocess.run(['node','-e',harness],cwd=ROOT,capture_output=True,text=True)
        self.assertEqual(result.returncode,0,result.stderr)

    def test_crossing_related_only_and_visible_reason(self):
        self.run_js('''
const match=plain(vm.runInContext("dictionaryMatch(D.find(e=>e.dictionary_entry_id==='pcd-v01-0028'),'crossing')",current.context));
assert.deepEqual(match.groups,['related']);
assert.equal(match.reason,'Match in related materials; title and aliases did not match.');
const found=results(current,'crossing');assert.deepEqual(found.headings,['Pedestrian movement']);
assert.ok(found.html.includes('<h2>Pedestrian movement</h2><p class="match-reason">'+match.reason+'</p>'));
const entry=plain(vm.runInContext("D.find(e=>e.dictionary_entry_id==='pcd-v01-0028')",current.context));
assert.deepEqual(entry.aliases,[]);assert.equal(entry.semantic_neighbourhood,'Pedestrian movement / walking / movement on foot');
assert.equal(current.elements['search-limit'].hidden,false);
''')

    def test_title_tokens_and_multiple_field_groups(self):
        self.run_js('''
let match=plain(vm.runInContext("dictionaryMatch(D.find(e=>e.dictionary_entry_id==='pcd-v01-0028'),'pedestrian movement')",current.context));
assert.deepEqual(match.groups,['title_aliases','related']);assert.equal(match.reason,'Match in title / aliases; related materials.');
assert.ok(results(current,'pedestrian movement').html.includes(match.reason));
match=plain(vm.runInContext("dictionaryMatch(D.find(e=>e.dictionary_entry_id==='pcd-v01-0006'),'comm_sound')",current.context));
assert.deepEqual(match.groups,['token_sequences','related']);assert.ok(match.reason.includes('token sequences / IDs'));
assert.ok(results(current,'comm_sound').headings.includes('Less noise, please.'));
match=plain(vm.runInContext("dictionaryMatch(D.find(e=>e.dictionary_entry_id==='pcd-v01-0006'),'noise')",current.context));
assert.deepEqual(match.groups,['title_aliases','related']);assert.equal(match.reason,'Match in title / aliases; related materials.');
match=plain(vm.runInContext("(()=>{const e=JSON.parse(JSON.stringify(D.find(e=>e.dictionary_entry_id==='pcd-v01-0006')));e.aliases=['comm_sound'];return dictionaryMatch(e,'comm_sound')})()",current.context));
assert.deepEqual(match.groups,['title_aliases','token_sequences','related']);
match=plain(vm.runInContext("(()=>{const e=JSON.parse(JSON.stringify(D.find(e=>e.dictionary_entry_id==='pcd-v01-0006')));e.semantic_neighbourhood='';e.candidate_lookup_material=[];return dictionaryMatch(e,'comm_sound')})()",current.context));
assert.deepEqual(match.groups,['token_sequences']);
''')

    def test_original_order_queries_and_all_existing_filters(self):
        self.run_js('''
const surfaces=plain(vm.runInContext('[...new Set(D.flatMap(e=>e.surface))]',current.context));
const filters=[{}, {mode:'EMBODIED'},{mode:'STANDALONE'}, {variants:true},{contextual:true},{ambiguity:true},
 {mode:'STANDALONE',variants:true,contextual:true,ambiguity:true},...surfaces.map(surface=>({surface}))];
for(const q of ['crossing','pedestrian movement','comm_sound','noise','','no-k05-match-9df52','headword','"aliases":[]',' CROSSING ']){
 for(const f of filters){const actual=results(current,q,f),old=results(original,q,f);
  assert.deepEqual(actual.headings,old.headings,{q,f});assert.equal(actual.count,old.count,{q,f});}
}
const empty=results(current,'');assert.equal(empty.headings.length,65);
assert.ok(!empty.html.includes('class="match-reason"'));assert.equal(current.elements['search-limit'].hidden,true);
assert.deepEqual(results(current,'no-k05-match-9df52').headings,[]);
assert.match(results(current,'"aliases":[]').html,/search metadata or combined field text/);
''')

    def test_corpus_only_entry_is_not_in_live_viewer_or_search(self):
        self.run_js('''
assert.equal(vm.runInContext("D.some(e=>e.dictionary_entry_id==='pcd-v01-0025')",current.context),false);
assert.equal(vm.runInContext('D.length',current.context),65);
assert.deepEqual(results(current,'No entry at this location').headings,[]);
assert.ok(!results(current,'').headings.includes('No entry at this location'));
''')

    def test_timetable_is_found_as_a_separate_live_entry(self):
        self.run_js('''
const entry=plain(vm.runInContext("D.find(e=>e.dictionary_entry_id==='pcd-v01-0066')",current.context));
assert.equal(entry.headword,'Public transport schedule / timetable');
assert.equal(entry.preferred_variant.token_sequence,'move_public + media_text + time + punct_question');
assert.deepEqual(results(current,'timetable').headings,['Public transport schedule / timetable']);
assert.equal(vm.runInContext("D.find(e=>e.dictionary_entry_id==='pcd-v01-0065').preferred_variant.token_sequence",current.context),'move_public + time + punct_question');
''')

    def test_generated_viewer_and_manifest_hash_reproducible(self):
        entries=json.loads((PACKAGE/'dictionary.json').read_text())['entries']
        generated=make_dictionary_viewer(entries)
        self.assertEqual(generated,make_dictionary_viewer(entries))
        self.assertEqual(generated,self.html)
        manifest=json.loads((PACKAGE/'manifest.json').read_text())
        self.assertEqual(manifest['artifact_sha256']['review/index.html'],hashlib.sha256(self.html.encode()).hexdigest())
        self.assertIn('do not establish semantic equivalence or complete QA',self.html)

    def test_protected_data_qa_snapshots_and_exports_unchanged(self):
        from tools.research.communication_context_clarification import receipt_refs, verify_sequence, encode
        relbase = 'docs/research/composition-dictionary-baseline-v0.1/'
        old = json.loads(subprocess.check_output(['git','show',REVISION+':'+relbase+'manifest.json'],cwd=ROOT))
        new = json.loads((PACKAGE/'manifest.json').read_bytes())
        dictionary = json.loads((PACKAGE/'dictionary.json').read_bytes())
        refs = receipt_refs(new)
        original, _, _ = verify_sequence((PACKAGE/'dictionary.json').read_bytes(),
                                         [json.loads((PACKAGE/r['path']).read_bytes()) for r in refs], ROOT)
        frozen_dictionary = subprocess.check_output(['git','show',REVISION+':'+relbase+'dictionary.json'],cwd=ROOT)
        self.assertEqual(encode(original), frozen_dictionary)
        # Only explicitly verified projections differ from the historical snapshot.
        active = {'dictionary.json','variants.json','lineage.json','validation.json',
                  'render-manifest.json','review/data.json','review/index.html','README.md','manifest.json'}
        paths = subprocess.check_output(['git','ls-tree','-r','--name-only',REVISION,'--',relbase],cwd=ROOT,text=True).splitlines()
        for rel in paths:
            if rel.removeprefix(relbase) in active:
                continue
            with self.subTest(path=rel):
                self.assertEqual((ROOT/rel).read_bytes(),subprocess.check_output(['git','show',REVISION+':'+rel],cwd=ROOT))
        self.assertEqual((PACKAGE/'review/data.json').read_bytes(), encode(dictionary))
        for filename, key, records in (
                ('variants.json','variants',[v for e in dictionary['entries'] for v in e['variants']]),
                ('lineage.json','records',[e['lineage'] for e in dictionary['entries']])):
            data = json.loads((PACKAGE/filename).read_bytes())
            self.assertEqual(data.pop(key), records)
            frozen = json.loads(subprocess.check_output(['git','show',REVISION+':'+relbase+filename],cwd=ROOT))
            frozen.pop(key)
            self.assertEqual(data, frozen)
        validation = json.loads((PACKAGE/'validation.json').read_bytes())
        self.assertEqual(validation['valid_message_count'], 72)
        self.assertEqual(validation['rendered_canonically'], 72)
        self.assertEqual(validation['failures'], [])
        frozen_renders = json.loads(subprocess.check_output(['git','show',REVISION+':'+relbase+'render-manifest.json'],cwd=ROOT))['renders']
        renders = json.loads((PACKAGE/'render-manifest.json').read_bytes())['renders']
        self.assertEqual(renders[:69], [r for r in frozen_renders if r['dictionary_entry_id'] != 'pcd-v01-0025'])
        self.assertEqual([r['variant_id'] for r in renders[69:]], ['pcd-v01-0028-preferred-feet','pcd-v01-0028-contextual-here','pcd-v01-0066-preferred'])
        frozen_readme = subprocess.check_output(['git','show',REVISION+':'+relbase+'README.md'],cwd=ROOT,text=True)
        expected_readme = frozen_readme.replace('All 70 preferred/accepted', 'All 72 preferred/accepted').replace('Two note portions remain in `creator-notes-follow-up.json`: the exact scope/token for a proposed UP/AHEAD prohibition and the exact order for a separate schedule/timetable composition. Neither is presented as an accepted Message. The arrival-time entry remains accepted.', 'The original two-note follow-up report remains in `creator-notes-follow-up.json` as history. Its timetable is now applied as the separate `pcd-v01-0066` entry; arrival-time entry `pcd-v01-0065` is unchanged. The proposed UP/AHEAD prohibition is not applied by this pass.')
        self.assertEqual((PACKAGE/'README.md').read_text(), expected_readme)
        counts = dict(old['counts'])
        counts.update(dictionary_entries=65, preferred_messages=65, contextual_variants=5, entries_with_multiple_variants=4, entries_with_context_warnings=13, entries_with_known_ambiguity=39, render_count=72)
        self.assertEqual(new['counts'], counts)
        self.assertEqual(set(new['artifact_sha256']), set(old['artifact_sha256']) | {r['path'] for r in refs} |
                         {'renders/pcd-v01-0028-preferred-feet.svg','renders/pcd-v01-0028-contextual-here.svg','renders/pcd-v01-0066-preferred.svg'})
        for path, digest in new['artifact_sha256'].items():
            self.assertEqual(hashlib.sha256((PACKAGE/path).read_bytes()).hexdigest(), digest)
        normalized = dict(new)
        normalized.pop('context_clarifications')
        normalized['artifact_sha256'] = old['artifact_sha256']
        normalized['counts'] = old['counts']
        self.assertEqual(normalized, old)


if __name__=='__main__':
    unittest.main()
