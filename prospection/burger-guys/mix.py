"""Musique + bruitages de la vidéo Burger Guys (sans voix), 22 s."""
import os, subprocess

ROOT = os.path.dirname(os.path.abspath(__file__))
SFX_DIR = os.path.join(ROOT, "..", "..", "video-excel-13h", "assets", "sfx")
MUSIC = os.path.join(ROOT, "..", "..", "video-cuisine-19h", "assets", "audio", "musique.wav")
OUT = os.path.join(ROOT, "assets", "audio", "mix.wav")
DUR = 22.0
SFX = [(0.1, "whoosh-short", 0.3), (0.62, "impact-bass-2", 0.32), (1.3, "whoosh", 0.3)]
for i in range(5):
    t = 1.45 + i * 1.05
    SFX += [(t, "whoosh-short", 0.3), (t + 0.4, "pop", 0.25)]
SFX += [(6.75, "whoosh-cinematic", 0.35), (7.25, "impact-bass-1", 0.4), (7.5, "sparkle", 0.28),
        (9.55, "whoosh", 0.32), (10.1, "whoosh-short", 0.3), (10.35, "pop", 0.22), (10.85, "whoosh-short", 0.3), (11.45, "whoosh-short", 0.3),
        (12.4, "whoosh-cinematic", 0.32), (12.85, "impact-bass-2", 0.3), (13.0, "pop", 0.22),
        (14.2, "whoosh", 0.32), (14.4, "whoosh-short", 0.28), (15.0, "glitch-1", 0.18), (15.7, "click-soft", 0.22),
        (17.5, "whoosh-cinematic", 0.32), (17.95, "sparkle", 0.28), (18.4, "pop", 0.25), (18.6, "whoosh", 0.28), (19.0, "chime", 0.3)]
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
