"""Musique + bruitages : mardi 13 h, 3 erreurs sur vos statuts (22 s), sans voix."""
import os, subprocess

ROOT = os.path.dirname(os.path.abspath(__file__))
SFX_DIR = os.path.join(ROOT, "..", "..", "..", "video-excel-13h", "assets", "sfx")
MUSIC = os.path.join(ROOT, "..", "..", "..", "video-excel-13h", "assets", "audio", "musique.wav")
OUT = os.path.join(ROOT, "assets", "audio", "mix.wav")
DUR = 22.0
SFX = [(0.1, "whoosh-short", 0.2), (0.25, "whoosh", 0.25), (0.8, "pop", 0.22), (1.55, "impact-bass-1", 0.25), (1.95, "impact-bass-2", 0.25), (2.4, "pop", 0.18),
       (3.15, "whoosh-cinematic", 0.3), (3.45, "pop", 0.2), (3.6, "impact-bass-2", 0.32), (4.1, "whoosh-short", 0.18),
       (5.2, "whoosh", 0.28), (5.25, "pop", 0.2), (5.55, "impact-bass-1", 0.25), (5.8, "whoosh-short", 0.22), (6.6, "click", 0.2), (6.9, "whoosh-short", 0.3), (7.4, "ping", 0.25),
       (9.2, "whoosh", 0.28), (9.25, "pop", 0.2), (9.55, "impact-bass-1", 0.25), (9.8, "whoosh-short", 0.22), (10.2, "whoosh-short", 0.22), (10.9, "whoosh-short", 0.3), (11.2, "sparkle", 0.22), (11.6, "ping", 0.25),
       (13.6, "whoosh", 0.28), (13.65, "pop", 0.2), (13.95, "impact-bass-1", 0.25), (14.2, "pop", 0.22), (14.6, "whoosh-short", 0.3), (15.4, "ping", 0.25),
       (17.15, "whoosh-cinematic", 0.3), (17.6, "whoosh", 0.25), (17.75, "impact-bass-2", 0.25), (18.3, "typing", 0.3), (19.0, "click", 0.25), (19.1, "notification", 0.3), (19.7, "notification", 0.22),
       (20.0, "pop", 0.25), (20.6, "chime", 0.3)]

os.makedirs(os.path.dirname(OUT), exist_ok=True)
inputs = ["-i", MUSIC]
fl = [f"[0:a]aresample=44100,aformat=channel_layouts=stereo,atrim=duration={DUR},volume=0.85,afade=t=in:d=0.5,afade=t=out:st={DUR - 1.2}:d=1.2[mus]"]
labels = ["[mus]"]
for i, (t, name, vol) in enumerate(SFX):
    inputs += ["-i", os.path.join(SFX_DIR, f"{name}.mp3")]
    d = int(t * 1000)
    extra = ",atrim=duration=0.7" if name == "typing" else ""
    fl.append(f"[{i + 1}:a]aresample=44100,aformat=channel_layouts=stereo{extra},volume={vol},adelay={d}|{d}[s{i}]")
    labels.append(f"[s{i}]")
fl.append("".join(labels) + f"amix=inputs={len(labels)}:normalize=0:duration=first,apad,atrim=duration={DUR},loudnorm=I=-14:TP=-1.5:LRA=11[out]")
subprocess.run(["ffmpeg", "-y", "-loglevel", "error"] + inputs + ["-filter_complex", ";".join(fl), "-map", "[out]", "-ar", "44100", OUT], check=True)
print("ok", OUT)
