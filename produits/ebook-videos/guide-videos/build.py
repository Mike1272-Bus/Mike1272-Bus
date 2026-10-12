"""Construit les 6 vidéos du guide « Gagne ta vie sans diplôme » (motion design 16:9, fond blanc, sans voix).

Chaque vidéo est décrite plus bas comme une liste de scènes. Le script écrit vN/index.html,
copie les ressources communes et fabrique la musique + les bruitages calés sur les animations.
Quand Mike enverra ses audios, on recalera les durées des scènes sur sa voix.

Utilisation : python3 build.py            (prépare tout)
              python3 build.py v2          (une seule vidéo)
Puis, dans vN/ : npx --yes hyperframes@0.8.77 render -o renders/vN.mp4
"""
import html, json, os, shutil, subprocess, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(ROOT, "..", "..", ".."))
SFX_DIR = os.path.join(REPO, "video-excel-13h", "assets", "sfx")
MUSIC = os.path.join(REPO, "pub-video-digitalmikaelson", "assets", "audio", "musique_fond.wav")
E = html.escape

# ------------------------------------------------------------------ les vidéos

VIDEOS = {
  "v0": ("Bienvenue", [
    ("media", 5.0, dict(kind="photo", src="mike.jpg", lines=[("Salut, c'est Mike", "sm"), ("Bienvenue", "big"), ("dans ton guide", "sm")])),
    ("media", 5.0, dict(kind="img", src="ebook.png", lines=[("« Gagne ta vie", "sm"), ("sans diplôme »", "big"), ("Merci pour ta confiance", "red")])),
    ("texte", 6.0, dict(img="money_bag_3d.png", lines=[("Pas de belles phrases.", "sm"), ("Une seule chose :", "sm"), ("transformer ce que tu sais faire", "big2"), ("en un produit que quelqu'un paie", "red")])),
    ("texte", 4.5, dict(img="clapper_board_3d.png", lines=[("Dans chaque chapitre,", "sm"), ("une vidéo comme celle-ci", "big2"), ("avec des exemples, pour agir tout de suite", "red")])),
    ("etapes", 7.0, dict(sm="On va faire ça", big="en 4 étapes", items=["Casser le mythe", "Trouver ta compétence vendable", "Choisir ton format", "Tester ton idée en 7 jours"], sub="sans dépenser un centime en publicité")),
    ("texte", 4.0, dict(img="pencil_3d.png", lines=[("Prends une feuille et un stylo.", "sm"), ("On y va !", "big")])),
  ]),
  "v1": ("Le mythe à casser", [
    ("titre", 3.6, dict(chap="Chapitre 1", titre="Le mythe à casser", img="locked_3d.png")),
    ("barre", 7.0, dict(titre="On t'a dit qu'il fallait :", items=["un diplôme rare", "savoir coder", "parler anglais couramment", "un talent spécial"], fin="C'est faux.")),
    ("texte", 6.0, dict(img="light_bulb_3d.png", lines=[("On ne vend presque jamais un talent rare.", "sm"), ("On vend la solution", "big2"), ("à un problème précis", "big2"), ("à quelqu'un qui ne veut pas tout apprendre seul", "red")])),
    ("cartes", 7.0, dict(sm="Regarde autour de toi.", big="Tu sais…", cartes=[("shopping_cart_3d.png", "négocier un prix au marché", ""), ("hammer_and_wrench_3d.png", "réparer un téléphone qui ne charge plus", ""), ("pot_of_food_3d.png", "cuisiner le plat que tout le monde réclame", "")])),
    ("cartes", 6.0, dict(sm="Aucun diplôme. Et chacun peut devenir :", big="un produit", cartes=[("page_facing_up_3d.png", "un petit guide", ""), ("clipboard_3d.png", "une checklist", ""), ("clapper_board_3d.png", "une courte formation", "")])),
    ("texte", 6.0, dict(img="magnifying_glass_tilted_left_3d.png", lines=[("Tu n'as pas « rien à vendre ».", "sm"), ("Tu cherches", "big2"), ("au mauvais endroit", "big2"), ("regarde ce que tu fais déjà, mieux que les autres", "red")])),
    ("media", 6.5, dict(kind="video", src="menuiserie.mp4", lines=[("Mon oncle David, menuisier :", "sm"), ("ses mains", "big"), ("→ un guide", "big"), ("que d'autres peuvent suivre", "red")])),
    ("texte", 3.6, dict(img="gem_stone_3d.png", lines=[("Chapitre 2 :", "sm"), ("trouve ta version", "big")])),
  ]),
  "v2": ("Trouve ta compétence vendable", [
    ("titre", 3.6, dict(chap="Chapitre 2", titre="Trouve ta compétence vendable", img="gem_stone_3d.png")),
    ("texte", 3.8, dict(img="light_bulb_3d.png", lines=[("Pas besoin d'une révélation.", "sm"), ("3 bonnes questions", "big")])),
    ("cartes", 9.5, dict(sm="3 familles de compétences", big="et leur question", cartes=[("hammer_and_wrench_3d.png", "La compétence pratique", "Qu'est-ce qu'on me demande souvent ?"), ("books_3d.png", "Le savoir transmis", "Que pourrais-je expliquer à quelqu'un qui part de zéro ?"), ("key_3d.png", "Le problème que tu résous", "Pour quoi m'appelle-t-on quand on est bloqué ?")])),
    ("media", 5.5, dict(kind="video", src="expliquer.mp4", lines=[("Pas besoin d'être le meilleur.", "sm"), ("1 ou 2 pas", "big"), ("d'avance suffisent", "red")])),
    ("feuille", 8.0, dict()),
    ("texte", 5.0, dict(img="check_mark_button_3d.png", lines=[("Pas la plus originale.", "sm"), ("La plus vérifiée.", "big"), ("celle pour laquelle on t'a déjà dit merci, ou payé", "red")])),
    ("texte", 3.6, dict(img="pencil_3d.png", lines=[("Fais l'exercice maintenant,", "sm"), ("avant le chapitre 3", "big2")])),
  ]),
  "v3": ("Choisis ton format", [
    ("titre", 3.6, dict(chap="Chapitre 3", titre="Choisis ton format", img="package_3d.png")),
    ("barre", 5.8, dict(titre="Pas besoin de :", items=["un site web", "une application", "des heures de montage"], fin="Ce que tu as suffit.")),
    ("cartes", 9.0, dict(sm="4 formats simples", big="à faire avec ton téléphone", cartes=[("page_facing_up_3d.png", "Le mini-guide", "ta méthode étape par étape"), ("memo_3d.png", "Le modèle", "prêt à remplir : budget, contrat…"), ("clipboard_3d.png", "La checklist", "pour ne rien oublier"), ("clapper_board_3d.png", "La capsule vidéo", "filmée au téléphone")])),
    ("texte", 4.2, dict(img="hourglass_not_done_3d.png", lines=[("Les gens paient pour", "sm"), ("gagner du temps", "big"), ("pas seulement pour apprendre", "red")])),
    ("texte", 4.8, dict(img="rocket_3d.png", lines=[("Ton premier produit ?", "sm"), ("le plus rapide à faire", "big2"), ("pas parfait : prêt cette semaine", "red")])),
    ("texte", 4.5, dict(img="spiral_calendar_3d.png", lines=[("Tu amélioreras la forme", "sm"), ("quand on voudra le fond", "big2"), ("chapitre 4 : le test en 7 jours", "red")])),
  ]),
  "v4": ("Le test en 7 jours", [
    ("titre", 3.6, dict(chap="Chapitre 4", titre="Le test en 7 jours", img="spiral_calendar_3d.png")),
    ("texte", 5.0, dict(img="coin_3d.png", lines=[("Avant de passer des semaines sur ton produit :", "sm"), ("des gens vont-ils", "big2"), ("vraiment payer ?", "big2"), ("sans un centime de publicité", "red")])),
    ("jour", 7.5, dict(actifs=[1, 2], titre="Écris ton offre en une phrase", kind="phrase", lignes=["J'aide [telle personne]", "à obtenir [tel résultat]", "grâce à [ma compétence]."], exemple="Ex. : j'aide les vendeuses du marché à calculer leurs prix sans perdre d'argent.")),
    ("jour", 6.0, dict(actifs=[3], titre="Écris à 10 ou 15 proches", kind="bulle", bulle="Je prépare un petit guide sur ce sujet, ça t'intéresserait ?", compte="Compte les « oui »")),
    ("jour", 5.5, dict(actifs=[4, 5], titre="Mets ta phrase en statut", kind="icones", icones=["icon_whatsapp.png", "icon_facebook.png", "icon_instagram.png"], legende="Qui réagit ? Qui pose des questions ?")),
    ("jour", 6.0, dict(actifs=[6], titre="Propose un petit prix", kind="versus")),
    ("jour", 5.0, dict(actifs=[7], titre="Le bilan", kind="bilan", texte="Une personne a payé ? Ton idée tient la route.")),
    ("texte", 5.0, dict(img="bullseye_3d.png", lines=[("Personne ne réagit ?", "sm"), ("C'est une information", "big2"), ("change d'angle, ou teste une autre compétence", "red")])),
    ("texte", 5.0, dict(img="pencil_3d.png", lines=[("La plupart font l'inverse.", "sm"), ("Toi, tu demandes d'abord.", "big2"), ("Ton test commence aujourd'hui", "red")])),
  ]),
  "v5": ("Et après ?", [
    ("etapes", 5.5, dict(sm="Bravo !", big="Tu as la base", items=["Casser le mythe", "Trouver ta compétence vendable", "Choisir ton format", "Tester ton idée en 7 jours"], coche=True)),
    ("cartes", 6.5, dict(sm="Maintenant, le vrai travail :", big="la suite", cartes=[("counterclockwise_arrows_button_3d.png", "Vendre encore et encore", ""), ("megaphone_3d.png", "Te faire connaître", ""), ("chart_increasing_3d.png", "Un revenu qui tient", "")])),
    ("texte", 4.0, dict(img="rocket_3d.png", lines=[("Un premier résultat, même petit ?", "sm"), ("Tu es prêt pour la suite", "big2")])),
    ("media", 7.0, dict(kind="photo", src="mike.jpg", lines=[("Écris-moi sur WhatsApp :", "sm"), ("où tu en es", "big"), ("ta compétence · ta phrase · ton test", "red")], bouton="Le bouton est à la dernière page")),
  ]),
}

# ------------------------------------------------------------------ outils

class Scene:
    def __init__(self, n, a, d, bg):
        self.n, self.a, self.d, self.bg = n, a, d, bg
        self.h, self.js, self.sfx, self.k = [], [], [], 0

    def id(self, p):
        self.k += 1
        return f"s{self.n}{p}{self.k}"

    def words(self, text, top, at, cls="sm", left=0, width=1920, gap=0.11, style=""):
        ids, spans = [], []
        for w in text.split(" "):
            i = self.id("w"); ids.append(i)
            spans.append(f'<span class="w {cls}" id="{i}">{E(w)}</span>')
        self.h.append(f'<div class="line" style="top:{top}px; left:{left}px; width:{width}px;{style}">{"".join(spans)}</div>')
        self.js.append(f'words({json.dumps(["#" + i for i in ids])}, {at:.2f}, {gap});')
        return at + gap * len(ids)

    def big(self, text, top, at, size=110, left=0, width=1920, how="bigIn", cls="big"):
        i = self.id("b")
        self.h.append(f'<div class="line" style="top:{top}px; left:{left}px; width:{width}px" data-layout-allow-overlap><span class="w {cls}" id="{i}" style="font-size:{size}px">{E(text)}</span></div>')
        self.js.append(f'{how}("#{i}", {at:.2f});')
        self.sfx.append((at, "whoosh-short", 0.22))

    def img(self, src, left, top, size, at, how="pop", flt=True):
        i = self.id("i")
        self.h.append(f'<img class="obj" id="{i}" src="assets/img/{src}" style="left:{left}px; top:{top}px; width:{size}px; height:{size}px" />')
        self.js.append(f'{how}("#{i}", {at:.2f});')
        if flt:
            self.js.append(f'float("#{i}", {at + 0.5:.2f}, {max(1.0, self.a + self.d - at - 0.6):.2f});')
        self.sfx.append((at, "pop", 0.2))
        return i

    def lines(self, lines, at, left=0, width=1920, gap=None):
        hts = {"sm": 78, "big": 128, "big2": 112, "red": 74}
        total = sum(hts[k] for _, k in lines)
        top = 540 - total // 2 - 20
        n = len(lines)
        g = gap if gap else min(1.0, max(0.45, (self.a + self.d - at - 1.4) / max(1, n)))
        t = at
        for text, k in lines:
            if k == "sm":
                self.words(text, top, t, "sm", left, width)
            elif k == "red":
                self.words(text, top + 4, t, "sm red", left, width, gap=0.08)
            else:
                size = 110 if k == "big" else 92
                if len(text) > 26: size = min(size, 84)
                self.big(text, top, t, size, left, width)
            top += hts[k]
            t += g


def scene_html(sc, kind, p):
    a, d = sc.a, sc.d
    if kind == "titre":
        sc.img(p["img"], 810, 130, 300, a + 0.15)
        sc.words(p["chap"], 470, a + 0.4)
        size = 120 if len(p["titre"]) <= 22 else 96
        sc.big(p["titre"], 565, a + 0.85, size, how="drop")
        sc.sfx.append((a + 0.85, "impact-bass-1", 0.18))
    elif kind == "texte":
        if p.get("img"):
            sc.img(p["img"], 150, 360, 340, a + 0.15)
            sc.lines(p["lines"], a + 0.3, left=520, width=1340)
        else:
            sc.lines(p["lines"], a + 0.3)
    elif kind == "media":
        k = p["kind"]
        i = sc.id("m")
        if k == "photo":
            sc.h.append(f'<div class="ab photo" id="{i}"><img src="assets/img/{p["src"]}" /></div>')
        elif k == "img":
            sc.h.append(f'<div class="ab cover" id="{i}"><img src="assets/img/{p["src"]}" /></div>')
        else:
            sc.h.append(f'<div class="ab vcard" id="{i}"><video id="{i}v" src="assets/video/{p["src"]}" muted playsinline data-start="{a:.2f}" data-duration="{d:.2f}" data-media-start="0"></video></div>')
        sc.js.append(f'IN("#{i}", {{ y: 400, rotation: 8, scale: 0.8 }}, {{ y: 0, rotation: -3, scale: 1, duration: 0.55, ease: "back.out(1.4)" }}, {a + 0.1:.2f});')
        sc.js.append(f'float("#{i}", {a + 0.7:.2f}, {d - 0.8:.2f}, -12);')
        sc.sfx.append((a + 0.1, "whoosh", 0.28))
        sc.lines(p["lines"], a + 0.6, left=1000, width=860)
        if p.get("bouton"):
            j = sc.id("wa")
            sc.h.append(f'<div class="ab wabtn" id="{j}"><img src="assets/img/icon_whatsapp.png" />{E(p["bouton"])}</div>')
            sc.js.append(f'IN("#{j}", {{ scale: 0.4 }}, {{ scale: 1, duration: 0.4, ease: "back.out(2.4)" }}, {a + 3.6:.2f});')
            sc.js.append(f'FT("#{j}", {{ scale: 1 }}, {{ scale: 1.06, duration: 0.3, yoyo: true, repeat: 3, ease: "sine.inOut" }}, {a + 4.3:.2f});')
            sc.sfx.append((a + 3.6, "ping", 0.25))
    elif kind == "barre":
        sc.words(p["titre"], 150, a + 0.2)
        items = p["items"]
        n = len(items)
        if n == 4:
            pos = [(210, 330), (990, 330), (210, 500), (990, 500)]; w = 720
        else:
            pos = [(90 + k * 600, 400) for k in range(n)]; w = 560
        t = a + 0.8
        for k, it in enumerate(items):
            i = sc.id("p")
            x, y = pos[k]
            sc.h.append(f'<div class="ab bpill" id="{i}" style="left:{x}px; top:{y}px; width:{w}px; font-size:{46 if n == 4 else 42}px">{E(it)}<i id="{i}x"></i></div>')
            sc.js.append(f'IN("#{i}", {{ scale: 0.4 }}, {{ scale: 1, duration: 0.35, ease: "back.out(2)" }}, {t:.2f});')
            sc.sfx.append((t, "pop", 0.2))
            t += 0.5
        t += 0.2
        for k in range(n):
            i = f"s{sc.n}p{k + sc.k - n + 1}"
        ids = [l.split('id="')[1].split('"')[0] for l in sc.h if 'class="ab bpill"' in l]
        for i in ids:
            sc.js.append(f'HIDE.push("#{i}x"); FT("#{i}x", {{ autoAlpha: 1, scaleX: 0 }}, {{ scaleX: 1, duration: 0.22, ease: "power2.out" }}, {t:.2f});')
            sc.js.append(f'FT("#{i}", {{ opacity: 1 }}, {{ opacity: 0.55, duration: 0.2 }}, {t + 0.1:.2f});')
            sc.sfx.append((t, "whoosh-short", 0.2))
            t += 0.3
        sc.big(p["fin"], 760, t + 0.15, 120, how="stamp")
        sc.sfx.append((t + 0.15, "impact-bass-2", 0.25))
    elif kind == "cartes":
        sc.words(p["sm"], 120, a + 0.2)
        sc.big(p["big"], 200, a + 0.55, 96)
        cards = p["cartes"]
        n = len(cards)
        w = min(440, (1720 - (n - 1) * 40) // n)
        x0 = (1920 - (n * w + (n - 1) * 40)) // 2
        g = min(1.4, max(0.5, (d - 2.2) / n))
        hh = 540 if any(c[2] for c in cards) else 440
        for k, (im, t1, t2) in enumerate(cards):
            i = sc.id("c")
            sub = f'<em>{E(t2)}</em>' if t2 else ""
            sc.h.append(f'<div class="ab card" id="{i}" style="left:{x0 + k * (w + 40)}px; width:{w}px; height:{hh}px"><img src="assets/img/{im}" /><b>{E(t1)}</b>{sub}</div>')
            at = a + 1.1 + k * g
            sc.js.append(f'IN("#{i}", {{ y: 300, scale: 0.6, rotation: {(-8 if k % 2 else 8)} }}, {{ y: 0, scale: 1, rotation: 0, duration: 0.45, ease: "back.out(1.6)" }}, {at:.2f});')
            sc.sfx.append((at, "pop", 0.22))
    elif kind == "etapes":
        sc.words(p["sm"], 130, a + 0.2)
        sc.big(p["big"], 215, a + 0.5, 104)
        items = p["items"]
        n = len(items)
        g = min(1.2, max(0.4, (d - 2.6) / n))
        for k, it in enumerate(items):
            i = sc.id("e")
            x = 150 + k * 420
            sc.h.append(f'<div class="ab step" id="{i}" style="left:{x}px"><div class="sn">{k + 1}</div><b>{E(it)}</b><img class="ck" id="{i}k" src="assets/img/check_mark_button_3d.png" /></div>')
            at = a + 1.0 + k * g
            sc.js.append(f'IN("#{i}", {{ y: 200, scale: 0.6 }}, {{ y: 0, scale: 1, duration: 0.4, ease: "back.out(1.8)" }}, {at:.2f});')
            sc.sfx.append((at, "pop", 0.22))
            if p.get("coche"):
                sc.js.append(f'IN("#{i}k", {{ scale: 0, rotation: -90 }}, {{ scale: 1, rotation: 0, duration: 0.35, ease: "back.out(2.5)" }}, {at + 0.35:.2f});')
                sc.sfx.append((at + 0.35, "ping", 0.15))
            else:
                sc.h[-1] = sc.h[-1].replace(f'<img class="ck" id="{i}k" src="assets/img/check_mark_button_3d.png" />', "")
        if p.get("sub"):
            sc.words(p["sub"], 870, a + 1.0 + n * g, "sm red", gap=0.08)
    elif kind == "feuille":
        sc.words("L'exercice :", 90, a + 0.2)
        sc.big("3 questions × 3 réponses", 165, a + 0.5, 84)
        i = sc.id("f")
        heads = ["On me demande souvent…", "Je peux expliquer…", "On m'appelle pour…"]
        cols = "".join(f'<div class="col" style="left:{40 + c * 390}px"><h4>{E(h)}</h4>' + "".join(f'<i id="{i}l{c}{r}" style="top:{110 + r * 110}px; width:{300 - (r * 37 + c * 23) % 90}px"></i>' for r in range(3)) + "</div>" for c, h in enumerate(heads))
        sc.h.append(f'<div class="ab sheet" id="{i}">{cols}<svg class="circ" viewBox="0 0 360 120" style="left:{40 + 390 - 30}px; top:{110 + 110 - 38}px"><ellipse id="{i}o" cx="180" cy="60" rx="170" ry="52" /></svg></div>')
        sc.js.append(f'IN("#{i}", {{ y: 500, rotation: 3 }}, {{ y: 0, rotation: 0, duration: 0.5, ease: "back.out(1.3)" }}, {a + 0.6:.2f});')
        t = a + 1.4
        for c in range(3):
            for r in range(3):
                sc.js.append(f'IN("#{i}l{c}{r}", {{ scaleX: 0, transformOrigin: "0% 50%" }}, {{ scaleX: 1, duration: 0.2, ease: "power2.out" }}, {t:.2f});')
                sc.sfx.append((t, "click-soft", 0.15))
                t += 0.28
        sc.js.append(f'FT("#{i}o", {{ strokeDasharray: 1000, strokeDashoffset: 1000 }}, {{ strokeDashoffset: 0, duration: 0.6, ease: "power2.inOut" }}, {t + 0.2:.2f});')
        sc.sfx.append((t + 0.2, "whoosh", 0.22))
        sc.words("Entoure celle qui revient le plus souvent", 960, t + 0.4, "sm red", gap=0.08)
    elif kind == "jour":
        act = p["actifs"]
        for dd in range(1, 8):
            i = sc.id("j")
            cls = "day on" if dd in act else ("day done" if dd < min(act) else "day")
            sc.h.append(f'<div class="ab {cls}" id="{i}" style="left:{270 + (dd - 1) * 200}px">J{dd}</div>')
            sc.js.append(f'IN("#{i}", {{ y: -80 }}, {{ y: 0, duration: 0.3, ease: "back.out(2)" }}, {a + 0.05 + dd * 0.04:.2f});')
            if dd in act:
                sc.js.append(f'FT("#{i}", {{ scale: 1 }}, {{ scale: 1.15, duration: 0.18, yoyo: true, repeat: 1 }}, {a + 0.5:.2f});')
        jt = "Jour " + str(act[0]) if len(act) == 1 else f"Jours {act[0]} et {act[1]}"
        sc.big(jt, 235, a + 0.45, 96, how="drop")
        sc.words(p["titre"], 360, a + 0.8)
        k = p["kind"]
        t = a + 1.5
        if k == "phrase":
            i = sc.id("ph")
            ws = []
            inner = []
            for li in p["lignes"]:
                spans = []
                for w in li.split(" "):
                    wi = sc.id("pw"); ws.append(wi)
                    cls = ' class="blank"' if w.startswith("[") or w.endswith("]") or w.endswith("].") else ""
                    spans.append(f'<span id="{wi}"{cls}>{E(w)}</span>')
                inner.append(" ".join(spans))
            sc.h.append(f'<div class="ab phrase" id="{i}">{"<br/>".join(inner)}</div>')
            sc.js.append(f'IN("#{i}", {{ scale: 0.8 }}, {{ scale: 1, duration: 0.35, ease: "back.out(1.6)" }}, {t:.2f});')
            sc.js.append(f'IN({json.dumps(["#" + w for w in ws])}, {{ y: 10 }}, {{ y: 0, duration: 0.12, stagger: 0.12 }}, {t + 0.3:.2f});')
            sc.sfx.append((t + 0.3, "typing", 0.25))
            sc.words(p["exemple"], 900, t + 0.6 + 0.12 * len(ws), "sm red", gap=0.06)
        elif k == "bulle":
            i = sc.id("bu")
            sc.h.append(f'<div class="ab bulle" id="{i}">{E(p["bulle"])}<span>✓✓</span></div>')
            sc.js.append(f'IN("#{i}", {{ x: 300, scale: 0.6, transformOrigin: "100% 100%" }}, {{ x: 0, scale: 1, duration: 0.4, ease: "back.out(1.8)" }}, {t:.2f});')
            sc.sfx.append((t, "notification", 0.25))
            sc.words(p["compte"], 760, t + 1.0, "sm red", gap=0.08)
            for q in range(5):
                j = sc.id("oui")
                sc.h.append(f'<div class="ab oui" id="{j}" style="left:{560 + q * 170}px">oui</div>')
                sc.js.append(f'IN("#{j}", {{ scale: 0, rotation: -30 }}, {{ scale: 1, rotation: 0, duration: 0.3, ease: "back.out(2.5)" }}, {t + 1.6 + q * 0.35:.2f});')
                sc.sfx.append((t + 1.6 + q * 0.35, "pop", 0.18))
        elif k == "icones":
            for q, ic in enumerate(p["icones"]):
                sc.img(ic, 600 + q * 280, 500, 200, t + q * 0.35, flt=False)
            sc.words(p["legende"], 800, t + 1.4, "sm red", gap=0.08)
        elif k == "versus":
            i, j = sc.id("vs"), sc.id("vs")
            sc.h.append(f'<div class="ab vs poli" id="{i}"><img src="assets/img/speech_balloon_3d.png" /><b>Intérêt poli</b><em>« ça m’intéresse… »</em></div>')
            sc.h.append(f'<div class="ab vs reel" id="{j}"><img src="assets/img/coin_3d.png" /><b>Intérêt réel</b><em>il sort son argent</em></div>')
            sc.js.append(f'IN("#{i}", {{ x: -600 }}, {{ x: 0, duration: 0.45, ease: "expo.out" }}, {t:.2f});')
            sc.js.append(f'IN("#{j}", {{ x: 600 }}, {{ x: 0, duration: 0.45, ease: "expo.out" }}, {t + 1.2:.2f});')
            sc.js.append(f'FT("#{i}", {{ opacity: 1 }}, {{ opacity: 0.5, duration: 0.3 }}, {t + 2.2:.2f}); FT("#{j}", {{ scale: 1 }}, {{ scale: 1.06, duration: 0.25, yoyo: true, repeat: 3 }}, {t + 2.2:.2f});')
            sc.sfx += [(t, "whoosh", 0.25), (t + 1.2, "whoosh", 0.25), (t + 2.2, "ping", 0.2)]
        elif k == "bilan":
            sc.img("check_mark_button_3d.png", 810, 470, 300, t, how="pop")
            sc.words(p["texte"], 830, t + 0.6, "sm red", gap=0.08)
            sc.sfx.append((t, "chime", 0.25))


CSS = """
@font-face { font-family: 'Inter'; font-weight: 600; src: url('assets/fonts/inter-latin-600-normal.woff2') format('woff2'); }
@font-face { font-family: 'Inter'; font-weight: 800; src: url('assets/fonts/inter-latin-800-normal.woff2') format('woff2'); }
@font-face { font-family: 'Inter'; font-weight: 900; src: url('assets/fonts/inter-latin-900-normal.woff2') format('woff2'); }
* { margin: 0; padding: 0; box-sizing: border-box; }
html, body { width: 1920px; height: 1080px; overflow: hidden; background: #fff; }
#root { position: relative; width: 1920px; height: 1080px; overflow: hidden; font-family: 'Inter', sans-serif; }
.ab { position: absolute; }
.scene { position: absolute; left: 0; top: 0; width: 1920px; height: 1080px; overflow: hidden; }
.cam { position: absolute; left: 0; top: 0; width: 1920px; height: 1080px; }
.white { background: radial-gradient(ellipse at 50% 45%, #ffffff 0%, #f7f7f7 65%, #ececec 100%); }
.cream { background: radial-gradient(ellipse at 50% 40%, #fbf8f3 0%, #efebe4 70%, #e4dfd7 100%); }
.grid { position: absolute; inset: 0; background-image: linear-gradient(rgba(0,0,0,0.035) 1px, transparent 1px), linear-gradient(90deg, rgba(0,0,0,0.035) 1px, transparent 1px); background-size: 60px 60px; }
.swoosh { position: absolute; left: -200px; top: -400px; width: 2320px; height: 1880px; }
.line { position: absolute; text-align: center; white-space: nowrap; }
.w { display: inline-block; margin: 0 0.12em; }
.sm { font-weight: 600; font-size: 54px; letter-spacing: -0.02em; color: #141414; }
.red { color: #e8401f; font-weight: 800; font-size: 46px; }
.big { font-weight: 900; letter-spacing: -0.045em; line-height: 0.95; color: #ff3d1f; text-shadow: 0 6px 0 #8f1d0c, 0 18px 30px rgba(0,0,0,0.25); }
.obj { position: absolute; filter: drop-shadow(0 30px 40px rgba(0,0,0,0.3)); }
.photo { left: 300px; top: 210px; width: 600px; height: 600px; border-radius: 50%; overflow: hidden; border: 14px solid #fff; box-shadow: 0 0 0 10px #ff3d1f, 0 40px 70px rgba(0,0,0,0.3); }
.photo img, .cover img { width: 100%; height: 100%; object-fit: cover; }
.cover { left: 270px; top: 190px; width: 640px; height: 640px; border-radius: 18px; overflow: hidden; box-shadow: 0 40px 70px rgba(0,0,0,0.3); }
.vcard { left: 90px; top: 240px; width: 880px; height: 495px; border-radius: 34px; overflow: hidden; border: 10px solid #fff; box-shadow: 0 30px 60px rgba(0,0,0,0.22); background: #ddd; }
.vcard video { width: 100%; height: 100%; object-fit: cover; display: block; }
.wabtn { left: 1060px; top: 860px; width: 740px; height: 110px; border-radius: 55px; background: #1a9e4b; color: #fff; font-weight: 800; font-size: 38px; line-height: 110px; padding-left: 120px; box-shadow: 0 16px 34px rgba(26,158,75,0.35); }
.wabtn img { position: absolute; left: 20px; top: 15px; width: 80px; height: 80px; border-radius: 20px; }
.bpill { height: 120px; border-radius: 60px; background: #fff; border: 4px solid #e6e1d9; box-shadow: 0 16px 32px rgba(0,0,0,0.1); font-weight: 800; font-size: 46px; line-height: 112px; text-align: center; color: #141414; }
.bpill i { position: absolute; left: 30px; right: 30px; top: 52px; height: 12px; border-radius: 6px; background: #ff3d1f; transform-origin: 0% 50%; }
.card { top: 380px; height: 560px; border-radius: 36px; background: #fff; border: 4px solid #e6e1d9; box-shadow: 0 22px 44px rgba(0,0,0,0.1); text-align: center; padding: 0 26px; }
.card img { display: block; width: 200px; height: 200px; margin: 40px auto 26px; }
.card b { display: block; font-size: 44px; font-weight: 900; line-height: 1.1; letter-spacing: -0.03em; color: #141414; }
.card em { display: block; margin-top: 18px; font-style: normal; font-size: 32px; font-weight: 700; line-height: 1.25; color: #e8401f; }
.step { top: 420px; width: 380px; text-align: center; }
.step .sn { width: 170px; height: 170px; margin: 0 auto 30px; border-radius: 50%; background: #ff3d1f; color: #fff; font-weight: 900; font-size: 100px; line-height: 170px; box-shadow: 0 0 0 12px rgba(255,61,31,0.15), 0 18px 34px rgba(255,61,31,0.35); }
.step b { display: block; font-size: 40px; font-weight: 900; line-height: 1.12; letter-spacing: -0.02em; color: #141414; }
.step .ck { position: absolute; left: 230px; top: -10px; width: 110px; height: 110px; }
.sheet { left: 360px; top: 320px; width: 1200px; height: 600px; border-radius: 26px; background: #fff; border: 3px solid #e6e1d9; box-shadow: 0 24px 50px rgba(0,0,0,0.12); background-image: repeating-linear-gradient(180deg, transparent 0 107px, #e4ecf7 107px 110px); }
.sheet .col { position: absolute; top: 30px; width: 360px; height: 540px; }
.sheet h4 { font-size: 34px; font-weight: 900; color: #141414; letter-spacing: -0.02em; }
.sheet .col i { position: absolute; left: 0; height: 26px; border-radius: 13px; background: #c9d3e6; }
.circ { position: absolute; width: 360px; height: 120px; overflow: visible; }
.circ ellipse { fill: none; stroke: #ff3d1f; stroke-width: 9; stroke-linecap: round; }
.day { top: 70px; width: 180px; height: 110px; border-radius: 24px; background: #fff; border: 4px solid #e6e1d9; font-weight: 900; font-size: 50px; line-height: 102px; text-align: center; color: #9a9a9a; }
.day.on { background: #ff3d1f; border-color: #ff3d1f; color: #fff; box-shadow: 0 14px 30px rgba(255,61,31,0.35); }
.day.done { background: #141414; border-color: #141414; color: #fff; }
.phrase { left: 360px; top: 480px; width: 1200px; padding: 40px 50px; border-radius: 30px; background: #fff; border: 4px solid #e6e1d9; box-shadow: 0 20px 40px rgba(0,0,0,0.1); font-weight: 800; font-size: 58px; line-height: 1.35; color: #141414; text-align: center; }
.phrase span { display: inline-block; }
.phrase .blank { color: #ff3d1f; }
.bulle { left: 460px; top: 480px; width: 1000px; padding: 40px 50px 56px; border-radius: 34px 34px 8px 34px; background: #d9fdd3; font-weight: 700; font-size: 50px; line-height: 1.3; color: #111; box-shadow: 0 16px 34px rgba(0,0,0,0.12); }
.bulle span { position: absolute; right: 30px; bottom: 10px; font-size: 32px; font-weight: 900; color: #2f9fd0; letter-spacing: -8px; }
.oui { top: 850px; width: 150px; height: 80px; border-radius: 40px; background: #1a9e4b; color: #fff; font-weight: 900; font-size: 40px; line-height: 80px; text-align: center; }
.vs { top: 470px; width: 640px; height: 400px; border-radius: 36px; text-align: center; border: 4px solid #e6e1d9; background: #fff; box-shadow: 0 22px 44px rgba(0,0,0,0.1); }
.vs img { display: block; width: 170px; height: 170px; margin: 36px auto 16px; }
.vs b { display: block; font-size: 54px; font-weight: 900; color: #141414; }
.vs em { display: block; margin-top: 10px; font-style: normal; font-size: 38px; font-weight: 700; color: #777; }
.poli { left: 220px; } .reel { left: 1060px; border-color: #ff3d1f; } .reel em { color: #e8401f; }
#fade { left: 0; top: 0; width: 1920px; height: 1080px; background: #fff; z-index: 50; }
"""

JS_HEAD = """
window.__timelines = window.__timelines || {};
const tl = gsap.timeline({ paused: true });
const HIDE = [];
const FT = (sel, from, to, at) => tl.fromTo(sel, from, { ...to, immediateRender: false }, at);
const IN = (sel, from, to, at) => { HIDE.push(...[].concat(sel)); return FT(sel, { ...from, autoAlpha: 0 }, { ...to, autoAlpha: 1 }, at); };
const word = (sel, at, d = 0.28) => IN(sel, { y: -40, scale: 1.3, filter: "blur(12px)" }, { y: 0, scale: 1, filter: "blur(0px)", duration: d, ease: "power3.out" }, at);
const words = (list, at, gap = 0.11) => list.forEach((s, i) => word(s, at + i * gap));
const pop = (sel, at) => IN(sel, { scale: 0.3, rotation: -20 }, { scale: 1, rotation: 0, duration: 0.45, ease: "back.out(2)" }, at);
const bigIn = (sel, at) => IN(sel, { scale: 2.0, filter: "blur(16px)" }, { scale: 1, filter: "blur(0px)", duration: 0.35, ease: "power4.out" }, at);
const drop = (sel, at) => IN(sel, { y: -260, scale: 1.4 }, { y: 0, scale: 1, duration: 0.45, ease: "bounce.out" }, at);
const stamp = (sel, at) => IN(sel, { scale: 2.6, rotation: -14 }, { scale: 1, rotation: -4, duration: 0.3, ease: "power4.in" }, at);
const float = (sel, at, d, y = -16) => FT(sel, { y: 0 }, { y: y, duration: d / 2, yoyo: true, repeat: 1, ease: "sine.inOut" }, at);
"""

SWOOSH = ['<svg class="swoosh" viewBox="0 0 2320 1880"><path d="M300 -100 C 900 700, 1400 900, 2300 1900" fill="none" stroke="#d9d4cc" stroke-width="200" stroke-linecap="round"/></svg>',
          '<svg class="swoosh" viewBox="0 0 2320 1880"><path d="M2100 -100 C 1500 700, 900 1000, 100 1900" fill="none" stroke="#d9d4cc" stroke-width="200" stroke-linecap="round"/></svg>']


def build(vid):
    titre, scenes = VIDEOS[vid]
    out = os.path.join(ROOT, vid)
    os.makedirs(os.path.join(out, "renders"), exist_ok=True)
    if os.path.exists(os.path.join(out, "assets")):
        shutil.rmtree(os.path.join(out, "assets"))
    shutil.copytree(os.path.join(ROOT, "commun"), os.path.join(out, "assets"))
    t = 0.0
    built, sfx = [], []
    for n, (kind, d, p) in enumerate(scenes, 1):
        bg = "white" if n % 2 else "cream"
        sc = Scene(n, t, d, bg)
        scene_html(sc, kind, p)
        built.append(sc)
        sfx.append((t, "whoosh" if n > 1 else "whoosh-cinematic", 0.3))
        sfx += sc.sfx
        t += d
    total = round(t + 0.4, 2)
    body = []
    for sc in built:
        sw = SWOOSH[sc.n % 2] if sc.bg == "cream" else ""
        body.append(f'<div class="scene {sc.bg}" id="s{sc.n}"><div class="cam" id="k{sc.n}"><div class="grid"></div>{sw}\n' + "\n".join(sc.h) + "\n</div></div>")
    sc_list = [[f"#s{sc.n}", f"#k{sc.n}", round(sc.a, 2), round(sc.d if sc is not built[-1] else sc.d + 0.4, 2)] for sc in built]
    js = [JS_HEAD,
          f"const SC = {json.dumps(sc_list)};",
          """SC.forEach(([s, c, a, d], i) => {
  HIDE.push(s);
  tl.set(s, { autoAlpha: 1 }, a);
  if (i !== SC.length - 1) tl.set(s, { autoAlpha: 0 }, a + d);
  FT(c, { scale: 1.12 }, { scale: 1.0, duration: 0.45, ease: "expo.out" }, a);
  FT(c, { rotation: 0, x: 0 }, { rotation: i % 2 ? 0.6 : -0.6, x: i % 2 ? -24 : 24, duration: d, ease: "sine.inOut" }, a);
});"""]
    for sc in built:
        js += sc.js
    js += [f'FT("#fade", {{ opacity: 0 }}, {{ opacity: 1, duration: 0.4 }}, {total - 0.4:.2f});',
           'gsap.set(HIDE, { autoAlpha: 0 });', 'gsap.set("#s1", { autoAlpha: 1 });', 'gsap.set("#fade", { opacity: 0 });',
           'window.__timelines["main"] = tl;']
    page = f"""<!doctype html>
<html lang="fr" data-resolution="landscape">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=1920, height=1080" />
<title>{E(titre)}</title>
<script src="assets/gsap.min.js"></script>
<style>{CSS}</style>
</head>
<body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{total}" data-width="1920" data-height="1080">
{chr(10).join(body)}
<div class="ab" id="fade"></div>
<audio id="mix" src="assets/audio/mix.wav" data-start="0" data-duration="{total}" data-track-index="1" data-volume="1"></audio>
</div>
<script>
{chr(10).join(js)}
</script>
</body>
</html>
"""
    open(os.path.join(out, "index.html"), "w").write(page)
    for f, c in [("meta.json", {"id": f"guide-{vid}", "name": f"Guide vidéo {vid} : {titre}"}),
                 ("package.json", {"name": f"guide-{vid}", "private": True, "type": "module",
                                   "scripts": {"check": "npx --yes hyperframes@0.8.77 check", "render": "npx --yes hyperframes@0.8.77 render"}})]:
        json.dump(c, open(os.path.join(out, f), "w"), ensure_ascii=False, indent=2)
    mix(out, total, sfx)
    print(vid, titre, total, "s")


def mix(out, dur, sfx):
    os.makedirs(os.path.join(out, "assets", "audio"), exist_ok=True)
    dst = os.path.join(out, "assets", "audio", "mix.wav")
    sfx = sorted(sfx)[:60]
    inputs = ["-stream_loop", "-1", "-i", MUSIC]
    fl = [f"[0:a]aresample=44100,aformat=channel_layouts=stereo,atrim=duration={dur},volume=0.55,afade=t=in:d=0.6,afade=t=out:st={dur - 1.5}:d=1.5[mus]"]
    labels = ["[mus]"]
    for i, (t, name, vol) in enumerate(sfx):
        inputs += ["-i", os.path.join(SFX_DIR, f"{name}.mp3")]
        ms = int(t * 1000)
        extra = ",atrim=duration=1.2" if name == "typing" else ""
        fl.append(f"[{i + 1}:a]aresample=44100,aformat=channel_layouts=stereo{extra},volume={vol},adelay={ms}|{ms}[s{i}]")
        labels.append(f"[s{i}]")
    fl.append("".join(labels) + f"amix=inputs={len(labels)}:normalize=0:duration=first,apad,atrim=duration={dur},loudnorm=I=-16:TP=-1.5:LRA=11[out]")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error"] + inputs + ["-filter_complex", ";".join(fl), "-map", "[out]", "-ar", "44100", dst], check=True)


if __name__ == "__main__":
    for v in (sys.argv[1:] or list(VIDEOS)):
        build(v)
