"""Musique + bruitages : Burger Lab (27,5 s), sans voix : musique et sons de « labo » discrets (bips, tampon, interrupteur), pas de bruitages gourmands."""
import os, subprocess

ROOT = os.path.dirname(os.path.abspath(__file__))
SFX_DIR = os.path.join(ROOT, "..", "..", "video-excel-13h", "assets", "sfx")
MUSIC = os.path.join(ROOT, "..", "..", "video-excel-13h", "assets", "audio", "musique.wav")
OUT = os.path.join(ROOT, "assets", "audio", "mix.wav")
DUR = 27.5
SFX = [(0.1, "pop", 0.25), (0.8, "whoosh-short", 0.15), (1.9, "whoosh-short", 0.15), (3.6, "whoosh-cinematic", 0.25), (3.7, "click-soft", 0.3), (4.1, "whoosh", 0.25)]
SFX += [(5.0 + i * 0.48, "ping", 0.18) for i in range(5)] + [(8.25, "impact-bass-2", 0.32)]
SFX += [(9.4, "whoosh-cinematic", 0.25), (9.5, "click-soft", 0.3), (9.9, "whoosh", 0.25)] + [(10.7 + i * 0.48, "ping", 0.18) for i in range(4)] + [(13.05, "impact-bass-2", 0.32)]
SFX += [(14.4, "whoosh-cinematic", 0.25), (14.5, "click-soft", 0.3), (14.9, "whoosh", 0.25)] + [(15.8 + i * 0.4, "pop", 0.2) for i in range(4)]
SFX += [(19.2, "whoosh-cinematic", 0.25), (19.3, "click-soft", 0.3), (19.6, "pop", 0.22), (20.2, "click", 0.5), (20.5, "whoosh", 0.22)] + [(21.2 + i * 0.18, "pop", 0.16) for i in range(4)]
SFX += [(23.2, "whoosh-cinematic", 0.28), (23.6, "pop", 0.25), (24.5, "impact-bass-1", 0.25), (25.2, "whoosh-short", 0.22), (25.8, "chime", 0.3)]

os.makedirs(os.path.dirname(OUT), exist_ok=True)
inputs = ["-i", MUSIC]
fl = [f"[0:a]aresample=44100,aformat=channel_layouts=stereo,atrim=duration={DUR},volume=0.8,afade=t=in:d=0.5,afade=t=out:st={DUR - 1.2}:d=1.2[mus]"]
labels = ["[mus]"]
for i, (t, name, vol) in enumerate(SFX):
    path = os.path.join(ROOT, "assets", "sfx", name[1:] + ".wav") if name.startswith("+") else os.path.join(SFX_DIR, f"{name}.mp3")
    inputs += ["-i", path]
    d = int(t * 1000)
    fl.append(f"[{i + 1}:a]aresample=44100,aformat=channel_layouts=stereo,volume={vol},adelay={d}|{d}[s{i}]")
    labels.append(f"[s{i}]")
fl.append("".join(labels) + f"amix=inputs={len(labels)}:normalize=0:duration=first,apad,atrim=duration={DUR},loudnorm=I=-14:TP=-1.5:LRA=11[out]")
subprocess.run(["ffmpeg", "-y", "-loglevel", "error"] + inputs + ["-filter_complex", ";".join(fl), "-map", "[out]", "-ar", "44100", OUT], check=True)
print("ok", OUT)
