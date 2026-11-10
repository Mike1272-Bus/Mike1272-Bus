"""Vidéo 13 h Excel + IA (Jonathan) : calage sur la voix accélérée, mixage et composition HyperFrames."""
import functools, json, os, re, subprocess

ROOT = os.path.dirname(os.path.abspath(__file__))
A = os.path.join(ROOT, "assets")
VOICE = f"{A}/audio/voix.mp3"
MUSIC = f"{A}/audio/musique.wav"

TEXT = """Tu as des bases en Excel ? Des grandes entreprises paieraient pour ce que tu sais faire. Je te montre comment Jonathan peut transformer ce savoir-faire en revenu, uniquement avec l'IA. Jonathan est étudiant. Il connaît les bases d'Excel, rien de plus. Pendant ce temps, dans une société de distribution qui a cinq dépôts à Kinshasa, le responsable des ventes passe deux jours chaque semaine à rassembler les chiffres de chaque dépôt pour son rapport au directeur. Ce rapport, Jonathan peut le faire à sa place. Sans être un expert. Il lui crée un tableau de bord : chaque dépôt entre ses ventes, et les graphiques se mettent à jour tout seuls. Le directeur voit d'un coup quel dépôt vend le plus et où le stock manque. Et le plus fou, c'est que Jonathan peut le faire avec l'intelligence artificielle. Il lui suffit de décrire ce qu'il veut, et l'IA l'aide à construire les formules et les graphiques. Mais un tableau, il faut encore trouver à qui le vendre. Là aussi, l'IA l'aide. Elle lui trouve les sociétés de distribution du pays, la bonne personne à contacter, et elle l'aide à écrire son message. Et quand il aura fait quelques tableaux, d'autres étudiants voudront savoir comment il a fait. Si tu es comme Jonathan, que tu as des bases en Excel, et que tu es partant, alors tu as tout pour commencer ton business dès maintenant."""
NONE = set()
ACCENT = {"Excel ?", "entreprises", "revenu,", "l'IA.", "étudiant.", "plus.", "cinq", "Kinshasa,", "jours", "place.", "expert.", "bord :",
          "seuls.", "manque.", "fou,", "artificielle.", "graphiques.", "vendre.", "pays,", "message.", "étudiants", "partant,", "business",
          "maintenant."}
SPOKEN_LEN = {"24": 12}


def spoken(s):
    for k, v in {"IA": "ia", "l'IA": "lia"}.items():
        s = s.replace(k, v)
    return len(re.sub(r"[^\wÀ-ÿ]", "", s))


def duration(f):
    return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f],
                                capture_output=True, text=True).stdout)


def synthetic_segments():
    chunks = [c.strip() for c in re.split(r"(?<=[,.:?»])\s+(?!»)", TEXT) if c.strip()]
    out, t = [], 0.3
    for c in chunks:
        d = spoken(c) / 17.5
        out.append((t, t + d)); t += d + (0.45 if c[-1] in ".?»" else 0.25)
    return out


def speech_segments():
    if not os.path.exists(VOICE):
        return synthetic_segments()
    out = subprocess.run(["ffmpeg", "-hide_banner", "-i", VOICE, "-af", "silencedetect=noise=-35dB:d=0.25", "-f", "null", "-"],
                         capture_output=True, text=True).stderr
    v = [float(x) for x in re.findall(r"silence_(?:start|end): ([0-9.]+)", out)]
    starts = [0.0] + v[1::2]
    ends = v[0::2] + [duration(VOICE)]
    return [(a, b) for a, b in zip(starts, ends) if b - a > 0.05]


def align():
    chunks = [c.strip() for c in re.split(r"(?<=[,.:?»])\s+(?!»)", TEXT) if c.strip()]
    segs = speech_segments()
    L = [spoken(c) for c in chunks]
    rate = sum(L) / sum(b - a for a, b in segs)
    n, m = len(chunks), len(segs)

    @functools.lru_cache(None)
    def f(i, j):
        if i == n and j == m:
            return (0.0, ())
        if j == m:
            return (1e9, ())
        best = (1e9, ())
        D = segs[j][1] - segs[j][0]
        if D < 0.3:  # souffle ou bruit sans texte
            r = f(i, j + 1)
            best = (D * 4 + r[0], ((i, i),) + r[1])
        for k in range(i + 1, min(n, i + 5) + 1):
            d = sum(L[i:k]) / rate
            r = f(k, j + 1)
            c = (d - D) ** 2 / (D + 0.3) + r[0]
            if c < best[0]:
                best = (c, ((i, k),) + r[1])
        return best

    _, path = f(0, 0)
    lines = []
    for (i, k), (a, b) in zip(path, segs):
        if k > i:
            lines.append((" ".join(chunks[i:k]), a, b))
    return lines


LINES = align()
SCRIPT = [l[0] for l in LINES]
SEGS = [(l[1], l[2]) for l in LINES]
DUR = round(SEGS[-1][1] + 1.8, 2)

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
    weights = [spoken(t) + 2 for t in merged]
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
PUNCT = ",.:?!»« "


def w(needle, after=0.0, exact=False):
    n = needle.lower()
    for x in WORDS:
        tok = x[1].lower().strip(PUNCT)
        if x[2] >= after - 1e-6 and (tok == n if exact else n in x[1].lower()):
            return x[2]
    raise KeyError(needle)


def we(needle, after=0.0):
    return w(needle, after, exact=True)



T = {"end": DUR}
T["excel"] = w("Excel")
T["entreprises"] = w("entreprises")
T["paieraient"] = w("paieraient")
T["montre"] = w("montre")
T["jonathan1"] = w("Jonathan")
T["revenu"] = w("revenu")
T["ia"] = w("l'IA.")
T["etudiant"] = w("étudiant")
T["bases2"] = w("bases", T["etudiant"])
T["pendant"] = w("Pendant")
T["societe"] = w("société")
T["cinq"] = we("cinq")
T["kinshasa"] = w("Kinshasa")
T["responsable"] = w("responsable")
T["jours"] = w("jours")
T["rassembler"] = w("rassembler")
T["chaque1"] = w("chaque", T["rassembler"])
T["directeur"] = w("directeur")
T["ce_rapport"] = w("rapport,", T["directeur"])
T["place"] = w("place")
T["expert"] = w("expert")
T["cree"] = w("crée")
T["chaque2"] = w("chaque", T["cree"])
T["graph1"] = w("graphiques", T["cree"])
T["seuls"] = w("seuls")
T["voit"] = w("voit")
T["vend"] = we("vend", T["voit"])
T["stock"] = w("stock")
T["fou"] = w("fou")
T["intelligence"] = w("intelligence")
T["suffit"] = w("suffit")
T["decrire"] = w("décrire")
T["formules"] = w("formules")
T["graph2"] = w("graphiques", T["formules"])
T["mais"] = w("Mais")
T["vendre"] = w("vendre")
T["la_aussi"] = w("Là")
T["trouve"] = w("trouve", T["la_aussi"])
T["societes"] = w("sociétés")
T["personne"] = w("personne")
T["ecrire"] = we("écrire")
T["message"] = w("message")
T["quand"] = w("quand")
T["etudiants"] = w("étudiants")
T["comment2"] = w("comment", T["etudiants"])
T["si"] = we("Si")
T["bases3"] = w("bases", T["si"])
T["partant"] = w("partant")
T["tout"] = we("tout", T["partant"])
T["business"] = w("business")
T = {k: round(v, 3) for k, v in T.items()}

SFX = [
    (0.05, "whoosh-short", 0.40), (T["excel"], "pop", 0.32), (T["excel"] + 0.25, "pop", 0.28), (T["entreprises"], "impact-bass-1", 0.30),
    (T["paieraient"], "chime", 0.32), (T["montre"] - 0.2, "whoosh", 0.38), (T["revenu"], "sparkle", 0.32), (T["ia"], "pop", 0.30),
    (T["etudiant"] - 0.3, "whoosh-short", 0.35), (T["pendant"] - 0.2, "whoosh", 0.38), (T["cinq"], "pop", 0.26), (T["cinq"] + 0.2, "pop", 0.26),
    (T["kinshasa"], "ping", 0.30), (T["responsable"] - 0.2, "whoosh-short", 0.35), (T["jours"], "error", 0.26), (T["rassembler"], ("typing", 0, 1.0), 0.20),
    (T["ce_rapport"] - 0.2, "whoosh", 0.38), (T["expert"], "sparkle", 0.32),
    (T["cree"] - 0.2, "whoosh", 0.40), (T["chaque2"], "click", 0.30), (T["graph1"], "pop", 0.28), (T["seuls"], "chime", 0.30),
    (T["voit"] - 0.2, "whoosh-short", 0.35), (T["vend"], "ping", 0.30), (T["stock"], "error", 0.28),
    (T["fou"] - 0.1, "impact-bass-2", 0.35), (T["intelligence"], "sparkle", 0.32), (T["decrire"], ("typing", 0, 1.2), 0.22), (T["formules"], "pop", 0.28),
    (T["mais"] - 0.2, "whoosh", 0.38), (T["la_aussi"] - 0.2, "whoosh-short", 0.38), (T["societes"], ("typing", 0, 0.8), 0.20),
    (T["personne"], "ping", 0.30), (T["ecrire"], ("typing", 0, 1.0), 0.22), (T["message"], "notification", 0.35),
    (T["quand"] - 0.2, "whoosh-short", 0.35), (T["etudiants"], "pop", 0.28),
    (T["si"] - 0.2, "whoosh", 0.40), (T["bases3"], "pop", 0.30), (T["partant"], "pop", 0.30), (T["tout"], "riser", 0.30),
    (T["business"], "sparkle", 0.35), (DUR - 1.3, "chime", 0.32),
]

def mix():
    voice = VOICE
    if not os.path.exists(VOICE):  # voix provisoire : silence, en attendant la vraie voix
        voice = f"{A}/audio/silence.wav"
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "lavfi", "-i", "anullsrc=r=44100:cl=stereo", "-t", str(DUR), voice], check=True)
    inputs = ["-i", voice, "-i", MUSIC]
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
    man = ('<svg viewBox="0 0 100 114" fill="currentColor"><circle cx="50" cy="28" r="22"/>'
           '<path d="M12 112 C12 74 28 58 50 58 C72 58 88 74 88 112 Z"/></svg>')
    S = {
        "HOOK": (0.05, T["montre"] + 0.1), "BIB": (T["montre"] - 0.35, T["etudiant"] + 0.1),
        "JON": (T["jonathan1"] if False else T["etudiant"] - 0.9, T["pendant"] + 0.1),
        "DEP": (T["pendant"] - 0.35, T["responsable"] + 0.1), "RESP": (T["responsable"] - 0.35, T["ce_rapport"] + 0.1),
        "JON2": (T["ce_rapport"] - 0.35, T["cree"] + 0.1), "DASH": (T["cree"] - 0.35, T["voit"] + 0.1),
        "DIR": (T["voit"] - 0.35, T["fou"] + 0.1), "TAB": (T["chaque2"] - 0.3, T["voit"] + 0.1),
        "JON3": (T["quand"] - 0.35, T["si"] + 0.1),
    }
    rep = {"__STAR__": STAR, "__T__": json.dumps(T), "__CAPS__": json.dumps(CAPS, ensure_ascii=False), "__DUR__": str(DUR),
           "__MAN__": man, "__BARS__": "<i></i>" * 14,
           "__PROMPT__": "".join(f"<span>{c}</span>" for c in "Crée-moi un tableau de bord des ventes de mes 5 dépôts, avec des graphiques."),
           "__SEARCH__": "".join(f"<span>{c}</span>" for c in "Sociétés de distribution en RDC"),
           "__MSG__": "".join(f"<span>{c}</span>" for c in "Bonjour, j'ai créé un tableau de bord pour suivre les ventes de vos dépôts. Je vous montre ?"),
           "__TYPED__": "".join(f"<span>{c}</span>" for c in "EXCEL")}
    for k, (a, e) in S.items():
        rep[f"__S_{k}__"] = str(round(a, 3))
        rep[f"__D_{k}__"] = str(round(e - a, 3))
    for k, v in rep.items():
        html = html.replace(k, v)
    open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8").write(html)


if __name__ == "__main__":
    mix()
    build_html()
    json.dump({"segments": SEGS, "T": T}, open(f"{A}/audio/timings.json", "w"), indent=1)
    print("ok", DUR, "s,", len(CAPS), "groupes de sous-titres,", len(SFX), "effets", "(voix provisoire)" if not os.path.exists(VOICE) else "")
