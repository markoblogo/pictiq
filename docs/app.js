/* Fully static lexicon search (no build step). */

const INDEX_URL = "../lexicon/icon-index.json";
const I18N_URL = (lang) => `../lexicon/i18n/${lang}.json`;

const $q = document.getElementById("q");
const $lang = document.getElementById("lang");
const $meta = document.getElementById("meta");
const $hint = document.getElementById("hint");
const $results = document.getElementById("results");

let baseIndex = null; // { icons: [...] }
let translations = null; // normalized map: { [id]: { meaning_en?, aliases_en?, tags_en?, examples? } }

function norm(s) {
  return (s || "").toString().toLowerCase();
}

function flattenText(entry) {
  const meaning = entry.meaning_en || "";
  const aliases = Array.isArray(entry.aliases_en) ? entry.aliases_en.join(" ") : "";
  const tags = Array.isArray(entry.tags_en) ? entry.tags_en.join(" ") : "";
  return norm(`${entry.id} ${meaning} ${aliases} ${tags}`);
}

function normalizeI18n(data) {
  // Supported shapes:
  // 1) { icons: { [id]: { meaning_en, aliases_en, tags_en, examples } } }
  // 2) { [id]: { meaning_en, aliases_en, tags_en, examples } }
  // 3) { icons: [ { id, meaning_en, aliases_en, tags_en, examples } ] }
  const out = {};
  if (!data || typeof data !== "object") return out;

  if (Array.isArray(data.icons)) {
    for (const e of data.icons) {
      if (e && typeof e === "object" && typeof e.id === "string") out[e.id] = e;
    }
    return out;
  }

  if (data.icons && typeof data.icons === "object") {
    for (const [id, v] of Object.entries(data.icons)) {
      if (v && typeof v === "object") out[id] = { id, ...v };
    }
    return out;
  }

  for (const [id, v] of Object.entries(data)) {
    if (v && typeof v === "object") out[id] = { id, ...v };
  }
  return out;
}

function mergedEntry(entry) {
  const t = translations && translations[entry.id];
  if (!t) return entry;

  // Swap labels/aliases (and tags/examples if provided by i18n).
  const merged = { ...entry };
  if (typeof t.meaning_en === "string") merged.meaning_en = t.meaning_en;
  if (Array.isArray(t.aliases_en)) merged.aliases_en = t.aliases_en;
  if (Array.isArray(t.tags_en)) merged.tags_en = t.tags_en;
  if (Array.isArray(t.examples)) merged.examples = t.examples;
  return merged;
}

function card(entry) {
  const e = mergedEntry(entry);
  const tags = Array.isArray(e.tags_en) ? e.tags_en : [];
  const examples = Array.isArray(e.examples) ? e.examples : [];
  const top3 = examples.slice(0, 3);

  const tagHtml = tags.map((t) => `<span class="tag">${escapeHtml(t)}</span>`).join("");
  const exHtml =
    top3.length > 0
      ? top3.map((x) => `<div class="ex">${escapeHtml(x)}</div>`).join("")
      : `<div class="ex">(no examples)</div>`;

  return `
    <article class="card">
      <div class="row">
        <div class="id">${escapeHtml(e.id)}</div>
      </div>
      <div class="meaning">${escapeHtml(e.meaning_en || "")}</div>
      <div class="tags">${tagHtml}</div>
      <div class="examples">${exHtml}</div>
    </article>
  `;
}

function escapeHtml(s) {
  return (s ?? "").toString().replace(/[&<>"']/g, (c) => {
    switch (c) {
      case "&":
        return "&amp;";
      case "<":
        return "&lt;";
      case ">":
        return "&gt;";
      case '"':
        return "&quot;";
      case "'":
        return "&#39;";
      default:
        return c;
    }
  });
}

function render() {
  if (!baseIndex) return;
  const icons = Array.isArray(baseIndex.icons) ? baseIndex.icons : [];

  const q = norm($q.value).trim();
  const filtered = q ? icons.filter((e) => flattenText(mergedEntry(e)).includes(q)) : icons;

  $meta.textContent = `${filtered.length} / ${icons.length} icons`;
  $results.innerHTML = filtered.map(card).join("");
}

async function loadIndex() {
  $meta.textContent = "Loading…";
  $hint.textContent = "";
  const res = await fetch(INDEX_URL, { cache: "no-store" });
  if (!res.ok) throw new Error(`failed to load index: ${res.status}`);
  const data = await res.json();
  baseIndex = data;
  render();
}

async function loadLang(lang) {
  translations = null;
  if (!lang || lang === "en") {
    $hint.textContent = "";
    render();
    return;
  }

  try {
    const res = await fetch(I18N_URL(lang), { cache: "no-store" });
    if (!res.ok) {
      translations = null;
      $hint.innerHTML = `<span class="warn">No i18n file for "${escapeHtml(lang)}" found.</span>`;
      render();
      return;
    }
    const data = await res.json();
    translations = normalizeI18n(data);
    $hint.textContent = "";
    render();
  } catch (err) {
    translations = null;
    $hint.innerHTML = `<span class="warn">Failed to load i18n for "${escapeHtml(lang)}".</span>`;
    render();
  }
}

function debounce(fn, ms) {
  let t = null;
  return (...args) => {
    if (t) clearTimeout(t);
    t = setTimeout(() => fn(...args), ms);
  };
}

async function boot() {
  try {
    await loadIndex();
  } catch (err) {
    $meta.textContent = "Failed to load lexicon index.";
    $hint.innerHTML =
      `<span class="warn">This page must be served over HTTP(S). If you opened it as a file, ` +
      `use a simple local server.</span>`;
    return;
  }

  await loadLang($lang.value);
}

$q.addEventListener("input", debounce(render, 40));
$lang.addEventListener("change", () => loadLang($lang.value));

boot();

