"""Version 30 s Instagram : mêmes coupes que la pub, fin "lien dans ma bio"."""
import os, subprocess
from build_ig import A, VOICE, MUSIC, SFX, T, DUR, HAS_CTA

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = f"{ROOT}/renders/pub_ig_complete.mp4"
OUT = f"{ROOT}/renders/pub_instagram_30s.mp4"

# (début, fin) dans le rendu 91 s ; chaque coupe tombe dans un silence de la voix
RANGES = [
    (0.00, 2.79),    # Vous avez déjà un savoir-faire qui vaut de l'argent.
    (10.55, 21.69),  # Que vous soyez salarié... tenir une comptabilité.
    (37.72, 44.75),  # Mon oncle David, menuisier... sans budget pub.
    (48.05, 50.66),  # J'ai écrit le guide pour faire pareil.
    # avec la phrase enregistrée : le CTA parlé seul ; sans : "Il suffit d'un message pour commencer." + carte bio
    ((84.30 if HAS_CTA else 82.08), DUR),
]
DUR = round(sum(b - a for a, b in RANGES), 3)


def remap_sfx():
    """Garde les effets qui tombent dans un passage conservé ; un effet juste avant une coupe est ramené sur la coupe."""
    out, off = [], 0.0
    for i, (a, b) in enumerate(RANGES):
        for t, spec, vol in SFX:
            lead = 0.3 if i else 0.0
            if a - lead <= t < b:
                out.append((round(max(t, a) - a + off, 3), spec, vol))
        off += b - a
    return sorted(out, key=lambda s: s[0])


def build():
    sfx = remap_sfx()
    inputs = ["-i", SRC, "-i", VOICE, "-i", MUSIC]
    fl = []
    for i, (a, b) in enumerate(RANGES):
        fl.append(f"[0:v]trim=start={a}:end={b},setpts=PTS-STARTPTS[v{i}]")
        fl.append(f"[1:a]atrim=start={a}:end={b},asetpts=PTS-STARTPTS[a{i}]")
    n = len(RANGES)
    fl.append("".join(f"[v{i}]" for i in range(n)) + f"concat=n={n}:v=1:a=0[vc]")
    fl.append("".join(f"[a{i}]" for i in range(n)) + f"concat=n={n}:v=0:a=1[voice]")
    # la barre de progression d'origine sauterait à chaque coupe : on la recouvre et on en redessine une sur 30 s
    fl.append("[vc]split[vm][vb]")
    fl.append("[vb]crop=1080:12:0:14[band]")
    fl.append("[vm][band]overlay=0:0[vclean]")
    fl.append(f"color=c=0xff5c00:s=1080x12:r=30:d={DUR}[bar]")
    fl.append("[vclean][bar]overlay=x='-w+w*t/" + str(DUR) + "':y=0:eval=frame,format=yuv420p[vout]")
    fl.append("[voice]aresample=44100,aformat=channel_layouts=stereo,highpass=f=70,asplit=2[vo][sc]")
    fl.append(f"[2:a]atrim=duration={DUR},volume=0.55,afade=t=out:st={DUR - 1.5}:d=1.5[mus]")
    fl.append("[mus][sc]sidechaincompress=threshold=0.03:ratio=8:attack=20:release=350:makeup=1[musd]")
    labels = []
    for i, (t, spec, vol) in enumerate(sfx):
        name, off, dur = (spec, 0, None) if isinstance(spec, str) else spec
        inputs += ["-i", f"{A}/sfx/{name}.mp3"]
        trim = f"atrim=start={off}" + (f":duration={dur}" if dur else "") + ",asetpts=PTS-STARTPTS,"
        d = int(t * 1000)
        fl.append(f"[{i + 3}:a]aresample=44100,aformat=channel_layouts=stereo,{trim}volume={vol},adelay={d}|{d}[s{i}]")
        labels.append(f"[s{i}]")
    fl.append("[vo][musd]" + "".join(labels) + f"amix=inputs={2 + len(labels)}:normalize=0:duration=longest,"
              f"atrim=duration={DUR},loudnorm=I=-14:TP=-1.5:LRA=11,aresample=48000[aout]")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error"] + inputs +
                   ["-filter_complex", ";".join(fl), "-map", "[vout]", "-map", "[aout]",
                    "-c:v", "libx264", "-crf", "18", "-preset", "medium", "-r", "30",
                    "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", OUT], check=True)
    print("ok", OUT, DUR, "s,", len(sfx), "effets")


if __name__ == "__main__":
    build()
