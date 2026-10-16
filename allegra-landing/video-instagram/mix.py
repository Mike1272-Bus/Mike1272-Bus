"""Musique + bruitages : présentation Allegra pour Instagram (29 s), sans voix."""
import os, subprocess
ROOT = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.join(ROOT, "..", "..")
SFX_DIR = os.path.join(REPO, "video-excel-13h", "assets", "sfx")
MUSIC = os.path.join(REPO, "video-excel-13h", "assets", "audio", "musique.wav")
OUT = os.path.join(ROOT, "assets", "audio", "mix.wav")
DUR = 32.0
SHIFT = 3.6
SFX = [(0.1, "pop", 0.22), (0.25, "pop", 0.2), (0.4, "whoosh-short", 0.2), (1.2, "impact-bass-1", 0.3), (1.45, "impact-bass-2", 0.28), (2.2, "click", 0.25),
       (3.1, "whoosh-cinematic", 0.3), (3.6, "whoosh", 0.22), (3.75, "whoosh", 0.18), (3.9, "whoosh", 0.18), (4.5, "sparkle", 0.3), (4.55, "impact-bass-1", 0.25),
       (5.2, "pop", 0.2), (5.3, "whoosh-short", 0.2), (5.45, "whoosh-short", 0.18), (5.6, "whoosh-short", 0.18),
       (7.7, "whoosh-cinematic", 0.3), (8.55, "impact-bass-2", 0.28), (9.2, "whoosh", 0.22), (9.6, "pop", 0.2), (9.85, "pop", 0.2), (10.0, "whoosh", 0.22), (10.45, "sparkle", 0.25),
       (12.3, "whoosh-cinematic", 0.3), (13.15, "impact-bass-1", 0.28), (13.5, "whoosh-short", 0.2), (13.9, "pop", 0.2), (14.1, "whoosh-short", 0.2), (14.75, "pop", 0.22), (15.0, "sparkle", 0.3), (15.05, "impact-bass-2", 0.25),
       (16.7, "whoosh-cinematic", 0.3), (17.55, "impact-bass-1", 0.28)] + [(17.95 + i * 0.22, "pop", 0.15) for i in range(9)] + [
       (21.1, "whoosh-cinematic", 0.3), (21.9, "impact-bass-2", 0.28), (22.15, "whoosh", 0.25), (22.75, "click", 0.22), (23.05, "click", 0.22), (23.35, "click", 0.22), (23.8, "impact-bass-1", 0.3),
       (24.5, "whoosh-cinematic", 0.3), (24.85, "impact-bass-2", 0.3), (25.6, "impact-bass-1", 0.25), (26.3, "pop", 0.25), (26.6, "notification", 0.3), (27.0, "chime", 0.3)]
SFX = [(t + SHIFT if t >= 3.4 else t, n, v) for t, n, v in SFX] + [
    (3.6, "impact-bass-2", 0.28), (3.65, "sparkle", 0.28), (4.5, "click", 0.22), (5.1, "pop", 0.22), (5.3, "pop", 0.22), (5.5, "pop", 0.22), (5.9, "impact-bass-1", 0.22), (6.7, "whoosh-cinematic", 0.3)]
WARP = [(0, 0), (3.4, 2.9), (7.0, 6.95), (11.6, 11.15), (16.2, 16.28), (20.6, 19.64), (25.0, 24.82), (28.4, 27.08), (32.6, 32.0)]
def W(t):
    for (a, x), (b, y) in zip(WARP, WARP[1:]):
        if t <= b: return x + (t - a) * (y - x) / (b - a)
    return t
SFX = [(round(W(t), 3), n, v * 0.8) for t, n, v in SFX]
VOIX = os.path.join(ROOT, "assets", "audio", "voix_brute.mp3")
V0 = 0.2  # la voix commence à 0,2 s
os.makedirs(os.path.dirname(OUT), exist_ok=True)
inputs = ["-i", MUSIC]
fl = [f"[0:a]aresample=44100,aformat=channel_layouts=stereo,atrim=duration={DUR},volume='if(between(t,0.1,30.6),0.32,0.8)':eval=frame,afade=t=in:d=0.4,afade=t=out:st={DUR - 1.5}:d=1.5[mus]"]
labels = ["[mus]"]
for i, (t, name, vol) in enumerate(SFX):
    inputs += ["-i", os.path.join(SFX_DIR, f"{name}.mp3")]
    d = int(t * 1000)
    fl.append(f"[{i + 1}:a]aresample=44100,aformat=channel_layouts=stereo,volume={vol},adelay={d}|{d}[s{i}]")
    labels.append(f"[s{i}]")
inputs += ["-i", VOIX]
nv = len(SFX) + 1
fl.append(f"[{nv}:a]aresample=44100,aformat=channel_layouts=stereo,highpass=f=80,equalizer=f=3500:t=q:w=1:g=2,acompressor=threshold=-18dB:ratio=3:attack=5:release=80,volume=1.5,adelay={int(V0*1000)}|{int(V0*1000)}[voix]")
labels.append("[voix]")
fl.append("".join(labels) + f"amix=inputs={len(labels)}:normalize=0:duration=first,apad,atrim=duration={DUR},loudnorm=I=-14:TP=-1.5:LRA=11[out]")
subprocess.run(["ffmpeg", "-y", "-loglevel", "error"] + inputs + ["-filter_complex", ";".join(fl), "-map", "[out]", "-ar", "44100", OUT], check=True)
print("ok", OUT)
