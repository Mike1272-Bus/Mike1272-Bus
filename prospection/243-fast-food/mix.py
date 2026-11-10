"""Musique + bruitages : +243 Fast Food (23,5 s), sans voix. Les noms en « + » sont nos bruitages gourmands (bruitages.py)."""
import os, subprocess

ROOT = os.path.dirname(os.path.abspath(__file__))
SFX_DIR = os.path.join(ROOT, "..", "..", "video-excel-13h", "assets", "sfx")
MUSIC = os.path.join(ROOT, "..", "..", "video-excel-13h", "assets", "audio", "musique.wav")
OUT = os.path.join(ROOT, "assets", "audio", "mix.wav")
DUR = 23.5
SFX = [(0.1, "pop", 0.25), (0.55, "whoosh-short", 0.2), (0.85, "impact-bass-1", 0.28), (1.25, "impact-bass-2", 0.3),
       (2.4, "whoosh-cinematic", 0.28), (2.5, "whoosh-short", 0.2)]
SFX += [(2.7 + i * 0.32, "pop", 0.14) for i in range(6)]
SFX += [(3.0 + i * 0.55, "whoosh-short", 0.16) for i in range(5)] + [(3.42 + i * 0.55, "+couche", 0.5) for i in range(5)]
SFX += [(5.6, "riser", 0.22), (6.05, "whoosh", 0.25), (6.85, "impact-bass-2", 0.32), (6.85, "+croquer", 0.75), (7.05, "impact-bass-1", 0.25),
        (7.3, "sparkle", 0.2), (7.4, "+gresillement", 0.3),
        (9.2, "whoosh-cinematic", 0.28), (9.5, "impact-bass-1", 0.28), (9.75, "whoosh", 0.25), (10.25, "+croquer", 0.7), (10.3, "+gresillement", 0.32),
        (12.4, "whoosh-cinematic", 0.28), (12.5, "impact-bass-2", 0.28)]
SFX += [(12.85 + i * 0.86, "whoosh-short", 0.15) for i in range(6)] + [(13.05 + i * 0.86, "+croustillant", 0.7) for i in range(6)]
SFX += [(18.4, "whoosh-cinematic", 0.26)] + [(18.6 + i * 0.12, "pop", 0.16) for i in range(4)]
SFX += [(19.9, "whoosh-cinematic", 0.3), (20.0, "pop", 0.25), (20.35, "impact-bass-2", 0.3), (20.95, "whoosh", 0.22), (21.3, "pop", 0.25),
        (21.6, "whoosh-short", 0.22), (22.1, "chime", 0.3)]

os.makedirs(os.path.dirname(OUT), exist_ok=True)
inputs = ["-i", MUSIC]
fl = [f"[0:a]aresample=44100,aformat=channel_layouts=stereo,atrim=duration={DUR},volume=0.8,afade=t=in:d=0.5,afade=t=out:st={DUR - 1.2}:d=1.2[mus]"]
labels = ["[mus]"]
for i, (t, name, vol) in enumerate(SFX):
    path = os.path.join(ROOT, "assets", "sfx", name[1:] + ".wav") if name.startswith("+") else os.path.join(SFX_DIR, f"{name}.mp3")
    inputs += ["-i", path]
    d = int(t * 1000)
    fl.append(f"[{i + 1}:a]aresample=44100,aformat=channel_layouts=stereo,volume={vol},adelay={d}|{d}[s{i}]")
    labels.append(f"[s{i}]")
fl.append("".join(labels) + f"amix=inputs={len(labels)}:normalize=0:duration=first,apad,atrim=duration={DUR},loudnorm=I=-14:TP=-1.5:LRA=11[out]")
subprocess.run(["ffmpeg", "-y", "-loglevel", "error"] + inputs + ["-filter_complex", ";".join(fl), "-map", "[out]", "-ar", "44100", OUT], check=True)
print("ok", OUT)
