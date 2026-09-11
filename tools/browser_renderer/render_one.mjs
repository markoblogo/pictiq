#!/usr/bin/env node
import fs from 'node:fs';
import { performance } from 'node:perf_hooks';
import { renderPictiqMessage } from '../../docs/renderer/browser-renderer.mjs';

const input = process.argv[2];
if (!input) {
  console.error('usage: node tools/browser_renderer/render_one.mjs <message.json>');
  process.exit(2);
}
try {
  const message = JSON.parse(fs.readFileSync(input, 'utf8'));
  const start = performance.now();
  const render = renderPictiqMessage(message);
  const elapsedMs = performance.now() - start;
  process.stdout.write(JSON.stringify({ ok: true, elapsedMs, render }));
} catch (error) {
  process.stdout.write(JSON.stringify({ ok: false, error: String(error?.message || error) }));
  process.exit(1);
}
