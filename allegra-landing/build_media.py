"""Médias de la landing v3 : boucles courtes (sans son, sauf la vitrine) et photos « avant ».
Sources : vidéos Allegra déjà faites (images libres de droits) et vidéos de Mike."""
import os, subprocess
R = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(R)
OUT = os.path.join(R, "site", "media")
CA = os.path.join(REPO, "prospection", "contenu-allegra")
V = {
    "burger": f"{CA}/mar13-burger/renders/allegra-mar13-burger.mp4",
    "trans": f"{CA}/mer14-transformations/renders/allegra-mer14-transformations.mp4",
    "pizza": f"{CA}/mer14-demo-pizza/renders/allegra-mer14-demo-pizza.mp4",
    "essai": f"{CA}/reels/r2-mar13-soir-essai/renders/allegra-r2-mar13-soir-essai.mp4",
    "ep5": f"{REPO}/contenu-organique/video-episode5-savoir-faire/renders/episode5_tiktok.mp4",
    "guide": f"{REPO}/produits/ebook-videos/guide-videos/finales/v0.mp4",
    "pres": f"{R}/sources/presentation.mp4",
}
# nom, source, début, durée, largeur, son
LOOPS = [
    ("burger-apres", "burger", 5.0, 4.5, 432, False),
    ("burger-fin", "burger", 17.6, 4.2, 432, False),
    ("glace-apres", "trans", 5.6, 3.6, 432, False),
    ("bague-apres", "trans", 10.3, 3.4, 432, False),
    ("beaute-apres", "trans", 15.4, 3.6, 432, False),
    ("catalogue", "trans", 0.6, 3.4, 432, False),
    ("pizza-apres", "pizza", 4.0, 6.5, 432, False),
    ("essai-plein", "essai", 0.0, 7.0, 432, False),
    ("essai-offre", "essai", 12.5, 7.5, 432, False),
    ("edu-motion", "ep5", 0.4, 7.0, 432, False),
    ("portrait", "guide", 0.0, 5.0, 640, False),
    ("explicative", "pres", 4.0, 6.0, 480, False),
    # vitrine avec le son (bouton « son » sur la page)
    ("vitrine-pizza", "pizza", 0.0, 21.0, 540, True),
    ("vitrine-burger", "burger", 0.0, 22.0, 540, True),
    ("vitrine-essai", "essai", 0.0, 25.0, 540, True),
]
def run(a): subprocess.run(["ffmpeg", "-v", "error", "-y"] + a, check=True)
os.makedirs(OUT, exist_ok=True)
for name, src, ss, d, w, son in LOOPS:
    o = os.path.join(OUT, name + ".mp4")
    a = ["-ss", str(ss), "-t", str(d), "-i", V[src], "-vf", f"scale={w}:-2,fps=30", "-c:v", "libx264", "-crf", "29", "-preset", "slow", "-pix_fmt", "yuv420p", "-movflags", "+faststart"]
    a += (["-c:a", "aac", "-b:a", "96k"] if son else ["-an"])
    run(a + [o])
    run(["-ss", str(round(d * 0.55, 2)), "-i", o, "-frames:v", "1", "-q:v", "4", os.path.join(OUT, name + ".jpg")])
# photos « avant »
for name, p in [("burger", f"{CA}/mar13-burger/assets/img/burger_photo.jpg"), ("pizza", f"{CA}/mer14-demo-pizza/assets/img/pizza_photo.jpg"),
                ("glace", f"{CA}/mer14-transformations/assets/img/glace_photo.jpg"), ("bague", f"{CA}/mer14-transformations/assets/img/bague_photo.jpg"),
                ("beaute", f"{CA}/mer14-transformations/assets/img/beaute_photo.jpg"), ("mike", f"{REPO}/produits/ebook-videos/guide-videos/commun/img/mike.jpg")]:
    run(["-i", p, "-vf", "scale='min(640,iw)':-2", "-q:v", "4", os.path.join(OUT, f"photo-{name}.jpg")])
for name, clip, t in [("jus", "jus.mp4", 1.0), ("cafe", "cafe.mp4", 1.0)]:
    run(["-ss", str(t), "-i", f"{CA}/reels/r2-mar13-soir-essai/assets/{clip}", "-frames:v", "1", "-vf", "scale=640:-2", "-q:v", "4", os.path.join(OUT, f"photo-{name}.jpg")])
# galerie : images tirées des vidéos
G = [("burger", 6.2), ("burger", 11.0), ("burger", 14.5), ("trans", 7.6), ("trans", 12.6), ("trans", 17.0), ("pizza", 5.0), ("pizza", 6.6), ("pizza", 8.4), ("pizza", 10.4),
     ("essai", 1.0), ("essai", 2.6), ("essai", 3.8), ("essai", 5.4), ("essai", 20.2), ("essai", 19.0), ("pizza", 16.0), ("burger", 21.0), ("ep5", 2.5), ("ep5", 8.5)]
for i, (src, t) in enumerate(G, 1):
    run(["-ss", str(t), "-i", V[src], "-frames:v", "1", "-vf", "scale=300:-2", "-q:v", "5", os.path.join(OUT, f"g{i:02d}.jpg")])
print("ok")
