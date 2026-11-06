"""Musique + bruitages de la vidéo Epicé Bon (sans voix), 20 s."""
import os, subprocess

ROOT = os.path.dirname(os.path.abspath(__file__))
SFX_DIR = os.path.join(ROOT, "..", "..", "video-excel-13h", "assets", "sfx")
MUSIC = os.path.join(ROOT, "..", "..", "video-excel-13h", "assets", "audio", "musique.wav")
OUT = os.path.join(ROOT, "assets", "audio", "mix.wav")
DUR = 20.0
SFX = [(0.2, "whoosh-cinematic", 0.35), (1.0, "impact-bass-1", 0.28), (1.25, "sparkle", 0.22), (2.0, "whoosh-short", 0.22),
       (3.1, "whoosh", 0.40), (3.45, "whoosh-short", 0.32), (3.7, "impact-bass-2", 0.18), (7.2, "whoosh-cinematic", 0.30),
       (8.1, "whoosh-short", 0.30), (8.4, "pop", 0.18), (9.75, "whoosh-short", 0.25), (10.15, "pop", 0.18), (10.4, "pop", 0.18),
       (10.75, "click-soft", 0.35), (11.6, "whoosh", 0.35), (12.35, "impact-bass-1", 0.30), (12.8, "whoosh-short", 0.22),
       (13.2, "pop", 0.2), (13.37, "pop", 0.2), (13.54, "pop", 0.2), (13.71, "pop", 0.2), (13.88, "pop", 0.2),
       (14.3, "whoosh-short", 0.25), (14.5, "click-soft", 0.25), (15.7, "whoosh-cinematic", 0.30),
       (16.2, "whoosh-short", 0.3), (17.45, "chime", 0.30), (17.5, "click-soft", 0.25)]

os.makedirs(os.path.dirname(OUT), exist_ok=True)
inputs = ["-i", MUSIC]
fl = [f"[0:a]aresample=44100,aformat=channel_layouts=stereo,atrim=duration={DUR},volume=0.9,afade=t=in:d=0.6,afade=t=out:st={DUR - 1.6}:d=1.6[mus]"]
labels = ["[mus]"]
for i, (t, name, vol) in enumerate(SFX):
    inputs += ["-i", os.path.join(SFX_DIR, f"{name}.mp3")]
    d = int(t * 1000)
    fl.append(f"[{i + 1}:a]aresample=44100,aformat=channel_layouts=stereo,volume={vol},adelay={d}|{d}[s{i}]")
    labels.append(f"[s{i}]")
fl.append("".join(labels) + f"amix=inputs={len(labels)}:normalize=0:duration=first,apad,atrim=duration={DUR},loudnorm=I=-14:TP=-1.5:LRA=11[out]")
subprocess.run(["ffmpeg", "-y", "-loglevel", "error"] + inputs + ["-filter_complex", ";".join(fl), "-map", "[out]", "-ar", "44100", OUT], check=True)
print("ok", OUT)
