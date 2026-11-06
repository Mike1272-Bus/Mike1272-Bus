"""Musique + bruitages de la vidéo Les Délices d'Émilie (sans voix), 24 s."""
import os, subprocess

ROOT = os.path.dirname(os.path.abspath(__file__))
SFX_DIR = os.path.join(ROOT, "..", "..", "video-excel-13h", "assets", "sfx")
MUSIC = os.path.join(ROOT, "..", "..", "video-excel-13h", "assets", "audio", "musique.wav")
OUT = os.path.join(ROOT, "assets", "audio", "mix.wav")
DUR = 24.0
SFX = [(0.15, "whoosh-cinematic", 0.35), (0.95, "impact-bass-1", 0.22), (1.3, "sparkle", 0.2), (2.6, "whoosh", 0.32),
       (3.1, "whoosh-short", 0.28), (3.3, "whoosh", 0.3),
       (4.3, "pop", 0.25), (5.0, "pop", 0.25), (5.7, "pop", 0.25), (6.4, "pop", 0.25), (6.9, "chime", 0.2), (7.45, "whoosh", 0.35),
       (8.05, "whoosh-short", 0.3), (9.0, "impact-bass-2", 0.2), (9.6, "impact-bass-2", 0.2), (10.2, "impact-bass-2", 0.22), (11.65, "whoosh", 0.35),
       (12.3, "whoosh-short", 0.3), (13.1, "pop", 0.22), (13.5, "pop", 0.22), (13.9, "pop", 0.22), (14.3, "pop", 0.22), (14.7, "pop", 0.22),
       (14.9, "whoosh-cinematic", 0.25), (15.95, "sparkle", 0.3), (16.2, "sparkle", 0.25), (17.6, "whoosh", 0.3),
       (18.1, "whoosh-short", 0.28), (18.6, "click-soft", 0.2), (19.0, "whoosh-short", 0.25), (19.85, "pop", 0.2), (20.4, "whoosh-short", 0.25), (20.9, "chime", 0.3)]

os.makedirs(os.path.dirname(OUT), exist_ok=True)
inputs = ["-stream_loop", "-1", "-i", MUSIC]
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
