import copy
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
import xml.etree.ElementTree as ET

from tools.replica_package import ROOT, PACKAGE, PackageError, build, verify, encode
from pictiq_renderer.registry import Registry
from pictiq_renderer.svg_renderer import render_svg

ENTRY = 'pcd-v01-0006'
VARIANT = 'pcd-v01-0006-preferred'
REVISION = '34366fc7396f49e40d5235b3a3cc897550b8ea92'
SAMPLE = ROOT / 'docs/research/replica-package-v0.1/examples/less-noise'


class ReplicaPackageTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(); self.addCleanup(self.temp.cleanup)
        self.tempdir = Path(self.temp.name)

    def fixture(self):
        root = self.tempdir / 'project'
        files = [PACKAGE+'/'+f for f in ('dictionary.json','manifest.json','creator-review-export.json','final-creator-qa-addendum-v0.2.json')]
        files += [PACKAGE + '/' + f for f in ('applied-decisions/pcd-v01-0002-context.json',
                  'applied-decisions/pcd-v01-0006-context.json',
                  'creator-final-qa-2026-11-19/creator-export.json', 'review/final-creator-qa-v0.2.json')]
        files += ['tools/research/medical_context_clarification.py', 'tools/research/communication_context_clarification.py']
        files += ['docs/research/composition-library-baseline-v0.1/accepted-corpus.json',
                  'lexicon/icon-index.json','lexicon/compatibility.json','entities/entity-index.json','notation/numeric/index.json',
                  'profiles/standalone-core-v0.1.json','profiles/embodied-core-v0.1.json',
                  'tools/replica_package.py','tools/validate_message_schema.py','icons/svg/comm_sound.svg','icons/svg/qty_minus.svg']
        files += [str(p.relative_to(ROOT)) for folder,glob in [('packs','*.json'),('pictiq_renderer','*.py')] for p in (ROOT/folder).glob(glob)]
        for rel in files:
            path=root/rel; path.parent.mkdir(parents=True,exist_ok=True); shutil.copyfile(ROOT/rel,path)
        return root

    def alter_message(self, root, change):
        path=root/PACKAGE/'dictionary.json';data=json.loads(path.read_bytes())
        variant=next(v for e in data['entries'] if e['dictionary_entry_id']==ENTRY for v in e['variants'] if v['variant_id']==VARIANT)
        change(variant['message']);path.write_bytes(encode(data));digest=hashlib.sha256(path.read_bytes()).hexdigest()
        path=root/PACKAGE/'manifest.json';m=json.loads(path.read_bytes());m['artifact_sha256']['dictionary.json']=digest
        # This synthetic Message fixture declares its own direct addendum
        # binding, rather than claiming the real description applications.
        m.pop('context_clarification', None);m.pop('context_clarifications', None);path.write_bytes(encode(m))
        path=root/PACKAGE/'final-creator-qa-addendum-v0.2.json';m=json.loads(path.read_bytes());m['source_dictionary_baseline']['dictionary_json_sha256']=digest;path.write_bytes(encode(m))
        return variant['message']

    def built(self, name='package', root=ROOT):
        out=self.tempdir/name;build(ENTRY,VARIANT,out,root,REVISION);return out

    def test_reproducibility_exact_variant_provenance_and_portability(self):
        first=self.built('a');second=self.built('b')
        self.assertEqual({p.name:p.read_bytes() for p in first.iterdir()},{p.name:p.read_bytes() for p in second.iterdir()})
        data=json.loads((ROOT/PACKAGE/'dictionary.json').read_bytes())
        entry=next(e for e in data['entries'] if e['dictionary_entry_id']==ENTRY)
        variant=next(v for v in entry['variants'] if v['variant_id']==VARIANT)
        self.assertEqual(json.loads((first/'message.json').read_bytes()),variant['message'])
        manifest=json.loads((first/'manifest.json').read_bytes())
        self.assertEqual(manifest['source']['message_selector'],'/entries/5/variants/0/message')
        self.assertEqual(manifest['creator_decision']['source']['selector'],'/records/5')
        self.assertEqual(manifest['creator_decision']['record']['creator_decision'],'KEEP_IN_DICTIONARY')
        self.assertEqual(manifest['corpus_lineage']['record_id'],'clc-v01-0008-r1')
        self.assertIn('AWAITING FINAL VISUAL QA',manifest['source_qa']['status'])
        self.assertEqual(manifest['review_status'],{'new_render':'NOT_REVIEWED','final_placement':'NOT_REVIEWED'})
        svg=ET.fromstring((first/'render.svg').read_bytes())
        self.assertEqual([e.attrib['data-id'] for e in svg.iter() if 'data-id' in e.attrib],['comm_sound','qty_minus'])
        self.assertFalse(any(k.endswith('href') and not v.startswith('#') for e in svg.iter() for k,v in e.attrib.items()))
        moved=self.tempdir/'relocated';shutil.move(str(first),moved)
        self.assertTrue(verify(moved)['ok'])
        self.assertEqual({p.name for p in moved.iterdir()},{'manifest.json','message.json','render.svg'})

    def test_corruption_and_rehashed_inconsistent_svg_rejected(self):
        out=self.built();before=(out/'render.svg').read_bytes()
        (out/'render.svg').write_bytes(before+b'corrupted')
        with self.assertRaisesRegex(PackageError,'Integrity mismatch'):verify(out)
        message=json.loads((out/'message.json').read_bytes());message['frames'][0]['tokens'].reverse()
        wrong,_=render_svg(message,Registry());(out/'render.svg').write_text(wrong)
        manifest=json.loads((out/'manifest.json').read_bytes());manifest['files']['render']['sha256']=hashlib.sha256((out/'render.svg').read_bytes()).hexdigest()
        (out/'manifest.json').write_bytes(encode(manifest))
        with self.assertRaisesRegex(PackageError,'canonical Renderer'):verify(out)

    def test_rehashed_message_and_upgraded_review_status_rejected(self):
        out=self.built();message=json.loads((out/'message.json').read_bytes());message['frames'][0]['tokens'].reverse()
        (out/'message.json').write_bytes(encode(message));manifest=json.loads((out/'manifest.json').read_bytes())
        manifest['files']['message']['sha256']=hashlib.sha256((out/'message.json').read_bytes()).hexdigest();(out/'manifest.json').write_bytes(encode(manifest))
        with self.assertRaisesRegex(PackageError,'message.json differs'):verify(out)
        out=self.built('review-status');manifest=json.loads((out/'manifest.json').read_bytes());manifest['review_status']['new_render']='APPROVED';(out/'manifest.json').write_bytes(encode(manifest))
        with self.assertRaisesRegex(PackageError,'review status'):verify(out)

    def test_unknown_variant_invalid_messages_and_no_overwrite(self):
        output=self.tempdir/'unknown'
        with self.assertRaisesRegex(PackageError,'found 0'):build(ENTRY,'not-a-variant',output,revision=REVISION)
        self.assertFalse(output.exists())
        root=self.fixture();self.alter_message(root,lambda m:m['frames'][0]['tokens'].append({'type':'icon','id':'unknown_k06'}))
        with self.assertRaisesRegex(PackageError,'Invalid Message'):build(ENTRY,VARIANT,self.tempdir/'bad',root,REVISION)
        self.assertFalse((self.tempdir/'bad').exists())
        self.alter_message(root,lambda m:m.update(frames=[]))
        with self.assertRaisesRegex(PackageError,'Invalid Message'):build(ENTRY,VARIANT,self.tempdir/'bad-shape',root,REVISION)
        self.assertFalse((self.tempdir/'bad-shape').exists())
        valid=self.built('valid');before={p.name:p.read_bytes() for p in valid.iterdir()}
        with self.assertRaisesRegex(PackageError,'refusing to overwrite'):build(ENTRY,VARIANT,valid,revision=REVISION)
        self.assertEqual(before,{p.name:p.read_bytes() for p in valid.iterdir()})
        empty=self.tempdir/'empty';empty.mkdir()
        with self.assertRaisesRegex(PackageError,'refusing to overwrite'):build(ENTRY,VARIANT,empty,revision=REVISION)

    def test_frames_params_profile_and_contexts_preserved(self):
        root=self.fixture()
        def change(m):
            m['frames'][0]['tokens'][0]['params']={'color':'#123456'}
            m['frames'].append({'tokens':[{'type':'icon','id':'qty_minus'},{'type':'icon','id':'comm_sound'}]})
            m['contexts']=['universal-core','road-wayfinding-v0.1']
        original=self.alter_message(root,change);out=self.built(root=root)
        self.assertEqual(json.loads((out/'message.json').read_bytes()),original)
        self.assertEqual([e.attrib['data-id'] for e in ET.fromstring((out/'render.svg').read_bytes()).iter() if 'data-id' in e.attrib],['comm_sound','qty_minus','qty_minus','comm_sound'])
        self.assertTrue(verify(out,root)['ok'])

    def test_actual_changed_or_unavailable_input_versions(self):
        root=self.fixture();out=self.built(root=root)
        asset=root/'icons/svg/comm_sound.svg';asset.write_text(asset.read_text().replace('</svg>','<!-- local bytes -->\n</svg>'))
        with self.assertRaisesRegex(PackageError,'input version unavailable or changed'):verify(out,root)
        new=self.built('modified-asset',root);manifest=json.loads((new/'manifest.json').read_bytes())
        bound=next(a for a in manifest['canonical_assets'] if a['original_id_or_value']=='comm_sound')
        self.assertEqual(bound['sha256'],hashlib.sha256(asset.read_bytes()).hexdigest())
        self.assertTrue(verify(new,root)['ok'])
        asset.unlink()
        with self.assertRaisesRegex(PackageError,'input version unavailable or changed'):verify(new,root)

    def test_sample_and_cli(self):
        # K06 remains bound to its historical input bytes; never rebind it to
        # the active Dictionary revision or silently refresh its manifest.
        with self.assertRaisesRegex(PackageError, 'input version unavailable or changed'):
            verify(SAMPLE)
        result=subprocess.run([sys.executable,str(ROOT/'tools/replica_package.py'),'verify',str(SAMPLE)],cwd=self.tempdir,text=True,capture_output=True)
        self.assertEqual(result.returncode,1,result.stdout+result.stderr)
        self.assertIn('input version unavailable or changed', result.stdout)
        bad=subprocess.run([sys.executable,str(ROOT/'tools/replica_package.py'),'build','--entry-id',ENTRY,'--variant-id','unknown','--output',str(self.tempdir/'cli-bad')],cwd=self.tempdir,text=True,capture_output=True)
        self.assertEqual(bad.returncode,1);self.assertFalse(json.loads(bad.stdout)['ok'])
        self.assertFalse((self.tempdir/'cli-bad').exists())

    def test_source_bytes_unchanged_after_builds_and_verification(self):
        original_paths=[]
        for folder in [PACKAGE,'docs/research/composition-library-baseline-v0.1','lexicon','entities','icons/svg','profiles','packs','notation/numeric']:
            original_paths.extend(p for p in (ROOT/folder).rglob('*') if p.is_file())
        before={p:hashlib.sha256(p.read_bytes()).hexdigest() for p in original_paths}
        out=self.built();verify(out)
        self.assertEqual(before,{p:hashlib.sha256(p.read_bytes()).hexdigest() for p in original_paths})


if __name__=='__main__':
    unittest.main()
