"""Musique + bruitages : Biloko (22 s), sans voix : musique et quelques sons d'appli (clic, notification), pas de bruitages gourmands."""
import os, subprocess

ROOT = os.path.dirname(os.path.abspath(__file__))
SFX_DIR = os.path.join(ROOT, "..", "..", "video-excel-13h", "assets", "sfx")
MUSIC = os.path.join(ROOT, "..", "..", "video-excel-13h", "assets", "audio", "musique.wav")
OUT = os.path.join(ROOT, "assets", "audio", "mix.wav")
DUR = 22.0
SFX = [(0.1, "whoosh-short", 0.15), (0.7, "pop", 0.15), (3.6, "whoosh-cinematic", 0.25), (4.0, "pop", 0.25), (4.9, "click", 0.5), (5.1, "impact-bass-1", 0.28),
       (6.7, "whoosh", 0.3), (7.8, "whoosh-cinematic", 0.25), (8.2, "pop", 0.2), (8.5, "pop", 0.2), (8.8, "whoosh-short", 0.15), (11.75, "ping", 0.3),
       (12.4, "whoosh-cinematic", 0.25), (12.5, "notification", 0.55), (13.2, "whoosh", 0.25), (16.8, "whoosh-cinematic", 0.28), (16.9, "pop", 0.25),
       (17.8, "pop", 0.2), (17.95, "pop", 0.2), (18.7, "whoosh-short", 0.22), (19.4, "chime", 0.3)]

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
