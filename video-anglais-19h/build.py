"""Vidéo 19 h jour 5 (Anglais, suite) : calage sur la voix accélérée, mixage et composition HyperFrames."""
import functools, json, os, re, subprocess

ROOT = os.path.dirname(os.path.abspath(__file__))
A = os.path.join(ROOT, "assets")
VOICE = f"{A}/audio/voix.mp3"
MUSIC = f"{A}/audio/musique.wav"

TEXT = """Ce matin, je t'ai montré ces jeunes qui enseignent l'anglais sans montrer leur visage. Ce soir, je te montre comment ils font. Tu veux publier des leçons d'anglais, sans caméra et sans montrer ton visage ? Voici trois façons, avec juste ton téléphone. Regarde ces comptes. Ces jeunes publient des leçons d'anglais. Leur visage, tu ne le vois jamais. S'ils le font, tu peux le faire. Regarde. Un : une feuille, un feutre. Ton téléphone filme ta main qui écrit la phrase, puis sa traduction. Deux : le texte animé. Dans CapCut, les mots apparaissent un par un, et ta voix les prononce. Trois : ton écran. Tu tapes la question dans Google Docs, et tu enregistres l'écran pendant que tu lis la réponse. Et chacune de ces vidéos peut t'amener une cliente. La veille de son entretien, Grâce tombe sur ta leçon. Elle l'écoute trois fois. Puis elle t'écrit : « Tu as d'autres questions comme ça ? » Ce message, c'est le début de ta première vente. Commente le numéro du format que tu vas essayer. Je te réponds en privé pour t'aider à te lancer."""
NONE = set()
ACCENT = {"matin,", "visage.", "soir,", "comment", "caméra", "trois", "téléphone.", "comptes.", "jamais.", "peux", "Un :", "main", "traduction.",
          "Deux :", "animé.", "CapCut,", "Trois :", "écran.", "Docs,", "cliente.", "Grâce", "trois", "vente.", "numéro", "privé", "lancer."}
SPOKEN_LEN = {"24": 12}


def spoken(s):
    for k, v in {"CapCut": "capcute", "Google Docs": "gougueul dokse"}.items():
        s = s.replace(k, v)
    return len(re.sub(r"[^\wÀ-ÿ]", "", s))


def duration(f):
    return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f],
                                capture_output=True, text=True).stdout)


def speech_segments():
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
DUR = round(SEGS[-1][1] + 1.4, 2)

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
T["matin"] = w("matin")
T["jeunes"] = w("jeunes")
T["enseignent"] = w("enseignent")
T["visage"] = w("visage")
T["soir"] = w("soir")
T["comment"] = w("comment")
T["font"] = w("font")
T["veux"] = w("veux")
T["lecons"] = w("leçons")
T["camera"] = w("caméra")
T["visage2"] = w("visage", T["camera"])
T["trois"] = we("trois")
T["facons"] = w("façons")
T["telephone"] = w("téléphone")
T["regarde"] = w("Regarde")
T["comptes"] = w("comptes")
T["publient"] = w("publient")
T["visage3"] = w("visage", T["publient"])
T["jamais"] = w("jamais")
T["sils"] = w("S'ils")
T["peux"] = we("peux")
T["regarde2"] = w("Regarde", T["peux"])
T["un"] = we("un", T["regarde2"])
T["feuille"] = w("feuille")
T["feutre"] = w("feutre")
T["filme"] = w("filme")
T["main"] = we("main")
T["ecrit"] = w("écrit")
T["phrase"] = w("phrase")
T["traduction"] = w("traduction")
T["deux"] = w("Deux")
T["anime"] = w("animé")
T["capcut"] = w("CapCut")
T["mots"] = we("mots")
T["unpar"] = we("un", T["capcut"])
T["voix"] = we("voix")
T["prononce"] = w("prononce")
T["troisF"] = w("Trois", T["prononce"])
T["ecran"] = w("écran")
T["tapes"] = w("tapes")
T["question"] = w("question")
T["docs"] = w("Docs")
T["enregistres"] = w("enregistres")
T["lis"] = we("lis")
T["reponse"] = w("réponse")
T["chacune"] = w("chacune")
T["videos"] = w("vidéos")
T["amener"] = w("amener")
T["cliente"] = w("cliente")
T["veille"] = w("veille")
T["entretien"] = w("entretien")
T["grace"] = w("Grâce")
T["tombe"] = w("tombe")
T["lecon"] = w("leçon.", T["grace"])
T["ecoute"] = w("l'écoute")
T["fois"] = w("fois")
T["ecrit2"] = w("t'écrit")
T["autres"] = w("autres")
T["questions"] = w("questions", T["autres"])
T["message"] = w("message")
T["debut"] = w("début")
T["vente"] = w("vente")
T["commente"] = w("Commente")
T["numero"] = w("numéro")
T["essayer"] = w("essayer")
T["prive"] = w("privé")
T["aider"] = w("aider")
T["lancer"] = w("lancer")
T = {k: round(v, 3) for k, v in T.items()}

SFX = [
    (0.05, "whoosh-short", 0.40), (T["jeunes"] - 0.2, "pop", 0.30), (T["enseignent"], "pop", 0.30), (T["visage"], "impact-bass-1", 0.32),
    (T["soir"] - 0.2, "whoosh", 0.40), (T["comment"], "chime", 0.32),
    (T["veux"] - 0.1, "whoosh-short", 0.35), (T["camera"], "error", 0.30), (T["visage2"], "error", 0.28),
    (T["trois"], "pop", 0.30), (T["trois"] + 0.2, "pop", 0.30), (T["trois"] + 0.4, "pop", 0.30), (T["telephone"], "sparkle", 0.32),
    (T["regarde"] - 0.2, "whoosh", 0.40), (T["jamais"], "impact-bass-1", 0.35),
    (T["sils"], "whoosh-short", 0.30), (T["peux"], "sparkle", 0.35), (T["regarde2"], "ping", 0.30),
    (T["un"] - 0.2, "impact-bass-2", 0.35), (T["feuille"], "pop", 0.30), (T["feutre"], "pop", 0.30), (T["filme"], "click", 0.35),
    (T["phrase"], ("typing", 0, 0.7), 0.20), (T["traduction"], "ping", 0.30),
    (T["deux"] - 0.2, "impact-bass-2", 0.35), (T["mots"], "pop", 0.26), (T["unpar"], "pop", 0.26), (T["unpar"] + 0.3, "pop", 0.26), (T["voix"], "sparkle", 0.30),
    (T["troisF"] - 0.2, "impact-bass-2", 0.35), (T["tapes"], ("typing", 0, 1.3), 0.25), (T["enregistres"], "click", 0.40), (T["lis"], "notification", 0.25),
    (T["chacune"] - 0.1, "whoosh", 0.38), (T["cliente"], "chime", 0.35),
    (T["veille"] - 0.2, "whoosh-short", 0.40), (T["grace"], "pop", 0.30), (T["ecoute"], "click-soft", 0.30), (T["fois"], "ping", 0.30),
    (T["ecrit2"], "notification", 0.40), (T["message"], "whoosh-short", 0.30), (T["vente"], "chime", 0.40),
    (T["commente"] - 0.2, "whoosh", 0.40), (T["numero"], ("typing", 0, 0.6), 0.25), (T["prive"], "notification", 0.40), (T["lancer"], "riser", 0.30),
    (DUR - 1.0, "sparkle", 0.30),
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
    man = ('<svg viewBox="0 0 100 114" fill="currentColor"><circle cx="50" cy="28" r="22"/>'
           '<path d="M12 112 C12 74 28 58 50 58 C72 58 88 74 88 112 Z"/></svg>')
    noface = ('<svg viewBox="0 0 100 100"><circle cx="50" cy="50" r="46" fill="#fff" stroke="#111" stroke-width="6"/><circle cx="50" cy="40" r="16" fill="#111"/>'
              '<path d="M22 84 C24 64 36 58 50 58 C64 58 76 64 78 84 Z" fill="#111"/><path d="M18 82 L82 18" stroke="#e0161a" stroke-width="9" stroke-linecap="round"/></svg>')
    cart = ('<svg viewBox="0 0 100 100"><path d="M6 18 H22 L34 66 H80 L90 32 H27" fill="none" stroke="#fff" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/>'
            '<circle cx="40" cy="82" r="8" fill="#fff"/><circle cx="74" cy="82" r="8" fill="#fff"/></svg>')
    heart = '<svg viewBox="0 0 100 90"><path d="M50 86 C20 62 4 46 4 26 C4 12 16 2 30 2 C40 2 46 8 50 16 C54 8 60 2 70 2 C84 2 96 12 96 26 C96 46 80 62 50 86 Z" fill="#e0161a" stroke="#111" stroke-width="6"/></svg>'
    play = '<svg viewBox="0 0 100 100"><path d="M34 22 L80 50 L34 78 Z" fill="#fff" stroke="#111" stroke-width="6" stroke-linejoin="round"/></svg>'
    S = {
        "H1": (0.05, T["soir"] + 0.1), "H2": (T["jeunes"] - 0.4, T["soir"] + 0.1), "VIS": (T["visage"] - 0.9, T["soir"] + 0.1),
        "Q1": (T["regarde"] - 0.4, T["sils"] + 0.1), "Q2": (T["regarde"] - 0.4, T["sils"] + 0.1), "Q3": (T["regarde"] - 0.4, T["sils"] + 0.1),
        "TAB": (T["un"] - 0.1, T["deux"] + 0.1), "CAP": (T["deux"] - 0.1, T["troisF"] + 0.1), "INT": (T["veille"] - 0.4, T["ecrit2"]),
    }
    rep = {"__STAR__": STAR, "__T__": json.dumps(T), "__CAPS__": json.dumps(CAPS, ensure_ascii=False), "__DUR__": str(DUR),
           "__BARS__": "<i></i>" * 14, "__MAN__": man, "__NOFACE__": noface, "__CART__": cart, "__HEART__": heart, "__PLAY__": play,
           "__GQ__": "".join(f"<span>{c}</span>" for c in "Tell me about yourself?"), "__TYPED__": "".join(f"<span>{c}</span>" for c in "FORMAT 2")}
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
    print("ok", DUR, "s,", len(CAPS), "groupes de sous-titres,", len(SFX), "effets")
