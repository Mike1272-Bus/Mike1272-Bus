import fs from "node:fs";
import path from "node:path";

const ROOT = "/home/user/Mike1272-Bus/videos/tiktok-boutique-18";

const scenes = [
  { n: "01", file: "01-accroche.html", dur: 9.429 },
  { n: "02", file: "02-abonne.html", dur: 5.056 },
  { n: "03", file: "03-lundi.html", dur: 5.504 },
  { n: "04", file: "04-mardi.html", dur: 4.885 },
  { n: "05", file: "05-mercredi.html", dur: 5.099 },
  { n: "06", file: "06-jeudi.html", dur: 4.608 },
  { n: "07", file: "07-vendredi.html", dur: 4.331 },
  { n: "08", file: "08-samedi-kit.html", dur: 26.325 },
  { n: "09", file: "09-cta.html", dur: 6.699 },
];
const GAP = 0.35;

let t = 0;
const starts = [];
for (const s of scenes) {
  starts.push(t);
  t += s.dur + GAP;
}
const TOTAL = +(t - GAP).toFixed(3); // end of last scene, no trailing gap

const sceneDivs = scenes
  .map((s, i) => {
    const trackIdx = i % 2;
    return `      <div
        id="el-${s.n}"
        class="scene"
        data-composition-id="${s.n}"
        data-composition-src="compositions/frames/${s.file}"
        data-start="${starts[i]}"
        data-duration="${s.dur}"
        data-track-index="${trackIdx}"
      ></div>`;
  })
  .join("\n");

const transitions = [];
for (let i = 0; i < scenes.length - 1; i++) {
  const curId = `#el-${scenes[i].n}`;
  const nextId = `#el-${scenes[i + 1].n}`;
  const at = +(starts[i + 1]).toFixed(3);
  if (i % 2 === 0) {
    transitions.push(`        tl.to("${curId}", { x: -1080, duration: 0.4, ease: "power3.inOut" }, ${at});`);
    transitions.push(`        tl.fromTo("${nextId}", { x: 1080, opacity: 1 }, { x: 0, duration: 0.4, ease: "power3.inOut" }, ${at});`);
  } else {
    transitions.push(`        tl.to("${curId}", { scale: 2.5, opacity: 0, filter: "blur(8px)", duration: 0.3, ease: "power3.in" }, ${at});`);
    transitions.push(`        tl.fromTo("${nextId}", { scale: 0.5, opacity: 0, filter: "blur(8px)" }, { scale: 1, opacity: 1, filter: "blur(0px)", duration: 0.3, ease: "power3.out" }, ${at});`);
  }
}
transitions.push(`        tl.to({}, { duration: ${TOTAL} }, 0);`);

const html = `<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1080, height=1920" />
    <script src="./vendor/gsap.min.js"></script>
    <style>
      * { margin: 0; padding: 0; box-sizing: border-box; }
      html, body { width: 1080px; height: 1920px; overflow: hidden; background: #000; }
      #root { position: relative; width: 1080px; height: 1920px; overflow: hidden; background: #FFFFFF; }
      .scene { position: absolute; inset: 0; width: 100%; height: 100%; }
    </style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="${TOTAL}" data-width="1080" data-height="1920">
${sceneDivs}

      <audio
        id="el-voice"
        src="audio/voice.mp3"
        data-start="0"
        data-duration="${TOTAL}"
        data-track-index="10"
        data-volume="1"
      ></audio>

      <div
        id="el-captions"
        class="scene"
        data-composition-id="captions"
        data-composition-src="compositions/captions.html"
        data-start="0"
        data-duration="${TOTAL}"
        data-track-index="2"
      ></div>

    </div>
    <script>
      window.__timelines = window.__timelines || {};
      window.__timelines["main"] = gsap.timeline({ paused: true });
      (function () { var tl = window.__timelines["main"];
${transitions.join("\n")}
      })();
    </script>
  </body>
</html>
`;

fs.writeFileSync(path.join(ROOT, "index.html"), html);
console.log("TOTAL duration:", TOTAL);
console.log("scene starts:", starts);
