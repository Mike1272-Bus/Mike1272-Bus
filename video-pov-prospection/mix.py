"""Voix (ElevenLabs Hugo, intro + fin) + musique + bruitages de la vidéo POV prospection, 34 s."""
import os, subprocess

ROOT = os.path.dirname(os.path.abspath(__file__))
SFX_DIR = os.path.join(ROOT, "..", "video-excel-13h", "assets", "sfx")
MUSIC = os.path.join(ROOT, "assets", "audio", "musique.wav")
VOIX = os.path.join(ROOT, "assets", "audio", "hugo", "voix_hugo.mp3")
OUT = os.path.join(ROOT, "assets", "audio", "mix.wav")
DUR = 34.0

# (début dans la vidéo, début dans le fichier voix, fin dans le fichier voix)
# 0 - 3,45 : « J'ai utilisé une compétence IA pour… attends, tu vas voir ! »
# 3,95 - 10,75 : « Bref ! Si tu es jeune … commente IA. »  /  12,0 - 14,05 : « Je t'envoie un guide gratuit ! »
VOIX_CUTS = [(0.15, 0.0, 3.45), (23.2, 3.95, 10.75), (30.35, 12.0, 14.05)]

RISER = (9.2, 0.8)  # on ne garde que la fin de la montée
CARDS = [3.8, 9.6, 16.6]
SFX = [(0.1, "pop", 0.5), (0.45, "whoosh-short", 0.4), (1.0, "whoosh", 0.45), (2.3, "pop", 0.4),
       (5.0, "pop", 0.45), (5.6, "typing", 0.35), (7.7, "impact-bass-2", 0.5), (7.72, "chime", 0.35), (8.5, "pop", 0.45), (9.3, "whoosh", 0.4),
       (11.3, "whoosh-cinematic", 0.4), (12.4, "sparkle", 0.4), (12.42, "pop", 0.4), (13.3, "click-soft", 0.3),
       (17.9, "pop", 0.45), (18.7, "notification", 0.45), (20.6, "impact-bass-1", 0.5), (20.62, "chime", 0.35), (22.7, "whoosh", 0.4),
       (23.2, "pop", 0.45), (28.6, "key-press", 0.5), (29.1, "click", 0.45), (29.15, "impact-bass-2", 0.45), (29.17, "sparkle", 0.4),
       (30.3, "whoosh-cinematic", 0.45), (31.0, "chime", 0.4)]
for t in CARDS:
    SFX += [(t - 0.8, "riser", 0.55), (t, "whoosh-cinematic", 0.5), (t + 0.15, "impact-bass-1", 0.7), (t + 1.05, "whoosh", 0.45)]

inputs = ["-i", MUSIC]
# musique plus basse sous la voix
duck = "+".join(f"between(t,{s - 0.2},{s + (b - a) + 0.2})" for s, a, b in VOIX_CUTS)
fl = [f"[0:a]aresample=44100,aformat=channel_layouts=stereo,atrim=duration={DUR},volume='0.32-0.18*({duck})':eval=frame,"
      f"afade=t=in:d=0.4,afade=t=out:st={DUR - 1.5}:d=1.5[mus]"]
labels = ["[mus]"]
for i, (t, name, vol) in enumerate(SFX):
    inputs += ["-i", os.path.join(SFX_DIR, f"{name}.mp3")]
    trim = f"atrim=start={RISER[0]}:duration={RISER[1]},asetpts=PTS-STARTPTS,afade=t=in:d=0.3," if name == "riser" else ""
    d = int(t * 1000)
    fl.append(f"[{len(inputs) // 2 - 1}:a]{trim}aresample=44100,aformat=channel_layouts=stereo,volume={vol * 0.6:.3f},adelay={d}|{d}[s{i}]")
    labels.append(f"[s{i}]")
for j, (t, a, b) in enumerate(VOIX_CUTS):
    inputs += ["-i", VOIX]
    d = int(t * 1000)
    fl.append(f"[{len(inputs) // 2 - 1}:a]atrim=start={a}:end={b},asetpts=PTS-STARTPTS,afade=t=out:st={b - a - 0.08}:d=0.08,"
              f"aresample=44100,aformat=channel_layouts=stereo,volume=1.4,adelay={d}|{d}[v{j}]")
    labels.append(f"[v{j}]")
fl.append("".join(labels) + f"amix=inputs={len(labels)}:normalize=0:duration=first,apad,atrim=duration={DUR},loudnorm=I=-14:TP=-1.5:LRA=11[out]")
subprocess.run(["ffmpeg", "-y", "-loglevel", "error"] + inputs + ["-filter_complex", ";".join(fl), "-map", "[out]", "-ar", "44100", OUT], check=True)
print("ok", OUT)
