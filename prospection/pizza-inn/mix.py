"""Musique + bruitages : Pizza Inn (26,5 s), sans voix : musique et quelques sons discrets (whoosh, pops, carillon), pas de bruitages gourmands."""
import os, subprocess

ROOT = os.path.dirname(os.path.abspath(__file__))
SFX_DIR = os.path.join(ROOT, "..", "..", "video-excel-13h", "assets", "sfx")
MUSIC = os.path.join(ROOT, "..", "..", "video-excel-13h", "assets", "audio", "musique.wav")
OUT = os.path.join(ROOT, "assets", "audio", "mix.wav")
DUR = 26.5
SFX = [(0.3, "whoosh-short", 0.15), (3.4, "whoosh-cinematic", 0.25), (3.5, "pop", 0.25), (6.8, "whoosh-cinematic", 0.25), (7.0, "whoosh", 0.25),
       (12.0, "whoosh-cinematic", 0.25), (12.2, "whoosh", 0.25)] + [(13.4 + i * 0.3, "pop", 0.16) for i in range(5)]
SFX += [(17.5, "whoosh-cinematic", 0.25)] + [(18.3 + i * 0.6, "ping", 0.2) for i in range(3)]
SFX += [(21.8, "whoosh-cinematic", 0.28), (21.9, "pop", 0.25), (23.2, "whoosh-short", 0.2), (23.4, "whoosh-short", 0.2), (24.0, "chime", 0.3)]

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
