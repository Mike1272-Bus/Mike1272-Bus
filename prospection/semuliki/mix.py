"""Semuliki version IA (13,6 s) : musique + bruitages « boissons » de Mike (prospection/sfx-boissons)."""
import os, subprocess
ROOT = os.path.dirname(os.path.abspath(__file__))
SFX_DIR = os.path.join(ROOT, "..", "..", "video-excel-13h", "assets", "sfx")
BOISSONS = os.path.join(ROOT, "..", "sfx-boissons")
MUSIC = os.path.join(ROOT, "..", "..", "video-excel-13h", "assets", "audio", "musique.wav")
OUT = os.path.join(ROOT, "assets", "audio", "mix.wav"); DUR = 13.6
B = lambda n: os.path.join(BOISSONS, n + ".wav")
L = lambda n: os.path.join(SFX_DIR, n + ".mp3")
SFX = [  # (heure, fichier, volume, durée max ou None)
    (0.1, B("boisson-4-ouverture-et-versement"), 0.85, 4.0),  # la bouteille s'ouvre, ça coule
    (0.6, L("whoosh-cinematic"), 0.25, None), (0.8, L("impact-bass-1"), 0.3, None),  # SEMULIKI
    (2.4, L("riser"), 0.2, 1.8),
    (4.15, L("impact-bass-2"), 0.4, None),
    (4.25, L("whoosh-short"), 0.35, None), (4.37, L("whoosh-short"), 0.35, None), (4.49, L("whoosh-short"), 0.35, None),  # les griffes
    (5.5, L("sparkle"), 0.25, None), (6.1, B("boisson-1-tintements"), 0.55, 1.8),  # glaçons
    (7.9, L("impact-bass-1"), 0.35, None), (8.0, L("whoosh-cinematic"), 0.25, None),
    (8.35, L("pop"), 0.25, None), (8.8, L("pop"), 0.25, None), (9.25, L("pop"), 0.25, None),
    (10.75, L("whoosh-short"), 0.25, None), (10.85, L("pop"), 0.25, None), (11.35, L("chime"), 0.3, None),
    (11.75, B("boisson-2-versement-petillant"), 0.5, 1.5),
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
