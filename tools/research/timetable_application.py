"""S01.16: one previously approved related timetable entry; exact append/inverse."""
from __future__ import annotations

import copy
import json
import xml.etree.ElementTree as ET

from tools.research.medical_context_clarification import PACKAGE, SOURCE, SOURCE_SHA, encode, sha, source_decision
from tools.research.corpus_only_application import ADDENDUM, ADDENDUM_SHA
from tools.research.pedestrian_preferred_application import CORPUS, CORPUS_SHA
from tools.validate_message_schema import schema_errors, semantic_errors

RECEIPT = 'applied-decisions/pcd-v01-0066-timetable.json'
BEFORE_SHA = '4679738d0d2e1bdf6a179e97c2f3ac966c1697b435ae730b383e2ddc197b7ff3'
REVISION = 'b74f03f111f2d22c6bea691b2488a8591c1c4a6f'
ENTRY = 'pcd-v01-0066'
TEMPORARY_ID = 'qa-new-public-transport-timetable'
RELATED = 'pcd-v01-0065'
CORPUS_ID = 'clh-v01-0022'
RELATIONSHIP = 'CREATOR_APPROVED_RELATED_ENTRY_NOT_CORPUS_MESSAGE'
EXPECTED_IDS = ['move_public', 'media_text', 'time', 'punct_question']


def approved_source(root):
    source_decision(root)  # Preserve the exact final-export and original QA bindings.
    raw = (root / ADDENDUM).read_bytes()
    corpus_raw = (root / CORPUS).read_bytes()
    if sha(raw) != ADDENDUM_SHA or sha(corpus_raw) != CORPUS_SHA:
        raise ValueError('Timetable application: addendum or Corpus source hash mismatch')
    addendum = json.loads(raw)
    hits = [(i, d) for i, d in enumerate(addendum['decisions'])
            if d.get('new_related_entry', {}).get('temporary_qa_id') == TEMPORARY_ID]
    if len(hits) != 1:
        raise ValueError('Timetable application: missing or ambiguous temporary_qa_id')
    index, decision = hits[0]
    pending = decision['new_related_entry']
    ids = [t['id'] for f in pending['message']['frames'] for t in f['tokens']]
    if (decision['dictionary_entry_id'] != RELATED or decision['corpus_record_id'] != CORPUS_ID
            or pending['status'] != 'CREATOR-APPROVED / PENDING BASELINE APPLICATION'
            or pending['is_variant_of_arrival_question'] is not False
            or ids != EXPECTED_IDS or pending['token_sequence'].split(' + ') != EXPECTED_IDS
            or schema_errors(pending['message']) or semantic_errors(pending['message'])):
        raise ValueError('Timetable application: approved Message/decision mismatch')
    preview = (root / PACKAGE / pending['preview_render']).read_bytes()
    if (sha(preview) != pending['preview_render_sha256']
            or [n.attrib['data-id'] for n in ET.fromstring(preview).iter() if 'data-id' in n.attrib] != EXPECTED_IDS):
        raise ValueError('Timetable application: corrected K01/K01a preview mismatch')
    corpus_hits = [(i, r) for i, r in enumerate(json.loads(corpus_raw)['records']) if r['corpus_record_id'] == CORPUS_ID]
    if len(corpus_hits) != 1:
        raise ValueError('Timetable application: ambiguous Corpus lineage')
    ci, record = corpus_hits[0]
    return index, decision, pending, ci, record


def apply(dictionary, root):
    export, _ = source_decision(root)
    index, decision, pending, ci, corpus = approved_source(root)
    if sha(encode(dictionary)) != BEFORE_SHA:
        raise ValueError('Timetable application: predecessor mismatch')
    assigned = [e['dictionary_entry_id'] for e in dictionary['entries']]
    if max(int(x.removeprefix('pcd-v01-')) for x in assigned) != 65 or ENTRY in assigned or 'pcd-v01-0025' in assigned:
        raise ValueError('Timetable application: unexpected stable ID allocation')
    arrivals = [e for e in dictionary['entries'] if e['dictionary_entry_id'] == RELATED]
    if len(arrivals) != 1 or arrivals[0]['preferred_variant']['message'] != corpus['current_message']:
        raise ValueError('Timetable application: arrival-time lineage mismatch')
    arrival = arrivals[0]
    if arrival['preferred_variant']['token_sequence'] != 'move_public + time + punct_question':
        raise ValueError('Timetable application: arrival-time composition changed')
    selector = f'/decisions/{index}/new_related_entry'
    source_ref = {'path': ADDENDUM, 'sha256': ADDENDUM_SHA, 'selector': selector}
    context_ref = {'path': CORPUS, 'sha256': CORPUS_SHA, 'selector': f'/records/{ci}/applicability'}
    context = copy.deepcopy(corpus['applicability'])
    mode = sorted({x['communication_mode'] for x in context})
    surface = sorted({x['communication_surface'] for x in context})
    message = copy.deepcopy(pending['message'])
    variant = {
        'variant_id': ENTRY + '-preferred', 'variant_type': 'PREFERRED', 'status': 'CURRENT_ACCEPTED',
        'message': message, 'token_sequence': pending['token_sequence'], 'render': f'renders/{ENTRY}-preferred.svg',
        'mode': mode, 'surface': surface, 'context': copy.deepcopy(context),
        'variant_context_note': 'Standalone related timetable entry; not a variant of the arrival-time question.',
        'semantic_distinction': pending['meaning'],
        'provenance': {'corpus_record_ids': [CORPUS_ID], 'dictionary_entry_id': ENTRY,
                       'authority': 'CREATOR-APPROVED ADDENDUM', 'creator_decision': source_ref,
                       'context_source': context_ref},
        'render_status': 'RENDERED_CANONICAL',
    }
    origin = copy.deepcopy(corpus['provenance'])
    origin['addendum'] = copy.deepcopy(source_ref)
    entry = {
        'dictionary_entry_id': ENTRY, 'semantic_id': 'pictiq-dict-sem-v0.1-0066',
        'headword': pending['headword'], 'aliases': [], 'semantic_neighbourhood': pending['meaning'],
        'candidate_lookup_material': [],
        'usage_note': 'Distinct timetable/schedule request, not a variant of the arrival-time question. ' + decision['resolved_follow_up'],
        'known_ambiguity': [], 'context_warnings': ['Distinct from the arrival-time question (pcd-v01-0065).'],
        'preferred_variant': copy.deepcopy(variant), 'variants': [variant],
        'mode': mode, 'surface': surface, 'context': context, 'corpus_refs': [CORPUS_ID],
        'source_evidence_summary': copy.deepcopy(arrival['source_evidence_summary']),
        'creator_review': {'decision': 'CREATOR-APPROVED', 'source_addendum': source_ref,
                           'temporary_qa_id': TEMPORARY_ID, 'is_variant_of_arrival_question': False},
        'system_candidate_history': {'candidate_entry_id': None, 'temporary_qa_id': TEMPORARY_ID},
        'lineage': {
            'dictionary_entry_id': ENTRY, 'corpus_record_id': CORPUS_ID, 'candidate_entry_id': None,
            'relationship': RELATIONSHIP, 'related_dictionary_entry_id': RELATED,
            'source_message': copy.deepcopy(message), 'source_sequence': pending['token_sequence'],
            'preferred_message': copy.deepcopy(message), 'preferred_sequence': pending['token_sequence'],
            'preferred_changed_by_creator_review': False,
            'authority_path': ['ACCEPTED_COMPOSITION_CORPUS_BASELINE_V0.1 / RELATED EVIDENCE',
                                'CREATOR-APPROVED TIMETABLE ADDENDUM', 'S01.16_BASELINE_APPLICATION'],
            'source_provenance': [origin], 'message_source': source_ref,
            'corpus_message': copy.deepcopy(corpus['current_message']), 'context_source': context_ref,
            'creator_review_ref': {'type': 'CREATOR_APPROVED_RELATED_ADDENDUM',
                                   'export_path': 'final-creator-qa-addendum-v0.2.json', 'corpus_record_id': CORPUS_ID,
                                   'selector': selector, 'temporary_qa_id': TEMPORARY_ID},
        },
    }
    result = json.loads(encode(dictionary))
    position = len(result['entries'])
    result['entries'].append(entry)
    receipt = {
        'application_id': 'S01.16-pcd-v01-0066-timetable', 'dictionary_entry_id': ENTRY,
        'application_status': 'APPLIED', 'scope': 'TIMETABLE_ENTRY_ADDITION', 'source_revision': REVISION,
        'source_decision': {'path': SOURCE, 'sha256': SOURCE_SHA, 'selector': '/records/9',
                            'qa_dataset_sha256': export['qa_dataset_sha256']},
        'creator_decision': {'source': source_ref, 'verbatim_object': copy.deepcopy(pending)},
        'recorded_addendum_decision': {'path': ADDENDUM, 'sha256': ADDENDUM_SHA, 'selector': f'/decisions/{index}'},
        'temporary_qa_id': TEMPORARY_ID, 'related_arrival_entry_id': RELATED, 'corpus_record_id': CORPUS_ID,
        'context_source': context_ref,
        'context_inheritance': 'The approved related object declares no separate mode/surface/context; use the explicitly linked Corpus applicability unchanged.',
        'id_allocation': {'policy': 'Append the next pcd-v01-NNNN after assigned IDs; never recycle withdrawn pcd-v01-0025.',
                           'previous_max_assigned_id': RELATED, 'assigned_id': ENTRY},
        'technical_correction': copy.deepcopy(pending['technical_correction']),
        'technical_evidence': [
            {'path': PACKAGE + '/repairs/K01-timetable-media-text/README.md', 'sha256': '03fabea343c732cda3c038a656acc903f7a44c45f040d8fa1789fcde016dbfe9'},
            {'path': PACKAGE + '/repairs/K01-timetable-media-text/K01a-REPORT.md', 'sha256': '6696140b787a3c744451f8b6ed64dd63ded0da41bf62a60113e70fd10afdd062'},
        ],
        'corpus_lineage': {'path': CORPUS, 'sha256': CORPUS_SHA, 'selector': f'/records/{ci}', 'relationship': RELATIONSHIP},
        'message': copy.deepcopy(message), 'token_sequence': pending['token_sequence'],
        'dictionary_before_sha256': BEFORE_SHA, 'dictionary_after_sha256': sha(encode(result)),
        'created_entry': entry,
        'changed_fields': [{'selector': f'/entries/{position}', 'operation': 'APPEND_ARRAY_ITEM', 'before': None, 'after': copy.deepcopy(entry)}],
        'changed_files': [PACKAGE + '/' + p for p in ('dictionary.json', 'variants.json', 'lineage.json', 'validation.json',
            'render-manifest.json', 'review/data.json', 'review/index.html', 'manifest.json', 'README.md', variant['render'], RECEIPT)],
        'other_qa_changes': 'NOT APPLIED BY THIS PASS', 'baseline_freeze': 'NOT PERFORMED',
    }
    return result, receipt


def verify(dictionary_bytes, receipt, root):
    current = json.loads(dictionary_bytes)
    predecessor = copy.deepcopy(current)
    changes = receipt['changed_fields']
    if (len(changes) != 1 or changes[0]['operation'] != 'APPEND_ARRAY_ITEM'
            or changes[0]['selector'] != f"/entries/{len(current['entries']) - 1}"
            or predecessor['entries'][-1] != receipt['created_entry']):
        raise ValueError('Timetable application: unexpected exact append delta')
    predecessor['entries'].pop()
    expected, expected_receipt = apply(predecessor, root)
    if receipt != expected_receipt or current != expected or sha(dictionary_bytes) != receipt['dictionary_after_sha256']:
        raise ValueError('Timetable application: incompatible receipt or Dictionary delta')
    export, _ = source_decision(root)
    return predecessor, export, export['records'][9]
