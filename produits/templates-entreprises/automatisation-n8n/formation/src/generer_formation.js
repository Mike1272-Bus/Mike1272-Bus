// Formation : installer le système de stock automatisé (Google Sheets + n8n + WhatsApp)
const pptxgen = require("pptxgenjs");
const React = require("react");
const RDS = require("react-dom/server");
const sharp = require("sharp");
const fa = require("react-icons/fa");
const si = require("react-icons/si");
const fs = require("fs");
const path = require("path");
const { applyTheme } = require(process.env.PPTX_SKILL + "/scripts/apply_theme.js");

const OUT = process.argv[2] || "formation.pptx";
const LOGO = process.env.LOGO;

const THEME = {
  name: "Allegra Formation",
  headFontFace: "Arial",
  bodyFontFace: "Calibri",
  colors: {
    dk1: "1B2340", lt1: "FFFFFF", dk2: "3A4566", lt2: "EEF2F8",
    accent1: "F5C518", // jaune Allegra
    accent2: "1E8E3E", // Google
    accent3: "EA4B71", // n8n
    accent4: "1877F2", // Meta
    accent5: "128C7E", // WhatsApp
    accent6: "D93025", // erreur
    hlink: "1877F2", folHlink: "6B4FBB",
  },
};
const HEX = { navy: "1B2340", ink2: "3A4566", light: "EEF2F8", yellow: "F5C518", google: "1E8E3E", n8n: "EA4B71", meta: "1877F2", wa: "128C7E", red: "D93025", gray: "6B7280", line: "D5DCE8", white: "FFFFFF", amber: "B26A00" };

const pres = new pptxgen();
pres.layout = "LAYOUT_WIDE"; // 13.333 x 7.5
pres.title = "Installer le système de stock automatisé";
pres.author = "Allegra Digital Ground";
pres.company = "Allegra Digital Ground";
pres.theme = { headFontFace: THEME.headFontFace, bodyFontFace: THEME.bodyFontFace };
const C = pres.SchemeColor;
const W = 13.333, H = 7.5, M = 0.6;

// ---------- layouts ----------
pres.defineSlideMaster({
  title: "COUVERTURE",
  background: { color: HEX.navy },
  objects: [
    { placeholder: { options: { name: "title", type: "title", x: M, y: 2.55, w: 8.4, h: 1.9, fontSize: 44, bold: true, color: C.background1, valign: "top", align: "left", margin: 0 }, text: "" } },
    { placeholder: { options: { name: "body", type: "body", x: M, y: 4.55, w: 8.0, h: 1.0, fontSize: 18, color: C.accent1, valign: "top", margin: 0 }, text: "" } },
  ],
});
pres.defineSlideMaster({
  title: "SECTION",
  background: { color: HEX.navy },
  objects: [
    { placeholder: { options: { name: "title", type: "title", x: 4.3, y: 2.6, w: 8.4, h: 1.3, fontSize: 40, bold: true, color: C.background1, valign: "top", align: "left", margin: 0 }, text: "" } },
    { placeholder: { options: { name: "body", type: "body", x: 4.3, y: 3.95, w: 8.2, h: 1.4, fontSize: 18, color: C.background2, valign: "top", margin: 0 }, text: "" } },
  ],
  slideNumber: { x: 12.3, y: 6.95, w: 0.6, h: 0.3, fontSize: 10, color: "9AA6C2", align: "right" },
});
pres.defineSlideMaster({
  title: "CONTENU",
  background: { color: HEX.white },
  objects: [
    { placeholder: { options: { name: "title", type: "title", x: M, y: 0.4, w: 9.6, h: 0.8, fontSize: 30, bold: true, color: C.text1, valign: "middle", align: "left", margin: 0 }, text: "" } },
    { text: { text: "Système de stock automatisé · Guide d'installation", options: { x: M, y: 7.0, w: 7, h: 0.3, fontSize: 10, color: "8A93A8", margin: 0 } } },
  ],
  slideNumber: { x: 12.3, y: 7.0, w: 0.45, h: 0.3, fontSize: 10, color: "8A93A8", align: "right" },
});

// ---------- icons ----------
const iconCache = {};
async function icon(name, color = "FFFFFF", size = 256) {
  const key = name + color;
  if (iconCache[key]) return iconCache[key];
  const Comp = fa[name] || si[name];
  if (!Comp) throw new Error("icon " + name);
  const svg = RDS.renderToStaticMarkup(React.createElement(Comp, { color: "#" + color, size: String(size) }));
  const buf = await sharp(Buffer.from(svg)).png().toBuffer();
  return (iconCache[key] = "image/png;base64," + buf.toString("base64"));
}
async function circleIcon(s, x, y, d, name, bg, fg = "FFFFFF") {
  s.addShape(pres.shapes.OVAL, { x, y, w: d, h: d, fill: { color: bg }, line: { color: bg }, objectName: "pastille " + name });
  const p = d * 0.22;
  s.addImage({ data: await icon(name, fg), x: x + p, y: y + p, w: d - 2 * p, h: d - 2 * p, altText: name });
}

// ---------- helpers ----------
const T = (s, text, o) => s.addText(text, Object.assign({ isTextBox: true, margin: 0, fontSize: 15, color: HEX.navy, valign: "top" }, o));

function badge(s, label, color) {
  // pastille d'étape en haut à droite (repère visuel du deck)
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: 10.45, y: 0.55, w: 2.28, h: 0.5, fill: { color }, line: { color }, rectRadius: 0.25, objectName: "badge étape" });
  T(s, label, { x: 10.45, y: 0.55, w: 2.28, h: 0.5, fontSize: 12, bold: true, color: HEX.white, align: "center", valign: "middle", charSpacing: 1 });
}

function content(title, step) {
  const s = pres.addSlide({ masterName: "CONTENU", sectionTitle: curSection });
  s.addText(title, { placeholder: "title" });
  if (step) badge(s, step[0], step[1]);
  return s;
}

// étapes numérotées : items = [[titre, détail], ...]
function steps(s, items, { x = M, y = 1.55, w = 6.6, gap = 0.12, color = HEX.navy, fs = 15, rowH } = {}) {
  const avail = 6.75 - y;
  const h = rowH || Math.min(0.95, (avail - gap * (items.length - 1)) / items.length);
  items.forEach((it, i) => {
    const yy = y + i * (h + gap);
    s.addShape(pres.shapes.OVAL, { x, y: yy + 0.02, w: 0.44, h: 0.44, fill: { color }, line: { color }, objectName: "numéro " + (i + 1) });
    T(s, String(i + 1), { x, y: yy + 0.02, w: 0.44, h: 0.44, fontSize: 15, bold: true, color: HEX.white, align: "center", valign: "middle" });
    const runs = [{ text: it[0], options: { bold: true } }];
    if (it[1]) runs.push({ text: "  " + it[1], options: { color: HEX.ink2 } });
    T(s, runs, { x: x + 0.62, y: yy, w: w - 0.62, h, fontSize: fs });
  });
}

const KIND = {
  tip: { bg: "E8F5EC", ic: "FaLightbulb", col: HEX.google, label: "Astuce" },
  warn: { bg: "FFF4D6", ic: "FaExclamationTriangle", col: HEX.amber, label: "Attention" },
  err: { bg: "FDE8E7", ic: "FaTimesCircle", col: HEX.red, label: "Erreur fréquente" },
  key: { bg: "E8F0FE", ic: "FaKey", col: HEX.meta, label: "Secret" },
  rule: { bg: "FFF4D6", ic: "FaStar", col: HEX.amber, label: "Règle d'or" },
};
async function callout(s, x, y, w, h, kind, text) {
  const k = KIND[kind];
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y, w, h, fill: { color: k.bg }, line: { color: k.bg }, rectRadius: 0.12, objectName: "encadré " + k.label });
  s.addImage({ data: await icon(k.ic, k.col), x: x + 0.22, y: y + 0.2, w: 0.38, h: 0.38, altText: k.label });
  T(s, [{ text: k.label + " : ", options: { bold: true, color: k.col } }, { text, options: { color: HEX.navy } }], { x: x + 0.78, y: y + 0.16, w: w - 0.98, h: h - 0.3, fontSize: 14, valign: "middle" });
}

function table(s, head, rows, { x = M, y = 1.55, w = W - 2 * M, colW, color = HEX.navy, fs = 14, rowH = 0.5 } = {}) {
  const hdr = head.map((t) => ({ text: t, options: { bold: true, color: HEX.white, fill: { color }, fontSize: fs, valign: "middle" } }));
  const body = rows.map((r, i) => r.map((t, j) => {
    const o = { fontSize: fs, color: HEX.navy, valign: "middle", fill: { color: i % 2 ? "F6F8FC" : HEX.white } };
    if (j === 0) o.bold = true;
    return typeof t === "string" ? { text: t, options: o } : { text: t.text, options: Object.assign(o, t.options) };
  }));
  s.addTable([hdr, ...body], { x, y, w, colW, rowH, border: { type: "solid", pt: 0.75, color: HEX.line }, margin: [4, 8, 4, 8], fontFace: "Calibri", objectName: "tableau" });
}

function card(s, x, y, w, h, fill = HEX.light) {
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y, w, h, fill: { color: fill }, line: { color: fill }, rectRadius: 0.15, objectName: "carte" });
}

function arrow(s, x1, y1, x2, y2, color = "9AA6C2") {
  s.addShape(pres.shapes.LINE, { x: Math.min(x1, x2), y: Math.min(y1, y2), w: Math.abs(x2 - x1) || 0.001, h: Math.abs(y2 - y1) || 0.001, flipH: x2 < x1, flipV: y2 < y1, line: { color, width: 2, endArrowType: "triangle" }, objectName: "flèche" });
}

async function section(num, title, body, color, ic) {
  curSection = title.replace(/\n/g, " ");
  pres.addSection({ title: curSection });
  const s = pres.addSlide({ masterName: "SECTION", sectionTitle: curSection });
  s.addShape(pres.shapes.OVAL, { x: 0.9, y: 2.15, w: 2.7, h: 2.7, fill: { color }, line: { color }, objectName: "cercle étape" });
  T(s, String(num), { x: 0.9, y: 2.15, w: 2.7, h: 1.75, fontSize: 80, bold: true, color: HEX.white, align: "center", valign: "bottom", fontFace: "Arial" });
  s.addImage({ data: await icon(ic, "FFFFFF"), x: 2.0, y: 3.95, w: 0.5, h: 0.5, altText: ic });
  T(s, "ÉTAPE " + num, { x: 4.3, y: 2.05, w: 5, h: 0.4, fontSize: 14, bold: true, color: HEX.yellow, charSpacing: 3 });
  s.addText(title, { placeholder: "title" });
  s.addText(body, { placeholder: "body" });
  return s;
}

// fausse fenêtre d'appli (maquette)
function windowFrame(s, x, y, w, h, label) {
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y, w, h, fill: { color: HEX.white }, line: { color: HEX.line, width: 1 }, rectRadius: 0.1, shadow: { type: "outer", color: "1B2340", opacity: 0.12, blur: 8, offset: 3, angle: 90 }, objectName: "fenêtre " + label });
  s.addShape(pres.shapes.RECTANGLE, { x: x + 0.02, y: y + 0.02, w: w - 0.04, h: 0.36, fill: { color: "F1F3F7" }, line: { color: "F1F3F7" }, objectName: "barre fenêtre" });
  ["FF5F57", "FEBC2E", "28C840"].forEach((c, i) => s.addShape(pres.shapes.OVAL, { x: x + 0.15 + i * 0.2, y: y + 0.13, w: 0.12, h: 0.12, fill: { color: c }, line: { color: c } }));
  T(s, label, { x: x + 0.85, y: y + 0.04, w: w - 1, h: 0.32, fontSize: 11, color: HEX.gray, valign: "middle" });
}

function bubble(s, x, y, w, h, title, body) {
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y, w, h, fill: { color: HEX.white }, line: { color: "E2E8F0" }, rectRadius: 0.12, shadow: { type: "outer", color: "000000", opacity: 0.12, blur: 4, offset: 1, angle: 90 }, objectName: "bulle WhatsApp" });
  T(s, [{ text: title, options: { bold: true, breakLine: true } }, { text: body }], { x: x + 0.15, y: y + 0.12, w: w - 0.3, h: h - 0.24, fontSize: 12 });
}

let curSection = "Introduction";

(async () => {
  // =============== 1. Couverture ===============
  pres.addSection({ title: "Introduction" });
  let s = pres.addSlide({ masterName: "COUVERTURE", sectionTitle: "Introduction" });
  if (LOGO) s.addImage({ path: LOGO, x: M, y: 0.6, w: 1.6, h: 1.27, altText: "Logo Allegra Digital Ground" });
  T(s, "FORMATION INTERNE", { x: M, y: 2.05, w: 6, h: 0.4, fontSize: 14, bold: true, color: HEX.yellow, charSpacing: 4 });
  s.addText("Installer le système de stock automatisé", { placeholder: "title" });
  s.addText("Google Sheets + n8n + WhatsApp, pas à pas, même si tu pars de zéro", { placeholder: "body" });
  const tools = [["SiGooglesheets", HEX.google, "Google Sheets"], ["FaProjectDiagram", HEX.n8n, "n8n"], ["SiMeta", HEX.meta, "Meta"], ["FaWhatsapp", HEX.wa, "WhatsApp"]];
  for (let i = 0; i < tools.length; i++) {
    const yy = 1.2 + i * 1.35;
    await circleIcon(s, 10.2, yy, 0.95, tools[i][0], tools[i][1]);
    T(s, tools[i][2], { x: 11.3, y: yy, w: 1.8, h: 0.95, fontSize: 16, bold: true, color: HEX.white, valign: "middle" });
  }

  // =============== 2. Comment utiliser ce guide ===============
  s = content("Comment utiliser ce guide");
  const how = [
    ["FaListOl", HEX.navy, "Suis l'ordre", "Les 4 étapes dépendent l'une de l'autre. Ne saute rien, même si ça paraît évident."],
    ["FaRegCheckSquare", HEX.google, "Coche au fur et à mesure", "Une check-list t'attend à la fin. Elle te dit si tout est prêt pour le client."],
    ["FaTools", HEX.red, "Bloqué ? Va au dépannage", "Les erreurs qu'on a déjà rencontrées sont expliquées avec leur solution."],
  ];
  for (let i = 0; i < 3; i++) {
    const x = M + i * 4.1;
    card(s, x, 1.6, 3.85, 3.4);
    await circleIcon(s, x + 0.35, 1.9, 0.85, how[i][0], how[i][1]);
    T(s, how[i][2], { x: x + 0.35, y: 2.95, w: 3.2, h: 0.5, fontSize: 19, bold: true });
    T(s, how[i][3], { x: x + 0.35, y: 3.5, w: 3.2, h: 1.4, fontSize: 15, color: HEX.ink2 });
  }
  await callout(s, M, 5.35, W - 2 * M, 1.1, "tip", "garde ce guide ouvert sur un écran et fais les manipulations sur l'autre (ou sur un deuxième onglet). Fais chaque étape en même temps que tu la lis.");

  // =============== 3. Le système en une image ===============
  s = content("Le système en une image");
  const flow = [
    ["FaStore", HEX.navy, "1. Le vendeur", "remplit un petit formulaire sur son téléphone à chaque vente"],
    ["FaProjectDiagram", HEX.n8n, "2. n8n", "reçoit la vente, retrouve le produit, calcule le nouveau stock"],
    ["SiGooglesheets", HEX.google, "3. Google Sheet", "la vente s'ajoute toute seule, le stock baisse"],
    ["FaWhatsapp", HEX.wa, "4. WhatsApp", "le patron est prévenu, le client reçoit sa confirmation"],
  ];
  for (let i = 0; i < 4; i++) {
    const x = M + i * 3.12;
    card(s, x, 1.75, 2.75, 3.3);
    await circleIcon(s, x + 0.9, 2.0, 0.95, flow[i][0], flow[i][1]);
    T(s, flow[i][2], { x: x + 0.2, y: 3.1, w: 2.35, h: 0.45, fontSize: 18, bold: true, align: "center" });
    T(s, flow[i][3], { x: x + 0.2, y: 3.6, w: 2.35, h: 1.3, fontSize: 14, color: HEX.ink2, align: "center" });
    if (i < 3) arrow(s, x + 2.8, 3.4, x + 3.07, 3.4, HEX.navy);
  }
  card(s, M, 5.4, W - 2 * M, 1.2, HEX.navy);
  T(s, [{ text: "À retenir : ", options: { bold: true, color: HEX.yellow } }, { text: "le patron n'a rien à faire. Tout part du formulaire du vendeur. Le soir et le matin, il reçoit aussi un résumé automatique sur WhatsApp.", options: { color: HEX.white } }], { x: M + 0.4, y: 5.4, w: W - 2 * M - 0.8, h: 1.2, fontSize: 17, valign: "middle" });

  // =============== 4. Les 4 automatisations ===============
  s = content("Les 4 automatisations du système");
  table(s, ["Workflow", "Se déclenche quand…", "Ce qu'il fait", "Message WhatsApp"], [
    ["Stock 1 · Commande", "le vendeur envoie le formulaire « Nouvelle commande »", "ajoute la vente dans l'onglet Commandes, vérifie le stock", "patron : nouvelle commande · client : confirmation · patron : alerte si stock bas"],
    ["Stock 2 · Bilan du soir", "chaque soir à 19 h, tout seul", "additionne les ventes et la marge du jour", "patron : bilan du soir"],
    ["Stock 3 · Arrivage", "le magasinier envoie le formulaire « Arrivage »", "ajoute la livraison dans l'onglet Arrivages, le stock monte", "patron : marchandise reçue"],
    ["Stock 4 · Point du matin", "chaque matin à 8 h, tout seul", "liste les produits à réapprovisionner", "patron : à commander aujourd'hui (seulement s'il y a quelque chose)"],
  ], { colW: [2.4, 3.1, 3.2, 3.43], rowH: [0.5, 0.9, 0.9, 0.9, 0.9], fs: 14 });
  await callout(s, M, 6.05, W - 2 * M, 0.75, "tip", "un « workflow » = une automatisation complète. Dans n8n, chacun est sur sa propre page.");

  // =============== 5-6. Lexique ===============
  s = content("Les mots à connaître (1/2)");
  table(s, ["Mot", "Ce que ça veut dire, simplement"], [
    ["n8n", "L'outil qui fait le travail tout seul, comme un employé invisible qui ne dort jamais."],
    ["Workflow", "Une automatisation complète : une page dans n8n. Le système en a 4 (Stock 1 à 4)."],
    ["Nœud", "Une case dans le workflow. Chaque case fait une seule action : lire, ajouter, calculer, envoyer."],
    ["Credential (connexion)", "La connexion enregistrée une fois pour toutes entre n8n et un autre service (Google, WhatsApp)."],
    ["Google Sheet", "Le tableau en ligne (comme Excel) où sont les produits, les ventes et les arrivages."],
    ["Onglet", "Une feuille du Google Sheet, en bas de l'écran : Produits, Commandes, Arrivages…"],
  ], { colW: [3.0, 9.13], rowH: 0.72, fs: 15 });
  s = content("Les mots à connaître (2/2)");
  table(s, ["Mot", "Ce que ça veut dire, simplement"], [
    ["Meta", "L'entreprise de Facebook et WhatsApp. C'est chez elle qu'on ouvre l'accès à WhatsApp pour n8n."],
    ["Modèle (template)", "Un message WhatsApp écrit à l'avance et validé par Meta, avec des trous {{1}}, {{2}}… que n8n remplit."],
    ["Variable {{1}}", "Un trou dans le modèle. Exemple : {{1}} devient « Jean », {{2}} devient « 0812345678 »."],
    ["Token (jeton)", "Un très long mot de passe qui permet à n8n d'envoyer des WhatsApp au nom de l'entreprise. Secret."],
    ["WABA ID", "Le numéro d'identité du compte WhatsApp Business (WhatsApp Business Account ID)."],
    ["Phone number ID", "Le numéro d'identité du numéro qui envoie les messages. n8n le trouve tout seul."],
  ], { colW: [3.0, 9.13], rowH: 0.72, fs: 15 });

  // =============== 7. Avant de commencer ===============
  s = content("Avant de commencer : ce qu'il te faut");
  const need = [
    ["Les comptes", HEX.navy, [["SiGoogledrive", "Un compte Google (Gmail)", "pour Google Drive et Google Sheets"], ["FaProjectDiagram", "Un compte n8n", "sur n8n.cloud (adresse du type tonnom.app.n8n.cloud)"], ["SiMeta", "Un compte Facebook", "relié au portefeuille Meta Business de l'entreprise"]]],
    ["Le matériel", HEX.wa, [["FaLaptop", "Un ordinateur", "avec Chrome, c'est plus confortable que le téléphone"], ["FaMobileAlt", "Un téléphone avec WhatsApp", "pour recevoir les messages de test"], ["FaFolderOpen", "Le kit de fichiers", "dossier automatisation-n8n (slide suivante)"]]],
  ];
  for (let c = 0; c < 2; c++) {
    const x = M + c * 6.15;
    card(s, x, 1.55, 5.9, 5.1);
    T(s, need[c][0], { x: x + 0.35, y: 1.75, w: 5, h: 0.5, fontSize: 20, bold: true, color: need[c][1] });
    for (let i = 0; i < 3; i++) {
      const yy = 2.45 + i * 1.35;
      await circleIcon(s, x + 0.35, yy, 0.8, need[c][2][i][0], need[c][1]);
      T(s, [{ text: need[c][2][i][1], options: { bold: true, breakLine: true } }, { text: need[c][2][i][2], options: { color: HEX.ink2 } }], { x: x + 1.35, y: yy - 0.05, w: 4.3, h: 1.0, fontSize: 15, valign: "middle" });
    }
  }

  // =============== 8. Le kit de fichiers ===============
  s = content("Le kit de fichiers");
  table(s, ["Fichier", "À quoi il sert"], [
    ["gestion_de_stock_auto.xlsx", "Le tableau de stock à mettre dans Google Drive (étape 1)"],
    ["workflow_1_commande_alerte_stock.json", "Le workflow Stock 1 à importer dans n8n"],
    ["workflow_2_bilan_du_soir.json", "Le workflow Stock 2"],
    ["workflow_3_arrivage_marchandise.json", "Le workflow Stock 3"],
    ["workflow_4_point_du_matin.json", "Le workflow Stock 4"],
    ["modeles_whatsapp_meta.md", "Les textes des 6 messages WhatsApp à faire valider par Meta (à copier-coller)"],
    ["systeme_gestion_stock_automatise.pdf", "Le PDF qui explique le système au client"],
  ], { colW: [4.7, 7.43], rowH: 0.5, fs: 14 });
  await callout(s, M, 5.85, W - 2 * M, 0.8, "err", "n'importe jamais le dossier « ancienne-version-telegram-NE-PAS-IMPORTER ». C'est une vieille version.");

  // =============== ÉTAPE 1 ===============
  await section(1, "Le Google Sheet", "Mettre le tableau de stock en ligne, pour que n8n puisse le lire et y écrire.", HEX.google, "SiGooglesheets");

  s = content("Mettre le tableau dans Google Drive", ["ÉTAPE 1 · SHEETS", HEX.google]);
  steps(s, [
    ["Ouvre drive.google.com", "avec le compte Google du client (ou le tien pour t'entraîner)."],
    ["Nouveau → Importer un fichier", "et choisis gestion_de_stock_auto.xlsx."],
    ["Ouvre le fichier, puis Fichier → Enregistrer au format Google Sheets.", ""],
    ["Une nouvelle version s'ouvre.", "C'est celle-là qu'on utilise, pas le .xlsx."],
    ["Vérifie les 6 onglets en bas de l'écran", "(voir à droite)."],
    ["Copie le lien de la barre d'adresse", "(docs.google.com/spreadsheets/d/…) et garde-le dans une note."],
  ], { w: 6.9, color: HEX.google });
  windowFrame(s, 7.85, 1.6, 4.9, 3.0, "docs.google.com/spreadsheets/d/…");
  for (let r = 0; r < 4; r++) for (let c = 0; c < 4; c++) s.addShape(pres.shapes.RECTANGLE, { x: 8.0 + c * 1.15, y: 2.15 + r * 0.38, w: 1.15, h: 0.38, fill: { color: r === 0 ? "E6F4EA" : HEX.white }, line: { color: HEX.line, width: 0.5 } });
  const tabs = ["Mode d'emploi", "Tableau de bord", "Produits", "Commandes", "Arrivages", "Mouvements"];
  tabs.forEach((t, i) => {
    const xx = 7.95 + (i % 3) * 1.6, yy = 3.8 + Math.floor(i / 3) * 0.38;
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: xx, y: yy, w: 1.52, h: 0.32, fill: { color: i >= 2 && i <= 4 ? "E6F4EA" : "F1F3F7" }, line: { color: HEX.line, width: 0.5 }, rectRadius: 0.05 });
    T(s, t, { x: xx, y: yy, w: 1.52, h: 0.32, fontSize: 10, align: "center", valign: "middle", bold: i >= 2 && i <= 4 });
  });
  await callout(s, 7.85, 4.85, 4.9, 1.9, "warn", "si plus tard n8n te montre seulement « Sheet1 », c'est que tu as copié le lien du fichier .xlsx. Reprends le lien de la version Google Sheets.");

  s = content("Ce que contient le tableau", ["ÉTAPE 1 · SHEETS", HEX.google]);
  table(s, ["Onglet", "Qui le remplit", "Ce qu'on y trouve"], [
    ["Produits", "toi, avec le client, au départ", "code (P001, P002…), nom, prix d'achat et de vente, stock de départ, seuil d'alerte, fournisseur. Le stock actuel se calcule tout seul."],
    ["Commandes", "n8n (Stock 1)", "une ligne par vente : date, client, téléphone, produit, quantité, montant, statut"],
    ["Arrivages", "n8n (Stock 3)", "une ligne par livraison du fournisseur"],
    ["Mouvements", "à la main, si besoin", "les corrections : casse, perte, retour"],
    ["Tableau de bord", "les formules", "les chiffres clés et les alertes, rien à remplir"],
  ], { colW: [2.2, 3.0, 6.93], rowH: [0.5, 0.75, 0.55, 0.55, 0.55, 0.55], fs: 14, color: HEX.google });
  await callout(s, M, 5.3, 5.95, 1.4, "rule", "ne renomme jamais un onglet ni un titre de colonne. n8n les retrouve par leur nom.");
  await callout(s, 6.78, 5.3, 5.95, 1.4, "tip", "supprime les lignes « EXEMPLE » et remplis les vrais produits avec le client. Une vente au statut « Annulée » ne compte plus.");

  // =============== ÉTAPE 2 ===============
  await section(2, "n8n : importer et connecter", "Mettre les 4 automatisations dans n8n et les relier au Google Sheet. Premier test sans WhatsApp.", HEX.n8n, "FaProjectDiagram");

  s = content("Importer les 4 workflows", ["ÉTAPE 2 · N8N", HEX.n8n]);
  steps(s, [
    ["Connecte-toi à ton espace n8n", "(ex. tonnom.app.n8n.cloud)."],
    ["Clique sur Create workflow :", "une page vide s'ouvre."],
    ["En haut à droite : … → Import from file", "et choisis workflow_1_commande_alerte_stock.json."],
    ["Renomme-le « Stock 1 »", "(clic sur le nom en haut à gauche), puis Ctrl+S."],
    ["Retourne à l'accueil et recommence", "pour les 3 autres fichiers : Stock 2, Stock 3, Stock 4."],
  ], { w: 6.9, color: HEX.n8n });
  card(s, 7.85, 1.6, 4.88, 2.9, HEX.n8n);
  T(s, "RÈGLE D'OR", { x: 8.2, y: 1.85, w: 4, h: 0.4, fontSize: 14, bold: true, color: HEX.white, charSpacing: 3 });
  T(s, "Une page vide = un fichier", { x: 8.2, y: 2.3, w: 4.3, h: 0.9, fontSize: 26, bold: true, color: HEX.white });
  T(s, "Jamais deux fichiers dans la même page.", { x: 8.2, y: 3.4, w: 4.3, h: 0.8, fontSize: 15, color: HEX.white });
  await callout(s, 7.85, 4.75, 4.88, 1.95, "err", "si tu vois des nœuds qui finissent par « 1 » (ex. « Lire les produits1 »), deux fichiers sont dans la même page. Supprime la page et réimporte proprement.");

  s = content("À quoi ressemble Stock 1", ["ÉTAPE 2 · N8N", HEX.n8n]);
  const types = { trig: ["9AA6C2", "Déclencheur"], gs: [HEX.google, "Google Sheets"], code: [HEX.n8n, "Calcul"], wa: [HEX.wa, "WhatsApp"], cond: ["6B4FBB", "Condition"] };
  const nodes = [["Formulaire de commande", "trig"], ["Lire les produits", "gs"], ["Préparer la commande", "code"], ["Ajouter dans Commandes", "gs"], ["WhatsApp patron : nouvelle commande", "wa"], ["WhatsApp client : confirmation", "wa"], ["Stock bas ?", "cond"], ["WhatsApp patron : alerte stock", "wa"]];
  const pos = (i) => [M + 0.2 + (i % 4) * 3.1, i < 4 ? 1.75 : 3.75];
  nodes.forEach((n, i) => {
    const [x, y] = pos(i);
    const col = types[n[1]][0];
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y, w: 2.55, h: 1.3, fill: { color: HEX.white }, line: { color: col, width: 2.5 }, rectRadius: 0.12, objectName: "nœud " + n[0] });
    s.addShape(pres.shapes.OVAL, { x: x + 0.15, y: y + 0.15, w: 0.34, h: 0.34, fill: { color: col }, line: { color: col } });
    T(s, String(i + 1), { x: x + 0.15, y: y + 0.15, w: 0.34, h: 0.34, fontSize: 11, bold: true, color: HEX.white, align: "center", valign: "middle" });
    T(s, n[0], { x: x + 0.15, y: y + 0.55, w: 2.25, h: 0.7, fontSize: 13, bold: true });
    if (i % 4 < 3) arrow(s, x + 2.58, y + 0.65, x + 3.07, y + 0.65, HEX.navy);
  });
  arrow(s, pos(3)[0] + 1.27, 3.08, pos(3)[0] + 1.27, 3.72, HEX.navy);
  T(s, "puis on continue sur la ligne du bas", { x: 9.45, y: 3.12, w: 3.3, h: 0.5, fontSize: 11, color: HEX.gray });
  Object.values(types).forEach((t, i) => {
    const x = M + 0.2 + i * 2.45;
    s.addShape(pres.shapes.OVAL, { x, y: 5.5, w: 0.3, h: 0.3, fill: { color: t[0] }, line: { color: t[0] } });
    T(s, t[1], { x: x + 0.42, y: 5.45, w: 1.9, h: 0.4, fontSize: 14, valign: "middle" });
  });
  T(s, "Le vendeur remplit le formulaire (1). n8n lit les produits (2), calcule (3), écrit la vente (4), prévient le patron (5) et le client (6). Si le stock est bas (7), le patron reçoit une alerte (8).", { x: M + 0.2, y: 6.0, w: 12, h: 0.8, fontSize: 14, color: HEX.ink2 });

  s = content("Connecter Google Sheets", ["ÉTAPE 2 · N8N", HEX.n8n]);
  steps(s, [
    ["Double-clique sur le nœud « Lire les produits ».", ""],
    ["Credential → Create new credential", "→ Sign in with Google → choisis le compte → autorise."],
    ["Document : By URL", "→ colle le lien du Google Sheet."],
    ["Sheet : passe de « By Name » à From list", "→ choisis l'onglet (tableau à droite)."],
    ["Dans les nœuds « Ajouter dans… » :", "Mapping Column Mode = Map Automatically."],
    ["Même chose dans chaque nœud Google Sheets", "des 4 workflows (même connexion, même lien)."],
  ], { w: 6.3, color: HEX.n8n, fs: 14 });
  table(s, ["Workflow", "Nœud", "Onglet"], [
    ["Stock 1", "Lire les produits", "Produits"],
    ["Stock 1", "Ajouter dans Commandes", "Commandes"],
    ["Stock 2", "Lire les commandes", "Commandes"],
    ["Stock 2", "Lire les produits", "Produits"],
    ["Stock 3", "Lire les produits", "Produits"],
    ["Stock 3", "Ajouter dans Arrivages", "Arrivages"],
    ["Stock 4", "Lire les produits", "Produits"],
  ], { x: 7.2, y: 1.55, w: 5.53, colW: [1.25, 2.73, 1.55], rowH: 0.44, fs: 13, color: HEX.google });
  await callout(s, 7.2, 5.25, 5.53, 1.45, "warn", "dans « Lire les produits », ne supprime pas l'option Range A4:P204 (dans Options). Sans elle, n8n lit mal le tableau.");

  s = content("Premier test, sans WhatsApp", ["ÉTAPE 2 · N8N", HEX.n8n]);
  steps(s, [
    ["Dans Stock 1, sélectionne les 3 nœuds WhatsApp et appuie sur D.", "Ils deviennent gris : ils sont en pause."],
    ["Ctrl+S, puis clique sur Execute workflow.", ""],
    ["Le formulaire s'ouvre :", "client Jean, ton numéro, code produit P002, quantité 2 → Envoyer."],
    ["Ouvre le Google Sheet", "et vérifie le résultat (à droite)."],
  ], { w: 6.6, color: HEX.n8n, rowH: 1.0 });
  card(s, 7.6, 1.6, 5.13, 5.05, "E8F5EC");
  T(s, "Résultat attendu", { x: 7.95, y: 1.85, w: 4.5, h: 0.5, fontSize: 20, bold: true, color: HEX.google });
  const exp = ["Une nouvelle ligne « Jean » dans l'onglet Commandes", "Dans Produits, le stock de P002 (Huile 5 L) passe de 10 à 8", "Dans n8n, les nœuds actifs sont verts"];
  for (let i = 0; i < exp.length; i++) {
    s.addImage({ data: await icon("FaCheckCircle", HEX.google), x: 7.95, y: 2.55 + i * 1.1, w: 0.42, h: 0.42, altText: "ok" });
    T(s, exp[i], { x: 8.55, y: 2.5 + i * 1.1, w: 3.95, h: 0.95, fontSize: 15 });
  }
  T(s, "Un nœud rouge ? Clique dessus, lis le message, va au dépannage.", { x: 7.95, y: 5.85, w: 4.5, h: 0.6, fontSize: 13, color: HEX.ink2, italic: true });

  // =============== ÉTAPE 3 ===============
  await section(3, "Meta : ouvrir l'accès WhatsApp", "Créer l'app Meta, recevoir le premier message, écrire les modèles et obtenir le token.", HEX.meta, "SiMeta");

  s = content("Créer l'app Meta", ["ÉTAPE 3 · META", HEX.meta]);
  steps(s, [
    ["Va sur developers.facebook.com", "et connecte-toi avec Facebook."],
    ["Mes applications → Créer une app.", ""],
    ["Cas d'utilisation :", "« Se connecter avec les clients via WhatsApp »."],
    ["Relie l'app au portefeuille business", "de l'entreprise (pour nous : ADigitalGround)."],
    ["Dans l'app, choisis « Intégrer avec l'API »", "puis « Étape 1. Faites un essai »."],
  ], { w: 6.9, color: HEX.meta });
  windowFrame(s, 7.85, 1.6, 4.88, 2.7, "developers.facebook.com/apps");
  card(s, 8.1, 2.2, 4.38, 1.85, "F6F8FC");
  T(s, [{ text: "Allegra business", options: { bold: true, breakLine: true, fontSize: 15 } }, { text: "Mode : En développement", options: { breakLine: true } }, { text: "Entreprise : ADigitalGround", options: { color: HEX.meta } }], { x: 8.35, y: 2.35, w: 4, h: 1.6, fontSize: 13 });
  await callout(s, 7.85, 4.55, 4.88, 2.1, "tip", "si l'entreprise a déjà une app (comme « Allegra business »), utilise-la. N'en crée pas une deuxième.");

  s = content("Le numéro de test et le « Hello World »", ["ÉTAPE 3 · META", HEX.meta]);
  steps(s, [
    ["Sur « Faites un essai », Meta te donne un numéro de test gratuit", "(+1 555…)."],
    ["Dans le champ « À », ajoute ton numéro +243…", "et tape le code reçu."],
    ["Clique sur Envoyer le message :", "tu reçois « Hello World » sur WhatsApp."],
  ], { w: 5.6, color: HEX.meta, rowH: 1.1 });
  table(s, ["Numéro à noter", "Où le trouver", "À quoi il sert"], [
    ["WhatsApp Business Account ID (WABA ID)", "page « Configuration de l'API », ou Paramètres Business → Comptes WhatsApp", { text: "à coller dans n8n (étape 4)", options: { bold: true, color: HEX.meta } }],
    ["Phone number ID", "même page, juste au-dessus", "rien à copier : n8n le propose tout seul"],
  ], { x: 6.5, y: 1.6, w: 6.23, colW: [2.0, 2.33, 1.9], rowH: [0.55, 1.15, 0.8], fs: 13, color: HEX.meta });
  await callout(s, 6.5, 5.1, 6.23, 1.3, "warn", "le numéro de test n'envoie qu'à des numéros vérifiés (5 au maximum). Parfait pour tester, pas pour un client.");
  await callout(s, M, 5.0, 5.6, 1.1, "tip", "pas de Hello World ? Vérifie que ton numéro est bien validé dans « À ».");

  s = content("Créer un modèle de message", ["ÉTAPE 3 · META", HEX.meta]);
  steps(s, [
    ["WhatsApp Manager → Modèles de message → Créer un modèle", "(business.facebook.com/wa/manage/message-templates)."],
    ["En haut, vérifie le compte :", "Test WhatsApp Business Account."],
    ["Catégorie Utilitaire, type Par défaut", "→ Suivant."],
    ["Nom exact (minuscules et tiret bas), langue Français.", ""],
    ["Type de variable : Valeur numérique.", "Titre sans variable. Colle le texte dans le Corps."],
    ["Un exemple pour chaque {{1}}, {{2}}…", "puis Soumettre à examen."],
  ], { w: 7.0, color: HEX.meta, fs: 14 });
  card(s, 7.9, 1.6, 4.83, 5.05, "FFF4D6");
  T(s, "Règles d'or", { x: 8.2, y: 1.8, w: 4, h: 0.5, fontSize: 20, bold: true, color: HEX.amber });
  const rules = [["FaCheckCircle", HEX.google, "Toujours Utilitaire, jamais Marketing"], ["FaCheckCircle", HEX.google, "Aucun bouton"], ["FaCheckCircle", HEX.google, "Pas de variable dans le titre"], ["FaCheckCircle", HEX.google, "Le nom exactement comme dans le fichier"], ["FaTimesCircle", HEX.red, "Pas de mots qui sonnent « pub » (ex. « recommander ») : Meta passe le modèle en Marketing, plus cher"]];
  for (let i = 0; i < rules.length; i++) {
    const yy = 2.4 + i * 0.68;
    s.addImage({ data: await icon(rules[i][0], rules[i][1]), x: 8.2, y: yy + 0.04, w: 0.32, h: 0.32, altText: "règle" });
    T(s, rules[i][2], { x: 8.65, y: yy, w: 3.85, h: i === 4 ? 1.2 : 0.6, fontSize: 14 });
  }

  s = content("Les 6 modèles à créer", ["ÉTAPE 3 · META", HEX.meta]);
  table(s, ["Nom du modèle", "Utilisé par", "Variables", "Envoyé à"], [
    ["nouvelle_commande", "Stock 1", "7", "patron"],
    ["confirmation_commande", "Stock 1", "4", "client"],
    ["alerte_stock_bas", "Stock 1", "5", "patron"],
    ["bilan_du_soir", "Stock 2", "7", "patron"],
    ["arrivage_stock", "Stock 3", "4", "patron"],
    ["stock_du_matin", "Stock 4", "4", "patron"],
  ], { w: 7.3, colW: [2.9, 1.5, 1.4, 1.5], rowH: 0.58, fs: 14, color: HEX.meta });
  T(s, "Les textes complets et les exemples sont dans modeles_whatsapp_meta.md : copie-colle, ne retape pas.", { x: M, y: 5.85, w: 7.3, h: 0.8, fontSize: 14, color: HEX.ink2 });
  card(s, 8.3, 1.55, 4.43, 5.1, "E7F6EF");
  T(s, "Ce que reçoit le patron", { x: 8.55, y: 1.7, w: 4, h: 0.4, fontSize: 13, bold: true, color: HEX.wa });
  bubble(s, 8.55, 2.2, 3.93, 2.0, "Nouvelle commande", "Nouvelle commande reçue. Client : Jean (0810000000). Produit : Riz 25 kg, quantité 2. Montant : 72. Adresse : Gombe. Stock restant : 18 sacs. Bonne journée !");
  T(s, "Exemple avec les valeurs de test : n8n met « Jean », « Riz 25 kg »… à la place de {{1}}, {{2}}…", { x: 8.55, y: 4.45, w: 3.93, h: 1.5, fontSize: 12, color: HEX.ink2 });

  s = content("Le token permanent", ["ÉTAPE 3 · META", HEX.meta]);
  steps(s, [
    ["business.facebook.com/settings → Utilisateurs système → Ajouter :", "nom n8n, rôle Admin."],
    ["Assigner des éléments → Applications →", "ton app → Contrôle total."],
    ["Assigner des éléments → Comptes WhatsApp →", "Test WhatsApp Business Account → Contrôle total."],
    ["Générer un token → ton app →", "expiration : Jamais."],
    ["Coche whatsapp_business_messaging et whatsapp_business_management", "→ Générer."],
    ["Copie le token dans une note privée :", "il ne s'affiche qu'une seule fois."],
  ], { w: 7.0, color: HEX.meta, fs: 14 });
  await callout(s, 7.9, 1.6, 4.83, 1.95, "err", "« Aucune autorisation disponible » = l'étape 2 est oubliée. Ou passe par Comptes → Applications → ton app → Assigner des personnes → n8n.");
  await callout(s, 7.9, 3.7, 4.83, 1.4, "warn", "ne choisis jamais le compte « Application WhatsApp Business » : c'est le WhatsApp du téléphone.");
  await callout(s, 7.9, 5.25, 4.83, 1.4, "key", "le token est un mot de passe. Jamais dans un groupe, jamais sur une capture d'écran.");

  // =============== ÉTAPE 4 ===============
  await section(4, "Brancher WhatsApp dans n8n", "Relier n8n à WhatsApp, régler chaque nœud, faire le grand test et mettre en service.", HEX.wa, "FaWhatsapp");

  s = content("Créer la connexion WhatsApp dans n8n", ["ÉTAPE 4 · WHATSAPP", HEX.wa]);
  steps(s, [
    ["Ouvre un nœud WhatsApp", "(s'il est gris : sélectionne-le et appuie sur D)."],
    ["Credential to connect with →", "+ Create new credential."],
    ["Access Token = le token", "Business Account ID = le WABA ID."],
    ["Clique sur Save :", "message vert « Connection tested successfully »."],
  ], { w: 6.4, color: HEX.wa, rowH: 1.0 });
  windowFrame(s, 7.4, 1.6, 5.33, 3.6, "WhatsApp API · n8n");
  [["Access Token", "••••••••••••••••••••"], ["Business Account ID", "123456789012345"]].forEach((f, i) => {
    T(s, f[0], { x: 7.7, y: 2.2 + i * 1.1, w: 4.7, h: 0.3, fontSize: 13, bold: true });
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: 7.7, y: 2.55 + i * 1.1, w: 4.73, h: 0.45, fill: { color: "F6F8FC" }, line: { color: HEX.line }, rectRadius: 0.06 });
    T(s, f[1], { x: 7.85, y: 2.55 + i * 1.1, w: 4.4, h: 0.45, fontSize: 13, color: HEX.gray, valign: "middle" });
  });
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: 7.7, y: 4.55, w: 4.73, h: 0.45, fill: { color: "E6F4EA" }, line: { color: "E6F4EA" }, rectRadius: 0.06 });
  T(s, "✓ Connection tested successfully", { x: 7.85, y: 4.55, w: 4.4, h: 0.45, fontSize: 13, bold: true, color: HEX.google, valign: "middle" });
  T(s, "(valeurs fictives)", { x: 7.4, y: 5.3, w: 5.33, h: 0.3, fontSize: 11, color: HEX.gray, italic: true });
  await callout(s, M, 5.75, 12.13, 0.9, "tip", "pour les autres nœuds WhatsApp, choisis simplement cette connexion dans la liste. On ne la crée qu'une fois.");

  s = content("Régler chaque nœud WhatsApp", ["ÉTAPE 4 · WHATSAPP", HEX.wa]);
  table(s, ["Champ", "Quoi mettre"], [
    ["Credential", "la connexion WhatsApp créée juste avant"],
    ["Operation", "Send Template (déjà réglé, ne touche pas)"],
    ["Sender Phone Number", "le numéro de test (+1 555…), choisi dans la liste"],
    ["Recipient's Phone Number", "le numéro du patron au format 2438XXXXXXXX (sans + ni espace ni 0 devant)"],
    ["Template", "le nom du modèle (slide « Les 6 modèles »), à choisir dans la liste une fois Actif"],
    ["Paramètres {{1}}, {{2}}…", "ne touche à rien : ils sont déjà branchés"],
  ], { colW: [3.2, 8.93], rowH: [0.5, 0.55, 0.55, 0.55, 0.55, 0.55, 0.55], fs: 15, color: HEX.wa });
  await callout(s, M, 5.6, 12.13, 1.05, "warn", "exception : dans « WhatsApp client : confirmation », ne touche pas au destinataire. Il prend tout seul le téléphone tapé dans le formulaire.");

  s = content("Le grand test", ["ÉTAPE 4 · WHATSAPP", HEX.wa]);
  steps(s, [
    ["Dans WhatsApp Manager, vérifie que les modèles sont « Actif »", "(vert). « En cours d'examen » = il faut attendre."],
    ["Réactive les nœuds WhatsApp (touche D), Ctrl+S.", ""],
    ["Execute workflow →", "Jean, TON numéro, P002, 2 → Envoyer."],
    ["Regarde ton téléphone", "et le Google Sheet."],
  ], { w: 6.6, color: HEX.wa, rowH: 1.0 });
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: 8.3, y: 1.45, w: 3.7, h: 5.35, fill: { color: HEX.navy }, line: { color: HEX.navy }, rectRadius: 0.35, objectName: "téléphone" });
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: 8.45, y: 1.65, w: 3.4, h: 4.95, fill: { color: "ECE5DD" }, line: { color: "ECE5DD" }, rectRadius: 0.2, objectName: "écran" });
  bubble(s, 8.6, 1.95, 3.1, 1.75, "Nouvelle commande", "Nouvelle commande reçue. Client : Jean (0812…). Produit : Huile 5 L, quantité 2. Stock restant : 8…");
  bubble(s, 8.6, 3.95, 3.1, 1.5, "Commande confirmée", "Bonjour Jean, votre commande est bien enregistrée : Huile 5 L, quantité 2…");
  T(s, "Exemple de messages reçus (textes raccourcis)", { x: 8.3, y: 6.82, w: 3.7, h: 0.25, fontSize: 10, color: HEX.gray, align: "center" });

  s = content("Mettre en service", ["ÉTAPE 4 · WHATSAPP", HEX.wa]);
  const svc = [
    ["FaPlug", HEX.wa, "Activer", "En haut de chaque workflow, mets l'interrupteur sur Active (ou clique sur Publish). Fais-le pour les 4."],
    ["FaLink", HEX.n8n, "Donner les formulaires", "Dans le nœud « Formulaire de commande », copie la Production URL. Envoie-la au vendeur sur WhatsApp. Même chose pour le formulaire « Arrivage » au magasinier."],
    ["FaClock", HEX.navy, "Laisser tourner", "Stock 2 (19 h) et Stock 4 (8 h) partent tout seuls, à l'heure de Kinshasa. Rien à faire."],
  ];
  for (let i = 0; i < 3; i++) {
    const x = M + i * 4.1;
    card(s, x, 1.6, 3.85, 3.65);
    await circleIcon(s, x + 0.35, 1.9, 0.85, svc[i][0], svc[i][1]);
    T(s, svc[i][2], { x: x + 0.35, y: 2.95, w: 3.2, h: 0.5, fontSize: 19, bold: true });
    T(s, svc[i][3], { x: x + 0.35, y: 3.5, w: 3.2, h: 1.7, fontSize: 14, color: HEX.ink2 });
  }
  await callout(s, M, 5.55, 12.13, 1.1, "warn", "le lien de test (Test URL) ne marche que pendant que tu cliques sur Execute workflow. Le vendeur doit recevoir la Production URL, sinon ses ventes ne partent nulle part.");

  // =============== Dépannage ===============
  curSection = "Dépannage et check-list";
  pres.addSection({ title: curSection });
  s = content("Dépannage : Google Sheets et n8n");
  table(s, ["Ce que tu vois", "Pourquoi", "La solution"], [
    ["« Parameter \"Sheet\" is required »", "l'onglet n'est pas choisi dans le nœud", "Sheet → From list → choisis l'onglet (Produits, Commandes…)"],
    ["La liste ne montre que « Sheet1 »", "le lien est celui du fichier .xlsx", "Fichier → Enregistrer au format Google Sheets, puis recolle le nouveau lien"],
    ["Des nœuds finissent par « 1 »", "deux fichiers importés dans la même page", "supprime la page, réimporte : une page vide par fichier"],
    ["Pas de nouvelle ligne dans le Sheet", "mauvais lien, ou onglet renommé", "vérifie le lien et le nom exact des onglets"],
    ["Le vendeur envoie, rien ne se passe", "workflow pas activé, ou Test URL au lieu de Production URL", "active le workflow, renvoie la Production URL"],
  ], { colW: [3.6, 3.9, 4.63], rowH: [0.55, 0.85, 0.85, 0.85, 0.85, 0.85], fs: 14, color: HEX.n8n });

  s = content("Dépannage : Meta et WhatsApp");
  table(s, ["Ce que tu vois", "Pourquoi", "La solution"], [
    ["« Aucune autorisation disponible » (token)", "l'app n'est pas assignée à l'utilisateur système", "Assigner des éléments → Applications → ton app → Contrôle total"],
    ["Modèle classé « Marketing » (triangle)", "un mot du texte sonne comme de la pub", "crée un nouveau modèle, autre nom, texte neutre, et change le nom dans n8n"],
    ["Modèle « En cours d'examen »", "Meta n'a pas encore validé", "attends (quelques minutes à 24 h)"],
    ["Le client ne reçoit rien pendant les tests", "son numéro n'est pas vérifié chez Meta", "teste avec ton numéro, ou ajoute le sien dans « À »"],
    ["Le nœud WhatsApp est rouge", "token expiré, mauvais WABA ID ou modèle pas actif", "lis le message d'erreur, vérifie ces 3 points dans l'ordre"],
  ], { colW: [3.6, 3.9, 4.63], rowH: [0.55, 0.85, 0.85, 0.85, 0.85, 0.85], fs: 14, color: HEX.meta });

  // =============== Check-list ===============
  s = content("Check-list finale");
  const cl = [
    ["Google Sheet", HEX.google, ["Version Google Sheets (pas .xlsx)", "6 onglets présents, noms inchangés", "Lignes EXEMPLE supprimées, vrais produits saisis"]],
    ["n8n", HEX.n8n, ["4 workflows, chacun sur sa page", "Tous les nœuds Sheets connectés au bon onglet", "Premier test OK : ligne ajoutée, stock baissé"]],
    ["Meta", HEX.meta, ["Hello World reçu", "6 modèles « Actif » en Utilitaire", "Token permanent copié en lieu sûr"]],
    ["WhatsApp + mise en service", HEX.wa, ["Grand test OK : messages reçus", "4 workflows activés", "Production URL envoyées au vendeur et au magasinier"]],
  ];
  for (let i = 0; i < 4; i++) {
    const x = M + (i % 2) * 6.15, y = 1.55 + Math.floor(i / 2) * 2.62;
    card(s, x, y, 5.9, 2.42);
    T(s, cl[i][0], { x: x + 0.3, y: y + 0.18, w: 5.3, h: 0.45, fontSize: 18, bold: true, color: cl[i][1] });
    for (let j = 0; j < 3; j++) {
      s.addImage({ data: await icon("FaRegSquare", cl[i][1]), x: x + 0.3, y: y + 0.78 + j * 0.5, w: 0.3, h: 0.3, altText: "case à cocher" });
      T(s, cl[i][2][j], { x: x + 0.75, y: y + 0.72 + j * 0.5, w: 5.0, h: 0.42, fontSize: 15, valign: "middle" });
    }
  }

  // =============== Chez un vrai client ===============
  s = content("Chez un vrai client : ce qui change");
  const real = [
    ["FaMobileAlt", "Un vrai numéro WhatsApp", "Un numéro qui n'est pas déjà utilisé dans l'appli WhatsApp. Le numéro de test ne suffit plus."],
    ["FaIdCard", "La vérification de l'entreprise", "Chez Meta : Paramètres Business → Commencer la vérification. Il faut les documents de l'entreprise."],
    ["FaCreditCard", "Un moyen de paiement chez Meta", "Meta facture chaque message envoyé avec un modèle. Vérifie le tarif du moment avant de fixer ton prix."],
    ["FaFileSignature", "L'accord écrit du client", "Avant d'installer quoi que ce soit, et avant toute publication. Toujours."],
  ];
  for (let i = 0; i < 4; i++) {
    const x = M + (i % 2) * 6.15, y = 1.55 + Math.floor(i / 2) * 2.62;
    card(s, x, y, 5.9, 2.42);
    await circleIcon(s, x + 0.3, y + 0.3, 0.8, real[i][0], HEX.navy, HEX.yellow);
    T(s, real[i][1], { x: x + 1.3, y: y + 0.3, w: 4.4, h: 0.8, fontSize: 17, bold: true, valign: "middle" });
    T(s, real[i][2], { x: x + 0.3, y: y + 1.25, w: 5.3, h: 1.05, fontSize: 14, color: HEX.ink2 });
  }

  // =============== Fin ===============
  s = pres.addSlide({ masterName: "COUVERTURE", sectionTitle: curSection });
  if (LOGO) s.addImage({ path: LOGO, x: M, y: 0.6, w: 1.6, h: 1.27, altText: "Logo Allegra Digital Ground" });
  T(s, "BRAVO", { x: M, y: 2.05, w: 6, h: 0.4, fontSize: 14, bold: true, color: HEX.yellow, charSpacing: 4 });
  s.addText("Tu sais installer le système de A à Z", { placeholder: "title" });
  s.addText("Refais une installation complète seul, sur ton propre compte, avant ta première installation chez un client.", { placeholder: "body" });
  await circleIcon(s, 10.3, 2.4, 2.2, "FaRocket", HEX.yellow, HEX.navy);

  await pres.writeFile({ fileName: OUT });
  await applyTheme(OUT, THEME);
  console.log("ok", OUT);
})().catch((e) => { console.error(e); process.exit(1); });
