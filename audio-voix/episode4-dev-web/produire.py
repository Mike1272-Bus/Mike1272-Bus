"""Épisode 4 (développeur web). Voix brute (enrhumée) -> version pro.

- On coupe le raclement de gorge du début (la voix commence à DEBUT).
- Les pauses trop longues sont raccourcies à PAUSE_MAX (on garde le souffle, on enlève les blancs).
- Réglages « rhume » : moins de souffle, moins de son nasal, voix plus claire, sifflements adoucis.
- Bruitages aux moments du script (temps du brut, lus dans transcription_brut.json), dans la pause qui suit.
"""
import json, os, subprocess
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..", "..")
SFX = os.path.join(ROOT, "video-excel-13h", "assets", "sfx")
MUSIC = os.path.join(ROOT, "pub-video-digitalmikaelson", "assets", "audio", "musique_fond.wav")
SR, TEMPO, T0, DEBUT, PAUSE_MAX = 44100, 1.10, 0.6, 7.55, 0.45
MOMENTS = [
    (12.46, "whoosh", 0.38, "fin du hook : « cette vidéo, je l'ai faite pour toi »"),
    (18.70, "sparkle", 0.30, "« avec un exemple précis »"),
    (40.50, "whoosh-short", 0.32, "« pas le même budget », avant « c'est là que ça devient intéressant »"),
    (46.30, "pop", 0.30, "« à l'entreprise, tu vends un service »"),
    (53.70, "notification", 0.28, "« un bouton qui ouvre WhatsApp »"),
    (56.70, "whoosh-short", 0.30, "passage au particulier"),
    (85.30, "ping", 0.30, "« tu le vends à toutes les vendeuses »"),
    (89.28, "whoosh", 0.36, "« il te faut seulement quatre outils »"),
    (101.66, "click", 0.30, "« Chariow, pour vendre et recevoir les paiements »"),
    (112.06, "pop", 0.32, "« commente VITRINE »"),
]

def run(*a, inp=None):
    return subprocess.run(list(a), input=inp, capture_output=True, check=True).stdout

y = np.frombuffer(run("ffmpeg", "-loglevel", "error", "-i", os.path.join(HERE, "brut.m4a"), "-f", "f32le", "-ac", "1", "-ar", str(SR), "-"), np.float32).copy()
fr = int(0.02 * SR); n = len(y) // fr
e = 20 * np.log10(np.sqrt((y[:n * fr].reshape(n, fr) ** 2).mean(1)) + 1e-9)
quiet = e < np.percentile(e, 10) + 10
voiced = np.where(~quiet)[0]
voiced = voiced[voiced * 0.02 >= DEBUT]
start, end = max(voiced[0] * 0.02 - 0.12, DEBUT - 0.05), min(voiced[-1] * 0.02 + 0.35, n * 0.02)

# pauses (dans la voix) et parties à retirer
pauses, cuts, i = [], [], 0
while i < n:
    if quiet[i]:
        j = i
        while j < n and quiet[j]: j += 1
        a, b = i * 0.02, j * 0.02
        if b - a >= 0.3 and start < a and b < end:
            pauses.append(a)
            if b - a > PAUSE_MAX:
                cuts.append((a + PAUSE_MAX / 2, b - PAUSE_MAX / 2))
        i = j
    else:
        i += 1

def cut_time(t):
    """temps du brut -> temps après coupes (avant accélération)"""
    t = max(t, start); removed = 0.0
    for a, b in cuts:
        if t >= b: removed += b - a
        elif t > a: removed += t - a
    return t - start - removed

def new_time(t):
    return cut_time(t) / TEMPO + T0

keep, cur = [], start
for a, b in cuts:
    keep.append((cur, a)); cur = b
keep.append((cur, end))
seg = np.concatenate([y[int(a * SR):int(b * SR)] for a, b in keep])
raw_wav = os.path.join(HERE, "_voix.wav")
run("ffmpeg", "-loglevel", "error", "-y", "-f", "f32le", "-ar", str(SR), "-ac", "1", "-i", "-", raw_wav, inp=seg.astype(np.float32).tobytes())

voice = os.path.join(HERE, "_voix_traitee.wav")
dur_cut = len(seg) / SR
chain = ("afftdn=nr=18:nf=-45,highpass=f=85,"
         "equalizer=f=300:t=q:w=1.0:g=-3,equalizer=f=950:t=q:w=1.2:g=-2,"
         "equalizer=f=3200:t=q:w=1.0:g=4,highshelf=f=8000:g=2,deesser=i=0.4,"
         "acompressor=threshold=-24dB:ratio=3:attack=6:release=100:makeup=4,"
         f"atempo={TEMPO},afade=t=in:d=0.05,afade=t=out:st={dur_cut / TEMPO - 0.2}:d=0.2,loudnorm=I=-16:TP=-2:LRA=6")
run("ffmpeg", "-loglevel", "error", "-y", "-i", raw_wav, "-af", chain, "-ar", str(SR), voice)
os.remove(raw_wav)
dur_v = float(run("ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", voice))

sfx = [(0.0, "whoosh-cinematic", 0.45), (0.35, "impact-bass-1", 0.35)]
for t, name, vol, _ in MOMENTS:
    t = min(pauses, key=lambda p: abs(p - t), default=t)
    sfx.append((new_time(t) + 0.08, name, vol))
END = T0 + dur_v
sfx.append((END - 0.1, "chime", 0.35))
total = END + 1.8

inputs = ["-i", voice, "-stream_loop", "-1", "-i", MUSIC]
d0 = int(T0 * 1000)
fl = [f"[0:a]adelay={d0}|{d0},apad,atrim=duration={total},asplit=2[v][sc]",
      f"[1:a]aresample={SR},aformat=channel_layouts=mono,atrim=duration={total},volume=0.32,afade=t=in:d=0.4,afade=t=out:st={total - 1.6}:d=1.6[m]",
      "[m][sc]sidechaincompress=threshold=0.03:ratio=6:attack=20:release=350[mduck]"]
labels = ["[v]", "[mduck]"]
for j, (t, name, vol) in enumerate(sfx):
    inputs += ["-i", os.path.join(SFX, name + ".mp3")]
    dl = int(t * 1000)
    fl.append(f"[{j + 2}:a]aresample={SR},aformat=channel_layouts=mono,volume={vol},adelay={dl}|{dl}[s{j}]")
    labels.append(f"[s{j}]")
fl.append("".join(labels) + f"amix=inputs={len(labels)}:normalize=0:duration=first,atrim=duration={total},loudnorm=I=-14:TP=-1.5:LRA=8[out]")
out = os.path.join(HERE, "episode4_dev_web_voix_pro.mp3")
run("ffmpeg", "-loglevel", "error", "-y", *inputs, "-filter_complex", ";".join(fl), "-map", "[out]", "-ar", str(SR), "-b:a", "192k", out)
os.remove(voice)

tr = json.load(open(os.path.join(HERE, "transcription_brut.json")))
json.dump([(round(new_time(a), 2), round(new_time(b), 2), x) for a, b, x in tr if a >= DEBUT],
          open(os.path.join(HERE, "transcription.json"), "w"), ensure_ascii=False, indent=1)
json.dump({"debut_voix": T0, "fin_voix": round(END, 2), "pauses_raccourcies": len(cuts),
           "bruitages": [(round(t, 2), nm) for t, nm, _ in sfx], "duree": round(total, 2)},
          open(os.path.join(HERE, "reperes.json"), "w"), indent=1)
print(f"brut {len(y) / SR:.1f} s -> final {total:.1f} s ; {len(cuts)} pauses raccourcies ; {len(sfx)} bruitages")
print([(round(t, 1), nm) for t, nm, _ in sfx])
