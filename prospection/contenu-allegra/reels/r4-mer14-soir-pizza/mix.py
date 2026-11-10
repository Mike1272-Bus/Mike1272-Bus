"""Musique + bruitages : mercredi 19 h, démo pub pizza (21 s), sans voix."""
import os, subprocess

ROOT = os.path.dirname(os.path.abspath(__file__))
SFX_DIR = os.path.join(ROOT, "..", "..", "..", "..", "video-excel-13h", "assets", "sfx")
MUSIC = os.path.join(ROOT, "..", "..", "..", "..", "video-excel-13h", "assets", "audio", "musique.wav")
OUT = os.path.join(ROOT, "assets", "audio", "mix.wav")
VOIX = os.path.join(ROOT, "assets", "audio", "voix-hook.wav")  # accroche, voix Kokoro ff_siwis
DUR = 21.0
SFX = [(0.1, "whoosh-short", 0.2), (0.45, "impact-bass-1", 0.25), (0.6, "whoosh", 0.25), (1.1, "pop", 0.2), (1.5, "click", 0.35), (1.9, "impact-bass-2", 0.28), (2.25, "pop", 0.2),
       (3.15, "whoosh-cinematic", 0.3), (3.5, "impact-bass-1", 0.3), (4.9, "impact-bass-1", 0.3), (6.3, "impact-bass-2", 0.3), (7.6, "whoosh", 0.25), (7.75, "pop", 0.22), (8.2, "whoosh-short", 0.25), (8.8, "sparkle", 0.25),
       (9.55, "whoosh-cinematic", 0.28), (9.9, "pop", 0.15), (10.3, "whoosh", 0.25), (10.75, "whoosh", 0.25), (11.2, "whoosh", 0.25), (11.7, "impact-bass-2", 0.3), (12.2, "ping", 0.2),
       (12.85, "pop", 0.2), (13.25, "whoosh-short", 0.2), (13.6, "pop", 0.15), (13.9, "pop", 0.15), (14.2, "pop", 0.15), (14.45, "pop", 0.15), (14.7, "sparkle", 0.2),
       (15.75, "whoosh-cinematic", 0.3), (16.2, "whoosh", 0.25), (16.35, "impact-bass-2", 0.25), (16.9, "typing", 0.3), (17.5, "click", 0.25), (17.6, "notification", 0.3), (18.2, "notification", 0.22),
       (18.5, "pop", 0.25), (19.1, "chime", 0.3)]

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
