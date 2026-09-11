import { renderPictiqMessage } from '../renderer/browser-renderer.mjs';
import { CONTEXTS, DATA, addFrame, compactMessage, deleteFrameAt, deleteTokenAt, entityEntries, iconById, iconEntries, initialState, messageForEditing, moveFrame, moveToken, normalizeAndValidateMessage, parseJsonText, parseShorthandText, searchPalette, serializeShorthand, tokenLabel } from './composer-core.mjs';
import { PICTIQ_BROWSER_ASSETS } from '../renderer/generated/pictiq-browser-assets.mjs';

let state = initialState(); state.importDiagnostics = [];
let undoStack = [];
let redoStack = [];
let lastRender = null;
let dragState = null;
let pendingScrollFrame = null;

const $ = (id) => document.getElementById(id);
const els = Object.fromEntries(['profile','contexts','search','paletteItems','entityItems','frames','inspectorBody','diagnostics','previewSvg','jsonOut','shorthandOut','importText'].map((id) => [id, $(id)]));

const COLOR_SWATCHES = ['#000000', '#D32F2F', '#F57C00', '#FBC02D', '#388E3C', '#1976D2', '#7B1FA2', '#616161'];

const PROFILE_LABELS = {
  'standalone-core-v0.1': 'Standalone',
  embodied: 'Embodied',
  standalone: 'Standalone',
};
const CONTEXT_LABELS = {
  'city-paris-v0.1': 'Paris',
  'road-wayfinding-v0.1': 'Road / Wayfinding',
  'universal-core': 'Core',
  'universal-v1': 'Universal',
  narrative: 'Narrative',
  odyssey: 'Odyssey',
};

export function displayProfileLabel(id) { return PROFILE_LABELS[id] || String(id || '').replace(/-v\d+(?:\.\d+)*$/, '').replace(/-/g, ' ').replace(/\b\w/g, (c) => c.toUpperCase()); }
export function displayContextLabel(id) { return CONTEXT_LABELS[id] || String(id || '').replace(/-v\d+(?:\.\d+)*$/, '').replace(/-/g, ' ').replace(/\b\w/g, (c) => c.toUpperCase()); }

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
    for (const id of Object.keys(DATA.profiles)) els.profile.add(new Option(displayProfileLabel(id), id));
  }
  const profileValue = state.message.profile || 'standalone-core-v0.1';
  if (![...els.profile.options].some((option) => option.value === profileValue)) {
    els.profile.add(new Option(displayProfileLabel(profileValue), profileValue));
  }
  els.profile.value = profileValue;
  els.contexts.innerHTML = [...CONTEXTS].map((id) => `<label title="${escapeHtml(id)}"><input type="checkbox" value="${escapeHtml(id)}" ${state.message.contexts?.includes(id) ? 'checked' : ''}> <span class="context-name">${escapeHtml(displayContextLabel(id))}</span><span class="context-id">${escapeHtml(id)}</span></label>`).join('');
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
    <section class="frame ${frameIndex === state.selectedFrame ? 'active' : ''}" data-frame="${frameIndex}" data-frame-drop="${frameIndex}">
      <div class="frame-head" draggable="true" data-drag-frame="${frameIndex}" tabindex="0" role="button" aria-label="Frame ${frameIndex + 1}. Drag to reorder. Use Alt plus arrow keys to move.">
        <span>Frame ${frameIndex + 1}</span>
        <button class="frame-delete" type="button" data-frame-delete="${frameIndex}" aria-label="Delete frame ${frameIndex + 1}" title="Delete frame">×</button>
      </div>
      <div class="tokens" data-token-drop-frame="${frameIndex}" aria-label="Frame ${frameIndex + 1} tokens. Drop tiles here.">
        ${frame.tokens.length ? frame.tokens.map((token, tokenIndex) => {
          const label = tokenLabel(token);
          const id = token.type === 'number' ? String(token.value) : token.id;
          const tooltip = `${label} · ${id}`;
          return `
          <article class="token ${frameIndex === state.selectedFrame && tokenIndex === state.selectedToken ? 'selected' : ''}" draggable="true" data-drag-token="${frameIndex}:${tokenIndex}" title="${escapeHtml(tooltip)}">
            <button class="token-select" type="button" data-select-token="${frameIndex}:${tokenIndex}" aria-label="Select ${escapeHtml(tooltip)}. Drag to reorder. Use arrow keys to move, Delete to remove.">${assetSvgForToken(token)}<span class="sr-only">${escapeHtml(tooltip)}</span></button>
            <button class="token-delete" type="button" data-token-delete="${frameIndex}:${tokenIndex}" aria-label="Delete ${escapeHtml(label)}" title="Delete tile">×</button>
          </article>`; }).join('') : '<p class="palette-gloss empty-frame-note">Drop tiles here or add from the Palette.</p>'}
      </div>
    </section>`).join('');
}

function selectFrame(frameIndex) {
  state.selectedFrame = frameIndex;
  state.selectedToken = null;
  render();
}

function deleteFrame(frameIndex) {
  mutate(() => {
    state.selectedFrame = deleteFrameAt(state.message, frameIndex);
    state.selectedToken = null;
  });
}

function addFinalFrame() {
  mutate(() => {
    state.selectedFrame = addFrame(state.message);
    state.selectedToken = null;
    pendingScrollFrame = state.selectedFrame;
  });
}

function reorderFrame(fromFrame, toFrame) {
  mutate(() => {
    state.selectedFrame = moveFrame(state.message, fromFrame, toFrame);
    state.selectedToken = null;
  });
}

function removeToken(frameIndex, tokenIndex) {
  mutate(() => {
    const next = deleteTokenAt(state.message, frameIndex, tokenIndex);
    state.selectedFrame = next.frameIndex;
    state.selectedToken = next.tokenIndex;
  });
}

function moveSelectedToken(fromFrame, fromToken, toFrame, toToken) {
  mutate(() => {
    const next = moveToken(state.message, fromFrame, fromToken, toFrame, toToken);
    state.selectedFrame = next.frameIndex;
    state.selectedToken = next.tokenIndex;
  });
}

function tokenDropIndex(container, clientX) {
  const tokens = [...container.querySelectorAll('.token:not(.dragging)')];
  const after = tokens.findIndex((token) => clientX < token.getBoundingClientRect().left + token.getBoundingClientRect().width / 2);
  return after === -1 ? tokens.length : after;
}

function clearDragFeedback() {
  document.querySelectorAll('.drop-before,.drop-after,.frame-drop-before,.frame-drop-after').forEach((node) => node.classList.remove('drop-before','drop-after','frame-drop-before','frame-drop-after'));
}

function clearDraggingState() {
  document.querySelectorAll('.dragging').forEach((node) => node.classList.remove('dragging'));
}

function applyTokenDropFeedback(container, clientX) {
  clearDragFeedback();
  container.classList.add('drop-after');
  const tokens = [...container.querySelectorAll('.token:not(.dragging)')];
  const index = tokenDropIndex(container, clientX);
  const marker = tokens[index] || tokens[index - 1];
  if (marker) marker.classList.add(tokens[index] ? 'drop-before' : 'drop-after');
}

function frameDropIndex(frame, clientY) {
  const target = Number(frame.dataset.frameDrop);
  const rect = frame.getBoundingClientRect();
  let to = target + (clientY > rect.top + rect.height / 2 ? 1 : 0);
  if (dragState?.type === 'frame' && dragState.fromFrame < to) to -= 1;
  return Math.max(0, Math.min(to, state.message.frames.length - 1));
}

function applyFrameDropFeedback(frame, clientY) {
  clearDragFeedback();
  const rect = frame.getBoundingClientRect();
  frame.classList.add(clientY > rect.top + rect.height / 2 ? 'frame-drop-after' : 'frame-drop-before');
}

function renderInspector() {
  const token = currentFrame()?.tokens[state.selectedToken];
  if (!token) { els.inspectorBody.textContent = 'Choose a tile from the palette to start.'; return; }
  if (token.type === 'icon') {
    const entry = iconById[token.id] || {};
    const currentColor = token.params?.color || '#000000';
    const swatches = COLOR_SWATCHES.map((color) => `<button class="color-swatch" type="button" data-color-swatch="${color}" title="Use ${color}" aria-label="Use color ${color}" style="--swatch:${color}"></button>`).join('');
    els.inspectorBody.innerHTML = `
      <p><strong>${escapeHtml(entry.meaning_en || token.id)}</strong><br><code>${escapeHtml(token.id)}</code></p>
      <details class="color-editor">
        <summary>Color <span class="color-chip" style="--swatch:${escapeHtml(currentColor)}"></span>${token.params?.color ? escapeHtml(currentColor) : 'Default'}</summary>
        <div class="color-tools" aria-label="Color controls">
          <div class="color-swatches" aria-label="Quick color swatches">${swatches}</div>
          <label>Custom <input id="colorPicker" type="color" value="${escapeHtml(currentColor)}"></label>
          <label>HEX <input id="colorParam" type="text" value="${escapeHtml(currentColor)}" pattern="#[0-9A-Fa-f]{6}"></label>
          <div class="control-row color-actions">
            <button id="resetColor" type="button">Default</button>
            ${'EyeDropper' in window ? '<button id="eyeDropper" type="button">Eyedropper</button>' : ''}
          </div>
          <p class="palette-gloss">Swatches are authoring shortcuts, not semantic Pictiq colors.</p>
        </div>
      </details>`;
    function applyColor(value) {
      const color = String(value || '').trim();
      if (!/^#[0-9A-Fa-f]{6}$/.test(color)) return render();
      mutate(() => {
        if (color.toLowerCase() === '#000000') delete token.params;
        else token.params = { color: color.toUpperCase() };
      });
    }
    $('colorParam').addEventListener('change', (event) => applyColor(event.target.value));
    $('colorPicker').addEventListener('change', (event) => applyColor(event.target.value));
    for (const swatch of els.inspectorBody.querySelectorAll('[data-color-swatch]')) swatch.addEventListener('click', () => applyColor(swatch.dataset.colorSwatch));
    $('resetColor').addEventListener('click', () => mutate(() => delete token.params));
    const eyedropper = $('eyeDropper');
    if (eyedropper) eyedropper.addEventListener('click', async () => {
      try { const result = await new EyeDropper().open(); applyColor(result.sRGBHex); }
      catch { /* user cancelled or browser blocked the picker */ }
    });
  } else if (token.type === 'number') {
    els.inspectorBody.innerHTML = `<p><strong>Number</strong></p><label>Value <input id="numberValue" type="number" min="0" max="9999" value="${token.value}"></label><p class="palette-gloss">Current numeric notation supports 50.</p>`;
    $('numberValue').addEventListener('change', (event) => mutate(() => { token.value = Number(event.target.value); }));
  } else {
    els.inspectorBody.innerHTML = `<p><strong>${escapeHtml(tokenLabel(token))}</strong><br><code>${escapeHtml(token.id)}</code></p><p class="palette-gloss">Entity Symbol; no editable parameters in v0.1.</p>`;
  }
}

function renderPreview() {
  const compact = compactMessage(state.message);
  const hasTokens = state.message.frames?.some((frame) => frame.tokens?.length);
  if (!hasTokens) {
    els.diagnostics.innerHTML = '<div class="diag ok">Empty message. Choose a tile from the palette to start.</div>';
    els.previewSvg.innerHTML = '<p class="palette-gloss">Your Pictiq message preview will appear here.</p>';
    els.jsonOut.textContent = JSON.stringify(compact, null, 2);
    els.shorthandOut.textContent = '';
    lastRender = null;
    return;
  }
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

function render() {
  renderProfileContexts(); renderPalette(); renderFrames(); renderInspector(); renderPreview();
  if (pendingScrollFrame !== null) {
    const target = els.frames.querySelector(`[data-frame="${pendingScrollFrame}"]`);
    if (target) target.scrollIntoView({ block: 'nearest', behavior: 'smooth' });
    pendingScrollFrame = null;
  }
}

function setImported(result) {
  if (result.message) mutate(() => { state.message = messageForEditing(result.message); state.selectedFrame = 0; state.selectedToken = null; state.importDiagnostics = result.diagnostics; document.querySelector('.import-panel').open = false; });
  else { state.importDiagnostics = result.diagnostics; render(); }
}

document.addEventListener('click', (event) => {
  const frameHead = event.target.closest?.('[data-drag-frame]');
  if (frameHead && !event.target.closest('button')) selectFrame(Number(frameHead.dataset.dragFrame));
  const target = event.target.closest('button'); if (!target) return;
  if (target.dataset.addIcon) addToken({ type: 'icon', id: target.dataset.addIcon });
  if (target.dataset.addEntity) addToken({ type: 'entity', id: target.dataset.addEntity });
  if (target.dataset.selectToken) { const [f,t] = target.dataset.selectToken.split(':').map(Number); selectToken(f,t); }
  if (target.dataset.tokenDelete) { const [f,t] = target.dataset.tokenDelete.split(':').map(Number); removeToken(f,t); }
  if (target.dataset.frameDelete) deleteFrame(Number(target.dataset.frameDelete));
});

document.addEventListener('keydown', (event) => {
  const tokenButton = event.target.closest?.('[data-select-token]');
  if (tokenButton) {
    const [f,t] = tokenButton.dataset.selectToken.split(':').map(Number);
    if (event.key === 'Delete' || event.key === 'Backspace') { event.preventDefault(); removeToken(f,t); return; }
    if (event.altKey && event.key === 'ArrowLeft') { event.preventDefault(); moveSelectedToken(f,t,f,Math.max(0,t - 1)); return; }
    if (event.altKey && event.key === 'ArrowRight') { event.preventDefault(); moveSelectedToken(f,t,f,Math.min(state.message.frames[f].tokens.length - 1,t + 1)); return; }
  }
  const frameHead = event.target.closest?.('[data-drag-frame]');
  if (frameHead) {
    const f = Number(frameHead.dataset.dragFrame);
    if (event.altKey && event.key === 'ArrowUp') { event.preventDefault(); reorderFrame(f, Math.max(0, f - 1)); return; }
    if (event.altKey && event.key === 'ArrowDown') { event.preventDefault(); reorderFrame(f, Math.min(state.message.frames.length - 1, f + 1)); return; }
    if (event.key === 'Delete' || event.key === 'Backspace') { event.preventDefault(); deleteFrame(f); }
  }
});

document.addEventListener('dragstart', (event) => {
  const token = event.target.closest?.('[data-drag-token]');
  const frame = event.target.closest?.('[data-drag-frame]');
  if (token) {
    const [f,t] = token.dataset.dragToken.split(':').map(Number);
    dragState = { type: 'token', fromFrame: f, fromToken: t };
    event.dataTransfer.effectAllowed = 'move';
    event.dataTransfer.setData('text/plain', `token:${f}:${t}`);
    token.classList.add('dragging');
    return;
  }
  if (frame && !event.target.closest('button')) {
    const f = Number(frame.dataset.dragFrame);
    dragState = { type: 'frame', fromFrame: f };
    event.dataTransfer.effectAllowed = 'move';
    event.dataTransfer.setData('text/plain', `frame:${f}`);
    frame.closest('.frame')?.classList.add('dragging');
  }
});

document.addEventListener('dragover', (event) => {
  if (!dragState) return;
  if (dragState.type === 'token') {
    const container = event.target.closest?.('[data-token-drop-frame]');
    if (!container) return;
    event.preventDefault();
    event.dataTransfer.dropEffect = 'move';
    applyTokenDropFeedback(container, event.clientX);
  } else if (dragState.type === 'frame') {
    const frame = event.target.closest?.('[data-frame-drop]');
    if (!frame) return;
    event.preventDefault();
    event.dataTransfer.dropEffect = 'move';
    applyFrameDropFeedback(frame, event.clientY);
  }
});

document.addEventListener('drop', (event) => {
  if (!dragState) return;
  if (dragState.type === 'token') {
    const container = event.target.closest?.('[data-token-drop-frame]');
    if (!container) return;
    event.preventDefault();
    const toFrame = Number(container.dataset.tokenDropFrame);
    const toToken = tokenDropIndex(container, event.clientX);
    moveSelectedToken(dragState.fromFrame, dragState.fromToken, toFrame, toToken);
  } else if (dragState.type === 'frame') {
    const frame = event.target.closest?.('[data-frame-drop]');
    if (!frame) return;
    event.preventDefault();
    reorderFrame(dragState.fromFrame, frameDropIndex(frame, event.clientY));
  }
  dragState = null;
  clearDragFeedback();
  clearDraggingState();
});

document.addEventListener('dragend', () => { dragState = null; clearDragFeedback(); clearDraggingState(); });

els.profile.addEventListener('change', () => mutate(() => { state.message.profile = els.profile.value; }));
els.contexts.addEventListener('change', () => mutate(() => { state.message.contexts = [...els.contexts.querySelectorAll('input:checked')].map((x) => x.value); }));
els.search.addEventListener('input', renderPalette);
$('addNumber').addEventListener('click', () => addToken({ type: 'number', value: 50 }));
$('addFrame').addEventListener('click', addFinalFrame);
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
