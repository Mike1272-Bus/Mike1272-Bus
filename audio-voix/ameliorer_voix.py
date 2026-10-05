"""Nettoie une voix déjà passée dans un outil qui coupe les silences à zéro.
1. coupe l'intro sonore de l'outil ; 2. raccourcit les trous de silence ; 3. ajoute un fond de pièce très léger ;
4. égalise et cale le volume pour les réseaux."""
import subprocess, sys
import numpy as np

SRC, OUT, START = sys.argv[1], sys.argv[2], float(sys.argv[3]) if len(sys.argv) > 3 else 0.0
SR = 44100
y = np.frombuffer(subprocess.run(["ffmpeg", "-loglevel", "error", "-i", SRC, "-f", "f32le", "-ac", "1", "-ar", str(SR), "-"],
                                 capture_output=True, check=True).stdout, np.float32).copy()
y = y[int(START * SR):]

# trous de silence numérique (son exactement à zéro)
z = np.abs(y) < 1e-6
d = np.diff(np.concatenate([[0], z.astype(np.int8), [0]]))
starts, ends = np.where(d == 1)[0], np.where(d == -1)[0]
KEEP, MIN = int(0.28 * SR), int(0.30 * SR)  # un trou plus long que 0,30 s est ramené à 0,28 s
FADE = int(0.012 * SR)
out, pos = [], 0
for s, e in zip(starts, ends):
    if e - s >= MIN:
        seg = y[pos:s].copy()
        if len(seg) > 2 * FADE:  # petit fondu pour éviter le « clac » de la coupure
            seg[-FADE:] *= np.linspace(1, 0, FADE)
            seg[:FADE] *= np.linspace(0, 1, FADE) if pos else 1
        out += [seg, np.zeros(KEEP, np.float32)]
        pos = e
seg = y[pos:].copy()
if len(seg) > FADE: seg[:FADE] *= np.linspace(0, 1, FADE)
out.append(seg)
v = np.concatenate(out)

# fond de pièce : bruit rose filtré, très bas (environ -56 dBFS)
rng = np.random.default_rng(7)
w = rng.standard_normal(len(v) + SR).astype(np.float32)
f = np.fft.rfftfreq(len(w), 1 / SR); W = np.fft.rfft(w)
W[1:] /= np.sqrt(f[1:]); W[(f < 120) | (f > 5000)] = 0
pink = np.fft.irfft(W, len(w))[:len(v)].astype(np.float32)
pink *= 10 ** (-56 / 20) / (np.sqrt(np.mean(pink ** 2)) + 1e-12)
v = v + pink

tmp = OUT + ".tmp.wav"
subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-f", "f32le", "-ar", str(SR), "-ac", "1", "-i", "-", tmp], input=v.tobytes(), check=True)
chain = ("highpass=f=80,equalizer=f=250:t=q:w=1.2:g=-3,equalizer=f=3500:t=q:w=1.0:g=4,equalizer=f=6500:t=q:w=1.0:g=2,"
         "acompressor=threshold=-20dB:ratio=2.5:attack=8:release=120:makeup=1,loudnorm=I=-14:TP=-1.5:LRA=7")
subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", tmp, "-af", chain, "-ar", str(SR), "-b:a", "192k", OUT], check=True)
import os; os.remove(tmp)
print(f"ok {OUT} : {len(y) / SR:.1f} s -> {len(v) / SR:.1f} s, {sum(1 for s, e in zip(starts, ends) if e - s >= MIN)} trous raccourcis")
