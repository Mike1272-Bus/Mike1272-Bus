"""Voix off de la vidéo POV (Kokoro, voix française ff_siwis), une phrase par scène, calée sur les temps de la vidéo."""
import os, subprocess

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "assets", "audio", "voix")
os.makedirs(OUT, exist_ok=True)
LIGNES = [
    (0.15, "Hahaha ! J'ai utilisé une compétence IA pour… attends, tu vas voir !"),
    (3.75, "Un : l'IA m'a trouvé cinquante entreprises. J'en ai gardé six."),
    (8.75, "Deux : j'ai créé une vidéo animée pour chacune… sans qu'elles me demandent rien ! Hahaha."),
    (15.4, "Trois : je leur ai envoyé ça en DM Instagram. Cadeau !"),
    (20.95, "Je vous fais une vidéo… s'ils sont d'accord ! Hahaha."),
    (24.3, "Bref ! Si tu es jeune et que tu veux apprendre à gagner de l'argent avec l'IA, commente IA. Je t'envoie un guide gratuit !"),
]
for i, (t, txt) in enumerate(LIGNES):
    f = os.path.join(OUT, f"l{i}.wav")
    subprocess.run(["npx", "--yes", "hyperframes@0.8.77", "tts", txt, "-v", "ff_siwis", "-s", "1.1", "-o", f], check=True, capture_output=True)
    d = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f], capture_output=True, text=True).stdout)
    print(f"l{i} début {t:5.2f}  durée {d:4.2f}  fin {t + d:5.2f}")
