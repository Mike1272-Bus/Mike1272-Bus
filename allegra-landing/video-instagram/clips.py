"""Clips de la vidéo, tirés des vidéos Allegra (720 px de large), bouclés à la durée voulue."""
import os, subprocess
R = os.path.dirname(os.path.abspath(__file__)); REPO = os.path.dirname(os.path.dirname(R))
CA = f"{REPO}/prospection/contenu-allegra"
SRC = {"burger": f"{CA}/mar13-burger/renders/allegra-mar13-burger.mp4", "trans": f"{CA}/mer14-transformations/renders/allegra-mer14-transformations.mp4",
       "pizza": f"{CA}/mer14-demo-pizza/renders/allegra-mer14-demo-pizza.mp4"}
# nom, source, début, longueur du segment, durée finale
CLIPS = [("bague", "trans", 10.3, 3.4, 5.0), ("burger", "burger", 5.0, 4.5, 5.0), ("glace", "trans", 5.8, 3.0, 5.0),
         ("pizza", "pizza", 4.0, 6.5, 5.0), ("glace2", "trans", 5.8, 3.0, 4.6)]
os.makedirs(f"{R}/assets/clips", exist_ok=True)
for n, s, ss, seg, d in CLIPS:
    tmp = f"{R}/assets/clips/_{n}.mp4"; out = f"{R}/assets/clips/{n}.mp4"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", str(ss), "-t", str(seg), "-i", SRC[s], "-vf", "scale=720:-2,fps=30", "-an", "-c:v", "libx264", "-crf", "18", "-pix_fmt", "yuv420p", tmp], check=True)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-stream_loop", "-1", "-i", tmp, "-t", str(d), "-c:v", "libx264", "-crf", "18", "-pix_fmt", "yuv420p", "-movflags", "+faststart", out], check=True)
    os.remove(tmp)
print("ok")
