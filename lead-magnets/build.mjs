import fs from "node:fs";
import path from "node:path";
import pkg from "/opt/node22/lib/node_modules/playwright/index.js";
const { chromium } = pkg;

const DIR = "/home/user/Mike1272-Bus/lead-magnets";

const CSS = `
@font-face { font-family: "Work Sans"; src: url("fonts/work-sans-variable.woff2") format("woff2"); font-weight: 100 900; font-style: normal; }
@font-face { font-family: "Archivo Black"; src: url("fonts/archivo-black-400.woff2") format("woff2"); font-weight: 400; font-style: normal; }
* { margin:0; padding:0; box-sizing:border-box; }
html,body { width:1080px; font-family:"Work Sans",sans-serif; }
:root { --ink:#0A0A05; --cream:#FFFDF5; --mint:#CFF3D8; --sky:#CDEFFA; --pink:#FBD6E9; --butter:#FDEBAE; }
.page { position:relative; width:1080px; height:1350px; overflow:hidden; page-break-after:always; }
.page:last-child { page-break-after:auto; }
.dots { position:absolute; inset:0; background-image:radial-gradient(rgba(10,10,5,0.16) 3px, transparent 3px); background-size:38px 38px; }
.badge { position:absolute; left:64px; top:64px; width:96px; height:96px; border-radius:50%; background:var(--cream); border:5px solid var(--ink); display:flex; align-items:center; justify-content:center; font-family:"Archivo Black",sans-serif; font-size:38px; color:var(--ink); z-index:3; }
.pill { position:absolute; right:64px; top:80px; background:var(--ink); color:var(--cream); font-family:"Work Sans",sans-serif; font-weight:700; font-size:24px; letter-spacing:0.06em; text-transform:uppercase; padding:14px 30px; border-radius:999px; z-index:3; }
.headline { position:absolute; left:64px; top:210px; right:64px; font-family:"Archivo Black",sans-serif; font-weight:400; text-transform:uppercase; font-size:74px; line-height:1.04; color:var(--ink); z-index:3; }
.card { position:absolute; left:64px; right:64px; background:var(--cream); border:6px solid var(--ink); border-radius:14px; box-shadow:14px 14px 0 var(--ink); padding:46px 50px; z-index:3; }
.card p { font-family:"Work Sans",sans-serif; font-weight:600; font-size:34px; line-height:1.42; color:var(--ink); }
.checklist { list-style:none; }
.checklist li { display:flex; align-items:flex-start; gap:22px; font-family:"Work Sans",sans-serif; font-weight:700; font-size:32px; line-height:1.32; color:var(--ink); margin-bottom:26px; }
.checklist li:last-child { margin-bottom:0; }
.x { flex:none; width:40px; height:40px; border-radius:50%; background:#E1544A; color:var(--cream); display:flex; align-items:center; justify-content:center; font-family:"Archivo Black",sans-serif; font-size:22px; margin-top:2px; }
.icon-ring { position:absolute; left:64px; top:210px; width:190px; height:190px; border-radius:50%; background:var(--cream); border:6px solid var(--ink); display:flex; align-items:center; justify-content:center; font-size:96px; z-index:3; box-shadow:10px 10px 0 var(--ink); }
.footer { position:absolute; left:64px; right:64px; bottom:52px; display:flex; justify-content:space-between; align-items:center; border-top:3px solid rgba(10,10,5,0.25); padding-top:20px; z-index:3; }
.footer span { font-family:"Work Sans",sans-serif; font-weight:700; font-size:22px; letter-spacing:0.08em; text-transform:uppercase; color:var(--ink); opacity:0.65; }
.cover-eyebrow { position:absolute; left:64px; top:110px; background:var(--ink); color:var(--cream); font-family:"Work Sans",sans-serif; font-weight:700; font-size:26px; letter-spacing:0.08em; text-transform:uppercase; padding:16px 34px; border-radius:999px; }
.cover-title { position:absolute; left:64px; right:64px; top:230px; font-family:"Archivo Black",sans-serif; font-weight:400; text-transform:uppercase; font-size:118px; line-height:1.0; color:var(--ink); }
.cover-tagline { position:absolute; left:64px; right:120px; top:560px; font-family:"Work Sans",sans-serif; font-weight:600; font-size:40px; line-height:1.35; color:var(--ink); }
.cover-mark { position:absolute; left:64px; bottom:70px; font-family:"Archivo Black",sans-serif; font-size:30px; color:var(--ink); text-transform:uppercase; }
.cover-mark small { display:block; font-family:"Work Sans",sans-serif; font-weight:600; font-size:24px; text-transform:none; margin-top:6px; opacity:0.7; }
.shape { position:absolute; z-index:1; }
.sq { width:200px; height:200px; border:6px solid var(--ink); background:var(--butter); transform:rotate(-8deg); }
.ring { width:170px; height:170px; border-radius:50%; border:9px solid var(--ink); }
.img-card { position:absolute; left:64px; right:64px; top:210px; height:420px; border:6px solid var(--ink); border-radius:14px; box-shadow:14px 14px 0 var(--ink); overflow:hidden; z-index:3; background:var(--ink); }
.img-card img { width:100%; height:100%; object-fit:cover; }
.numbadge { flex:none; width:56px; height:56px; border-radius:50%; background:var(--ink); color:var(--cream); font-family:"Archivo Black",sans-serif; font-size:28px; display:flex; align-items:center; justify-content:center; }
.recap li { display:flex; align-items:center; gap:24px; font-family:"Work Sans",sans-serif; font-weight:700; font-size:32px; color:var(--ink); margin-bottom:24px; }
.recap li:last-child { margin-bottom:0; }
`;

function coverPage({ bg, eyebrow, title, tagline, episode }) {
  return `<div class="page" style="background:${bg}">
    <div class="dots"></div>
    <div class="shape sq" style="top:-40px; right:130px;"></div>
    <div class="shape ring" style="bottom:120px; right:70px; border-color:var(--ink);"></div>
    <div class="cover-eyebrow">Mini guide</div>
    <div class="cover-title">${title}</div>
    <div class="cover-tagline">${tagline}</div>
    <div class="cover-mark">DigitalMikaelson<small>Michaelson Digital Academy — ${episode}</small></div>
  </div>`;
}

function textPage({ bg, num, category, title, text, page, total }) {
  return `<div class="page" style="background:${bg}">
    <div class="dots"></div>
    <div class="badge">${num}</div>
    <div class="pill">${category}</div>
    <div class="headline">${title}</div>
    <div class="card" style="top:460px;"><p>${text}</p></div>
    <div class="footer"><span>${category}</span><span>${page} / ${total}</span></div>
  </div>`;
}

function checklistPage({ bg, num, category, title, items, page, total }) {
  const lis = items.map(t => `<li><span class="x">&#10005;</span><span>${t}</span></li>`).join("");
  return `<div class="page" style="background:${bg}">
    <div class="dots"></div>
    <div class="badge">${num}</div>
    <div class="pill">${category}</div>
    <div class="headline">${title}</div>
    <div class="card" style="top:460px;"><ul class="checklist">${lis}</ul></div>
    <div class="footer"><span>${category}</span><span>${page} / ${total}</span></div>
  </div>`;
}

function iconStepPage({ bg, num, category, title, icon, text, page, total }) {
  return `<div class="page" style="background:${bg}">
    <div class="dots"></div>
    <div class="badge">${num}</div>
    <div class="pill">${category}</div>
    <div class="icon-ring">${icon}</div>
    <div class="headline" style="top:440px;">${title}</div>
    <div class="card" style="top:600px;"><p>${text}</p></div>
    <div class="footer"><span>${category}</span><span>${page} / ${total}</span></div>
  </div>`;
}

function examplePage({ bg, num, category, title, img, text, page, total }) {
  return `<div class="page" style="background:${bg}">
    <div class="dots"></div>
    <div class="badge">${num}</div>
    <div class="pill">${category}</div>
    <div class="headline">${title}</div>
    <div class="img-card" style="top:400px; height:360px;"><img src="${img}" /></div>
    <div class="card" style="top:800px;"><p>${text}</p></div>
    <div class="footer"><span>${category}</span><span>${page} / ${total}</span></div>
  </div>`;
}

function recapPage({ bg, num, category, title, items, cta, page, total }) {
  const lis = items.map((t, i) => `<li><span class="numbadge">${i + 1}</span><span>${t}</span></li>`).join("");
  return `<div class="page" style="background:${bg}">
    <div class="dots"></div>
    <div class="badge">${num}</div>
    <div class="pill">${category}</div>
    <div class="headline">${title}</div>
    <div class="card" style="top:460px;"><ul class="recap">${lis}</ul></div>
    <div class="card" style="top:900px; background:var(--ink);"><p style="color:var(--cream);">${cta}</p></div>
    <div class="footer"><span>${category}</span><span>${page} / ${total}</span></div>
  </div>`;
}

function wrap(pagesHtml) {
  return `<!doctype html><html lang="fr"><head><meta charset="UTF-8"><style>${CSS}</style></head><body>${pagesHtml}</body></html>`;
}

// ---------------- GUIDE 1: LA DISTRIBUTION ----------------
const distTotal = 8;
const distPages = [
  coverPage({
    bg: "var(--cream)",
    title: "La<br/>Distribution",
    tagline: "Transforme ta notoriété en clients qui reviennent.",
    episode: "Épisode 6",
  }),
  textPage({
    bg: "var(--mint)", num: "01", category: "Pourquoi ce guide", page: 1, total: distTotal,
    title: "Être connu ne suffit pas",
    text: "Les gens te connaissent, ils aiment ce que tu fais, certains disent même qu'ils vont acheter. Et pourtant, rien ne se passe. Ce guide t'explique pourquoi, et ce qu'il faut changer.",
  }),
  checklistPage({
    bg: "var(--sky)", num: "02", category: "Le problème", page: 2, total: distTotal,
    title: "Ce qui bloque la vente",
    items: [
      "Il faut écrire en message privé pour savoir comment acheter",
      "Le lien pour payer change à chaque publication",
      "Il y a plusieurs étapes avant de pouvoir payer",
      "Personne ne sait où te retrouver pour acheter",
    ],
  }),
  iconStepPage({
    bg: "var(--butter)", num: "03", category: "Étape 1", page: 3, total: distTotal,
    title: "Un seul lien", icon: "&#128279;",
    text: "Choisis un seul endroit où on peut acheter. Toujours le même, partout. Un lien que tu pourrais réciter de mémoire.",
  }),
  iconStepPage({
    bg: "var(--mint)", num: "04", category: "Étape 2", page: 4, total: distTotal,
    title: "Moins de clics", icon: "&#128070;",
    text: "Entre « je veux acheter » et « j'ai payé », vise deux ou trois clics maximum. Chaque étape en plus, c'est une personne qui abandonne en route.",
  }),
  iconStepPage({
    bg: "var(--sky)", num: "05", category: "Étape 3", page: 5, total: distTotal,
    title: "Répète-le partout", icon: "&#128260;",
    text: "Mets ce lien dans ta bio, sous chaque vidéo, dans tes réponses aux commentaires, sans jamais en changer.",
  }),
  examplePage({
    bg: "var(--butter)", num: "06", category: "Exemple réel", page: 6, total: distTotal,
    title: "Ce qu'a fait Oncle David",
    img: "guide-menuiserie-cover.jpg",
    text: "Son guide de menuiserie existait depuis des mois. Chaque vente demandait un message privé, et beaucoup abandonnaient avant la réponse. Un seul lien fixe a tout changé : les commandes tombent maintenant chaque semaine.",
  }),
  recapPage({
    bg: "var(--cream)", num: "07", category: "Passe à l'action", page: 7, total: distTotal,
    title: "À toi de jouer",
    items: ["Choisis ton lien unique", "Réduis le chemin jusqu'au paiement", "Répète ce lien partout, tout le temps"],
    cta: "Abonne-toi à DigitalMikaelson pour la suite de la stratégie VENDRE : la Relance (R), au prochain épisode.",
  }),
];

// ---------------- GUIDE 2: LA RELANCE ----------------
const relTotal = 8;
const relPages = [
  coverPage({
    bg: "var(--cream)",
    title: "La<br/>Relance",
    tagline: "Fais revenir tes clients, au lieu d'en chercher sans arrêt de nouveaux.",
    episode: "Épisode 7",
  }),
  textPage({
    bg: "var(--pink)", num: "01", category: "Pourquoi ce guide", page: 1, total: relTotal,
    title: "Chercher du neuf, ça coûte cher",
    text: "Tu passes du temps à chercher de nouvelles personnes, alors que celles qui ont déjà acheté chez toi une fois sont juste là, à côté. Ce guide t'explique comment les faire revenir.",
  }),
  checklistPage({
    bg: "var(--sky)", num: "02", category: "Le problème", page: 2, total: relTotal,
    title: "Ce qu'on oublie de faire",
    items: [
      "On ne garde aucune trace de qui a déjà acheté",
      "On ne recontacte jamais après la première vente",
      "Le seul message envoyé, c'est « achète encore »",
      "On attend que les clients reviennent tout seuls",
    ],
  }),
  iconStepPage({
    bg: "var(--butter)", num: "03", category: "Étape 1", page: 3, total: relTotal,
    title: "Garde une trace", icon: "&#128209;",
    text: "Note qui a acheté. Un contact, un numéro, une liste toute simple suffit. Sans ça, impossible de recontacter qui que ce soit.",
  }),
  iconStepPage({
    bg: "var(--pink)", num: "04", category: "Étape 2", page: 4, total: relTotal,
    title: "Propose du nouveau", icon: "&#128172;",
    text: "Propose une vraie offre, un vrai message, presque personnel, comme si tu écrivais à quelqu'un que tu connais.",
  }),
  iconStepPage({
    bg: "var(--sky)", num: "05", category: "Étape 3", page: 5, total: relTotal,
    title: "Fais-le régulièrement", icon: "&#128197;",
    text: "Recontacte tes clients toutes les quelques semaines, même juste pour prendre des nouvelles. Sinon, le lien retombe à zéro.",
  }),
  examplePage({
    bg: "var(--butter)", num: "06", category: "Exemple réel", page: 6, total: relTotal,
    title: "Ce qu'a fait Oncle David",
    img: "guide-menuiserie-cover.jpg",
    text: "Après sa première vente, il attendait juste que de nouvelles personnes le découvrent. Un jour, il a réécrit à tous ses anciens clients pour leur proposer un deuxième guide. La moitié ont acheté à nouveau en quelques jours.",
  }),
  recapPage({
    bg: "var(--cream)", num: "07", category: "Passe à l'action", page: 7, total: relTotal,
    title: "À toi de jouer",
    items: ["Note qui a déjà acheté", "Recontacte avec une vraie offre", "Reviens vers eux régulièrement"],
    cta: "Abonne-toi à DigitalMikaelson pour la suite de la stratégie VENDRE : l'Évolution (E), au prochain épisode.",
  }),
];

fs.writeFileSync(path.join(DIR, "guide-distribution.html"), wrap(distPages.join("\n")));
fs.writeFileSync(path.join(DIR, "guide-relance.html"), wrap(relPages.join("\n")));

const browser = await chromium.launch();
for (const name of ["guide-distribution", "guide-relance"]) {
  const page = await browser.newPage();
  await page.goto(`file://${DIR}/${name}.html`);
  await page.waitForTimeout(300);
  await page.pdf({
    path: path.join(DIR, `${name}.pdf`),
    width: "1080px",
    height: "1350px",
    printBackground: true,
    margin: { top: 0, bottom: 0, left: 0, right: 0 },
  });
  await page.close();
  console.log(`${name}.pdf done`);
}
await browser.close();
