import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
import path from 'path';
const dir = path.dirname(new URL(import.meta.url).pathname);
const url = 'http://127.0.0.1:8765/index.html';
const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' });
const errs = [];
const m = await b.newPage({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, reducedMotion: 'reduce' });
m.on('console', (x) => x.type() === 'error' && errs.push(x.text())); m.on('requestfailed', (r) => errs.push('fail ' + r.url()));
await m.goto(url); await m.evaluate(() => document.fonts.ready); await m.waitForTimeout(400);
await m.screenshot({ path: path.join(dir, 'apercu/mobile_complet.png'), fullPage: true });
for (const [i, sel] of [[1, '.hero'], [2, '#miels'], [3, '#packs'], [4, '#contact']]) {
  await m.locator(sel).scrollIntoViewIfNeeded(); await m.evaluate((s) => document.querySelector(s).scrollIntoView(), sel); await m.waitForTimeout(150);
  await m.screenshot({ path: path.join(dir, `apercu/mobile_${i}.png`) });
}
const overflow = await m.evaluate(() => document.documentElement.scrollWidth - window.innerWidth);
const d = await b.newPage({ viewport: { width: 1440, height: 900 }, reducedMotion: 'reduce' });
await d.goto(url); await d.evaluate(() => document.fonts.ready); await d.waitForTimeout(400);
await d.screenshot({ path: path.join(dir, 'apercu/ordinateur_complet.png'), fullPage: true });
await d.screenshot({ path: path.join(dir, 'apercu/ordinateur_accueil.png') });
const og = await b.newPage({ viewport: { width: 1200, height: 630 }, reducedMotion: 'reduce' });
await og.goto(url); await og.evaluate(() => document.fonts.ready);
await og.addStyleTag({ content: '.top,.fab,.badges{display:none!important}.hero__in{padding-block:2.2rem!important;grid-template-columns:1.05fr 1fr!important}.hero h1{font-size:3.6rem!important}' });
await og.waitForTimeout(300);
await og.screenshot({ path: path.join(dir, 'og-image.jpg'), type: 'jpeg', quality: 88, clip: { x: 0, y: 0, width: 1200, height: 630 } });
await b.close();
console.log('overflow-x', overflow, 'errors', JSON.stringify(errs));
