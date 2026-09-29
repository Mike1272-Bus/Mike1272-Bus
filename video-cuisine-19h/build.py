"""Vidéo 19 h jour 1 (Cuisine) : calage sur la voix, mixage et composition HyperFrames."""
import json, os, re, subprocess

ROOT = os.path.dirname(os.path.abspath(__file__))
A = os.path.join(ROOT, "assets")
VOICE = f"{A}/audio/voix.mp3"
MUSIC = f"{A}/audio/musique.wav"

SCRIPT = [
    "Ce qu'on ne vous dit pas sur les produits digitaux :",
    "vous voulez créer un produit pour tout le monde ?",
    "Au final, personne ne l'achètera.",
    "Je vais vous montrer pourquoi, avec un exemple tout simple.",
    "Et la seule question à vous poser avant de créer le vôtre.",
    "Vous dites :",
    "« Mes recettes de cuisine ».",
    "Personne ne se sent concerné.",
    "C'est parce que tout le monde mange, oui.",
    "Mais personne ne se dit :",
    "« Ça, c'est pour moi. »",
    "Maintenant, regardez ce qui se passe quand on change une seule phrase.",
    "Si vous dites plutôt :",
    "« Des recettes pour les femmes qui veulent prendre du poids sainement ».",
    "Nadine, en train de faire défiler son téléphone, s'arrête tout de suite.",
    "Parce qu'on parle d'elle.",
    "Et ce petit changement fait une grosse différence au moment de vendre.",
    "Plus vous parlez à une personne précise, plus elle se sent concernée.",
    "Et plus elle se sent concernée, plus elle a envie d'acheter.",
    "Alors avant de créer votre produit,",
    "posez-vous une seule question :",
    "à qui exactement je le vends ?",
    "Une fois que vous avez la réponse, il reste à savoir si ces personnes sont prêtes à payer.",
    "Dans mon guide, il y a un plan de 7 jours",
    "pour tester votre idée sans budget pub.",
    "Écrivez « EBOOK » en commentaire,",
    "je vous réponds et je vous accompagne.",
]
NONE = {1, 26}          # le texte est déjà le visuel
ACCENT = {"monde ?", "personne", "simple.", "question", "« Mes", "cuisine ».", "concerné.", "moi. »", "phrase.", "sainement ».", "Nadine,",
          "d'elle.", "vendre.", "précise,", "d'acheter.", "exactement", "vends ?", "payer.", "7", "pub.", "« EBOOK »", "accompagne."}
SPOKEN_LEN = {"7": 4, "« EBOOK »": 5}


def duration(f):
    return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f],
                                capture_output=True, text=True).stdout)


def speech_segments():
    out = subprocess.run(["ffmpeg", "-hide_banner", "-i", VOICE, "-af", "silencedetect=noise=-35dB:d=0.3", "-f", "null", "-"],
                         capture_output=True, text=True).stderr
    v = [float(x) for x in re.findall(r"silence_(?:start|end): ([0-9.]+)", out)]
    starts = [0.0] + v[1::2]
    ends = v[0::2] + [duration(VOICE)]
    segs = [(a, b) for a, b in zip(starts, ends) if b - a > 0.05]
    assert len(segs) == len(SCRIPT), (len(segs), len(SCRIPT))
    return segs


SEGS = speech_segments()
DUR = round(SEGS[-1][1] + 1.6, 2)

WORDS = []
for si, ((a, b), line) in enumerate(zip(SEGS, SCRIPT)):
    toks = [t for t in line.replace("« ", "«").replace(" »", "»").split(" ") if t]
    toks = [t.replace("«", "« ").replace("»", " »") for t in toks]
    merged = []
    for t in toks:
        if merged and t.strip() in (":", "?", "!"):
            merged[-1] += " " + t
        else:
            merged.append(t)
    weights = [SPOKEN_LEN.get(t.strip(",.:? "), len(t.strip(",.:?'«» "))) + 2 for t in merged]
    total, t = sum(weights), a
    for tok, w in zip(merged, weights):
        d = (b - a) * w / total
        WORDS.append((si, tok, t, t + d))
        t += d


def seg(i):
    return SEGS[i - 1]


def word(si, needle, which=0):
    return [w for w in WORDS if w[0] == si - 1 and needle.lower() in w[1].lower()][which]


def chunks():
    out = []
    for si in range(1, len(SCRIPT) + 1):
        if si in NONE:
            continue
        ws = [w for w in WORDS if w[0] == si - 1]
        n = max(1, round(len(ws) / 6 + 0.49))
        per = -(-len(ws) // n)
        for k in range(0, len(ws), per):
            grp = ws[k:k + per]
            out.append({"start": round(grp[0][2], 3), "end": round(grp[-1][3], 3),
                        "words": [{"t": w[1], "s": round(w[2], 3), "e": round(w[3], 3),
                                   "acc": w[1].rstrip(",") in ACCENT or w[1] in ACCENT} for w in grp]})
    for c, nxt in zip(out, out[1:]):
        c["hide"] = round(min(nxt["start"], c["end"] + 0.45), 3)
    out[-1]["hide"] = DUR - 0.2
    return out


CAPS = chunks()

T = {
    "tlm": word(2, "monde")[2], "final": seg(3)[0], "personne": word(3, "personne")[2], "ach": word(3, "l'achètera")[2],
    "montrer": seg(4)[0], "exemple": word(4, "exemple")[2], "question": word(5, "question")[2],
    "dites": seg(6)[0], "mes": seg(7)[0], "concerne": word(8, "concerné")[2], "mange": word(9, "mange")[2], "pasmoi": seg(10)[0], "moi": seg(11)[0],
    "maintenant": seg(12)[0], "phrase": word(12, "phrase")[2],
    "plutot": seg(13)[0], "postB": seg(14)[0], "femmes": word(14, "femmes")[2], "sainement": word(14, "sainement")[2],
    "nadine": seg(15)[0], "defiler": word(15, "défiler")[2], "arrete": word(15, "s'arrête")[2], "delle": seg(16)[0],
    "changement": seg(17)[0], "difference": word(17, "différence")[2], "vendre": word(17, "vendre")[2],
    "precise": word(18, "précise")[2], "concernee": word(18, "concernée")[2], "envie": word(19, "envie")[2], "acheter": word(19, "d'acheter")[2],
    "alors": seg(20)[0], "question2": seg(21)[0], "qui": seg(22)[0], "vends": word(22, "vends")[2],
    "reponse": word(23, "réponse")[2], "payer": word(23, "payer")[2],
    "cta": seg(24)[0], "sept": word(24, "7")[2], "pub": word(25, "pub")[2],
    "ebook": seg(26)[0], "ebookWord": word(26, "EBOOK")[2], "accomp": word(27, "accompagne")[2],
    "end": DUR,
}
T = {k: round(v, 3) for k, v in T.items()}

SFX = [
    (0.05, "whoosh-short", 0.40), (0.2, "impact-bass-2", 0.40), (T["tlm"], "pop", 0.35), (T["tlm"] + 0.3, "sparkle", 0.30),
    (T["personne"], "error", 0.35), (T["ach"], "impact-bass-1", 0.40),
    (T["montrer"] - 0.3, "whoosh", 0.40), (T["exemple"], "pop", 0.35), (T["question"], "pop", 0.35),
    (T["dites"] - 0.3, "whoosh-short", 0.40), (T["mes"], "click", 0.35), (T["concerne"], "error", 0.30), (T["mange"], "pop", 0.32), (T["moi"], "glitch-1", 0.30),
    (T["maintenant"] - 0.2, "whoosh", 0.40), (T["phrase"], "click", 0.35),
    (T["plutot"] - 0.2, "whoosh-short", 0.40), (T["postB"], "pop", 0.35), (T["sainement"], "sparkle", 0.35),
    (T["nadine"], "whoosh-short", 0.35), (T["arrete"], "impact-bass-2", 0.45), (T["delle"], "ping", 0.35),
    (T["changement"] - 0.2, "whoosh", 0.40), (T["difference"], "riser", 0.25), (T["vendre"], "chime", 0.35),
    (T["precise"] - 0.2, "whoosh-short", 0.40), (T["precise"], "pop", 0.32), (T["concernee"], "pop", 0.32), (T["acheter"], "sparkle", 0.35),
    (T["alors"] - 0.2, "whoosh", 0.40), (T["qui"], "impact-bass-1", 0.40),
    (T["reponse"], "ping", 0.35), (T["payer"], "pop", 0.35),
    (T["cta"] - 0.3, "whoosh", 0.40), (T["sept"], "pop", 0.35), (T["pub"], "pop", 0.35),
    (T["ebook"] - 0.2, "whoosh-short", 0.40), (T["ebookWord"], ("typing", 0, 0.9), 0.25), (T["accomp"] + 0.3, "notification", 0.40),
]


def mix():
    inputs = ["-i", VOICE, "-i", MUSIC]
    fl = ["[0:a]aresample=44100,aformat=channel_layouts=stereo,highpass=f=70,asplit=2[vo][sc]",
          f"[1:a]atrim=duration={DUR},volume=0.5,afade=t=out:st={DUR - 1.5}:d=1.5[mus]",
          "[mus][sc]sidechaincompress=threshold=0.03:ratio=8:attack=20:release=350:makeup=1[musd]"]
    labels = []
    for i, (t, spec, vol) in enumerate(SFX):
        name, off, dur = (spec, 0, None) if isinstance(spec, str) else spec
        inputs += ["-i", f"{A}/sfx/{name}.mp3"]
        trim = f"atrim=start={off}" + (f":duration={dur}" if dur else "") + ",asetpts=PTS-STARTPTS,"
        d = max(0, int(t * 1000))
        fl.append(f"[{i+2}:a]aresample=44100,aformat=channel_layouts=stereo,{trim}volume={vol},adelay={d}|{d}[s{i}]")
        labels.append(f"[s{i}]")
    fl.append("[vo][musd]" + "".join(labels) + f"amix=inputs={2+len(labels)}:normalize=0:duration=longest,apad,atrim=duration={DUR}[mix]")
    fl.append("[mix]loudnorm=I=-14:TP=-1.5:LRA=11[out]")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error"] + inputs +
                   ["-filter_complex", ";".join(fl), "-map", "[out]", "-ar", "44100", f"{A}/audio/mix.wav"], check=True)


STAR = '<svg viewBox="0 0 100 100"><path d="M50 0 C54 38 62 46 100 50 C62 54 54 62 50 100 C46 62 38 54 0 50 C38 46 46 38 50 0Z"/></svg>'


def build_html():
    html = open(os.path.join(ROOT, "template.html.tpl"), encoding="utf-8").read()
    person = ('<div class="pp"><svg viewBox="0 0 100 114" fill="currentColor"><circle cx="50" cy="28" r="22"/>'
              '<path d="M12 112 C12 74 28 58 50 58 C72 58 88 74 88 112 Z"/></svg></div>')
    rep = {"__STAR__": STAR, "__T__": json.dumps(T), "__CAPS__": json.dumps(CAPS, ensure_ascii=False), "__DUR__": str(DUR),
           "__CROWD__": person * 24}
    for k, v in rep.items():
        html = html.replace(k, v)
    open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8").write(html)


if __name__ == "__main__":
    mix()
    build_html()
    json.dump({"segments": SEGS, "T": T}, open(f"{A}/audio/timings.json", "w"), indent=1)
    print("ok", DUR, "s,", len(CAPS), "groupes de sous-titres,", len(SFX), "effets")
    print(json.dumps(T))
