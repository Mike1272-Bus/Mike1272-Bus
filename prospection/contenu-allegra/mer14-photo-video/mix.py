"""Musique + bruitages : mercredi 13 h, photo ou vidéo ? (22 s), sans voix."""
import os, subprocess

ROOT = os.path.dirname(os.path.abspath(__file__))
SFX_DIR = os.path.join(ROOT, "..", "..", "..", "video-excel-13h", "assets", "sfx")
MUSIC = os.path.join(ROOT, "..", "..", "..", "video-excel-13h", "assets", "audio", "musique.wav")
OUT = os.path.join(ROOT, "assets", "audio", "mix.wav")
DUR = 22.0
SFX = [(0.1, "whoosh-short", 0.2), (0.2, "whoosh", 0.25), (0.5, "riser", 0.18), (1.2, "pop", 0.2), (1.7, "impact-bass-1", 0.25), (2.1, "impact-bass-2", 0.28),
       (3.15, "whoosh-cinematic", 0.3), (3.45, "pop", 0.2), (3.6, "impact-bass-1", 0.28), (4.15, "impact-bass-2", 0.32),
       (5.45, "whoosh-short", 0.2), (5.85, "impact-bass-1", 0.22), (6.1, "whoosh", 0.25), (6.45, "whoosh", 0.25), (6.7, "pop", 0.18),
       (7.6, "whoosh-short", 0.32), (8.0, "pop", 0.2), (8.25, "ping", 0.25), (8.7, "sparkle", 0.22),
       (10.3, "impact-bass-2", 0.3), (10.9, "whoosh", 0.25), (11.6, "whoosh", 0.25), (12.3, "whoosh", 0.25), (13.0, "pop", 0.15),
       (14.25, "whoosh-short", 0.2), (14.5, "whoosh", 0.25), (14.65, "pop", 0.2), (15.1, "pop", 0.2), (15.6, "click", 0.25),
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
