"""Musique + bruitages : mardi 13 h, avant/après burger (22 s), sans voix."""
import os, subprocess

ROOT = os.path.dirname(os.path.abspath(__file__))
SFX_DIR = os.path.join(ROOT, "..", "..", "..", "..", "video-excel-13h", "assets", "sfx")
MUSIC = os.path.join(ROOT, "..", "..", "..", "..", "video-excel-13h", "assets", "audio", "musique.wav")
OUT = os.path.join(ROOT, "assets", "audio", "mix.wav")
VOIX = os.path.join(ROOT, "assets", "audio", "voix-hook.wav")  # accroche, voix Kokoro ff_siwis
DUR = 22.0
SFX = [(0.1, "whoosh-short", 0.2), (0.55, "impact-bass-1", 0.25), (0.9, "whoosh", 0.25), (1.5, "pop", 0.22), (2.3, "click", 0.35),
       (3.15, "whoosh-cinematic", 0.3), (3.45, "sparkle", 0.25), (3.85, "impact-bass-2", 0.3),
       (4.55, "whoosh-cinematic", 0.3), (5.0, "pop", 0.2), (5.18, "impact-bass-1", 0.28), (6.53, "impact-bass-1", 0.28), (7.88, "impact-bass-2", 0.28), (9.2, "whoosh", 0.22), (9.4, "pop", 0.22), (9.7, "whoosh-short", 0.22), (10.2, "sparkle", 0.22),
       (11.95, "impact-bass-2", 0.28), (12.2, "whoosh", 0.25), (12.5, "pop", 0.18), (12.6, "whoosh", 0.25), (12.9, "pop", 0.18), (13.9, "pop", 0.2), (14.2, "whoosh-short", 0.2),
       (15.45, "pop", 0.2), (15.9, "pop", 0.15), (16.08, "pop", 0.15), (16.26, "pop", 0.15), (16.44, "pop", 0.15), (16.8, "ping", 0.2),
       (17.35, "whoosh-cinematic", 0.3), (17.8, "whoosh", 0.25), (17.95, "impact-bass-2", 0.25), (18.5, "typing", 0.3), (19.1, "click", 0.25), (19.2, "notification", 0.3), (19.8, "notification", 0.22),
       (20.1, "pop", 0.25), (20.7, "chime", 0.3)]

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
