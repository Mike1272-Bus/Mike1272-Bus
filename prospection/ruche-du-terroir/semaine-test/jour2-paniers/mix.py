"""Musique + bruitages du jour 2 (paniers cadeaux pour les entreprises, motion design), 20 s, sans voix."""
import os, subprocess

ROOT = os.path.dirname(os.path.abspath(__file__))
SFX_DIR = os.path.join(ROOT, "..", "..", "..", "..", "video-excel-13h", "assets", "sfx")
MUSIC = os.path.join(ROOT, "..", "..", "..", "..", "video-excel-13h", "assets", "audio", "musique.wav")
OUT = os.path.join(ROOT, "assets", "audio", "mix.wav")
DUR = 20.0
SFX = [(0.1, "whoosh-short", 0.25), (0.6, "pop", 0.22), (0.9, "impact-bass-1", 0.22), (1.4, "whoosh-short", 0.2), (1.6, "whoosh-short", 0.2),
       (2.7, "whoosh", 0.3), (3.3, "whoosh-short", 0.22), (3.65, "pop", 0.22), (4.1, "click-soft", 0.2),
       (4.2, "riser", 0.25), (4.6, "whoosh-cinematic", 0.35), (5.45, "impact-bass-2", 0.3), (5.5, "pop", 0.15), (5.65, "pop", 0.15),
       (6.05, "whoosh-short", 0.25), (6.5, "sparkle", 0.25), (6.7, "pop", 0.18), (7.9, "sparkle", 0.18),
       (9.0, "whoosh", 0.3), (10.3, "whoosh-short", 0.22), (9.4, "pop", 0.2), (10.8, "pop", 0.22),
       (12.2, "whoosh", 0.3), (13.0, "whoosh-short", 0.25), (13.45, "ping", 0.2), (13.75, "whoosh-short", 0.25), (14.2, "ping", 0.2), (14.5, "whoosh-short", 0.25), (14.95, "ping", 0.2),
       (16.0, "whoosh-cinematic", 0.3), (16.5, "typing", 0.3), (17.5, "click", 0.25), (17.65, "notification", 0.3), (17.9, "impact-bass-1", 0.2), (18.5, "pop", 0.25), (19.1, "chime", 0.3)]

os.makedirs(os.path.dirname(OUT), exist_ok=True)
inputs = ["-i", MUSIC]
fl = [f"[0:a]aresample=44100,aformat=channel_layouts=stereo,atrim=duration={DUR},volume=0.85,afade=t=in:d=0.5,afade=t=out:st={DUR - 1.2}:d=1.2[mus]"]
labels = ["[mus]"]
for i, (t, name, vol) in enumerate(SFX):
    inputs += ["-i", os.path.join(SFX_DIR, f"{name}.mp3")]
    d = int(t * 1000)
    extra = ",atrim=duration=1.0" if name == "typing" else ""
    fl.append(f"[{i + 1}:a]aresample=44100,aformat=channel_layouts=stereo{extra},volume={vol},adelay={d}|{d}[s{i}]")
    labels.append(f"[s{i}]")
fl.append("".join(labels) + f"amix=inputs={len(labels)}:normalize=0:duration=first,apad,atrim=duration={DUR},loudnorm=I=-14:TP=-1.5:LRA=11[out]")
subprocess.run(["ffmpeg", "-y", "-loglevel", "error"] + inputs + ["-filter_complex", ";".join(fl), "-map", "[out]", "-ar", "44100", OUT], check=True)
print("ok", OUT)
