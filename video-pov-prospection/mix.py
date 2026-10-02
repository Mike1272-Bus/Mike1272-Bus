"""Musique + bruitages de la vidéo POV prospection (sans voix), 30 s."""
import os, subprocess

ROOT = os.path.dirname(os.path.abspath(__file__))
SFX_DIR = os.path.join(ROOT, "..", "video-excel-13h", "assets", "sfx")
MUSIC = os.path.join(ROOT, "assets", "audio", "musique.wav")
OUT = os.path.join(ROOT, "assets", "audio", "mix.wav")
DUR = 30.0
SFX = [(0.1, "pop", 0.3), (0.45, "whoosh-short", 0.25), (1.0, "whoosh", 0.3), (3.3, "whoosh-cinematic", 0.3),
       (3.7, "pop", 0.3), (3.95, "whoosh-short", 0.3), (4.45, "typing", 0.25), (6.05, "pop", 0.15), (6.3, "pop", 0.15), (6.55, "pop", 0.15),
       (7.0, "impact-bass-1", 0.3), (7.05, "chime", 0.2), (8.2, "whoosh", 0.3), (8.6, "pop", 0.3), (9.1, "whoosh-cinematic", 0.3),
       (10.2, "sparkle", 0.25), (15.0, "whoosh", 0.3), (15.3, "pop", 0.3), (16.1, "notification", 0.3), (16.6, "whoosh-short", 0.25),
       (17.5, "click-soft", 0.3), (18.3, "impact-bass-1", 0.3), (20.5, "whoosh", 0.3), (20.75, "whoosh-short", 0.3),
       (22.6, "glitch-1", 0.15), (23.7, "whoosh-cinematic", 0.3), (24.2, "pop", 0.3), (26.3, "key-press", 0.35), (26.9, "click", 0.3),
       (27.0, "impact-bass-1", 0.3), (27.05, "sparkle", 0.25), (28.0, "chime", 0.25)]

inputs = ["-i", MUSIC]
fl = [f"[0:a]aresample=44100,aformat=channel_layouts=stereo,atrim=duration={DUR},volume=0.9,afade=t=in:d=0.4,afade=t=out:st={DUR - 1.5}:d=1.5[mus]"]
labels = ["[mus]"]
for i, (t, name, vol) in enumerate(SFX):
    inputs += ["-i", os.path.join(SFX_DIR, f"{name}.mp3")]
    d = int(t * 1000)
    fl.append(f"[{i + 1}:a]aresample=44100,aformat=channel_layouts=stereo,volume={vol},adelay={d}|{d}[s{i}]")
    labels.append(f"[s{i}]")
fl.append("".join(labels) + f"amix=inputs={len(labels)}:normalize=0:duration=first,apad,atrim=duration={DUR},loudnorm=I=-14:TP=-1.5:LRA=11[out]")
subprocess.run(["ffmpeg", "-y", "-loglevel", "error"] + inputs + ["-filter_complex", ";".join(fl), "-map", "[out]", "-ar", "44100", OUT], check=True)
print("ok", OUT)
