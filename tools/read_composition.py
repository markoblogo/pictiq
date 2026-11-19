#!/usr/bin/env python3
"""Read current Dictionary/Corpus v0.1 records without applying or normalizing them."""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DICTIONARY = 'docs/research/composition-dictionary-baseline-v0.1'
CORPUS = 'docs/research/composition-library-baseline-v0.1'
ADDENDUM = 'final-creator-qa-addendum-v0.2.json'  # Active source, never filename-ranked.
sys.path.insert(0, str(ROOT))


class ReadError(Exception):
    pass


class Reader:
    def __init__(self, root: Path):
        self.root = root.resolve()
        self.files = {}
        self.diagnostics = []

    def path(self, base: Path, relative: str) -> Path:
        path = (base / relative).resolve()
        if not path.is_relative_to(self.root):
            raise ReadError(f'Path outside repository: {relative}')
        return path

    def file(self, path: Path):
        relative = str(path.relative_to(self.root))
        if not path.is_file():
            return {'path': relative, 'exists': False, 'sha256': None}
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        self.files[relative] = digest
        return {'path': relative, 'exists': True, 'sha256': digest}

    def load(self, path: Path):
        ref = self.file(path)
        if not ref['exists']:
            raise ReadError(f'Missing data source: {ref["path"]}')
        return json.loads(path.read_bytes())

    def note(self, code, message, error=False):
        self.diagnostics.append({'code': code, 'message': message, 'level': 'error' if error else 'warning'})

    def one(self, rows, field, value, required=True):
        hits = [(i, row) for i, row in enumerate(rows) if row.get(field) == value]
        if len(hits) > 1:
            raise ReadError(f'Ambiguous {field}: {value}')
        if not hits:
            if required:
                raise ReadError(f'Unknown {field}: {value}; no fallback to another source')
            return None
        return hits[0]

    def verify(self, path, expected, label):
        actual = self.file(path)
        if not expected or actual['sha256'] != expected:
            self.note('BINDING_MISMATCH', label, error=True)
            return False
        return True

    def ref(self, path, selector):
        return {**self.file(path), 'selector': selector}

    def renders(self, value, base, selector=''):
        out = []
        if isinstance(value, dict):
            for key, child in value.items():
                where = selector + '/' + key
                if key in ('render', 'preview_render') and isinstance(child, str):
                    ref = self.file(self.path(base, child))
                    out.append({**ref, 'record_selector': where})
                    if not ref['exists']:
                        self.note('MISSING_RENDER', ref['path'])
                else:
                    out.extend(self.renders(child, base, where))
        elif isinstance(value, list):
            for i, child in enumerate(value):
                out.extend(self.renders(child, base, selector + '/' + str(i)))
        return out

    def assets(self, value):
        icons = {e['id']: e for e in self.load(self.root / 'lexicon/icon-index.json')['icons']}
        entities = {e['id']: e for e in self.load(self.root / 'entities/entity-index.json')['symbols']}
        numbers = {str(e['value']): e for e in self.load(self.root / 'notation/numeric/index.json')['implemented_numbers']}
        out = []

        def walk(node, selector=''):
            if isinstance(node, dict):
                if isinstance(node.get('frames'), list):
                    for fi, frame in enumerate(node['frames']):
                        for ti, token in enumerate(frame.get('tokens', [])):
                            kind = token.get('type'); identity = token.get('id') if kind != 'number' else token.get('value')
                            relative = None
                            if kind == 'icon' and identity in icons:
                                relative = f'icons/svg/{identity}.svg'
                            elif kind == 'entity' and identity in entities:
                                relative = entities[identity]['icon_path']
                            elif kind == 'number' and str(identity) in numbers:
                                relative = numbers[str(identity)]['svg']
                            registered = relative is not None
                            ref = self.file(self.path(self.root, relative)) if registered else {'path': None, 'exists': False, 'sha256': None}
                            out.append({'message_selector': selector, 'frame': fi, 'token': ti,
                                        'type': kind, 'original_id_or_value': identity,
                                        'registered': registered, 'asset': ref, 'substitution': None})
                            if not registered:
                                self.note('UNRESOLVED_CANONICAL_TOKEN', f'{selector}/frames/{fi}/tokens/{ti}: {identity}')
                            elif not ref['exists']:
                                self.note('MISSING_CANONICAL_ASSET', ref['path'])
                    # Messages are left intact; never invoke Renderer normalization.
                    return
                for key, child in node.items():
                    walk(child, selector + '/' + key)
            elif isinstance(node, list):
                for i, child in enumerate(node):
                    walk(child, selector + '/' + str(i))
        walk(value)
        return out

    def historical_render(self, record):
        link = record.get('source_harvest')
        if not link:
            return []
        # The declared harvest ID is not its directory name; support this explicit v0.1 binding.
        if link['harvest_id'] != 'pictiq-composition-library-historical-harvest-v0.1':
            self.note('HARVEST_LINK_MISMATCH', 'Unsupported declared harvest ID', error=True)
            return []
        base = self.root / 'docs/research/composition-library-historical-harvest-v0.1'
        manifest = self.load(base / 'manifest.json')
        if manifest['harvest_id'] != link['harvest_id'] or manifest['snapshot_commit'] != link['snapshot_commit']:
            self.note('HARVEST_LINK_MISMATCH', record['corpus_record_id'], error=True)
            return []
        _, registered = self.one(manifest['records'], 'composition_id', link['composition_id'])
        if registered['path'] != link['record_path']:
            self.note('HARVEST_LINK_MISMATCH', 'record_path disagrees with harvest manifest', error=True)
            return []
        source = self.load(self.path(base, registered['path']))
        if source['composition_id'] != link['composition_id'] or source['pictiq_message'] != record['historical_message']:
            self.note('HISTORICAL_MESSAGE_MISMATCH', 'Historical render is not linked to the exact historical Message', error=True)
            return []
        review_path = self.path(base, manifest['review_dataset_path'])
        review = self.load(review_path)
        i, row = self.one(review, 'composition_id', link['composition_id'])
        if row['pictiq_sequence_human_readable'] != [record['historical_sequence']]:
            self.note('HISTORICAL_RENDER_LINK_MISMATCH', record['corpus_record_id'], error=True)
            return []
        ref = self.file(self.path(base, row['visual_render']))
        if not ref['exists']:
            self.note('MISSING_RENDER', ref['path'])
        return [{**ref, 'role': 'SAVED_HISTORICAL_RENDER_NOT_CURRENT_REGISTRY_VALIDATION',
                 'declared_render_status': row['render_status'], 'link': self.ref(review_path, f'/{i}') }]

    def read(self, source, record_id):
        if source not in ('dictionary', 'corpus'):
            raise ReadError(f'Unsupported source: {source}; expected dictionary or corpus')
        db = self.root / DICTIONARY
        dp = db / 'dictionary.json'; dm = self.load(db / 'manifest.json'); dictionary = self.load(dp)
        cp = self.path(db, dm['source_corpus_baseline']['path'])
        cb = cp.parent; corpus = self.load(cp); cm = self.load(cb / 'manifest.json')
        primary = dictionary if source == 'dictionary' else corpus
        key, group, primary_path = ('dictionary_entry_id', 'entries', dp) if source == 'dictionary' else ('corpus_record_id', 'records', cp)
        index, record = self.one(primary[group], key, record_id)
        baseline_ref = self.ref(primary_path, f'/{group}/{index}')
        self.selected_record = record
        self.selected_provenance = baseline_ref
        source_bound = all([
            self.verify(dp, dm['artifact_sha256']['dictionary.json'], 'Dictionary manifest → dictionary.json'),
            self.verify(cp, dm['source_corpus_baseline']['sha256'], 'Dictionary manifest → Corpus'),
            self.verify(cp, cm['artifact_sha256']['accepted-corpus.json'], 'Corpus manifest → accepted-corpus.json'),
        ])
        if dictionary['source_corpus_baseline_version'] != corpus['baseline_version'] or dm['source_corpus_baseline']['version'] != corpus['baseline_version']:
            self.note('BINDING_MISMATCH', 'Corpus baseline version mismatch', error=True)
        add_path = db / ADDENDUM; addendum = self.load(add_path)
        binding = addendum['source_dictionary_baseline']
        applied = []
        bound_dictionary_sha = self.file(dp)['sha256']
        if 'context_clarification' in dm or 'context_clarifications' in dm:
            from tools.research.communication_context_clarification import receipt_refs, verify_sequence, SOURCE, QA_DATA
            try:
                applications = receipt_refs(dm)
                receipts = [self.load(db / ref['path']) for ref in applications]
                checks = [self.verify(db / ref['path'], ref['sha256'], 'manifest → context clarification')
                          for ref in applications]
                if not all(checks):
                    raise ValueError('Context clarification receipt hash mismatch')
                _, _, raw_decisions = verify_sequence(dp.read_bytes(), receipts, self.root)
            except (ReadError, ValueError, KeyError, TypeError, IndexError, OSError) as exc:
                self.note('CONTEXT_CLARIFICATION_MISMATCH', str(exc), error=True)
            else:
                bound_dictionary_sha = receipts[0]['dictionary_before_sha256']
                self.file(self.root / QA_DATA)
                for ref, receipt, raw_decision in zip(applications, receipts, raw_decisions):
                    source_ref = self.ref(self.root / SOURCE, receipt['source_decision']['selector'])
                    if (source == 'dictionary' and record_id == receipt['dictionary_entry_id']) or (
                            source == 'corpus' and record_id == raw_decision['corpus_record_id']):
                        applied.append({'action': raw_decision['decision'], 'application_status': 'APPLIED',
                                        'scope': receipt['scope'], 'link_verified': True,
                                        'source_decision': raw_decision, 'source_provenance': source_ref,
                                        'provenance': self.ref(db / ref['path'], ''), 'application': receipt})
        bound = (source_bound and binding['version'] == dictionary['dictionary_version'] == dm['dictionary_version'] and
                 binding['source_snapshot'] == dictionary['source_snapshot'] == dm['creator_review_export']['source_snapshot'] and
                 binding['dictionary_json_sha256'] == bound_dictionary_sha)
        if not bound:
            for application in applied:
                application['link_verified'] = False
            self.note('ADDENDUM_BASELINE_MISMATCH', 'Active creator decisions cannot be resolved against this baseline', error=True)
        related = []
        if source == 'dictionary':
            refs = record['corpus_refs']
            if record['lineage']['dictionary_entry_id'] != record_id or record['lineage']['corpus_record_id'] not in refs:
                self.note('LINEAGE_MISMATCH', 'Entry lineage disagrees with corpus_refs', error=True)
            for cid in refs:
                ci, cr = self.one(corpus['records'], 'corpus_record_id', cid)
                related.append({'record': cr, 'provenance': self.ref(cp, f'/records/{ci}')})
                if cr.get('dictionary_entry_id') not in (None, record_id):
                    self.note('LINEAGE_MISMATCH', f'Corpus backlink differs: {cid}', error=True)
            dictionary_entries = [record]
        else:
            refs = [record_id]
            dictionary_entries = [e for e in dictionary['entries'] if record_id in e['corpus_refs']]
            if record.get('dictionary_entry_id') and not dictionary_entries:
                self.note('LINEAGE_MISMATCH', 'Corpus Dictionary backlink has no matching forward reference', error=True)
            if len(dictionary_entries) > 1:
                self.note('AMBIGUOUS_LINEAGE', 'Multiple Dictionary entries reference this Corpus record', error=True)
            for e in dictionary_entries:
                if record.get('dictionary_entry_id') not in (None, e['dictionary_entry_id']) or e['lineage']['corpus_record_id'] != record_id:
                    self.note('LINEAGE_MISMATCH', 'Corpus and Dictionary backlinks disagree', error=True)
        ids = [e['dictionary_entry_id'] for e in dictionary_entries]
        decisions = []
        for i, decision in enumerate(addendum['decisions']):
            if decision['dictionary_entry_id'] not in ids and decision['corpus_record_id'] not in refs:
                continue
            hits = [e for e in dictionary['entries'] if e['dictionary_entry_id'] == decision['dictionary_entry_id']]
            resolved = (bound and not any(d['level'] == 'error' for d in self.diagnostics) and len(hits) == 1 and decision['dictionary_entry_id'] in ids and
                        decision['corpus_record_id'] in refs and
                        hits[0]['corpus_refs'] == [decision['corpus_record_id']] and
                        hits[0]['lineage']['corpus_record_id'] == decision['corpus_record_id'])
            duplicates = [d for d in addendum['decisions'] if d['dictionary_entry_id'] == decision['dictionary_entry_id'] or d['corpus_record_id'] == decision['corpus_record_id']]
            if len(duplicates) != 1:
                resolved = False
            if 'current_baseline' in decision and hits:
                if any(decision['current_baseline'][key] != value for key, value in {
                    'message': hits[0]['preferred_variant']['message'],
                    'headword': hits[0]['headword'],
                    'token_sequence': hits[0]['preferred_variant']['token_sequence']}.items()):
                    resolved = False
            if not resolved:
                self.note('DECISION_LINK_UNRESOLVED', f'/decisions/{i}: incompatible or ambiguous linkage', error=True)
            pending = 'PENDING' in addendum['status'] or 'PENDING' in decision['application_status']
            if pending:
                self.note('PENDING_CREATOR_DECISION', f'{decision["decision"]}: not applied; baseline retained')
            decisions.append({'action': decision['decision'], 'application_status': decision['application_status'],
                              'source_authority': addendum['provenance'], 'source_date': addendum['date'],
                              'addendum_status': addendum['status'], 'link_verified': resolved,
                              'baseline_mutated_by_reader': False, 'raw_decision': decision,
                              'provenance': self.ref(add_path, f'/decisions/{i}')})
        if source == 'dictionary':
            self.note('FINAL_QA_OUTSTANDING', dm['status'] + '; absence of a pending action does not complete QA')
        if source == 'corpus' and record.get('compatibility', {}).get('message_validity') == 'HISTORICAL':
            self.note('HISTORICAL_ONLY', 'Saved Message/render do not imply current canonical token availability')
        renders = self.renders(record, primary_path.parent)
        if source == 'corpus' and record.get('historical_message') and not record.get('render'):
            renders.extend(self.historical_render(record))
        if not renders:
            self.note('NO_SAVED_RENDER_LINK', 'No linked render available; nothing generated or substituted')
        assets = self.assets({'baseline_record': record, 'linked_corpus_records': related,
                              'subsequent_creator_decisions': decisions})
        for decision in decisions:
            renders.extend(self.renders(decision['raw_decision'], db, decision['provenance']['selector']))
        # A reader reports contradictions, never repairs the stored Message/string.
        def check_sequences(node, selector=''):
            if isinstance(node, dict):
                message = node.get('message'); sequence = node.get('token_sequence')
                if message and isinstance(sequence, str):
                    actual = ' + '.join(str(t['id']) for f in message['frames'] for t in f['tokens'] if t.get('type') == 'icon')
                    if actual != sequence:
                        self.note('MESSAGE_SEQUENCE_MISMATCH', selector, error=True)
                for k, v in node.items(): check_sequences(v, selector + '/' + k)
            elif isinstance(node, list):
                for i, v in enumerate(node): check_sequences(v, selector + '/' + str(i))
        check_sequences(record); check_sequences(decisions)
        if any(d['level'] == 'error' for d in self.diagnostics):
            for application in applied:
                application['link_verified'] = False
        return {'ok': not any(d['level'] == 'error' for d in self.diagnostics),
                'source': source, 'id': record_id, 'baseline_record': record,
                'record_statuses': {k: record[k] for k in ('creator_review', 'reconciliation_disposition', 'dictionary_eligibility', 'compatibility', 'render_status') if k in record},
                'package': {'source_metadata': {k: v for k, v in primary.items() if k not in ('entries', 'records')},
                            'version': primary.get('dictionary_version', primary.get('baseline_version')),
                            'declared_status': primary['status'], 'manifest_status': (dm if source == 'dictionary' else cm)['status'],
                            'dictionary_qa_status': dm['status'], 'no_new_semantic_approval_inferred': True},
                'linked_corpus_records': related, 'subsequent_creator_decisions': decisions,
                'applied_creator_decisions': applied,
                'renders': renders, 'canonical_assets': assets, 'baseline_provenance': baseline_ref,
                'files_sha256': self.files, 'diagnostics': self.diagnostics}


def read_composition(source, record_id, root=ROOT):
    reader = Reader(Path(root))
    try:
        return reader.read(source, record_id)
    except (ReadError, OSError, ValueError, KeyError, TypeError) as exc:
        reader.note('READ_FAILED', str(exc), error=True)
        result = {'ok': False, 'source': source, 'id': record_id,
                  'files_sha256': reader.files, 'diagnostics': reader.diagnostics}
        if hasattr(reader, 'selected_record'):
            result.update(baseline_record=reader.selected_record, baseline_provenance=reader.selected_provenance)
        return result


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', required=True)
    parser.add_argument('--id', required=True)
    args = parser.parse_args(argv)
    result = read_composition(args.source, args.id)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result['ok'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
