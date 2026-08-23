// Match ordered phrases against a line's words.json to derive per-image
// display windows (start,duration), continuing the phrase-matching approach
// used on videos 16/17.
import fs from "node:fs";

function norm(s) {
  return s
    .toLowerCase()
    .normalize("NFD").replace(/[̀-ͯ]/g, "") // strip accents for robust matching
    .replace(/[^a-z0-9]+/g, " ")
    .trim();
}

function findPhraseStart(words, tokens, searchFromIdx) {
  const wnorm = words.map((w) => norm(w.text));
  for (let i = searchFromIdx; i <= wnorm.length - tokens.length; i++) {
    let ok = true;
    for (let j = 0; j < tokens.length; j++) {
      if (wnorm[i + j] !== tokens[j]) { ok = false; break; }
    }
    if (ok) return i;
  }
  // fallback: try matching just the first token from searchFromIdx
  for (let i = searchFromIdx; i < wnorm.length; i++) {
    if (wnorm[i] === tokens[0]) return i;
  }
  return searchFromIdx;
}

const [, , wordsPath, phrasesPath, lineDuration, outPath] = process.argv;
const words = JSON.parse(fs.readFileSync(wordsPath, "utf8"));
const phrases = JSON.parse(fs.readFileSync(phrasesPath, "utf8")); // [{phrase, image}]
const totalDur = parseFloat(lineDuration);

let searchIdx = 0;
const starts = phrases.map((p) => {
  const tokens = norm(p.phrase).split(" ").filter(Boolean);
  const idx = findPhraseStart(words, tokens, searchIdx);
  searchIdx = Math.max(searchIdx, idx + 1);
  const start = idx < words.length ? words[idx].start : totalDur;
  return start;
});

const out = phrases.map((p, i) => {
  const start = i === 0 ? 0 : starts[i];
  const end = i + 1 < phrases.length ? starts[i + 1] : totalDur;
  return { image: p.image, start: +start.toFixed(3), duration: +Math.max(end - start, 0.15).toFixed(3) };
});

fs.writeFileSync(outPath, JSON.stringify(out, null, 2));
console.log(`wrote ${out.length} image windows -> ${outPath}`);
