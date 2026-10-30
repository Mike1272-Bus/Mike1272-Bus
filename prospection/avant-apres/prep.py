"""Prépare, pour chaque produit, le clip « après » (carte 960x1200, 8 s) et la photo « avant » (image fixe)."""
import os, subprocess
RAW = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "contenu-allegra", "stock", "raw")
# (source, début, durée à garder, vitesse, cadrage horizontal 0..1)
P = {
  "burger": [("burger-1", 0.0, 5.0, 1.0, 0.5), ("burger-3", 2.0, 3.0, 1.0, 0.45)],
  "cosmetiques": [("maquillage-3", 0.0, 5.0, 1.0, 0.5), ("cosmetique-1", 0.5, 3.0, 1.0, 0.45)],
  "glace": [("glace-1", 0.0, 5.0, 1.0, 0.5), ("glace-2", 1.0, 3.0, 1.0, 0.5)],
  "chaussures": [("baskets-3", 0.3, 4.6, 1.0, 0.62), ("baskets-2", 3.6, 3.4, 1.0, 0.45)],
  "gadget": [("smartwatch-2", 0.0, 5.0, 1.0, 0.3), ("montre-1", 0.0, 3.0, 1.0, 0.45)],
  "vetements-femmes": [("robe-2", 0.0, 1.3, 0.4, 0.5), ("robe-1", 0.0, 2.0, 1.0, 0.12), ("tissu-1", 0.0, 3.0, 1.0, 0.5)],
}
W, H, DUR = 960, 1200, 8.0
for name, segs in P.items():
    d = os.path.join(name, "assets"); os.makedirs(d, exist_ok=True)
    inputs, fl, labels = [], [], []
    for i, (src, ss, dur, sp, cx) in enumerate(segs):
        inputs += ["-ss", str(ss), "-t", str(dur), "-i", os.path.join(RAW, src + ".mp4")]
        fl.append(f"[{i}:v]setpts=PTS/{sp},scale=-2:{H}:flags=lanczos,scale='max(iw,{W})':'max(ih,{H})':force_original_aspect_ratio=increase:flags=lanczos,"
                  f"crop={W}:{H}:'(iw-{W})*{cx}':0,unsharp=5:5:0.6,fps=30,setsar=1[v{i}]")
        labels.append(f"[v{i}]")
    fl.append("".join(labels) + f"concat=n={len(segs)}:v=1:a=0,trim=duration={DUR},setpts=PTS-STARTPTS[out]")
    out = os.path.join(d, "apres.mp4")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error"] + inputs + ["-filter_complex", ";".join(fl), "-map", "[out]", "-c:v", "libx264", "-crf", "20", "-pix_fmt", "yuv420p", "-an", out], check=True)
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-ss", "0.3", "-i", out, "-frames:v", "1", "-q:v", "2", os.path.join(d, "avant.jpg")], check=True)
    dd = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", out], capture_output=True, text=True).stdout.strip()
    print(name, dd)
