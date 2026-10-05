# Voix : épisode 6 « Distribution »

`episode6_ameliore.mp3` = l'original avec :
- un filtre sous 80 Hz (bourdonnement, chocs sur le micro) ;
- -3 dB vers 250 Hz (son « boîte ») ;
- +4 dB vers 3,5 kHz et +2 dB vers 6,5 kHz (clarté, la voix sort du téléphone) ;
- une compression légère et un volume calé pour les réseaux.

Commande : `ffmpeg -i episode6_original.mp3 -af "highpass=f=80,equalizer=f=250:t=q:w=1.2:g=-3,equalizer=f=3500:t=q:w=1.0:g=4,equalizer=f=6500:t=q:w=1.0:g=2,acompressor=threshold=-20dB:ratio=2.5:attack=8:release=120:makeup=1,loudnorm=I=-14:TP=-1.5:LRA=7" -ar 44100 -b:a 192k episode6_ameliore.mp3`
