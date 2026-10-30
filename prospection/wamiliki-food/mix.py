"""Musique + bruitages : Wamiliki Food, tacos et poulet mayo (20 s), sans voix."""
import os, subprocess

ROOT = os.path.dirname(os.path.abspath(__file__))
SFX_DIR = os.path.join(ROOT, "..", "..", "video-excel-13h", "assets", "sfx")
MUSIC = os.path.join(ROOT, "..", "..", "video-excel-13h", "assets", "audio", "musique.wav")
OUT = os.path.join(ROOT, "assets", "audio", "mix.wav")
DUR = 20.0
SFX = [(0.1, "pop", 0.25), (0.6, "whoosh-short", 0.2), (0.95, "impact-bass-1", 0.28), (1.35, "impact-bass-2", 0.3), (2.8, "whoosh-cinematic", 0.28), (3.1, "impact-bass-1", 0.28), (3.4, "whoosh", 0.28), (3.95, "impact-bass-2", 0.3), (4.3, "sparkle", 0.22), (7.0, "whoosh-cinematic", 0.28), (7.05, "whoosh", 0.25), (7.7, "impact-bass-1", 0.3), (10.4, "whoosh-cinematic", 0.28), (10.7, "impact-bass-1", 0.28), (11.0, "whoosh", 0.25), (11.5, "impact-bass-2", 0.3), (11.8, "sparkle", 0.2), (14.6, "whoosh-cinematic", 0.3), (14.7, "pop", 0.25), (15.1, "impact-bass-2", 0.3), (15.7, "whoosh", 0.25), (15.85, "whoosh", 0.22), (16.3, "pop", 0.25), (16.7, "whoosh-short", 0.22), (17.3, "chime", 0.3)]

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
