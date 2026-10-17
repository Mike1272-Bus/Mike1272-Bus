"""Voix brute -> version pro : nettoyage, pauses resserrées, accélération, musique de fond qui s'efface sous la voix, bruitages."""
import json, os, subprocess
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..", "..")
SFX = os.path.join(ROOT, "video-excel-13h", "assets", "sfx")
MUSIC = os.path.join(ROOT, "pub-video-digitalmikaelson", "assets", "audio", "musique_fond.wav")
SR, START, TEMPO = 44100, 3.6, 1.10
SECTIONS = [12.70, 36.52, 57.08]  # pauses longues du brut (secondes) = changements de partie

def run(*a, inp=None):
    return subprocess.run(list(a), input=inp, capture_output=True, check=True).stdout

y = np.frombuffer(run("ffmpeg", "-loglevel", "error", "-i", os.path.join(HERE, "brut.m4a"), "-f", "f32le", "-ac", "1", "-ar", str(SR), "-"), np.float32).copy()
y = y[int(START * SR):]

# 1. pauses : tout silence de plus de 0,35 s est ramené à 0,22 s (fondus de 15 ms)
fr = int(0.02 * SR); n = len(y) // fr
e = 20 * np.log10(np.sqrt((y[:n * fr].reshape(n, fr) ** 2).mean(1)) + 1e-9)
quiet = e < np.percentile(e, 10) + 10
keep_q, fade = int(0.22 * SR), int(0.015 * SR)
pieces, mapping, pos, out_len, i = [], [], 0, 0, 0
while i < n:
    if quiet[i]:
        j = i
        while j < n and quiet[j]: j += 1
        if (j - i) * fr >= int(0.35 * SR):
            a, b = i * fr, j * fr
            seg = y[pos:a + keep_q // 2].copy()
            if len(seg) > fade: seg[-fade:] *= np.linspace(1, 0, fade)
            mapping.append((pos / SR, out_len / SR)); pieces.append(seg); out_len += len(seg)
            nxt = b - keep_q // 2
            pos = nxt
        i = j
    else:
        i += 1
seg = y[pos:].copy(); mapping.append((pos / SR, out_len / SR)); pieces.append(seg); out_len += len(seg)
fixed = []
for k, s in enumerate(pieces):
    s = s.copy()
    if k and len(s) > fade: s[:fade] *= np.linspace(0, 1, fade)
    fixed.append(s)
v = np.concatenate(fixed)

def new_time(t_brut):
    t = t_brut - START
    best = max((m for m in mapping if m[0] <= t), key=lambda m: m[0])
    return (best[1] + (t - best[0])) / TEMPO

raw_wav = os.path.join(HERE, "_voix_coupee.wav")
run("ffmpeg", "-loglevel", "error", "-y", "-f", "f32le", "-ar", str(SR), "-ac", "1", "-i", "-", raw_wav, inp=v.tobytes())

# 2. voix : réduction de bruit douce, sifflement à 2,3 kHz retiré, égalisation, compression, accélération
voice = os.path.join(HERE, "voix_traitee.wav")
chain = ("afftdn=nr=12:nf=-50,highpass=f=85,equalizer=f=2300:t=q:w=8:g=-18,equalizer=f=220:t=q:w=1.2:g=-3,"
         "equalizer=f=3200:t=q:w=1.0:g=4,equalizer=f=120:t=q:w=1.0:g=2,"
         "acompressor=threshold=-24dB:ratio=3:attack=6:release=100:makeup=4,"
         f"atempo={TEMPO},loudnorm=I=-16:TP=-2:LRA=6")
run("ffmpeg", "-loglevel", "error", "-y", "-i", raw_wav, "-af", chain, "-ar", str(SR), voice)
os.remove(raw_wav)
dur_v = float(run("ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", voice))

# 3. bruitages placés sur les changements de partie
T0 = 0.6  # la voix commence après une petite intro musicale
marks = [new_time(t) + T0 for t in SECTIONS]
sfx = [(0.0, "whoosh-cinematic", 0.45), (0.35, "impact-bass-1", 0.35)]
for k, m in enumerate(marks):
    sfx += [(max(m - 0.35, 0), "whoosh", 0.4), (m - 0.05, "pop" if k != 2 else "sparkle", 0.35)]
END = T0 + dur_v
sfx += [(END - 0.2, "chime", 0.35)]
total = END + 1.8

# 4. mixage : musique qui baisse sous la voix (compression par la voix), bruitages, volume final réseaux
inputs = ["-i", voice, "-stream_loop", "-1", "-i", MUSIC]
d0 = int(T0 * 1000)
fl = [f"[0:a]adelay={d0}|{d0},apad,atrim=duration={total},asplit=2[v][sc]",
      f"[1:a]aresample={SR},aformat=channel_layouts=mono,atrim=duration={total},volume=0.32,"
      f"afade=t=in:d=0.4,afade=t=out:st={total - 1.6}:d=1.6[m]",
      "[m][sc]sidechaincompress=threshold=0.03:ratio=6:attack=20:release=350[mduck]"]
labels = ["[v]", "[mduck]"]
for k, (t, name, vol) in enumerate(sfx):
    inputs += ["-i", os.path.join(SFX, name + ".mp3")]
    d = int(t * 1000)
    fl.append(f"[{k + 2}:a]aresample={SR},aformat=channel_layouts=mono,volume={vol},adelay={d}|{d}[s{k}]")
    labels.append(f"[s{k}]")
fl.append("".join(labels) + f"amix=inputs={len(labels)}:normalize=0:duration=first,atrim=duration={total},loudnorm=I=-14:TP=-1.5:LRA=8[out]")
out = os.path.join(HERE, "montage_video_voix_pro.mp3")
run("ffmpeg", "-loglevel", "error", "-y", *inputs, "-filter_complex", ";".join(fl), "-map", "[out]", "-ar", str(SR), "-b:a", "192k", out)
json.dump({"debut_voix": T0, "fin_voix": END, "parties": marks, "duree": total}, open(os.path.join(HERE, "reperes.json"), "w"), indent=1)
print(f"brut {len(y) / SR + START:.1f} s -> final {total:.1f} s ; parties à {[round(m, 1) for m in marks]}")
