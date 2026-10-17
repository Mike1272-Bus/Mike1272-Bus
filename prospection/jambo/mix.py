"""Jambo (12 s) : musique + bruitages « boissons » de Mike (prospection/sfx-boissons)."""
import os, subprocess
ROOT = os.path.dirname(os.path.abspath(__file__))
SFX_DIR = os.path.join(ROOT, "..", "..", "video-excel-13h", "assets", "sfx")
BOISSONS = os.path.join(ROOT, "..", "sfx-boissons")
MUSIC = os.path.join(ROOT, "..", "..", "video-excel-13h", "assets", "audio", "musique.wav")
OUT = os.path.join(ROOT, "assets", "audio", "mix.wav"); DUR = 12.0
B = lambda n: os.path.join(BOISSONS, n + ".wav")
L = lambda n: os.path.join(SFX_DIR, n + ".mp3")
SFX = [  # (heure, fichier, volume, durée max ou None)
    (0.1, B("boisson-4-ouverture-et-versement"), 0.9, 3.3),  # la bouteille s'ouvre
    (0.4, L("riser"), 0.15, 3.0),
    (3.35, L("impact-bass-1"), 0.35, None), (3.4, B("boisson-2-versement-petillant"), 0.8, 3.2),  # bulles
    (3.6, L("whoosh-short"), 0.2, None), (4.6, L("sparkle"), 0.2, None),
    (6.55, L("impact-bass-2"), 0.3, None),
] + [(7.0 + i * 0.38, L("click"), 0.35, None) for i in range(5)] + [  # les lumières s'allument
    (8.9, L("whoosh-cinematic"), 0.25, None),
    (9.55, B("boisson-1-tintements"), 0.6, 1.6), (9.7, L("pop"), 0.25, None), (10.2, L("chime"), 0.3, None),
    (10.6, B("boisson-5-gorgee"), 0.9, None),
]
os.makedirs(os.path.dirname(OUT), exist_ok=True)
inputs = ["-i", MUSIC]
fl = [f"[0:a]aresample=44100,aformat=channel_layouts=stereo,atrim=duration={DUR},volume=0.55,afade=t=in:d=0.5,afade=t=out:st={DUR - 1.2}:d=1.2[mus]"]
labels = ["[mus]"]
for i, (t, path, vol, maxd) in enumerate(SFX):
    inputs += ["-i", path]; d = int(t * 1000)
    trim = f",atrim=duration={maxd},afade=t=out:st={maxd - 0.4}:d=0.4" if maxd else ""
    fl.append(f"[{i + 1}:a]aresample=44100,aformat=channel_layouts=stereo{trim},volume={vol},adelay={d}|{d}[s{i}]"); labels.append(f"[s{i}]")
fl.append("".join(labels) + f"amix=inputs={len(labels)}:normalize=0:duration=first,apad,atrim=duration={DUR},loudnorm=I=-14:TP=-1.5:LRA=11[out]")
subprocess.run(["ffmpeg", "-y", "-loglevel", "error"] + inputs + ["-filter_complex", ";".join(fl), "-map", "[out]", "-ar", "44100", OUT], check=True)
print("ok", OUT)
