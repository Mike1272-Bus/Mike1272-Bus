import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
import path from 'path';
const dir = path.dirname(new URL(import.meta.url).pathname);
const out = path.join(dir, '..');
const jobs = [['vignette.html', 1080, 1080, 'vignette_guide_gratuit.png'], ['banniere.html', 1920, 640, 'banniere_guide_gratuit.png']];
const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' });
for (const [f, w, h, o] of jobs) {
  const p = await b.newPage({ viewport: { width: w, height: h } });
  await p.goto('file://' + path.join(dir, f));
  await p.evaluate(() => document.fonts.ready);
  await p.waitForTimeout(300);
  await p.screenshot({ path: path.join(out, o) });
  await p.close();
}
await b.close();
