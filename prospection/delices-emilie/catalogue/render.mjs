import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
import path from 'path';
const dir = path.dirname(new URL(import.meta.url).pathname);
const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' });
const m = await b.newPage({ viewport: { width: 430, height: 932 }, deviceScaleFactor: 2.5 });
await m.goto('file://' + path.join(dir, 'index.html'));
await m.evaluate(() => document.fonts.ready); await m.waitForTimeout(400);
await m.screenshot({ path: path.join(dir, 'apercu_catalogue_complet.png'), fullPage: true });
for (const [i, y] of [[1, 0], [2, 930], [3, 1860]]) {
  await m.evaluate((yy) => window.scrollTo(0, yy), y); await m.waitForTimeout(100);
  await m.screenshot({ path: path.join(dir, `apercu_ecran_${i}.png`) });
}
const c = await b.newPage({ viewport: { width: 1240, height: 1748 } });
await c.goto('file://' + path.join(dir, 'carte_qr.html'));
await c.evaluate(() => document.fonts.ready); await c.waitForTimeout(300);
await c.locator('#card').screenshot({ path: path.join(dir, 'carte_qr_a6.png') });
await c.pdf({ path: path.join(dir, 'carte_qr_a6.pdf'), width: '105mm', height: '148mm', printBackground: true, pageRanges: '1' });
await b.close();
