"""S01.14: one creator-authorized, road-sign preferred change and its exact inverse."""
from __future__ import annotations

import copy
import json

from tools.research.medical_context_clarification import PACKAGE, SOURCE, SOURCE_SHA, encode, sha, source_decision
from tools.validate_message_schema import schema_errors, semantic_errors

RECEIPT = 'applied-decisions/pcd-v01-0028-preferred.json'
BEFORE_SHA = '13b868cc4abc5d68b4aae2135a31cf12888013254c94b6512ba61d67891a643a'
REVISION = 'e95b79858d6d4314f668884b57c425595b546ca8'
ENTRY = 'pcd-v01-0028'
CORPUS = 'docs/research/composition-library-baseline-v0.1/accepted-corpus.json'
CORPUS_SHA = '8dc2509dfc9d31d006726732e1825bc120dbeef06c5c1b0b1798e6315808e14e'


def apply(dictionary, root):
    export, _ = source_decision(root)
    decision = export['records'][7]
    if (decision['dictionary_entry_id'] != ENTRY or decision['corpus_record_id'] != 'clh-v01-0047'
            or decision['decision'] != 'KEEP_ENTRY_CHANGE_PREFERRED' or sha(encode(dictionary)) != BEFORE_SHA):
        raise ValueError('Pedestrian preferred: decision or predecessor mismatch')
    raw_corpus = (root / CORPUS).read_bytes()
    if sha(raw_corpus) != CORPUS_SHA:
        raise ValueError('Pedestrian preferred: historical Corpus hash mismatch')
    corpus_hits = [(i, r) for i, r in enumerate(json.loads(raw_corpus)['records'])
                   if r['corpus_record_id'] == 'clh-v01-0047']
    if len(corpus_hits) != 1:
        raise ValueError('Pedestrian preferred: ambiguous historical Corpus record')
    corpus_index, corpus_record = corpus_hits[0]
    result = json.loads(encode(dictionary))
    hits = [(i, e) for i, e in enumerate(result['entries']) if e['dictionary_entry_id'] == ENTRY]
    if len(hits) != 1:
        raise ValueError('Pedestrian preferred: missing or ambiguous entry')
    index, entry = hits[0]
    old = copy.deepcopy(entry['preferred_variant'])
    historical = copy.deepcopy(corpus_record['historical_message'])
    if (entry['variants'] != [old] or old['variant_id'] != ENTRY + '-preferred'
            or old['token_sequence'] != 'person_generic + move_feet'
            or historical != entry['lineage']['source_message']):
        raise ValueError('Pedestrian preferred: unexpected prior variant or lineage')
    # Exact author-supplied single ID encoded in the existing Message format.
    feet = {'schema': '0.1', 'pictiq': '1.1', 'frames': [{'tokens': [{'type': 'icon', 'id': 'move_feet'}]}]}
    messages = [feet, old['message'], historical]
    sequences = [['move_feet'], ['person_generic', 'move_feet'], ['person_generic', 'move_feet', 'rel_here']]
    for message, ids in zip(messages, sequences):
        errors = schema_errors(message) + semantic_errors(message)
        if errors or [t['id'] for t in message['frames'][0]['tokens']] != ids:
            raise ValueError(f'Pedestrian preferred: invalid exact Message: {errors}')
    context = copy.deepcopy(entry['context'])
    for item in context:
        item['context']['task'] = ['pedestrian movement / walking / movement on foot']
    source_ref = {'path': SOURCE, 'sha256': SOURCE_SHA, 'selector': '/records/7'}
    origins = [
        {**source_ref, 'message_encoding': 'Existing Message v0.1 encoding of the author\'s exact move_feet sequence'},
        {'path': PACKAGE + '/dictionary.json', 'sha256': BEFORE_SHA,
         'selector': f'/entries/{index}/preferred_variant/message'},
        {'path': CORPUS, 'sha256': CORPUS_SHA, 'selector': f'/records/{corpus_index}/historical_message'},
    ]
    notes = [
        'Preferred for the road sign (WAYFINDING); not a universal preference for other modes or surfaces.',
        'Explicit PERSON form remains accepted for movement on foot in context; former preferred retained.',
        'Explicit PERSON and HERE form remains accepted for movement on foot at an indicated location. '
        'Its historical crossing-point interpretation is evidence, not a meaning guaranteed by these tokens.',
    ]
    ids = [ENTRY + '-preferred-feet', old['variant_id'], ENTRY + '-contextual-here']
    variants = []
    for n, (variant_id, message, origin, note) in enumerate(zip(ids, messages, origins, notes)):
        variant = copy.deepcopy(old)
        variant.update(variant_id=variant_id, variant_type='PREFERRED' if n == 0 else 'CONTEXTUAL',
                       message=message, token_sequence=' + '.join(sequences[n]),
                       render=old['render'] if n == 1 else f'renders/{variant_id}.svg',
                       context=copy.deepcopy(context), variant_context_note=note,
                       semantic_distinction='Pedestrian movement / walking / movement on foot')
        if n == 2:
            for item in variant['context']:
                item['context']['task'] = ['movement on foot at the indicated location']
        variant['provenance'].update(final_creator_decision=copy.deepcopy(source_ref), message_source=origin)
        variants.append(variant)
    updates = {
        'semantic_neighbourhood': 'Pedestrian movement / walking / movement on foot',
        'usage_note': 'All three forms are accepted: move_feet; person_generic + move_feet; '
                      'person_generic + move_feet + rel_here. For a road sign (WAYFINDING), the creator '
                      'prefers move_feet. This is not a universal preference for every mode or surface. '
                      'Movement on foot does not by itself identify a crossing point; crossing is a more '
                      'specific situation supplied by context. The historical crossing task remains in '
                      'Corpus and source evidence, not as the general meaning of move_feet.',
        'context_warnings': [
            'Road-sign preferred only: move_feet; explicit PERSON and PERSON + HERE forms remain accepted in context.',
            'Walking / movement on foot does not entail a crossing-place relation or driver-yield instruction.',
        ],
        'context': context, 'preferred_variant': copy.deepcopy(variants[0]), 'variants': variants,
        'lineage/preferred_message': copy.deepcopy(feet), 'lineage/preferred_sequence': 'move_feet',
        'lineage/authority_path': [*entry['lineage']['authority_path'], 'FINAL_CREATOR_QA_V0.2 / S01.14'],
    }
    changes = []
    for relative, after in updates.items():
        node = entry
        parts = relative.split('/')
        for part in parts[:-1]:
            node = node[part]
        key = parts[-1]
        changes.append({'selector': f'/entries/{index}/' + relative,
                        'before': copy.deepcopy(node[key]), 'after': copy.deepcopy(after)})
        node[key] = copy.deepcopy(after)
    receipt = {
        'application_id': 'S01.14-pcd-v01-0028-preferred', 'dictionary_entry_id': ENTRY,
        'application_status': 'APPLIED', 'scope': 'PREFERRED_VARIANT_CHANGE', 'source_revision': REVISION,
        'source_decision': {**source_ref, 'qa_dataset_sha256': export['qa_dataset_sha256']},
        'dictionary_before_sha256': BEFORE_SHA, 'dictionary_after_sha256': sha(encode(result)),
        'changed_fields': changes,
        'messages_before_after': {'preferred_before': old['message'], 'preferred_after': feet,
                                  'variants_before': [old['message']], 'variants_after': messages},
        'variant_lineage': [{'variant_id': v['variant_id'], 'message_source': o,
                             'creator_decision': source_ref} for v, o in zip(variants, origins)],
        'preference_context': {'mode': entry['mode'], 'surface': entry['surface'],
                               'situation': 'road sign', 'universal_preference': False},
        'other_qa_changes': 'PENDING', 'baseline_freeze': 'NOT PERFORMED',
    }
    return result, receipt


def verify(dictionary_bytes, receipt, root):
    current = json.loads(dictionary_bytes)
    predecessor = copy.deepcopy(current)
    for change in receipt['changed_fields']:
        node = predecessor
        parts = change['selector'].strip('/').split('/')
        for part in parts[:-1]:
            node = node[int(part)] if isinstance(node, list) else node[part]
        if node[parts[-1]] != change['after']:
            raise ValueError('Pedestrian preferred: applied field differs from receipt')
        node[parts[-1]] = copy.deepcopy(change['before'])
    expected, expected_receipt = apply(predecessor, root)
    if receipt != expected_receipt or current != expected or sha(dictionary_bytes) != receipt['dictionary_after_sha256']:
        raise ValueError('Pedestrian preferred: incompatible receipt or Dictionary delta')
    export, _ = source_decision(root)
    return predecessor, export, export['records'][7]
