"""Fuegos (25 s) : musique seule, sans voix ni bruitages (demande de Mike)."""
import os, subprocess
ROOT = os.path.dirname(os.path.abspath(__file__))
MUSIC = os.path.join(ROOT, "..", "..", "video-excel-13h", "assets", "audio", "musique.wav")
OUT = os.path.join(ROOT, "assets", "audio", "mix.wav"); DUR = 25.0
os.makedirs(os.path.dirname(OUT), exist_ok=True)
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", MUSIC, "-af",
                f"aresample=44100,aformat=channel_layouts=stereo,atrim=duration={DUR},afade=t=in:d=1.0,afade=t=out:st={DUR - 1.8}:d=1.8,loudnorm=I=-14:TP=-1.5:LRA=11",
                "-ar", "44100", OUT], check=True)
print("ok", OUT)
