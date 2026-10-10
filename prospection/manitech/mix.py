"""Musique + bruitages de la vidéo ManiTech (sans voix), 25 s."""
import os, subprocess

ROOT = os.path.dirname(os.path.abspath(__file__))
SFX_DIR = os.path.join(ROOT, "..", "..", "video-excel-13h", "assets", "sfx")
MUSIC = os.path.join(ROOT, "..", "..", "video-excel-13h", "assets", "audio", "musique.wav")
OUT = os.path.join(ROOT, "assets", "audio", "mix.wav")
DUR = 25.0
SFX = [(0.1, "whoosh-cinematic", 0.35), (1.3, "impact-bass-1", 0.3), (1.35, "sparkle", 0.25), (1.8, "pop", 0.2), (3.25, "whoosh", 0.35),
       (3.9, "whoosh-short", 0.3), (4.5, "whoosh-short", 0.28), (5.0, "pop", 0.25), (5.25, "pop", 0.25), (7.8, "whoosh-cinematic", 0.35),
       (8.4, "click-soft", 0.2), (9.25, "pop", 0.25), (9.53, "pop", 0.25), (9.81, "pop", 0.25), (10.09, "pop", 0.25), (10.9, "sparkle", 0.2),
       (13.0, "whoosh", 0.35), (13.5, "whoosh-short", 0.3), (15.1, "impact-bass-2", 0.3), (17.2, "whoosh", 0.35), (17.5, "whoosh-short", 0.3),
       (18.0, "click-soft", 0.2), (20.95, "whoosh-cinematic", 0.35), (21.45, "impact-bass-1", 0.3), (22.5, "pop", 0.25), (23.1, "chime", 0.3)]
os.makedirs(os.path.dirname(OUT), exist_ok=True)
inputs = ["-stream_loop", "-1", "-i", MUSIC]
fl = [f"[0:a]aresample=44100,aformat=channel_layouts=stereo,atrim=duration={DUR},volume=0.9,afade=t=in:d=0.5,afade=t=out:st={DUR - 1.5}:d=1.5[mus]"]
labels = ["[mus]"]
for i, (t, name, vol) in enumerate(SFX):
    inputs += ["-i", os.path.join(SFX_DIR, f"{name}.mp3")]
    d = int(t * 1000)
    fl.append(f"[{i + 1}:a]aresample=44100,aformat=channel_layouts=stereo,volume={vol},adelay={d}|{d}[s{i}]")
    labels.append(f"[s{i}]")
fl.append("".join(labels) + f"amix=inputs={len(labels)}:normalize=0:duration=first,apad,atrim=duration={DUR},loudnorm=I=-14:TP=-1.5:LRA=11[out]")
subprocess.run(["ffmpeg", "-y", "-loglevel", "error"] + inputs + ["-filter_complex", ";".join(fl), "-map", "[out]", "-ar", "44100", OUT], check=True)
print("ok", OUT)
