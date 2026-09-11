#!/usr/bin/env node
import assert from 'node:assert/strict';
import { renderPictiqMessage } from '../../docs/renderer/browser-renderer.mjs';
import { compactMessage, initialState, normalizeAndValidateMessage, parseJsonText, parseShorthandText, searchPalette, serializeShorthand } from '../../docs/composer/composer-core.mjs';

function same(a, b) { assert.deepEqual(a, b); }
function noErrors(result) { assert.equal(result.diagnostics.filter((d) => d.level === 'error').length, 0, JSON.stringify(result.diagnostics)); }

let state = initialState();
assert.equal(state.message.schema, '0.1');
assert.equal(state.message.frames.length, 1);
assert.equal(state.message.frames[0].tokens.length, 0);

state.message.frames[0].tokens.push({ type: 'icon', id: 'need_water' }, { type: 'icon', id: 'punct_question' });
let normalized = normalizeAndValidateMessage(compactMessage(state.message));
noErrors(normalized);
assert.equal(normalized.message.frames[0].tokens.length, 2);

state.message.frames[0].tokens.splice(0, 1);
assert.equal(state.message.frames[0].tokens[0].id, 'punct_question');
state.message.frames[0].tokens.unshift({ type: 'icon', id: 'need_water' });
[state.message.frames[0].tokens[0], state.message.frames[0].tokens[1]] = [state.message.frames[0].tokens[1], state.message.frames[0].tokens[0]];
assert.equal(state.message.frames[0].tokens[0].id, 'punct_question');

state.message.frames.push({ tokens: [{ type: 'number', value: 50 }] });
normalized = normalizeAndValidateMessage(compactMessage(state.message));
noErrors(normalized);
assert.equal(normalized.message.frames.length, 2);

state.message.frames[1].tokens[0].value = 120;
normalized = normalizeAndValidateMessage(compactMessage(state.message));
assert.ok(normalized.diagnostics.some((d) => d.type === 'invalid-number' && d.level === 'error'));
state.message.frames[1].tokens[0].value = 50;

state.message.frames[1].tokens.push({ type: 'icon', id: 'nature_cloud', params: { color: '#555555' } });
normalized = normalizeAndValidateMessage(compactMessage(state.message));
noErrors(normalized);
const svg = renderPictiqMessage(normalized.message).svg;
assert.ok(svg.includes('data-id="50"'));
assert.ok(svg.includes('color="#555555"'));

let imported = parseJsonText('{"schema":"0.1","pictiq":"1.1","frames":[{"tokens":[{"type":"icon","id":"need_bar"}]}]}');
noErrors(imported);
assert.equal(imported.message.frames[0].tokens[0].id, 'drink_alcohol');
assert.ok(imported.diagnostics.some((d) => d.type === 'legacy-id'));

imported = parseShorthandText('!context odyssey\n@poseidon entity:polyphemus@odyssey\n50\nnature_cloud{color:#555555}\n');
noErrors(imported);
assert.equal(imported.message.frames[0].tokens[0].id, 'entity:poseidon@odyssey');
assert.equal(imported.message.frames[1].tokens[0].value, 50);

let exported = serializeShorthand(imported.message);
noErrors(exported);
assert.ok(exported.text.includes('entity:poseidon@odyssey'));
assert.ok(exported.text.includes('50'));
assert.ok(exported.text.includes('nature_cloud{color:#555555}'));
let reparsed = parseShorthandText(exported.text);
noErrors(reparsed);
same(reparsed.message, imported.message);

let bad = parseJsonText('{bad');
assert.ok(bad.diagnostics.some((d) => d.type === 'malformed-json' && d.level === 'error'));
let unknown = parseShorthandText('food_pizza\n');
assert.ok(unknown.diagnostics.some((d) => d.type === 'unknown-id' && d.level === 'error'));
let unsupported = parseJsonText('{"schema":"0.1","pictiq":"1.1","frames":[{"tokens":[{"type":"icon","id":"nature_cloud","params":{"tone":"grey"}}]}]}');
assert.ok(unsupported.diagnostics.some((d) => d.type === 'unsupported-parameter'));

assert.ok(searchPalette('water').some((entry) => entry.id === 'need_water'));
assert.ok(searchPalette('', ['universal-core'], 'standalone-core-v0.1').length < 83);
console.log('OK: Composer core semantics');
