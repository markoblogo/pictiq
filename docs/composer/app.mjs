import { renderPictiqMessage } from '../renderer/browser-renderer.mjs';
import { CONTEXTS, DATA, compactMessage, entityEntries, iconById, iconEntries, initialState, messageForEditing, normalizeAndValidateMessage, parseJsonText, parseShorthandText, searchPalette, serializeShorthand, tokenLabel } from './composer-core.mjs';
import { PICTIQ_BROWSER_ASSETS } from '../renderer/generated/pictiq-browser-assets.mjs';

let state = initialState(); state.importDiagnostics = [];
let undoStack = [];
let redoStack = [];
let lastRender = null;

const $ = (id) => document.getElementById(id);
const els = Object.fromEntries(['profile','contexts','search','paletteItems','entityItems','frames','inspectorBody','diagnostics','previewSvg','jsonOut','shorthandOut','importText'].map((id) => [id, $(id)]));

function clone(v) { return structuredClone(v); }
function escapeHtml(s) { return String(s ?? '').replace(/[&<>"']/g, (c) => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c])); }
function pushHistory() { undoStack.push(clone(state)); if (undoStack.length > 50) undoStack.shift(); redoStack = []; }
function mutate(fn) { pushHistory(); fn(); render(); }
function assetSvgForToken(token) {
  if (token.type === 'number') return PICTIQ_BROWSER_ASSETS.numbers[String(token.value)]?.svg || '';
  if (token.type === 'entity') return PICTIQ_BROWSER_ASSETS.entities[token.id]?.svg || '';
  return PICTIQ_BROWSER_ASSETS.icons[token.id]?.svg || '';
}
function download(name, type, text) {
  const url = URL.createObjectURL(new Blob([text], { type }));
  const a = document.createElement('a'); a.href = url; a.download = name; a.click(); URL.revokeObjectURL(url);
}
async function copyText(text) { try { await navigator.clipboard.writeText(text); } catch { window.prompt('Copy:', text); } }

function currentFrame() { return state.message.frames[state.selectedFrame] || state.message.frames[0]; }
function selectToken(frameIndex, tokenIndex) { state.selectedFrame = frameIndex; state.selectedToken = tokenIndex; render(); }
function addToken(token) { mutate(() => { currentFrame().tokens.push(clone(token)); state.selectedToken = currentFrame().tokens.length - 1; }); }

function renderProfileContexts() {
  if (!els.profile.options.length) {
    for (const id of Object.keys(DATA.profiles)) els.profile.add(new Option(id.replace('-core-v0.1',''), id));
  }
  els.profile.value = state.message.profile || 'standalone-core-v0.1';
  els.contexts.innerHTML = [...CONTEXTS].map((id) => `<label><input type="checkbox" value="${escapeHtml(id)}" ${state.message.contexts?.includes(id) ? 'checked' : ''}> ${escapeHtml(id)}</label>`).join('');
}

function renderPalette() {
  const selectedContexts = state.message.contexts || [];
  const items = searchPalette(els.search.value, selectedContexts, state.message.profile).slice(0, 80);
  els.paletteItems.innerHTML = items.map((entry) => `
    <button class="palette-card ${entry.inSelectedContext ? 'context' : ''}" type="button" data-add-icon="${escapeHtml(entry.id)}" title="${escapeHtml(entry.id)}">
      <span>${PICTIQ_BROWSER_ASSETS.icons[entry.id]?.svg || ''}</span>
      <span><span class="palette-title">${escapeHtml(entry.meaning_en || entry.id)}</span><span class="palette-gloss">${escapeHtml((entry.aliases_en || []).slice(0,3).join(', ') || entry.category || '')}</span></span>
      <span class="palette-id">${escapeHtml(entry.id)}</span>
    </button>`).join('');
  const allowEntities = selectedContexts.includes('odyssey') || selectedContexts.includes('narrative') || els.search.value.trim();
  els.entityItems.innerHTML = allowEntities ? entityEntries.filter((e) => {
    const hay = [e.id, e.display_name, e.namespace, ...(e.aliases || [])].join(' ').toLowerCase();
    return !els.search.value || hay.includes(els.search.value.toLowerCase());
  }).map((entry) => `
    <button class="palette-card" type="button" data-add-entity="${escapeHtml(entry.id)}" title="${escapeHtml(entry.id)}">
      <span>${PICTIQ_BROWSER_ASSETS.entities[entry.id]?.svg || ''}</span>
      <span><span class="palette-title">${escapeHtml(entry.display_name)}</span><span class="palette-gloss">${escapeHtml(entry.namespace)}</span></span>
      <span class="palette-id">entity</span>
    </button>`).join('') : '<p class="palette-gloss">Select Odyssey/Narrative context or search to show entities.</p>';
}

function renderFrames() {
  els.frames.innerHTML = state.message.frames.map((frame, frameIndex) => `
    <section class="frame ${frameIndex === state.selectedFrame ? 'active' : ''}" data-frame="${frameIndex}">
      <div class="frame-head">
        <button type="button" data-select-frame="${frameIndex}">Frame ${frameIndex + 1}</button>
        <div class="frame-actions">
          <button type="button" data-frame-up="${frameIndex}" aria-label="Move frame ${frameIndex + 1} up">↑</button>
          <button type="button" data-frame-down="${frameIndex}" aria-label="Move frame ${frameIndex + 1} down">↓</button>
        </div>
      </div>
      <div class="tokens">
        ${frame.tokens.length ? frame.tokens.map((token, tokenIndex) => `
          <article class="token ${frameIndex === state.selectedFrame && tokenIndex === state.selectedToken ? 'selected' : ''}">
            <button type="button" data-select-token="${frameIndex}:${tokenIndex}" aria-label="Select ${escapeHtml(tokenLabel(token))}">${assetSvgForToken(token)}</button>
            <div class="token-name">${escapeHtml(tokenLabel(token))}</div>
            <div class="token-actions">
              <button type="button" data-token-left="${frameIndex}:${tokenIndex}" aria-label="Move token left">←</button>
              <button type="button" data-token-right="${frameIndex}:${tokenIndex}" aria-label="Move token right">→</button>
              <button type="button" data-token-delete="${frameIndex}:${tokenIndex}" aria-label="Delete token">×</button>
            </div>
          </article>`).join('') : '<p class="palette-gloss">Add tiles from the palette.</p>'}
      </div>
    </section>`).join('');
}

function renderInspector() {
  const token = currentFrame()?.tokens[state.selectedToken];
  if (!token) { els.inspectorBody.textContent = 'Select a token.'; return; }
  if (token.type === 'icon') {
    const entry = iconById[token.id] || {};
    els.inspectorBody.innerHTML = `
      <p><strong>${escapeHtml(entry.meaning_en || token.id)}</strong><br><code>${escapeHtml(token.id)}</code></p>
      <label>COLOR parameter <input id="colorParam" type="text" value="${escapeHtml(token.params?.color || '#000000')}" pattern="#[0-9A-Fa-f]{6}"></label>
      <button id="clearColor" type="button">Clear color parameter</button>`;
    $('colorParam').addEventListener('change', (event) => mutate(() => {
      const value = event.target.value.trim();
      if (value && value !== '#000000') token.params = { color: value }; else delete token.params;
    }));
    $('clearColor').addEventListener('click', () => mutate(() => delete token.params));
  } else if (token.type === 'number') {
    els.inspectorBody.innerHTML = `<p><strong>Number</strong></p><label>Value <input id="numberValue" type="number" min="0" max="9999" value="${token.value}"></label><p class="palette-gloss">Current numeric notation supports 50.</p>`;
    $('numberValue').addEventListener('change', (event) => mutate(() => { token.value = Number(event.target.value); }));
  } else {
    els.inspectorBody.innerHTML = `<p><strong>${escapeHtml(tokenLabel(token))}</strong><br><code>${escapeHtml(token.id)}</code></p><p class="palette-gloss">Entity Symbol; no editable parameters in v0.1.</p>`;
  }
}

function renderPreview() {
  const compact = compactMessage(state.message);
  const normalized = normalizeAndValidateMessage(compact);
  const shownDiagnostics = [...(state.importDiagnostics || []), ...normalized.diagnostics];
  state.diagnostics = shownDiagnostics;
  const valid = Boolean(normalized.message);
  els.diagnostics.innerHTML = shownDiagnostics.length
    ? shownDiagnostics.map((d) => `<div class="diag ${d.level}"><strong>${escapeHtml(d.level.toUpperCase())}</strong> ${escapeHtml(d.message)}${d.location ? ` <code>${escapeHtml(d.location)}</code>` : ''}</div>`).join('')
    : `<div class="diag ok">No validation errors.</div>`;
  if (!valid) {
    els.previewSvg.innerHTML = '<p class="palette-gloss">Preview unavailable until the message is valid.</p>';
    els.jsonOut.textContent = JSON.stringify(compact, null, 2);
    els.shorthandOut.textContent = '';
    lastRender = null;
    return;
  }
  lastRender = renderPictiqMessage(normalized.message);
  els.previewSvg.innerHTML = lastRender.svg;
  els.jsonOut.textContent = JSON.stringify(normalized.message, null, 2);
  els.shorthandOut.textContent = serializeShorthand(normalized.message).text;
}

function render() { renderProfileContexts(); renderPalette(); renderFrames(); renderInspector(); renderPreview(); }

function setImported(result) {
  if (result.message) mutate(() => { state.message = messageForEditing(result.message); state.selectedFrame = 0; state.selectedToken = null; state.importDiagnostics = result.diagnostics; });
  else { state.importDiagnostics = result.diagnostics; render(); }
}

document.addEventListener('click', (event) => {
  const target = event.target.closest('button'); if (!target) return;
  if (target.dataset.addIcon) addToken({ type: 'icon', id: target.dataset.addIcon });
  if (target.dataset.addEntity) addToken({ type: 'entity', id: target.dataset.addEntity });
  if (target.dataset.selectFrame) { state.selectedFrame = Number(target.dataset.selectFrame); state.selectedToken = null; render(); }
  if (target.dataset.selectToken) { const [f,t] = target.dataset.selectToken.split(':').map(Number); selectToken(f,t); }
  if (target.dataset.tokenDelete) mutate(() => { const [f,t] = target.dataset.tokenDelete.split(':').map(Number); state.message.frames[f].tokens.splice(t,1); state.selectedFrame=f; state.selectedToken=null; });
  if (target.dataset.tokenLeft) mutate(() => { const [f,t] = target.dataset.tokenLeft.split(':').map(Number); if (t>0) [state.message.frames[f].tokens[t-1], state.message.frames[f].tokens[t]]=[state.message.frames[f].tokens[t], state.message.frames[f].tokens[t-1]]; state.selectedFrame=f; state.selectedToken=Math.max(0,t-1); });
  if (target.dataset.tokenRight) mutate(() => { const [f,t] = target.dataset.tokenRight.split(':').map(Number); const a=state.message.frames[f].tokens; if (t<a.length-1) [a[t+1], a[t]]=[a[t], a[t+1]]; state.selectedFrame=f; state.selectedToken=Math.min(a.length-1,t+1); });
  if (target.dataset.frameUp) mutate(() => { const f=Number(target.dataset.frameUp); if (f>0) [state.message.frames[f-1], state.message.frames[f]]=[state.message.frames[f], state.message.frames[f-1]]; state.selectedFrame=Math.max(0,f-1); state.selectedToken=null; });
  if (target.dataset.frameDown) mutate(() => { const f=Number(target.dataset.frameDown); if (f<state.message.frames.length-1) [state.message.frames[f+1], state.message.frames[f]]=[state.message.frames[f], state.message.frames[f+1]]; state.selectedFrame=Math.min(state.message.frames.length-1,f+1); state.selectedToken=null; });
});

els.profile.addEventListener('change', () => mutate(() => { state.message.profile = els.profile.value; }));
els.contexts.addEventListener('change', () => mutate(() => { state.message.contexts = [...els.contexts.querySelectorAll('input:checked')].map((x) => x.value); }));
els.search.addEventListener('input', renderPalette);
$('addNumber').addEventListener('click', () => addToken({ type: 'number', value: 50 }));
$('addFrame').addEventListener('click', () => mutate(() => { state.message.frames.push({ tokens: [] }); state.selectedFrame = state.message.frames.length - 1; state.selectedToken = null; }));
$('clearFrame').addEventListener('click', () => mutate(() => { currentFrame().tokens = []; state.selectedToken = null; }));
$('deleteFrame').addEventListener('click', () => mutate(() => { if (state.message.frames.length > 1) state.message.frames.splice(state.selectedFrame, 1); else state.message.frames = [{ tokens: [] }]; state.selectedFrame = Math.max(0, state.selectedFrame - 1); state.selectedToken = null; }));
$('newMessage').addEventListener('click', () => { if (confirm('Start a new message?')) mutate(() => { state = initialState(); state.importDiagnostics = []; }); });
$('undo').addEventListener('click', () => { if (!undoStack.length) return; redoStack.push(clone(state)); state = undoStack.pop(); render(); });
$('redo').addEventListener('click', () => { if (!redoStack.length) return; undoStack.push(clone(state)); state = redoStack.pop(); render(); });
$('importJson').addEventListener('click', () => setImported(parseJsonText(els.importText.value)));
$('importShorthand').addEventListener('click', () => setImported(parseShorthandText(els.importText.value)));
$('copyJson').addEventListener('click', () => copyText(els.jsonOut.textContent));
$('downloadJson').addEventListener('click', () => download('pictiq-message.json', 'application/json', els.jsonOut.textContent));
$('copyShorthand').addEventListener('click', () => copyText(els.shorthandOut.textContent));
$('downloadShorthand').addEventListener('click', () => download('pictiq-message.pictiq', 'text/plain', els.shorthandOut.textContent));
$('downloadSvg').addEventListener('click', () => { if (lastRender) download('pictiq-message.svg', 'image/svg+xml', lastRender.svg); });

render();
