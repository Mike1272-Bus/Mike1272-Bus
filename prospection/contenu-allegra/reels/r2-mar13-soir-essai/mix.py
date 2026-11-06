"""Musique + bruitages : mardi 19 h, vidéo d'essai gratuite (25 s), sans voix."""
import os, subprocess

ROOT = os.path.dirname(os.path.abspath(__file__))
SFX_DIR = os.path.join(ROOT, "..", "..", "..", "..", "video-excel-13h", "assets", "sfx")
MUSIC = os.path.join(ROOT, "..", "..", "..", "..", "video-excel-13h", "assets", "audio", "musique.wav")
OUT = os.path.join(ROOT, "assets", "audio", "mix.wav")
VOIX = os.path.join(ROOT, "assets", "audio", "voix-hook.wav")  # accroche, voix Kokoro ff_siwis
DUR = 25.0
SFX = [(0.0, "impact-bass-2", 0.3), (0.15, "whoosh-short", 0.25), (1.4, "impact-bass-1", 0.25), (1.55, "whoosh-short", 0.25), (2.8, "impact-bass-1", 0.25), (2.95, "whoosh-short", 0.25),
       (4.2, "impact-bass-2", 0.28), (4.35, "whoosh-short", 0.25), (5.0, "pop", 0.25), (5.6, "sparkle", 0.22),
       (6.35, "whoosh-cinematic", 0.3), (6.8, "pop", 0.22), (7.45, "impact-bass-1", 0.25),
       (9.2, "whoosh", 0.28), (9.55, "impact-bass-2", 0.25), (9.9, "whoosh-short", 0.22), (10.15, "whoosh-short", 0.22), (10.4, "whoosh-short", 0.22), (10.8, "pop", 0.22), (11.3, "click", 0.3),
       (12.4, "whoosh", 0.28), (12.5, "pop", 0.2), (12.95, "click", 0.25), (13.6, "impact-bass-2", 0.32), (14.0, "sparkle", 0.25),
       (15.2, "whoosh", 0.28), (15.5, "whoosh-short", 0.25), (15.95, "ping", 0.25), (16.6, "whoosh-short", 0.25), (17.05, "ping", 0.2), (17.8, "pop", 0.22),
       (19.4, "whoosh", 0.28), (19.45, "pop", 0.2), (19.8, "impact-bass-1", 0.28), (20.0, "riser", 0.2),
       (21.0, "whoosh-cinematic", 0.3), (21.4, "whoosh", 0.25), (21.55, "impact-bass-2", 0.25), (22.0, "typing", 0.3), (22.6, "click", 0.25), (22.7, "notification", 0.3), (23.2, "notification", 0.22),
       (23.3, "pop", 0.25), (23.8, "chime", 0.3)]

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
