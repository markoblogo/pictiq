"""S01.13: the parking description step after the unchanged S01.10/11/12 receipts."""
from __future__ import annotations

import copy
import json

from tools.research.medical_context_clarification import SOURCE, SOURCE_SHA, encode, sha, source_decision

RECEIPT = 'applied-decisions/pcd-v01-0030-context.json'
BEFORE_SHA = '9b4bddcb3cff4d06c94f0e8da63f0609dc666efc366242683e347fecc7ac03a3'
ENTRY = 'pcd-v01-0030'
REVISION = '044bb6959810782cbe04ef6a10f6b536c8a3faaa'


def clarified(dictionary):
    result = json.loads(encode(dictionary))
    hits = [(i, e) for i, e in enumerate(result['entries']) if e['dictionary_entry_id'] == ENTRY]
    if len(hits) != 1:
        raise ValueError('Parking clarification: missing or ambiguous entry')
    index, entry = hits[0]
    if [v['variant_id'] for v in entry['variants']] != [ENTRY + '-preferred']:
        raise ValueError('Parking clarification: unexpected variants')
    scope = ('Vehicle prohibition: no passage, no parking, or both according to the situation; '
             'No parking is the parking-context reading.')
    note = ('In writing or on a map, rel_here + logic_no + move_car, or the creator\'s example '
            'rel_here + [place icon] + logic_no + move_car, prohibits vehicles there, including passage and parking. '
            'The place icon is unspecified; this explanation assigns no ID or new Message. '
            'On site, logic_no + move_car means no passage at a passage/road, '
            'no parking at a place that may be taken for parking, or both where both situations apply. '
            'In these specified contexts, logic_no + move_car and move_car + logic_no are equivalent: '
            '«запрещено авто» / «авто запрещено». No parking is one situational reading; '
            'the combination does not always mean only no parking.')
    condition = ('The existing written/map form prohibits vehicles there, including passage and parking; '
                 'on-site interpretation depends on the road/parking situation. '
                 'The creator accepts both logic_no + move_car and move_car + logic_no in these contexts. '
                 'The lineage retains rel_here + move_car + logic_no as history; no new current variant is added.')
    updates = {'semantic_neighbourhood': scope, 'usage_note': note,
               'known_ambiguity': [
                   'Passage-only, parking-only and combined prohibitions depend on the situation; '
                   'AUTO/NO does not by itself force the parking-only reading.',
               ],
               'context_warnings': [
                   'The situation supplies whether passage, parking or both are prohibited; '
                   'do not force a parking-only reading.',
                   'The equivalence of AUTO/NO orders is scoped to these uses, not a general negation-order rule.',
               ]}
    for prefix in ('preferred_variant', 'variants/0'):
        updates[prefix + '/semantic_distinction'] = scope
        updates[prefix + '/variant_context_note'] = condition
    changes = []
    for relative, after in updates.items():
        node = entry
        parts = relative.split('/')
        for part in parts[:-1]:
            node = node[int(part)] if isinstance(node, list) else node[part]
        key = parts[-1]
        changes.append({'selector': f'/entries/{index}/' + relative,
                        'before': copy.deepcopy(node[key]), 'after': copy.deepcopy(after)})
        node[key] = copy.deepcopy(after)
    return result, changes


def apply(dictionary, root):
    export, _ = source_decision(root)
    decision = export['records'][8]
    if (decision['dictionary_entry_id'] != ENTRY or decision['corpus_record_id'] != 'clh-v01-0049'
            or decision['decision'] != 'NEEDS_CORRECTION' or sha(encode(dictionary)) != BEFORE_SHA):
        raise ValueError('Parking clarification: source decision or predecessor mismatch')
    updated, changes = clarified(dictionary)
    receipt = {'application_id': 'S01.13-pcd-v01-0030-context', 'dictionary_entry_id': ENTRY,
               'application_status': 'APPLIED', 'scope': 'CONTEXT_CLARIFICATION_ONLY',
               'source_revision': REVISION,
               'source_decision': {'path': SOURCE, 'sha256': SOURCE_SHA, 'selector': '/records/8',
                                   'qa_dataset_sha256': export['qa_dataset_sha256']},
               'dictionary_before_sha256': BEFORE_SHA, 'dictionary_after_sha256': sha(encode(updated)),
               'changed_fields': changes, 'other_qa_changes': 'PENDING', 'baseline_freeze': 'NOT PERFORMED'}
    return updated, receipt


def verify(dictionary_bytes, receipt, root):
    current = json.loads(dictionary_bytes)
    predecessor = copy.deepcopy(current)
    for change in receipt['changed_fields']:
        node = predecessor
        parts = change['selector'].strip('/').split('/')
        for part in parts[:-1]:
            node = node[int(part)] if isinstance(node, list) else node[part]
        if node[parts[-1]] != change['after']:
            raise ValueError('Parking clarification: applied field differs from receipt')
        node[parts[-1]] = copy.deepcopy(change['before'])
    expected, expected_receipt = apply(predecessor, root)
    if receipt != expected_receipt or current != expected or sha(dictionary_bytes) != receipt['dictionary_after_sha256']:
        raise ValueError('Parking clarification: incompatible receipt or Dictionary delta')
    export, _ = source_decision(root)
    return predecessor, export, export['records'][8]
