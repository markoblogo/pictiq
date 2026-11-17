// K01a: exactly one known technical snapshot transition; no general hash rewriting.
const MIGRATION = __MIGRATION_CONTRACT__;
const OLD_KEY = 'pictiq.final-creator-qa.v0.2:' + MIGRATION.dataset.qa_dataset_sha256;
const clone = x => JSON.parse(JSON.stringify(x));
const stable = x => JSON.stringify(x, (_, v) => v && typeof v === 'object' && !Array.isArray(v)
  ? Object.fromEntries(Object.keys(v).sort().map(k => [k, v[k]])) : v);
function assertKnownPair(oldData = MIGRATION.dataset, newData = DATA) {
  if (oldData.qa_dataset_sha256 !== MIGRATION.old_dataset_sha256 ||
      newData.qa_dataset_sha256 !== MIGRATION.new_dataset_sha256 ||
      oldData.pending_addendum.sha256 !== MIGRATION.old_addendum_sha256 ||
      newData.pending_addendum.sha256 !== MIGRATION.new_addendum_sha256)
    throw Error('Unknown snapshot pair; no decisions transferred.');
  const comparable = d => { const x = clone(d); delete x.qa_dataset_sha256;
    delete x.pending_addendum.sha256; return x; };
  if (stable(comparable(oldData)) !== stable(comparable(newData)))
    throw Error('Card content, previews, locked decisions or baseline bindings changed; transfer stopped.');
}
function validateSnapshotExport(x, snapshot) {
  if (!x || typeof x !== 'object' || x.qa_type !== snapshot.qa_type || x.version !== snapshot.version)
    throw Error('QA type/version mismatch');
  if (stable(x.source_baseline) !== stable(snapshot.source_baseline)) throw Error('baseline snapshot mismatch');
  if (x.qa_dataset_sha256 !== snapshot.qa_dataset_sha256 ||
      stable(x.pending_addendum) !== stable(snapshot.pending_addendum)) throw Error('QA dataset/addendum snapshot mismatch');
  if (x.technical_migration) {
    const m = x.technical_migration;
    if (snapshot.qa_dataset_sha256 !== MIGRATION.new_dataset_sha256 ||
        m.kind !== 'K01a_TECHNICAL_SNAPSHOT_MIGRATION' ||
        m.from_dataset_sha256 !== MIGRATION.old_dataset_sha256 || m.to_dataset_sha256 !== MIGRATION.new_dataset_sha256 ||
        m.from_addendum_sha256 !== MIGRATION.old_addendum_sha256 || m.to_addendum_sha256 !== MIGRATION.new_addendum_sha256 ||
        !/^[0-9a-f]{64}$/.test(m.source_export_sha256) || typeof m.migrated_at !== 'string' || !m.migrated_at)
      throw Error('invalid technical migration lineage');
  }
  const expected = new Map(snapshot.entries.map(r => [r.dictionary_entry_id, r]));
  if (x.unique_primary_entry_count !== expected.size) throw Error('unique entry count mismatch');
  if (!Array.isArray(x.entry_ids) || x.entry_ids.length !== expected.size ||
      new Set(x.entry_ids).size !== expected.size || x.entry_ids.some(id => !expected.has(id)))
    throw Error('entry ID list mismatch');
  if (!Array.isArray(x.records) || x.records.length !== expected.size) throw Error('missing expected unique review records');
  const seen = new Set(); let reviewedCount = 0, unresolvedCount = 0;
  for (const r of x.records) {
    if (!r || !expected.has(r.dictionary_entry_id) || seen.has(r.dictionary_entry_id))
      throw Error('unknown or duplicate Dictionary entry ID');
    seen.add(r.dictionary_entry_id); const row = expected.get(r.dictionary_entry_id);
    if (r.corpus_record_id !== row.corpus_record_id) throw Error('corpus record ID mismatch');
    if (r.decision !== null && !DECISIONS.includes(r.decision)) throw Error('invalid decision');
    if (typeof r.creator_note !== 'string') throw Error('creator note must be text');
    if (r.decision === 'NEEDS_CORRECTION' && !r.creator_note.trim()) throw Error('NEEDS_CORRECTION requires a note');
    if (row.recorded_decision && r.decision !== row.recorded_decision) throw Error('recorded addendum decision mismatch');
    if (r.decision_source !== (row.recorded_decision ? 'PENDING_ADDENDUM' : 'LOCAL_QA_OVERLAY'))
      throw Error('decision source mismatch');
    if (r.decision) reviewedCount++;
    if (r.decision === 'UNRESOLVED') unresolvedCount++;
  }
  if (x.reviewed_count !== reviewedCount || x.unresolved_decision_count !== unresolvedCount ||
      x.unresolved_follow_up_count !== snapshot.remaining_unresolved_follow_up_count)
    throw Error('review counters mismatch');
  return true;
}
function snapshotExport(records, snapshot = DATA) {
  return {qa_type: snapshot.qa_type, version: snapshot.version, source_baseline: clone(snapshot.source_baseline),
    qa_dataset_sha256: snapshot.qa_dataset_sha256, pending_addendum: clone(snapshot.pending_addendum),
    unique_primary_entry_count: snapshot.unique_primary_entry_count,
    reviewed_count: records.filter(r => r.decision).length,
    unresolved_follow_up_count: snapshot.remaining_unresolved_follow_up_count,
    unresolved_decision_count: records.filter(r => r.decision === 'UNRESOLVED').length,
    entry_ids: snapshot.entries.map(r => r.dictionary_entry_id), records: clone(records)};
}
function oldOverlayExport(raw) {
  const overlay = JSON.parse(raw);
  if (!overlay || typeof overlay !== 'object' || Array.isArray(overlay)) throw Error('invalid old overlay');
  const rows = new Map(MIGRATION.dataset.entries.map(r => [r.dictionary_entry_id, r]));
  for (const [id, value] of Object.entries(overlay)) {
    if (!rows.has(id)) throw Error('unknown old overlay ID');
    if (!value || typeof value !== 'object' || Array.isArray(value)) throw Error('invalid old overlay record');
    if (value.decision !== undefined && !DECISIONS.includes(value.decision)) throw Error('invalid old overlay decision');
    if (value.dictionary_entry_id !== undefined && value.dictionary_entry_id !== id) throw Error('old overlay record ID mismatch');
    if (value.note !== undefined && typeof value.note !== 'string') throw Error('invalid old overlay note');
    if (rows.get(id).recorded_decision && value.decision && value.decision !== rows.get(id).recorded_decision)
      throw Error('recorded addendum decision mismatch');
  }
  const records = MIGRATION.dataset.entries.map(row => {
    const v = overlay[row.dictionary_entry_id] || {};
    return {...clone(v), dictionary_entry_id: row.dictionary_entry_id, corpus_record_id: row.corpus_record_id,
      decision: row.recorded_decision || v.decision || null, creator_note: v.note || '',
      decision_source: row.recorded_decision ? 'PENDING_ADDENDUM' : 'LOCAL_QA_OVERLAY'};
  });
  const out = snapshotExport(records, MIGRATION.dataset); validateSnapshotExport(out, MIGRATION.dataset); return out;
}
function migrateKnownExport(oldExport, sourceHash, at) {
  assertKnownPair(); validateSnapshotExport(oldExport, MIGRATION.dataset);
  // Records (including timestamps and unread notes) are copied without reinterpretation.
  const out = snapshotExport(oldExport.records);
  out.technical_migration = {kind: 'K01a_TECHNICAL_SNAPSHOT_MIGRATION',
    from_dataset_sha256: MIGRATION.old_dataset_sha256, from_addendum_sha256: MIGRATION.old_addendum_sha256,
    to_dataset_sha256: MIGRATION.new_dataset_sha256, to_addendum_sha256: MIGRATION.new_addendum_sha256,
    source_export_sha256: sourceHash, migrated_at: at};
  validateSnapshotExport(out, DATA); return out;
}
function overlayFromExport(x) {
  return Object.fromEntries(x.records.filter(r => !DATA.entries.find(e => e.dictionary_entry_id === r.dictionary_entry_id).recorded_decision)
    .map(r => [r.dictionary_entry_id, {...clone(r), decision: r.decision || undefined, note: r.creator_note}]));
}
function installMigration(storage, oldExport, sourceHash, at, original) {
  const output = migrateKnownExport(oldExport, sourceHash, at);
  const existing = storage.getItem(KEY);
  if (existing !== null && existing !== '{}') {
    let prior; try { prior = JSON.parse(existing); } catch { /* preserve corrupt target too */ }
    if (prior?.migration_lineage?.source_export_sha256 === sourceHash && stable(prior.source_export) === stable(oldExport)) return {status: 'ALREADY_MIGRATED'};
    throw Error('CONFLICT: corrected snapshot already has saved work. Both sources preserved; download each separately. No merge or overwrite.');
  }
  const envelope = {qa_overlay: overlayFromExport(output), migration_lineage: output.technical_migration,
    source_export: clone(oldExport), original_source: original};
  const serialized = JSON.stringify(envelope);
  storage.setItem(KEY, serialized); // Single atomic storage write; never touches OLD_KEY.
  if (storage.getItem(KEY) !== serialized) throw Error('New state could not be verified; original source preserved.');
  return {status: 'MIGRATED', envelope, output};
}
async function textHash(text) {
  return Array.from(new Uint8Array(await crypto.subtle.digest('SHA-256', new TextEncoder().encode(text))))
    .map(b => b.toString(16).padStart(2, '0')).join('');
}
async function verifyMigrationAssets() {
  for (const [path, expected] of Object.entries(MIGRATION.asset_sha256)) {
    const response = await fetch(path, {cache: 'no-store'});
    if (!response.ok) throw Error('Preview unavailable: ' + path);
    const bytes = await response.arrayBuffer();
    const hash = Array.from(new Uint8Array(await crypto.subtle.digest('SHA-256', bytes)))
      .map(b => b.toString(16).padStart(2, '0')).join('');
    if (hash !== expected) throw Error('Preview changed: ' + path + '; transfer stopped.');
  }
}
function migrationMessage(message) { $('migration-status').textContent = message; }
function refreshMigrationNotice() {
  try {
    const raw = localStorage.getItem(OLD_KEY);
    if (raw !== null && raw !== '{}') {
      $('migrate-local').hidden = false; $('backup-old').hidden = false;
      const x = oldOverlayExport(raw);
      migrationMessage('Saved work found in the previous snapshot: ' + x.reviewed_count + ' / ' + x.unique_primary_entry_count +
        ' reviewed (including locked decisions). Original data will be kept. Use the explicit transfer action.');
    } else migrationMessage('No saved work found under the known previous key in this browser. You can explicitly migrate an old JSON export.');
    if (migrationLineage) migrationMessage('Technical migration complete. New export is available; old key and source export are preserved.');
    if (storageLoadError) migrationMessage(storageLoadError + ' Saved data was preserved.');
  } catch (e) { migrationMessage('Previous work found but validation failed: ' + e.message + '. Source preserved.'); }
}
async function performMigration(oldExport, original) {
  // Save the original export BEFORE attempting any target write.
  download(oldExport, 'pictiq-final-qa-before-K01a.json');
  await verifyMigrationAssets();
  const sourceHash = await textHash(stable(oldExport));
  const result = installMigration(localStorage, oldExport, sourceHash, new Date().toISOString(), original);
  if (result.envelope) {
    state = result.envelope.qa_overlay; migrationLineage = result.envelope.migration_lineage;
    preservedExport = result.envelope.source_export; preservedOriginal = result.envelope.original_source;
    storageLoadError = null; draw();
  }
  migrationMessage(result.status + ': original source preserved; use EXPORT FINAL QA JSON to download corrected snapshot.');
}
function initMigration() {
  $('migrate-local').onclick = async () => { try {
    const raw = localStorage.getItem(OLD_KEY);
    if (raw === null) throw Error('Old source key no longer present');
    await performMigration(oldOverlayExport(raw), {kind: 'OLD_LOCAL_STORAGE', key: OLD_KEY, raw});
  } catch (e) { migrationMessage(e.message); } };
  $('migrate-file').onchange = async e => { try {
    const raw = await e.target.files[0].text(); const x = JSON.parse(raw);
    validateSnapshotExport(x, MIGRATION.dataset);
    await performMigration(x, {kind: 'OLD_EXPORT', raw});
  } catch (err) { migrationMessage('Transfer rejected: ' + err.message); } e.target.value = ''; };
  $('backup-old').onclick = () => { const raw = localStorage.getItem(OLD_KEY);
    if (raw !== null) download({key: OLD_KEY, raw}, 'pictiq-old-QA-storage-backup.json'); };
  $('backup-new').onclick = () => { const raw = localStorage.getItem(KEY);
    if (raw !== null) download({key: KEY, raw}, 'pictiq-new-QA-storage-backup.json'); };
  refreshMigrationNotice();
}
