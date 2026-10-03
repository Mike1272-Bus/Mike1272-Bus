import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
import path from 'path';
const dir = path.dirname(new URL(import.meta.url).pathname);
const out = path.join(dir, '..');
const jobs = [
  ['vignette.html', '', 1080, 1080, 'vignette_chariow_lancement.png'],
  ['vignette.html', '#noprice', 1080, 1080, 'vignette_chariow.png'],
  ['banniere.html', '', 1920, 640, 'banniere_chariow.png'],
];
const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' });
for (const [f, h, w, hh, o] of jobs) {
  const p = await b.newPage({ viewport: { width: w, height: hh } });
  await p.goto('file://' + path.join(dir, f) + h);
  await p.evaluate(() => document.fonts.ready);
  await p.waitForTimeout(300);
  await p.screenshot({ path: path.join(out, o) });
  await p.close();
}
await b.close();
