"""Musique + bruitages de la vidéo Tomela (sans voix), 20 s."""
import os, subprocess

ROOT = os.path.dirname(os.path.abspath(__file__))
SFX_DIR = os.path.join(ROOT, "..", "..", "video-excel-13h", "assets", "sfx")
MUSIC = os.path.join(ROOT, "..", "..", "video-excel-13h", "assets", "audio", "musique.wav")
OUT = os.path.join(ROOT, "assets", "audio", "mix.wav")
DUR = 20.0
SFX = [(0.2, "whoosh-cinematic", 0.35), (1.0, "impact-bass-1", 0.25), (1.3, "click-soft", 0.2), (1.65, "click-soft", 0.2), (2.0, "whoosh-short", 0.22),
       (3.1, "whoosh", 0.40), (3.45, "whoosh-short", 0.32), (3.75, "impact-bass-2", 0.18), (4.55, "click-soft", 0.22), (5.4, "click-soft", 0.22), (6.25, "click-soft", 0.22),
       (7.3, "whoosh-cinematic", 0.30), (8.1, "pop", 0.18), (8.4, "pop", 0.18), (9.55, "impact-bass-1", 0.3), (10.0, "whoosh-short", 0.25), (10.3, "sparkle", 0.2),
       (11.55, "whoosh", 0.35), (12.35, "impact-bass-2", 0.22), (12.75, "whoosh-short", 0.25), (12.97, "whoosh-short", 0.22), (13.19, "whoosh-short", 0.22),
       (13.9, "pop", 0.18), (15.7, "whoosh-cinematic", 0.30), (16.2, "whoosh-short", 0.3), (17.5, "chime", 0.30), (17.55, "click-soft", 0.25)]

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
