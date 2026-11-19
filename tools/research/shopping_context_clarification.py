"""S01.12: the shopping description step after the unchanged S01.10/11 receipts."""
from __future__ import annotations

import copy
import json

from tools.research.medical_context_clarification import SOURCE, SOURCE_SHA, encode, sha, source_decision

RECEIPT = 'applied-decisions/pcd-v01-0009-context.json'
BEFORE_SHA = 'fea29c8aa2d1aee8b53d7b786f6656d64ceda9a7d7af4622d8c4bc0a480a2081'
ENTRY = 'pcd-v01-0009'
REVISION = '39bf2d3d2f181d8f78626b68c6bca11b7babbf8a'


def clarified(dictionary):
    result = json.loads(encode(dictionary))
    hits = [(i, e) for i, e in enumerate(result['entries']) if e['dictionary_entry_id'] == ENTRY]
    if len(hits) != 1:
        raise ValueError('Shopping clarification: missing or ambiguous entry')
    index, entry = hits[0]
    if [v['variant_id'] for v in entry['variants']] != [ENTRY + '-preferred']:
        raise ValueError('Shopping clarification: unexpected variants')
    scope = ('General grocery / food shop or classic supermarket: in place_shop + need_food, '
             'place_shop denotes shopping and need_food specifies the shop type.')
    note = ('For this entry and its existing place_shop + need_food form, place_shop denotes the process of shopping; '
            'the second icon need_food specifies a grocery / food shop or a classic supermarket. '
            'In the creator\'s explanatory examples, a meat icon after place_shop specifies a specialized meat shop, '
            'and a repair icon specifies a DIY shop. These examples explain the shop-type distinction; '
            'they do not add variants or assign an ID to the repair icon.')
    condition = ('This existing form uses need_food as the second icon to specify a grocery / food shop or '
                 'classic supermarket; place_shop supplies shopping.')
    updates = {'semantic_neighbourhood': scope, 'usage_note': note,
               'context_warnings': [
                   'This clarification is scoped to the existing entry and the creator\'s shop-type examples, '
                   'not a universal rule for every combination with place_shop.',
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
    decision = export['records'][3]
    if (decision['dictionary_entry_id'] != ENTRY or decision['corpus_record_id'] != 'clh-v01-0014'
            or decision['decision'] != 'NEEDS_CORRECTION' or sha(encode(dictionary)) != BEFORE_SHA):
        raise ValueError('Shopping clarification: source decision or predecessor mismatch')
    updated, changes = clarified(dictionary)
    receipt = {'application_id': 'S01.12-pcd-v01-0009-context', 'dictionary_entry_id': ENTRY,
               'application_status': 'APPLIED', 'scope': 'CONTEXT_CLARIFICATION_ONLY',
               'source_revision': REVISION,
               'source_decision': {'path': SOURCE, 'sha256': SOURCE_SHA, 'selector': '/records/3',
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
            raise ValueError('Shopping clarification: applied field differs from receipt')
        node[parts[-1]] = copy.deepcopy(change['before'])
    expected, expected_receipt = apply(predecessor, root)
    if receipt != expected_receipt or current != expected or sha(dictionary_bytes) != receipt['dictionary_after_sha256']:
        raise ValueError('Shopping clarification: incompatible receipt or Dictionary delta')
    export, _ = source_decision(root)
    return predecessor, export, export['records'][3]
