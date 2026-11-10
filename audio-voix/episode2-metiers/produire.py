"""Épisode 2 (métiers manuels). Voix brute -> version pro.

Les pauses de Mike sont gardées telles quelles : on coupe seulement le silence avant le début et après la fin.
Les bruitages ne vont qu'aux moments choisis selon le script, dans la pause qui suit la phrase.
"""
import json, os, subprocess
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..", "..")
SFX = os.path.join(ROOT, "video-excel-13h", "assets", "sfx")
MUSIC = os.path.join(ROOT, "pub-video-digitalmikaelson", "assets", "audio", "musique_fond.wav")
SR, TEMPO, T0 = 44100, 1.10, 0.6
# bruitages choisis selon le script, posés dans la pause qui suit la phrase (temps du brut)
# temps du brut, recalés sur la transcription (transcription.json, temps de la vidéo finale)
MOMENTS = [
    (14.58, "whoosh", 0.38, "fin de l'accroche, l'histoire de Patrick commence"),
    (24.32, "error", 0.22, "« Pas d'argent. »"),
    (30.14, "pop", 0.30, "la question : « et si les gens pouvaient voir mon travail… ? »"),
    (33.78, "click", 0.30, "il filme ses mains (REC)"),
    (37.16, "notification", 0.30, "les commentaires : « Comment tu fais ça ? »"),
    (39.74, "sparkle", 0.32, "« C'est là qu'il a l'idée. »"),
    (55.84, "ping", 0.30, "la vente sur Chariow (paiement reçu)"),
    (58.90, "whoosh-short", 0.30, "les réseaux et la publicité"),
    (75.97, "whoosh", 0.38, "« Et ce n'est pas que la menuiserie »"),
    (87.19, "impact-bass-1", 0.30, "« Patrick, c'est une histoire » : la révélation"),
    (94.45, "pop", 0.30, "la question finale : « Et toi, c'est quoi ta compétence ? »"),
]


def run(*a, inp=None):
    return subprocess.run(list(a), input=inp, capture_output=True, check=True).stdout


y = np.frombuffer(run("ffmpeg", "-loglevel", "error", "-i", os.path.join(HERE, "brut.m4a"), "-f", "f32le", "-ac", "1", "-ar", str(SR), "-"), np.float32).copy()

# 1. trouver le début et la fin de la voix, et toutes les pauses
fr = int(0.02 * SR); n = len(y) // fr
e = 20 * np.log10(np.sqrt((y[:n * fr].reshape(n, fr) ** 2).mean(1)) + 1e-9)
quiet = e < np.percentile(e, 10) + 10
voiced = np.where(~quiet)[0]
start, end = max(voiced[0] * 0.02 - 0.15, 0), voiced[-1] * 0.02 + 0.35
pauses, i = [], 0
while i < n:
    if quiet[i]:
        j = i
        while j < n and quiet[j]: j += 1
        if (j - i) * 0.02 >= 0.45 and start < i * 0.02 < end - 0.5:
            pauses.append((i * 0.02, (j - i) * 0.02))
        i = j
    else:
        i += 1

raw_wav = os.path.join(HERE, "_voix.wav")
seg = y[int(start * SR):int(end * SR)]
run("ffmpeg", "-loglevel", "error", "-y", "-f", "f32le", "-ar", str(SR), "-ac", "1", "-i", "-", raw_wav, inp=seg.tobytes())

# 2. voix : bruit de fond, ronflement 50 Hz, clarté, compression, accélération légère, volume
voice = os.path.join(HERE, "_voix_traitee.wav")
chain = ("afftdn=nr=12:nf=-50,highpass=f=90,equalizer=f=220:t=q:w=1.2:g=-3,"
         "equalizer=f=3200:t=q:w=1.0:g=4,equalizer=f=120:t=q:w=1.0:g=2,"
         "acompressor=threshold=-24dB:ratio=3:attack=6:release=100:makeup=4,"
         f"atempo={TEMPO},afade=t=in:d=0.05,afade=t=out:st={(end - start) / TEMPO - 0.2}:d=0.2,loudnorm=I=-16:TP=-2:LRA=6")
run("ffmpeg", "-loglevel", "error", "-y", "-i", raw_wav, "-af", chain, "-ar", str(SR), voice)
os.remove(raw_wav)
dur_v = float(run("ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", voice))


def new_time(t_raw):
    return (t_raw - start) / TEMPO + T0


# 3. bruitages : l'intro, puis uniquement les moments du script
sfx = [(0.0, "whoosh-cinematic", 0.45), (0.35, "impact-bass-1", 0.35)]
for t, name, vol, _ in MOMENTS:
    t = min((p for p, _ in pauses), key=lambda p: abs(p - t), default=t)  # au début de la pause la plus proche
    sfx.append((new_time(t) + 0.08, name, vol))
END = T0 + dur_v
sfx.append((END - 0.1, "chime", 0.35))
total = END + 1.8

# 4. mixage : musique qui baisse sous la voix, bruitages, volume final réseaux
inputs = ["-i", voice, "-stream_loop", "-1", "-i", MUSIC]
d0 = int(T0 * 1000)
fl = [f"[0:a]adelay={d0}|{d0},apad,atrim=duration={total},asplit=2[v][sc]",
      f"[1:a]aresample={SR},aformat=channel_layouts=mono,atrim=duration={total},volume=0.32,"
      f"afade=t=in:d=0.4,afade=t=out:st={total - 1.6}:d=1.6[m]",
      "[m][sc]sidechaincompress=threshold=0.03:ratio=6:attack=20:release=350[mduck]"]
labels = ["[v]", "[mduck]"]
for j, (t, name, vol) in enumerate(sfx):
    inputs += ["-i", os.path.join(SFX, name + ".mp3")]
    dl = int(t * 1000)
    fl.append(f"[{j + 2}:a]aresample={SR},aformat=channel_layouts=mono,volume={vol},adelay={dl}|{dl}[s{j}]")
    labels.append(f"[s{j}]")
fl.append("".join(labels) + f"amix=inputs={len(labels)}:normalize=0:duration=first,atrim=duration={total},loudnorm=I=-14:TP=-1.5:LRA=8[out]")
out = os.path.join(HERE, "episode2_metiers_voix_pro.mp3")
run("ffmpeg", "-loglevel", "error", "-y", *inputs, "-filter_complex", ";".join(fl), "-map", "[out]", "-ar", str(SR), "-b:a", "192k", out)
os.remove(voice)
parties = [(round(new_time(t) + 0.08, 2), quoi) for t, _, _, quoi in MOMENTS]
json.dump({"debut_voix": T0, "fin_voix": round(END, 2), "parties": parties, "bruitages": [(round(t, 2), nm) for t, nm, _ in sfx], "duree": round(total, 2)},
          open(os.path.join(HERE, "reperes.json"), "w"), indent=1)
print(f"brut {len(y) / SR:.1f} s -> final {total:.1f} s ; {len(sfx)} bruitages ; parties à {parties}")
