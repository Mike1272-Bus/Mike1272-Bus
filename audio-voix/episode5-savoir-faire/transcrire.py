import subprocess, numpy as np, sherpa_onnx, json, sys
SR=16000; M="/tmp/claude-0/sherpa-onnx-whisper-small/"
rec = sherpa_onnx.OfflineRecognizer.from_whisper(encoder=M+"small-encoder.int8.onnx", decoder=M+"small-decoder.int8.onnx", tokens=M+"small-tokens.txt", language="fr", task="transcribe", num_threads=4)
src=sys.argv[1]
y=np.frombuffer(subprocess.run(["ffmpeg","-loglevel","error","-i",src,"-f","f32le","-ac","1","-ar",str(SR),"-"],capture_output=True).stdout,np.float32)
fr=int(0.02*SR); n=len(y)//fr
e=20*np.log10(np.sqrt((y[:n*fr].reshape(n,fr)**2).mean(1))+1e-9)
quiet=e<np.percentile(e,10)+10
segs=[]; i=0; cur=None
while i<n:
    if not quiet[i]:
        if cur is None: cur=i
        i+=1
    else:
        j=i
        while j<n and quiet[j]: j+=1
        if cur is not None and (j-i)*0.02>=0.3: segs.append((cur*0.02,i*0.02)); cur=None
        i=j
if cur is not None: segs.append((cur*0.02,n*0.02))
out=[]
for a,b in segs:
    if b-a<0.25: continue
    s=rec.create_stream(); s.accept_waveform(SR,y[int(max(a-0.1,0)*SR):int((b+0.15)*SR)]); rec.decode_stream(s)
    out.append((round(a,2),round(b,2),s.result.text.strip())); print(f"{a:6.2f}-{b:6.2f}  {s.result.text.strip()}",flush=True)
json.dump(out,open(sys.argv[2],"w"),ensure_ascii=False,indent=1)
