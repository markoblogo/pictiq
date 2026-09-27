#!/usr/bin/env python3
"""Build Composition Library v0.1 research baselines from frozen inputs."""
from __future__ import annotations

import hashlib
import html
import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
HARVEST = ROOT / "docs/research/composition-library-historical-harvest-v0.1"
OUT = ROOT / "docs/research/composition-library-baseline-v0.1"
sys.path.insert(0, str(ROOT))
from pictiq_renderer.svg_renderer import render_svg  # noqa: E402
from pictiq_renderer.registry import Registry  # noqa: E402
from tools.validate_message_schema import schema_errors, semantic_errors  # noqa: E402

EXPORT = HARVEST / "reconciliation/creator-export-2026-09-27.json"
ADDENDUM = HARVEST / "reconciliation/creator-reconciliation-addendum-2026-09-27.json"
EXPECTED_EXPORT_SHA = "455588e54a561e162d4b8ffdad38ad1b0f59612ccb3fafb889cc6e8ba41b40bc"

REVIEW: dict[str, tuple[str, str]] = {
    "clh-v01-0002": ("REVIEW", "The accepted question is reusable in principle, but the referent HOME can be personal or venue-specific; choose a public-facing lookup label/context."),
    "clh-v01-0007": ("REVIEW", "The accepted composition encodes a contrastive interpretation (bad food, not unavailable); confirm how narrowly the Dictionary should present this reading."),
    "clh-v01-0011": ("REVIEW", "The accepted polite request depends on the interaction supplying pointing/direction; confirm whether the narrow context is clear enough for a standalone Dictionary entry."),
    "clh-v01-0017": ("REVIEW", "The accepted Handbook gloss ‘many waters’ is unusual in English and quantity interpretation depends on the Handbook convention; choose a clear lookup label."),
    "clh-v01-0022": ("REVIEW", "The accepted sequence combines public transport, time and a question; decide whether the intended schedule/when reading is sufficiently bounded for a public entry."),
}

CORPUS_ONLY: dict[str, str] = {
    "clh-v01-0009": "A single literary character action from the 04A trial; useful experimental/narrative evidence, but not a reusable general Dictionary expression.",
}

DISPLAY_LABELS = {
    "clh-v01-0040": "Turn right", "clh-v01-0041": "Turn left", "clh-v01-0042": "Straight ahead",
    "clh-v01-0043": "Down / lower level", "clh-v01-0044": "Do not enter", "clh-v01-0045": "Pedestrian route",
    "clh-v01-0046": "No pedestrians", "clh-v01-0047": "Pedestrian crossing", "clh-v01-0048": "Parking",
    "clh-v01-0049": "No parking", "clh-v01-0050": "Fuel service", "clh-v01-0051": "Medical service",
    "clh-v01-0052": "Police service", "clh-v01-0053": "Food service", "clh-v01-0055": "Information point",
    "clh-v01-0056": "Danger / caution", "clh-v01-0057": "Road works", "clh-v01-0058": "Slippery surface",
    "clh-v01-0059": "No through route", "clh-v01-0060": "Speed limit: 50", "clh-v01-0061": "No left turn",
    "clh-v01-0062": "You are here",
}

def read(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))

def write(path: Path, obj: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

def esc(x: Any) -> str:
    return html.escape(str(x if x is not None else ""), quote=True)

def token_label(message: dict[str, Any]) -> str:
    return " / ".join(" + ".join(t.get("id", str(t.get("value", t.get("type")))) for t in f["tokens"]) for f in message["frames"])

def main() -> None:
    export_bytes = EXPORT.read_bytes()
    export_sha = hashlib.sha256(export_bytes).hexdigest()
    if export_sha != EXPECTED_EXPORT_SHA:
        raise SystemExit(f"creator export SHA mismatch: {export_sha}")
    manifest, exp, add = read(HARVEST / "manifest.json"), read(EXPORT), read(ADDENDUM)
    harvest_entries = manifest["records"]
    export_rows = {x["composition_id"]: x for x in exp["records"]}
    decisions = {x["composition_id"]: x for x in add["decisions"]}
    if len(harvest_entries) != 81 or len(export_rows) != 81 or set(export_rows) != {x["composition_id"] for x in harvest_entries}:
        raise SystemExit("Harvest/export ID reconciliation failed")
    if add["harvest_snapshot"] != manifest["snapshot_commit"] or set(decisions) != {"clh-v01-0008", "clh-v01-0010", "clh-v01-0012", "clh-v01-0070"}:
        raise SystemExit("addendum binding or case set mismatch")

    (OUT / "renders").mkdir(parents=True, exist_ok=True)
    (OUT / "review").mkdir(exist_ok=True)
    registry = Registry()
    corpus: list[dict[str, Any]] = []
    replacement_corpus: list[dict[str, Any]] = []
    current: list[dict[str, Any]] = []
    negative: list[dict[str, Any]] = []
    lineage: list[dict[str, Any]] = []
    blocked: list[dict[str, Any]] = []
    eligibility: list[dict[str, Any]] = []
    accounting: list[dict[str, Any]] = []

    replacements = {
        "clh-v01-0008": ("clc-v01-0008-r1", ["comm_sound", "qty_minus"], "Less noise, please."),
        "clh-v01-0012": ("clc-v01-0012-r1", ["rel_here", "action_conflict"], "This place is a battlefield."),
        "clh-v01-0070": ("clc-v01-0070-r1", ["action_change"], "Loading / processing"),
    }
    original_count = {"ACCEPT": 0, "EDIT": 0, "REJECT": 0}
    source_by_id = {}
    for entry in harvest_entries:
        hist = read(HARVEST / entry["path"])
        cid = hist["composition_id"]
        source_by_id[cid] = entry
        decision = export_rows[cid]["primary_decision"]
        original_count[decision] = original_count.get(decision, 0) + 1
        message_errors = schema_errors(hist["pictiq_message"]) + semantic_errors(hist["pictiq_message"])
        status = "ACCEPTED_UNCHANGED" if decision == "ACCEPT" else "HISTORICAL_SUPERSEDED" if cid in replacements or cid == "clh-v01-0010" else "REJECTED_WITHOUT_REPLACEMENT"
        if decision == "ACCEPT" and message_errors:
            status = "ACCEPTED_HISTORICAL_ONLY_INCOMPATIBLE"
        if cid == "clh-v01-0010": status = "BLOCKED_HISTORICAL_REJECTED"
        seq = token_label(hist["pictiq_message"])
        hist_elig, hist_reason = "CORPUS_ONLY", "Historical Harvest form is not a current accepted composition."
        rec = {
            "corpus_record_id": cid,
            "record_kind": "HISTORICAL_HARVEST_RECORD",
            "reconciliation_disposition": status,
            "creator_decision": decision,
            "source_harvest": {"harvest_id": manifest["harvest_id"], "snapshot_commit": manifest["snapshot_commit"], "composition_id": cid, "record_path": entry["path"]},
            "source_family": entry["source_family"],
            "historical_message": hist["pictiq_message"],
            "historical_sequence": seq,
            "semantic_neighbourhoods": hist["semantic_neighbourhoods"],
            "applicability": hist["applicability"],
            "provenance": {"origin": hist["origin"], "uses": hist["uses"], "creator_review_id": export_rows[cid]["review_id"], "addendum": decisions.get(cid)},
            "tests": hist["tests"], "failures": hist["failures"], "compatibility": hist["compatibility"],
            "historical_dictionary_status": "HISTORICAL_ONLY" if message_errors and decision == "ACCEPT" else hist_elig,
            "historical_validation_errors": message_errors,
            "current_message": None,
            "dictionary_entry_id": None,
        }
        if decision == "ACCEPT" and not message_errors:
            current.append({"corpus_record_id": cid, "message": hist["pictiq_message"], "neighbourhoods": hist["semantic_neighbourhoods"], "applicability": hist["applicability"], "tests": hist["tests"], "failures": hist["failures"], "provenance": rec["provenance"], "source_family": entry["source_family"], "source_harvest_id": cid, "authority": ["HUMAN_ACCEPTED", "HISTORICAL_HARVEST_EXACT"]})
        if cid in replacements:
            repl_id, ids, intent = replacements[cid]
            dm = dict(hist["pictiq_message"])
            dm["frames"] = [{"tokens": [{"type": "icon", "id": icon_id} for icon_id in ids]}]
            new = {
                "corpus_record_id": repl_id,
                "record_kind": "CREATOR_REPLACEMENT",
                "reconciliation_disposition": "ACCEPTED_REPLACEMENT",
                "creator_decision": "CREATOR_RECONCILIATION",
                "source_harvest": {"harvest_id": manifest["harvest_id"], "snapshot_commit": manifest["snapshot_commit"], "composition_id": cid, "record_path": entry["path"]},
                "message": dm,
                "sequence": " + ".join(ids),
                "neighbourhoods": [{"intent_id": f"creator-reconciliation:{cid}", "canonical_intent": intent, "semantic_examples": decisions[cid].get("semantic_neighbourhood", [decisions[cid].get("semantic_reading", intent)]), "required_context": [], "optional_context": [], "known_ambiguities": [], "coverage_assessments": []}],
                "applicability": hist["applicability"],
                "provenance": {"source_type": "CREATOR_RECONCILIATION", "export_path": "../composition-library-historical-harvest-v0.1/reconciliation/creator-export-2026-09-27.json", "addendum_path": "../composition-library-historical-harvest-v0.1/reconciliation/creator-reconciliation-addendum-2026-09-27.json", "historical_record_id": cid, "creator_reason": decisions[cid].get("creator_reason", decisions[cid].get("historical_reason")), "provenance": "CREATOR_RECONCILIATION"},
                "tests": [], "failures": [], "compatibility": {"pictiq_version": "1.1", "message_schema_version": "0.1", "message_validity": "CURRENT"},
                "source_family": entry["source_family"], "source_harvest_id": cid,
                "authority": ["CREATOR_RECONCILIATION", "CURRENT_ACCEPTED_REPLACEMENT"],
                "dictionary_entry_id": None,
            }
            current.append(new)
            replacement_corpus.append(new)
            lineage.append({"historical_record_id": cid, "historical_message": hist["pictiq_message"], "original_decision": decision, "addendum_decision": decisions[cid], "current_record_id": repl_id, "current_message": dm, "eligibility": "PENDING_GENERATION", "evidence_path": entry["path"]})
        if cid == "clh-v01-0010":
            b = {"blocked_id": "blocked-clh-v01-0010", "historical_record_id": cid, "semantic_intent": "HOTEL + BLUE + GOOD", "historical_rejected_message": hist["pictiq_message"], "creator_decision": decisions[cid], "current_message": None, "status": "BLOCKED_BY_MISSING_EXPLICIT_COLOR_TILE_MECHANISM", "dictionary_eligibility": "DEFERRED_BLOCKED", "repair_dependency": "Explicit Color Modifier Mechanism — REQUIRED / NOT IMPLEMENTED", "evidence_path": entry["path"]}
            blocked.append(b)
            lineage.append({"historical_record_id": cid, "historical_message": hist["pictiq_message"], "original_decision": decision, "addendum_decision": decisions[cid], "current_record_id": None, "blocked_id": b["blocked_id"], "eligibility": "DEFERRED_BLOCKED", "evidence_path": entry["path"]})
        if cid in decisions and cid != "clh-v01-0010":
            negative.append({"historical_record_id": cid, "historical_message": hist["pictiq_message"], "historical_sequence": seq, "intent": hist["semantic_neighbourhoods"], "historical_status": "SUPERSEDED", "creator_reason": decisions[cid].get("creator_reason", decisions[cid].get("historical_reason")), "replacement_record_id": replacements[cid][0], "creator_provenance": "CREATOR_RECONCILIATION", "evidence_path": entry["path"]})
        elif decision == "REJECT":
            negative.append({"historical_record_id": cid, "historical_message": hist["pictiq_message"], "historical_sequence": seq, "intent": hist["semantic_neighbourhoods"], "historical_status": "REJECTED", "creator_reason": export_rows[cid].get("human_notes", "Creator decision preserved in byte-identical export."), "replacement_record_id": None, "creator_provenance": "CREATOR_EXPORT", "evidence_path": entry["path"]})
        corpus.append(rec)
        accounting.append({"harvest_candidate_id": cid, "original_decision": decision, "final_disposition": "BLOCKED_REPLACEMENT" if cid == "clh-v01-0010" else "ACCEPTED_REPLACEMENT" if cid in replacements else "ACCEPTED_HISTORICAL_ONLY_INCOMPATIBLE" if decision == "ACCEPT" and message_errors else "ACCEPTED_UNCHANGED" if decision == "ACCEPT" else "REJECTED_WITHOUT_REPLACEMENT", "current_record_id": replacements[cid][0] if cid in replacements else cid if decision == "ACCEPT" and not message_errors else None})

    # Add replacement records to Corpus after their immutable harvested forms.
    corpus.extend(replacement_corpus)
    for rec in corpus:
        if rec["record_kind"] == "HISTORICAL_HARVEST_RECORD" and rec["reconciliation_disposition"] == "ACCEPTED_UNCHANGED":
            rec["current_message"] = rec["historical_message"]
            rec["current_record_id"] = rec["corpus_record_id"]
        elif rec["record_kind"] == "HISTORICAL_HARVEST_RECORD" and rec["corpus_record_id"] in replacements:
            rec["current_record_id"] = replacements[rec["corpus_record_id"]][0]
        elif rec["record_kind"] == "CREATOR_REPLACEMENT":
            rec["current_record_id"] = rec["corpus_record_id"]

    # Editorial eligibility is deliberately independent of human semantic acceptance.
    dict_groups: dict[str, list[dict[str, Any]]] = {"YES": [], "CORPUS_ONLY": [], "REVIEW": []}
    for rec in current:
        cid = rec["corpus_record_id"]
        hist_id = rec["source_harvest_id"]
        fam = rec["source_family"]
        intent = rec["neighbourhoods"][0].get("canonical_intent", "")
        if cid in REVIEW:
            status, rationale = REVIEW[cid]
        elif cid in CORPUS_ONLY:
            status, rationale = "CORPUS_ONLY", CORPUS_ONLY[cid]
        elif fam == "ODYSSEY":
            status, rationale = "CORPUS_ONLY", "Whole accepted Odyssey narrative/discourse record; preserved without extracting reusable sub-compositions."
        elif fam == "STRESS TEST 05" or len(rec["message"].get("frames", [])) > 1:
            status, rationale = "CORPUS_ONLY", "Whole multi-frame dialogue or discourse unit; keep as Corpus evidence without automatic splitting."
        elif fam == "LANDING":
            status, rationale = "CORPUS_ONLY", "Landing/source-specific Pictiq identity or project-structure wording; not a reusable general concept entry."
        else:
            status, rationale = "YES", "Accepted, current-valid compact concept, practical expression, sign, or UI state/action with source-bounded context."
        if status == "CORPUS_ONLY" and cid not in REVIEW:
            rationale = rationale or "Source-bounded discourse evidence."
        rec["dictionary_eligibility"] = status
        rec["eligibility_rationale"] = rationale
        eligibility.append({"corpus_record_id": cid, "intent": intent, "eligibility": status, "rationale": rationale, "dictionary_entry_id": None, "review_question": rationale if status == "REVIEW" else None})
        dict_groups[status].append(rec)

    for rec in corpus:
        if rec.get("reconciliation_disposition") == "ACCEPTED_HISTORICAL_ONLY_INCOMPATIBLE":
            rec["dictionary_eligibility"] = "HISTORICAL_ONLY"
            rec["eligibility_rationale"] = "Creator accepted the exact historical message, but place_hotel is absent from the current registry; no current equivalent is supplied, so this remains non-executable historical evidence outside the Dictionary candidate."

    # Stable candidate entries; do not collapse differing intent/applicability.
    entries: list[dict[str, Any]] = []
    by_key: dict[str, dict[str, Any]] = {}
    for rec in dict_groups["YES"]:
        intent = rec["neighbourhoods"][0].get("canonical_intent", "")
        app = rec["applicability"]
        key_data = {"intent": intent, "message": rec["message"], "mode": sorted({a["communication_mode"] for a in app}), "surface": sorted({a["communication_surface"] for a in app}), "context": app}
        key = json.dumps(key_data, sort_keys=True, ensure_ascii=False)
        if key not in by_key:
            eid = f"pcd-v01-{len(entries)+1:04d}"
            examples = [x for x in rec["neighbourhoods"][0].get("semantic_examples", []) if not x.startswith("Required target slots:")]
            ent = {"dictionary_entry_id": eid, "headword": DISPLAY_LABELS.get(rec["corpus_record_id"], intent), "semantic_neighbourhood": intent, "label_status": "LOOKUP_LABEL / NOT CANONICAL ENGLISH MEANING", "aliases_or_examples": examples, "variants": [], "usage_explanation": "See the evidence-bounded semantic neighbourhood and applicability below; English is a lookup/display label.", "known_ambiguity": rec["neighbourhoods"][0].get("known_ambiguities", []), "corpus_record_ids": [], "source_evidence_summary": [], "provenance_detail": []}
            entries.append(ent); by_key[key] = ent
        ent = by_key[key]
        ent["corpus_record_ids"].append(rec["corpus_record_id"])
        ent["variants"].append({"corpus_record_id": rec["corpus_record_id"], "message": rec["message"], "token_sequence": token_label(rec["message"]), "render": f"../renders/{rec['corpus_record_id']}.svg", "mode": sorted({a["communication_mode"] for a in rec["applicability"]}), "surface": sorted({a["communication_surface"] for a in rec["applicability"]}), "context": rec["applicability"]})
        ent["source_evidence_summary"].append(f"{rec['source_family']} / Harvest {hist_id}")
        ent["provenance_detail"].append(rec["provenance"])
        rec["dictionary_entry_id"] = ent["dictionary_entry_id"]
        next(x for x in eligibility if x["corpus_record_id"] == rec["corpus_record_id"])["dictionary_entry_id"] = ent["dictionary_entry_id"]

    render_results = []
    for rec in current:
        msg = rec["message"]
        errors = schema_errors(msg) + semantic_errors(msg)
        rid = rec["corpus_record_id"]
        if errors:
            rec["render_status"] = "NOT_RENDERED_INVALID_CURRENT_MESSAGE"
            render_results.append({"corpus_record_id": rid, "status": "INVALID", "errors": errors})
            continue
        svg, _ = render_svg(msg, registry=registry)
        (OUT / "renders" / f"{rid}.svg").write_text(svg, encoding="utf-8")
        rec["render"] = f"renders/{rid}.svg"
        rec["render_status"] = "RENDERED_CANONICAL"
        render_results.append({"corpus_record_id": rid, "status": "RENDERED_CANONICAL", "path": f"renders/{rid}.svg"})
    # Replace dictionary relative render links with links from the viewer directory.
    for ent in entries:
        for variant in ent["variants"]:
            variant["render"] = f"../renders/{variant['corpus_record_id']}.svg"
    current_by_id = {r["corpus_record_id"]: r for r in current}
    for r in corpus:
        current_id = r.get("current_record_id")
        if current_id in current_by_id:
            cur = current_by_id[current_id]
            for key in ("render", "render_status", "dictionary_eligibility", "eligibility_rationale", "dictionary_entry_id"):
                if key in cur:
                    r[key] = cur[key]
    current_by_id = {r["corpus_record_id"]: r for r in current}
    for r in corpus:
        current_id = r.get("current_record_id")
        if current_id in current_by_id:
            cur = current_by_id[current_id]
            for key in ("render", "render_status", "dictionary_eligibility", "eligibility_rationale", "dictionary_entry_id"):
                if key in cur:
                    r[key] = cur[key]

    for row in lineage:
        row["eligibility"] = next((x["eligibility"] for x in eligibility if x["corpus_record_id"] == row["current_record_id"]), "DEFERRED_BLOCKED")
    write(OUT / "accepted-corpus.json", {"baseline_version": "0.1", "status": "HUMAN-RECONCILED BASELINE", "records": corpus})
    write(OUT / "dictionary-candidate.json", {"candidate_version": "0.1", "status": "SYSTEM-CLASSIFIED / AWAITING CREATOR ELIGIBILITY REVIEW", "entries": entries})
    write(OUT / "dictionary-eligibility.json", {"classification_authority": "SYSTEM CANDIDATE; CREATOR REVIEW NOT YET PERFORMED", "records": eligibility})
    write(OUT / "lineage.json", {"records": lineage})
    write(OUT / "negative-evidence.json", {"records": negative})
    write(OUT / "blocked.json", {"records": blocked})
    write(OUT / "reconciliation-accounting.json", {"records": accounting})
    manifest_out = {
        "baseline_version": "0.1", "created_on": "2026-09-27", "status": "RESEARCH BASELINE / NOT NORMATIVE GRAMMAR",
        "source_harvest": manifest["harvest_id"], "source_harvest_snapshot": manifest["snapshot_commit"],
        "creator_export": {"path": "../composition-library-historical-harvest-v0.1/reconciliation/creator-export-2026-09-27.json", "sha256": export_sha, "reviewed_count": exp["reviewed_count"], "unreviewed_count": exp["unreviewed_count"], "decision_counts": original_count},
        "addendum": {"path": "../composition-library-historical-harvest-v0.1/reconciliation/creator-reconciliation-addendum-2026-09-27.json", "sha256": hashlib.sha256(ADDENDUM.read_bytes()).hexdigest(), "harvest_snapshot": add["harvest_snapshot"], "cases": sorted(decisions)},
        "input_commit": "45609d58ad55de975ae8e4b316fa84b101677dcd",
        "counts": {"harvest_candidates": len(harvest_entries), "corpus_records_including_history_and_replacements": len(corpus), "current_accepted": len(current), "accepted_unchanged": sum(x["final_disposition"] == "ACCEPTED_UNCHANGED" for x in accounting), "accepted_historical_only_incompatible": sum(x["final_disposition"] == "ACCEPTED_HISTORICAL_ONLY_INCOMPATIBLE" for x in accounting), "accepted_replacements": len(replacements), "blocked": len(blocked), "negative_or_superseded": len(negative), "dictionary_yes": len(dict_groups["YES"]), "dictionary_corpus_only": len(dict_groups["CORPUS_ONLY"]), "dictionary_review": len(dict_groups["REVIEW"]), "dictionary_entries": len(entries), "entries_with_multiple_composition_variants": sum(len(x["variants"]) > 1 for x in entries), "entries_with_embodied_variant": sum(any("EMBODIED" in v["mode"] for v in x["variants"]) for x in entries), "entries_with_standalone_variant": sum(any("STANDALONE" in v["mode"] for v in x["variants"]) for x in entries), "entries_with_known_ambiguity": sum(bool(x["known_ambiguity"]) for x in entries), "review_queue": len(dict_groups["REVIEW"]), "renders": sum(x["status"] == "RENDERED_CANONICAL" for x in render_results), "historical_only_compatibility": sum(1 for r in corpus if r.get("reconciliation_disposition") == "ACCEPTED_HISTORICAL_ONLY_INCOMPATIBLE"), "records_with_tests": sum(bool(r.get("tests")) for r in current), "records_with_failures_or_ambiguities": sum(bool(r.get("failures")) or any(n.get("known_ambiguities") for n in r.get("neighbourhoods", [])) for r in current)},
        "validation": {"export_sha": "PASS", "harvest_ids": "PASS", "addendum_binding": "PASS", "current_message_schema_shape_and_registry_validation": "PASS" if all(x["status"] == "RENDERED_CANONICAL" for x in render_results) else "FAIL", "canonical_renderer": "PASS" if all(x["status"] == "RENDERED_CANONICAL" for x in render_results) else "FAIL"},
    }
    write(OUT / "render-manifest.json", {"renders": render_results})
    write(OUT / "manifest.json", manifest_out)
    write(OUT / "validation.json", {"message_validation": render_results, "rendered": sum(x["status"] == "RENDERED_CANONICAL" for x in render_results), "failed": [x for x in render_results if x["status"] != "RENDERED_CANONICAL"]})
    make_viewers(corpus, current, entries, dict_groups, negative, blocked)
    artifact_paths = ["accepted-corpus.json", "dictionary-candidate.json", "dictionary-eligibility.json", "lineage.json", "negative-evidence.json", "blocked.json", "reconciliation-accounting.json", "review/corpus.html", "review/dictionary.html", "review/eligibility-review.html", "review/replacement-qa.html", "corpus-only-summary.md", "explicit-color-modifier-repair.md"]
    manifest_out["artifact_sha256"] = {p: hashlib.sha256((OUT / p).read_bytes()).hexdigest() for p in artifact_paths}
    render_hash = hashlib.sha256()
    for p in sorted((OUT / "renders").glob("*.svg")):
        render_hash.update(p.name.encode("utf-8") + b"\0" + p.read_bytes())
    manifest_out["render_bundle_sha256"] = render_hash.hexdigest()
    write(OUT / "manifest.json", manifest_out)
    print(json.dumps(manifest_out["counts"], indent=2))

def make_viewers(corpus: list[dict[str, Any]], current: list[dict[str, Any]], entries: list[dict[str, Any]], groups: dict[str, list[dict[str, Any]]], negative: list[dict[str, Any]], blocked: list[dict[str, Any]]) -> None:
    # Embed compact display payloads so the pages also work from file://.
    cc=[]
    for r in corpus:
        cc.append({"id":r["corpus_record_id"],"status":r.get("reconciliation_disposition", "ACCEPTED_REPLACEMENT"),"kind":r["record_kind"],"historical":r.get("reconciliation_disposition") not in {"ACCEPTED_UNCHANGED", "ACCEPTED_REPLACEMENT"},"source":r.get("source_harvest",{}).get("composition_id",r["corpus_record_id"]),"sourceHref":"../../composition-library-historical-harvest-v0.1/records/"+r.get("source_harvest",{}).get("composition_id",r["corpus_record_id"])+".json","family":r.get("source_family",source_family_for(r["corpus_record_id"])),"message":r.get("current_message") or r.get("historical_message") or r.get("message"),"sequence":r.get("sequence") or r.get("historical_sequence",""),"intent":"HOTEL + BLUE + GOOD" if r["corpus_record_id"]=="clh-v01-0010" else (r.get("semantic_neighbourhoods") or r.get("neighbourhoods") or [{}])[0].get("canonical_intent", ""),"eligibility":r.get("dictionary_eligibility", r.get("historical_dictionary_status", "HISTORICAL")),"render":r.get("render"),"context":r.get("applicability",[]),"tests":r.get("tests",[]),"failures":r.get("failures",[]),"lineage":r.get("current_record_id"),"statusNote":r.get("render_status", "")})
    corpus_html='''<!doctype html><meta charset="utf-8"><title>Accepted Corpus Baseline v0.1 — review</title><style>body{font:15px system-ui;max-width:1300px;margin:2rem auto;padding:0 1rem;color:#151515}header{position:sticky;top:0;background:white;padding:1rem 0;border-bottom:1px solid #bbb}select,input{padding:.45rem;margin:.25rem}article{border-bottom:1px solid #bbb;padding:1rem 0;display:grid;grid-template-columns:220px 1fr;gap:1rem}.art img{max-width:210px;max-height:180px}.muted{color:#666}code{overflow-wrap:anywhere}.bad{color:#8a2800}</style><h1>Accepted Composition Corpus Baseline v0.1</h1><p>Internal research QA. Historical and negative evidence are labelled; this Corpus is not normative Grammar. Blocked hotel/color has no current render.</p><header><input id="q" placeholder="Search ID, intent, token"><select id="s"><option value="">All statuses</option></select><select id="f"><option value="">All source families</option></select><select id="m"><option value="">All modes</option></select><select id="u"><option value="">All surfaces</option></select><select id="e"><option value="">All eligibility</option></select><label><input id="fail" type="checkbox"> has failures</label><label><input id="hist" type="checkbox"> historical only</label><span id="count"></span></header><main id="items"></main><script>'''+"const D="+json.dumps(cc,ensure_ascii=False,separators=(",",":")).replace("<", "\\u003c")+''';const $=x=>document.getElementById(x),esc=x=>String(x??"").replace(/[&<>]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;"}[c])).replaceAll(String.fromCharCode(34),"&quot;").replaceAll(String.fromCharCode(39),"&#39;");for(const [id,k] of [["s","status"],["f","family"],["e","eligibility"]])for(const v of [...new Set(D.map(x=>x[k]))].sort()){let o=document.createElement("option");o.value=v;o.textContent=v;$(id).append(o)}for(const [id,k] of [["m","communication_mode"],["u","communication_surface"]]){const vals=[...new Set(D.flatMap(x=>x.context.flatMap(a=>[a[k]||a["communication_"+k.split("_")[1]]]).filter(Boolean)))].sort();for(const v of vals){let o=document.createElement("option");o.value=v;o.textContent=v;$(id).append(o)}}function render(){let a=D.filter(x=>(!$("q").value||JSON.stringify(x).toLowerCase().includes($("q").value.toLowerCase()))&&(!$("s").value||x.status===$("s").value)&&(!$("f").value||x.family===$("f").value)&&(!$("e").value||x.eligibility===$("e").value)&&(!$("m").value||x.context.some(c=>c.communication_mode===$("m").value))&&(!$("u").value||x.context.some(c=>c.communication_surface===$("u").value))&&(!$("fail").checked||x.failures.length)&&(!$("hist").checked||x.historical));$("count").textContent=` ${a.length} / ${D.length}`;$("items").innerHTML=a.map(x=>`<article id="${esc(x.id)}"><div class="art">${x.render?`<img src="../${esc(x.render)}">`:x.id==="clh-v01-0010"?"NO VALID CURRENT MESSAGE — COLOR MECHANISM BLOCKED":"No current render"}</div><div><h2>${esc(x.id)} <small>${esc(x.status)}</small></h2><p><b>${esc(x.intent)}</b></p><p>${esc(x.sequence)}</p><p>${esc(x.family)} · ${esc(x.eligibility)} · current/replacement: ${esc(x.lineage)}</p><p>${esc(JSON.stringify(x.context))}</p><p>Source record: <a href="${esc(x.sourceHref)}">${esc(x.source)}</a></p><details><summary>Tests, failures, provenance</summary><pre>${esc(JSON.stringify({tests:x.tests,failures:x.failures,source:x.source},null,2))}</pre></details></div></article>`).join("")}for(const id of ["q","s","f","m","u","e","fail","hist"])$(id).addEventListener("input",render);render()</script>'''
    (OUT/"review/corpus.html").write_text(corpus_html,encoding="utf-8")
    dd=json.dumps(entries,ensure_ascii=False,separators=(",",":")).replace("<", "\\u003c")
    dict_html='''<!doctype html><meta charset="utf-8"><title>Public Composition Dictionary Candidate v0.1</title><style>body{font:16px system-ui;max-width:1150px;margin:2rem auto;padding:0 1rem;color:#161616}header{position:sticky;top:0;background:white;padding:1rem 0;border-bottom:1px solid #bbb}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(290px,1fr));gap:1rem}article{border:1px solid #bbb;border-radius:8px;padding:1rem}.viz{min-height:120px;display:flex;align-items:center}.viz img{max-width:100%;max-height:150px}button{padding:.5rem;margin:.2rem}</style><h1>Public Composition Dictionary Candidate v0.1</h1><p>Internal candidate only — English labels are lookup labels, not canonical translations. Creator eligibility review remains pending; this is not a public Dictionary.</p><header><input id="q" placeholder="Search candidate entries"><span id="count"></span></header><main id="cards" class="grid"></main><script>const D='''+dd+''';const $=x=>document.getElementById(x),e=x=>String(x??"").replace(/[&<>]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;"}[c])).replaceAll(String.fromCharCode(34),"&quot;").replaceAll(String.fromCharCode(39),"&#39;");function draw(){let a=D.filter(x=>JSON.stringify(x).toLowerCase().includes($("q").value.toLowerCase()));$("count").textContent=`${a.length} entries`;$("cards").innerHTML=a.map(x=>`<article>${x.variants.map(v=>`<div class="viz"><img src="${e(v.render)}"></div>`).join("")}<h2>${e(x.headword)}</h2><p><small>Lookup/display label; semantic neighborhood and context remain authoritative.</small></p><p><b>Also:</b> ${e(x.aliases_or_examples.join(" / "))}</p><p>${e(x.usage_explanation)}</p><p><b>Mode / surface:</b> ${e(x.variants.map(v=>v.mode.join(", ")+" / "+v.surface.join(", ")).join("; "))}</p><p><b>Exact sequence:</b> <code>${e(x.variants.map(v=>v.token_sequence).join("; "))}</code></p><p><b>Context:</b> ${e(JSON.stringify(x.variants.map(v=>v.context)))}</p><p><b>Evidence:</b> ${e(x.source_evidence_summary.join("; "))}</p><p>Evidence: ${x.corpus_record_ids.map(id=>`<a href="corpus.html#${e(id)}">${e(id)}</a>`).join(", ")}</p><details><summary>Provenance</summary><pre>${e(JSON.stringify(x.provenance_detail,null,2))}</pre></details><p>Eligibility: SYSTEM CANDIDATE — choose KEEP_IN_DICTIONARY / MOVE_TO_CORPUS_ONLY / REVIEW_LATER after human review.</p></article>`).join("")}$("q").addEventListener("input",draw);draw()</script>'''
    (OUT/"review/dictionary.html").write_text(dict_html,encoding="utf-8")
    rr=[x for x in groups["REVIEW"]]
    review_data=[{"id":x["corpus_record_id"],"intent":x["neighbourhoods"][0].get("canonical_intent"),"source":x["source_family"],"why":x["eligibility_rationale"],"sequence":token_label(x["message"]),"render":f"../renders/{x['corpus_record_id']}.svg","mode":sorted({a["communication_mode"] for a in x["applicability"]}),"surface":sorted({a["communication_surface"] for a in x["applicability"]}),"context":x["applicability"],"corpus_record_id":x["corpus_record_id"]} for x in rr]
    (OUT/"review/eligibility-review.html").write_text('''<!doctype html><meta charset="utf-8"><title>Dictionary Eligibility Review Queue</title><style>body{font:16px system-ui;max-width:1100px;margin:2rem auto;padding:0 1rem}article{border-bottom:1px solid #aaa;padding:1rem 0;display:grid;grid-template-columns:200px 1fr;gap:1rem}img{max-width:190px;max-height:150px}</style><h1>Dictionary eligibility review queue</h1><p>System classification only. Review the specific editorial question; do not re-review semantic acceptance. Later creator actions: KEEP_IN_DICTIONARY, MOVE_TO_CORPUS_ONLY, REVIEW_LATER, or EDIT_ENTRY_METADATA. Decisions are not recorded by this static viewer.</p><main id="items"></main><script>const D='''+json.dumps(review_data,ensure_ascii=False,separators=(",",":")).replace("<", "\\u003c")+''';const e=x=>String(x??"").replace(/[&<>]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;"}[c])).replaceAll(String.fromCharCode(34),"&quot;").replaceAll(String.fromCharCode(39),"&#39;");document.getElementById("items").innerHTML=D.map(x=>`<article><img src="${e(x.render)}"><div><h2>${e(x.id)} — ${e(x.intent)}</h2><p><b>Source:</b> ${e(x.source)} · ${e(x.mode.join(", "))} / ${e(x.surface.join(", "))}</p><p><b>Exact tokens:</b> ${e(x.sequence)}</p><p><b>Question:</b> ${e(x.why)}</p><details><summary>Context/evidence</summary><pre>${e(JSON.stringify(x.context,null,2))}</pre></details><p>Decision to record later: KEEP_IN_DICTIONARY / MOVE_TO_CORPUS_ONLY / REVIEW_LATER / EDIT_ENTRY_METADATA.</p></div></article>`).join("")</script>''',encoding="utf-8")
    replacement_ids = ["clc-v01-0008-r1", "clc-v01-0012-r1", "clc-v01-0070-r1"]
    comparisons = []
    for rid in replacement_ids:
        rec = next(x for x in current if x["corpus_record_id"] == rid)
        hid = rec["source_harvest_id"]
        comparisons.append((rec["neighbourhoods"][0]["canonical_intent"], hid, rid, token_label(rec["message"]), None))
    comparisons.append(("HOTEL + BLUE + GOOD", "clh-v01-0010", None, "NO VALID CURRENT MESSAGE — COLOR MECHANISM BLOCKED", "Explicit Color Modifier Mechanism required; no blue tile is faked."))
    rows = []
    for title, hid, rid, seq, note in comparisons:
        old = f"../../composition-library-historical-harvest-v0.1/renders/{hid}.svg"
        new = f"../renders/{rid}.svg" if rid else ""
        rows.append(f'<section><h2>{esc(title)}</h2><div class="pair"><div><h3>Historical</h3><img src="{old}" alt="Historical {hid}"><p>{hid}</p></div><div><h3>{"Creator replacement" if rid else "Blocked target"}</h3>{f"<img src=\"{new}\" alt=\"{rid}\">" if rid else f"<p class=\"blocked\">{esc(seq)}</p><p>{esc(note)}</p>"}<p>{esc(seq)}</p></div></div></section>')
    (OUT/"review/replacement-qa.html").write_text('<!doctype html><meta charset="utf-8"><title>Creator replacement visual QA</title><style>body{font:16px system-ui;max-width:1100px;margin:2rem auto;padding:0 1rem}section{border-bottom:1px solid #aaa;padding:1rem 0}.pair{display:grid;grid-template-columns:1fr 1fr;gap:2rem}img{max-width:100%;height:140px;object-fit:contain;background:white}.blocked{min-height:100px;padding:2rem;border:1px dashed #777}</style><h1>Creator replacement visual QA</h1><p>Canonical Renderer output for exact current replacements; the blocked color target has no fabricated render.</p>'+''.join(rows),encoding="utf-8")

def source_family_for(cid: str) -> str:
    return "CREATOR_RECONCILIATION" if cid.startswith("clc-") else "HISTORICAL HARVEST"

if __name__ == "__main__":
    main()
