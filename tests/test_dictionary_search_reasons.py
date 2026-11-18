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
        harness += 'const current=viewer('+json.dumps(self.script)+');const original=viewer('+json.dumps(self.old_script)+');\n'+body
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
assert.deepEqual(entry.aliases,[]);assert.equal(entry.semantic_neighbourhood,'Person moving on foot');
assert.equal(current.elements['search-limit'].hidden,false);
''')

    def test_title_tokens_and_multiple_field_groups(self):
        self.run_js('''
let match=plain(vm.runInContext("dictionaryMatch(D.find(e=>e.dictionary_entry_id==='pcd-v01-0028'),'pedestrian movement')",current.context));
assert.deepEqual(match.groups,['title_aliases']);assert.equal(match.reason,'Match in title / aliases.');
assert.ok(results(current,'pedestrian movement').html.includes(match.reason));
match=plain(vm.runInContext("dictionaryMatch(D.find(e=>e.dictionary_entry_id==='pcd-v01-0006'),'comm_sound')",current.context));
assert.deepEqual(match.groups,['token_sequences']);assert.ok(match.reason.includes('token sequences / IDs'));
assert.ok(results(current,'comm_sound').headings.includes('Less noise, please.'));
match=plain(vm.runInContext("dictionaryMatch(D.find(e=>e.dictionary_entry_id==='pcd-v01-0006'),'noise')",current.context));
assert.deepEqual(match.groups,['title_aliases','related']);assert.equal(match.reason,'Match in title / aliases; related materials.');
match=plain(vm.runInContext("(()=>{const e=JSON.parse(JSON.stringify(D.find(e=>e.dictionary_entry_id==='pcd-v01-0006')));e.aliases=['comm_sound'];return dictionaryMatch(e,'comm_sound')})()",current.context));
assert.deepEqual(match.groups,['title_aliases','token_sequences']);
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

    def test_generated_viewer_and_manifest_hash_reproducible(self):
        entries=json.loads((PACKAGE/'dictionary.json').read_text())['entries']
        generated=make_dictionary_viewer(entries)
        self.assertEqual(generated,make_dictionary_viewer(entries))
        self.assertEqual(generated,self.html)
        manifest=json.loads((PACKAGE/'manifest.json').read_text())
        self.assertEqual(manifest['artifact_sha256']['review/index.html'],hashlib.sha256(self.html.encode()).hexdigest())
        self.assertIn('do not establish semantic equivalence or complete QA',self.html)

    def test_protected_data_qa_snapshots_and_exports_unchanged(self):
        # Historical source snapshot is an independent oracle for source preservation.
        relbase='docs/research/composition-dictionary-baseline-v0.1/'
        paths=subprocess.check_output(['git','ls-tree','-r','--name-only',REVISION,'--',relbase],cwd=ROOT,text=True).splitlines()
        for rel in paths:
            if rel in (relbase+'review/index.html',relbase+'manifest.json'):continue
            with self.subTest(path=rel):
                self.assertEqual((ROOT/rel).read_bytes(),subprocess.check_output(['git','show',REVISION+':'+rel],cwd=ROOT))
        old=json.loads(subprocess.check_output(['git','show',REVISION+':'+relbase+'manifest.json'],cwd=ROOT))
        new=json.loads((PACKAGE/'manifest.json').read_text())
        old['artifact_sha256']['review/index.html']=new['artifact_sha256']['review/index.html']
        self.assertEqual(old,new)


if __name__=='__main__':
    unittest.main()
