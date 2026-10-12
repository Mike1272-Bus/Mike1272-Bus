"""Musique + bruitages du jour 2 v2 (paniers, visuel du client, 25 s), sans voix."""
import os, subprocess

ROOT = os.path.dirname(os.path.abspath(__file__))
SFX_DIR = os.path.join(ROOT, "..", "..", "..", "..", "video-excel-13h", "assets", "sfx")
MUSIC = os.path.join(ROOT, "..", "..", "..", "..", "video-excel-13h", "assets", "audio", "musique.wav")
OUT = os.path.join(ROOT, "assets", "audio", "mix.wav")
DUR = 36.0
SFX = [(0.05, 'whoosh-short', 0.22), (0.3, 'whoosh-short', 0.18), (0.8, 'impact-bass-2', 0.28), (1.3, 'whoosh', 0.25), (1.8, 'sparkle', 0.25), (4.0, 'whoosh-cinematic', 0.3), (4.05, 'whoosh-short', 0.22), (4.7, 'impact-bass-1', 0.28), (5.3, 'pop', 0.2), (5.65, 'pop', 0.2), (6.0, 'pop', 0.2), (6.6, 'pop', 0.22), (8.0, 'whoosh', 0.28), (8.05, 'impact-bass-1', 0.25), (8.7, 'pop', 0.2), (9.2, 'pop', 0.2), (9.55, 'whoosh-short', 0.22), (10.0, 'whoosh-short', 0.18), (10.15, 'click-soft', 0.2), (10.85, 'whoosh-short', 0.18), (11.0, 'click-soft', 0.2), (11.7, 'whoosh-short', 0.18), (11.85, 'ping', 0.2), (12.55, 'whoosh-short', 0.18), (12.7, 'click-soft', 0.2), (15.0, 'whoosh', 0.28), (15.05, 'impact-bass-1', 0.25), (15.7, 'pop', 0.2), (16.2, 'pop', 0.2), (16.7, 'pop', 0.2), (17.05, 'whoosh-short', 0.22), (17.5, 'whoosh-short', 0.18), (17.65, 'click-soft', 0.2), (18.35, 'whoosh-short', 0.18), (18.5, 'click-soft', 0.2), (19.2, 'whoosh-short', 0.18), (19.35, 'ping', 0.2), (20.05, 'whoosh-short', 0.18), (20.2, 'click-soft', 0.2), (22.0, 'whoosh', 0.28), (22.05, 'impact-bass-1', 0.25), (22.7, 'pop', 0.2), (23.2, 'pop', 0.2), (23.7, 'pop', 0.2), (24.2, 'pop', 0.2), (24.55, 'whoosh-short', 0.22), (25.0, 'whoosh-short', 0.18), (25.15, 'click-soft', 0.2), (25.85, 'whoosh-short', 0.18), (26.0, 'click-soft', 0.2), (26.7, 'whoosh-short', 0.18), (26.85, 'ping', 0.2), (27.55, 'whoosh-short', 0.18), (27.7, 'click-soft', 0.2), (29.5, 'whoosh', 0.3), (29.55, 'pop', 0.22), (30.55, 'whoosh-short', 0.22), (31.05, 'pop', 0.22), (31.4, 'sparkle', 0.2), (32.5, 'whoosh-cinematic', 0.3), (33.0, 'typing', 0.3), (34.0, 'click', 0.25), (34.15, 'notification', 0.3), (34.3, 'impact-bass-1', 0.2), (34.9, 'pop', 0.25), (35.4, 'chime', 0.3)]

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
