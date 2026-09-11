import { PICTIQ_COMPOSER_DATA } from './generated/pictiq-composer-data.mjs';

export const DATA = PICTIQ_COMPOSER_DATA;
export const PROFILES = new Set(['embodied', 'standalone', ...Object.keys(DATA.profiles)]);
export const CONTEXTS = new Set([...Object.keys(DATA.packs), 'narrative', 'odyssey']);
const ICON_RE = /^[a-z][a-z0-9]*(?:_[a-z0-9]+)*$/;
const ENTITY_RE = /^entity:[a-z0-9]+(?:-[a-z0-9]+)*@[a-z0-9]+(?:-[a-z0-9]+)*$/;
const COLOR_RE = /^#[0-9A-Fa-f]{6}$/;
const PARAM_RE = /^([a-z][a-z0-9]*(?:_[a-z0-9]+)*)\{([^{}]+)\}$/;
const NUMBER_RE = /^[0-9]+$/;

export const iconEntries = DATA.lexicon.icons || [];
export const iconById = Object.fromEntries(iconEntries.map((entry) => [entry.id, entry]));
export const entityEntries = DATA.entities.symbols || [];
export const entityById = Object.fromEntries(entityEntries.map((entry) => [entry.id, entry]));
export const implementedNumbers = new Set((DATA.numeric.implemented_numbers || []).map((entry) => Number(entry.value)));
export const legacyMap = Object.fromEntries((DATA.compatibility.migrations || [])
  .filter((entry) => entry.kind === 'SEMANTIC_MIGRATION' && entry.preferred_id)
  .map((entry) => [entry.legacy_id, entry.preferred_id]));

function slugify(value) {
  return String(value || '').toLowerCase().replace('entity:', '').replace('@', '-').replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
}

const entityAliases = new Map();
for (const entry of entityEntries) {
  const raw = [entry.id, entry.display_name || '', entry.slug || '', ...(entry.aliases || [])];
  for (const value of raw) {
    const key = slugify(value);
    if (!key) continue;
    if (!entityAliases.has(key)) entityAliases.set(key, []);
    if (!entityAliases.get(key).includes(entry.id)) entityAliases.get(key).push(entry.id);
  }
}

export function createDiagnostic(level, type, message, input = null, normalizedTo = null, location = null) {
  const out = { level, type, message };
  if (input !== null) out.input = input;
  if (normalizedTo !== null) out.normalizedTo = normalizedTo;
  if (location !== null) out.location = location;
  return out;
}

export function initialState() {
  return {
    message: { schema: '0.1', pictiq: '1.1', profile: 'standalone-core-v0.1', contexts: ['universal-core'], frames: [{ tokens: [] }] },
    selectedFrame: 0,
    selectedToken: null,
    diagnostics: [],
    importText: '',
    lastExport: '',
  };
}

export function compactMessage(message) {
  const frames = (message.frames || []).filter((frame) => Array.isArray(frame.tokens) && frame.tokens.length > 0).map((frame) => ({ tokens: frame.tokens }));
  const out = { schema: '0.1', pictiq: '1.1' };
  if (message.profile) out.profile = message.profile;
  if (Array.isArray(message.contexts) && message.contexts.length) out.contexts = [...new Set(message.contexts)];
  out.frames = frames;
  return out;
}

export function messageForEditing(message) {
  const clone = structuredClone(message || initialState().message);
  if (!Array.isArray(clone.frames) || clone.frames.length === 0) clone.frames = [{ tokens: [] }];
  return clone;
}

export function normalizeAndValidateMessage(data) {
  const diagnostics = [];
  if (!data || typeof data !== 'object' || Array.isArray(data)) {
    return { message: null, diagnostics: [createDiagnostic('error', 'unknown-id', 'Message must be a JSON object.')] };
  }
  const allowedDoc = new Set(['schema', 'pictiq', 'profile', 'contexts', 'frames']);
  for (const key of Object.keys(data)) if (!allowedDoc.has(key)) diagnostics.push(createDiagnostic('error', 'unknown-id', `Unexpected document property: ${key}`, key));
  if (data.schema !== '0.1') diagnostics.push(createDiagnostic('error', 'unknown-id', 'schema must be 0.1', String(data.schema)));
  if (data.pictiq !== '1.1') diagnostics.push(createDiagnostic('error', 'unknown-id', 'pictiq must be 1.1', String(data.pictiq)));

  const normalized = { schema: '0.1', pictiq: '1.1' };
  const profile = data.profile;
  if (profile !== undefined) {
    if (!PROFILES.has(profile)) diagnostics.push(createDiagnostic('error', 'profile-mismatch', `Invalid profile '${profile}'.`, String(profile)));
    else normalized.profile = profile;
  }
  let contexts = data.contexts || [];
  if (!Array.isArray(contexts) || contexts.some((x) => typeof x !== 'string')) {
    diagnostics.push(createDiagnostic('error', 'context-mismatch', 'contexts must be an array of strings.'));
    contexts = [];
  } else {
    for (const context of contexts) if (!CONTEXTS.has(context)) diagnostics.push(createDiagnostic('error', 'context-mismatch', `Invalid context '${context}'.`, context));
    contexts = [...new Set(contexts)];
    if (contexts.length) normalized.contexts = contexts;
  }
  if (!Array.isArray(data.frames) || data.frames.length === 0) {
    diagnostics.push(createDiagnostic('error', 'unknown-id', 'frames must be a non-empty array.'));
    return { message: null, diagnostics };
  }
  const normalizedFrames = [];
  data.frames.forEach((frame, frameIndex) => {
    if (!frame || typeof frame !== 'object' || Array.isArray(frame)) {
      diagnostics.push(createDiagnostic('error', 'illegal-grouping', 'Frame must be an object.', null, null, `frames[${frameIndex}]`));
      return;
    }
    for (const key of Object.keys(frame)) if (key !== 'tokens') diagnostics.push(createDiagnostic('error', 'illegal-grouping', `Frame property '${key}' is not allowed in v0.1.`, key, null, `frames[${frameIndex}]`));
    if (!Array.isArray(frame.tokens) || frame.tokens.length === 0) {
      diagnostics.push(createDiagnostic('error', 'unknown-id', 'Frame tokens must be a non-empty array.', null, null, `frames[${frameIndex}].tokens`));
      return;
    }
    const outTokens = [];
    frame.tokens.forEach((token, tokenIndex) => {
      const loc = `frames[${frameIndex}].tokens[${tokenIndex}]`;
      if (!token || typeof token !== 'object' || Array.isArray(token)) {
        diagnostics.push(createDiagnostic('error', 'illegal-grouping', 'Token must be an object; grouping is not supported.', null, null, loc));
        return;
      }
      if (token.type === 'icon') {
        let iconId = token.id;
        if (typeof iconId !== 'string' || !ICON_RE.test(iconId)) {
          diagnostics.push(createDiagnostic('error', 'unknown-id', 'Invalid icon id syntax.', String(iconId), null, loc));
          return;
        }
        if (legacyMap[iconId]) {
          diagnostics.push(createDiagnostic('warning', 'legacy-id', `Legacy id '${iconId}' normalized to '${legacyMap[iconId]}'.`, iconId, legacyMap[iconId], loc));
          iconId = legacyMap[iconId];
        }
        if (!iconById[iconId]) {
          diagnostics.push(createDiagnostic('error', 'unknown-id', `Unknown icon id '${iconId}'.`, iconId, null, loc));
          return;
        }
        const out = { type: 'icon', id: iconId };
        if (token.params !== undefined) {
          if (!token.params || typeof token.params !== 'object' || Array.isArray(token.params) || Object.keys(token.params).length === 0) {
            diagnostics.push(createDiagnostic('error', 'unsupported-parameter', 'params must be a non-empty object.', null, null, loc));
            return;
          }
          for (const [key, value] of Object.entries(token.params)) {
            if (key !== 'color' || typeof value !== 'string' || !COLOR_RE.test(value)) diagnostics.push(createDiagnostic('error', 'unsupported-parameter', `Unsupported or malformed parameter '${key}'.`, String(value), null, loc));
          }
          if (diagnostics.some((d) => d.level === 'error' && d.location === loc && d.type === 'unsupported-parameter')) return;
          out.params = { color: token.params.color };
        }
        outTokens.push(out);
      } else if (token.type === 'entity') {
        if (typeof token.id !== 'string' || !ENTITY_RE.test(token.id) || !entityById[token.id]) {
          diagnostics.push(createDiagnostic('error', 'unknown-id', `Unknown or invalid entity id '${token.id}'.`, String(token.id), null, loc));
          return;
        }
        outTokens.push({ type: 'entity', id: token.id });
      } else if (token.type === 'number') {
        const value = token.value;
        if (!Number.isInteger(value) || value < 0 || value > 9999 || !implementedNumbers.has(value)) {
          diagnostics.push(createDiagnostic('error', 'invalid-number', `Unsupported numeric notation value '${value}'.`, String(value), null, loc));
          return;
        }
        outTokens.push({ type: 'number', value });
      } else {
        diagnostics.push(createDiagnostic('error', 'unknown-id', `Unsupported token type '${token.type}'.`, String(token.type), null, loc));
      }
    });
    if (outTokens.length) normalizedFrames.push({ tokens: outTokens });
  });
  normalized.frames = normalizedFrames;
  return diagnostics.some((d) => d.level === 'error') ? { message: null, diagnostics } : { message: normalized, diagnostics };
}

export function parseJsonText(text) {
  try {
    return normalizeAndValidateMessage(JSON.parse(text));
  } catch (error) {
    return { message: null, diagnostics: [createDiagnostic('error', 'malformed-json', `Malformed JSON: ${error.message}.`)] };
  }
}

export function resolveEntityAlias(alias, contexts, location) {
  const key = slugify(alias.replace(/^@/, ''));
  const candidates = [...(entityAliases.get(key) || [])];
  if (!candidates.length) return { id: null, diagnostics: [createDiagnostic('error', 'unknown-id', `Unknown entity alias '@${key}'.`, alias, null, location)] };
  const filtered = candidates.filter((id) => contexts.includes(id.split('@').at(-1)));
  if (filtered.length === 1) return { id: filtered[0], diagnostics: [] };
  if (candidates.length === 1) return { id: candidates[0], diagnostics: [] };
  return { id: null, diagnostics: [createDiagnostic('error', 'ambiguous-entity', `Ambiguous entity alias '@${key}'.`, alias, null, location)] };
}

export function parseShorthandText(text) {
  const diagnostics = [];
  let profile = null;
  const contexts = [];
  const frames = [];
  String(text || '').replace(/\r\n?/g, '\n').split('\n').forEach((raw, index) => {
    const line = raw.trim();
    if (!line || line.startsWith('#')) return;
    const loc = `line ${index + 1}`;
    if (line.startsWith('!')) {
      const parts = line.split(/\s+/);
      if (parts.length !== 2 || !['!profile', '!context'].includes(parts[0])) {
        diagnostics.push(createDiagnostic('error', 'malformed-directive', `Malformed directive: ${line}`, line, null, loc));
        return;
      }
      if (parts[0] === '!profile') profile = parts[1];
      if (parts[0] === '!context' && !contexts.includes(parts[1])) contexts.push(parts[1]);
      return;
    }
    const tokens = [];
    line.split(/\s+/).forEach((unit, col) => {
      const tokenLoc = `${loc}, token ${col + 1}`;
      if (/[\[\]()]/.test(unit)) {
        diagnostics.push(createDiagnostic('error', 'illegal-grouping', `Grouping syntax is not supported in v0.1: ${unit}`, unit, null, tokenLoc));
        return;
      }
      if (NUMBER_RE.test(unit)) return tokens.push({ type: 'number', value: Number(unit) });
      if (ENTITY_RE.test(unit)) return tokens.push({ type: 'entity', id: unit });
      if (unit.startsWith('@')) {
        const resolved = resolveEntityAlias(unit, contexts, tokenLoc);
        diagnostics.push(...resolved.diagnostics);
        if (resolved.id) tokens.push({ type: 'entity', id: resolved.id });
        return;
      }
      const match = PARAM_RE.exec(unit);
      if (match) {
        const params = {};
        for (const piece of match[2].split(',')) {
          if (!piece.includes(':')) {
            diagnostics.push(createDiagnostic('error', 'unsupported-parameter', `Malformed parameter: ${piece}`, piece, null, tokenLoc));
            continue;
          }
          const [key, ...rest] = piece.split(':');
          params[key.trim()] = rest.join(':').trim();
        }
        const token = { type: 'icon', id: match[1] };
        if (Object.keys(params).length) token.params = params;
        tokens.push(token);
        return;
      }
      tokens.push({ type: 'icon', id: unit });
    });
    if (tokens.length) frames.push({ tokens });
  });
  const message = { schema: '0.1', pictiq: '1.1', frames };
  if (profile) message.profile = profile;
  if (contexts.length) message.contexts = contexts;
  if (diagnostics.some((d) => d.level === 'error')) return { message: null, diagnostics };
  const normalized = normalizeAndValidateMessage(message);
  return { message: normalized.message, diagnostics: [...diagnostics, ...normalized.diagnostics] };
}

export function serializeShorthand(message) {
  const { message: normalized, diagnostics } = normalizeAndValidateMessage(compactMessage(message));
  if (!normalized) return { text: '', diagnostics };
  const lines = [];
  if (normalized.profile) lines.push(`!profile ${normalized.profile}`);
  for (const context of normalized.contexts || []) lines.push(`!context ${context}`);
  if (lines.length) lines.push('');
  for (const frame of normalized.frames) {
    lines.push(frame.tokens.map((token) => {
      if (token.type === 'number') return String(token.value);
      if (token.type === 'entity') return token.id;
      if (token.type === 'icon' && token.params?.color) return `${token.id}{color:${token.params.color}}`;
      return token.id;
    }).join(' '));
  }
  return { text: `${lines.join('\n')}\n`, diagnostics };
}

export function searchPalette(query, selectedContexts = [], profile = 'standalone-core-v0.1') {
  const q = String(query || '').toLowerCase().trim();
  const contextIds = new Set(selectedContexts.flatMap((context) => DATA.packs[context]?.icons || []));
  const profileIds = new Set(DATA.profiles[profile]?.included_ids || []);
  const recommendedIds = new Set([...profileIds, ...contextIds]);
  return iconEntries.filter((entry) => {
    const hay = [entry.id, entry.meaning_en, entry.category, ...(entry.aliases_en || []), ...(entry.tags_en || [])].join(' ').toLowerCase();
    if (q) return hay.includes(q);
    return recommendedIds.has(entry.id);
  }).map((entry) => ({ ...entry, inSelectedContext: contextIds.has(entry.id), inProfile: profileIds.has(entry.id) }));
}

export function tokenLabel(token) {
  if (!token) return '';
  if (token.type === 'number') return String(token.value);
  if (token.type === 'entity') return entityById[token.id]?.display_name || token.id;
  return iconById[token.id]?.meaning_en || token.id;
}
