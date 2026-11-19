#!/usr/bin/env python3
"""Build/verify one read-only Dictionary-variant replica package (JSON + standalone SVG)."""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from pictiq_renderer.registry import Registry
from pictiq_renderer.svg_renderer import RenderOptions, render_svg
from pictiq_renderer.validator import normalize_and_validate_message
from tools.validate_message_schema import schema_errors

PACKAGE = 'docs/research/composition-dictionary-baseline-v0.1'
FORMAT = 'pictiq-replica-package'
VERSION = '0.1'


class PackageError(ValueError):
    pass


def digest(data):
    return hashlib.sha256(data).hexdigest()


def encode(value):
    return (json.dumps(value, ensure_ascii=False, indent=2) + '\n').encode('utf-8')


def one(rows, key, value):
    matches = [(i, r) for i, r in enumerate(rows) if r.get(key) == value]
    if len(matches) != 1:
        raise PackageError(f'Expected one {key}={value}, found {len(matches)}; no fallback selected')
    return matches[0]


class Inputs:
    """Read each source state once; detect changes while rendering instead of certifying a mixed state."""
    def __init__(self, root):
        self.root = Path(root).resolve()
        self.bytes = {}

    def path(self, relative):
        path = (self.root / relative).resolve()
        if not path.is_relative_to(self.root):
            raise PackageError(f'Input outside repository: {relative}')
        return path

    def take(self, relative):
        key = str(self.path(relative).relative_to(self.root))
        if key not in self.bytes:
            self.bytes[key] = self.path(key).read_bytes()
        return self.bytes[key]

    def json(self, relative):
        return json.loads(self.take(relative))

    def ref(self, relative, selector=None):
        result = {'path': str(self.path(relative).relative_to(self.root)), 'sha256': digest(self.take(relative))}
        if selector is not None:
            result['selector'] = selector
        return result

    def unchanged(self):
        for relative, data in self.bytes.items():
            if self.path(relative).read_bytes() != data:
                raise PackageError(f'Input changed during assembly: {relative}')


def validate_and_render(message, registry):
    errors = schema_errors(message)
    if errors:
        raise PackageError('Invalid Message: ' + '; '.join(errors))
    _, diagnostics = normalize_and_validate_message(copy.deepcopy(message), registry)
    errors = [d.message for d in diagnostics if d.level == 'error']
    if errors:
        raise PackageError('Invalid Message: ' + '; '.join(errors))
    # Validation may suggest legacy normalization; a package must never apply it.
    for frame in message['frames']:
        for token in frame['tokens']:
            if token['type'] == 'icon' and token['id'] not in registry.icon_entries:
                raise PackageError('Noncanonical icon; automatic substitution forbidden: ' + token['id'])
    svg, _ = render_svg(message, registry, RenderOptions())  # Render the ORIGINAL Message, not normalized output.
    tree = ET.fromstring(svg)
    for element in tree.iter():
        for attr, value in element.attrib.items():
            if attr.rsplit('}', 1)[-1] == 'href' and not value.startswith('#'):
                raise PackageError('SVG has an external dependency')
            if any(not target.strip(' \"\'').startswith('#') for target in re.findall(r'url\(([^)]+)\)', value)):
                raise PackageError('SVG has an external URL dependency')
    if any(not target.strip(' \"\'').startswith('#') for target in re.findall(r'url\(([^)]+)\)', svg)):
        raise PackageError('SVG has an external CSS dependency')
    if '@import' in svg:
        raise PackageError('SVG has an external stylesheet dependency')
    return svg.encode('utf-8'), [d.to_dict() for d in diagnostics]


def compose(entry_id, variant_id, root=ROOT, revision=None):
    inputs = Inputs(root)
    relative = PACKAGE + '/dictionary.json'
    dictionary = inputs.json(relative)
    ei, entry = one(dictionary['entries'], 'dictionary_entry_id', entry_id)
    vi, variant = one(entry['variants'], 'variant_id', variant_id)
    # Single fixed source object, never reconstructed from a label or token_sequence.
    message = copy.deepcopy(variant['message'])
    shape_errors = schema_errors(message)
    if shape_errors:
        raise PackageError('Invalid Message: ' + '; '.join(shape_errors))
    manifest = inputs.json(PACKAGE + '/manifest.json')
    if manifest['artifact_sha256']['dictionary.json'] != inputs.ref(relative)['sha256']:
        raise PackageError('Dictionary source hash differs from its baseline manifest')
    review_ref = entry['lineage']['creator_review_ref']
    export_path = str((Path(PACKAGE) / review_ref['export_path']))
    export = inputs.json(export_path)
    ri, decision = one(export['records'], 'corpus_record_id', review_ref['corpus_record_id'])
    if (decision['dictionary_entry_id'] != entry_id or decision['creator_decision'] != review_ref['decision'] or
        export['source_snapshot'] != dictionary['source_snapshot'] or
        inputs.ref(export_path)['sha256'] != manifest['creator_review_export']['sha256']):
        raise PackageError('Creator decision/source snapshot linkage mismatch')
    corpus_path = str(Path(PACKAGE) / manifest['source_corpus_baseline']['path'])
    corpus = inputs.json(corpus_path)
    ci, corpus_record = one(corpus['records'], 'corpus_record_id', review_ref['corpus_record_id'])
    if (corpus_record['corpus_record_id'] not in entry['corpus_refs'] or
        inputs.ref(corpus_path)['sha256'] != manifest['source_corpus_baseline']['sha256']):
        raise PackageError('Corpus lineage mismatch')
    addendum_path = PACKAGE + '/final-creator-qa-addendum-v0.2.json'
    addendum = inputs.json(addendum_path)
    binding = addendum['source_dictionary_baseline']
    bound_sha = inputs.ref(relative)['sha256']
    if 'context_clarification' in manifest:
        from tools.research.medical_context_clarification import verify as verify_context, RECEIPT, SOURCE, QA_DATA
        application = manifest['context_clarification']
        if application['path'] != RECEIPT or inputs.ref(PACKAGE + '/' + RECEIPT)['sha256'] != application['sha256']:
            raise PackageError('Context clarification receipt binding mismatch')
        receipt = inputs.json(PACKAGE + '/' + RECEIPT)
        inputs.take(SOURCE); inputs.take(QA_DATA)
        inputs.take('tools/research/medical_context_clarification.py')
        try:
            verify_context(inputs.take(relative), receipt, inputs.root)
        except (ValueError, KeyError, TypeError, IndexError, OSError) as exc:
            raise PackageError(f'Context clarification verification failed: {exc}') from exc
        bound_sha = receipt['dictionary_before_sha256']
    if (binding['dictionary_json_sha256'] != bound_sha or
        binding['source_snapshot'] != dictionary['source_snapshot'] or
        binding['version'] != dictionary['dictionary_version']):
        raise PackageError('Active pending addendum is not bound to this Dictionary')
    pending = [{'decision': d, 'source': inputs.ref(addendum_path, f'/decisions/{i}')}
               for i, d in enumerate(addendum['decisions'])
               if d['dictionary_entry_id'] == entry_id or d['corpus_record_id'] in entry['corpus_refs']]

    # Hash real implementation/registry bytes, not a Git object pretending to represent local files.
    code = sorted(str(p.relative_to(inputs.root)) for p in (inputs.root / 'pictiq_renderer').glob('*.py'))
    code += ['tools/validate_message_schema.py', 'tools/replica_package.py']
    for path in code:
        inputs.take(path)
    registry_paths = ['lexicon/icon-index.json', 'lexicon/compatibility.json', 'entities/entity-index.json',
                      'notation/numeric/index.json', 'profiles/standalone-core-v0.1.json', 'profiles/embodied-core-v0.1.json']
    registry_paths += [str(p.relative_to(inputs.root)) for p in sorted((inputs.root / 'packs').glob('*.json'))]
    for path in registry_paths:
        inputs.take(path)
    registry = Registry(inputs.root)
    assets = []
    for fi, frame in enumerate(message['frames']):
        for ti, token in enumerate(frame['tokens']):
            kind = token.get('type')
            if kind == 'icon' and token.get('id') in registry.icon_entries:
                path = registry.icon_path(token['id'])
            elif kind == 'entity' and token.get('id') in registry.entity_entries:
                path = registry.entity_path(token['id'])
            elif kind == 'number' and token.get('value') in registry.implemented_numbers:
                path = registry.number_path(token['value'])
            else:
                continue  # Existing validation below supplies the diagnostic.
            assets.append({'frame': fi, 'token': ti, 'type': kind,
                           'original_id_or_value': token.get('id', token.get('value')),
                           **inputs.ref(str(path.relative_to(inputs.root)))})
    svg, validation = validate_and_render(message, registry)
    message_bytes = encode(message)
    if revision is None:
        revision = subprocess.check_output(['git', '-C', str(inputs.root), 'rev-parse', 'HEAD'], text=True).strip()
    identity = digest(encode({'entry_id': entry_id, 'variant_id': variant_id, 'message_sha256': digest(message_bytes)}))[:24]
    result = {
        'format': FORMAT, 'format_version': VERSION, 'package_id': 'replica-' + identity,
        'reference_git_revision': revision,
        'source': {**inputs.ref(relative), 'entry_id': entry_id, 'entry_selector': f'/entries/{ei}',
                   'variant_id': variant_id, 'variant_selector': f'/entries/{ei}/variants/{vi}',
                   'message_selector': f'/entries/{ei}/variants/{vi}/message',
                   'variant_provenance': variant['provenance']},
        'files': {'message': {'path': 'message.json', 'sha256': digest(message_bytes)},
                  'render': {'path': 'render.svg', 'sha256': digest(svg)}},
        'implementation': {'renderer': 'existing Python Renderer v0.1 / render_svg',
                           'render_options': vars(RenderOptions()),
                           'files': [inputs.ref(p) for p in code]},
        'registry_files': [inputs.ref(p) for p in registry_paths], 'canonical_assets': assets,
        'creator_decision': {'record': decision, 'source': inputs.ref(export_path, f'/records/{ri}')},
        'corpus_lineage': {'source': inputs.ref(corpus_path, f'/records/{ci}'),
                           'record_id': corpus_record['corpus_record_id'],
                           'provenance': corpus_record.get('provenance')},
        'source_constraints': {k: entry[k] for k in ('mode', 'surface', 'context', 'usage_note', 'known_ambiguity', 'context_warnings')},
        'variant_constraints': {k: variant[k] for k in ('variant_type', 'status', 'mode', 'surface', 'context', 'variant_context_note', 'semantic_distinction')},
        'source_qa': {'dictionary_version': dictionary['dictionary_version'], 'status': dictionary['status'],
                      'manifest_status': manifest['status'], 'subsequent_creator_decisions': pending,
                      'no_new_context_permission_inferred': True},
        'review_status': {'new_render': 'NOT_REVIEWED', 'final_placement': 'NOT_REVIEWED'},
        'validation_diagnostics': validation,
        'input_files': [{'path': p, 'sha256': digest(data)} for p, data in sorted(inputs.bytes.items())],
    }
    inputs.unchanged()
    return {'message.json': message_bytes, 'render.svg': svg, 'manifest.json': encode(result)}


def build(entry_id, variant_id, output, root=ROOT, revision=None):
    output = Path(output)
    if output.exists() or output.is_symlink():
        raise PackageError(f'Output already exists; refusing to overwrite: {output}')
    contents = compose(entry_id, variant_id, root, revision)
    output.parent.mkdir(parents=True, exist_ok=True)
    stage = Path(tempfile.mkdtemp(prefix='.replica-', dir=output.parent))
    try:
        for name, data in contents.items():
            (stage / name).write_bytes(data)
        # Reserve destination exclusively; never replace an existing directory, even an empty one.
        output.mkdir()
        try:
            for name in contents:
                os.rename(stage / name, output / name)
        except BaseException:
            shutil.rmtree(output)
            raise
    finally:
        shutil.rmtree(stage)
    return json.loads(contents['manifest.json'])


def verify(directory, root=ROOT):
    directory = Path(directory)
    manifest = json.loads((directory / 'manifest.json').read_bytes())
    if manifest.get('format') != FORMAT or manifest.get('format_version') != VERSION:
        raise PackageError('Unsupported package format/version')
    for key, name in [('message', 'message.json'), ('render', 'render.svg')]:
        ref = manifest['files'][key]
        if ref['path'] != name or digest((directory / name).read_bytes()) != ref['sha256']:
            raise PackageError(f'Integrity mismatch: {name}')
    for ref in manifest['input_files']:
        path = Inputs(root).path(ref['path'])
        if not path.is_file() or digest(path.read_bytes()) != ref['sha256']:
            raise PackageError(f'Required input version unavailable or changed: {ref["path"]}')
    expected = compose(manifest['source']['entry_id'], manifest['source']['variant_id'], root,
                       manifest['reference_git_revision'])
    for name in ('message.json', 'render.svg'):
        if (directory / name).read_bytes() != expected[name]:
            raise PackageError(f'{name} differs from the selected source / canonical Renderer output')
    if manifest != json.loads(expected['manifest.json']):
        raise PackageError('Manifest provenance, input bindings or review status differs from reproduced package')
    return {'ok': True, 'package_id': manifest['package_id'], 'review_status': manifest['review_status'],
            'note': 'Integrity/reproduction check only; not creator visual QA or placement approval.'}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    create = sub.add_parser('build'); create.add_argument('--entry-id', required=True)
    create.add_argument('--variant-id', required=True); create.add_argument('--output', type=Path, required=True)
    check = sub.add_parser('verify'); check.add_argument('directory', type=Path)
    args = parser.parse_args(argv)
    try:
        if args.command == 'build':
            manifest = build(args.entry_id, args.variant_id, args.output)
            result = {'ok': True, 'package_id': manifest['package_id'], 'review_status': manifest['review_status']}
        else:
            result = verify(args.directory)
    except (PackageError, OSError, ValueError, KeyError, TypeError, subprocess.CalledProcessError) as exc:
        print(json.dumps({'ok': False, 'error': str(exc)}, ensure_ascii=False)); return 1
    print(json.dumps(result, ensure_ascii=False)); return 0


if __name__ == '__main__':
    raise SystemExit(main())
