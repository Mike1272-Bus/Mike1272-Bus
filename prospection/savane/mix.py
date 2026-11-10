"""Musique + bruitages de la vidéo Savane (sans voix), 22 s."""
import os, subprocess

ROOT = os.path.dirname(os.path.abspath(__file__))
SFX_DIR = os.path.join(ROOT, "..", "..", "video-excel-13h", "assets", "sfx")
MUSIC = os.path.join(ROOT, "..", "..", "video-cuisine-13h", "assets", "audio", "musique.wav")
OUT = os.path.join(ROOT, "assets", "audio", "mix.wav")
DUR = 22.0
SFX = [(0.1, "whoosh-cinematic", 0.22), (0.55, "sparkle", 0.18), (2.55, "whoosh", 0.22), (5.2, "whoosh-short", 0.18),
       (9.8, "whoosh", 0.22), (11.1, "whoosh-short", 0.16), (12.4, "whoosh-short", 0.16), (13.7, "whoosh-short", 0.16),
       (15.0, "whoosh", 0.2), (16.75, "whoosh-cinematic", 0.22), (17.25, "sparkle", 0.18), (18.6, "chime", 0.22)]
os.makedirs(os.path.dirname(OUT), exist_ok=True)
inputs = ["-stream_loop", "-1", "-i", MUSIC]
fl = [f"[0:a]aresample=44100,aformat=channel_layouts=stereo,atrim=duration={DUR},volume=0.85,afade=t=in:d=1.0,afade=t=out:st={DUR - 1.5}:d=1.5[mus]"]
labels = ["[mus]"]
for i, (t, name, vol) in enumerate(SFX):
    inputs += ["-i", os.path.join(SFX_DIR, f"{name}.mp3")]
    d = int(t * 1000)
    fl.append(f"[{i + 1}:a]aresample=44100,aformat=channel_layouts=stereo,volume={vol},adelay={d}|{d}[s{i}]")
    labels.append(f"[s{i}]")
fl.append("".join(labels) + f"amix=inputs={len(labels)}:normalize=0:duration=first,apad,atrim=duration={DUR},loudnorm=I=-14:TP=-1.5:LRA=11[out]")
subprocess.run(["ffmpeg", "-y", "-loglevel", "error"] + inputs + ["-filter_complex", ";".join(fl), "-map", "[out]", "-ar", "44100", OUT], check=True)
print("ok", OUT)
