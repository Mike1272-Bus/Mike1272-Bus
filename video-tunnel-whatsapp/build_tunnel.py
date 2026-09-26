"""Vidéo du tunnel WhatsApp : calage sur la voix, mixage et composition HyperFrames."""
import json, os, re, subprocess

ROOT = os.path.dirname(os.path.abspath(__file__))
A = os.path.join(ROOT, "assets")
VOICE = f"{A}/audio/voix_tunnel.mp3"
MUSIC = f"{A}/audio/musique_tunnel.wav"
DUR = 30.8

TEXT = ("Merci pour ta réponse ! Je te montre ce qu'il y a dans le guide. "
        "Des exemples de produits que tu peux créer, comme un modèle de CV ou une mini-formation de cuisine filmée au téléphone. "
        "Et un plan pour tester ton idée et trouver tes premiers clients en une semaine, sans dépenser un centime : "
        "tu écris ton offre en une phrase, tu en parles autour de toi, tu la postes en statut WhatsApp. "
        "À la fin de la semaine, tu sais si des gens sont prêts à payer. "
        "Je t'envoie le lien juste après. Si tu as une question, écris-moi.")


def segments():
    out = subprocess.run(["ffmpeg", "-hide_banner", "-i", VOICE, "-af", "silencedetect=noise=-35dB:d=0.25", "-f", "null", "-"],
                         capture_output=True, text=True).stderr
    v = [float(x) for x in re.findall(r"silence_(?:start|end): ([0-9.]+)", out)]
    dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", VOICE],
                               capture_output=True, text=True).stdout)
    if len(v) % 2:
        v.append(dur)
    sil = list(zip(v[0::2], v[1::2]))
    segs, t = [], 0.0
    for a, b in sil:
        if a - t > 0.05:
            segs.append((t, a))
        t = b
    if dur - t > 0.05:
        segs.append((t, dur))
    return segs


def tokens(text):
    toks = []
    for t in text.split(" "):
        if toks and t in (":", "?", "!"):
            toks[-1] += " " + t
        elif t:
            toks.append(t)
    return toks


SEGS = segments()
TOKS = tokens(TEXT)

# --- alignement mots / phrases de la voix ---
w = [len(t.strip(",.:!? ")) + 2 for t in TOKS]
cum = [0]
for x in w:
    cum.append(cum[-1] + x)
total_w = cum[-1]
seg_d = [b - a for a, b in SEGS]
total_d = sum(seg_d)
bounds, acc = [0], 0.0
for k in range(len(SEGS) - 1):
    acc += seg_d[k]
    target = acc / total_d * total_w
    best, best_cost = None, 1e9
    for i in range(bounds[-1] + 1, len(TOKS)):
        cost = abs(cum[i] - target) / total_w
        if not re.search(r"[,.:!?]$", TOKS[i - 1]):
            cost += 0.04
        if cost < best_cost:
            best, best_cost = i, cost
    bounds.append(best)
bounds.append(len(TOKS))

WORDS = []
for k, (a, b) in enumerate(SEGS):
    grp = list(range(bounds[k], bounds[k + 1]))
    tw = sum(w[i] for i in grp)
    t = a
    for i in grp:
        d = (b - a) * w[i] / tw
        WORDS.append((k, TOKS[i], round(t, 3), round(t + d, 3)))
        t += d


def wt(needle, which=0, end=False):
    hits = [x for x in WORDS if needle.lower() in x[1].lower()]
    return hits[which][3 if end else 2]


# --- sous-titres ---
ACCENT = {"guide.", "CV", "cuisine", "semaine,", "centime :", "WhatsApp.", "payer.", "écris-moi."}
CAPS = []
for k in range(len(SEGS)):
    ws = [x for x in WORDS if x[0] == k]
    n = max(1, round(len(ws) / 6 + 0.49))
    per = -(-len(ws) // n)
    for i in range(0, len(ws), per):
        g = ws[i:i + per]
        CAPS.append({"start": g[0][2], "end": g[-1][3],
                     "words": [{"t": x[1], "s": x[2], "e": x[3], "acc": x[1] in ACCENT} for x in g]})
for c, nxt in zip(CAPS, CAPS[1:]):
    c["hide"] = round(min(nxt["start"], c["end"] + 0.45), 3)
CAPS[-1]["hide"] = DUR - 0.2

T = {
    "merci": SEGS[0][0],
    "guide": wt("montre") - 0.25,
    "open": wt("guide.", end=True) - 0.15,
    "p10": wt("exemples") - 0.2,
    "cv": wt("CV"),
    "p11": wt("mini-formation") - 0.2,
    "cuisine": wt("cuisine"),
    "plan": wt("plan") - 0.3,
    "semaine": wt("semaine,"),
    "centime": wt("centime"),
    "s1": wt("écris"), "s2": wt("parles"), "s3": wt("postes"),
    "week": wt("fin") - 0.3,
    "payer": wt("payer."),
    "sais": wt("sais"),
    "link": wt("envoie") - 0.3,
    "ask": wt("question"),
    "end": DUR,
}
T = {k: round(v, 3) for k, v in T.items()}

SFX = [
    (0.0, "whoosh-short", 0.40), (T["merci"] + 0.1, "sparkle", 0.35),
    (T["guide"], "whoosh", 0.35), (T["open"], "whoosh-short", 0.35),
    (T["cv"], "pop", 0.35), (T["p11"], "whoosh-short", 0.30), (T["cuisine"], "pop", 0.35),
    (T["plan"], "whoosh", 0.35), (T["semaine"], "pop", 0.35), (T["centime"], "impact-bass-1", 0.30),
    (T["s1"], "click", 0.40), (T["s2"], "click", 0.40), (T["s3"], "click", 0.40),
    (T["sais"], "ping", 0.30),
    (T["link"] + 0.2, "notification", 0.40), (T["ask"], "pop", 0.35),
]
week_step = (T["sais"] - T["week"] - 0.55) / 7
for i in range(7):
    SFX.append((T["week"] + 0.4 + i * week_step, "key-press", 0.30))
T["weekStep"] = round(week_step, 3)


def mix():
    inputs = ["-i", VOICE, "-i", MUSIC]
    fl = ["[0:a]aresample=44100,aformat=channel_layouts=stereo,highpass=f=70,asplit=2[vo][sc]",
          "[1:a]volume=0.45[mus]",
          "[mus][sc]sidechaincompress=threshold=0.03:ratio=8:attack=20:release=350:makeup=1[musd]"]
    labels = []
    for i, (t, name, vol) in enumerate(SFX):
        inputs += ["-i", f"{A}/sfx/{name}.mp3"]
        d = max(0, int(t * 1000))
        fl.append(f"[{i+2}:a]aresample=44100,aformat=channel_layouts=stereo,volume={vol},adelay={d}|{d}[s{i}]")
        labels.append(f"[s{i}]")
    fl.append("[vo][musd]" + "".join(labels) + f"amix=inputs={2+len(labels)}:normalize=0:duration=longest,atrim=duration={DUR}[mix]")
    fl.append("[mix]loudnorm=I=-14:TP=-1.5:LRA=11[out]")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error"] + inputs +
                   ["-filter_complex", ";".join(fl), "-map", "[out]", "-ar", "44100", f"{A}/audio/mix_tunnel.wav"], check=True)


if __name__ == "__main__":
    for k, (a, b) in enumerate(SEGS):
        print(f"{a:6.2f}-{b:6.2f}  " + " ".join(x[1] for x in WORDS if x[0] == k))
    mix()
    html = open(os.path.join(ROOT, "template_tunnel.html.tpl"), encoding="utf-8").read()
    html = (html.replace("__T__", json.dumps(T)).replace("__CAPS__", json.dumps(CAPS, ensure_ascii=False))
                .replace("__DUR__", str(DUR)))
    open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8").write(html)
    print("ok", T)
