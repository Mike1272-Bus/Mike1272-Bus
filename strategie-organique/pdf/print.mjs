import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
import path from 'path';
const dir = path.dirname(new URL(import.meta.url).pathname);
const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' });
const p = await b.newPage();
await p.goto('file://' + path.join(dir, 'plan_30_jours.html'));
await p.evaluate(() => document.fonts.ready);
await p.pdf({
  path: path.join(dir, '..', 'plan_30_jours.pdf'), format: 'A4', printBackground: true, preferCSSPageSize: true,
  displayHeaderFooter: true, headerTemplate: '<span></span>',
  footerTemplate: '<div style="width:100%;font-size:8px;color:#8a89a8;padding:0 16mm;display:flex;justify-content:space-between;font-family:sans-serif"><span>DigitalMikaelson · Stratégie organique 30 jours</span><span class="pageNumber"></span></div>',
});
await b.close();
