"""S01.10: one exact descriptive revision, preserving the original QA snapshot."""
from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path

PACKAGE = 'docs/research/composition-dictionary-baseline-v0.1'
RECEIPT = 'applied-decisions/pcd-v01-0002-context.json'
SOURCE = PACKAGE + '/creator-final-qa-2026-11-19/creator-export.json'
QA_DATA = PACKAGE + '/review/final-creator-qa-v0.2.json'
SOURCE_SHA = '609c38175864d5da66e9f969364ea5dc84f71a15eab7bf4cfed14d81d1412152'
BEFORE_SHA = '9c0ed9e048b9a4d134635e7f21eab68809b42bfd495ee0697db3ad67063ae107'
ENTRY = 'pcd-v01-0002'
REVISION = '36bf1b2421ce900eab5123f0ff646c48a9133c4e'


def encode(value):
    return (json.dumps(value, ensure_ascii=False, indent=2) + '\n').encode('utf-8')


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def source_decision(root: Path):
    raw = (root / SOURCE).read_bytes()
    if sha(raw) != SOURCE_SHA:
        raise ValueError('Medical clarification: creator export hash mismatch')
    export = json.loads(raw)
    qa = json.loads((root / QA_DATA).read_bytes())
    core = {k: v for k, v in qa.items() if k != 'qa_dataset_sha256'}
    digest = sha(json.dumps(core, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode())
    if (digest != qa['qa_dataset_sha256'] or export['qa_dataset_sha256'] != digest
            or export['source_baseline'] != qa['source_baseline']
            or export['source_baseline']['dictionary_json_sha256'] != BEFORE_SHA):
        raise ValueError('Medical clarification: original QA snapshot mismatch')
    decision = export['records'][0]
    if (decision['dictionary_entry_id'] != ENTRY or decision['corpus_record_id'] != 'clh-v01-0003'
            or decision['decision'] != 'NEEDS_CORRECTION'):
        raise ValueError('Medical clarification: source decision mismatch')
    return export, decision


def clarified(dictionary):
    # The generator shares preferred_variant with variants[0] in memory;
    # receipts describe independent JSON locations, not Python object aliases.
    result = json.loads(encode(dictionary))
    hits = [(i, e) for i, e in enumerate(result['entries']) if e['dictionary_entry_id'] == ENTRY]
    if len(hits) != 1:
        raise ValueError('Medical clarification: missing or ambiguous entry')
    index, entry = hits[0]
    if [v['variant_id'] for v in entry['variants']] != [ENTRY + '-preferred', ENTRY + '-contextual-person']:
        raise ValueError('Medical clarification: unexpected variants')
    values = {
        'semantic_neighbourhood': 'Urgent medical help for oneself or another person; the form depends on the request and shared visible or written context.',
        'usage_note': ('For this request, safety_medical + punct_exclaim is sufficient when asking for oneself, including written requests. '
                       'It is also sufficient for another person in a shared visible situation when that person is explicitly pointed to. '
                       'Use person_generic + safety_medical + punct_exclaim for another person outside shared visual contact, '
                       'or in a written message about another person. The self-referential default belongs to use of this request; '
                       'absence of PERSON is not a grammatical first-person pronoun.'),
        'context_warnings': [
            'The short form covers a request for oneself, including in writing.',
            'For another person, the short form relies on shared visibility and explicit pointing.',
            'Use the PERSON form for another person outside shared visual contact or in writing about another person.',
        ],
    }
    preferred_meaning = 'Urgent medical help for oneself, including in writing, or for another person explicitly pointed to in a shared visible situation.'
    preferred_note = 'The self-referential default applies to this request; omission of PERSON does not encode a grammatical first-person pronoun.'
    person_meaning = 'Urgent medical help for another person outside shared visual contact, or in a written message about another person.'
    person_note = 'For another person in a shared visible situation, explicit pointing allows the shorter form without PERSON.'
    updates = dict(values)
    for field, value in [('semantic_distinction', preferred_meaning), ('variant_context_note', preferred_note)]:
        updates['preferred_variant/' + field] = value
        updates['variants/0/' + field] = value
    updates['variants/1/semantic_distinction'] = person_meaning
    updates['variants/1/variant_context_note'] = person_note
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


def apply(dictionary, root: Path):
    export, _ = source_decision(root)
    if sha(encode(dictionary)) != BEFORE_SHA:
        raise ValueError('Medical clarification: unexpected generated predecessor; no snapshot rebinding')
    updated, changes = clarified(dictionary)
    receipt = {
        'application_id': 'S01.10-pcd-v01-0002-context',
        'dictionary_entry_id': ENTRY,
        'application_status': 'APPLIED',
        'scope': 'CONTEXT_CLARIFICATION_ONLY',
        'source_revision': REVISION,
        'source_decision': {'path': SOURCE, 'sha256': SOURCE_SHA, 'selector': '/records/0',
                            'qa_dataset_sha256': export['qa_dataset_sha256']},
        'dictionary_before_sha256': BEFORE_SHA,
        'dictionary_after_sha256': sha(encode(updated)),
        'changed_fields': changes,
        'other_qa_changes': 'PENDING',
        'baseline_freeze': 'NOT PERFORMED',
    }
    return updated, receipt


def verify(dictionary_bytes: bytes, receipt, root: Path):
    """Verify the exact field delta back to the still-bound original snapshot."""
    export, decision = source_decision(root)
    current = json.loads(dictionary_bytes)
    predecessor = copy.deepcopy(current)
    for change in receipt['changed_fields']:
        parts = change['selector'].strip('/').split('/')
        node = predecessor
        for part in parts[:-1]:
            node = node[int(part)] if isinstance(node, list) else node[part]
        if node[parts[-1]] != change['after']:
            raise ValueError('Medical clarification: applied field differs from receipt')
        node[parts[-1]] = copy.deepcopy(change['before'])
    expected, expected_receipt = apply(predecessor, root)
    if receipt != expected_receipt or current != expected or sha(dictionary_bytes) != receipt['dictionary_after_sha256']:
        raise ValueError('Medical clarification: incompatible receipt or Dictionary delta')
    return predecessor, export, decision
