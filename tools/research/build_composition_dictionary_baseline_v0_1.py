#!/usr/bin/env python3
"""Build the creator-reviewed Composition Dictionary Baseline v0.1.

All decisions come from the archived creator export. Ambiguous proposals are
kept in the amendment/follow-up records and are never guessed into Messages.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import html
import json
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "docs/research/composition-library-baseline-v0.1"
OUT = ROOT / "docs/research/composition-dictionary-baseline-v0.1"
ARCHIVE = OUT / "creator-review-export.json"
EXPECTED_SNAPSHOT = "clb-v0.1:33b00632bedb342af8aed35b62824b9b60663474bca556bb69e4ab16ea22d3e0"
EXPECTED_REVIEW_IDS = {
    "clh-v01-0002", "clh-v01-0007", "clh-v01-0011", "clh-v01-0017", "clh-v01-0022",
}
DECISIONS = {"KEEP_IN_DICTIONARY", "MOVE_TO_CORPUS_ONLY", "REVIEW_LATER", "EDIT_ENTRY_METADATA"}

NOTE_CLASSIFICATIONS: dict[str, list[str]] = {
    "clh-v01-0003": ["DISPLAY_METADATA_EDIT", "PREFERRED_COMPOSITION_CORRECTION", "SEMANTIC_CLARIFICATION", "TRANSLATOR_LESSON"],
    "clh-v01-0006": ["PREFERRED_COMPOSITION_CORRECTION", "TRANSLATOR_LESSON"],
    "clc-v01-0008-r1": ["CONTEXTUAL_VARIANT", "ALTERNATIVE_VARIANT", "TRANSLATOR_LESSON"],
    "clh-v01-0014": ["DISPLAY_METADATA_EDIT", "SEMANTIC_CLARIFICATION", "TRANSLATOR_LESSON"],
    "clh-v01-0016": ["ALTERNATIVE_VARIANT", "TRANSLATOR_LESSON"],
    "clh-v01-0044": ["DISPLAY_METADATA_EDIT", "CONTEXTUAL_VARIANT", "ALTERNATIVE_VARIANT", "SEMANTIC_CLARIFICATION", "TRANSLATOR_LESSON", "REQUIRES_FOLLOW_UP"],
    "clh-v01-0046": ["PREFERRED_COMPOSITION_CORRECTION", "TRANSLATOR_LESSON"],
    "clh-v01-0047": ["DISPLAY_METADATA_EDIT", "PREFERRED_COMPOSITION_CORRECTION", "SEMANTIC_CLARIFICATION", "TRANSLATOR_LESSON"],
    "clh-v01-0049": ["PREFERRED_COMPOSITION_CORRECTION", "TRANSLATOR_LESSON"],
    "clh-v01-0022": ["DISPLAY_METADATA_EDIT", "SEMANTIC_CLARIFICATION", "TRANSLATOR_LESSON", "REQUIRES_FOLLOW_UP"],
}

NOTE_PROCESSING: dict[str, dict[str, Any]] = {
    "clh-v01-0003": {"summary": "Use MEDICAL + URGENT as a live/self-referential practical expression; an explicit PERSON token adds a person referent. This does not define first-person grammar.", "actions": ["preferred Message changed", "explicit-person contextual variant retained"]},
    "clh-v01-0006": {"summary": "Prefer the existing direct food_meat primitive for the reusable meat meaning.", "actions": ["preferred Message changed to food_meat"]},
    "clc-v01-0008-r1": {"summary": "Keep SOUND + LESS preferred. Preserve DOWN and speech-specific combinations as labeled variants; communication/speech maps to the current comm_speak primitive.", "actions": ["one alternative variant", "two shouting/talking contextual variants"]},
    "clh-v01-0014": {"summary": "Scope this composition to general food shops, supermarkets, and general markets; specialized shop categories may need a matching existing primitive.", "actions": ["usage/context clarified", "no shop family generated"]},
    "clh-v01-0016": {"summary": "DOWN is an alternative to LESS for this reviewed food-quantity neighborhood only; no global equivalence is inferred.", "actions": ["one alternative variant"]},
    "clh-v01-0044": {"summary": "The accepted HERE + NO form is a narrow wayfinding message. Prohibition must retain its referent; the suggested UP/AHEAD concept does not resolve to one exact intended token.", "actions": ["headword/context narrowed", "referent-specific proposals retained as non-accepted candidates", "one exact-token follow-up"]},
    "clh-v01-0046": {"summary": "Use the creator's shorter FEET + NO form for this pedestrian prohibition entry.", "actions": ["preferred Message changed"]},
    "clh-v01-0047": {"summary": "Use PERSON + FEET for the reviewed pedestrian-movement neighborhood; do not imply a crossing-place relation without its token/context.", "actions": ["preferred Message changed", "headword/context narrowed"]},
    "clh-v01-0049": {"summary": "Use the creator's exact HERE + NO + CAR order for this no-parking entry; this is a local correction, not a general order rule.", "actions": ["preferred token order changed"]},
    "clh-v01-0022": {"summary": "Distinguish an arrival-time question from a timetable/schedule request; the latter's exact ordered composition remains unspecified.", "actions": ["headword/meaning clarified", "schedule proposal held for follow-up"]},
}

DISPLAY_OVERRIDES: dict[str, dict[str, Any]] = {
    "clh-v01-0003": {"headword": "Urgent medical help", "semantic_neighbourhood": "Urgent medical help; the live/self context can supply the affected person, while PERSON adds an explicit person referent.", "usage_note": "In live/self-referential use, the interaction may supply who needs help. Adding PERSON makes a person referent explicit and can shift the reading toward someone specified or other than the speaker. This is context economy, not a first-person grammatical rule.", "context_warnings": ["Live interaction may supply the affected person", "PERSON adds an explicit person referent"]},
    "clh-v01-0006": {"headword": "Meat", "semantic_neighbourhood": "Meat / meat food", "usage_note": "The accepted direct primitive food_meat is the preferred compact representation for this reusable meaning."},
    "clh-v01-0014": {"headword": "General food shop", "semantic_neighbourhood": "General grocery / food shop", "usage_note": "For a general food shop, supermarket, or general market. A specialized shop may require a matching existing food-category primitive; this note does not generate additional entries."},
    "clh-v01-0044": {"headword": "No entry at this location", "semantic_neighbourhood": "A location-specific wayfinding prohibition", "usage_note": "HERE + NO is source-bounded to a marked location/entry. It is not a universal translation for every prohibited action or object. Preserve the prohibited referent when it matters.", "context_warnings": ["Wayfinding context", "Context/referent-dependent; not a universal prohibition"]},
    "clh-v01-0047": {"headword": "Pedestrian movement", "semantic_neighbourhood": "Person moving on foot", "usage_note": "In a wayfinding context, PERSON + FEET indicates pedestrian movement; it does not by itself assert a crossing location.", "context_warnings": ["Wayfinding context", "Movement on foot is not necessarily a crossing-place relation"]},
    "clh-v01-0022": {"headword": "When does public transport arrive?", "semantic_neighbourhood": "A question about public-transport arrival time", "usage_note": "The creator's reading is approximately ‘When does the train/public transport arrive?’ or ‘When is the public transport?’ This is distinct from a timetable/schedule request, which remains unresolved.", "context_warnings": ["Arrival-time question; not a general timetable entry"]},
}


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def message_sequence(message: dict[str, Any]) -> str:
    return " / ".join(" + ".join(t.get("id", str(t.get("value", t.get("type")))) for t in f["tokens"]) for f in message["frames"])


def replace_tokens(message: dict[str, Any], ids: list[str]) -> dict[str, Any]:
    updated = copy.deepcopy(message)
    if len(updated["frames"]) != 1:
        raise ValueError("Creator-specified single-frame correction cannot be applied to a multi-frame source")
    updated["frames"] = [{"tokens": [{"type": "icon", "id": icon_id} for icon_id in ids]}]
    return updated


def validate_review(review: dict[str, Any], candidate: dict[str, Any], eligibility: dict[str, Any], corpus: dict[str, Any]) -> None:
    expected = {
        "review_type": "PICTIQ_DICTIONARY_CREATOR_ELIGIBILITY_REVIEW",
        "review_version": "0.1",
        "corpus_baseline_version": "0.1",
        "dictionary_candidate_version": "0.1",
        "source_snapshot": EXPECTED_SNAPSHOT,
        "total_records": 65,
        "reviewed_records": 65,
    }
    for key, value in expected.items():
        if review.get(key) != value:
            raise ValueError(f"review binding mismatch at {key}: expected {value!r}, got {review.get(key)!r}")
    rows = review.get("records")
    if not isinstance(rows, list) or len(rows) != 65:
        raise ValueError("review export must contain exactly 65 records")
    ids = [row.get("corpus_record_id") for row in rows]
    if len(ids) != len(set(ids)):
        raise ValueError("creator review has duplicate Corpus IDs")
    corpus_ids = {r["corpus_record_id"] for r in corpus["records"]}
    candidate_by_corpus = {cid: entry for entry in candidate["entries"] for cid in entry["corpus_record_ids"]}
    eligibility_by = {r["corpus_record_id"]: r for r in eligibility["records"]}
    expected_ids = set(candidate_by_corpus) | EXPECTED_REVIEW_IDS
    if set(ids) != expected_ids:
        raise ValueError(f"review IDs differ from the 60 candidate + 5 former REVIEW IDs; missing={sorted(expected_ids-set(ids))}, unknown={sorted(set(ids)-expected_ids)}")
    if set(ids) - corpus_ids:
        raise ValueError(f"creator review references unknown Corpus IDs: {sorted(set(ids)-corpus_ids)}")
    for row in rows:
        cid = row["corpus_record_id"]
        source = eligibility_by.get(cid)
        if not source or source["eligibility"] not in {"YES", "REVIEW"}:
            raise ValueError(f"not an eligible review unit: {cid}")
        expected_entry = candidate_by_corpus.get(cid, {}).get("dictionary_entry_id")
        if row.get("dictionary_entry_id") != expected_entry:
            raise ValueError(f"candidate ID mismatch for {cid}")
        if row.get("system_eligibility") != source["eligibility"]:
            raise ValueError(f"system eligibility mismatch for {cid}")
        if row.get("creator_decision") not in DECISIONS:
            raise ValueError(f"unreviewed or invalid creator decision for {cid}")
        if not isinstance(row.get("creator_notes", ""), str):
            raise ValueError(f"creator notes must be text for {cid}")


def context_data(record: dict[str, Any], candidate_entry: dict[str, Any] | None) -> list[dict[str, Any]]:
    if candidate_entry:
        for variant in candidate_entry["variants"]:
            if record["corpus_record_id"] in candidate_entry["corpus_record_ids"]:
                return copy.deepcopy(variant.get("context", []))
    return copy.deepcopy(record.get("applicability", []))


def make_note_classification(row: dict[str, Any]) -> dict[str, Any] | None:
    note = row.get("creator_notes", "")
    if not note.strip():
        return None
    cid = row["corpus_record_id"]
    return {
        "source_review_record_id": cid,
        "original_creator_note": note,
        "classifications": NOTE_CLASSIFICATIONS[cid],
        "structured_interpretation": NOTE_PROCESSING[cid]["summary"],
        "processing_actions": NOTE_PROCESSING[cid]["actions"],
    }


def build_variant(entry_id: str, variant_id: str, kind: str, message: dict[str, Any], corpus_ids: list[str], context: list[dict[str, Any]], meaning: str, note_ref: str | None = None, extra_context: str | None = None) -> dict[str, Any]:
    return {
        "variant_id": variant_id,
        "variant_type": kind,
        "status": "CURRENT_ACCEPTED",
        "message": message,
        "token_sequence": message_sequence(message),
        "render": f"renders/{variant_id}.svg",
        "mode": sorted({x.get("communication_mode", "STANDALONE") for x in context}),
        "surface": sorted({x.get("communication_surface", "OTHER") for x in context}),
        "context": context,
        "variant_context_note": extra_context,
        "semantic_distinction": meaning,
        "provenance": {
            "corpus_record_ids": corpus_ids,
            "creator_review_record_id": note_ref,
            "dictionary_entry_id": entry_id,
            "authority": "ACCEPTED_CORPUS_MESSAGE" if note_ref is None else "EXPLICIT_CREATOR_DICTIONARY_REVIEW",
        },
    }


def html_escape(value: Any) -> str:
    return html.escape(str(value if value is not None else ""), quote=True)


DICTIONARY_SEARCH_JS = r"""
function dictionaryMatch(entry, query) {
  const q = query.toLowerCase();
  if (!q) return {matched: true, groups: [], reason: ''};
  // Keep the existing search surface, including serialized metadata, unchanged.
  const matched = JSON.stringify({headword: entry.headword, aliases: entry.aliases,
    lookup: entry.candidate_lookup_material, meaning: entry.semantic_neighbourhood,
    variants: entry.variants.map(v => v.token_sequence)}).toLowerCase().includes(q);
  if (!matched) return {matched: false, groups: [], reason: ''};
  const includes = values => values.some(value => String(value ?? '').toLowerCase().includes(q));
  const groups = [];
  if (includes([entry.headword, ...entry.aliases])) groups.push('title_aliases');
  if (includes(entry.variants.map(v => v.token_sequence))) groups.push('token_sequences');
  if (includes([...entry.candidate_lookup_material, entry.semantic_neighbourhood])) groups.push('related');
  const labels = {title_aliases: 'title / aliases', token_sequences: 'token sequences / IDs', related: 'related materials'};
  let reason = groups.length ? 'Match in ' + groups.map(g => labels[g]).join('; ')
    : 'Match in search metadata or combined field text';
  if (!groups.includes('title_aliases')) reason += '; title and aliases did not match';
  return {matched, groups, reason: reason + '.'};
}
function dictionaryRows(entries, q, mode, surface, variants, contextual, ambiguity) {
  return entries.filter(x => dictionaryMatch(x, q).matched &&
    (!mode || x.mode.includes(mode)) && (!surface || x.surface.includes(surface)) &&
    (!variants || x.variants.length > 1) && (!contextual || x.context_warnings.length > 0) &&
    (!ambiguity || x.known_ambiguity.length > 0));
}
"""


def make_dictionary_viewer(entries: list[dict[str, Any]]) -> str:
    payload = json.dumps(entries, ensure_ascii=False, separators=(",", ":")).replace("<", "\\u003c")
    return f'''<!doctype html>
<html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Composition Dictionary Baseline v0.1</title>
<style>body{{font:16px/1.5 system-ui,-apple-system,sans-serif;color:#161616;max-width:1100px;margin:24px auto;padding:0 16px}}h1{{margin-bottom:.2em}}.boundary{{padding:12px;border:1px solid #333;margin:16px 0}}header{{position:sticky;top:0;background:#fff;padding:10px 0;border-bottom:1px solid #aaa;z-index:2}}input,select{{font:inherit;padding:8px;margin:4px}}#count{{font-weight:650}}article{{border-bottom:1px solid #aaa;padding:20px 0}}.entry{{display:grid;grid-template-columns:minmax(240px,420px) 1fr;gap:24px}}.render{{max-width:100%;max-height:220px;object-fit:contain;object-position:left center}}h2{{margin:.2em 0}}.variant{{margin:12px 0;padding:10px;background:#f5f5f5}}.tag{{font-size:.85em;font-weight:700}}.warning{{padding:9px 12px;border-left:4px solid #8a4d00;background:#fff8eb;margin:8px 0}}code{{overflow-wrap:anywhere}}details{{margin-top:10px}}pre{{white-space:pre-wrap;overflow-wrap:anywhere}}@media(max-width:700px){{.entry{{grid-template-columns:1fr}}}}</style>
<body><h1>Composition Dictionary</h1><p>Creator-reviewed internal research reference · Baseline v0.1 · not deployed.</p>
<div class="boundary"><strong>Evidence-bounded use:</strong> A Dictionary entry is a reusable semantic unit with one or more context-bounded Pictiq representations. It is not an English phrase equated with one universal sequence. English headwords are lookup labels.</div>
<header><input id="q" type="search" placeholder="Search headword, wording, or token ID"><label>Mode <select id="mode"><option value="">All</option><option>EMBODIED</option><option>STANDALONE</option></select></label><label>Surface <select id="surface"><option value="">All</option></select></label><label><input id="variants" type="checkbox"> has variants</label><label><input id="contextual" type="checkbox"> context-dependent</label><label><input id="ambiguity" type="checkbox"> known ambiguity</label><span id="count"></span><p id="search-limit" hidden>Search reasons describe text matches only; they do not establish semantic equivalence or complete QA.</p></header><main id="entries"></main>
<script>const D={payload};const $=x=>document.getElementById(x),esc=x=>String(x??"").replace(/[&<>]/g,c=>({{"&":"&amp;","<":"&lt;",">":"&gt;"}}[c])).replaceAll(String.fromCharCode(34),"&quot;").replaceAll(String.fromCharCode(39),"&#39;");{DICTIONARY_SEARCH_JS}const surfaces=[...new Set(D.flatMap(x=>x.surface))].sort();for(const s of surfaces){{const o=document.createElement("option");o.textContent=s;o.value=s;$("surface").append(o)}}function draw(){{const q=$("q").value.toLowerCase(),m=$("mode").value,s=$("surface").value,v=$("variants").checked,c=$("contextual").checked,a=$("ambiguity").checked;const rows=dictionaryRows(D,q,m,s,v,c,a);$("search-limit").hidden=!q;$("count").textContent=` ${{rows.length}} / ${{D.length}}`;$("entries").innerHTML=rows.map(x=>`<article><div class="entry"><div><h2>${{esc(x.headword)}}</h2>${{q?`<p class="match-reason">${{esc(dictionaryMatch(x,q).reason)}}</p>`:""}}<p><strong>Meaning:</strong> ${{esc(x.semantic_neighbourhood)}}</p><img class="render" src="../${{esc(x.preferred_variant.render)}}" alt="${{esc(x.headword)}} Pictiq composition"><p class="tag">Preferred</p><p><code>${{esc(x.preferred_variant.token_sequence)}}</code></p></div><div>${{x.context_warnings.map(w=>`<p class="warning">${{esc(w)}}</p>`).join("")}}${{x.known_ambiguity.map(w=>`<p class="warning"><strong>Known ambiguity:</strong> ${{esc(w)}}</p>`).join("")}}<p><strong>Used when / context:</strong> ${{esc(JSON.stringify(x.context))}}</p>${{x.usage_note?`<p>${{esc(x.usage_note)}}</p>`:""}}${{x.aliases.length?`<p><strong>Aliases:</strong> ${{esc(x.aliases.join("; "))}}</p>`:""}}${{x.variants.slice(1).map(y=>`<div class="variant"><p class="tag">${{esc(y.variant_type==='ALTERNATIVE'?'Alternative':'Contextual')}}</p><img class="render" src="../${{esc(y.render)}}" alt="${{esc(y.variant_type)}} variant"><p><code>${{esc(y.token_sequence)}}</code></p><p>${{esc(y.semantic_distinction)}} ${{esc(y.variant_context_note||"")}}</p></div>`).join("")}}<details><summary>History / evidence / technical details</summary><p>Token IDs: ${{esc(x.variants.map(y=>y.token_sequence).join("; "))}}</p><p>Corpus: ${{x.corpus_refs.map(r=>`<a href="../../composition-library-baseline-v0.1/review/corpus.html#${{esc(r)}}">${{esc(r)}}</a>`).join(", ")}}</p><p>Source evidence: ${{esc(x.source_evidence_summary.join("; "))}}</p><p>Known ambiguity: ${{esc(x.known_ambiguity.join("; ")||"None recorded")}}</p><pre>${{esc(JSON.stringify({{lineage:x.lineage,creator_review:x.creator_review,system_candidate_history:x.system_candidate_history}},null,2))}}</pre></details></div></div></article>`).join("")}}for(const id of ["q","mode","surface","variants","contextual","ambiguity"])$(id).addEventListener("input",draw);draw();</script></body></html>'''


def make_followup_viewer(items: list[dict[str, Any]]) -> str:
    data = json.dumps(items, ensure_ascii=False, separators=(",", ":")).replace("<", "\\u003c")
    return f'''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Creator Notes Follow-up</title><style>body{{font:16px/1.5 system-ui;max-width:900px;margin:24px auto;padding:0 16px}}article{{border-top:1px solid #aaa;padding:16px 0}}.question{{padding:10px;background:#f5f5f5}}</style><h1>Creator-notes follow-up</h1><p>Only note portions that could not safely become accepted Dictionary metadata or exact variants are listed. Current accepted entries remain usable where stated.</p><main id="items"></main><script>const D={data};const esc=s=>String(s??"").replace(/[&<>]/g,c=>({{"&":"&amp;","<":"&lt;",">":"&gt;"}}[c]));document.getElementById("items").innerHTML=D.map(x=>`<article><h2>${{esc(x.corpus_record_id)}} · ${{esc(x.dictionary_entry_id)}}</h2><p><strong>Creator note (verbatim):</strong> ${{esc(x.original_creator_note)}}</p><p><strong>Current preferred:</strong> ${{esc(x.current_preferred_sequence)}}</p><p><strong>Can be inferred:</strong> ${{esc(x.safe_inference)}}</p><p><strong>Cannot be inferred:</strong> ${{esc(x.unresolved)}}</p><p class="question"><strong>Creator question:</strong> ${{esc(x.creator_question)}}</p></article>`).join("");</script></html>'''


def make_qa_viewer(groups: dict[str, list[dict[str, Any]]]) -> str:
    payload = json.dumps(groups, ensure_ascii=False, separators=(",", ":")).replace("<", "\\u003c")
    return f'''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Composition Dictionary v0.1 — final creator visual QA</title><style>body{{font:15px/1.45 system-ui;max-width:1200px;margin:22px auto;padding:0 14px}}.boundary{{padding:10px;border:1px solid #333}}section{{margin:24px 0}}article{{border-top:1px solid #aaa;padding:16px 0}}.pair{{display:grid;grid-template-columns:1fr 1fr;gap:20px}}img{{width:100%;max-height:220px;object-fit:contain;object-position:left center}}.note{{background:#f4f4f4;padding:10px}}.tag{{font-weight:700}}@media(max-width:650px){{.pair{{grid-template-columns:1fr}}}}</style><h1>Dictionary Baseline v0.1 — creator visual QA</h1><p class="boundary">Prepared for creator review only. No visual acceptance is recorded here. Review changed preferred forms, metadata/context and promoted former REVIEW items.</p><main id="groups"></main><script>const G={payload};const esc=s=>String(s??"").replace(/[&<>]/g,c=>({{"&":"&amp;","<":"&lt;",">":"&gt;"}}[c]));document.getElementById("groups").innerHTML=Object.entries(G).map(([name,items])=>`<section><h2>${{esc(name)}}</h2>${{items.map(x=>`<article><h3>${{esc(x.corpus_record_id)}} · ${{esc(x.headword)}}</h3><div class="pair"><div><p class="tag">BEFORE — candidate/corpus source</p><img src="${{esc(x.before_render)}}"><p><code>${{esc(x.before_sequence)}}</code></p></div><div><p class="tag">AFTER — current preferred</p><img src="${{esc(x.after_render)}}"><p><code>${{esc(x.after_sequence)}}</code></p></div></div>${{x.note?`<p class="note"><strong>Creator note:</strong> ${{esc(x.note)}}</p>`:""}}<p><strong>Structured interpretation:</strong> ${{esc(x.interpretation)}}</p><details><summary>Lineage</summary><pre>${{esc(JSON.stringify(x.lineage,null,2))}}</pre></details></article>`).join("")}}</section>`).join("");</script></html>'''


def build(output_dir: Path = OUT) -> dict[str, Any]:
    candidate = read_json(SOURCE / "dictionary-candidate.json")
    eligibility = read_json(SOURCE / "dictionary-eligibility.json")
    corpus = read_json(SOURCE / "accepted-corpus.json")
    source_manifest = read_json(SOURCE / "manifest.json")
    review_bytes = (output_dir / "creator-review-export.json").read_bytes()
    review = json.loads(review_bytes)
    export_sha = sha256_bytes(review_bytes)
    expected_snapshot = EXPECTED_SNAPSHOT
    hashes = source_manifest["artifact_sha256"]
    bound = "\n".join(["0.1"] + [f"{name}:{hashes[name]}" for name in ("accepted-corpus.json", "dictionary-candidate.json", "dictionary-eligibility.json")])
    computed_snapshot = "clb-v0.1:" + sha256_bytes(bound.encode())
    if computed_snapshot != expected_snapshot:
        raise ValueError(f"frozen candidate snapshot mismatch: {computed_snapshot}")
    for name in ("accepted-corpus.json", "dictionary-candidate.json", "dictionary-eligibility.json"):
        if sha256_bytes((SOURCE / name).read_bytes()) != hashes[name]:
            raise ValueError(f"frozen input changed from manifest: {name}")
    validate_review(review, candidate, eligibility, corpus)

    sys.path.insert(0, str(ROOT))
    from pictiq_renderer.registry import Registry  # noqa: PLC0415
    from pictiq_renderer.svg_renderer import render_svg  # noqa: PLC0415
    from tools.validate_message_schema import schema_errors, semantic_errors  # noqa: PLC0415

    registry = Registry()
    corpus_by = {r["corpus_record_id"]: r for r in corpus["records"]}
    eligibility_by = {r["corpus_record_id"]: r for r in eligibility["records"]}
    candidate_by = {cid: entry for entry in candidate["entries"] for cid in entry["corpus_record_ids"]}
    review_by = {r["corpus_record_id"]: r for r in review["records"]}
    icons = set(registry.icon_entries)
    for required in ("safety_medical", "punct_exclaim", "person_generic", "food_meat", "comm_sound", "comm_speak", "qty_minus", "rel_down", "move_feet", "logic_no", "move_car", "rel_here", "move_public", "time", "punct_question", "media_text"):
        if required not in icons:
            raise ValueError(f"creator-mentioned primitive is not in current registry: {required}")

    # Current generic core registries remain read-only inputs. New promoted IDs
    # use stable Corpus identity; English never serves as a primary identifier.
    new_review_ids = sorted(EXPECTED_REVIEW_IDS)
    new_ids = {cid: f"pcd-v01-{61+i:04d}" for i, cid in enumerate(new_review_ids)}
    source_ids = sorted(review_by, key=lambda cid: (candidate_by[cid]["dictionary_entry_id"] if cid in candidate_by else new_ids[cid]))
    entries: list[dict[str, Any]] = []
    all_variants: list[dict[str, Any]] = []
    amendment_records: list[dict[str, Any]] = []
    lineage_records: list[dict[str, Any]] = []
    render_results: list[dict[str, Any]] = []
    candidate_variant_links: dict[str, dict[str, Any]] = {}
    for cid, entry in candidate_by.items():
        for variant in entry["variants"]:
            candidate_variant_links[variant["corpus_record_id"]] = variant

    for cid in source_ids:
        row = review_by[cid]
        source_record = corpus_by[cid]
        old_entry = candidate_by.get(cid)
        old_variant = candidate_variant_links.get(cid)
        dictionary_id = old_entry["dictionary_entry_id"] if old_entry else new_ids[cid]
        semantic_number = int(dictionary_id.rsplit("-", 1)[1])
        current_message = copy.deepcopy(old_variant["message"] if old_variant else source_record.get("message") or source_record.get("historical_message"))
        if not current_message:
            raise ValueError(f"no current accepted Message for {cid}")
        current_sequence_before = message_sequence(current_message)
        preferred_ids: dict[str, list[str]] = {
            "clh-v01-0003": ["safety_medical", "punct_exclaim"],
            "clh-v01-0006": ["food_meat"],
            "clh-v01-0046": ["move_feet", "logic_no"],
            "clh-v01-0047": ["person_generic", "move_feet"],
            "clh-v01-0049": ["rel_here", "logic_no", "move_car"],
        }
        preferred_changed = cid in preferred_ids
        if preferred_changed:
            current_message = replace_tokens(current_message, preferred_ids[cid])
        token_context = old_variant.get("context", []) if old_variant else copy.deepcopy(source_record.get("applicability", []))
        raw_intent = old_entry.get("semantic_neighbourhood") if old_entry else next((x.get("canonical_intent") for x in source_record.get("semantic_neighbourhoods", []) if x.get("canonical_intent")), row.get("intent", ""))
        entry = {
            "dictionary_entry_id": dictionary_id,
            "semantic_id": f"pictiq-dict-sem-v0.1-{semantic_number:04d}",
            "headword": old_entry.get("headword") if old_entry else row.get("intent", raw_intent),
            "aliases": [],
            "semantic_neighbourhood": raw_intent,
            "candidate_lookup_material": copy.deepcopy(old_entry.get("aliases_or_examples", [])) if old_entry else [],
            "usage_note": "",
            "known_ambiguity": copy.deepcopy(old_entry.get("known_ambiguity", [])) if old_entry else sorted({a for n in source_record.get("semantic_neighbourhoods", []) for a in n.get("known_ambiguities", [])}),
            "context_warnings": [],
            "preferred_variant": None,
            "variants": [],
            "mode": sorted({x.get("communication_mode", "STANDALONE") for x in token_context}),
            "surface": sorted({x.get("communication_surface", "OTHER") for x in token_context}),
            "context": copy.deepcopy(token_context),
            "corpus_refs": [cid],
            "source_evidence_summary": copy.deepcopy(old_entry.get("source_evidence_summary", [])) if old_entry else [source_record.get("source_family", "")],
            "creator_review": {"review_record_id": cid, "decision": row["creator_decision"], "source_snapshot": review["source_snapshot"], "note_present": bool(row.get("creator_notes", "").strip())},
            "system_candidate_history": {"eligibility": row["system_eligibility"], "candidate_entry_id": row.get("dictionary_entry_id"), "former_question": eligibility_by[cid].get("review_question")},
        }
        entry.update(copy.deepcopy(DISPLAY_OVERRIDES.get(cid, {})))
        headword_for_slug = re.sub(r"[^a-z0-9]+", "-", dictionary_id.lower()).strip("-")
        preferred = build_variant(dictionary_id, f"{dictionary_id}-preferred", "PREFERRED", current_message, [cid], token_context, entry["semantic_neighbourhood"], cid if row.get("creator_notes", "").strip() else None)
        entry["preferred_variant"] = preferred
        entry["variants"].append(preferred)

        if cid == "clh-v01-0003":
            contextual_message = copy.deepcopy(old_variant["message"])
            entry["variants"].append(build_variant(dictionary_id, f"{dictionary_id}-contextual-person", "CONTEXTUAL", contextual_message, [cid], token_context, "PERSON makes a person referent explicit; it can shift the reading toward someone specified or other than the speaker.", cid, "For an explicit person referent; no first-person or person-role grammar is implied."))
        if cid == "clc-v01-0008-r1":
            for suffix, kind, ids, meaning, condition in [
                ("alternative-down", "ALTERNATIVE", ["comm_sound", "rel_down"], "Sound reduction expressed with DOWN; an alternative for this noise-request neighborhood.", None),
                ("context-speech-less", "CONTEXTUAL", ["comm_speak", "qty_minus"], "Noise specifically from shouting or conversation, expressed with SPEECH + LESS.", "Noise from shouting or conversation"),
                ("context-speech-down", "CONTEXTUAL", ["comm_speak", "rel_down"], "Noise specifically from shouting or conversation, expressed with SPEECH + DOWN.", "Noise from shouting or conversation"),
            ]:
                variant_message = replace_tokens(current_message, ids)
                entry["variants"].append(build_variant(dictionary_id, f"{dictionary_id}-{suffix}", kind, variant_message, [cid], token_context, meaning, cid, condition))
        if cid == "clh-v01-0016":
            variant_message = replace_tokens(current_message, ["need_food", "rel_down"])
            entry["variants"].append(build_variant(dictionary_id, f"{dictionary_id}-alternative-down", "ALTERNATIVE", variant_message, [cid], token_context, "DOWN as an alternative to LESS in this food-quantity neighborhood only.", cid))
        if cid == "clh-v01-0002": entry["context_warnings"].append("Context-dependent: HOME may refer to a person or a venue.")
        if cid == "clh-v01-0007": entry["context_warnings"].append("The accepted reading is BAD FOOD, not food unavailable.")
        if cid == "clh-v01-0011": entry["context_warnings"].append("Live interaction supplies the pointing/direction context.")
        if cid == "clh-v01-0017": entry["context_warnings"].append("Quantity interpretation follows the Handbook convention; ‘many waters’ is a lookup label.")
        if cid == "clh-v01-0016": entry["context_warnings"].append("LESS / DOWN alternative is local to this entry; no global equivalence is implied.")
        if cid == "clh-v01-0046": entry["context_warnings"].append("Wayfinding context; this entry concerns pedestrian access.")
        if cid == "clh-v01-0049": entry["context_warnings"].append("Wayfinding context; preserve the parking-specific reading.")
        entry["variants"] = [{**v, "render": f"renders/{v['variant_id']}.svg"} for v in entry["variants"]]
        entry["preferred_variant"] = entry["variants"][0]
        entries.append(entry)
        all_variants.extend(entry["variants"])

        note_classification = make_note_classification(row)
        amendment_records.append({
            **copy.deepcopy(row),
            "previous_system_eligibility": row["system_eligibility"],
            "final_creator_disposition": "ACCEPTED_IN_DICTIONARY" if row["creator_decision"] in {"KEEP_IN_DICTIONARY", "EDIT_ENTRY_METADATA"} else row["creator_decision"],
            "dictionary_entry_id_after_processing": dictionary_id if row["creator_decision"] in {"KEEP_IN_DICTIONARY", "EDIT_ENTRY_METADATA"} else None,
            "creator_note_processing": note_classification,
        })
        lineage_record = {
            "dictionary_entry_id": dictionary_id,
            "corpus_record_id": cid,
            "candidate_entry_id": row.get("dictionary_entry_id"),
            "source_message": copy.deepcopy(old_variant["message"] if old_variant else source_record.get("message") or source_record.get("historical_message")),
            "source_sequence": current_sequence_before,
            "preferred_message": current_message,
            "preferred_sequence": message_sequence(current_message),
            "preferred_changed_by_creator_review": preferred_changed,
            "authority_path": ["HISTORICAL_COMPOSITION_HARVEST", "ACCEPTED_COMPOSITION_CORPUS_BASELINE_V0.1", "DICTIONARY_CREATOR_ELIGIBILITY_REVIEW_V0.1", "COMPOSITION_DICTIONARY_BASELINE_V0.1"],
            "source_provenance": copy.deepcopy(old_entry.get("provenance_detail", [])) if old_entry else copy.deepcopy(source_record.get("provenance", {})),
            "creator_review_ref": {"export_path": "creator-review-export.json", "corpus_record_id": cid, "decision": row["creator_decision"], "creator_notes_verbatim_in_export": bool(row.get("creator_notes", "").strip())},
        }
        lineage_records.append(lineage_record)
        entry["lineage"] = copy.deepcopy(lineage_record)

    entries.sort(key=lambda x: x["dictionary_entry_id"])
    all_variants = [v for e in entries for v in e["variants"]]
    if len(entries) != 65 or len({x["dictionary_entry_id"] for x in entries}) != 65:
        raise ValueError("final dictionary entry IDs are not unique 65-entry set")

    # Keep referent-specific prohibition suggestions as unaccepted candidates.
    prohibition_candidates = [
        {"label": "FEET + NO", "token_ids": ["move_feet", "logic_no"], "status": "CANDIDATE_NOT_ACCEPTED_VARIANT"},
        {"label": "PERSON + FEET + NO", "token_ids": ["person_generic", "move_feet", "logic_no"], "status": "CANDIDATE_NOT_ACCEPTED_VARIANT"},
        {"label": "CAR + NO", "token_ids": ["move_car", "logic_no"], "status": "CANDIDATE_NOT_ACCEPTED_VARIANT"},
        {"label": "PERSON + NO", "token_ids": ["person_generic", "logic_no"], "status": "CANDIDATE_NOT_ACCEPTED_VARIANT"},
        {"label": "UP/AHEAD + NO", "token_ids": None, "mentioned_possible_id": "rel_up", "status": "UNRESOLVED_TOKEN_AND_CONTEXT"},
    ]
    follow_up = [
        {
            "corpus_record_id": "clh-v01-0044", "dictionary_entry_id": "pcd-v01-0025", "original_creator_note": review_by["clh-v01-0044"]["creator_notes"],
            "current_preferred_sequence": next(e for e in entries if e["dictionary_entry_id"] == "pcd-v01-0025")["preferred_variant"]["token_sequence"],
            "safe_inference": "The existing HERE + NO entry is narrow wayfinding; prohibited referents differ. The listed exact-token candidates are retained only as ideas, not accepted public variants.",
            "unresolved": "The UP/AHEAD alternative does not identify one exact primitive or context; the note does not approve any specific contextual variant as current Dictionary content.",
            "creator_question": "Should any of the referent-specific proposals become accepted contextual variants; if so, which context applies to each, and which exact current token do you intend for UP/AHEAD?",
            "variant_candidates": prohibition_candidates,
        },
        {
            "corpus_record_id": "clh-v01-0022", "dictionary_entry_id": new_ids["clh-v01-0022"], "original_creator_note": review_by["clh-v01-0022"]["creator_notes"],
            "current_preferred_sequence": next(e for e in entries if e["dictionary_entry_id"] == new_ids["clh-v01-0022"])["preferred_variant"]["token_sequence"],
            "safe_inference": "move_public + time + punct_question is an arrival-time question. A distinct timetable/schedule message may include media_text.",
            "unresolved": "The exact order and relation of move_public, media_text, time, and punct_question were not specified.",
            "creator_question": "For a separate timetable/schedule request, what exact ordered token sequence using move_public, media_text, time, and punct_question should be accepted?",
            "variant_candidates": [{"mentioned_token_ids": ["move_public", "media_text", "time", "punct_question"], "sequence_status": "ORDER_NOT_SPECIFIED", "status": "CREATOR_VARIANT_CANDIDATE_NOT_ACCEPTED"}],
        },
    ]
    for item in follow_up:
        item["entry_status"] = "CURRENT_ENTRY_ACCEPTED; ONLY_NOTE_PORTION_REQUIRES_FOLLOW_UP"

    # Canonical validation and rendering for each preferred Message and accepted variant.
    output_dir.mkdir(parents=True, exist_ok=True)
    renders_dir = output_dir / "renders"
    renders_dir.mkdir(parents=True, exist_ok=True)
    validation_rows = []
    for entry in entries:
        for variant in entry["variants"]:
            message = variant["message"]
            errors = schema_errors(message) + semantic_errors(message)
            if errors:
                validation_rows.append({"variant_id": variant["variant_id"], "dictionary_entry_id": entry["dictionary_entry_id"], "status": "INVALID", "errors": errors})
                continue
            svg, _ = render_svg(message, registry=registry)
            target = renders_dir / f"{variant['variant_id']}.svg"
            target.write_text(svg, encoding="utf-8")
            variant["render_status"] = "RENDERED_CANONICAL"
            validation_rows.append({"variant_id": variant["variant_id"], "dictionary_entry_id": entry["dictionary_entry_id"], "status": "VALIDATED_AND_RENDERED_CANONICALLY", "path": f"renders/{target.name}"})
    failures = [x for x in validation_rows if x["status"] != "VALIDATED_AND_RENDERED_CANONICALLY"]
    if failures:
        raise ValueError(f"current Message validation/render failures: {failures}")

    # Accepted dictionary review amendment, including every decision and all raw notes.
    note_classes = Counter(c for r in amendment_records for c in (r["creator_note_processing"] or {}).get("classifications", []))
    amendment = {
        "amendment_version": "0.1",
        "status": "CREATOR REVIEW PROCESSED; FINAL VISUAL QA PENDING",
        "source_review": {"path": "creator-review-export.json", "sha256": export_sha, "review_type": review["review_type"], "review_version": review["review_version"], "source_snapshot": review["source_snapshot"], "total_records": review["total_records"], "reviewed_records": review["reviewed_records"]},
        "source_dictionary_candidate": {"path": "../composition-library-baseline-v0.1/dictionary-candidate.json", "version": candidate["candidate_version"], "sha256": hashes["dictionary-candidate.json"]},
        "source_corpus_baseline": {"path": "../composition-library-baseline-v0.1/accepted-corpus.json", "version": corpus["baseline_version"], "sha256": hashes["accepted-corpus.json"]},
        "note_classification_semantics": "Counts are notes carrying each class; a note may carry multiple classes. Original Russian notes remain byte-preserved in creator-review-export.json and are copied verbatim per amendment record.",
        "note_classification_counts": dict(sorted(note_classes.items())),
        "prohibition_variant_candidates": prohibition_candidates,
        "records": amendment_records,
    }
    dictionary = {
        "dictionary_version": "0.1", "status": "CREATOR-REVIEWED / ACCEPTED RESEARCH BASELINE; AWAITING FINAL VISUAL QA",
        "normative_grammar": False, "comprehension_validation_claim": False,
        "meaning_boundary": "An evidence-backed reusable semantic unit with one or more context-bounded Pictiq representations; not an English phrase-to-universal-sequence translation table.",
        "source_corpus_baseline_version": corpus["baseline_version"], "source_snapshot": review["source_snapshot"], "entries": entries,
    }
    variant_data = {"dictionary_version": "0.1", "variant_types": ["PREFERRED", "ALTERNATIVE", "CONTEXTUAL", "HISTORICAL"], "variants": all_variants}
    lineage = {"dictionary_version": "0.1", "source_layers": ["HISTORICAL_COMPOSITION_HARVEST", "ACCEPTED_COMPOSITION_CORPUS_BASELINE_V0.1", "DICTIONARY_CREATOR_ELIGIBILITY_REVIEW_V0.1", "COMPOSITION_DICTIONARY_BASELINE_V0.1"], "records": lineage_records}
    lessons = {
        "status": "TRANSLATOR DESIGN EVIDENCE / NOT EXECUTABLE RULE",
        "boundary": "This ledger does not change Grammar, Protocol, Composer, or implement translation behavior.",
        "lessons": [
            {"id": "lesson-001", "source_corpus_record_ids": ["clh-v01-0003"], "lesson": "Live/self context may supply the affected person; adding PERSON introduces an explicit referent and can change interpretation. Do not encode first person by omission."},
            {"id": "lesson-002", "source_corpus_record_ids": ["clh-v01-0006"], "lesson": "Prefer an accepted direct primitive such as food_meat over unnecessary decomposition when it matches the semantic unit."},
            {"id": "lesson-003", "source_corpus_record_ids": ["clc-v01-0008-r1", "clh-v01-0016"], "lesson": "LESS and DOWN may be alternatives in specified semantic neighborhoods; do not generalize them as globally equivalent."},
            {"id": "lesson-004", "source_corpus_record_ids": ["clh-v01-0014"], "lesson": "A general food-shop composition is not automatically a specialized shop taxonomy; select a supported category only when the task/context requires it."},
            {"id": "lesson-005", "source_corpus_record_ids": ["clh-v01-0044"], "lesson": "A prohibition should retain the prohibited referent/action when that distinction matters; one location-specific NO message is not universal."},
            {"id": "lesson-006", "source_corpus_record_ids": ["clh-v01-0047"], "lesson": "PERSON + FEET supports pedestrian movement in context but does not independently establish a crossing-place relation."},
            {"id": "lesson-007", "source_corpus_record_ids": ["clh-v01-0049"], "lesson": "Creator review can correct token order for a specific practical reading; a local order correction is not a general syntax rule."},
            {"id": "lesson-008", "source_corpus_record_ids": ["clh-v01-0022"], "lesson": "Arrival-time questions and schedule/timetable requests are distinct; keep the latter unresolved until an exact composition is specified."},
        ],
    }
    corpus_decisions = Counter(r["creator_decision"] for r in review["records"])
    counts = {
        "creator_review_records": len(review["records"]), "creator_notes_nonempty": sum(bool(r.get("creator_notes", "").strip()) for r in review["records"]),
        "dictionary_entries": len(entries), "preferred_messages": len(entries), "alternative_variants": sum(v["variant_type"] == "ALTERNATIVE" for v in all_variants),
        "contextual_variants": sum(v["variant_type"] == "CONTEXTUAL" for v in all_variants), "entries_with_multiple_variants": sum(len(e["variants"]) > 1 for e in entries),
        "entries_with_context_warnings": sum(bool(e["context_warnings"]) for e in entries), "entries_with_known_ambiguity": sum(bool(e["known_ambiguity"]) for e in entries),
        "render_count": len(validation_rows), "former_review_promoted": len(EXPECTED_REVIEW_IDS), "follow_up_items": len(follow_up),
    }
    creator_counts = {d: corpus_decisions.get(d, 0) for d in sorted(DECISIONS)}
    write_json(output_dir / "dictionary.json", dictionary)
    write_json(output_dir / "variants.json", variant_data)
    write_json(output_dir / "creator-review-amendment.json", amendment)
    write_json(output_dir / "lineage.json", lineage)
    write_json(output_dir / "translator-lessons.json", lessons)
    write_json(output_dir / "creator-notes-follow-up.json", {"status": "TWO NOTE PORTIONS REQUIRE CREATOR INPUT; CURRENT ENTRIES REMAIN ACCEPTED", "items": follow_up})
    write_json(output_dir / "validation.json", {"method": "Deterministic structural checks plus repository Message schema-shape and registry-aware validation; no formal Dictionary JSON Schema is defined.", "valid_message_count": len(validation_rows), "rendered_canonically": len(validation_rows), "failures": failures})
    write_json(output_dir / "render-manifest.json", {"renders": validation_rows})
    write_json(output_dir / "review/data.json", dictionary)
    (output_dir / "review/index.html").write_text(make_dictionary_viewer(entries), encoding="utf-8")
    (output_dir / "creator-notes-follow-up").mkdir(parents=True, exist_ok=True)
    (output_dir / "creator-notes-follow-up/index.html").write_text(make_followup_viewer(follow_up), encoding="utf-8")

    changed_ids = {"clh-v01-0003", "clh-v01-0006", "clc-v01-0008-r1", "clh-v01-0014", "clh-v01-0016", "clh-v01-0044", "clh-v01-0046", "clh-v01-0047", "clh-v01-0049", "clh-v01-0022"}
    qa_groups: dict[str, list[dict[str, Any]]] = {
        "A. PREFERRED MESSAGE CHANGED": [], "B. METADATA / MEANING CLARIFIED": [], "C. VARIANT ADDED": [],
        "D. FORMER REVIEW → DICTIONARY": [], "E. FOLLOW-UP REQUIRED": [],
    }
    final_by_corpus = {e["corpus_refs"][0]: e for e in entries}
    for cid in sorted(changed_ids):
        e = final_by_corpus[cid]; old = candidate_variant_links.get(cid)
        before = f"../../composition-library-baseline-v0.1/renders/{cid}.svg"
        qa = {"corpus_record_id": cid, "headword": e["headword"], "before_render": before, "after_render": "../" + e["preferred_variant"]["render"], "before_sequence": old.get("token_sequence") if old else message_sequence(corpus_by[cid].get("historical_message") or corpus_by[cid].get("message")), "after_sequence": e["preferred_variant"]["token_sequence"], "note": review_by[cid].get("creator_notes", ""), "interpretation": NOTE_PROCESSING.get(cid, {}).get("summary", e["usage_note"]), "lineage": lineage_records[source_ids.index(cid)]}
        if cid in {"clh-v01-0003", "clh-v01-0006", "clh-v01-0046", "clh-v01-0047", "clh-v01-0049"}:
            qa_groups["A. PREFERRED MESSAGE CHANGED"].append(qa)
        if cid in {"clh-v01-0003", "clh-v01-0014", "clh-v01-0044", "clh-v01-0047", "clh-v01-0022"}:
            qa_groups["B. METADATA / MEANING CLARIFIED"].append(qa)
        if len(e["variants"]) > 1:
            qa_groups["C. VARIANT ADDED"].append(qa)
        if cid in EXPECTED_REVIEW_IDS:
            qa_groups["D. FORMER REVIEW → DICTIONARY"].append(qa)
        if cid in {x["corpus_record_id"] for x in follow_up}:
            qa_groups["E. FOLLOW-UP REQUIRED"].append(qa)
    (output_dir / "review/final-creator-visual-qa.html").write_text(make_qa_viewer(qa_groups), encoding="utf-8")

    artifact_paths = ["creator-review-export.json", "creator-review-amendment.json", "dictionary.json", "variants.json", "lineage.json", "translator-lessons.json", "creator-notes-follow-up.json", "validation.json", "render-manifest.json", "review/index.html", "review/data.json", "review/final-creator-visual-qa.html", "creator-notes-follow-up/index.html"]
    manifest = {
        "dictionary_version": "0.1", "created_on": "2026-09-27", "status": "CREATOR-REVIEWED / ACCEPTED RESEARCH BASELINE; AWAITING FINAL VISUAL QA",
        "normative_grammar": False, "publication_status": "INTERNAL / NOT DEPLOYED",
        "source_corpus_baseline": {"version": corpus["baseline_version"], "path": "../composition-library-baseline-v0.1/accepted-corpus.json", "sha256": hashes["accepted-corpus.json"]},
        "source_dictionary_candidate": {"version": candidate["candidate_version"], "path": "../composition-library-baseline-v0.1/dictionary-candidate.json", "sha256": hashes["dictionary-candidate.json"]},
        "source_dictionary_eligibility_sha256": hashes["dictionary-eligibility.json"],
        "creator_review_export": {"path": "creator-review-export.json", "sha256": export_sha, "source_snapshot": review["source_snapshot"], "record_count": len(review["records"])},
        "creator_review_amendment_sha256": sha256_bytes((output_dir / "creator-review-amendment.json").read_bytes()),
        "creator_decision_counts": creator_counts, "counts": counts,
        "status_dependencies": {"color_modifier": "REQUIRED / NOT IMPLEMENTED", "practical_coverage": "NOT STARTED", "translator": "NOT IMPLEMENTED", "machine_agent_access": "NOT IMPLEMENTED", "stress_test_07_1": "PAUSED / PRESERVED / UNCHANGED", "blocked_hotel_color": "EXCLUDED / STILL BLOCKED"},
        "validation": "PASS" if len(validation_rows) == len(all_variants) and not failures else "FAIL",
        "artifact_sha256": {name: sha256_bytes((output_dir / name).read_bytes()) for name in artifact_paths},
    }
    write_json(output_dir / "manifest.json", manifest)

    readme = f'''# Composition Dictionary Baseline v0.1

**Status:** creator-reviewed accepted research baseline; awaiting final creator visual QA. Internal research only; not normative Grammar and not deployed.

## Purpose and boundaries

A Dictionary entry is an evidence-backed reusable semantic unit with one or more context-bounded Pictiq representations. It is not an English phrase equated with one universal Pictiq sequence. English headwords are lookup labels; exact current Messages, contexts, and evidence remain authoritative. No comprehension, universal-meaning, or external-validation claim follows from creator review.

The Lexicon remains the primitive registry. The Dictionary organizes reusable words/concepts/short phrases. The Accepted Composition Corpus remains the wider evidence/history archive. This package does not rewrite the Corpus or Candidate predecessor. Historical, rejected, superseded, and blocked lineage remains accessible through Corpus sources and this package's lineage file. Odyssey narrative containers and Stress Test 05 discourse remain outside the Dictionary. The hotel + color case remains blocked because Explicit Color Modifier Mechanism is REQUIRED / NOT IMPLEMENTED.

## Sources and review

Built from Accepted Composition Corpus Baseline v0.1, Dictionary Candidate v0.1, current registries, and the archived owner-supplied creator review. The export is preserved byte-for-byte at `creator-review-export.json` (SHA-256 `{export_sha}`). Its source snapshot is `{review['source_snapshot']}`. All 65 units were decided: `{json.dumps(creator_counts, sort_keys=True)}`. Ten records carry non-empty Russian notes; each note is preserved verbatim and separately classified in `creator-review-amendment.json`.

The Candidate's old YES/REVIEW classifications survive only as history. All five former REVIEW records received KEEP_IN_DICTIONARY and are included. Twelve prior CORPUS_ONLY records were not reviewed and remain excluded.

## Variants, context, and unresolved items

Each entry has a preferred current Message and may have evidence-backed ALTERNATIVE or CONTEXTUAL variants. Historical source forms are lineage, not current alternatives. Context warnings remain visible in the viewer. Two note portions remain in `creator-notes-follow-up.json`: the exact scope/token for a proposed UP/AHEAD prohibition and the exact order for a separate schedule/timetable composition. Neither is presented as an accepted Message. The arrival-time entry remains accepted.

`translator-lessons.json` contains **DESIGN EVIDENCE / NOT EXECUTABLE RULE** only. It does not change Grammar, Protocol, Composer, or implement a Translator.

## Review and validation

- Full Dictionary-style viewer: `review/index.html`
- Changed-entry before/after creator QA: `review/final-creator-visual-qa.html`
- Follow-up question view: `creator-notes-follow-up/index.html`
- Exact messages and variants: `dictionary.json`, `variants.json`
- Creator amendment and lineage: `creator-review-amendment.json`, `lineage.json`
- Validation and hashes: `validation.json`, `render-manifest.json`, `manifest.json`

All {len(validation_rows)} preferred/accepted variant Messages passed the repository's schema-shape and registry-aware checks and rendered through the canonical Renderer. New research records receive deterministic structural validation; this project has no formal Dictionary schema. These checks are not a human visual acceptance. Run `python3 tools/research/build_composition_dictionary_baseline_v0_1.py` from the repository root to rebuild deterministically from the archived export. Run `pytest -q tests/test_composition_dictionary_baseline_v0_1.py` for the research builder tests.

**Next gate:** creator visually reviews the changed-items QA surface and full viewer; then close/freeze this baseline. Public Dictionary deployment is a later product decision. After visual acceptance, the planned sequence is Color Modifier repair, Practical Coverage Corpus, Composer coverage, Translator Spike, and later retrieval research. Current stage: `FINAL CREATOR VISUAL QA`.
'''
    (output_dir / "README.md").write_text(readme, encoding="utf-8")
    # Manifest binds README too, but is written last after all deterministic docs.
    manifest["artifact_sha256"]["README.md"] = sha256_bytes((output_dir / "README.md").read_bytes())
    write_json(output_dir / "manifest.json", manifest)
    return manifest


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, default=OUT, help="Output directory (used by deterministic tests)")
    args = parser.parse_args()
    if not (args.output_dir / "creator-review-export.json").is_file():
        raise SystemExit(f"missing archived creator export: {args.output_dir / 'creator-review-export.json'}")
    result = build(args.output_dir)
    print(json.dumps({"counts": result["counts"], "creator_decision_counts": result["creator_decision_counts"], "follow_up_items": result["counts"]["follow_up_items"], "validation": result["validation"]}, indent=2))


if __name__ == "__main__":
    main()
