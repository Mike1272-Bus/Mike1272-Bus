from PIL import Image, ImageDraw, ImageFont
import os

HERE = os.path.dirname(os.path.abspath(__file__))
CF = "/root/.claude/skills/synced/e026b770-e89c-4483-b66d-20d65ff8a59c_b603504e-56cc-43ac-8018-db062e692acb/canvas-design/canvas-fonts/"
BALOO = "/home/user/Mike1272-Bus/preview-style-alight/assets/Baloo2-ExtraBold.ttf"

W, H = 1620, 2880
M = 96
CREAM = (251, 246, 238)
GRID = (231, 225, 214)
INK = (17, 17, 17)
ORANGE = (255, 92, 0)
ORANGE_TXT = (201, 66, 0)
YELLOW = (255, 214, 10)
WHITE = (255, 255, 255)
MUTED = (110, 104, 96)


def f(path, size):
    return ImageFont.truetype(path, size)


baloo = lambda s: f(BALOO, s)
sans = lambda s: f(CF + "InstrumentSans-Regular.ttf", s)
sansb = lambda s: f(CF + "InstrumentSans-Bold.ttf", s)
mono = lambda s: f(CF + "GeistMono-Regular.ttf", s)
monob = lambda s: f(CF + "GeistMono-Bold.ttf", s)

TYPES = {
    "VIDÉO": {"label": "EXTRAIT VIDÉO", "fill": ORANGE, "text": WHITE},
    "IMAGE": {"label": "IMAGE", "fill": INK, "text": WHITE},
    "MOTION": {"label": "MOTION DESIGN", "fill": YELLOW, "text": INK},
}

RATE = 2.64  # mots par seconde, mesuré sur la première voix ElevenLabs

SEG = [
    ("HOOK", "VIDÉO", "Vous avez déjà un savoir-faire qui vaut de l'argent.",
     "3 ou 4 plans très courts de mains au travail (cuisine, couture, écriture, calcul) dans des cartes inclinées. Badge orange « VAUT DE L'ARGENT ».",
     "whoosh, pop sur chaque carte, scintillement"),
    ("HOOK", "MOTION", "Vous ne le savez juste pas encore.",
     "Les cartes se retournent en 3D et montrent un « ? ».",
     "whoosh"),
    ("PROMESSE", "MOTION", "Je vais vous expliquer exactement pourquoi, dans quelques secondes.",
     "Couverture de l'ebook qui pivote en 3D et minuteur qui se remplit, comme dans l'aperçu validé.",
     "montée en tension"),
    ("PARTIE 1", "IMAGE", "Que vous soyez salarié, étudiant, ou sans emploi,",
     "3 portraits dans des cartes qui tombent l'une après l'autre : salarié, étudiante, personne sans emploi.",
     "impact grave à l'entrée, pop sur chaque carte"),
    ("PARTIE 1", "VIDÉO", "vous savez faire quelque chose : cuisiner, coudre, parler une langue, tenir une comptabilité.",
     "4 extraits dans 4 cartes en cascade, une par compétence, avec une étiquette noire sur chacune.",
     "pop sur chaque carte"),
    ("PARTIE 1", "MOTION", "Et quelqu'un, quelque part, a besoin d'apprendre exactement ça.",
     "Un point lumineux trace une ligne jusqu'à un autre point : une connexion à distance.",
     "ping"),
    ("BOUCLE 1", "MOTION", "Et pourtant... ce n'est même pas la partie la plus folle.",
     "Texte seul, en très gros, sur le quadrillage vide. La musique se coupe.",
     "impact grave"),
    ("PARTIE 2", "VIDÉO", "Avec un produit digital, vous pouvez le lui enseigner à des milliers de kilomètres, sans jamais le rencontrer.",
     "Extrait : une personne qui donne un cours en appel vidéo. Badge « À DES MILLIERS DE KM ».",
     "whoosh cinématique"),
    ("PARTIE 2", "VIDÉO", "Mon oncle David, menuisier, a transformé son savoir-faire en produit digital, sans budget pub.",
     "Mains de menuisier qui travaillent le bois, idéalement une vraie vidéo de David. Badge « SANS BUDGET PUB ».",
     "carillon"),
    ("BOUCLE 2", "MOTION", "Mais ce n'est toujours pas le plus important.",
     "Texte seul, en très gros. La musique se coupe.",
     "impact grave"),
    ("PARTIE 3", "IMAGE", "J'ai écrit le guide pour faire pareil.",
     "La couverture de l'ebook arrive en 3D, avec une ombre portée. Déjà prête.",
     "pop"),
    ("PARTIE 3", "MOTION", "Dedans, je vous explique pourquoi le diplôme n'est pas nécessaire pour commencer. Comment vous faire connaître sur internet. Quelle forme donner à votre produit. Comment le fabriquer et le vendre avec ce que vous avez déjà. Et comment savoir en une semaine si des gens en veulent, sans dépenser un centime.",
     "5 badges numérotés qui s'empilent, avec les vraies pages du guide derrière : 1. Pas besoin de diplôme · 2. Se faire connaître · 3. Choisir son produit (petit livre, vidéo, modèle, checklist, kit) · 4. Créer et vendre · 5. Tester en 7 jours.",
     "pop sur chaque badge"),
    ("PARTIE 3", "MOTION", "En suivant le guide, vous saurez ce que vous vendez et à qui, vous aurez un premier produit, et vous saurez si des gens sont prêts à le payer.",
     "Une liste de 3 cases qui se cochent une à une.",
     "clic sur chaque case"),
    ("PARTIE 3", "MOTION", "Pas de blabla, juste ce qu'il faut faire, concrètement.",
     "La phrase claque mot par mot, en très gros.",
     "pop"),
    ("BOUCLE 3", "MOTION", "Et la meilleure partie ? Il suffit d'un message pour commencer.",
     "Une bulle de message WhatsApp qui s'écrit. La musique se coupe.",
     "montée en tension"),
    ("CTA", "VIDÉO", "Cliquez sur « Envoyer un message », écrivez-moi sur WhatsApp, et je vous accompagne.",
     "Main qui tient un téléphone avec WhatsApp ouvert. Bouton « ENVOYER UN MESSAGE » qui pulse et numéro +243 831 710 181.",
     "impact, notification WhatsApp, ping final"),
]

# timecodes estimés
t = 0.0
TIMES = []
for part, typ, vo, vis, son in SEG:
    words = len(vo.replace("...", " ").replace(" : ", " ").replace(" ? ", " ").split())
    d = words / RATE
    TIMES.append((t, t + d))
    t += d
TOTAL = t


def tc(s):
    s = int(round(s))
    return f"{s // 60}:{s % 60:02d}"


def paper():
    im = Image.new("RGB", (W, H), CREAM)
    d = ImageDraw.Draw(im)
    step = 54
    for x in range(0, W, step):
        d.line([(x, 0), (x, H)], fill=GRID, width=2)
    for y in range(0, H, step):
        d.line([(0, y), (W, y)], fill=GRID, width=2)
    return im, d


def wrap(d, text, font, width):
    words = text.split(" ")
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if d.textlength(trial, font=font) <= width:
            cur = trial
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def text_block(d, xy, text, font, width, fill, lh, draw=True):
    x, y = xy
    lines = wrap(d, text, font, width)
    if draw:
        for i, ln in enumerate(lines):
            d.text((x, y + i * lh), ln, font=font, fill=fill)
    return len(lines) * lh


def chip(d, x, y, typ, size=26, right=False):
    tpe = TYPES[typ]
    fnt = monob(size)
    tw = d.textlength(tpe["label"], font=fnt)
    w, h = tw + 2 * int(size * 0.9), int(size * 1.9)
    if right:
        x = x - w
    d.rounded_rectangle([x, y, x + w, y + h], radius=h // 2, fill=tpe["fill"], outline=INK, width=3)
    d.text((x + int(size * 0.9), y + int(size * 0.42)), tpe["label"], font=fnt, fill=tpe["text"])
    return w, h


def header(d, page, total):
    d.text((M, 70), "DÉCOUPAGE  ·  PUB DIGITALMIKAELSON  ·  VERSION FINALE", font=mono(26), fill=MUTED)
    lab = f"{page:02d} / {total:02d}"
    d.text((W - M - d.textlength(lab, font=mono(26)), 70), lab, font=mono(26), fill=MUTED)
    d.line([(M, 118), (W - M, 118)], fill=INK, width=3)


# ---------- page 1 : vue d'ensemble ----------
def page_overview(total_pages):
    im, d = paper()
    header(d, 1, total_pages)
    d.text((M, 170), "Découpage", font=baloo(150), fill=INK)
    d.text((M, 320), "de la pub", font=baloo(150), fill=INK)
    dur = f"{int(round(TOTAL))} s"
    d.text((W - M - d.textlength(dur, font=baloo(150)), 320), dur, font=baloo(150), fill=ORANGE)
    d.text((M, 545), "16 segments. La hauteur de chaque bloc correspond à sa durée.", font=sans(34), fill=INK)

    top, bottom = 650, 2570
    scale = (bottom - top) / TOTAL
    bx0, bx1 = M, M + 92
    col_part = M + 150
    col_num = M + 390
    col_chip_right = W - M
    fnt_lab = monob(28)
    fnt_num = baloo(44)
    prev_part = None
    for i, ((part, typ, *_), (a, b)) in enumerate(zip(SEG, TIMES)):
        y0, y1 = top + a * scale, top + b * scale
        tpe = TYPES[typ]
        d.rectangle([bx0, y0, bx1, y1], fill=tpe["fill"], outline=INK, width=3)
        cy = y0 + 6
        d.line([(bx1, y0), (W - M, y0)], fill=(205, 198, 186), width=2)
        if part != prev_part:
            d.text((col_part, cy + 4), part, font=fnt_lab, fill=INK)
        prev_part = part
        d.text((col_part + 150, cy + 4), tc(a), font=mono(26), fill=MUTED)
        d.text((col_num, cy - 10), f"{i + 1:02d}", font=fnt_num, fill=INK)
        snippet = SEG[i][2]
        fs = sans(28)
        maxw = col_chip_right - 300 - (col_num + 80)
        if d.textlength(snippet, font=fs) > maxw:
            while d.textlength(snippet + "…", font=fs) > maxw:
                snippet = snippet[:-1]
            snippet = snippet.rstrip(" ,") + "…"
        d.text((col_num + 80, cy + 6), snippet, font=fs, fill=INK)
        chip(d, col_chip_right, cy, typ, size=20, right=True)
    d.line([(bx1, bottom), (W - M, bottom)], fill=INK, width=3)
    d.text((col_part + 150, bottom + 8), tc(TOTAL), font=mono(26), fill=MUTED)

    counts = {k: sum(1 for s in SEG if s[1] == k) for k in TYPES}
    y = 2650
    x = M
    for k in ("VIDÉO", "IMAGE", "MOTION"):
        w, h = chip(d, x, y, k, size=26)
        lab = f"× {counts[k]}"
        d.text((x + w + 16, y + 6), lab, font=baloo(40), fill=INK)
        x += w + 16 + d.textlength(lab, font=baloo(40)) + 56
    d.text((M, 2760), "Timecodes estimés à environ 2,6 mots par seconde. Je les recale sur la voix finale dès réception.", font=sans(28), fill=MUTED)
    return im


# ---------- pages de cartes ----------
CARD_X0, CARD_X1 = M, W - M - 16
PAD = 52
STRIPE = 22


def card_height(d, seg):
    part, typ, vo, vis, son = seg
    inner = CARD_X1 - CARD_X0 - PAD * 2 - STRIPE
    h = PAD + 118
    h += text_block(d, (0, 0), f"« {vo} »", sansb(40), inner, INK, 54, draw=False) + 34
    h += 40 + text_block(d, (0, 0), vis, sans(34), inner, INK, 46, draw=False) + 26
    h += 40 + text_block(d, (0, 0), son, sans(34), inner, INK, 46, draw=False) + PAD
    return int(h)


def draw_card(d, y, idx, seg):
    part, typ, vo, vis, son = seg
    a, b = TIMES[idx]
    h = card_height(d, seg)
    x0, x1 = CARD_X0, CARD_X1
    d.rounded_rectangle([x0 + 16, y + 16, x1 + 16, y + h + 16], radius=36, fill=INK)
    d.rounded_rectangle([x0, y, x1, y + h], radius=36, fill=WHITE, outline=INK, width=5)
    tpe = TYPES[typ]
    d.rounded_rectangle([x0 + 5, y + 5, x0 + 5 + STRIPE + 20, y + h - 5], radius=31, fill=tpe["fill"])
    d.rectangle([x0 + 5 + STRIPE, y + 5, x0 + 5 + STRIPE + 20, y + h - 5], fill=WHITE)
    cx = x0 + STRIPE + PAD
    inner = x1 - cx - PAD
    d.text((cx, y + PAD - 26), f"{idx + 1:02d}", font=baloo(104), fill=INK)
    d.text((cx + 150, y + PAD + 4), part, font=monob(30), fill=INK)
    d.text((cx + 150, y + PAD + 46), f"{tc(a)} → {tc(b)}  ·  durée {b - a:.1f} s".replace(".", ","), font=mono(26), fill=MUTED)
    chip(d, x1 - PAD, y + PAD + 6, typ, size=26, right=True)
    yy = y + PAD + 118
    yy += text_block(d, (cx, yy), f"« {vo} »", sansb(40), inner, INK, 54) + 34
    d.text((cx, yy), "À L'ÉCRAN", font=monob(26), fill=ORANGE_TXT)
    yy += 40
    yy += text_block(d, (cx, yy), vis, sans(34), inner, INK, 46) + 26
    d.text((cx, yy), "SON", font=monob(26), fill=ORANGE_TXT)
    yy += 40
    text_block(d, (cx, yy), son, sans(34), inner, INK, 46)
    return h


def layout_cards():
    probe = ImageDraw.Draw(Image.new("RGB", (10, 10)))
    pages, cur, y = [], [], 170
    for i, s in enumerate(SEG):
        h = card_height(probe, s)
        if y + h + 16 > H - 110 and cur:
            pages.append(cur)
            cur, y = [], 170
        cur.append(i)
        y += h + 16 + 44
    if cur:
        pages.append(cur)
    return pages


# ---------- dernière page : à fournir ----------
def checkbox_list(d, x, y, items, width):
    for it in items:
        d.rounded_rectangle([x, y + 6, x + 38, y + 44], radius=8, outline=INK, width=4, fill=WHITE)
        hgt = text_block(d, (x + 64, y), it, sans(36), width - 64, INK, 48)
        y += max(hgt, 50) + 22
    return y


def page_todo(page, total):
    im, d = paper()
    header(d, page, total)
    d.text((M, 170), "À m'envoyer", font=baloo(130), fill=INK)
    y = 360
    w, h = chip(d, M, y, "VIDÉO", size=26)
    d.text((M + w + 20, y + 4), "8 à 10 extraits de 3 à 5 s, verticaux si possible", font=sans(32), fill=INK)
    y += 90
    y = checkbox_list(d, M, y, [
        "Hook : 3 ou 4 plans de mains au travail (0,5 s chacun suffit)",
        "Cuisine",
        "Couture",
        "Langues (quelqu'un qui enseigne ou parle une langue)",
        "Comptabilité (calculatrice, cahier de comptes)",
        "Une personne qui donne un cours en appel vidéo",
        "Mains de menuisier au travail, idéalement l'oncle David",
        "Main qui tient un téléphone avec WhatsApp ouvert",
    ], W - 2 * M)
    y += 40
    w, h = chip(d, M, y, "IMAGE", size=26)
    d.text((M + w + 20, y + 4), "les portraits Canva déjà générés", font=sans(32), fill=INK)
    y += 90
    y = checkbox_list(d, M, y, ["Portrait salarié", "Portrait étudiante", "Portrait personne sans emploi"], W - 2 * M)
    y += 40
    d.text((M, y), "AUDIO", font=monob(30), fill=ORANGE_TXT)
    y += 56
    y = checkbox_list(d, M, y, ["La voix ElevenLabs de la version finale (environ 85 s)"], W - 2 * M)
    y += 60
    d.line([(M, y), (W - M, y)], fill=INK, width=3)
    y += 40
    d.text((M, y), "Déjà prêt de mon côté", font=baloo(64), fill=INK)
    y += 100
    for it in ["Couverture et pages de l'ebook", "Icône WhatsApp", "Musique de fond originale",
               "19 effets sonores (licence commerciale)", "Style validé : quadrillage, Baloo 2, surlignage jaune"]:
        d.ellipse([M + 6, y + 16, M + 26, y + 36], fill=ORANGE)
        d.text((M + 60, y), it, font=sans(36), fill=INK)
        y += 64
    return im


def main():
    card_pages = layout_cards()
    total = 1 + len(card_pages) + 1
    pages = [page_overview(total)]
    for pi, idxs in enumerate(card_pages):
        im, d = paper()
        header(d, pi + 2, total)
        y = 170
        for i in idxs:
            h = draw_card(d, y, i, SEG[i])
            y += h + 16 + 44
        pages.append(im)
    pages.append(page_todo(total, total))
    out = os.path.join(HERE, "decoupage_pub_digitalmikaelson.pdf")
    pages[0].save(out, save_all=True, append_images=pages[1:], resolution=150)
    for i, p in enumerate(pages):
        p.resize((540, 960), Image.LANCZOS).save(os.path.join(HERE, f"_apercu_{i + 1:02d}.png"))
    print(out, len(pages), f"{TOTAL:.1f}s")


if __name__ == "__main__":
    main()
