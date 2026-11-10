const fs = require('fs');
const path = require('path');
const { chromium } = require(require('child_process').execSync('npm root -g').toString().trim() + '/playwright');

const OUT = path.resolve(__dirname, '..');
const TPL = fs.readFileSync(path.join(__dirname, 'logo.html'), 'utf8');
const DEPTH = 12;

const PICTOS = {
  phone: `
    <path d="M88 8 H36 Q18 8 18 26 V144 Q18 162 36 162 H100 Q118 162 118 144 V64" fill="none" stroke-width="12" stroke-linecap="round" stroke-linejoin="round"/>
    <circle cx="50" cy="74" r="14" stroke="none"/>
    <path d="M28 146 C30 116 38 98 52 97 C64 96 70 106 73 118 L76 146 Z" stroke="none"/>
    <path d="M60 132 L82 110 L96 120 L134 70" fill="none" stroke-width="12" stroke-linecap="round" stroke-linejoin="round"/>
    <path d="M114 62 L144 52 L138 84 Z" stroke-width="6" stroke-linejoin="round"/>`,
  bag: `
    <path d="M18 56 H124 L116 162 H26 Z" fill="none" stroke-width="12" stroke-linejoin="round"/>
    <path d="M46 56 V42 Q46 12 71 12 Q96 12 96 42 V56" fill="none" stroke-width="12" stroke-linecap="round"/>
    <circle cx="52" cy="92" r="12" stroke="none"/>
    <path d="M40 146 L62 120 L76 130 L104 98" fill="none" stroke-width="11" stroke-linecap="round" stroke-linejoin="round"/>
    <path d="M90 94 L112 88 L108 112 Z" stroke-width="5" stroke-linejoin="round"/>`,
};

function lerp(a, b, t) {
  const pa = a.match(/\w\w/g).map((h) => parseInt(h, 16));
  const pb = b.match(/\w\w/g).map((h) => parseInt(h, 16));
  return '#' + pa.map((v, i) => Math.round(v + (pb[i] - v) * t).toString(16).padStart(2, '0')).join('');
}

function build({ picto, name, tag, flat }) {
  const face = flat ? '#2f66d8' : '#ffffff';
  const deep = flat ? '#0b1c45' : '#0c1d47';
  const near = flat ? '#1d3f8f' : '#8fa8dc';
  const layers = [];
  for (let i = DEPTH; i >= 1; i--) {
    const c = lerp(near, deep, (i - 1) / (DEPTH - 1));
    layers.push(`<g transform="translate(${i * 0.9} ${i * 0.9})" fill="${c}" stroke="${c}">${PICTOS[picto]}</g>`);
  }
  const svg = `<svg viewBox="0 0 150 170">
    <defs><filter id="sh" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="5"/></filter></defs>
    <g transform="translate(${DEPTH + 5} ${DEPTH + 7})" fill="rgba(0,0,0,0.45)" stroke="rgba(0,0,0,0.45)" filter="url(#sh)">${PICTOS[picto]}</g>
    ${layers.join('')}
    <g fill="${face}" stroke="${face}">${PICTOS[picto]}</g></svg>`;
  const shadow = [];
  for (let i = 1; i <= DEPTH; i++) shadow.push(`${i}px ${i}px 0 ${lerp(near, deep, (i - 1) / (DEPTH - 1))}`);
  shadow.push(`${DEPTH + 5}px ${DEPTH + 8}px 16px rgba(0,0,0,0.45)`);
  return TPL.replace('__PIC__', svg).replace('__NAME__', name).replace('__TAG__', tag)
    .replace('__SHADOW__', shadow.join(', ')).replace('__MODE__', flat ? 'flat' : '')
    .replace('.name {', flat ? '.name { color: ' + face + ' !important;' : '.name {');
}

const BRANDS = [
  { id: 'digitalmikaelson', picto: 'phone', name: 'DIGITALMIKAELSON', tag: 'TA COMPÉTENCE, TON REVENU' },
  { id: 'allegra', picto: 'bag', name: 'ALLEGRA DIGITAL', tag: 'BOUTIQUES EN LIGNE · PUBLICITÉ · IA' },
];

(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1024, height: 1024 }, deviceScaleFactor: 2 });
  for (const br of BRANDS) {
    for (const flat of [false, true]) {
      const file = path.join(__dirname, `_${br.id}_${flat ? 'flat' : 'badge'}.html`);
      fs.writeFileSync(file, build({ ...br, flat }));
      await p.goto('file://' + file);
      await p.evaluate(() => document.fonts.ready);
      await p.waitForTimeout(300);
      const fit = await p.evaluate(() => {
        const w = document.querySelector('#logo').getBoundingClientRect().width;
        const s = Math.min(1, 820 / w);
        document.querySelector('#logo').style.transform = `translate(-50%, -50%) scale(${s})`;
        return { w, s };
      });
      const out = path.join(OUT, `logo_${br.id}_${flat ? 'transparent' : 'rond'}.png`);
      if (flat) {
        const box = await p.evaluate(() => { const r = document.querySelector('#logo').getBoundingClientRect(); return { x: r.x, y: r.y, width: r.width, height: r.height }; });
        await p.screenshot({ path: out, omitBackground: true, clip: { x: box.x - 20, y: box.y - 20, width: box.width + 60, height: box.height + 60 } });
      } else {
        await p.screenshot({ path: out, omitBackground: true });
      }
      console.log(out, JSON.stringify(fit));
      fs.unlinkSync(file);
    }
  }
  await b.close();
})();
