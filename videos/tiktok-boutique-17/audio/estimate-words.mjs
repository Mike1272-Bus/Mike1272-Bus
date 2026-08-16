// Deterministic word-timing estimate for caption sync when ASR (whisper/parakeet)
// is unavailable (offline environment, no HF model download). Allocates each
// line's known TTS duration across its words, weighted by character count,
// with a small fixed inter-word gap. Re-run against the real duration once
// the user's own voice recording replaces the Kokoro line.
import fs from "node:fs";

const GAP = 0.06; // seconds between words

function estimate(text, duration) {
  const words = text
    .replace(/[""]/g, '"')
    .trim()
    .split(/\s+/)
    .map((w) => w.replace(/^[("]+|[)",.;:!?]+$/g, "") ? w : w);

  const weights = words.map((w) => {
    const bare = w.replace(/[^\p{L}\p{N}]/gu, "");
    let weight = Math.max(bare.length, 1);
    if (/[,;:]$/.test(w)) weight += 1.5; // mid-sentence pause
    if (/[.!?]$/.test(w)) weight += 2.5; // sentence-end pause
    return weight;
  });

  const totalGap = GAP * (words.length - 1);
  const speakBudget = Math.max(duration - totalGap, duration * 0.5);
  const totalWeight = weights.reduce((a, b) => a + b, 0);

  let t = 0;
  const out = [];
  words.forEach((w, i) => {
    const dur = (weights[i] / totalWeight) * speakBudget;
    const start = t;
    const end = start + dur;
    out.push({ id: "w" + i, text: w, start: +start.toFixed(3), end: +end.toFixed(3) });
    t = end + GAP;
  });
  return out;
}

const [, , textArg, durationArg, outArg] = process.argv;
if (!textArg || !durationArg || !outArg) {
  console.error("usage: node estimate-words.mjs <text> <duration_s> <out.json>");
  process.exit(1);
}
const words = estimate(textArg, parseFloat(durationArg));
fs.writeFileSync(outArg, JSON.stringify(words, null, 2));
console.log(`wrote ${words.length} words -> ${outArg}`);
