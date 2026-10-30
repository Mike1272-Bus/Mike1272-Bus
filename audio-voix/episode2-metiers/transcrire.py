"""Transcription phrase par phrase (temps de la vidéo finale), pour caler les scènes sur la voix.
Modèle : whisper-small de sherpa-onnx, téléchargé depuis les releases GitHub (huggingface est bloqué ici) :
  pip install sherpa-onnx
  curl -L -o wb.tar.bz2 https://github.com/k2-fsa/sherpa-onnx/releases/download/asr-models/sherpa-onnx-whisper-small.tar.bz2 && tar xjf wb.tar.bz2
"""
import subprocess, numpy as np, sherpa_onnx, json, sys
SR=16000; M="/tmp/claude-0/sherpa-onnx-whisper-small/"
rec = sherpa_onnx.OfflineRecognizer.from_whisper(encoder=M+"small-encoder.int8.onnx", decoder=M+"small-decoder.int8.onnx", tokens=M+"small-tokens.txt", language="fr", task="transcribe", num_threads=4)
src="/home/user/Mike1272-Bus/audio-voix/episode2-metiers/brut.m4a"
y=np.frombuffer(subprocess.run(["ffmpeg","-loglevel","error","-i",src,"-f","f32le","-ac","1","-ar","44100","-"],capture_output=True).stdout,np.float32)
# same start detection as produire.py
fr=int(0.02*44100); n=len(y)//fr
e=20*np.log10(np.sqrt((y[:n*fr].reshape(n,fr)**2).mean(1))+1e-9)
quiet=e<np.percentile(e,10)+10
voiced=np.where(~quiet)[0]; start=max(voiced[0]*0.02-0.15,0); end=voiced[-1]*0.02+0.35
# segments of speech separated by pauses >=0.3s
segs=[]; i=0; cur=None
while i<n:
    if not quiet[i]:
        if cur is None: cur=i
        i+=1
    else:
        j=i
        while j<n and quiet[j]: j+=1
        if cur is not None and (j-i)*0.02>=0.3:
            segs.append((cur*0.02,i*0.02)); cur=None
        i=j
if cur is not None: segs.append((cur*0.02,n*0.02))
y16=np.frombuffer(subprocess.run(["ffmpeg","-loglevel","error","-i",src,"-f","f32le","-ac","1","-ar",str(SR),"-"],capture_output=True).stdout,np.float32)
out=[]
for a,b in segs:
    if b-a<0.25: continue
    s=rec.create_stream(); s.accept_waveform(SR,y16[int(max(a-0.1,0)*SR):int((b+0.15)*SR)]); rec.decode_stream(s)
    nt=lambda t:(t-start)/1.10+0.6
    out.append((round(nt(a),2),round(nt(b),2),s.result.text.strip()))
    print(f"{nt(a):6.2f}-{nt(b):6.2f}  {s.result.text.strip()}", flush=True)
json.dump(out,open("/home/user/Mike1272-Bus/audio-voix/episode2-metiers/transcription.json","w"),ensure_ascii=False,indent=1)
