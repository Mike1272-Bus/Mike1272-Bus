const { chromium } = require(require('child_process').execSync('npm root -g').toString().trim() + '/playwright');
const path = require('path');
const C = {
  resultats: ['#ff5c00', '<svg viewBox="0 0 100 100"><path d="M28 12 H72 V40 C72 54 62 62 50 62 C38 62 28 54 28 40 Z" fill="#ffd60a" stroke="#111" stroke-width="6" stroke-linejoin="round"/><path d="M28 20 H14 C14 34 20 42 30 44 M72 20 H86 C86 34 80 42 70 44" fill="none" stroke="#111" stroke-width="6" stroke-linecap="round"/><path d="M44 62 V76 H56 V62 M32 88 H68 V78 H32 Z" fill="#fff" stroke="#111" stroke-width="6" stroke-linejoin="round"/></svg>'],
  temoignages: ['#ffd60a', '<svg viewBox="0 0 100 100"><path d="M10 18 H90 V68 H44 L24 86 V68 H10 Z" fill="#fff" stroke="#111" stroke-width="6" stroke-linejoin="round"/><path d="M50 28 L55 38 L66 39 L58 46 L60 57 L50 51 L40 57 L42 46 L34 39 L45 38 Z" fill="#ff5c00" stroke="#111" stroke-width="4" stroke-linejoin="round"/></svg>'],
  offre: ['#1d7a46', '<svg viewBox="0 0 100 100"><rect x="14" y="40" width="72" height="48" fill="#ffd60a" stroke="#111" stroke-width="6"/><rect x="8" y="28" width="84" height="16" fill="#fff" stroke="#111" stroke-width="6"/><path d="M50 28 V88" stroke="#111" stroke-width="6"/><path d="M50 28 C40 10 22 14 30 26 C34 30 44 28 50 28 C56 28 66 30 70 26 C78 14 60 10 50 28 Z" fill="#ff5c00" stroke="#111" stroke-width="5" stroke-linejoin="round"/></svg>'],
  coulisses: ['#1c2f6b', '<svg viewBox="0 0 100 100"><rect x="8" y="30" width="62" height="46" rx="10" fill="#fff" stroke="#111" stroke-width="6"/><path d="M70 44 L92 32 V74 L70 62 Z" fill="#ffd60a" stroke="#111" stroke-width="6" stroke-linejoin="round"/><circle cx="39" cy="53" r="11" fill="#ff5c00" stroke="#111" stroke-width="5"/></svg>'],
};
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
  await p.goto('file://' + path.join(__dirname, 'covers.html'));
  await p.evaluate(() => document.fonts.ready);
  for (const [name, [bg, svg]] of Object.entries(C)) {
    await p.evaluate(([bg, svg]) => { const c = document.getElementById('c'); c.style.background = bg; c.innerHTML = svg; }, [bg, svg]);
    await p.screenshot({ path: path.join(__dirname, `alaune_${name}.png`) });
    console.log(name);
  }
  await b.close();
})();
