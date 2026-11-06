"""Vidéo 13 h jour 1 (Cuisine) : calage sur la voix, mixage et composition HyperFrames."""
import json, os, re, subprocess

ROOT = os.path.dirname(os.path.abspath(__file__))
A = os.path.join(ROOT, "assets")
VOICE = f"{A}/audio/voix.mp3"
MUSIC = f"{A}/audio/musique.wav"

SCRIPT = [
    "Tu sais cuisiner ?",
    "Tu peux en faire un produit qui se vend.",
    "Je te montre comment,",
    "avec un exemple précis.",
    "Imagine Nadine,",
    "24 ans,",
    "étudiante.",
    "Elle se trouve trop mince,",
    "et elle en souffre.",
    "Elle voudrait prendre du poids sainement,",
    "avec ce qu'on trouve au marché.",
    "Mais elle ne sait pas quoi manger, ni en quelle quantité.",
    "Et toi,",
    "tu as la réponse à son problème.",
    "Tu peux lui vendre un livre de recettes,",
    "avec un plan de repas sur 4 semaines et la liste de courses.",
    "Elle sait quoi cuisiner chaque jour.",
    "Ou un défi de 30 jours dans un groupe WhatsApp :",
    "une recette par jour, et tu la suis.",
    "Et pour créer ça, il te faut seulement trois choses.",
    "Canva pour mettre ton livre en page.",
    "Ton téléphone pour photographier tes plats.",
    "Et Google Docs pour écrire tes recettes et ta liste de courses.",
    "Et ce n'est pas tout : quand ton livre se vendra, d'autres cuisinières voudront savoir comment tu l'as fait.",
    "Commente ta compétence :",
    "je te réponds en privé avec le guide pour la transformer en revenu.",
]
NONE = {1, 25}          # le texte est déjà le visuel
ACCENT = {"vend.", "précis.", "Nadine,", "souffre.", "marché.", "réponse", "recettes,", "WhatsApp", "trois",
          "Canva", "téléphone", "Docs", "cuisinières", "compétence", "revenu."}
SPOKEN_LEN = {"24": 12, "4": 6, "30": 6}   # longueur parlée des nombres écrits en chiffres


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
    toks = [t for t in line.split(" ") if t]
    merged = []
    for t in toks:
        if merged and t in (":", "?", "!"):
            merged[-1] += " " + t
        else:
            merged.append(t)
    weights = [SPOKEN_LEN.get(t.strip(",.:?"), len(t.strip(",.:?' "))) + 2 for t in merged]
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
                                   "acc": w[1] in ACCENT} for w in grp]})
    for c, nxt in zip(out, out[1:]):
        c["hide"] = round(min(nxt["start"], c["end"] + 0.45), 3)
    out[-1]["hide"] = DUR - 0.2
    return out


CAPS = chunks()

T = {
    "produit": word(2, "produit")[2], "vend": word(2, "vend")[2],
    "montre": seg(3)[0], "exemple": word(4, "exemple")[2],
    "nadine": seg(5)[0], "age": seg(6)[0], "etud": seg(7)[0], "mince": word(8, "mince")[2], "souffre": word(9, "souffre")[2],
    "poids": seg(10)[0], "marche": seg(11)[0], "quoi": word(12, "quoi")[2], "quant": word(12, "quantité")[2],
    "toi": seg(13)[0], "rep": word(14, "réponse")[2],
    "livre": seg(15)[0], "recettes": word(15, "recettes")[2], "plan": word(16, "plan")[2], "sem": word(16, "semaines")[2],
    "courses": word(16, "courses")[2], "jour": seg(17)[0], "chaque": word(17, "chaque")[2],
    "defi": seg(18)[0], "wa": word(18, "WhatsApp")[2], "rec": seg(19)[0], "suis": word(19, "suis")[2],
    "tools": seg(20)[0], "trois": word(20, "trois")[2],
    "canva": seg(21)[0], "tel": seg(22)[0], "docs": seg(23)[0], "ecrire": word(23, "écrire")[2], "courses2": word(23, "courses")[2],
    "boucle": seg(24)[0], "vendra": word(24, "vendra")[2], "cuisinieres": word(24, "cuisinières")[2], "comment": word(24, "comment")[2],
    "cta": seg(25)[0], "rep2": seg(26)[0], "prive": word(26, "privé")[2], "guide": word(26, "guide")[2], "revenu": word(26, "revenu")[2],
    "end": DUR,
}
T = {k: round(v, 3) for k, v in T.items()}

SFX = [
    (0.05, "whoosh-short", 0.40), (0.15, "pop", 0.35), (T["produit"], "pop", 0.35), (T["vend"] + 0.2, "sparkle", 0.35),
    (T["montre"] - 0.3, "whoosh", 0.40), (T["exemple"], "pop", 0.35),
    (T["nadine"] - 0.3, "whoosh-short", 0.40), (T["nadine"] + 0.1, "pop", 0.30), (T["age"], "click", 0.35), (T["etud"], "click", 0.35),
    (T["mince"], "pop", 0.32), (T["souffre"], "impact-bass-1", 0.35),
    (T["poids"] - 0.3, "whoosh-short", 0.40), (T["marche"], "whoosh-short", 0.35), (T["quoi"], "pop", 0.32), (T["quant"], "pop", 0.32),
    (T["toi"] - 0.1, "impact-bass-2", 0.40), (T["rep"], "sparkle", 0.35),
    (T["livre"] - 0.25, "whoosh", 0.40), (T["recettes"], "pop", 0.30), (T["plan"], "click", 0.35), (T["courses"], "pop", 0.32),
    (T["chaque"], "chime", 0.30),
    (T["defi"] - 0.25, "whoosh-short", 0.40), (T["rec"], "notification", 0.30), (T["rec"] + 0.5, "notification", 0.22), (T["suis"], "ping", 0.30),
    (T["tools"] - 0.25, "whoosh", 0.40), (T["trois"], "impact-bass-1", 0.35),
    (T["canva"], "click", 0.40), (T["tel"], "click", 0.40), (T["docs"], "click", 0.40), (T["ecrire"], ("typing", 0, 1.6), 0.22),
    (T["boucle"] - 0.25, "whoosh-short", 0.40), (T["vendra"], "impact-bass-2", 0.40), (T["cuisinieres"], "whoosh-short", 0.35), (T["comment"], "pop", 0.32),
    (T["cta"] - 0.2, "whoosh", 0.40), (T["cta"] + 0.6, ("typing", 0, 1.0), 0.25), (T["prive"], "notification", 0.40), (T["guide"], "pop", 0.35),
    (T["revenu"], "sparkle", 0.35),
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
    rep = {"__STAR__": STAR, "__T__": json.dumps(T), "__CAPS__": json.dumps(CAPS, ensure_ascii=False), "__DUR__": str(DUR),
           "__TOI_START__": str(round(T["toi"] - 0.3, 3)), "__CANVA_START__": str(round(T["tools"] - 0.2, 3))}
    for k, v in rep.items():
        html = html.replace(k, v)
    open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8").write(html)


if __name__ == "__main__":
    mix()
    build_html()
    json.dump({"segments": SEGS, "T": T}, open(f"{A}/audio/timings.json", "w"), indent=1)
    print("ok", DUR, "s,", len(CAPS), "groupes de sous-titres,", len(SFX), "effets")
    print(json.dumps(T))
