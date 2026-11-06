"""Musique + bruitages du jour 3 v2 (miel au gingembre, 30 s), sans voix."""
import os, subprocess

ROOT = os.path.dirname(os.path.abspath(__file__))
SFX_DIR = os.path.join(ROOT, "..", "..", "..", "..", "video-excel-13h", "assets", "sfx")
MUSIC = os.path.join(ROOT, "..", "..", "..", "..", "video-excel-13h", "assets", "audio", "musique.wav")
OUT = os.path.join(ROOT, "assets", "audio", "mix.wav")
DUR = 30.0
SFX = [(0.1, 'whoosh', 0.25), (0.4, 'pop', 0.2), (1.0, 'click-soft', 0.2), (1.6, 'impact-bass-1', 0.25), (2.2, 'pop', 0.2), (3.6, 'whoosh', 0.3), (3.7, 'pop', 0.22), (4.3, 'pop', 0.18), (4.8, 'impact-bass-2', 0.3), (5.15, 'riser', 0.2), (6.6, 'riser', 0.22), (7.0, 'whoosh-cinematic', 0.35), (7.85, 'impact-bass-2', 0.3), (7.9, 'pop', 0.15), (8.05, 'pop', 0.15), (8.4, 'whoosh-short', 0.25), (8.9, 'sparkle', 0.25), (9.1, 'pop', 0.18), (10.4, 'sparkle', 0.18), (11.6, 'whoosh', 0.3), (12.1, 'whoosh-short', 0.25), (12.7, 'pop', 0.25), (13.1, 'whoosh-short', 0.25), (13.9, 'pop', 0.22), (15.0, 'whoosh', 0.3), (16.0, 'whoosh-short', 0.22), (16.6, 'ping', 0.2), (17.4, 'whoosh-short', 0.22), (18.0, 'ping', 0.2), (18.8, 'whoosh-short', 0.22), (19.4, 'ping', 0.2), (20.2, 'whoosh-short', 0.22), (20.8, 'ping', 0.2), (22.6, 'whoosh', 0.3), (22.65, 'pop', 0.22), (23.65, 'whoosh-short', 0.22), (24.15, 'pop', 0.22), (24.4, 'whoosh-short', 0.2), (25.8, 'whoosh-cinematic', 0.3), (26.3, 'typing', 0.3), (27.3, 'click', 0.25), (27.45, 'notification', 0.3), (27.6, 'impact-bass-1', 0.2), (28.2, 'pop', 0.25), (28.7, 'chime', 0.3)]

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
