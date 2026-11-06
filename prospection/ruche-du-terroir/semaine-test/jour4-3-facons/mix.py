"""Musique + bruitages du jour 4 (3 façons d'utiliser le miel, 32 s), sans voix."""
import os, subprocess

ROOT = os.path.dirname(os.path.abspath(__file__))
SFX_DIR = os.path.join(ROOT, "..", "..", "..", "..", "video-excel-13h", "assets", "sfx")
MUSIC = os.path.join(ROOT, "..", "..", "..", "..", "video-excel-13h", "assets", "audio", "musique.wav")
OUT = os.path.join(ROOT, "assets", "audio", "mix.wav")
DUR = 32.0
SFX = [(0.1, 'pop', 0.2), (0.5, 'pop', 0.22), (1.3, 'impact-bass-1', 0.28), (3.6, 'whoosh', 0.3), (4.15, 'impact-bass-2', 0.28), (6.2, 'riser', 0.22), (6.6, 'whoosh', 0.28), (6.6, 'whoosh-cinematic', 0.35), (6.7, 'impact-bass-1', 0.28), (7.3, 'whoosh-short', 0.2), (7.9, 'sparkle', 0.2), (8.2, 'whoosh-short', 0.22), (8.8, 'ping', 0.2), (9.7, 'whoosh-short', 0.22), (10.3, 'ping', 0.2), (12.0, 'whoosh', 0.28), (12.1, 'impact-bass-1', 0.28), (12.7, 'whoosh-short', 0.2), (13.3, 'sparkle', 0.2), (13.6, 'whoosh-short', 0.22), (14.2, 'ping', 0.2), (15.1, 'whoosh-short', 0.22), (15.7, 'ping', 0.2), (17.4, 'whoosh', 0.28), (17.5, 'impact-bass-1', 0.28), (18.1, 'whoosh-short', 0.2), (18.7, 'sparkle', 0.2), (19.0, 'whoosh-short', 0.22), (19.6, 'ping', 0.2), (20.5, 'whoosh-short', 0.22), (21.1, 'ping', 0.2), (22.8, 'whoosh', 0.3), (22.85, 'pop', 0.22), (23.35, 'whoosh-short', 0.2), (23.75, 'pop', 0.14), (23.93, 'pop', 0.14), (24.11, 'pop', 0.14), (24.29, 'pop', 0.14), (24.47, 'pop', 0.14), (24.65, 'pop', 0.14), (24.83, 'pop', 0.14), (25.65, 'whoosh-short', 0.2), (26.1, 'pop', 0.22), (27.6, 'whoosh-cinematic', 0.3), (28.1, 'typing', 0.3), (29.1, 'click', 0.25), (29.25, 'notification', 0.3), (29.4, 'impact-bass-1', 0.2), (30.0, 'pop', 0.25), (30.5, 'chime', 0.3)]

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
