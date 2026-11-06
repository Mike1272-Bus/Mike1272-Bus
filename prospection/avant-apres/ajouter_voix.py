"""Ajoute la voix ElevenLabs (accroche au début, fin commune) aux 6 avant / après.
voix/tout.mp3 = les 7 phrases dans l'ordre de voix/TEXTE_ELEVENLABS.md, séparées par des silences (découpe automatique),
ou bien un fichier par phrase (voix/burger.mp3 ... voix/fin.mp3). La musique baisse pendant que la voix parle."""
import os, re, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))
V = os.path.join(HERE, "voix"); OUT = os.path.join(HERE, "renders", "voix"); os.makedirs(OUT, exist_ok=True)
ORDRE = ["burger", "glace", "vetements-femmes", "cosmetiques", "chaussures", "gadget", "fin"]
T_HOOK, T_FIN = 0.3, 12.5  # la voix commence sur « AVANT », puis sur la carte de fin

def run(cmd): return subprocess.run(cmd, check=True, capture_output=True, text=True)
def duree(f): return float(run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f]).stdout)

def decouper(src):
    err = subprocess.run(["ffmpeg", "-i", src, "-af", "silencedetect=noise=-38dB:d=0.45", "-f", "null", "-"], capture_output=True, text=True).stderr
    starts = [float(x) for x in re.findall(r"silence_start: ([\d.]+)", err)]
    ends = [float(x) for x in re.findall(r"silence_end: ([\d.]+)", err)]
    total = duree(src); segs = []; cur = 0.0
    if starts and starts[0] < 0.05 and ends: cur = ends.pop(0); starts.pop(0)
    for s, e in zip(starts, ends + [total]):
        if s - cur > 0.3: segs.append((cur, s))
        cur = e
    if total - cur > 0.3: segs.append((cur, total))
    if len(segs) != len(ORDRE):
        sys.exit(f"{len(segs)} phrases trouvées au lieu de {len(ORDRE)} : couper à la main (un fichier par phrase).")
    for nom, (a, b) in zip(ORDRE, segs):
        run(["ffmpeg", "-y", "-loglevel", "error", "-i", src, "-ss", f"{max(0, a - 0.05):.3f}", "-to", f"{b + 0.1:.3f}", os.path.join(V, nom + ".wav")])
    print("découpé :", [f"{b - a:.1f}s" for a, b in segs])

src = os.path.join(V, "tout.mp3")
coupes = os.path.join(V, "coupes.txt")
if os.path.exists(coupes):  # découpe à la main (les pauses dans une phrase ressemblent aux pauses entre phrases)
    lignes = [l.split() for l in open(coupes) if l.strip() and not l.startswith("#")]
    srcm = os.path.join(V, "hugo-elevenlabs.mp3")
    for nom, (a, b) in zip(ORDRE, lignes):
        run(["ffmpeg", "-y", "-loglevel", "error", "-i", srcm, "-ss", a, "-to", b, "-af", "afade=t=in:d=0.03,areverse,afade=t=in:d=0.08,areverse", os.path.join(V, nom + ".wav")])
elif os.path.exists(src): decouper(src)
def fichier(n):
    for ext in (".wav", ".mp3"):
        p = os.path.join(V, n + ext)
        if os.path.exists(p): return p
    sys.exit(f"manque voix/{n}.mp3")

fin = fichier("fin"); dfin = duree(fin)
for slug in ORDRE[:-1]:
    hook = fichier(slug); dh = duree(hook)
    if dh > 4.0: print(f"attention : accroche {slug} longue ({dh:.1f} s), elle déborde sur l'APRÈS")
    vid = os.path.join(HERE, "renders", f"avant-apres-{slug}.mp4")
    duck = f"volume='if(between(t,{T_HOOK - 0.1},{T_HOOK + dh + 0.2})+between(t,{T_FIN - 0.1},{T_FIN + dfin + 0.2}),0.22,1)':eval=frame"
    fl = (f"[0:a]{duck}[m];"
          f"[1:a]aresample=44100,aformat=channel_layouts=stereo,highpass=f=80,acompressor=threshold=-20dB:ratio=3,loudnorm=I=-12:TP=-1.5,aresample=44100,adelay={int(T_HOOK*1000)}|{int(T_HOOK*1000)}[h];"
          f"[2:a]aresample=44100,aformat=channel_layouts=stereo,highpass=f=80,acompressor=threshold=-20dB:ratio=3,loudnorm=I=-12:TP=-1.5,aresample=44100,adelay={int(T_FIN*1000)}|{int(T_FIN*1000)}[f];"
          f"[m][h][f]amix=inputs=3:normalize=0:duration=first,loudnorm=I=-14:TP=-1.5:LRA=11[a]")
    o = os.path.join(OUT, f"avant-apres-{slug}.mp4")
    run(["ffmpeg", "-y", "-loglevel", "error", "-i", vid, "-i", hook, "-i", fin, "-filter_complex", fl,
         "-map", "0:v", "-map", "[a]", "-c:v", "copy", "-c:a", "aac", "-b:a", "160k", "-ar", "44100", "-movflags", "+faststart", o])
    print("ok", o)
