"""Ruche jour 5 (26 s), version BD : musique + « PAF » (impact grave + pop) à chaque explosion, pops, carillon."""
import os, subprocess
ROOT = os.path.dirname(os.path.abspath(__file__)); TOP = os.path.join(ROOT, "..", "..", "..", "..")
SFX_DIR = os.path.join(TOP, "video-excel-13h", "assets", "sfx"); BOISSONS = os.path.join(TOP, "prospection", "sfx-boissons")
MUSIC = os.path.join(TOP, "video-excel-13h", "assets", "audio", "musique.wav")
OUT = os.path.join(ROOT, "assets", "audio", "mix.wav"); DUR = 26.0
B = lambda n: os.path.join(BOISSONS, n + ".wav"); L = lambda n: os.path.join(SFX_DIR, n + ".mp3")
SFX = [  # (heure, fichier, volume, durée max ou None) : chaque « PAF » BD = impact grave + pop
    (0.2, L("whoosh-short"), 0.2, None), (0.3, L("impact-bass-2"), 0.4, None), (0.32, L("pop"), 0.3, None), (0.6, L("sparkle"), 0.2, None),
    (1.9, L("pop"), 0.2, None),
    (3.8, L("whoosh-cinematic"), 0.25, None), (4.0, L("impact-bass-1"), 0.3, None), (4.3, L("pop"), 0.25, None), (4.5, L("whoosh"), 0.25, None), (5.0, L("impact-bass-2"), 0.3, None),
    (5.6, L("sparkle"), 0.2, None),
    (10.6, L("whoosh-cinematic"), 0.28, None), (10.85, L("impact-bass-2"), 0.45, None), (10.87, L("pop"), 0.35, None), (11.15, L("impact-bass-1"), 0.3, None), (11.3, L("sparkle"), 0.22, None),
    (12.4, L("whoosh"), 0.2, None), (12.6, L("whoosh"), 0.2, None), (13.6, L("pop"), 0.25, None), (14.5, L("pop"), 0.25, None), (15.4, L("pop"), 0.25, None), (16.5, L("ping"), 0.22, None),
    (21.2, L("whoosh-cinematic"), 0.28, None), (21.3, L("impact-bass-1"), 0.28, None), (21.9, L("impact-bass-2"), 0.32, None), (21.92, L("pop"), 0.25, None), (22.6, L("whoosh-short"), 0.2, None), (23.2, L("chime"), 0.3, None),
]
os.makedirs(os.path.dirname(OUT), exist_ok=True)
inputs = ["-i", MUSIC]
fl = [f"[0:a]aresample=44100,aformat=channel_layouts=stereo,atrim=duration={DUR},volume=0.6,afade=t=in:d=0.8,afade=t=out:st={DUR - 1.5}:d=1.5[mus]"]
labels = ["[mus]"]
for i, (t, path, vol, maxd) in enumerate(SFX):
    inputs += ["-i", path]; d = int(t * 1000)
    trim = f",atrim=duration={maxd},afade=t=out:st={maxd - 0.6}:d=0.6" if maxd else ""
    fl.append(f"[{i + 1}:a]aresample=44100,aformat=channel_layouts=stereo{trim},volume={vol},adelay={d}|{d}[s{i}]"); labels.append(f"[s{i}]")
fl.append("".join(labels) + f"amix=inputs={len(labels)}:normalize=0:duration=first,apad,atrim=duration={DUR},loudnorm=I=-14:TP=-1.5:LRA=11[out]")
subprocess.run(["ffmpeg", "-y", "-loglevel", "error"] + inputs + ["-filter_complex", ";".join(fl), "-map", "[out]", "-ar", "44100", OUT], check=True)
print("ok", OUT)
