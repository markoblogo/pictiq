(function () {
  "use strict";

  var EXPECTED = {
    harvestId: "pictiq-composition-library-historical-harvest-v0.1",
    harvestVersion: "0.1",
    snapshot: "8fae507",
    count: 81,
    evidenceOnly: 86,
    unsafe: 7,
    reviewSha256: "59497cd6eef91732de7a2bae44b5e5953847f1ad0f9935787e8c0746f7572084",
    manifestSha256: "4d284c8e0d93266411698ff96e42ffe5f8172099e9a8d5195b478c730c53dccf"
  };
  var RECONCILIATION_VERSION = "pictiq-composition-human-reconciliation-v0.1";
  var STORAGE_KEY = "pictiq-composition-human-reconciliation-v0.1-8fae507";
  var DECISIONS = ["ACCEPT", "ACCEPT_CONTEXTUAL", "EDIT", "REJECT", "EVIDENCE_ONLY", "UNREVIEWED"];
  var TAGS = ["SEMANTICS", "CONTEXT", "AMBIGUOUS", "LOSSY", "MESSAGE_BOUNDARY", "PROVENANCE", "HISTORICAL", "COMPATIBILITY", "NEEDS_REBUILD", "TOO_EXPLICIT", "TOO_COMPRESSED", "SURFACE_SPECIFIC", "MODE_SPECIFIC", "FAILURE_EVIDENCE", "OTHER"];
  var DECISION_TEXT = {
    ACCEPT: "Suitable for the first accepted Composition Library baseline as represented.",
    ACCEPT_CONTEXTUAL: "Suitable only under explicitly recorded mode, surface, or context constraints.",
    EDIT: "Underlying intent/use is useful, but the Message, semantics, context, boundaries, or metadata need creator correction before acceptance.",
    REJECT: "Do not include this composition in the accepted baseline.",
    EVIDENCE_ONLY: "Preserve as historical/test/failure evidence; do not treat as an accepted reusable composition.",
    UNREVIEWED: "No creator decision yet."
  };
  var PASS_ORDER = {
    "HANDBOOK": 1,
    "ROAD _ WAYFINDING": 1,
    "WEB_UI": 1,
    "LANDING": 1,
    "ODYSSEY": 2,
    "STRESS TEST 05": 2,
    "CONSTRAINED TRANSLATION PILOT 04A": 3
  };
  var PASS_LABEL = {
    1: "Pass 1 — Stronger / easier sources",
    2: "Pass 2 — Complex compositions",
    3: "Pass 3 — Problem / experimental material"
  };
  var records = [];
  var byId = new Map();
  var ordered = [];
  var overlay = {};
  var currentId = null;
  var quickFilter = "";
  var compareIds = [];
  var locked = true;
  var storageAvailable = true;
  var storageMessage = "";

  function $(id) { return document.getElementById(id); }
  function text(node, value) { node.textContent = value == null ? "" : String(value); }
  function make(tag, className, content) {
    var node = document.createElement(tag);
    if (className) node.className = className;
    if (content != null) text(node, content);
    return node;
  }
  function addOption(select, value, label) {
    var option = make("option", "", label);
    option.value = value;
    select.appendChild(option);
  }
  function sha256(buffer) {
    return crypto.subtle.digest("SHA-256", buffer).then(function (hash) {
      return Array.from(new Uint8Array(hash)).map(function (b) { return b.toString(16).padStart(2, "0"); }).join("");
    });
  }
  function getPass(candidate) {
    var rank = PASS_ORDER[candidate.source_family];
    if (!rank) rank = 3;
    var label = PASS_LABEL[rank];
    if (candidate.source_family === "HANDBOOK") label += " · Handbook";
    else if (candidate.source_family === "ROAD _ WAYFINDING") label += " · Road / Wayfinding";
    else if (candidate.source_family === "WEB_UI") label += " · Web/UI";
    else if (candidate.source_family === "LANDING") label += " · Landing";
    else if (candidate.source_family === "ODYSSEY") label += " · Odyssey";
    else if (candidate.source_family === "STRESS TEST 05") label += " · Stress Test 05";
    else if (candidate.source_family === "CONSTRAINED TRANSLATION PILOT 04A") label += " · Constrained Translation Pilot 04A";
    else label += " · Remaining / issue evidence";
    return {rank: rank, label: label};
  }
  function wrapper(candidate) {
    var frames = Array.isArray(candidate.pictiq_sequence_human_readable) ? candidate.pictiq_sequence_human_readable : [];
    var preservation = Array.isArray(candidate.preservation) ? candidate.preservation : [];
    var failures = Array.isArray(candidate.failures) ? candidate.failures : [];
    return {
      candidate: candidate,
      pass: getPass(candidate),
      multiFrame: frames.length > 1,
      historical: !!(candidate.compatibility && candidate.compatibility.message_validity === "HISTORICAL"),
      failureEvidence: failures.length > 0 || preservation.indexOf("LOSSY") !== -1 || preservation.indexOf("GAP") !== -1
    };
  }
  function decision(id) {
    var item = overlay[id];
    return item && DECISIONS.indexOf(item.primary_decision) !== -1 ? item.primary_decision : "UNREVIEWED";
  }
  function tagsFor(id) { return overlay[id] && Array.isArray(overlay[id].reason_tags) ? overlay[id].reason_tags : []; }
  function notesFor(id) { return overlay[id] && typeof overlay[id].human_notes === "string" ? overlay[id].human_notes : ""; }
  function setStatus(message, isError) {
    var node = $("action-status");
    text(node, message);
    node.setAttribute("role", isError ? "alert" : "status");
    node.className = isError ? "action-status error-text" : "action-status";
  }
  function setLocked(message) {
    locked = true;
    var warning = $("lock-warning");
    text(warning, message);
    warning.hidden = false;
    ["export-button", "clear-button", "previous-button", "next-button", "next-unreviewed-button", "jump-select"].forEach(function (id) { $(id).disabled = true; });
    $("record-panel").replaceChildren(make("p", "", "Review controls are disabled until the frozen Harvest integrity check passes."));
    $("storage-status").textContent = "Harvest integrity check failed.";
  }
  function appendBlock(parent, title, values) {
    var block = make("section", "metadata-block");
    block.appendChild(make("h3", "", title));
    if (Array.isArray(values)) {
      if (!values.length) block.appendChild(make("p", "muted", "None recorded."));
      else {
        var list = make("ul");
        values.forEach(function (value) {
          var li = make("li");
          if (typeof value === "string") text(li, value);
          else {
            text(li, [value.observed_interpretation, value.failure_type, value.disposition, value.status, value.reference, value.notes].filter(Boolean).join(" · "));
          }
          list.appendChild(li);
        });
        block.appendChild(list);
      }
    } else block.appendChild(make("p", "", values || "Not recorded."));
    parent.appendChild(block);
  }
  function recordRefs(candidate) {
    var list = [];
    if (candidate.origin && candidate.origin.reference) list.push(candidate.origin.reference);
    (candidate.where_used || []).forEach(function (ref) { if (list.indexOf(ref) === -1) list.push(ref); });
    return list;
  }
  function related(candidate) {
    var ownSequence = JSON.stringify(candidate.pictiq_sequence_human_readable || []);
    return records.filter(function (other) {
      if (other.composition_id === candidate.composition_id) return false;
      return other.canonical_intent === candidate.canonical_intent || JSON.stringify(other.pictiq_sequence_human_readable || []) === ownSequence;
    });
  }
  function addFlag(parent, label, type) { parent.appendChild(make("span", "badge " + (type || "neutral"), label)); }
  function renderRecord() {
    var panel = $("record-panel");
    panel.replaceChildren();
    if (!currentId || !byId.has(currentId)) {
      panel.appendChild(make("p", "muted", "No record matches the current filters."));
      return;
    }
    var item = byId.get(currentId);
    var candidate = item.candidate;
    var top = make("div", "record-top");
    var titleGroup = make("div");
    titleGroup.appendChild(make("h2", "", candidate.composition_id));
    titleGroup.appendChild(make("p", "muted", "Source family: " + candidate.source_family + " · provenance: " + (candidate.provenance_quality || "not stated")));
    top.appendChild(titleGroup);
    var badges = make("div", "record-badges");
    addFlag(badges, item.pass.label, "neutral");
    if (item.multiFrame) addFlag(badges, "MULTI-FRAME / CHECK MESSAGE BOUNDARY", "alert");
    if (item.historical) addFlag(badges, "HISTORICAL COMPATIBILITY", "alert");
    if (item.failureEvidence) addFlag(badges, "HAS FAILURE EVIDENCE", "alert");
    top.appendChild(badges);
    panel.appendChild(top);

    var hero = make("div", "record-hero");
    var renderBox = make("div", "render-box");
    var image = document.createElement("img");
    image.src = "../" + candidate.visual_render;
    image.alt = "Canonical Renderer preview for " + candidate.composition_id + ": " + (candidate.pictiq_sequence_human_readable || []).join(" ; ");
    image.onerror = function () { text(renderBox, "Renderer preview could not be loaded: " + candidate.visual_render); };
    renderBox.appendChild(image);
    hero.appendChild(renderBox);
    var intent = make("div", "intent-block");
    intent.appendChild(make("h3", "", candidate.canonical_intent || "Intent not recorded"));
    (candidate.semantic_examples || []).forEach(function (example) { intent.appendChild(make("p", "", example)); });
    intent.appendChild(make("p", "muted", (candidate.communication_mode || "Mode unknown") + " · " + (candidate.communication_surface || "Surface unknown")));
    var sequenceTitle = make("h4", "", "Exact Pictiq token sequence");
    intent.appendChild(sequenceTitle);
    var sequences = make("ol", "token-list");
    (candidate.pictiq_sequence_human_readable || []).forEach(function (frame, index) {
      var li = make("li");
      if (item.multiFrame) li.appendChild(make("span", "muted", "Frame " + (index + 1) + ": "));
      li.appendChild(make("code", "", frame));
      sequences.appendChild(li);
    });
    intent.appendChild(sequences);
    hero.appendChild(intent);
    panel.appendChild(hero);

    var metadata = make("div", "metadata-grid");
    appendBlock(metadata, "Context", candidate.context_summary);
    appendBlock(metadata, "context_supplies", candidate.context_supplies || []);
    appendBlock(metadata, "Preservation assessments", candidate.preservation || []);
    appendBlock(metadata, "Harvest lifecycle", candidate.lifecycle || "Not recorded");
    appendBlock(metadata, "Compatibility", [((candidate.compatibility || {}).message_validity || "UNKNOWN") + " · Pictiq " + ((candidate.compatibility || {}).pictiq_version || "unknown") + " · Message Schema " + ((candidate.compatibility || {}).message_schema_version || "unknown")]);
    appendBlock(metadata, "Origin", [candidate.origin && candidate.origin.reference, candidate.origin && candidate.origin.status, candidate.origin && candidate.origin.notes].filter(Boolean));
    appendBlock(metadata, "Uses", candidate.where_used || []);
    appendBlock(metadata, "Tests", candidate.tests || []);
    appendBlock(metadata, "Failures / ambiguity", candidate.failures || []);
    appendBlock(metadata, "Harvest issues", candidate.issues || []);
    panel.appendChild(metadata);

    if (item.failureEvidence) {
      var summary = make("div", "evidence-summary failure-box");
      summary.appendChild(make("strong", "", "HAS FAILURE EVIDENCE"));
      if ((candidate.failures || []).length) {
        (candidate.failures || []).forEach(function (failure) {
          summary.appendChild(make("p", "", [failure.observed_interpretation, failure.failure_type, failure.disposition].filter(Boolean).join(" · ")));
        });
      } else {
        summary.appendChild(make("p", "", "Preservation assessment: " + (candidate.preservation || []).filter(function (x) { return x === "LOSSY" || x === "GAP"; }).join(", ")));
        (candidate.issues || []).forEach(function (issue) { summary.appendChild(make("p", "", issue)); });
      }
      panel.appendChild(summary);
    }

    var relatives = related(candidate);
    if (relatives.length) {
      var rel = make("section", "evidence-summary");
      rel.appendChild(make("h3", "", "Related records in Harvest"));
      var relList = make("div", "related-list");
      relatives.forEach(function (other) {
        var reason = other.canonical_intent === candidate.canonical_intent ? "same intent" : "same exact token sequence";
        var b = make("button", "", other.composition_id + " · " + reason);
        b.type = "button";
        b.addEventListener("click", function () { selectRecord(other.composition_id); });
        relList.appendChild(b);
      });
      rel.appendChild(relList);
      panel.appendChild(rel);
    }
    panel.appendChild(makeDecisionForm(candidate));
  }
  function makeDecisionForm(candidate) {
    var form = make("section", "decision-form");
    var decisionLabel = make("label", "", "Creator decision");
    decisionLabel.htmlFor = "primary-decision";
    form.appendChild(decisionLabel);
    var select = make("select", "decision-select");
    select.id = "primary-decision";
    DECISIONS.forEach(function (value) { addOption(select, value, value); });
    select.value = decision(candidate.composition_id);
    select.addEventListener("change", function () {
      updateItem(candidate.composition_id, "primary_decision", select.value);
      renderQueue();
    });
    form.appendChild(select);
    var definitions = make("div", "decision-definitions");
    DECISIONS.forEach(function (value) {
      var entry = make("div");
      entry.appendChild(make("strong", "", value));
      entry.appendChild(make("span", "", DECISION_TEXT[value]));
      definitions.appendChild(entry);
    });
    form.appendChild(definitions);

    var fieldset = make("fieldset", "tag-fieldset");
    fieldset.appendChild(make("legend", "", "Optional reason tags · multi-select"));
    var options = make("div", "tag-options");
    TAGS.forEach(function (tag, index) {
      var id = "reason-tag-" + index;
      var label = make("label");
      var input = document.createElement("input");
      input.type = "checkbox";
      input.id = id;
      input.checked = tagsFor(candidate.composition_id).indexOf(tag) !== -1;
      input.addEventListener("change", function () {
        var selected = tagsFor(candidate.composition_id).slice();
        if (input.checked && selected.indexOf(tag) === -1) selected.push(tag);
        if (!input.checked) selected = selected.filter(function (value) { return value !== tag; });
        updateItem(candidate.composition_id, "reason_tags", selected);
        renderProgress();
        renderQueue();
      });
      label.htmlFor = id;
      label.appendChild(input);
      label.appendChild(document.createTextNode(tag));
      options.appendChild(label);
    });
    fieldset.appendChild(options);
    form.appendChild(fieldset);

    var notesLabel = make("label", "notes-label", "Creator notes");
    notesLabel.htmlFor = "human-notes";
    form.appendChild(notesLabel);
    var notes = make("textarea");
    notes.id = "human-notes";
    notes.value = notesFor(candidate.composition_id);
    notes.placeholder = "Record your own reasoning or requested correction. Notes are not interpreted automatically.";
    notes.addEventListener("input", function () { updateItem(candidate.composition_id, "human_notes", notes.value); });
    form.appendChild(notes);
    return form;
  }
  function updateItem(id, key, value) {
    if (!overlay[id]) overlay[id] = {primary_decision: "UNREVIEWED", reason_tags: [], human_notes: ""};
    overlay[id][key] = value;
    overlay[id].updated_at = new Date().toISOString();
    if (overlay[id].primary_decision === "UNREVIEWED" && !overlay[id].reason_tags.length && !overlay[id].human_notes) delete overlay[id];
    saveOverlay();
    renderProgress();
  }
  function saveOverlay() {
    try {
      var compact = {};
      Object.keys(overlay).forEach(function (id) {
        var item = overlay[id];
        if (decision(id) !== "UNREVIEWED" || (item.reason_tags || []).length || item.human_notes) compact[id] = item;
      });
      localStorage.setItem(STORAGE_KEY, JSON.stringify({
        reconciliation_version: RECONCILIATION_VERSION,
        harvest_version: EXPECTED.harvestVersion,
        harvest_snapshot: EXPECTED.snapshot,
        records: compact
      }));
      storageAvailable = true;
      $("persistence-warning").hidden = true;
      text($("storage-status"), "Saved locally in this browser · not a Harvest edit");
    } catch (error) {
      storageAvailable = false;
      $("persistence-warning").hidden = false;
      text($("persistence-warning"), "Local persistence is unavailable. Keep an exported JSON copy before leaving this page.");
      text($("storage-status"), "Decisions currently exist only in this page.");
    }
  }
  function loadOverlay() {
    var raw;
    try { raw = localStorage.getItem(STORAGE_KEY); }
    catch (error) {
      storageAvailable = false;
      $("persistence-warning").hidden = false;
      text($("persistence-warning"), "This browser blocks local storage. Decisions will stay only until this page closes; export them to keep a copy.");
      text($("storage-status"), "Local storage unavailable.");
      return;
    }
    if (!raw) {
      text($("storage-status"), "No local decisions saved · 81 UNREVIEWED");
      return;
    }
    try {
      var saved = JSON.parse(raw);
      if (saved.reconciliation_version !== RECONCILIATION_VERSION || saved.harvest_version !== EXPECTED.harvestVersion || saved.harvest_snapshot !== EXPECTED.snapshot || !saved.records || typeof saved.records !== "object") throw new Error("Saved review belongs to a different version or Harvest snapshot.");
      Object.keys(saved.records).forEach(function (id) {
        var item = saved.records[id];
        if (!byId.has(id) || !validOverlayRecord(item)) throw new Error("Saved review contains an unknown ID or invalid decision: " + id);
        overlay[id] = item;
      });
      text($("storage-status"), "Restored from this browser · Harvest remains read-only");
    } catch (error) {
      $("persistence-warning").hidden = false;
      text($("persistence-warning"), "Saved local review could not be loaded: " + error.message + " Export or clear the old local review after checking it.");
      storageAvailable = false;
      text($("storage-status"), "Saved local data needs attention.");
    }
  }
  function validOverlayRecord(item) {
    return !!item && DECISIONS.indexOf(item.primary_decision) !== -1 &&
      Array.isArray(item.reason_tags) && item.reason_tags.every(function (tag) { return TAGS.indexOf(tag) !== -1; }) &&
      typeof item.human_notes === "string";
  }
  function populateFilters() {
    var selectValues = [
      ["filter-pass", ordered.map(function (item) { return item.pass.label; })],
      ["filter-source", records.map(function (x) { return x.source_family; })],
      ["filter-decision", DECISIONS],
      ["filter-lifecycle", records.map(function (x) { return x.lifecycle; })],
      ["filter-mode", records.map(function (x) { return x.communication_mode; })],
      ["filter-surface", records.map(function (x) { return x.communication_surface; })],
      ["filter-preservation", records.reduce(function (all, x) { return all.concat(x.preservation || []); }, [])],
      ["filter-compatibility", records.map(function (x) { return (x.compatibility || {}).message_validity || "UNKNOWN"; })],
      ["filter-tag", TAGS]
    ];
    selectValues.forEach(function (pair) {
      Array.from(new Set(pair[1].filter(Boolean))).sort().forEach(function (value) { addOption($(pair[0]), value, value); });
    });
  }
  function matchesFilters(item) {
    var c = item.candidate;
    var currentDecision = decision(c.composition_id);
    var selectedTag = $("filter-tag").value;
    if ($("filter-pass").value && $("filter-pass").value !== item.pass.label) return false;
    if ($("filter-source").value && $("filter-source").value !== c.source_family) return false;
    if ($("filter-decision").value && $("filter-decision").value !== currentDecision) return false;
    if ($("filter-lifecycle").value && $("filter-lifecycle").value !== c.lifecycle) return false;
    if ($("filter-mode").value && $("filter-mode").value !== c.communication_mode) return false;
    if ($("filter-surface").value && $("filter-surface").value !== c.communication_surface) return false;
    if ($("filter-preservation").value && (c.preservation || []).indexOf($("filter-preservation").value) === -1) return false;
    if ($("filter-compatibility").value && $("filter-compatibility").value !== ((c.compatibility || {}).message_validity || "UNKNOWN")) return false;
    if (selectedTag && tagsFor(c.composition_id).indexOf(selectedTag) === -1) return false;
    if ($("filter-tests").checked && !(c.tests || []).length) return false;
    if ($("filter-failures").checked && !item.failureEvidence) return false;
    if (quickFilter === "unreviewed" && currentDecision !== "UNREVIEWED") return false;
    if (quickFilter === "accepted" && currentDecision !== "ACCEPT" && currentDecision !== "ACCEPT_CONTEXTUAL") return false;
    if (quickFilter === "attention" && ["EDIT", "REJECT", "EVIDENCE_ONLY"].indexOf(currentDecision) === -1 && !tagsFor(c.composition_id).length) return false;
    var query = $("filter-search").value.trim().toLowerCase();
    if (query && JSON.stringify(c).toLowerCase().indexOf(query) === -1 && item.pass.label.toLowerCase().indexOf(query) === -1) return false;
    return true;
  }
  function visibleItems() { return ordered.filter(matchesFilters); }
  function renderQueue() {
    var visible = visibleItems();
    if (currentId && !visible.some(function (item) { return item.candidate.composition_id === currentId; })) currentId = visible.length ? visible[0].candidate.composition_id : null;
    if (!currentId && visible.length) currentId = visible[0].candidate.composition_id;
    var list = $("queue-list");
    list.replaceChildren();
    visible.forEach(function (item) {
      var c = item.candidate;
      var li = make("li", "queue-item");
      var pick = document.createElement("input");
      pick.type = "checkbox";
      pick.className = "compare-pick";
      pick.checked = compareIds.indexOf(c.composition_id) !== -1;
      pick.setAttribute("aria-label", "Select " + c.composition_id + " for comparison");
      pick.addEventListener("change", function () {
        if (pick.checked) {
          if (compareIds.length >= 4) { pick.checked = false; setStatus("Comparison is limited to four records.", true); return; }
          if (compareIds.indexOf(c.composition_id) === -1) compareIds.push(c.composition_id);
        } else compareIds = compareIds.filter(function (id) { return id !== c.composition_id; });
        renderComparison();
      });
      li.appendChild(pick);
      var button = make("button");
      button.type = "button";
      button.setAttribute("aria-current", c.composition_id === currentId ? "true" : "false");
      button.addEventListener("click", function () { selectRecord(c.composition_id); });
      button.appendChild(make("span", "queue-id", c.composition_id + " · " + decision(c.composition_id)));
      button.appendChild(make("span", "queue-intent", c.canonical_intent));
      button.appendChild(make("span", "queue-meta", item.pass.label + " · " + c.source_family));
      li.appendChild(button);
      list.appendChild(li);
    });
    text($("queue-count"), visible.length + " / " + records.length + " records");
    updatePosition();
    renderRecord();
    renderComparison();
    var has = visible.length > 0 && !locked;
    ["previous-button", "next-button", "next-unreviewed-button"].forEach(function (id) { $(id).disabled = !has; });
    $("jump-select").disabled = locked || records.length === 0;
  }
  function updatePosition() {
    var index = ordered.findIndex(function (item) { return item.candidate.composition_id === currentId; });
    if (index < 0) text($("position"), "No current record · " + (visibleItems().length) + " match filters");
    else {
      var item = ordered[index];
      text($("position"), "Record " + (index + 1) + " of " + records.length + " · " + item.pass.label + " · " + (visibleItems().length) + " shown by filters");
    }
  }
  function renderProgress() {
    var counts = {};
    DECISIONS.forEach(function (state) { counts[state] = 0; });
    records.forEach(function (candidate) { counts[decision(candidate.composition_id)] += 1; });
    var reviewed = records.length - counts.UNREVIEWED;
    text($("reviewed-count"), "Reviewed: " + reviewed + " / " + records.length);
    $("progress-fill").style.width = (records.length ? (reviewed / records.length * 100) : 0) + "%";
    var countList = $("decision-counts");
    countList.replaceChildren();
    DECISIONS.forEach(function (state) {
      var item = make("span", "count-item", state + ": " + counts[state]);
      countList.appendChild(item);
    });
    if (counts.UNREVIEWED) text($("completion-status"), "PARTIAL RECONCILIATION — " + counts.UNREVIEWED + " RECORDS UNREVIEWED. Export remains available.");
    else text($("completion-status"), "HUMAN RECONCILIATION INPUT COMPLETE — all 81 records have a creator disposition. This does not create an accepted baseline.");
    document.querySelectorAll("[data-quick]").forEach(function (button) { button.setAttribute("aria-pressed", button.getAttribute("data-quick") === quickFilter ? "true" : "false"); });
  }
  function selectRecord(id) {
    if (!byId.has(id)) return;
    currentId = id;
    renderQueue();
  }
  function moveRecord(delta) {
    var visible = visibleItems();
    if (!visible.length) return;
    var index = visible.findIndex(function (item) { return item.candidate.composition_id === currentId; });
    if (index < 0) index = 0;
    var next = Math.max(0, Math.min(visible.length - 1, index + delta));
    selectRecord(visible[next].candidate.composition_id);
  }
  function nextUnreviewed() {
    var visible = visibleItems();
    if (!visible.length) return;
    var start = visible.findIndex(function (item) { return item.candidate.composition_id === currentId; });
    for (var step = 1; step <= visible.length; step += 1) {
      var item = visible[(Math.max(start, -1) + step) % visible.length];
      if (decision(item.candidate.composition_id) === "UNREVIEWED") {
        selectRecord(item.candidate.composition_id);
        return;
      }
    }
    setStatus("No unreviewed records match the current filters.", false);
  }
  function renderComparison() {
    var panel = $("comparison-panel");
    panel.replaceChildren();
    if (compareIds.length < 2) { panel.hidden = true; return; }
    panel.hidden = false;
    var top = make("div", "filter-heading");
    top.appendChild(make("h2", "", "Side-by-side record comparison · " + compareIds.length + " selected"));
    var clear = make("button", "secondary", "Clear comparison");
    clear.type = "button";
    clear.addEventListener("click", function () { compareIds = []; renderQueue(); });
    top.appendChild(clear);
    panel.appendChild(top);
    var grid = make("div", "comparison-grid");
    compareIds.forEach(function (id) {
      var item = byId.get(id);
      if (!item) return;
      var c = item.candidate;
      var card = make("article", "comparison-card");
      card.appendChild(make("h3", "", c.composition_id + " · " + c.canonical_intent));
      var image = document.createElement("img");
      image.src = "../" + c.visual_render;
      image.alt = "Renderer preview " + c.composition_id;
      card.appendChild(image);
      card.appendChild(make("p", "", (c.pictiq_sequence_human_readable || []).join(" | ")));
      card.appendChild(make("p", "", c.communication_mode + " · " + c.communication_surface + " · " + item.pass.label));
      card.appendChild(make("p", "", "Context: " + (c.context_summary || "Not recorded")));
      card.appendChild(make("p", "", "Compatibility: " + ((c.compatibility || {}).message_validity || "UNKNOWN") + " · Failures: " + (item.failureEvidence ? "yes" : "no")));
      grid.appendChild(card);
    });
    panel.appendChild(grid);
  }
  function makeExport() {
    var counts = {};
    DECISIONS.forEach(function (state) { counts[state] = 0; });
    var exportRecords = ordered.map(function (item) {
      var c = item.candidate;
      var ref = {
        source_family: c.source_family || "unknown",
        origin_reference: c.origin && c.origin.reference || "",
        source_references: recordRefs(c)
      };
      var state = decision(c.composition_id);
      counts[state] += 1;
      return {
        composition_id: c.composition_id,
        review_id: c.review_id,
        original_harvest_identity: ref,
        primary_decision: state,
        reason_tags: tagsFor(c.composition_id).slice(),
        human_notes: notesFor(c.composition_id)
      };
    });
    var reviewed = records.length - counts.UNREVIEWED;
    return {
      reconciliation_version: RECONCILIATION_VERSION,
      harvest_version: EXPECTED.harvestVersion,
      harvest_snapshot: EXPECTED.snapshot,
      exported_at: new Date().toISOString(),
      reviewed_count: reviewed,
      unreviewed_count: counts.UNREVIEWED,
      decision_counts: counts,
      records: exportRecords
    };
  }
  function exportReview() {
    if (locked) return;
    var data = makeExport();
    var blob = new Blob([JSON.stringify(data, null, 2) + "\n"], {type: "application/json"});
    var url = URL.createObjectURL(blob);
    var link = document.createElement("a");
    link.href = url;
    link.download = "pictiq-human-reconciliation-v0.1-8fae507.json";
    document.body.appendChild(link);
    link.click();
    link.remove();
    setTimeout(function () { URL.revokeObjectURL(url); }, 1000);
    if (data.unreviewed_count) setStatus("PARTIAL RECONCILIATION — " + data.unreviewed_count + " RECORDS UNREVIEWED. Exported all 81 overlay rows.", false);
    else setStatus("HUMAN RECONCILIATION INPUT COMPLETE. Exported dispositions; no baseline was created.", false);
  }
  function importFile(file) {
    if (!file || locked) return;
    file.text().then(function (raw) {
      var incoming = JSON.parse(raw);
      if (incoming.reconciliation_version !== RECONCILIATION_VERSION) throw new Error("Reconciliation version mismatch.");
      if (incoming.harvest_version !== EXPECTED.harvestVersion) throw new Error("Harvest version mismatch.");
      if (incoming.harvest_snapshot !== EXPECTED.snapshot) throw new Error("Harvest snapshot mismatch.");
      if (!Array.isArray(incoming.records)) throw new Error("The file has no reconciliation records array.");
      var next = {};
      var seen = {};
      incoming.records.forEach(function (entry) {
        if (!entry || typeof entry.composition_id !== "string") throw new Error("A record is missing its composition_id.");
        if (!byId.has(entry.composition_id)) throw new Error("Unknown composition ID: " + entry.composition_id + ". No decisions were imported.");
        if (seen[entry.composition_id]) throw new Error("Duplicate composition ID: " + entry.composition_id + ". No decisions were imported.");
        seen[entry.composition_id] = true;
        if (DECISIONS.indexOf(entry.primary_decision) === -1) throw new Error("Invalid primary decision for " + entry.composition_id + ".");
        if (!Array.isArray(entry.reason_tags) || !entry.reason_tags.every(function (tag) { return TAGS.indexOf(tag) !== -1; })) throw new Error("Invalid reason tags for " + entry.composition_id + ".");
        if (typeof entry.human_notes !== "string") throw new Error("Invalid notes value for " + entry.composition_id + ".");
        if (entry.primary_decision !== "UNREVIEWED" || entry.reason_tags.length || entry.human_notes) {
          next[entry.composition_id] = {primary_decision: entry.primary_decision, reason_tags: entry.reason_tags.slice(), human_notes: entry.human_notes, updated_at: new Date().toISOString()};
        }
      });
      var old = overlay;
      overlay = next;
      saveOverlay();
      if (!storageAvailable) {
        overlay = old;
        throw new Error("Local storage is unavailable, so import was not applied. Export a copy or enable local storage.");
      }
      renderProgress();
      renderQueue();
      var omitted = records.length - Object.keys(seen).length;
      if (omitted) setStatus("Imported " + Object.keys(seen).length + " known records. " + omitted + " absent IDs are now UNREVIEWED in the imported overlay.", false);
      else setStatus("Imported " + Object.keys(seen).length + " records. Harvest data remains unchanged.", false);
    }).catch(function (error) {
      setStatus("Import rejected: " + error.message, true);
    }).finally(function () { $("import-file").value = ""; });
  }
  function clearLocal() {
    if (!window.confirm("Clear local reconciliation decisions, reason tags, and notes for this Harvest in this browser? This does not change the Harvest files.")) return;
    try {
      localStorage.removeItem(STORAGE_KEY);
      overlay = {};
      storageAvailable = true;
      $("persistence-warning").hidden = true;
      text($("storage-status"), "Cleared · 81 UNREVIEWED · Harvest files unchanged");
      renderProgress();
      renderQueue();
      setStatus("Local reconciliation cleared.", false);
    } catch (error) { setStatus("Could not clear local data: " + error.message, true); }
  }
  function setupEvents() {
    ["filter-pass", "filter-source", "filter-decision", "filter-lifecycle", "filter-mode", "filter-surface", "filter-preservation", "filter-compatibility", "filter-tag", "filter-tests", "filter-failures", "filter-search"].forEach(function (id) {
      $(id).addEventListener("input", renderQueue);
      $(id).addEventListener("change", renderQueue);
    });
    $("clear-filters").addEventListener("click", function () {
      ["filter-pass", "filter-source", "filter-decision", "filter-lifecycle", "filter-mode", "filter-surface", "filter-preservation", "filter-compatibility", "filter-tag", "filter-search"].forEach(function (id) { $(id).value = ""; });
      $("filter-tests").checked = false;
      $("filter-failures").checked = false;
      quickFilter = "";
      renderProgress();
      renderQueue();
    });
    document.querySelectorAll("[data-quick]").forEach(function (button) {
      button.addEventListener("click", function () {
        var selected = button.getAttribute("data-quick");
        quickFilter = quickFilter === selected ? "" : selected;
        renderProgress();
        renderQueue();
      });
    });
    $("previous-button").addEventListener("click", function () { moveRecord(-1); });
    $("next-button").addEventListener("click", function () { moveRecord(1); });
    $("next-unreviewed-button").addEventListener("click", nextUnreviewed);
    $("jump-select").addEventListener("change", function () { selectRecord($("jump-select").value); });
    $("export-button").addEventListener("click", exportReview);
    $("clear-button").addEventListener("click", clearLocal);
    $("import-file").addEventListener("change", function (event) { importFile(event.target.files && event.target.files[0]); });
    document.addEventListener("keydown", function (event) {
      if (event.metaKey || event.ctrlKey || event.altKey) return;
      var tag = event.target && event.target.tagName;
      if (["INPUT", "TEXTAREA", "SELECT", "BUTTON"].indexOf(tag) !== -1 || (event.target && event.target.isContentEditable)) return;
      if (event.key === "ArrowLeft") { event.preventDefault(); moveRecord(-1); }
      else if (event.key === "ArrowRight") { event.preventDefault(); moveRecord(1); }
      else if (event.key.toLowerCase() === "j") { event.preventDefault(); nextUnreviewed(); }
      else if (event.key.toLowerCase() === "d") { event.preventDefault(); var select = $("primary-decision"); if (select) select.focus(); }
    });
  }
  function initialize(manifest, counts, dataset) {
    if (manifest.harvest_id !== EXPECTED.harvestId || manifest.snapshot_commit !== EXPECTED.snapshot ||
        manifest.records.length !== EXPECTED.count || counts.unique_exact_records !== EXPECTED.count ||
        counts.evidence_only !== EXPECTED.evidenceOnly || counts.unsafe_to_harvest !== EXPECTED.unsafe ||
        dataset.length !== EXPECTED.count) {
      setLocked("HARVEST SNAPSHOT MISMATCH — expected Historical Composition Harvest v0.1 / 8fae507 / 81 records / 86 evidence-only / 7 unsafe. No decisions will be loaded or accepted against changed data.");
      return;
    }
    var manifestIds = manifest.records.map(function (record) { return record.composition_id; });
    var datasetIds = dataset.map(function (record) { return record.composition_id; });
    if (new Set(manifestIds).size !== EXPECTED.count || new Set(datasetIds).size !== EXPECTED.count ||
        manifestIds.some(function (id) { return datasetIds.indexOf(id) === -1; })) {
      setLocked("HARVEST SNAPSHOT MISMATCH — candidate IDs are duplicated or do not match the locked manifest. Review is disabled.");
      return;
    }
    records = dataset.slice();
    records.forEach(function (candidate) { byId.set(candidate.composition_id, wrapper(candidate)); });
    ordered = records.map(wrapper).sort(function (a, b) {
      if (a.pass.rank !== b.pass.rank) return a.pass.rank - b.pass.rank;
      var aa = parseInt(a.candidate.composition_id.slice(-4), 10);
      var bb = parseInt(b.candidate.composition_id.slice(-4), 10);
      return aa - bb;
    });
    locked = false;
    loadOverlay();
    populateFilters();
    var jump = $("jump-select");
    addOption(jump, "", "Select a record…");
    ordered.forEach(function (item) { addOption(jump, item.candidate.composition_id, item.candidate.composition_id + " · " + item.candidate.canonical_intent); });
    jump.disabled = false;
    currentId = ordered.length ? ordered[0].candidate.composition_id : null;
    $("export-button").disabled = false;
    $("clear-button").disabled = false;
    setupEvents();
    renderProgress();
    renderQueue();
  }
  function boot() {
    var base = "../";
    Promise.all([
      fetch(base + "manifest.json").then(function (response) { if (!response.ok) throw new Error("manifest.json could not be loaded"); return response.arrayBuffer(); }),
      fetch(base + "harvest-counts.json").then(function (response) { if (!response.ok) throw new Error("harvest-counts.json could not be loaded"); return response.json(); }),
      fetch(base + "review-dataset.json").then(function (response) { if (!response.ok) throw new Error("review-dataset.json could not be loaded"); return response.arrayBuffer(); })
    ]).then(function (loaded) {
      return Promise.all([sha256(loaded[0]), sha256(loaded[2])]).then(function (hashes) {
        if (hashes[0] !== EXPECTED.manifestSha256 || hashes[1] !== EXPECTED.reviewSha256) {
          setLocked("HARVEST CONTENT HASH MISMATCH — the manifest or review dataset differs from the frozen v0.1 files. No decisions can be made in this viewer.");
          return;
        }
        initialize(JSON.parse(new TextDecoder().decode(loaded[0])), loaded[1], JSON.parse(new TextDecoder().decode(loaded[2])));
      });
    }).catch(function (error) {
      setLocked("HARVEST LOAD ERROR — " + error.message + ". Open the viewer through the local HTTP server and keep the Harvest package beside this reconciliation folder.");
    });
  }
  boot();
}());
