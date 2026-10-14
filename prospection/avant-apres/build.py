"""Construit les 6 vidéos « avant / après » (16 s, 1080x1920) d'Allegra Digital Ground."""
import os, re, shutil, subprocess
HERE = os.path.dirname(os.path.abspath(__file__))
C = os.path.join(HERE, "_commun")
SFX_DIR = os.path.join(HERE, "..", "..", "video-excel-13h", "assets", "sfx")
MUSIC = os.path.join(HERE, "..", "..", "video-excel-13h", "assets", "audio", "musique.wav")
PRODUITS = {
  "burger": ("Burger", ["Juteux.", "Croustillant.", "Irrésistible."], "#ff8a00", ["hamburger", "french_fries", "fire"]),
  "cosmetiques": ("Cosmétiques", ["Éclat.", "Couleur.", "Glamour."], "#ff4f9a", ["lipstick", "sparkles", "hundred_points"]),
  "glace": ("Glaces", ["Fraîche.", "Fondante.", "Gourmande."], "#ff6fa8", ["soft_ice_cream", "ice_cream", "sparkles"]),
  "chaussures": ("Chaussures", ["Confort.", "Style.", "Énergie."], "#2fd06b", ["running_shoe", "high_voltage", "sparkles"]),
  "gadget": ("Gadgets", ["Précis.", "Élégant.", "Connecté."], "#2ec4ff", ["watch", "mobile_phone", "high_voltage"]),
  "vetements-femmes": ("Mode femme", ["Élégance.", "Douceur.", "Confiance."], "#e8b04b", ["dress", "handbag", "ribbon"]),
}
DUR = 16.0
WA = '<svg width="58" height="58" viewBox="0 0 24 24" fill="#0b1e4a"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm5.2 14.1c-.2.6-1.3 1.2-1.8 1.2-.5.1-1 .1-3.3-.8-2.8-1.1-4.5-3.9-4.7-4.1-.1-.2-1.1-1.5-1.1-2.9s.7-2 1-2.3c.2-.3.5-.3.7-.3h.5c.2 0 .4 0 .6.5l.8 2c.1.2.1.4 0 .5l-.4.6-.4.4c-.1.2-.3.3-.1.6.2.3.8 1.3 1.7 2.1 1.2 1 2.1 1.4 2.4 1.5.3.2.5.1.6-.1l.9-1c.2-.3.4-.2.6-.1l1.9.9c.3.1.5.2.5.3.1.2.1.8-.2 1.5z"/></svg>'
LOGO = '<svg width="110" height="124" viewBox="0 0 120 120"><g transform="translate(6 7)" fill="none" stroke="#ffd60a" stroke-width="8" stroke-linejoin="round" stroke-linecap="round"><path d="M42 32v-8a16 16 0 0 1 32 0v8"/><path d="M18 32h80l-7 66a8 8 0 0 1-8 7H33a8 8 0 0 1-8-7z"/></g><g fill="none" stroke="#fff" stroke-width="8" stroke-linejoin="round" stroke-linecap="round"><path d="M42 32v-8a16 16 0 0 1 32 0v8"/><path d="M18 32h80l-7 66a8 8 0 0 1-8 7H33a8 8 0 0 1-8-7z"/></g><path d="M50 52 L76 68 L50 84 Z" fill="#ffd60a" stroke="#ffd60a" stroke-width="6" stroke-linejoin="round"/></svg>'

def fs(w):
    return 150 if len(w) <= 8 else (124 if len(w) <= 11 else 108)

SCRIPT = """    <script>
      window.__timelines = window.__timelines || {};
      const tl = gsap.timeline({ paused: true });
      const HIDE = [];
      const FT = (s, f, t, at) => tl.fromTo(s, f, { ...t, immediateRender: false }, at);
      const IN = (s, f, t, at) => { HIDE.push(s); return FT(s, { ...f, autoAlpha: 0 }, { ...t, autoAlpha: 1 }, at); };
      const OUT = (s, at) => FT(s, { autoAlpha: 1 }, { autoAlpha: 0, duration: 0.01 }, at);
      const pop = (s, at) => IN(s, { scale: 0.2, rotation: -25 }, { scale: 1, rotation: 0, duration: 0.45, ease: "back.out(2)" }, at);
      const slam = (s, at) => IN(s, { scale: 2.3, filter: "blur(14px)" }, { scale: 1, filter: "blur(0px)", duration: 0.35, ease: "power4.out" }, at);
      const word = (s, at) => IN(s, { y: -50, scale: 1.3, filter: "blur(12px)" }, { y: 0, scale: 1, filter: "blur(0px)", duration: 0.3, ease: "power3.out" }, at);
      const float = (s, at, d, y) => FT(s, { y: 0 }, { y: y, duration: d / 2, yoyo: true, repeat: 1, ease: "sine.inOut" }, at);
      [["#s1", "#k1", 0, 4.2], ["#s2", "#k2", 4.2, 8.2], ["#s3", "#k3", 12.4, 3.6]].forEach(([s, c, a, d], i) => {
        HIDE.push(s); tl.set(s, { autoAlpha: 1 }, a); if (i < 2) tl.set(s, { autoAlpha: 0 }, a + d);
        FT(c, { scale: 1.14 }, { scale: 1, duration: 0.45, ease: "expo.out" }, a);
        FT(c, { rotation: 0, x: 0 }, { rotation: i % 2 ? 0.6 : -0.6, x: i % 2 ? -16 : 16, duration: d, ease: "sine.inOut" }, a);
      });
      // AVANT : une photo fixe que l'on fait défiler
      IN("#p1", { y: -80 }, { y: 0, duration: 0.35, ease: "back.out(2)" }, 0.1);
      word("#t1", 0.3);
      IN("#feed", { y: 400 }, { y: 0, duration: 0.6, ease: "power2.out" }, 0.2);
      IN("#meta", { y: 20 }, { y: 0, duration: 0.3 }, 0.8);
      word("#t2", 1.8);
      pop("#zz", 2.2); float("#zz", 2.5, 1.2, -20);
      FT(["#feed", "#meta"], { y: 0 }, { y: -1500, duration: 0.7, ease: "power2.in" }, 3.0);
      // passage
      HIDE.push("#iris");
      FT("#iris", { autoAlpha: 1, scale: 0 }, { scale: 24, duration: 0.3, ease: "power2.in" }, 3.9);
      FT("#iris", { scale: 24 }, { scale: 0, duration: 0.35, ease: "power2.out" }, 4.2);
      tl.set("#iris", { autoAlpha: 0 }, 4.6);
      // APRÈS : la vidéo et les animations
      IN("#p2", { y: -80, scale: 1.5 }, { y: 0, scale: 1, duration: 0.4, ease: "back.out(2)" }, 4.3);
      IN("#card", { y: 300, scale: 0.85, rotation: -4 }, { y: 0, scale: 1, rotation: -1.5, duration: 0.6, ease: "back.out(1.4)" }, 4.25);
      FT("#card", { rotation: -1.5 }, { rotation: 1.5, duration: 3.6, yoyo: true, repeat: 1, ease: "sine.inOut" }, 4.9);
      IN("#w1", { y: -300, scale: 1.4 }, { y: 0, scale: 1, duration: 0.5, ease: "bounce.out" }, 5.0); OUT("#w1", 6.6);
      slam("#w2", 6.6); OUT("#w2", 8.2);
      slam("#w3", 8.2);
      FT("#k2", { x: 0 }, { x: 12, duration: 0.05, yoyo: true, repeat: 5 }, 6.65);
      FT("#k2", { x: 0 }, { x: 12, duration: 0.05, yoyo: true, repeat: 5 }, 8.25);
      pop("#i1", 5.4); float("#i1", 5.8, 3.0, -24);
      pop("#i2", 6.9); float("#i2", 7.3, 3.0, -20);
      pop("#i3", 8.5); float("#i3", 8.9, 2.4, -18);
      IN("#badge", { scale: 0, rotation: -180 }, { scale: 1, rotation: 12, duration: 0.6, ease: "back.out(1.8)" }, 7.4);
      FT("#badge", { rotation: 12 }, { rotation: -8, duration: 0.8, yoyo: true, repeat: 4, ease: "sine.inOut" }, 8.0);
      FT("#shine", { backgroundPosition: "100% 0%" }, { backgroundPosition: "-50% 0%", duration: 0.9, ease: "power2.inOut" }, 5.6);
      FT("#shine", { backgroundPosition: "100% 0%" }, { backgroundPosition: "-50% 0%", duration: 0.9, ease: "power2.inOut" }, 9.4);
      IN("#cta", { y: 200, scale: 0.6 }, { y: 0, scale: 1, duration: 0.5, ease: "back.out(2)" }, 9.8);
      FT("#cta", { scale: 1 }, { scale: 1.06, duration: 0.25, yoyo: true, repeat: 3, ease: "sine.inOut" }, 10.5);
      IN("#tag", { y: 20 }, { y: 0, duration: 0.4 }, 10.2);
      // FIN
      pop("#lg", 12.5);
      word("#e1", 12.75);
      IN("#e2", { y: -300, scale: 1.4 }, { y: 0, scale: 1, duration: 0.5, ease: "bounce.out" }, 13.0);
      IN("#e3", { scale: 0.4 }, { scale: 1, duration: 0.4, ease: "back.out(2.2)" }, 13.5);
      IN("#btn", { scale: 0.3 }, { scale: 1, duration: 0.45, ease: "back.out(2.5)" }, 13.9);
      FT("#btn", { scale: 1 }, { scale: 1.06, duration: 0.25, yoyo: true, repeat: 3, ease: "sine.inOut" }, 14.5);
      word("#num", 14.2); word("#wm", 14.4);
      FT("#fade", { opacity: 0 }, { opacity: 1, duration: 0.3 }, 15.7);
      gsap.set(HIDE, { autoAlpha: 0 });
      gsap.set("#s1", { autoAlpha: 1 });
      gsap.set("#fade", { opacity: 0 });
      window.__timelines["main"] = tl;
    </script>
  </body>
</html>
"""

def dark(h, k):
    h = h.lstrip('#'); r, g, b = (int(h[i:i+2], 16) for i in (0, 2, 4))
    return '#%02x%02x%02x' % (int(r*k), int(g*k), int(b*k))

def page(titre, mots, acc, icons):
    w1, w2, w3 = mots
    d1, d2, d3 = dark(acc, .82), dark(acc, .62), dark(acc, .45)
    depth = f"0 4px 0 {d1}, 0 8px 0 {d2}, 0 12px 0 {d3}, 0 26px 36px rgba(60,30,0,0.3)"
    sw = lambda d: f'<svg class="swoosh" viewBox="0 0 1680 2520"><path d="{d}" fill="none" stroke="#efe6d6" stroke-width="230" stroke-linecap="round"/></svg>'
    logo = LOGO.replace('stroke="#fff"', 'stroke="#1c1206"').replace('stroke="#ffd60a"', f'stroke="{acc}"').replace('fill="#ffd60a" stroke="#ffd60a"', f'fill="{acc}" stroke="{acc}"')
    return f"""<!doctype html>
<html lang="fr" data-resolution="portrait">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1080, height=1920" />
    <script src="assets/gsap.min.js"></script>
    <style>
      @font-face {{ font-family: 'Inter'; font-weight: 600; src: url('assets/fonts/inter-latin-600-normal.woff2') format('woff2'); }}
      @font-face {{ font-family: 'Inter'; font-weight: 800; src: url('assets/fonts/inter-latin-800-normal.woff2') format('woff2'); }}
      @font-face {{ font-family: 'Inter'; font-weight: 900; src: url('assets/fonts/inter-latin-900-normal.woff2') format('woff2'); }}
      * {{ margin: 0; padding: 0; box-sizing: border-box; }}
      html, body {{ width: 1080px; height: 1920px; overflow: hidden; background: #ffffff; }}
      #root {{ position: relative; width: 1080px; height: 1920px; overflow: hidden; font-family: 'Inter', sans-serif; color: #1c1206; }}
      .ab {{ position: absolute; }}
      .scene {{ position: absolute; left: 0; top: 0; width: 1080px; height: 1920px; overflow: hidden; }}
      .cam {{ position: absolute; left: 0; top: 0; width: 1080px; height: 1920px; }}
      .cream {{ background: radial-gradient(ellipse at 50% 42%, #fffaf0 0%, #f6eddc 68%, #ecdfc6 100%); }}
      .white {{ background: radial-gradient(ellipse at 50% 45%, #ffffff 0%, #f8f6f2 65%, #eeeae3 100%); }}
      .swoosh {{ position: absolute; left: -300px; top: -300px; width: 1680px; height: 2520px; }}
      .line {{ position: absolute; left: 0; width: 1080px; text-align: center; white-space: nowrap; }}
      .sm {{ font-weight: 600; font-size: 62px; letter-spacing: -0.02em; color: #1c1206; }}
      .big {{ font-weight: 900; font-size: 124px; letter-spacing: -0.045em; line-height: 0.95; color: {acc}; text-shadow: {depth}; }}
      .pill {{ position: absolute; height: 96px; border-radius: 48px; font-weight: 800; font-size: 46px; line-height: 96px; text-align: center; white-space: nowrap; }}
      .obj {{ position: absolute; filter: drop-shadow(0 22px 28px rgba(60,30,0,0.3)); }}
      /* avant */
      #s1 {{ background: #e4e2de; }}
      .feed {{ position: absolute; left: 110px; top: 330px; width: 860px; height: 1075px; border-radius: 30px; overflow: hidden; background: #ccc; box-shadow: 0 18px 36px rgba(0,0,0,0.12); }}
      .feed img {{ width: 100%; height: 100%; object-fit: cover; }}
      #meta {{ left: 120px; top: 1430px; font-weight: 600; font-size: 34px; color: #7a776f; }}
      .gray {{ color: #4a4740; }}
      /* après */
      #card {{ position: absolute; left: 110px; top: 250px; width: 860px; height: 1075px; border-radius: 40px; overflow: hidden; border: 12px solid #fff; box-shadow: 0 34px 60px rgba(60,30,0,0.28); }}
      #card video {{ width: 100%; height: 100%; object-fit: cover; }}
      #shine {{ position: absolute; left: 0; top: 0; width: 100%; height: 100%; background: linear-gradient(105deg, rgba(255,255,255,0) 40%, rgba(255,255,255,0.55) 50%, rgba(255,255,255,0) 60%); background-size: 300% 100%; background-repeat: no-repeat; }}
      .kw {{ position: absolute; left: 0; width: 1080px; top: 1370px; text-align: center; }}
      #badge {{ position: absolute; left: 790px; top: 190px; width: 230px; height: 230px; border-radius: 50%; background: {acc}; color: #fff; font-weight: 900; font-size: 38px; line-height: 230px; text-align: center; white-space: nowrap; box-shadow: 0 8px 0 {d2}, 0 20px 30px rgba(60,30,0,0.3); }}
      .pg {{ background: #1a9e4b; color: #fff; box-shadow: 0 14px 30px rgba(0,0,0,0.18); display: flex; align-items: center; justify-content: center; gap: 18px; }}
      .pa {{ background: {acc}; color: #fff; box-shadow: 0 8px 0 {d2}, 0 18px 30px rgba(60,30,0,0.25); }}
      #tag {{ left: 0; width: 1080px; top: 1800px; text-align: center; font-weight: 800; font-size: 24px; letter-spacing: .16em; text-transform: uppercase; color: #a08a66; white-space: nowrap; }}
      #iris {{ left: 540px; top: 960px; width: 100px; height: 100px; margin: -50px 0 0 -50px; border-radius: 50%; background: {acc}; z-index: 30; }}
      #fade {{ left: 0; top: 0; width: 1080px; height: 1920px; background: #fff; z-index: 40; }}
    </style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="{DUR:g}" data-width="1080" data-height="1920">

      <!-- AVANT (0 - 4,2) -->
      <div class="scene" id="s1"><div class="cam" id="k1">
        <div class="pill" id="p1" style="left:390px; top:110px; width:300px; background:#e5483b; color:#fff">AVANT</div>
        <div class="line sm gray" id="t1" style="top:225px">Une simple photo…</div>
        <div class="feed" id="feed"><img src="assets/avant.jpg" alt="" /></div>
        <div class="ab" id="meta">♡ 0 &nbsp;&nbsp; 💬 0 &nbsp;&nbsp; ↗ 0</div>
        <div class="line sm gray" id="t2" style="top:1540px">…on passe sans s'arrêter</div>
        <img class="obj" id="zz" src="assets/icons/zzz_3d.png" style="left:860px; top:260px; width:170px; height:170px" />
      </div></div>

      <!-- APRÈS (4,2 - 12,4) -->
      <div class="scene cream" id="s2"><div class="cam" id="k2">
        {sw("M200 -100 C 700 700, 1000 1300, 1500 2600")}
        <div class="pill" id="p2" style="left:390px; top:110px; width:300px; background:#1a9e4b; color:#fff">APRÈS</div>
        <div id="card">
          <video id="vcard" class="clip" src="assets/apres.mp4" muted playsinline data-start="4.2" data-duration="8.2" data-track-index="2"></video>
          <div id="shine"></div>
        </div>
        <div class="kw" id="w1"><span class="big" style="font-size:{fs(w1)}px">{w1}</span></div>
        <div class="kw" id="w2"><span class="big" style="font-size:{fs(w2)}px">{w2}</span></div>
        <div class="kw" id="w3"><span class="big" style="font-size:{fs(w3)}px">{w3}</span></div>
        <div id="badge">NOUVEAU</div>
        <img class="obj" id="i1" src="assets/icons/{icons[0]}_3d.png" style="left:20px; top:170px; width:230px; height:230px" />
        <img class="obj" id="i2" src="assets/icons/{icons[1]}_3d.png" style="left:860px; top:1180px; width:190px; height:190px" />
        <img class="obj" id="i3" src="assets/icons/{icons[2]}_3d.png" style="left:30px; top:1200px; width:170px; height:170px" />
        <div class="pill pg ab" id="cta" style="left:150px; top:1600px; width:780px">{WA.replace('#0b1e4a', '#fff').replace('58', '50')}Commandez sur WhatsApp</div>
        <div class="ab" id="tag">Exemple de pub · Allegra · {titre}</div>
      </div></div>

      <!-- FIN (12,4 - 16) -->
      <div class="scene white" id="s3"><div class="cam" id="k3">
        {sw("M1500 -100 C 900 800, 700 1300, 200 2600")}
        <div class="ab" id="lg" style="left:440px; top:300px; transform-origin:100px 110px; zoom:1.8">{logo}</div>
        <div class="line sm" id="e1" style="top:560px">Vos produits</div>
        <div class="line" id="e2" style="top:660px"><span class="big" style="font-size:130px">méritent ça.</span></div>
        <div class="pill pa" id="e3" style="left:190px; top:880px; width:700px">Vidéo d'essai gratuite 🎁</div>
        <div class="pill pg ab" id="btn" style="left:190px; top:1080px; width:700px; height:120px; line-height:120px; border-radius:60px; font-size:56px">{WA.replace('#0b1e4a', '#fff')}Écrivez ESSAI</div>
        <div class="line" id="num" style="top:1250px; font-weight:800; font-size:56px">+243 831 710 181</div>
        <div class="line" id="wm" style="top:1360px; font-weight:800; font-size:34px; letter-spacing:.08em; text-transform:uppercase; color:#a08a66">Allegra Digital Ground</div>
      </div></div>

      <div class="ab" id="iris"></div>
      <div class="ab" id="fade"></div>
      <audio id="mix" src="assets/mix.wav" data-start="0" data-duration="{DUR:g}" data-track-index="1" data-volume="1"></audio>
    </div>
""" + SCRIPT

SFX = [(0.1, "pop", 0.2), (0.2, "whoosh-short", 0.18), (1.8, "click-soft", 0.15), (2.2, "pop", 0.15), (3.0, "whoosh", 0.25),
       (3.9, "riser", 0.25), (4.2, "whoosh-cinematic", 0.35), (4.3, "impact-bass-2", 0.3),
       (5.0, "impact-bass-1", 0.28), (5.4, "pop", 0.2), (5.6, "sparkle", 0.2), (6.6, "impact-bass-1", 0.28), (6.9, "pop", 0.2),
       (7.4, "whoosh-short", 0.22), (8.2, "impact-bass-2", 0.3), (8.5, "pop", 0.2), (9.4, "sparkle", 0.2), (9.8, "pop", 0.25), (10.5, "notification", 0.25),
       (12.4, "whoosh", 0.3), (12.5, "pop", 0.22), (12.8, "impact-bass-1", 0.25), (13.15, "impact-bass-2", 0.25), (13.9, "pop", 0.25), (14.5, "chime", 0.3)]
def mix(out):
    inputs = ["-i", MUSIC]
    fl = [f"[0:a]aresample=44100,aformat=channel_layouts=stereo,atrim=start=20:duration={DUR},asetpts=PTS-STARTPTS,volume=0.85,afade=t=in:d=0.4,afade=t=out:st={DUR-1}:d=1[mus]"]
    lab = ["[mus]"]
    for i, (t, n, v) in enumerate(SFX):
        inputs += ["-i", os.path.join(SFX_DIR, n + ".mp3")]; d = int(t * 1000)
        fl.append(f"[{i+1}:a]aresample=44100,aformat=channel_layouts=stereo,volume={v},adelay={d}|{d}[s{i}]"); lab.append(f"[s{i}]")
    fl.append("".join(lab) + f"amix=inputs={len(lab)}:normalize=0:duration=first,apad,atrim=duration={DUR},loudnorm=I=-14:TP=-1.5:LRA=11[out]")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error"] + inputs + ["-filter_complex", ";".join(fl), "-map", "[out]", "-ar", "44100", out], check=True)

mixwav = os.path.join(C, "mix.wav")
if not os.path.exists(mixwav): mix(mixwav)
for slug, (titre, mots, acc, icons) in PRODUITS.items():
    d = os.path.join(HERE, slug); a = os.path.join(d, "assets")
    for f in ["gsap.min.js", "mix.wav"]: shutil.copy(os.path.join(C, f), a)
    for sub in ["fonts"]:
        if not os.path.exists(os.path.join(a, sub)): shutil.copytree(os.path.join(C, sub), os.path.join(a, sub))
    os.makedirs(os.path.join(a, "icons"), exist_ok=True)
    for ic in icons + ["zzz"]: shutil.copy(os.path.join(C, "icons", ic + "_3d.png"), os.path.join(a, "icons"))
    for f in ["hyperframes.json", "package.json"]: shutil.copy(os.path.join(C, f), d)
    open(os.path.join(d, "meta.json"), "w").write('{"id":"avant-apres-%s","name":"Avant / après : %s"}' % (slug, titre))
    open(os.path.join(d, "index.html"), "w").write(page(titre, mots, acc, icons))
    print("ok", slug)
