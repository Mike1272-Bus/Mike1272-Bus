"""Bilengi (24 s) : musique + les bruitages « boissons » de Mike (prospection/sfx-boissons) + quelques sons discrets."""
import os, subprocess
ROOT = os.path.dirname(os.path.abspath(__file__))
SFX_DIR = os.path.join(ROOT, "..", "..", "video-excel-13h", "assets", "sfx")
BOISSONS = os.path.join(ROOT, "..", "sfx-boissons")
MUSIC = os.path.join(ROOT, "..", "..", "video-excel-13h", "assets", "audio", "musique.wav")
OUT = os.path.join(ROOT, "assets", "audio", "mix.wav"); DUR = 24.0
B = lambda n: os.path.join(BOISSONS, n + ".wav")
L = lambda n: os.path.join(SFX_DIR, n + ".mp3")
SFX = [  # (heure, fichier, volume, durée max ou None)
    (0.25, B("boisson-4-ouverture-et-versement"), 0.9, 6.6),  # l'ouverture, puis ça coule sur le verre
    (3.3, L("whoosh-cinematic"), 0.22, None),
    (7.9, L("whoosh-cinematic"), 0.22, None), (8.1, B("boisson-1-tintements"), 0.85, 3.6),  # leurs bouteilles qui tintent
    (8.6, B("boisson-2-versement-petillant"), 0.45, 3.0),
    (12.0, L("whoosh-cinematic"), 0.22, None), (12.6, L("pop"), 0.2, None), (14.4, L("pop"), 0.2, None),
    (16.6, B("boisson-5-gorgee"), 1.0, None),  # la gorgée, juste avant le logo
    (17.6, L("pop"), 0.22, None), (20.2, L("whoosh-short"), 0.2, None), (21.0, L("chime"), 0.28, None),
]
os.makedirs(os.path.dirname(OUT), exist_ok=True)
inputs = ["-i", MUSIC]
fl = [f"[0:a]aresample=44100,aformat=channel_layouts=stereo,atrim=duration={DUR},volume=0.6,afade=t=in:d=0.8,afade=t=out:st={DUR - 1.5}:d=1.5[mus]"]
labels = ["[mus]"]
for i, (t, path, vol, maxd) in enumerate(SFX):
    inputs += ["-i", path]; d = int(t * 1000)
    trim = f",atrim=duration={maxd},afade=t=out:st={maxd - 0.4}:d=0.4" if maxd else ""
    fl.append(f"[{i + 1}:a]aresample=44100,aformat=channel_layouts=stereo{trim},volume={vol},adelay={d}|{d}[s{i}]"); labels.append(f"[s{i}]")
fl.append("".join(labels) + f"amix=inputs={len(labels)}:normalize=0:duration=first,apad,atrim=duration={DUR},loudnorm=I=-14:TP=-1.5:LRA=11[out]")
subprocess.run(["ffmpeg", "-y", "-loglevel", "error"] + inputs + ["-filter_complex", ";".join(fl), "-map", "[out]", "-ar", "44100", OUT], check=True)
print("ok", OUT)
