"""Ruche jour 5 (27 s) : musique + quelques sons (le versement doux sous le miel qui coule, impact sur CONCOURS, carillon)."""
import os, subprocess
ROOT = os.path.dirname(os.path.abspath(__file__)); TOP = os.path.join(ROOT, "..", "..", "..", "..")
SFX_DIR = os.path.join(TOP, "video-excel-13h", "assets", "sfx"); BOISSONS = os.path.join(TOP, "prospection", "sfx-boissons")
MUSIC = os.path.join(TOP, "video-excel-13h", "assets", "audio", "musique.wav")
OUT = os.path.join(ROOT, "assets", "audio", "mix.wav"); DUR = 27.0
B = lambda n: os.path.join(BOISSONS, n + ".wav"); L = lambda n: os.path.join(SFX_DIR, n + ".mp3")
SFX = [  # (heure, fichier, volume, durée max ou None)
    (0.1, L("whoosh-cinematic"), 0.2, None), (2.0, L("impact-bass-1"), 0.22, None), (2.4, L("impact-bass-2"), 0.25, None),
    (4.2, L("whoosh-cinematic"), 0.22, None), (4.5, L("whoosh"), 0.22, None), (4.65, L("impact-bass-1"), 0.22, None),
    (5.0, B("boisson-3-versement-long"), 0.35, 6.0),  # le miel qui coule sur le pot
    (6.0, L("sparkle"), 0.2, None),
    (11.4, L("whoosh-cinematic"), 0.25, None), (12.4, L("impact-bass-2"), 0.32, None), (13.6, L("whoosh"), 0.2, None), (13.8, L("whoosh"), 0.2, None),
    (15.0, L("pop"), 0.22, None), (15.9, L("pop"), 0.22, None), (16.8, L("pop"), 0.22, None), (17.9, L("ping"), 0.2, None),
    (22.2, L("whoosh-cinematic"), 0.25, None), (22.3, L("pop"), 0.22, None), (22.8, L("impact-bass-1"), 0.22, None), (23.4, L("whoosh-short"), 0.2, None), (24.0, L("chime"), 0.3, None),
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
