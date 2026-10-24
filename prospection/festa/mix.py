"""Musique + bruitages de la vidéo Festa (sans voix), 20 s."""
import os, subprocess

ROOT = os.path.dirname(os.path.abspath(__file__))
SFX_DIR = os.path.join(ROOT, "..", "..", "video-excel-13h", "assets", "sfx")
MUSIC = os.path.join(ROOT, "..", "..", "video-excel-13h", "assets", "audio", "musique.wav")
OUT = os.path.join(ROOT, "assets", "audio", "mix.wav")
DUR = 20.0
SFX = [(0.15, "pop", 0.25), (0.3, "whoosh-cinematic", 0.35), (1.0, "impact-bass-1", 0.25), (1.85, "whoosh-short", 0.25), (2.05, "sparkle", 0.25),
       (2.1, "pop", 0.2), (2.4, "pop", 0.2), (3.25, "whoosh", 0.4), (3.7, "whoosh-short", 0.3), (4.3, "impact-bass-2", 0.3),
       (4.75, "whoosh", 0.35), (4.9, "pop", 0.25), (5.1, "pop", 0.18), (5.3, "pop", 0.18), (7.45, "whoosh-cinematic", 0.3),
       (8.1, "pop", 0.22), (8.85, "click-soft", 0.3), (9.25, "glitch-1", 0.22), (9.3, "whoosh", 0.35), (11.5, "whoosh", 0.35),
       (12.2, "impact-bass-1", 0.25), (12.6, "pop", 0.2), (12.74, "pop", 0.2), (12.88, "pop", 0.2), (13.02, "pop", 0.2), (13.1, "sparkle", 0.18),
       (15.7, "whoosh-cinematic", 0.3), (16.2, "pop", 0.2), (16.3, "whoosh-short", 0.3), (17.3, "whoosh-short", 0.22), (17.42, "chime", 0.3), (18.1, "pop", 0.25)]

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
