// Extracts the <script type="module"> from index.html and runs `node --check` on it.
// The game is one self-contained HTML file, so this is our "lint": it catches syntax
// errors without a browser. Used by the SessionStart hook and runnable directly:
//   node scripts/syntax-check.mjs
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { execFileSync } from 'node:child_process';

const root = new URL('..', import.meta.url);
const src = fs.readFileSync(new URL('index.html', root), 'utf8');
const m = src.match(/<script type="module">([\s\S]*?)<\/script>/);
if (!m) { console.error('syntax-check: no <script type="module"> found in index.html'); process.exit(1); }

const tmp = path.join(os.tmpdir(), `bk-syntax-${process.pid}.mjs`);
fs.writeFileSync(tmp, m[1]);
try {
  execFileSync('node', ['--check', tmp], { stdio: 'pipe' });
  console.log('syntax-check: OK (index.html module script parses)');
} catch (e) {
  console.error('syntax-check: SYNTAX ERROR\n' + (e.stderr?.toString() || e.message));
  process.exit(1);
} finally {
  try { fs.unlinkSync(tmp); } catch {}
}
