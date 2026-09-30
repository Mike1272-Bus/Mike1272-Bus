"""Vidéo 13 h jour 5 (Anglais) : calage sur la voix accélérée, mixage et composition HyperFrames."""
import functools, json, os, re, subprocess

ROOT = os.path.dirname(os.path.abspath(__file__))
A = os.path.join(ROOT, "assets")
VOICE = f"{A}/audio/voix.mp3"
MUSIC = f"{A}/audio/musique.wav"

TEXT = """Tu es sûrement déjà tombé sur ces vidéos : des jeunes qui apprennent l'anglais aux autres, sur TikTok ou sur Facebook. Et tu t'es peut-être dit : « Moi aussi, je parle anglais. » Alors regarde ce qu'on ne voit pas derrière ces vidéos. Et comment toi, tu peux faire pareil. Une bonne vidéo d'anglais, ce n'est pas juste pour les likes. Elle attire des gens qui ont un vrai besoin. Comme Grâce, 24 ans. Elle a un entretien dans une ONG, en anglais. Et dès qu'elle doit parler, elle bloque. Et ce besoin-là, tu peux y répondre. Crée-lui une simulation d'entretien en audio. Tu poses la question, elle répond à voix haute, puis elle écoute ta réponse modèle. Tes vidéos gratuites lui donnent confiance. Ton audio, elle l'achète. Et la meilleure partie, tu peux faire ça en plusieurs formats : mini cours vidéo, guide d'anglais, check-list. Et regarde bien ces comptes : certains ne montrent même pas leur visage. Une main qui écrit sur une feuille. Un texte animé. Un écran qui défile. Il te faut juste ton téléphone. Ce soir, je te montre ces trois formats, un par un. Et si toi aussi, tu as une compétence que tu voudrais apprendre aux autres, commente-la. Je te réponds en privé, et je te montre comment la transformer en revenu. Abonne-toi, pour ne pas manquer ça."""
NONE = set()
ACCENT = {"vidéos", "anglais. »", "derrière", "pareil.", "besoin.", "Grâce,", "bloque.", "audio.", "l'achète.", "formats", "visage.",
          "téléphone.", "soir,", "compétence", "commente-la.", "revenu.", "Abonne-toi"}
SPOKEN_LEN = {"24": 12}


def spoken(s):
    for k, v in {"24": "vingt-quatre", "ONG": "oénjé", "TikTok": "tiktok"}.items():
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

def w(needle, after=0.0):
    return [x for x in WORDS if needle.lower() in x[1].lower() and x[2] >= after - 1e-6][0][2]


T = {"end": DUR}
T.update({
    "videos": w("vidéos"), "jeunes": w("jeunes"), "tiktok": w("TikTok"), "facebook": w("Facebook"), "dit": w("dit"), "moi": w("Moi"),
    "alors": w("Alors"), "derriere": w("derrière"), "toi": w("toi,"), "pareil": w("pareil"),
    "bonne": w("bonne"), "likes": w("likes"), "attire": w("attire"), "besoin": w("besoin."),
    "grace": w("Grâce"), "entretien": w("entretien"), "ong": w("ONG"), "bloque": w("bloque"),
    "besoinla": w("besoin-là"), "repondre": w("répondre"),
    "simulation": w("simulation"), "question": w("question"), "haute": w("haute"), "modele": w("modèle"),
    "gratuites": w("gratuites"), "audio2": w("audio,"), "achete": w("l'achète"),
    "partie": w("partie"), "formats": w("formats"), "mini": w("mini"), "guide": w("guide"), "check": w("check-list"),
    "comptes": w("comptes"), "visage": w("visage"),
    "main": w("main"), "texte": w("texte"), "ecran": w("écran"), "telephone": w("téléphone"),
    "soir": w("soir"), "trois": w("trois"), "competence": w("compétence"), "commente": w("commente-la"),
    "prive": w("privé"), "revenu": w("revenu"), "abonne": w("Abonne-toi"),
})
T = {k: round(v, 3) for k, v in T.items()}

SFX = [
    (0.05, "whoosh-short", 0.40), (T["videos"] - 0.2, "pop", 0.32), (T["jeunes"], "pop", 0.32), (T["tiktok"], "pop", 0.32),
    (T["moi"], "sparkle", 0.35),
    (T["alors"] - 0.2, "whoosh", 0.40), (T["derriere"], "whoosh-short", 0.35), (T["pareil"], "ping", 0.32),
    (T["likes"], "pop", 0.28), (T["likes"] + 0.2, "pop", 0.24), (T["attire"], "chime", 0.30),
    (T["grace"] - 0.2, "whoosh-short", 0.40), (T["entretien"], "click", 0.35), (T["bloque"], "error", 0.35),
    (T["besoinla"], "sparkle", 0.32),
    (T["simulation"] - 0.2, "whoosh", 0.40), (T["question"], "notification", 0.30), (T["haute"], "click", 0.30), (T["modele"], "ping", 0.32),
    (T["gratuites"], "pop", 0.30), (T["achete"], "chime", 0.35),
    (T["partie"], "whoosh-short", 0.35), (T["mini"], "pop", 0.32), (T["guide"], "pop", 0.32), (T["check"], "pop", 0.32),
    (T["comptes"] - 0.2, "whoosh", 0.40), (T["visage"], "impact-bass-1", 0.35),
    (T["main"], ("typing", 0, 0.8), 0.22), (T["texte"], "pop", 0.30), (T["ecran"], "click-soft", 0.35), (T["telephone"], "sparkle", 0.32),
    (T["soir"], "chime", 0.32),
    (T["competence"] - 0.2, "whoosh", 0.40), (T["commente"], ("typing", 0, 0.9), 0.25), (T["prive"], "notification", 0.40), (T["revenu"], "sparkle", 0.35),
    (T["abonne"], "click", 0.45), (T["abonne"] + 0.15, "pop", 0.35),
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
    grace = ('<svg viewBox="0 0 440 600"><rect width="440" height="600" fill="#fde3c8"/><circle cx="220" cy="220" r="160" fill="#ffd9a8"/>'
             '<ellipse cx="220" cy="196" rx="94" ry="104" fill="#1d1410"/><circle cx="220" cy="92" r="46" fill="#1d1410"/>'
             '<rect x="196" y="272" width="48" height="64" fill="#6f4126"/><ellipse cx="220" cy="212" rx="74" ry="86" fill="#86502f"/>'
             '<path d="M146 200 C150 132 200 112 236 118 C276 124 298 158 294 200 C276 160 240 150 206 156 C180 160 160 178 146 200 Z" fill="#1d1410"/>'
             '<ellipse cx="192" cy="214" rx="8" ry="10" fill="#1d1410"/><ellipse cx="248" cy="214" rx="8" ry="10" fill="#1d1410"/>'
             '<path d="M178 192 L204 198 M262 192 L236 198" stroke="#1d1410" stroke-width="6" stroke-linecap="round"/>'
             '<path d="M200 262 Q220 252 240 262" fill="none" stroke="#3a1d10" stroke-width="6" stroke-linecap="round"/>'
             '<circle cx="146" cy="236" r="9" fill="#ffd60a"/><circle cx="294" cy="236" r="9" fill="#ffd60a"/>'
             '<path d="M60 600 C66 430 128 340 220 330 C312 340 374 430 380 600 Z" fill="#1c2f6b"/>'
             '<path d="M186 336 L220 430 L254 336 Z" fill="#fff"/><path d="M186 336 L220 430 L172 400 L160 350 Z M254 336 L220 430 L268 400 L280 350 Z" fill="#274394"/>'
             '<rect x="276" y="470" width="120" height="150" rx="10" fill="#fff" stroke="#111" stroke-width="5" transform="rotate(-8 336 545)"/>'
             '<path d="M296 510 H370 M296 540 H360 M296 570 H350" stroke="#9aa6c2" stroke-width="7" stroke-linecap="round" transform="rotate(-8 336 545)"/></svg>')
    recruiter = ('<svg viewBox="0 0 170 190"><circle cx="85" cy="56" r="40" fill="#5b4636"/><path d="M14 190 C16 128 44 104 85 104 C126 104 154 128 156 190 Z" fill="#3b3f4a"/>'
                 '<path d="M76 106 L85 150 L94 106 Z" fill="#e0161a"/><rect x="0" y="160" width="170" height="30" fill="#c79a6b" stroke="#111" stroke-width="4"/></svg>')
    noface = ('<svg viewBox="0 0 100 100"><circle cx="50" cy="50" r="46" fill="#fff" stroke="#111" stroke-width="6"/><circle cx="50" cy="40" r="16" fill="#111"/>'
              '<path d="M22 84 C24 64 36 58 50 58 C64 58 76 64 78 84 Z" fill="#111"/><path d="M18 82 L82 18" stroke="#e0161a" stroke-width="9" stroke-linecap="round"/></svg>')
    heart = '<svg viewBox="0 0 100 90"><path d="M50 86 C20 62 4 46 4 26 C4 12 16 2 30 2 C40 2 46 8 50 16 C54 8 60 2 70 2 C84 2 96 12 96 26 C96 46 80 62 50 86 Z" fill="#e0161a" stroke="#111" stroke-width="6"/></svg>'
    play = '<svg viewBox="0 0 100 100"><path d="M34 22 L80 50 L34 78 Z" fill="#fff" stroke="#111" stroke-width="6" stroke-linejoin="round"/></svg>'
    cart = ('<svg viewBox="0 0 100 100"><path d="M6 18 H22 L34 66 H80 L90 32 H27" fill="none" stroke="#fff" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/>'
            '<circle cx="40" cy="82" r="8" fill="#fff"/><circle cx="74" cy="82" r="8" fill="#fff"/></svg>')
    book = ('<svg viewBox="0 0 100 100"><path d="M50 26 C38 18 22 18 10 22 V82 C22 78 38 78 50 86 C62 78 78 78 90 82 V22 C78 18 62 18 50 26 Z" fill="#fff" stroke="#111" stroke-width="6" stroke-linejoin="round"/>'
            '<path d="M50 26 V86" stroke="#111" stroke-width="6"/></svg>')
    lst = ('<svg viewBox="0 0 100 100"><g stroke="#fff" stroke-width="9" stroke-linecap="round" stroke-linejoin="round" fill="none">'
           '<path d="M12 24 L20 32 L32 18 M12 54 L20 62 L32 48 M12 84 L20 92 L32 78"/><path d="M46 26 H88 M46 56 H88 M46 86 H80"/></g></svg>')
    typed = "".join(f"<span>{c}</span>" for c in "ANGLAIS")
    S = {
        "H1": (0.05, T["alors"] + 0.5), "H2": (T["jeunes"] - 0.35, T["grace"] + 0.1),
        "INT": (T["entretien"] - 0.25, T["besoinla"] + 0.1), "FREE": (T["gratuites"] - 0.35, T["partie"] + 0.1),
        "VIS": (T["comptes"] - 0.35, T["soir"] + 0.1), "SK": (T["competence"] - 1.05, T["commente"]),
    }
    times = {}
    for k, (a, e) in S.items():
        times[f"__S_{k}__"] = str(round(a, 3))
        times[f"__D_{k}__"] = str(round(e - a, 3))
    rep = {**times, "__STAR__": STAR, "__T__": json.dumps(T), "__CAPS__": json.dumps(CAPS, ensure_ascii=False), "__DUR__": str(DUR),
           "__MAN__": man, "__GRACE__": grace, "__RECRUITER__": recruiter, "__NOFACE__": noface, "__HEART__": heart, "__PLAY__": play,
           "__CART__": cart, "__BOOK__": book, "__LIST__": lst, "__TYPED__": typed, "__BARS__": "<i></i>" * 18}
    for k, v in rep.items():
        html = html.replace(k, v)
    open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8").write(html)


if __name__ == "__main__":
    mix()
    build_html()
    json.dump({"segments": SEGS, "T": T}, open(f"{A}/audio/timings.json", "w"), indent=1)
    print("ok", DUR, "s,", len(CAPS), "groupes de sous-titres,", len(SFX), "effets")
