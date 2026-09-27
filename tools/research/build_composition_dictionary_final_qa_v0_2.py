#!/usr/bin/env python3
"""Build and validate entry-centric final creator QA v0.2 (research only)."""
from __future__ import annotations

import copy
import hashlib
import json
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
PKG = ROOT / "docs/research/composition-dictionary-baseline-v0.1"
REVIEW = PKG / "review"
OUT_DATA = REVIEW / "final-creator-qa-v0.2.json"
ADDENDUM = PKG / "final-creator-qa-addendum-v0.2.json"
HTML = REVIEW / "final-creator-qa-v0.2.html"
README = PKG / "FINAL-CREATOR-QA-v0.2-README.md"
ALLOWED = {"ACCEPT_AS_SHOWN", "NEEDS_CORRECTION", "MOVE_TO_CORPUS_ONLY", "KEEP_ENTRY_CHANGE_PREFERRED", "UNRESOLVED"}


def read(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def message_sequence(message: dict[str, Any]) -> str:
    return " + ".join(t["id"] for f in message["frames"] for t in f["tokens"] if t.get("type") == "icon")


def old_groups() -> dict[str, list[dict[str, Any]]]:
    source = (REVIEW / "final-creator-visual-qa.html").read_text(encoding="utf-8")
    match = re.search(r"const G=(.*?);const esc=", source)
    if not match:
        raise ValueError("cannot extract immutable v0.1 QA category dataset")
    return json.loads(match.group(1))


def make_addendum(entries_by_corpus: dict[str, dict[str, Any]], dictionary: dict[str, Any], preview_sha: str) -> dict[str, Any]:
    return {
        "qa_addendum_type": "PICTIQ_COMPOSITION_DICTIONARY_FINAL_CREATOR_QA_ADDENDUM",
        "version": "0.2",
        "date": "2026-09-27",
        "recorded_after_commit": "59e23b2",
        "source_dictionary_baseline": {
            "version": dictionary["dictionary_version"],
            "source_snapshot": dictionary["source_snapshot"],
            "dictionary_json_sha256": sha((PKG / "dictionary.json").read_bytes()),
            "status": "UNCHANGED; QA DECISIONS PENDING BASELINE APPLICATION",
        },
        "provenance": "CREATOR_FINAL_QA",
        "status": "PENDING_BASELINE_APPLICATION",
        "authority_chain": ["HISTORICAL_EVIDENCE", "CREATOR_SEMANTIC_RECONCILIATION", "ACCEPTED_CORPUS", "DICTIONARY_ELIGIBILITY_REVIEW", "DICTIONARY_BASELINE_V0.1", "FINAL_CREATOR_QA_ADDENDUM_V0.2"],
        "decisions": [
            {
                "corpus_record_id": "clh-v01-0044",
                "dictionary_entry_id": entries_by_corpus["clh-v01-0044"]["dictionary_entry_id"],
                "current_baseline": {"headword": "No entry at this location", "message": entries_by_corpus["clh-v01-0044"]["preferred_variant"]["message"], "token_sequence": "rel_here + logic_no"},
                "decision": "MOVE_TO_CORPUS_ONLY",
                "creator_reason": "HERE + NO may work in a sufficiently obvious physical context, but it is too underspecified to be a recommended reusable Dictionary entry. A prohibition should normally preserve what is prohibited where that distinction matters.",
                "corpus_disposition": "Keep as CONTEXT-DEPENDENT CORPUS EVIDENCE; this is not rejection as invalid Pictiq.",
                "replacement": None,
                "creator_examples_not_approved": ["FEET + NO", "PERSON + FEET + NO", "CAR + NO", "UP/AHEAD + NO", "PERSON + NO"],
                "application_status": "PENDING; remove only from future Dictionary projection; preserve Corpus evidence",
            },
            {
                "corpus_record_id": "clh-v01-0022",
                "dictionary_entry_id": entries_by_corpus["clh-v01-0022"]["dictionary_entry_id"],
                "decision": "ACCEPT_AS_SHOWN",
                "clarification": {"meaning": "When does the train/public transport arrive?", "token_sequence": "move_public + time + punct_question", "status": "KEEP EXISTING ENTRY"},
                "new_related_entry": {
                    "temporary_qa_id": "qa-new-public-transport-timetable",
                    "headword": "Public transport schedule / timetable",
                    "meaning": "Public transport + textual/information schedule + time/question.",
                    "message": copy.deepcopy(entries_by_corpus["clh-v01-0022"]["preferred_variant"]["message"]),
                    "token_sequence": "move_public + media_text + time + punct_question",
                    "preview_render": "review/previews/qa-new-public-transport-timetable.svg",
                    "preview_render_sha256": preview_sha,
                    "status": "CREATOR-APPROVED / PENDING BASELINE APPLICATION",
                    "is_variant_of_arrival_question": False,
                },
                "resolved_follow_up": "Exact ordered timetable composition; no longer unresolved.",
                "application_status": "PENDING; preserve arrival-time entry and add a distinct related semantic unit",
            },
        ],
    }


def build() -> dict[str, Any]:
    dictionary = read(PKG / "dictionary.json")
    entries = dictionary["entries"]
    by_corpus = {cid: e for e in entries for cid in e["corpus_refs"]}
    groups = old_groups()
    categories = {cid: [] for cid in by_corpus}
    category_to_badge = {
        "A. PREFERRED MESSAGE CHANGED": "PREFERRED_CHANGED",
        "B. METADATA / MEANING CLARIFIED": "METADATA_CHANGED",
        "C. VARIANT ADDED": "VARIANT_ADDED",
        "D. FORMER REVIEW → DICTIONARY": "FORMER_REVIEW",
        "E. FOLLOW-UP REQUIRED": "FOLLOW_UP_RESOLVED",
    }
    for category, items in groups.items():
        for item in items:
            categories[item["corpus_record_id"]].append(category)

    sys.path.insert(0, str(ROOT))
    from pictiq_renderer.registry import Registry  # noqa: PLC0415
    from pictiq_renderer.svg_renderer import render_svg  # noqa: PLC0415
    from tools.validate_message_schema import schema_errors, semantic_errors  # noqa: PLC0415

    registry = Registry()
    transport = by_corpus["clh-v01-0022"]
    timetable = copy.deepcopy(transport["preferred_variant"]["message"])
    timetable["frames"][0]["tokens"] = [{"type": "icon", "id": token} for token in ("move_public", "media_text", "time", "punct_question")]
    validation_errors = schema_errors(timetable) + semantic_errors(timetable)
    if validation_errors:
        raise ValueError(f"creator-specified timetable preview failed validation: {validation_errors}")
    svg, _ = render_svg(timetable, registry=registry)
    preview_path = REVIEW / "previews/qa-new-public-transport-timetable.svg"
    preview_path.parent.mkdir(parents=True, exist_ok=True)
    preview_path.write_text(svg, encoding="utf-8")
    preview_hash = sha(svg.encode())

    addendum = make_addendum(by_corpus, dictionary, preview_hash)
    write_json(ADDENDUM, addendum)
    addendum_hash = sha(ADDENDUM.read_bytes())
    scope_ids = {"clh-v01-0047"}
    changed = {e["corpus_refs"][0] for e in entries if e["lineage"]["preferred_changed_by_creator_review"]}
    metadata = {"clh-v01-0003", "clh-v01-0014", "clh-v01-0022", "clh-v01-0044", "clh-v01-0047"}
    rows: list[dict[str, Any]] = []
    for cid in sorted((cid for cid, cats in categories.items() if cats), key=lambda x: by_corpus[x]["dictionary_entry_id"]):
        e = by_corpus[cid]
        lineage = e["lineage"]
        cats = categories[cid]
        badges = {category_to_badge[c] for c in cats}
        if cid in scope_ids:
            badges.add("SCOPE_CHANGED")
        if cid == "clh-v01-0049":
            badges.add("LOCAL_ORDER_CORRECTION")
        if cid == "clh-v01-0006":
            badges.add("DIRECT_PRIMITIVE_PREFERRED")
        if cid in {"clh-v01-0002", "clh-v01-0007", "clh-v01-0011", "clh-v01-0017", "clh-v01-0022"}:
            badges.add("FORMER_REVIEW")
        if cid == "clh-v01-0044":
            badges.add("MOVE_TO_CORPUS_ONLY_PENDING")
        if cid == "clh-v01-0022":
            badges.add("NEW_RELATED_ENTRY")
        for v in e["variants"][1:]:
            if v["variant_type"] == "ALTERNATIVE":
                v["qa_warning"] = "NEARBY CONTEXTUAL READING — VERIFY AS VARIANT"
            elif cid == "clc-v01-0008-r1":
                v["qa_warning"] = "SPEECH-SPECIFIC CONTEXT; not a universal equivalent of SOUND + LESS."
        old = lineage["source_message"]
        before_meta = None
        # The candidate source preserves old lookup labels and scope where it existed.
        cand_file = read(ROOT / "docs/research/composition-library-baseline-v0.1/dictionary-candidate.json")
        candidate = next((x for x in cand_file["entries"] if cid in x.get("corpus_record_ids", [])), None)
        if candidate and cid in metadata:
            before_meta = {"headword": candidate.get("headword"), "semantic_neighbourhood": candidate.get("semantic_neighbourhood"), "mode": candidate.get("variants", [{}])[0].get("mode"), "surface": candidate.get("variants", [{}])[0].get("surface"), "context": candidate.get("variants", [{}])[0].get("context")}
        current_message = e["preferred_variant"]["message"]
        changed_preferred = message_sequence(old) != message_sequence(current_message)
        existing_decision = None
        pending = None
        if cid == "clh-v01-0044":
            existing_decision = "MOVE_TO_CORPUS_ONLY"
            pending = {"state": "RECORDED_FROM_CURRENT_CREATOR_QA", "baseline_effect": "REMOVE FROM FUTURE DICTIONARY PROJECTION / KEEP IN CORPUS", "replacement": None}
        elif cid == "clh-v01-0022":
            existing_decision = "ACCEPT_AS_SHOWN"
            pending = {"state": "RECORDED_FROM_CURRENT_CREATOR_QA", "related_entry_id": "qa-new-public-transport-timetable", "related_entry_status": "CREATOR-APPROVED / PENDING BASELINE APPLICATION"}
        variants = []
        for v in e["variants"]:
            variants.append({"variant_id": v["variant_id"], "type": v["variant_type"], "message": v["message"], "token_sequence": v["token_sequence"], "render": "../" + v["render"], "mode": v["mode"], "surface": v["surface"], "context": v["context"], "provenance": copy.deepcopy(v.get("provenance", lineage["source_provenance"])), "qa_warning": v.get("qa_warning"), "visible_in_viewer": True})
        note_record = next((x for x in read(PKG / "creator-review-amendment.json")["records"] if x["corpus_record_id"] == cid), {})
        warnings = []
        if cid == "clh-v01-0003":
            warnings.append("MODE / CONTEXT MAY BE OVERSTATED: current preferred Message profile/mode is STANDALONE, but compact MEDICAL + URGENT relies on speaker/situation to supply the affected person. No PERSON does not encode grammatical first person.")
        if cid == "clh-v01-0047":
            warnings.append("SOURCE TASK ≠ CURRENT DICTIONARY SCOPE: source refers to a crossing/crossing point; current entry means pedestrian movement. PERSON + FEET is not an exact general translation of pedestrian crossing.")
        if cid == "clh-v01-0044":
            warnings.append("This entry is visually distinguished as a recorded MOVE_TO_CORPUS_ONLY decision, not a normal acceptance card.")
        proposals = []
        if cid == "clh-v01-0044":
            old_follow = next(x for x in read(PKG / "creator-notes-follow-up.json")["items"] if x["corpus_record_id"] == cid)
            proposals = [{"label": v["label"], "token_ids_mentioned": v.get("token_ids"), "status": "PROPOSED / NOT ACCEPTED", "exact_message": None, "render": None, "note": "Creator examples refer to distinct prohibited referents/contexts; none is a replacement or accepted variant."} for v in old_follow["variant_candidates"]]
        badges_sorted = sorted(badges)
        previous = {"message": old if changed_preferred else None, "token_sequence": lineage["source_sequence"] if changed_preferred else None, "render": f"../../composition-library-baseline-v0.1/renders/{cid}.svg" if changed_preferred else None, "provenance": lineage["source_provenance"], "metadata": before_meta, "change_display": "BEFORE → AFTER" if changed_preferred else "CURRENT ONCE; metadata/context details below"}
        qa_row = {
            "dictionary_entry_id": e["dictionary_entry_id"], "corpus_record_id": cid,
            "headword": e["headword"], "semantic_neighbourhood": e["semantic_neighbourhood"],
            "badges": badges_sorted, "legacy_category_memberships": cats,
            "current_baseline": {"preferred_message": current_message, "preferred_token_sequence": e["preferred_variant"]["token_sequence"], "preferred_render": "../" + e["preferred_variant"]["render"], "message_profile": current_message.get("profile"), "mode": e["mode"], "surface": e["surface"], "context": e["context"], "known_ambiguity": e["known_ambiguity"], "context_warnings": e["context_warnings"]},
            "previous_state": previous,
            "accepted_variants": variants,
            "proposed_unaccepted": proposals,
            "creator_note": note_record.get("creator_notes", ""),
            "structured_interpretation": ("Current HERE + NO is retained as context-dependent Corpus evidence, not a universal replacement." if cid == "clh-v01-0044" else ("Arrival time remains distinct from a separate timetable request; the supplied timetable sequence is recorded as a pending new entry." if cid == "clh-v01-0022" else next((x.get("interpretation") for cat in cats for x in groups[cat] if x["corpus_record_id"] == cid and x.get("interpretation")), e["semantic_neighbourhood"]))),
            "scope_warnings": warnings,
            "lineage": lineage,
            "former_system_review": e["system_candidate_history"] if "FORMER_REVIEW" in badges else None,
            "pending_addendum": pending,
            "recorded_decision": existing_decision,
            "review_state": "RECORDED_FROM_CURRENT_CREATOR_QA" if existing_decision else "UNREVIEWED",
            "related_pending_entry": ({"temporary_qa_id": "qa-new-public-transport-timetable", "headword": "Public transport schedule / timetable", "meaning": "Public transport + textual/information schedule + time/question.", "message": timetable, "token_sequence": message_sequence(timetable), "render": "previews/qa-new-public-transport-timetable.svg", "status": "CREATOR-APPROVED / PENDING BASELINE APPLICATION", "provenance": "CREATOR_FINAL_QA"} if cid == "clh-v01-0022" else None),
            "previous_metadata": before_meta,
        }
        rows.append(qa_row)

    ids = [r["dictionary_entry_id"] for r in rows]
    if len(ids) != len(set(ids)):
        raise ValueError("duplicate primary Dictionary entry in QA dataset")
    if len(rows) != 10:
        raise ValueError(f"expected scope derived from existing QA categories to deduplicate to 10, got {len(rows)}")
    category_badges = {k: category_to_badge[k] for k in groups}
    for row in rows:
        for category in row["legacy_category_memberships"]:
            if category_badges[category] not in row["badges"]:
                raise ValueError(f"lost old category membership: {row['dictionary_entry_id']} {category}")
        for variant in row["accepted_variants"]:
            render_file = PKG / variant["render"].replace("../", "", 1)
            if not render_file.is_file() or not variant["token_sequence"] or not variant["type"]:
                raise ValueError(f"accepted variant not fully visible: {variant['variant_id']}")
    if any(r["corpus_record_id"] == "clh-v01-0022" and r["proposed_unaccepted"] for r in rows):
        raise ValueError("resolved timetable proposal must not remain an unresolved variant")
    preview_record = {"valid": True, "errors": [], "renderer": "canonical Python Renderer", "path": "previews/qa-new-public-transport-timetable.svg", "sha256": preview_hash}
    dataset_core = {
        "qa_type": "PICTIQ_COMPOSITION_DICTIONARY_FINAL_CREATOR_QA", "version": "0.2", "status": "READY FOR CREATOR QA; BASELINE UNCHANGED",
        "source_baseline": {"version": dictionary["dictionary_version"], "commit": "59e23b2", "source_snapshot": dictionary["source_snapshot"], "dictionary_json_sha256": sha((PKG / "dictionary.json").read_bytes())},
        "pending_addendum": {"path": "final-creator-qa-addendum-v0.2.json", "sha256": addendum_hash, "status": addendum["status"]},
        "unique_primary_entry_count": len(rows), "old_category_event_count": sum(map(len, groups.values())),
        "old_category_memberships": {k: category_to_badge[k] for k in groups},
        "already_recorded_decisions_count": sum(bool(r["recorded_decision"]) for r in rows),
        "remaining_unresolved_follow_up_count": 0,
        "timetable_preview": {"temporary_qa_id": "qa-new-public-transport-timetable", "token_sequence": message_sequence(timetable), **preview_record},
        "entries": rows,
    }
    dataset_core["qa_dataset_sha256"] = sha(json.dumps(dataset_core, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode())
    write_json(OUT_DATA, dataset_core)
    HTML.write_text(make_html(dataset_core), encoding="utf-8")
    README.write_text(make_readme(dataset_core, groups), encoding="utf-8")
    return dataset_core


def make_html(data: dict[str, Any]) -> str:
    payload = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("<", "\\u003c")
    html = '''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Composition Dictionary — Final Creator QA v0.2</title>
<style>body{{font:16px/1.48 system-ui,sans-serif;color:#151515;max-width:1200px;margin:20px auto;padding:0 16px}}h1{{margin-bottom:.25em}}.boundary,.pending,.warn{{border:1px solid #777;padding:12px;margin:12px 0}}.pending{{background:#fff6dc;border-color:#936500}}.warn{{background:#fff2e5;border-color:#a40}}header{{position:sticky;top:0;background:white;z-index:5;padding:10px 0;border-bottom:1px solid #aaa}}button,select,input{{font:inherit;padding:7px;margin:4px}}.controls{{display:flex;flex-wrap:wrap;align-items:center}}.progress{{font-weight:700;margin-left:auto}}.card{{border-top:2px solid #333;padding:24px 0}}.card.recorded{{border:3px solid #936500;padding:16px;background:#fffdf6}}.badges span{{display:inline-block;background:#e8edf2;padding:4px 8px;margin:3px;border-radius:4px;font:12px monospace}}.visuals{{display:grid;grid-template-columns:repeat(auto-fit,minmax(330px,1fr));gap:16px}}.visual{{border:1px solid #aaa;padding:12px}}.visual img{{display:block;width:100%;max-height:360px;object-fit:contain;object-position:left center;background:#fff}}.variants{{display:grid;grid-template-columns:repeat(auto-fit,minmax(290px,1fr));gap:12px}}.variant{{border:1px solid #bbb;padding:12px}}.variant img{{width:100%;max-height:300px;object-fit:contain;object-position:left center}}.meta{{display:grid;grid-template-columns:140px 1fr;gap:5px 12px;background:#f3f4f5;padding:12px}}.note{{white-space:pre-wrap;background:#f6f6f6;padding:12px}}details{{margin:12px 0}}pre,code{{white-space:pre-wrap;overflow-wrap:anywhere}}.readonly{{font-weight:700;color:#754b00}}.proposal{{border-left:4px solid #999;padding:8px;margin:8px 0;background:#f7f7f7}}@media(max-width:620px){{.meta{{grid-template-columns:1fr}}}}</style>
<body><h1>Composition Dictionary Baseline v0.1 — Final Creator QA v0.2</h1>
<p class="boundary"><b>Scope:</b> reviews the processed Composition Dictionary Baseline v0.1, not Historical Harvest reconciliation. This QA may approve presentation, correct preferred forms, change Dictionary/Corpus-only status, resolve context/mode questions, assess variants, and approve the supplied related entry. Decisions here do not automatically mutate the baseline.</p>
<p>Each affected Dictionary entry appears once. The baseline remains unchanged until a later application pass.</p>
<div class="pending"><b>Already recorded creator decisions — read-only:</b> HERE + NO is marked MOVE_TO_CORPUS_ONLY_PENDING; the arrival-time entry is kept and a distinct timetable entry is approved pending baseline application.</div>
<header><div class="controls"><button id="prev">Previous</button><button id="next">Next</button><label><input id="unreviewed" type="checkbox"> Show unreviewed only</label><input id="search" type="search" placeholder="Search entry / token"><select id="badge"><option value="">All badges</option></select><select id="decisionFilter"><option value="">All decisions</option><option>UNREVIEWED</option><option>RECORDED_FROM_CURRENT_CREATOR_QA</option><option>ACCEPT_AS_SHOWN</option><option>NEEDS_CORRECTION</option><option>MOVE_TO_CORPUS_ONLY</option><option>KEEP_ENTRY_CHANGE_PREFERRED</option><option>UNRESOLVED</option></select><span class="progress" id="progress"></span></div><div><button id="export">EXPORT FINAL QA JSON</button><label>Import JSON <input id="import" type="file" accept="application/json"></label><button id="reset">RESET LOCAL QA</button><a href="index.html">Open full current Dictionary</a></div></header>
<main id="cards"></main><script>const DATA=__DATA__;const KEY='pictiq.final-creator-qa.v0.2:'+DATA.qa_dataset_sha256;const DECISIONS=__DECISIONS__;const $=id=>document.getElementById(id);const esc=s=>String(s??'').replace(/[&<>]/g,c=>({{'&':'&amp;','<':'&lt;','>':'&gt;'}}[c])).replaceAll('"','&quot;').replaceAll("'",'&#39;');let state=load(),active=0;function load(){{try{{return JSON.parse(localStorage.getItem(KEY)||'{{}}')}}catch{{return {{}}}}}}function locked(r){{return !!r.recorded_decision}}function decision(r){{return locked(r)?r.recorded_decision:(state[r.dictionary_entry_id]?.decision||'UNREVIEWED')}}function reviewed(r){{return locked(r)||!!state[r.dictionary_entry_id]?.decision}}function save(){{localStorage.setItem(KEY,JSON.stringify(state));draw()}}function options(selected){{return ['','ACCEPT_AS_SHOWN','NEEDS_CORRECTION','MOVE_TO_CORPUS_ONLY','KEEP_ENTRY_CHANGE_PREFERRED','UNRESOLVED'].map(x=>`<option value="${{x}}" ${{x===selected?'selected':''}}>${{x||'UNREVIEWED'}}</option>`).join('')}}function visual(label,seq,img,msg,provenance){{return `<div class="visual"><h3>${{esc(label)}}</h3><img src="${{esc(img)}}" alt="${{esc(label)}} Pictiq render"><p><b>Exact Message:</b> <code>${{esc(seq)}}</code></p><details><summary>Message structure and provenance</summary><pre>${{esc(JSON.stringify(msg,null,2))}}</pre><pre>${{esc(JSON.stringify(provenance,null,2))}}</pre></details></div>`}}function card(r){{const lockedDecision=locked(r),cur=r.current_baseline,prev=r.previous_state;let visuals='';if(prev.message)visuals=`<div class="visuals">${{visual('BEFORE — candidate / source',prev.token_sequence,prev.render,prev.message,prev.provenance)}}${{visual('AFTER — current baseline',cur.preferred_token_sequence,cur.preferred_render,cur.preferred_message,r.accepted_variants.find(v=>v.type==='PREFERRED')?.provenance)}}</div>`;else visuals=visual('CURRENT PICTIQ MESSAGE',cur.preferred_token_sequence,cur.preferred_render,cur.preferred_message,r.accepted_variants.find(v=>v.type==='PREFERRED')?.provenance);const extra=r.accepted_variants.filter(v=>v.variant_id!==r.accepted_variants.find(z=>z.type==='PREFERRED')?.variant_id);const variants=extra.length?`<h3>Accepted variants — part of the same card</h3><div class="variants">${{extra.map(v=>`<div class="variant"><h4>${{esc(v.type)}} · ${{esc(v.variant_id)}}</h4><img src="${{esc(v.render)}}"><p><b>Exact Message:</b> <code>${{esc(v.token_sequence)}}</code></p><details><summary>Message structure</summary><pre>${{esc(JSON.stringify(v.message,null,2))}}</pre></details><p>Mode: ${{esc(v.mode.join(', '))}} · Surface: ${{esc(v.surface.join(', '))}}</p><p>Context: ${{esc(JSON.stringify(v.context))}}</p><p>Provenance: ${{esc(JSON.stringify(v.provenance))}}</p>${{v.qa_warning?`<p class="warn">${{esc(v.qa_warning)}}</p>`:''}}</div>`).join('')}}</div>`:'';const proposals=r.proposed_unaccepted.length?`<h3>PROPOSED / NOT ACCEPTED</h3>${{r.proposed_unaccepted.map(p=>`<div class="proposal"><b>${{esc(p.label)}}</b> — ${{esc(p.status)}}<p>${{esc(p.note)}} ${{p.token_ids_mentioned?`Mentioned tokens: ${{esc(p.token_ids_mentioned.join(' + '))}}`:''}}</p><p>No exact Message and no render are asserted.</p></div>`).join('')}`:'';const related=r.related_pending_entry?`<section class="pending"><h3>Related creator-approved entry — PENDING BASELINE APPLICATION</h3><p><b>${{esc(r.related_pending_entry.headword)}}</b> · ${{esc(r.related_pending_entry.meaning)}}</p>${{visual('QA PREVIEW — NOT BASELINE DATA',r.related_pending_entry.token_sequence,r.related_pending_entry.render,r.related_pending_entry.message,r.related_pending_entry.provenance)}}<p>Status: ${{esc(r.related_pending_entry.status)}} · Temporary ID: ${{esc(r.related_pending_entry.temporary_qa_id)}}</p></section>`:'';const metadata=prev.metadata?`<p><b>OLD HEADWORD / MEANING:</b> ${{esc(prev.metadata.headword)}} → <b>NEW:</b> ${{esc(r.headword)}} · ${{esc(prev.metadata.semantic_neighbourhood)}} → ${{esc(r.semantic_neighbourhood)}}<br>Previous mode/surface: ${{esc([...(prev.metadata.mode||[]),...(prev.metadata.surface||[])].join(' / '))}<br>Previous context: ${{esc(JSON.stringify(prev.metadata.context||[]))}}</p>`:'';const warnings=r.scope_warnings.map(w=>`<p class="warn">${{esc(w)}}</p>`).join('');const decisionUI=lockedDecision?`<p class="readonly">RECORDED FROM CURRENT CREATOR QA — ${{esc(r.recorded_decision)}}. Read-only; already counted.</p><p>${{esc(JSON.stringify(r.pending_addendum))}}</p>`:`<label>One decision for this entry: <select data-decision="${{esc(r.dictionary_entry_id)}}">${{options(state[r.dictionary_entry_id]?.decision||'')}}</select></label><label>Creator notes <textarea data-note="${{esc(r.dictionary_entry_id)}}" rows="3" style="width:100%">${{esc(state[r.dictionary_entry_id]?.note||'')}}</textarea></label>`;return `<article class="card ${{lockedDecision?'recorded':''}}" data-id="${{esc(r.dictionary_entry_id)}}"><h2>${{esc(r.dictionary_entry_id)}} · ${{esc(r.corpus_record_id)}} · ${{esc(r.headword)}}</h2><div class="badges">${{r.badges.map(b=>`<span>${{esc(b)}}</span>`).join('')}}</div>${{r.pending_addendum?.baseline_effect?`<div class="pending"><b>CURRENT BASELINE ENTRY</b><p><code>${{esc(cur.preferred_token_sequence)}}</code></p><b>PENDING FINAL APPLICATION:</b><p>${{esc(r.pending_addendum.baseline_effect)}</p>Reason: underspecified as a reusable Dictionary recommendation; keep Corpus evidence.</p></div>`:''}}${{visuals}}${{metadata}}<div class="meta"><b>Meaning</b><span>${{esc(r.semantic_neighbourhood)}}</span><b>Mode / Profile</b><span>${{esc(cur.mode.join(', '))}} / ${{esc(cur.message_profile||'unspecified')}}</span><b>Surface</b><span>${{esc(cur.surface.join(', '))}}</span><b>Context / supplies</b><span>${{esc(JSON.stringify(cur.context))}}</span><b>Known ambiguity</b><span>${{esc(cur.known_ambiguity.join('; ')||'None recorded')}}</span></div>${{r.creator_note?`<h3>Creator note (verbatim)</h3><p class="note">${{esc(r.creator_note)}}</p>`:''}}<p><b>Interpretation:</b> ${{esc(r.structured_interpretation)}}</p>${{warnings}}${{variants}}${{proposals}}${{related}}<details><summary>Full lineage and source evidence</summary><pre>${{esc(JSON.stringify(r.lineage,null,2))}}</pre></details>${{decisionUI}}<p><a href="index.html">Open full Dictionary viewer</a></p></article>`}}function filtered(){{let a=DATA.entries.slice();if($('unreviewed').checked)a=a.filter(r=>!reviewed(r));const q=$('search').value.toLowerCase();if(q)a=a.filter(r=>JSON.stringify(r).toLowerCase().includes(q));const b=$('badge').value;if(b)a=a.filter(r=>r.badges.includes(b));const d=$('decisionFilter').value;if(d)a=a.filter(r=>decision(r)===d);return a}}function draw(){{const badges=[...new Set(DATA.entries.flatMap(x=>x.badges))].sort();const sel=$('badge');const old=sel.value;if(sel.options.length===1)badges.forEach(b=>{{const o=document.createElement('option');o.value=b;o.textContent=b;sel.append(o)}});sel.value=old;const rows=filtered(),reviewedCount=DATA.entries.filter(reviewed).length;$('progress').textContent=`${{reviewedCount}} / ${{DATA.unique_primary_entry_count}} UNIQUE ENTRIES REVIEWED`;if(!rows.length){{$('cards').innerHTML='<p>No matching entries.</p>';return}}if(active>=rows.length)active=rows.length-1;$('cards').innerHTML=rows.map((r,i)=>card(r)).join('');document.querySelectorAll('[data-decision]').forEach(el=>el.addEventListener('change',e=>{{const id=e.target.dataset.decision,val=e.target.value;if(val)state[id]={{...(state[id]||{{}}),decision:val}};else if(state[id])delete state[id].decision;save()}}));document.querySelectorAll('[data-note]').forEach(el=>el.addEventListener('change',e=>{{const id=e.target.dataset.note;state[id]={{...(state[id]||{{}}),note:e.target.value}};save()}}))}}function exportRecords(){{return DATA.entries.map(r=>({{dictionary_entry_id:r.dictionary_entry_id,corpus_record_id:r.corpus_record_id,decision:decision(r)==='UNREVIEWED'?null:decision(r),creator_note:locked(r)?'':(state[r.dictionary_entry_id]?.note||''),decision_source:locked(r)?'PENDING_ADDENDUM':'LOCAL_QA_OVERLAY'}}))}}function validateImport(x){{if(x.qa_type!==DATA.qa_type||x.version!==DATA.version)throw Error('QA type/version mismatch');if(x.source_baseline?.dictionary_json_sha256!==DATA.source_baseline.dictionary_json_sha256||x.source_baseline?.commit!==DATA.source_baseline.commit||x.source_baseline?.source_snapshot!==DATA.source_baseline.source_snapshot)throw Error('baseline snapshot mismatch');if(x.unique_primary_entry_count!==DATA.unique_primary_entry_count)throw Error('unique entry count mismatch');const suppliedIds=x.entry_ids||[];const expectedIds=DATA.entries.map(r=>r.dictionary_entry_id);if(suppliedIds.length!==expectedIds.length||new Set(suppliedIds).size!==suppliedIds.length||expectedIds.some(id=>!suppliedIds.includes(id)))throw Error('entry ID list mismatch');if(x.qa_dataset_sha256!==DATA.qa_dataset_sha256||x.pending_addendum?.sha256!==DATA.pending_addendum.sha256)throw Error('QA dataset/addendum snapshot mismatch');const expected=new Set(DATA.entries.map(r=>r.dictionary_entry_id)),seen=new Set();for(const r of x.records||[]){{if(!expected.has(r.dictionary_entry_id)||seen.has(r.dictionary_entry_id))throw Error('unknown or duplicate Dictionary entry ID');seen.add(r.dictionary_entry_id);if(r.decision&&!DECISIONS.includes(r.decision))throw Error('invalid decision');if(r.decision==='NEEDS_CORRECTION'&&!String(r.creator_note||'').trim())throw Error('NEEDS_CORRECTION requires a note');const lockedRow=DATA.entries.find(e=>e.dictionary_entry_id===r.dictionary_entry_id);if(locked(lockedRow)&&r.decision!==lockedRow.recorded_decision)throw Error('recorded addendum decision mismatch')}}if(seen.size!==expected.size)throw Error('missing expected unique review records');return true}}function download(obj,name){{const blob=new Blob([JSON.stringify(obj,null,2)],{{type:'application/json'}}),a=document.createElement('a');a.href=URL.createObjectURL(blob);a.download=name;a.click();URL.revokeObjectURL(a.href)}}$('export').onclick=()=>{{const records=exportRecords();if(records.some(r=>r.decision==='NEEDS_CORRECTION'&&!r.creator_note.trim()))return alert('Add a note for each NEEDS_CORRECTION decision before export.');download({{qa_type:DATA.qa_type,version:DATA.version,source_baseline:DATA.source_baseline,qa_dataset_sha256:DATA.qa_dataset_sha256,pending_addendum:DATA.pending_addendum,unique_primary_entry_count:DATA.unique_primary_entry_count,reviewed_count:DATA.entries.filter(reviewed).length,unresolved_follow_up_count:DATA.remaining_unresolved_follow_up_count,unresolved_decision_count:records.filter(r=>r.decision==='UNRESOLVED').length,entry_ids:DATA.entries.map(r=>r.dictionary_entry_id),records}},'pictiq-final-creator-qa-v0.2.json')}};$('import').onchange=async e=>{{try{{const x=JSON.parse(await e.target.files[0].text());validateImport(x);const next={{}};for(const r of x.records)if(!locked(DATA.entries.find(e=>e.dictionary_entry_id===r.dictionary_entry_id))&&r.decision)next[r.dictionary_entry_id]={{decision:r.decision,note:r.creator_note||''}};state=next;save();alert('Import validated and applied to local review overlay.')}}catch(err){{alert('Import rejected: '+err.message)}}e.target.value=''}};$('reset').onclick=()=>{{if(confirm('Reset only local QA decisions and notes? The repository pending addendum will remain unchanged.')){{localStorage.removeItem(KEY);state={{}};draw()}}}};$('prev').onclick=()=>{{active=Math.max(0,active-1);const e=filtered()[active];if(e)document.querySelector(`[data-id="${{CSS.escape(e.dictionary_entry_id)}}"]`)?.scrollIntoView()}};$('next').onclick=()=>{{active=Math.min(filtered().length-1,active+1);const e=filtered()[active];if(e)document.querySelector(`[data-id="${{CSS.escape(e.dictionary_entry_id)}}"]`)?.scrollIntoView()}};for(const id of ['unreviewed','search','badge','decisionFilter'])$(id).addEventListener('input',()=>{{active=0;draw()}});draw();</script></body></html>'''
    html = html.replace('{{', '{').replace('}}', '}')
    return html.replace('__DATA__', payload).replace('__DECISIONS__', json.dumps(sorted(ALLOWED)))


def make_readme(data: dict[str, Any], groups: dict[str, list[dict[str, Any]]]) -> str:
    return f'''# Final Creator QA v0.2

**Status:** prepared; creator review is open. Dictionary Baseline v0.1 is unchanged and not frozen.

The v0.1 QA sheet grouped records under change categories, causing the same semantic entry to appear repeatedly (16 category events). That duplication invalidated it as a single-decision final gate; it does not by itself indicate a defect in the baseline. v0.2 aggregates all category memberships, variants, context, and pending questions into **{data['unique_primary_entry_count']} unique entry cards**. Each entry gets one decision.

Open `review/final-creator-qa-v0.2.html` (local server URL: `http://localhost:8765/docs/research/composition-dictionary-baseline-v0.1/review/final-creator-qa-v0.2.html`). Actions are ACCEPT_AS_SHOWN, NEEDS_CORRECTION, MOVE_TO_CORPUS_ONLY, KEEP_ENTRY_CHANGE_PREFERRED, and UNRESOLVED. The two decisions already supplied in this task are shown as read-only evidence and counted reviewed; remaining cards start UNREVIEWED.

Editable decisions and notes live only in browser `localStorage`, keyed to the dataset snapshot. EXPORT / IMPORT uses JSON bound to baseline, dataset, and pending-addendum hashes; import rejects mismatched snapshots, unknown/duplicate IDs, missing entry records, invalid actions, and changed locked decisions. RESET LOCAL QA asks for confirmation and clears only the local overlay; it cannot remove the repository addendum.

`final-creator-qa-addendum-v0.2.json` records the new creator decisions with status `PENDING_BASELINE_APPLICATION`. The timetable preview uses the canonical renderer and lives under `review/previews/`; neither it nor the addendum is baseline data. No review decision is automatically applied.

After creator completes v0.2, a separate processing pass should apply the QA export and addendum, validate the resulting baseline, and freeze v0.1. Only after that research arc is complete should it be pushed; Color Modifier repair comes next. This task does not start that pass.

Dataset SHA-256: `{data['qa_dataset_sha256']}`. Pending addendum SHA-256: `{data['pending_addendum']['sha256']}`. Old v0.1 QA remains at `review/final-creator-visual-qa.html` unchanged.
'''


if __name__ == "__main__":
    result = build()
    print(json.dumps({"unique_primary_entry_count": result["unique_primary_entry_count"], "old_category_event_count": result["old_category_event_count"], "recorded": result["already_recorded_decisions_count"], "dataset_sha256": result["qa_dataset_sha256"], "timetable_preview": result["timetable_preview"]}, indent=2))
