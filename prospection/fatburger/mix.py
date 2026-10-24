"""Musique + bruitages de la vidéo Fatburger (sans voix), 22 s."""
import os, subprocess

ROOT = os.path.dirname(os.path.abspath(__file__))
SFX_DIR = os.path.join(ROOT, "..", "..", "video-excel-13h", "assets", "sfx")
MUSIC = os.path.join(ROOT, "..", "..", "video-anglais-19h", "assets", "audio", "musique.wav")
OUT = os.path.join(ROOT, "assets", "audio", "mix.wav")
DUR = 22.0
SFX = [(0.15, "pop", 0.25), (0.39, "pop", 0.25), (1.2, "whoosh", 0.3)]
for i in range(7):
    t = 1.5 + i * 0.72
    SFX += [(t, "whoosh-short", 0.22), (t + 0.42, "impact-bass-2" if 1 <= i <= 3 else "pop", 0.3 if 1 <= i <= 3 else 0.25)]
SFX += [(2.52, "click-soft", 0.2), (3.24, "click-soft", 0.2), (3.96, "sparkle", 0.25),
        (6.3, "impact-bass-1", 0.35), (6.35, "sparkle", 0.28), (7.1, "whoosh-short", 0.28), (7.6, "pop", 0.22),
        (9.3, "whoosh", 0.32), (9.7, "whoosh-short", 0.25), (9.85, "whoosh-short", 0.25), (10.2, "pop", 0.22), (10.45, "pop", 0.22),
        (12.5, "whoosh-cinematic", 0.32), (12.75, "whoosh", 0.28), (13.4, "pop", 0.2),
        (15.5, "whoosh", 0.32), (15.7, "whoosh-short", 0.28), (16.3, "click-soft", 0.2),
        (18.2, "whoosh-cinematic", 0.32), (18.5, "sparkle", 0.28), (18.95, "pop", 0.25), (19.1, "whoosh", 0.28), (19.6, "chime", 0.3)]
os.makedirs(os.path.dirname(OUT), exist_ok=True)
inputs = ["-stream_loop", "-1", "-i", MUSIC]
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
