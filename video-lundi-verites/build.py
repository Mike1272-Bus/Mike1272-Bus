"""Vidéo du lundi "3 vérités" : calage sur la voix, mixage et composition HyperFrames."""
import json, os, re, subprocess

ROOT = os.path.dirname(os.path.abspath(__file__))
A = os.path.join(ROOT, "assets")
VOICE = f"{A}/audio/voix.mp3"
MUSIC = f"{A}/audio/musique.wav"

SCRIPT = [
    "Plus de 12 millions de francs CFA de ventes.",
    "Ça fait rêver.",
    "Mais ce chiffre ne dit pas ce que ce vendeur a vraiment gagné.",
    "Voici 3 vérités qu'on ne vous dit pas sur les produits digitaux.",
    "Un : ce chiffre, c'est le chiffre d'affaires,",
    "pas le bénéfice.",
    "Il faut encore retirer la pub, les commissions, les remboursements, les frais et les impôts.",
    "Sur un gros lancement,",
    "il reste souvent 10 à 30 %.",
    "Deux :",
    "on vous montre le chiffre brut parce que c'est lui qui fait rêver.",
    "Le bénéfice, on ne le montre presque jamais.",
    "Trois :",
    "ce qui compte, c'est ce qui vous reste sur chaque vente.",
    "Un produit créé avec votre téléphone, et que vous faites connaître sans pub, garde vos frais au plus bas.",
    "Dans mon guide, il y a un plan de 7 jours",
    "pour tester votre idée sans dépenser un franc en publicité.",
    "Écrivez « EBOOK » en commentaire,",
    "je vous réponds",
    "et je vous accompagne.",
]
NONE = {4, 10, 13}          # le texte est déjà le visuel
ACCENT = {"rêver.", "gagné.", "bénéfice.", "jamais.", "EBOOK", "accompagne.", "vente."}


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
DUR = round(SEGS[-1][1] + 1.2, 2)

WORDS = []
for si, ((a, b), line) in enumerate(zip(SEGS, SCRIPT)):
    toks = [t for t in line.replace("« ", "«").replace(" »", "»").split(" ") if t]
    toks = [t.replace("«", "« ").replace("»", " »") for t in toks]
    merged = []
    for t in toks:
        if merged and t.strip() in (":", "?", "!", "%", "%."):
            merged[-1] += " " + t
        else:
            merged.append(t)
    weights = [len(t.strip("«» ,.:?%")) + 2 for t in merged]
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
                                   "acc": w[1].strip("«» ") in ACCENT} for w in grp]})
    for c, nxt in zip(out, out[1:]):
        c["hide"] = round(min(nxt["start"], c["end"] + 0.45), 3)
    out[-1]["hide"] = DUR - 0.2
    return out


CAPS = chunks()

T = {
    "reve": seg(2)[0], "gagne": seg(3)[0], "title": seg(4)[0] - 0.25,
    "v1": seg(5)[0] - 0.3, "benef1": seg(6)[0],
    "c1": word(7, "pub")[2], "c2": word(7, "commissions")[2], "c3": word(7, "remboursements")[2],
    "c4": word(7, "frais")[2], "c5": word(7, "impôts")[2], "lanc": seg(8)[0], "reste": word(9, "10")[2],
    "v2": seg(10)[0] - 0.25, "brut": seg(11)[0], "reveBrut": word(11, "rêver")[2], "benef2": seg(12)[0], "jamais": word(12, "jamais")[2],
    "v3": seg(13)[0] - 0.25, "compte": seg(14)[0], "tel": word(15, "téléphone")[2], "pub3": word(15, "pub")[2], "frais3": word(15, "frais")[2],
    "cta": seg(16)[0] - 0.3, "sept": word(16, "7")[2], "franc": word(17, "franc")[2],
    "ebook": seg(18)[0] - 0.2, "ebookWord": word(18, "EBOOK")[2], "accomp": seg(20)[0],
    "end": DUR,
}
T = {k: round(v, 3) for k, v in T.items()}

SFX = [
    (0.05, "whoosh-short", 0.45), (0.55, "pop", 0.35), (T["reve"], "sparkle", 0.40), (T["gagne"] + 0.5, "impact-bass-1", 0.40),
    (T["title"], "whoosh", 0.40), (T["title"] + 0.25, "impact-bass-2", 0.45),
    (T["v1"], "whoosh-short", 0.40), (T["v1"] + 0.2, "pop", 0.35),
    (T["c1"], "click", 0.40), (T["c2"], "click", 0.40), (T["c3"], "click", 0.40), (T["c4"], "click", 0.40), (T["c5"], "click", 0.40),
    (T["reste"], "ping", 0.40),
    (T["v2"], "whoosh-short", 0.40), (T["v2"] + 0.2, "pop", 0.35), (T["reveBrut"], "sparkle", 0.35), (T["jamais"], "impact-bass-1", 0.40),
    (T["v3"], "whoosh-short", 0.40), (T["v3"] + 0.2, "pop", 0.35), (T["tel"], "pop", 0.32), (T["pub3"], "pop", 0.32), (T["frais3"], "pop", 0.32),
    (T["cta"], "whoosh", 0.40), (T["sept"], "pop", 0.35), (T["franc"], "pop", 0.35),
    (T["ebook"], "whoosh-short", 0.40), (T["ebookWord"], ("typing", 0, 0.9), 0.25), (T["accomp"] + 0.3, "notification", 0.40),
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
    html = (html.replace("__STAR__", STAR).replace("__T__", json.dumps(T))
                .replace("__CAPS__", json.dumps(CAPS, ensure_ascii=False)).replace("__DUR__", str(DUR)))
    open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8").write(html)


if __name__ == "__main__":
    mix()
    build_html()
    json.dump({"segments": SEGS, "T": T}, open(f"{A}/audio/timings.json", "w"), indent=1)
    print("ok", DUR, "s,", len(CAPS), "groupes de sous-titres,", len(SFX), "effets")
