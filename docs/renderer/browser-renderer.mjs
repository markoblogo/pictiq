import { PICTIQ_BROWSER_ASSETS } from './generated/pictiq-browser-assets.mjs';

const DEFAULT_OPTIONS = Object.freeze({
  tileSize: 64,
  tokenGap: 8,
  frameGap: 16,
  padding: 16,
  direction: 'ltr',
});

const XML_DECL_RE = /^\s*<\?xml[^>]*>\s*/i;
const SVG_OPEN_RE = /^\s*<svg\b([^>]*)>/is;
const SVG_CLOSE_RE = /<\/svg>\s*$/is;
const VIEWBOX_RE = /viewBox="([^"]+)"/;

function escapeAttr(value) {
  return String(value)
    .replaceAll('&', '&amp;')
    .replaceAll('"', '&quot;')
    .replaceAll('<', '&lt;')
    .replaceAll('>', '&gt;');
}

export function layoutMessage(message, options = {}) {
  const opts = { ...DEFAULT_OPTIONS, ...options };
  const frames = message.frames || [];
  const maxTokens = Math.max(...frames.map((frame) => frame.tokens.length));
  const width = opts.padding * 2 + maxTokens * opts.tileSize + Math.max(0, maxTokens - 1) * opts.tokenGap;
  const height = opts.padding * 2 + frames.length * opts.tileSize + Math.max(0, frames.length - 1) * opts.frameGap;
  const laidOutFrames = frames.map((frame, frameIndex) => {
    const y = opts.padding + frameIndex * (opts.tileSize + opts.frameGap);
    const tokenCount = frame.tokens.length;
    const rowWidth = tokenCount * opts.tileSize + Math.max(0, tokenCount - 1) * opts.tokenGap;
    const x0 = opts.direction === 'rtl' ? width - opts.padding - rowWidth : opts.padding;
    return {
      tokens: frame.tokens.map((token, tokenIndex) => ({
        x: x0 + tokenIndex * (opts.tileSize + opts.tokenGap),
        y,
        width: opts.tileSize,
        height: opts.tileSize,
        token,
      })),
    };
  });
  return { width, height, frames: laidOutFrames };
}

function prefixInternalIds(svgInner, prefix) {
  const idMap = new Map();
  let out = svgInner.replace(/id=("|')([^"']+)("|')/g, (match, quote, value) => {
    const newValue = `${prefix}${value}`;
    idMap.set(value, newValue);
    return `id=${quote}${newValue}${quote}`;
  });
  for (const [oldValue, newValue] of idMap.entries()) {
    out = out.replaceAll(`url(#${oldValue})`, `url(#${newValue})`);
    out = out.replaceAll(`href="#${oldValue}"`, `href="#${newValue}"`);
    out = out.replaceAll(`href='#${oldValue}'`, `href='#${newValue}'`);
    out = out.replaceAll(`xlink:href="#${oldValue}"`, `xlink:href="#${newValue}"`);
    out = out.replaceAll(`xlink:href='#${oldValue}'`, `xlink:href='#${newValue}'`);
  }
  return out;
}

function nestedSvg(asset, x, y, size, color = '#000000', prefix = '') {
  const text = asset.svg.replace(XML_DECL_RE, '').trim();
  const match = SVG_OPEN_RE.exec(text);
  if (!match) throw new Error(`not an SVG asset: ${asset.path}`);
  const openTag = match[0];
  const viewBoxMatch = VIEWBOX_RE.exec(openTag);
  const viewBox = viewBoxMatch ? viewBoxMatch[1] : '0 0 32 32';
  let inner = text.slice(match.index + match[0].length).replace(SVG_CLOSE_RE, '').trim();
  inner = prefix ? prefixInternalIds(inner, prefix) : inner;
  return `<svg x="${x}" y="${y}" width="${size}" height="${size}" viewBox="${escapeAttr(viewBox)}" color="${escapeAttr(color)}">${inner}</svg>`;
}

function resolveAsset(token, assets) {
  if (token.type === 'icon') return assets.icons[token.id];
  if (token.type === 'entity') return assets.entities[token.id];
  if (token.type === 'number') return assets.numbers[String(token.value)];
  throw new Error(`unsupported token type: ${token.type}`);
}

function tokenDataId(token) {
  return token.id ?? token.value;
}

export function renderPictiqMessage(message, options = {}, assets = PICTIQ_BROWSER_ASSETS) {
  const layout = layoutMessage(message, options);
  const parts = [
    "<?xml version='1.0' encoding='utf-8'?>",
    `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${layout.width} ${layout.height}" width="${layout.width}" height="${layout.height}" role="img" aria-label="Pictiq rendered message">`,
    '<g id="pictiq-message" fill="none">',
  ];
  layout.frames.forEach((frame, frameIndex) => {
    parts.push(`<g class="pictiq-frame" data-frame="${frameIndex}">`);
    frame.tokens.forEach((item, tokenIndex) => {
      const token = item.token;
      const color = token.type === 'icon' ? token.params?.color || '#000000' : '#000000';
      const asset = resolveAsset(token, assets);
      if (!asset) throw new Error(`missing canonical asset for ${token.type}:${tokenDataId(token)}`);
      parts.push(`<g class="pictiq-token" data-type="${escapeAttr(token.type)}" data-id="${escapeAttr(tokenDataId(token))}">`);
      parts.push(nestedSvg(asset, item.x, item.y, item.width, color, `f${frameIndex}_t${tokenIndex}_`));
      parts.push('</g>');
    });
    parts.push('</g>');
  });
  parts.push('</g></svg>');
  return { format: 'svg', width: layout.width, height: layout.height, svg: `${parts.join('\n')}\n` };
}
