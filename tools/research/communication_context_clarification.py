"""S01.11: the communication-only description step after the S01.10 receipt."""
from __future__ import annotations

import copy
import json

from tools.research.medical_context_clarification import (
    PACKAGE, SOURCE, SOURCE_SHA, QA_DATA, encode, sha, source_decision,
    RECEIPT as MEDICAL_RECEIPT, verify as verify_medical,
)

RECEIPT = 'applied-decisions/pcd-v01-0006-context.json'
BEFORE_SHA = 'dccfa377a630b1a789fb8167373c067a887dc3a0510409d6a626144a5098282e'
ENTRY = 'pcd-v01-0006'
REVISION = '9ae6675e5529c63b592074a14399465f725d2601'


def clarified(dictionary):
    result = json.loads(encode(dictionary))
    hits = [(i, e) for i, e in enumerate(result['entries']) if e['dictionary_entry_id'] == ENTRY]
    if len(hits) != 1:
        raise ValueError('Communication clarification: missing or ambiguous entry')
    index, entry = hits[0]
    if [v['variant_id'] for v in entry['variants']] != [ENTRY + suffix for suffix in (
            '-preferred', '-alternative-down', '-context-speech-less', '-context-speech-down')]:
        raise ValueError('Communication clarification: unexpected variants')
    scope = ('For comm_sound + qty_minus and comm_sound + rel_down: less human communication '
             'or human-produced sound; Less noise, please. is one context-dependent reading.')
    note = ('This clarification applies to comm_sound + qty_minus and comm_sound + rel_down. '
            'In these forms, comm_sound covers human communication (oral, written and social-media messages), '
            'and sound produced by people directly or through technical means: voice, rustling, playing music, a car. '
            'Natural sounds such as rain and animal sounds are outside this definition. '
            'Context determines the reading: «говори поменьше», «можно потише», «сделайте потише», «пиши меньше». '
            'Less noise, please. is one such reading. In these specified uses, qty_minus and rel_down are synonymous. '
            'The two comm_speak variants retain their existing meanings; no general LESS/DOWN equivalence is introduced.')
    condition = ('Human communication or human-produced sound; natural sounds are excluded. '
                 'LESS and DOWN are synonymous in these specified uses, with the reading supplied by context.')
    updates = {'semantic_neighbourhood': scope, 'usage_note': note,
               'context_warnings': [
                   'The expanded readings apply to the two comm_sound forms only; comm_speak descriptions are unchanged.',
                   'Less noise, please. is one contextual reading, not the full scope of the comm_sound forms.',
                   'LESS/DOWN synonymy is local to the specified human-communication and human-produced-sound uses.',
               ]}
    for prefix in ('preferred_variant', 'variants/0', 'variants/1'):
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
    decision = export['records'][2]
    if (decision['dictionary_entry_id'] != ENTRY or decision['corpus_record_id'] != 'clc-v01-0008-r1'
            or decision['decision'] != 'NEEDS_CORRECTION' or sha(encode(dictionary)) != BEFORE_SHA):
        raise ValueError('Communication clarification: source decision or predecessor mismatch')
    updated, changes = clarified(dictionary)
    receipt = {'application_id': 'S01.11-pcd-v01-0006-context', 'dictionary_entry_id': ENTRY,
               'application_status': 'APPLIED', 'scope': 'CONTEXT_CLARIFICATION_ONLY',
               'source_revision': REVISION,
               'source_decision': {'path': SOURCE, 'sha256': SOURCE_SHA, 'selector': '/records/2',
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
            raise ValueError('Communication clarification: applied field differs from receipt')
        node[parts[-1]] = copy.deepcopy(change['before'])
    expected, expected_receipt = apply(predecessor, root)
    if receipt != expected_receipt or current != expected or sha(dictionary_bytes) != receipt['dictionary_after_sha256']:
        raise ValueError('Communication clarification: incompatible receipt or Dictionary delta')
    export, _ = source_decision(root)
    return predecessor, export, export['records'][2]


def receipt_refs(manifest):
    """Only the existing one-step receipt or this exact ordered two-step sequence."""
    if 'context_clarifications' in manifest:
        refs = manifest['context_clarifications']
        if 'context_clarification' in manifest or [r['path'] for r in refs] != [MEDICAL_RECEIPT, RECEIPT]:
            raise ValueError('Context clarification sequence mismatch')
        return refs
    if 'context_clarification' in manifest:
        ref = manifest['context_clarification']
        if ref['path'] != MEDICAL_RECEIPT:
            raise ValueError('Unknown context clarification receipt path')
        return [ref]
    return []


def verify_sequence(dictionary_bytes, receipts, root):
    if len(receipts) == 1:
        original, export, decision = verify_medical(dictionary_bytes, receipts[0], root)
        return original, export, [decision]
    if len(receipts) != 2 or receipts[0]['dictionary_after_sha256'] != receipts[1]['dictionary_before_sha256']:
        raise ValueError('Context clarification sequence has a broken intermediate hash link')
    intermediate, _, communication_decision = verify(dictionary_bytes, receipts[1], root)
    original, export, medical_decision = verify_medical(encode(intermediate), receipts[0], root)
    return original, export, [medical_decision, communication_decision]
