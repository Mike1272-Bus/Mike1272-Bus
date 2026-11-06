"""Musique + bruitages : mercredi 13 h, 3 transformations (22,5 s), sans voix."""
import os, subprocess

ROOT = os.path.dirname(os.path.abspath(__file__))
SFX_DIR = os.path.join(ROOT, "..", "..", "..", "..", "video-excel-13h", "assets", "sfx")
MUSIC = os.path.join(ROOT, "..", "..", "..", "..", "video-excel-13h", "assets", "audio", "musique.wav")
OUT = os.path.join(ROOT, "assets", "audio", "mix.wav")
VOIX = os.path.join(ROOT, "assets", "audio", "voix-hook.wav")  # accroche, voix Kokoro ff_siwis
DUR = 22.5
SFX = [(0.1, "whoosh-short", 0.2), (0.4, "whoosh", 0.2), (0.6, "whoosh", 0.2), (0.8, "whoosh", 0.2), (1.5, "impact-bass-1", 0.25), (1.9, "impact-bass-2", 0.28), (2.75, "whoosh-cinematic", 0.3), (17.95, "whoosh-cinematic", 0.3), (3.05, "pop", 0.2), (3.15, "whoosh", 0.25), (3.50, "pop", 0.18), (4.20, "whoosh-short", 0.25), (4.35, "whoosh", 0.25), (4.58, "impact-bass-1", 0.28), (5.58, "impact-bass-2", 0.28), (6.65, "pop", 0.2), (6.95, "sparkle", 0.2), (8.25, "pop", 0.2), (8.35, "whoosh", 0.25), (8.70, "pop", 0.18), (9.40, "whoosh-short", 0.25), (9.55, "whoosh", 0.25), (9.78, "impact-bass-1", 0.28), (10.78, "impact-bass-2", 0.28), (11.85, "pop", 0.2), (12.15, "sparkle", 0.2), (13.45, "pop", 0.2), (13.55, "whoosh", 0.25), (13.90, "pop", 0.18), (14.60, "whoosh-short", 0.25), (14.75, "whoosh", 0.25), (14.98, "impact-bass-1", 0.28), (15.98, "impact-bass-2", 0.28), (17.05, "pop", 0.2), (17.35, "sparkle", 0.2), (18.40, "whoosh", 0.25), (18.55, "impact-bass-2", 0.25), (19.10, "typing", 0.3), (19.70, "click", 0.25), (19.80, "notification", 0.3), (20.40, "notification", 0.22), (20.70, "pop", 0.25), (21.30, "chime", 0.3)]

os.makedirs(os.path.dirname(OUT), exist_ok=True)
inputs = ["-i", MUSIC]
fl = [f"[0:a]aresample=44100,aformat=channel_layouts=stereo,atrim=duration={DUR},volume='if(lt(t,2.9),0.3,0.85)':eval=frame,afade=t=in:d=0.5,afade=t=out:st={DUR - 1.2}:d=1.2[mus]"]
labels = ["[mus]"]
for i, (t, name, vol) in enumerate(SFX):
    inputs += ["-i", os.path.join(SFX_DIR, f"{name}.mp3")]
    d = int(t * 1000)
    extra = ",atrim=duration=0.7" if name == "typing" else ""
    fl.append(f"[{i + 1}:a]aresample=44100,aformat=channel_layouts=stereo{extra},volume={vol},adelay={d}|{d}[s{i}]")
    labels.append(f"[s{i}]")
inputs += ["-i", VOIX]
n = len(SFX) + 1
fl.append(f"[{n}:a]aresample=44100,aformat=channel_layouts=stereo,volume=1.6,adelay=100|100[voix]")
labels.append("[voix]")
fl.append("".join(labels) + f"amix=inputs={len(labels)}:normalize=0:duration=first,apad,atrim=duration={DUR},loudnorm=I=-14:TP=-1.5:LRA=11[out]")
subprocess.run(["ffmpeg", "-y", "-loglevel", "error"] + inputs + ["-filter_complex", ";".join(fl), "-map", "[out]", "-ar", "44100", OUT], check=True)
print("ok", OUT)
