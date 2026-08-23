import fs from "node:fs";
import path from "node:path";

const ROOT = "/home/user/Mike1272-Bus/videos/tiktok-boutique-18";
const LINES = path.join(ROOT, "audio/lines");
const FRAMES = path.join(ROOT, "compositions/frames");
fs.mkdirSync(FRAMES, { recursive: true });

const scenes = [
  { n: "01", id: "01-accroche", dur: 9.429, bg: "var(--pink-bg)" },
  { n: "02", id: "02-abonne", dur: 5.056, bg: "var(--yellow-bg)" },
  { n: "03", id: "03-lundi", dur: 5.504, bg: "var(--blue-bg)" },
  { n: "04", id: "04-mardi", dur: 4.885, bg: "var(--cream-bg)" },
  { n: "05", id: "05-mercredi", dur: 5.099, bg: "var(--green-bg)" },
  { n: "06", id: "06-jeudi", dur: 4.608, bg: "var(--blue-bg)" },
  { n: "07", id: "07-vendredi", dur: 4.331, bg: "var(--pink-bg)" },
  { n: "08", id: "08-samedi-kit", dur: 26.325, bg: "var(--yellow-bg)" },
  { n: "09", id: "09-cta", dur: 6.699, bg: "var(--yellow-bg)" },
];

function baseStyle() {
  return `
    #root {
      position: relative;
      width: 1080px;
      height: 1920px;
      overflow: hidden;
      font-family: -apple-system, "Segoe UI", Roboto, Arial, sans-serif;
      --f-display: "Arial Black", "Helvetica Neue", Arial, sans-serif;
      --black: #000000;
      --offwhite: #fffdf5;
      --blue-bg: #c0f7fe;
      --pink-bg: #fe90e8;
      --cream-bg: #ffdc8b;
      --yellow-bg: #f7cb46;
      --green-bg: #99e885;
    }
    #root * { box-sizing: border-box; }
    .fbg { position: absolute; inset: 0; }
    .fbg::before {
      content: "";
      position: absolute; inset: 0;
      background-image: radial-gradient(rgba(0,0,0,0.08) 1.2px, transparent 1.6px);
      background-size: 24px 24px;
    }
    .fcounter {
      position: absolute; left: 60px; top: 90px;
      width: 84px; height: 84px; border-radius: 50%;
      background: #ffffff; border: 4px solid var(--black); box-shadow: 6px 6px 0 var(--black);
      display: flex; align-items: center; justify-content: center;
      font-family: var(--f-display); font-weight: 800; font-size: 26px;
    }
    .flogo {
      position: absolute; right: 50px; top: 92px;
      width: 80px; height: 80px; border-radius: 50%;
      background: #ffffff; border: 4px solid var(--black); box-shadow: 5px 5px 0 var(--black);
      display: flex; align-items: center; justify-content: center; overflow: hidden;
    }
    .flogo img { width: 70%; height: 70%; object-fit: contain; display: block; }
    .fimg {
      position: absolute; left: 50%; top: 620px;
      width: 900px; height: 900px;
      transform: translateX(-50%);
      transform-origin: 50% 50%;
      opacity: 0;
      will-change: transform, opacity;
    }
    .fimg img { width: 100%; height: 100%; object-fit: contain; display: block; }
    .fimg.cover img { object-fit: cover; }
  `;
}

function renderScene(scene) {
  const timingPath = path.join(LINES, `${scene.n}.timing.json`);
  let images;
  if (fs.existsSync(timingPath)) {
    images = JSON.parse(fs.readFileSync(timingPath, "utf8"));
  } else {
    // single-image line (e.g. 09)
    images = [{ image: `l${scene.n}-nouvellefacon.jpeg`, start: 0, duration: scene.dur }];
  }

  const prefix = "f" + scene.n;
  const divs = images
    .map((im, i) => {
      const id = `${prefix}-img${i + 1}`;
      return `      <div class="fimg cover clip" data-start="${im.start}" data-duration="${im.duration}" data-track-index="2" id="${id}">
        <img src="assets/${im.image}" alt="" />
      </div>`;
    })
    .join("\n");

  const beats = images
    .map((im, i) => `      beat("${prefix}-img${i + 1}", ${im.start});`)
    .join("\n");

  const lastIdx = images.length;
  const lastImg = images[images.length - 1];
  const idleStart = lastImg.start + Math.min(lastImg.duration, 0.4);
  const idleDur = scene.dur - idleStart;
  const idleBlock = idleDur > 0.3
    ? `
      var phase = { p: 0 };
      var IDLE_START = ${idleStart.toFixed(3)};
      var IDLE_DUR = ${scene.dur} - IDLE_START;
      if (IDLE_DUR > 0.3) {
        tl.to(phase, {
          p: Math.PI * 2 * (IDLE_DUR / 2.5),
          duration: IDLE_DUR,
          ease: "none",
          onUpdate: function () {
            var s = Math.sin(phase.p);
            document.getElementById("${prefix}-img${lastIdx}").style.transform = "translateX(-50%) translateY(" + (s * 6).toFixed(2) + "px)";
          },
        }, IDLE_START);
      }`
    : "";

  // logo: small corner mark on every scene except the final CTA (which gets a big centered badge instead)
  const logoCorner = scene.n === "09" ? "" : `    <div class="flogo clip" data-start="0" data-duration="${scene.dur}" data-track-index="1">
      <img src="assets/adg-logo-transparent.png" alt="ADG" />
    </div>\n`;

  const ctaBadge = scene.n === "09" ? `
    <div class="fcta-badge clip" data-start="0" data-duration="${scene.dur}" data-track-index="3" id="${prefix}-badge">
      <img src="assets/adg-logo-transparent.png" alt="ADG" />
    </div>
    <div class="fcta-text clip" data-start="0.4" data-duration="${scene.dur - 0.4}" data-track-index="4" id="${prefix}-ctatext">
      ÉCRIS "KIT"<br>EN MESSAGE
    </div>` : "";

  const ctaStyles = scene.n === "09" ? `
    .fcta-badge {
      position: absolute; top: 130px; left: 50%; transform: translateX(-50%);
      width: 300px; height: 300px; border-radius: 50%; background: #fff;
      border: 7px solid var(--black); box-shadow: 12px 12px 0 var(--black);
      display: flex; align-items: center; justify-content: center; opacity: 0;
    }
    .fcta-badge img { width: 68%; height: 68%; object-fit: contain; }
    .fcta-text {
      position: absolute; top: 1420px; left: 50px; right: 50px; text-align: center;
      font-family: var(--f-display); font-weight: 900; font-size: 62px; line-height: 1.18;
      text-transform: uppercase; color: #000; opacity: 0;
    }
  ` : "";

  const ctaAnim = scene.n === "09" ? `
      tl.fromTo("#${prefix}-badge", { scale: 0.4, opacity: 0, rotation: -6 }, { scale: 1, opacity: 1, rotation: 0, duration: 0.35, ease: "back.out(2)" }, 0);
      tl.fromTo("#${prefix}-ctatext", { opacity: 0, y: 30 }, { opacity: 1, y: 0, duration: 0.35, ease: "power2.out" }, 0.4);
  ` : "";

  return `<template>
  <style>${baseStyle()}
    .f${scene.n}-bgfill { background-color: ${scene.bg}; }
    ${ctaStyles}
  </style>

  <div id="root" data-composition-id="${scene.id}" data-duration="${scene.dur}" data-width="1080" data-height="1920">
    <div class="fbg f${scene.n}-bgfill clip" data-start="0" data-duration="${scene.dur}" data-track-index="0"></div>
    <div class="fcounter clip" data-start="0" data-duration="${scene.dur}" data-track-index="1">${scene.n}</div>
${logoCorner}${divs}
${ctaBadge}
  </div>

  <script>
    (function () {
      window.__timelines = window.__timelines || {};
      var tl = gsap.timeline({ paused: true });

      function beat(id, start) {
        var el = document.getElementById(id);
        if (!el) return;
        tl.fromTo(
          el,
          { scale: 0.55, opacity: 0, rotation: -4 },
          { scale: 1, opacity: 1, rotation: 0, duration: 0.22, ease: "back.out(2.2)" },
          start
        );
      }

${beats}
${idleBlock}
${ctaAnim}

      window.__timelines["${scene.id}"] = tl;
    })();
  </script>
</template>
`;
}

for (const scene of scenes) {
  const html = renderScene(scene);
  const fp = path.join(FRAMES, `${scene.n}-${scene.id.split("-").slice(1).join("-")}.html`);
  fs.writeFileSync(fp, html);
  console.log("wrote", fp);
}
