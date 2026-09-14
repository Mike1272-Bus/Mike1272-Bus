const { chromium } = require('/opt/node22/lib/node_modules/playwright');
const path = require('path');

async function shoot(file, width, height, out) {
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' });
  const page = await browser.newPage({ viewport: { width, height } });
  await page.goto('file://' + path.resolve(__dirname, file));
  await page.waitForTimeout(400);
  await page.screenshot({ path: out, type: 'jpeg', quality: 95 });
  await browser.close();
  console.log('wrote', out);
}

(async () => {
  await shoot('avatar-full.html', 1080, 1080, path.resolve(__dirname, 'michaelson-cube-avatar-full.jpg'));
})();
