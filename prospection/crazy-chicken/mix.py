"""Musique + bruitages : Crazy Chicken, seau de poulet (20 s), sans voix."""
import os, subprocess

ROOT = os.path.dirname(os.path.abspath(__file__))
SFX_DIR = os.path.join(ROOT, "..", "..", "video-excel-13h", "assets", "sfx")
MUSIC = os.path.join(ROOT, "..", "..", "video-excel-13h", "assets", "audio", "musique.wav")
OUT = os.path.join(ROOT, "assets", "audio", "mix.wav")
DUR = 20.0
SFX = [(0.1, "pop", 0.22), (0.35, "whoosh-short", 0.2), (0.75, "impact-bass-1", 0.28), (1.15, "impact-bass-2", 0.3), (1.6, "glitch-1", 0.12),
       (2.6, "whoosh-cinematic", 0.3), (2.7, "pop", 0.15), (3.0, "impact-bass-1", 0.28), (3.4, "whoosh", 0.28), (3.85, "impact-bass-2", 0.35), (3.9, "pop", 0.18), (4.2, "sparkle", 0.25), (4.9, "pop", 0.15), (5.2, "pop", 0.15),
       (7.6, "whoosh-cinematic", 0.3), (7.7, "whoosh", 0.28), (8.1, "impact-bass-1", 0.3), (8.45, "impact-bass-2", 0.25), (8.9, "pop", 0.15),
       (11.6, "whoosh-cinematic", 0.28), (11.65, "impact-bass-1", 0.25), (12.4, "whoosh", 0.25), (12.9, "whoosh", 0.25),
       (14.6, "whoosh-cinematic", 0.3), (14.7, "pop", 0.25), (15.2, "impact-bass-2", 0.32), (15.9, "whoosh", 0.25), (16.1, "whoosh", 0.25), (16.8, "pop", 0.25), (17.4, "chime", 0.3)]

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
