"""S01.15: remove one active projection, preserving its exact history and inverse."""
from __future__ import annotations

import copy
import json

from tools.research.medical_context_clarification import PACKAGE, SOURCE, SOURCE_SHA, encode, sha, source_decision
from tools.research.pedestrian_preferred_application import CORPUS, CORPUS_SHA

RECEIPT = 'applied-decisions/pcd-v01-0025-corpus-only.json'
BEFORE_SHA = 'fe50cf5f62c908cb05abc2ba57fe28132475599400dc061203c35fb46773873a'
REVISION = 'c21b0d9f3ad9367dd2aa4419e2573881a9619bda'
ENTRY = 'pcd-v01-0025'
CORPUS_ID = 'clh-v01-0044'
ADDENDUM = PACKAGE + '/final-creator-qa-addendum-v0.2.json'
ADDENDUM_SHA = '8c5cfda80ee90dea0e185d142249a03e6be83b7ec40f1523f07e74dcd5ed0b51'


def apply(dictionary, root):
    export, _ = source_decision(root)
    decision = export['records'][5]
    if (decision['dictionary_entry_id'] != ENTRY or decision['corpus_record_id'] != CORPUS_ID
            or decision['decision'] != 'MOVE_TO_CORPUS_ONLY' or sha(encode(dictionary)) != BEFORE_SHA):
        raise ValueError('Corpus-only application: source decision or predecessor mismatch')
    raw_addendum = (root / ADDENDUM).read_bytes()
    raw_corpus = (root / CORPUS).read_bytes()
    if sha(raw_addendum) != ADDENDUM_SHA or sha(raw_corpus) != CORPUS_SHA:
        raise ValueError('Corpus-only application: addendum or Corpus source hash mismatch')
    addendum = json.loads(raw_addendum)
    recorded = addendum['decisions'][0]
    if (recorded['dictionary_entry_id'] != ENTRY or recorded['corpus_record_id'] != CORPUS_ID
            or recorded['decision'] != decision['decision'] or recorded['replacement'] is not None):
        raise ValueError('Corpus-only application: recorded decision mismatch')
    hits = [(i, e) for i, e in enumerate(dictionary['entries']) if e['dictionary_entry_id'] == ENTRY]
    corpus_hits = [(i, r) for i, r in enumerate(json.loads(raw_corpus)['records']) if r['corpus_record_id'] == CORPUS_ID]
    if len(hits) != 1 or len(corpus_hits) != 1:
        raise ValueError('Corpus-only application: missing or ambiguous entry/Corpus record')
    index, entry = hits[0]
    ci, record = corpus_hits[0]
    if (entry['corpus_refs'] != [CORPUS_ID] or entry['lineage']['corpus_record_id'] != CORPUS_ID
            or entry['preferred_variant']['message'] != record['current_message']
            or entry['lineage']['source_message'] != record['historical_message']
            or recorded['current_baseline'] != {k: v for k, v in (
                ('headword', entry['headword']), ('message', entry['preferred_variant']['message']),
                ('token_sequence', entry['preferred_variant']['token_sequence']))}):
        raise ValueError('Corpus-only application: exact Message/lineage mismatch')
    result = json.loads(encode(dictionary))
    removed = result['entries'].pop(index)
    receipt = {
        'application_id': 'S01.15-pcd-v01-0025-corpus-only', 'dictionary_entry_id': ENTRY,
        'application_status': 'APPLIED', 'scope': 'CORPUS_ONLY_PROJECTION', 'source_revision': REVISION,
        'source_decision': {'path': SOURCE, 'sha256': SOURCE_SHA, 'selector': '/records/5',
                            'qa_dataset_sha256': export['qa_dataset_sha256']},
        'recorded_addendum_decision': {'path': ADDENDUM, 'sha256': ADDENDUM_SHA, 'selector': '/decisions/0'},
        'reason': 'MOVE_TO_CORPUS_ONLY', 'creator_reason': recorded['creator_reason'],
        'corpus_disposition': recorded['corpus_disposition'], 'replacement': None,
        'dictionary_before_sha256': BEFORE_SHA, 'dictionary_after_sha256': sha(encode(result)),
        'removed_dictionary_id': ENTRY, 'removed_entry': removed,
        'removed_entry_provenance': {'path': PACKAGE + '/dictionary.json', 'sha256': BEFORE_SHA,
                                      'selector': f'/entries/{index}'},
        'preserved_corpus': {'path': CORPUS, 'sha256': CORPUS_SHA, 'selector': f'/records/{ci}',
                             'corpus_record_id': CORPUS_ID, 'message': record['current_message']},
        'preserved_render': {'path': PACKAGE + '/' + removed['preferred_variant']['render'],
                              'sha256': '61d9313fa8020090115dfc51d6f538345931f71988350255d505f91fa316f429'},
        'changed_fields': [{'selector': f'/entries/{index}', 'operation': 'REMOVE_ARRAY_ITEM',
                             'before': copy.deepcopy(removed), 'after': None}],
        'changed_files': [PACKAGE + '/' + p for p in (
            'dictionary.json', 'variants.json', 'lineage.json', 'render-manifest.json', 'validation.json',
            'review/data.json', 'review/index.html', 'manifest.json', 'README.md', RECEIPT)],
        'other_qa_changes': 'PENDING', 'baseline_freeze': 'NOT PERFORMED',
    }
    return result, receipt


def verify(dictionary_bytes, receipt, root):
    current = json.loads(dictionary_bytes)
    predecessor = copy.deepcopy(current)
    changes = receipt['changed_fields']
    if len(changes) != 1 or changes[0]['operation'] != 'REMOVE_ARRAY_ITEM':
        raise ValueError('Corpus-only application: unexpected removal delta')
    selector = changes[0]['selector'].split('/')
    if len(selector) != 3 or selector[1] != 'entries':
        raise ValueError('Corpus-only application: unexpected original selector')
    index = int(selector[2])
    if index < 0 or index > len(predecessor['entries']):
        raise ValueError('Corpus-only application: original index out of range')
    predecessor['entries'].insert(index, copy.deepcopy(receipt['removed_entry']))
    expected, expected_receipt = apply(predecessor, root)
    if receipt != expected_receipt or current != expected or sha(dictionary_bytes) != receipt['dictionary_after_sha256']:
        raise ValueError('Corpus-only application: incompatible receipt or Dictionary delta')
    export, _ = source_decision(root)
    return predecessor, export, export['records'][5]
