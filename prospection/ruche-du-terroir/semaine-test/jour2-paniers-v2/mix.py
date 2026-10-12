"""Musique + bruitages du jour 2 v2 (paniers, visuel du client, 25 s), sans voix."""
import os, subprocess

ROOT = os.path.dirname(os.path.abspath(__file__))
SFX_DIR = os.path.join(ROOT, "..", "..", "..", "..", "video-excel-13h", "assets", "sfx")
MUSIC = os.path.join(ROOT, "..", "..", "..", "..", "video-excel-13h", "assets", "audio", "musique.wav")
OUT = os.path.join(ROOT, "assets", "audio", "mix.wav")
DUR = 25.0
SFX = [(0.05, 'whoosh-short', 0.22), (0.3, 'whoosh-short', 0.18), (0.75, 'impact-bass-2', 0.28), (1.1, 'whoosh', 0.25), (1.6, 'sparkle', 0.25), (3.4, 'whoosh-cinematic', 0.3), (3.45, 'whoosh-short', 0.22), (4.0, 'impact-bass-1', 0.28), (4.5, 'pop', 0.2), (4.72, 'pop', 0.2), (4.94, 'pop', 0.2), (5.3, 'pop', 0.22), (6.6, 'whoosh', 0.28), (6.6499999999999995, 'impact-bass-1', 0.25), (6.9, 'pop', 0.16), (7.04, 'pop', 0.16), (7.15, 'whoosh-short', 0.22), (7.5, 'ping', 0.2), (7.82, 'click-soft', 0.2), (8.14, 'click-soft', 0.2), (8.46, 'click-soft', 0.2), (8.78, 'click-soft', 0.2), (10.4, 'whoosh', 0.28), (10.450000000000001, 'impact-bass-1', 0.25), (10.7, 'pop', 0.16), (10.84, 'pop', 0.16), (10.98, 'pop', 0.16), (10.95, 'whoosh-short', 0.22), (11.3, 'ping', 0.2), (11.62, 'click-soft', 0.2), (11.94, 'click-soft', 0.2), (12.26, 'click-soft', 0.2), (12.58, 'click-soft', 0.2), (14.2, 'whoosh', 0.28), (14.25, 'impact-bass-1', 0.25), (14.5, 'pop', 0.16), (14.64, 'pop', 0.16), (14.78, 'pop', 0.16), (14.92, 'pop', 0.16), (14.75, 'whoosh-short', 0.22), (15.1, 'ping', 0.2), (15.42, 'click-soft', 0.2), (15.74, 'click-soft', 0.2), (16.06, 'click-soft', 0.2), (16.38, 'click-soft', 0.2), (18.4, 'whoosh', 0.3), (18.45, 'pop', 0.22), (19.45, 'whoosh-short', 0.22), (19.95, 'pop', 0.22), (20.3, 'sparkle', 0.2), (21.4, 'whoosh-cinematic', 0.3), (21.9, 'typing', 0.3), (22.9, 'click', 0.25), (23.05, 'notification', 0.3), (23.2, 'impact-bass-1', 0.2), (23.8, 'pop', 0.25), (24.3, 'chime', 0.3)]

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
