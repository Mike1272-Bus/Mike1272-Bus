"""Son de la vidéo : voix + musique d'origine (volume réseaux), bruitages calés sur les graphiques, fin prolongée pour la carte finale."""
import os, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "source_originale.mp4")
SFX_DIR = os.path.join(HERE, "..", "..", "..", "video-excel-13h", "assets", "sfx")
OUT = os.path.join(HERE, "assets", "audio", "mix.wav")
SRC_END, DUR = 18.95, 21.0
# (début, bruitage, volume, durée max)
SFX = [(2.3, "glitch-1", 0.18, None), (3.45, "error", 0.22, None), (4.35, "ping", 0.28, None),
       (6.2, "whoosh", 0.32, None), (6.32, "impact-bass-1", 0.3, None), (7.38, "whoosh-short", 0.22, None),
       (8.45, "pop", 0.3, None), (10.35, "ping", 0.24, None), (12.05, "pop", 0.26, None), (12.55, "whoosh-short", 0.2, None),
       (14.75, "pop", 0.22, None), (16.9, "whoosh-cinematic", 0.3, None), (17.3, "typing", 0.22, 1.0),
       (18.4, "click", 0.32, None), (18.95, "whoosh", 0.3, None), (19.25, "chime", 0.3, None)]
os.makedirs(os.path.dirname(OUT), exist_ok=True)
inputs = ["-i", SRC]
fl = [f"[0:a]aresample=44100,aformat=channel_layouts=stereo,atrim=duration={SRC_END},afade=t=out:st={SRC_END - 0.35}:d=0.35,"
      f"loudnorm=I=-15:TP=-2:LRA=7,apad,atrim=duration={DUR}[voix]"]
labels = ["[voix]"]
for i, (t, name, vol, dmax) in enumerate(SFX):
    inputs += ["-i", os.path.join(SFX_DIR, f"{name}.mp3")]
    d = int(t * 1000)
    cut = f"atrim=duration={dmax},afade=t=out:st={dmax - 0.15}:d=0.15," if dmax else ""
    fl.append(f"[{i + 1}:a]aresample=44100,aformat=channel_layouts=stereo,{cut}volume={vol},adelay={d}|{d}[s{i}]")
    labels.append(f"[s{i}]")
fl.append("".join(labels) + f"amix=inputs={len(labels)}:normalize=0:duration=first,atrim=duration={DUR},loudnorm=I=-14:TP=-1.5:LRA=9[out]")
subprocess.run(["ffmpeg", "-y", "-loglevel", "error"] + inputs + ["-filter_complex", ";".join(fl), "-map", "[out]", "-ar", "44100", OUT], check=True)
print("ok", OUT)
