"""Musique + bruitages du jour 1 v2 (texte du client, 25 s), sans voix."""
import os, subprocess

ROOT = os.path.dirname(os.path.abspath(__file__))
SFX_DIR = os.path.join(ROOT, "..", "..", "..", "..", "video-excel-13h", "assets", "sfx")
MUSIC = os.path.join(ROOT, "..", "..", "..", "..", "video-excel-13h", "assets", "audio", "musique.wav")
OUT = os.path.join(ROOT, "assets", "audio", "mix.wav")
DUR = 25.0
SFX = [(0.1, "pop", 0.22), (0.3, "whoosh-short", 0.22), (1.25, "impact-bass-1", 0.25), (2.0, "click-soft", 0.2),
       (3.0, "whoosh", 0.3), (3.15, "whoosh-short", 0.25), (3.6, "click", 0.2), (3.75, "whoosh-short", 0.25), (4.35, "whoosh-short", 0.25),
       (5.1, "impact-bass-2", 0.3), (5.5, "impact-bass-1", 0.25), (5.9, "pop", 0.22), (6.0, "riser", 0.2),
       (8.0, "whoosh-cinematic", 0.3), (8.05, "pop", 0.2), (8.75, "whoosh-short", 0.22),
       (9.6, "riser", 0.25), (10.0, "whoosh-cinematic", 0.35), (10.85, "impact-bass-2", 0.3), (10.9, "pop", 0.15), (11.05, "pop", 0.15),
       (11.45, "whoosh-short", 0.25), (11.9, "sparkle", 0.25), (12.1, "pop", 0.18), (13.3, "sparkle", 0.18),
       (14.4, "whoosh", 0.3), (15.2, "whoosh-short", 0.25), (15.65, "ping", 0.2), (16.0, "whoosh-short", 0.25), (16.45, "ping", 0.2), (16.8, "whoosh-short", 0.25), (17.25, "ping", 0.2),
       (18.6, "whoosh", 0.3), (19.7, "whoosh-short", 0.22), (20.2, "pop", 0.22),
       (21.4, "whoosh-cinematic", 0.3), (21.9, "typing", 0.3), (22.9, "click", 0.25), (23.05, "notification", 0.3), (23.2, "impact-bass-1", 0.2), (23.8, "pop", 0.25), (24.3, "chime", 0.3)]

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
