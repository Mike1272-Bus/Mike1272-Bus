import fs from "node:fs";
import path from "node:path";

const ROOT = "/home/user/Mike1272-Bus/videos/tiktok-boutique-18";
const LINES = path.join(ROOT, "audio/lines");

const lineMeta = [
  { n: "01", start: 0 },
  { n: "02", start: 9.779 },
  { n: "03", start: 15.185 },
  { n: "04", start: 21.039 },
  { n: "05", start: 26.274 },
  { n: "06", start: 31.723 },
  { n: "07", start: 36.681 },
  { n: "08", start: 41.362 },
  { n: "09", start: 68.037 },
];
const DURATION = 74.736;

let groups = [];
let gIdx = 0;
for (const meta of lineMeta) {
  const words = JSON.parse(fs.readFileSync(path.join(LINES, `${meta.n}.words.json`), "utf8"));
  for (let i = 0; i < words.length; i += 3) {
    const chunk = words.slice(i, i + 3);
    const gwords = chunk.map((w, k) => ({
      id: `caption-word-${gIdx}-${k}`,
      text: w.text,
      start: +(w.start + meta.start).toFixed(3),
      end: +(w.end + meta.start).toFixed(3),
    }));
    groups.push({
      id: `caption-group-${gIdx}`,
      frame: parseInt(meta.n, 10),
      start: gwords[0].start,
      end: gwords[gwords.length - 1].end,
      text: chunk.map((w) => w.text).join(" "),
      words: gwords,
    });
    gIdx++;
  }
}

const captionsTemplate = fs.readFileSync(path.join(ROOT, "compositions/captions.html.template"), "utf8");
const out = captionsTemplate
  .replaceAll("__GROUPS__", JSON.stringify(groups))
  .replaceAll("__DURATION__", String(DURATION));

fs.writeFileSync(path.join(ROOT, "compositions/captions.html"), out);
console.log(`wrote ${groups.length} caption groups, duration=${DURATION}`);
