"""Montage final de la pub DigitalMikaelson : timings, mixage audio et composition HyperFrames."""
import json, os, re, subprocess

ROOT = os.path.dirname(os.path.abspath(__file__))
A = os.path.join(ROOT, "assets")
VOICE = f"{A}/audio/voix_pub_finale_x110.mp3"
MUSIC = f"{A}/audio/musique_fond_x110.wav"
DUR = 91.0

# ---------- 1. phrases de la voix (détection des pauses) ----------
SCRIPT = [
    "Vous avez déjà un savoir-faire qui vaut de l'argent.",
    "Vous ne le savez juste pas encore.",
    "Je vais vous expliquer exactement pourquoi,",
    "dans quelques secondes.",
    "Que vous soyez salarié, étudiant, ou sans emploi,",
    "vous savez faire quelque chose :",
    "cuisiner,",
    "coudre,",
    "parler une langue,",
    "tenir une comptabilité.",
    "Et quelqu'un,",
    "quelque part,",
    "a besoin d'apprendre exactement ça.",
    "Et pourtant...",
    "ce n'est même pas la partie la plus folle.",
    "Avec un produit digital, vous pouvez le lui enseigner",
    "à des milliers de kilomètres,",
    "sans jamais le rencontrer.",
    "Mon oncle David,",
    "menuisier,",
    "a transformé son savoir-faire",
    "en produit digital,",
    "sans budget pub.",
    "Mais ce n'est toujours pas le plus important.",
    "J'ai écrit le guide pour faire pareil.",
    "Dedans, je vous explique pourquoi le diplôme n'est pas nécessaire pour commencer.",
    "Comment vous faire connaître sur internet.",
    "Quelle forme donner à votre produit.",
    "Comment le fabriquer",
    "et le vendre avec ce que vous avez déjà.",
    "Et comment savoir en une semaine si des gens en veulent,",
    "sans dépenser un centime.",
    "En suivant le guide, vous saurez ce que vous vendez et à qui, vous aurez un premier produit, et vous saurez si des gens sont prêts à le payer.",
    "Pas de blabla, juste ce qu'il faut faire,",
    "concrètement.",
    "Et la meilleure partie ?",
    "Il suffit d'un message pour commencer.",
    "Cliquez sur",
    "« Envoyer un message »,",
    "écrivez-moi sur WhatsApp,",
    "et je vous accompagne.",
]


def speech_segments():
    out = subprocess.run(["ffmpeg", "-hide_banner", "-i", VOICE, "-af", "silencedetect=noise=-35dB:d=0.27", "-f", "null", "-"],
                         capture_output=True, text=True).stderr
    v = [float(x) for x in re.findall(r"silence_(?:start|end): ([0-9.]+)", out)]
    dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", VOICE],
                               capture_output=True, text=True).stdout)
    starts = [0.0] + v[1::2]
    ends = v[0::2] + [dur]
    segs = [(a, b) for a, b in zip(starts, ends) if b - a > 0.05]
    assert len(segs) == len(SCRIPT), (len(segs), len(SCRIPT))
    return segs


SEGS = speech_segments()

# ---------- 2. timing mot à mot ----------
WORDS = []  # (seg, text, start, end)
for si, ((a, b), line) in enumerate(zip(SEGS, SCRIPT)):
    toks = [t for t in line.replace("« ", "«").replace(" »", "»").split(" ") if t]
    toks = [t.replace("«", "« ").replace("»", " »") for t in toks]
    merged = []
    for t in toks:
        if merged and t.strip() in (":", "?", "!"):
            merged[-1] += " " + t
        else:
            merged.append(t)
    toks = merged
    weights = [len(t.strip("«» ,.:?")) + 2 for t in toks]
    total = sum(weights)
    t = a
    for tok, w in zip(toks, weights):
        d = (b - a) * w / total
        WORDS.append((si, tok, t, t + d))
        t += d


def seg(i):
    return SEGS[i - 1]


def word(si, needle, which=0):
    hits = [w for w in WORDS if w[0] == si - 1 and needle.lower() in w[1].lower()]
    return hits[which]


# ---------- 3. sous-titres (karaoké) ----------
BIG = {14, 15, 24, 36}          # boucles ouvertes : texte géant au centre
NONE = {34, 35}                 # signature : les mots sont déjà le visuel
ACCENT = {"l'argent.", "encore.", "secondes.", "folle.", "important.", "centime.", "WhatsApp,", "partie"}


def chunks():
    out = []
    for si in range(1, len(SCRIPT) + 1):
        if si in NONE:
            continue
        ws = [w for w in WORDS if w[0] == si - 1]
        mode = "big" if si in BIG else "low"
        size = 6 if mode == "low" else 5
        n = max(1, round(len(ws) / size + 0.49))
        per = -(-len(ws) // n)
        for k in range(0, len(ws), per):
            grp = ws[k:k + per]
            out.append({
                "mode": mode,
                "start": round(grp[0][2], 3),
                "end": round(grp[-1][3], 3),
                "words": [{"t": w[1], "s": round(w[2], 3), "e": round(w[3], 3),
                           "acc": w[1].strip("«» ") in ACCENT} for w in grp],
            })
    # chaque groupe reste affiché jusqu'au suivant (max 0,45 s de blanc)
    for c, nxt in zip(out, out[1:]):
        c["hide"] = round(min(nxt["start"], c["end"] + 0.45), 3)
    out[-1]["hide"] = DUR - 0.3
    return out


CAPS = chunks()

# ---------- 4. temps clés des scènes ----------
T = {
    "hookFlip": seg(2)[0],
    "argent": word(1, "argent")[2],
    "promise": seg(3)[0] - 0.3,
    "promiseEnd": seg(5)[0] - 0.25,
    "salarie": word(5, "salarié")[2],
    "etudiant": word(5, "étudiant")[2],
    "sansEmploi": word(5, "sans")[2],
    "p1b": seg(6)[0] - 0.15,
    "cuisiner": seg(7)[0], "coudre": seg(8)[0], "langue": seg(9)[0], "compta": seg(10)[0],
    "p1c": seg(11)[0] - 0.1, "quelquePart": seg(12)[0], "besoin": seg(13)[0],
    "b1": seg(14)[0] - 0.25, "b1b": seg(15)[0],
    "p2": seg(16)[0] - 0.2, "km": seg(17)[0], "distB": seg(18)[0] - 0.1,
    "david": seg(19)[0] - 0.2, "menuisier": seg(20)[0], "budget": seg(23)[0],
    "b2": seg(24)[0] - 0.25,
    "guide": seg(25)[0] - 0.2,
    "step1": seg(26)[0], "step2": seg(27)[0], "step3": seg(28)[0], "step4": seg(29)[0], "step5": seg(31)[0],
    "check": seg(33)[0] - 0.2,
    "tick1": word(33, "qui,")[3], "tick2": word(33, "produit,")[3], "tick3": word(33, "payer")[3] - 0.2,
    "sig": seg(34)[0] - 0.15, "sig2": word(34, "juste")[2], "sig3": seg(35)[0],
    "b3": seg(36)[0] - 0.25, "bubble": seg(37)[0],
    "cta": seg(38)[0] - 0.2, "ctaCard": seg(38)[0] - 0.2 + 3.3, "whatsapp": word(40, "WhatsApp")[2],
    "end": DUR,
}
T = {k: round(v, 3) for k, v in T.items()}

# ---------- 5. effets sonores et mixage ----------
SFX = [
    (0.00, "whoosh-short", 0.45), (0.15, "pop", 0.32), (0.35, "pop", 0.32), (0.55, "pop", 0.32),
    (T["argent"] - 0.05, "sparkle", 0.40),
    (T["hookFlip"] - 0.05, "whoosh", 0.40),
    (T["promise"] - 0.15, "whoosh-short", 0.40),
    (T["promiseEnd"] - 3.6, ("riser", 6.43, 3.6), 0.30),
    (seg(5)[0] - 0.02, "impact-bass-1", 0.50),
    (T["salarie"], "pop", 0.32), (T["etudiant"], "pop", 0.32), (T["sansEmploi"], "pop", 0.32),
    (T["p1b"] - 0.1, "whoosh-short", 0.38),
    (T["coudre"] - 0.05, "pop", 0.32), (T["langue"] - 0.05, "pop", 0.32), (T["compta"] - 0.05, "pop", 0.32),
    (T["quelquePart"], "whoosh-short", 0.25), (T["besoin"], "ping", 0.30),
    (seg(14)[0] - 0.03, "impact-bass-2", 0.45),
    (T["p2"], "whoosh-cinematic", 0.35), (T["distB"], "whoosh-short", 0.35),
    (T["david"], "whoosh-short", 0.35), (T["menuisier"], "chime", 0.28), (T["budget"], "pop", 0.40),
    (seg(24)[0] - 0.03, "impact-bass-2", 0.45),
    (T["guide"], "whoosh", 0.35),
    (T["step1"], "pop", 0.30), (T["step2"], "pop", 0.30), (T["step3"], "pop", 0.30),
    (T["step4"], "pop", 0.30), (T["step5"], "pop", 0.30),
    (T["tick1"], "click", 0.40), (T["tick2"], "click", 0.40), (T["tick3"], "click", 0.40),
    (T["sig"] + 0.1, "impact-bass-1", 0.35), (T["sig2"], "pop", 0.30), (T["sig3"], "pop", 0.35),
    (T["b3"] - 0.1, ("riser", 6.2, 3.83), 0.30),
    (T["bubble"] + 0.1, ("typing", 0, 1.3), 0.22),
    (seg(38)[0] - 0.03, "impact-bass-1", 0.50),
    (T["whatsapp"] + 0.25, "notification", 0.40),
    (seg(41)[1] + 0.1, "ping", 0.35),
]


def mix():
    inputs = ["-i", VOICE, "-i", MUSIC]
    fl = ["[0:a]aresample=44100,aformat=channel_layouts=stereo,highpass=f=70,asplit=2[vo][sc]",
          "[1:a]volume=0.55[mus]",
          "[mus][sc]sidechaincompress=threshold=0.03:ratio=8:attack=20:release=350:makeup=1[musd]"]
    labels = []
    for i, (t, spec, vol) in enumerate(SFX):
        name, off, dur = (spec, 0, None) if isinstance(spec, str) else spec
        inputs += ["-i", f"{A}/sfx/{name}.mp3"]
        trim = f"atrim=start={off}" + (f":duration={dur}" if dur else "") + ",asetpts=PTS-STARTPTS,"
        d = max(0, int(t * 1000))
        fl.append(f"[{i+2}:a]aresample=44100,aformat=channel_layouts=stereo,{trim}volume={vol},adelay={d}|{d}[s{i}]")
        labels.append(f"[s{i}]")
    fl.append("[vo][musd]" + "".join(labels) + f"amix=inputs={2+len(labels)}:normalize=0:duration=longest,atrim=duration={DUR}[mix]")
    fl.append("[mix]loudnorm=I=-14:TP=-1.5:LRA=11[out]")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error"] + inputs +
                   ["-filter_complex", ";".join(fl), "-map", "[out]", "-ar", "44100", f"{A}/audio/mix_final.wav"], check=True)


# ---------- 6. composition ----------
def clip_len(name):
    return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0",
                                 f"{A}/clips/{name}.mp4"], capture_output=True, text=True).stdout)


def video_card(cid, name, start, end, label=None, cls="vcard"):
    """Carte avec poster (dernière image) sous la vidéo : pas de trou quand l'extrait est plus court que la scène."""
    ln = clip_len(name)
    dur = round(min(end - start, ln - 0.05), 3)
    lab = f'<div class="tag" id="{cid}-tag">{label}</div>' if label else ""
    return (f'<div class="{cls}" id="{cid}"><div class="inner">'
            f'<img class="poster" src="assets/clips/{name}_last.jpg" />'
            f'<video id="{cid}-v" src="assets/clips/{name}.mp4" data-start="{round(start, 3)}" data-duration="{dur}" '
            f'data-track-index="2" muted playsinline></video>{lab}</div></div>')


STAR = '<svg viewBox="0 0 100 100"><path d="M50 0 C54 38 62 46 100 50 C62 54 54 62 50 100 C46 62 38 54 0 50 C38 46 46 38 50 0Z"/></svg>'
ICON_JOB = '<svg viewBox="0 0 100 100"><rect x="15" y="38" width="70" height="46" rx="6"/><path d="M38 38 V28 a6 6 0 0 1 6 -6 h12 a6 6 0 0 1 6 6 v10"/><line x1="15" y1="58" x2="85" y2="58"/></svg>'
ICON_STUDENT = '<svg viewBox="0 0 100 100"><path d="M6 40 L50 20 L94 40 L50 60 Z"/><path d="M28 48 V70 c0 6 10 12 22 12 s22 -6 22 -12 V48"/><path d="M94 40 V62"/></svg>'
ICON_SEARCH = '<svg viewBox="0 0 100 100"><circle cx="44" cy="44" r="24"/><line x1="62" y1="62" x2="84" y2="84"/></svg>'


def build_html():
    cards_p1 = "".join([
        video_card("k1", "cuisiner", T["p1b"], T["b1"], "Cuisiner", "vcard stack"),
        video_card("k2", "coudre", T["coudre"] - 0.35, T["b1"], "Coudre", "vcard stack"),
        video_card("k3", "langue", T["langue"] - 0.35, T["b1"], "Parler une langue", "vcard stack"),
        video_card("k4", "comptabilite", T["compta"] - 0.35, T["b1"], "Comptabilité", "vcard stack"),
    ])
    p2 = (video_card("d1", "distance_a", T["p2"], T["david"], None, "vcard big") +
          video_card("d2", "distance_b", T["distB"] - 0.2, T["david"], None, "vcard big") +
          video_card("dv", "david", T["david"], T["b2"], None, "vcard big"))
    cta = video_card("cv", "cta", T["cta"], T["ctaCard"], None, "vcard big")
    html = open(os.path.join(ROOT, "template_final.html.tpl"), encoding="utf-8").read()
    html = (html.replace("__CARDS_P1__", cards_p1).replace("__P2__", p2).replace("__CTA__", cta)
                .replace("__STAR__", STAR).replace("__ICON_JOB__", ICON_JOB)
                .replace("__ICON_STUDENT__", ICON_STUDENT).replace("__ICON_SEARCH__", ICON_SEARCH)
                .replace("__T__", json.dumps(T)).replace("__CAPS__", json.dumps(CAPS, ensure_ascii=False))
                .replace("__DUR__", str(DUR)))
    open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8").write(html)


if __name__ == "__main__":
    mix()
    build_html()
    json.dump({"segments": SEGS, "T": T, "sfx": [(t, s if isinstance(s, str) else s[0], v) for t, s, v in SFX]},
              open(f"{A}/audio/timings_final.json", "w"), indent=1, ensure_ascii=False)
    print("ok", len(CAPS), "groupes de sous-titres,", len(SFX), "effets")
