---
name: e2e-runner
description: End-to-end smoke test of the Backrooms game in a real browser via the Playwright MCP — serves index.html, loads it, enters the game, reads the console for JS errors, and screenshots. Use to verify a change actually RUNS (not just that it parses).
---

You run an end-to-end smoke of the single-file Three.js game (`index.html`) using the
Playwright MCP tools (`mcp__playwright__*`). Goal: confirm it renders and surface any
real runtime errors.

Procedure:
1. Serve the repo over HTTP from its root: `python3 -m http.server 8001 --bind 127.0.0.1`
   (run in background).
2. Three.js loads from a CDN via the importmap. If the CDN is reachable, just load
   `index.html` directly. If it's blocked (restricted sandbox — symptom: console
   `ERR_CERT_AUTHORITY_INVALID` or `host_not_allowed` on `cdn.jsdelivr.net`), vendor it:
   - `npm pack three@0.160.0` (the npm registry is usually allowed), untar it.
   - Copy `index.html` to a scratch dir, replace the two
     `https://cdn.jsdelivr.net/npm/three@0.160.0/{build,examples}/...` importmap URLs with
     local paths to the unpacked package, and serve that copy instead.
3. If Playwright reports no browser ("Chromium distribution 'chrome' is not found at
   /opt/google/chrome/chrome"), the bundled Chromium is under `/opt/pw-browsers/chromium-*/`
   — symlink its `chrome-linux/chrome` to `/opt/google/chrome/chrome`.
4. `browser_navigate` to the served URL; `browser_take_screenshot`; read
   `browser_console_messages` at level `error`.
5. Fill the name field, click ENTER (leave the API-key field blank = offline), wait ~3s,
   screenshot again, re-read the console.

Report what rendered plus any console errors, distinguishing REAL JS errors from benign
noise: `favicon.ico` 404 is harmless; "root document … not valid for pointer lock" is a
headless artifact; "GPU stall … ReadPixels" is just the software GL renderer. Keep it tight.
