<!doctype html>
<html lang="fr" data-resolution="portrait">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1080, height=1920" />
    <script src="assets/gsap.min.js"></script>
    <style>
      @font-face { font-family: 'Baloo 2'; font-weight: 800; src: url('assets/fonts/Baloo2-ExtraBold.ttf') format('truetype'); }
      @font-face { font-family: 'Work Sans'; font-weight: 400; src: url('assets/fonts/worksans-400.ttf') format('truetype'); }
      @font-face { font-family: 'Work Sans'; font-weight: 700; src: url('assets/fonts/worksans-700.ttf') format('truetype'); }
      @font-face { font-family: 'Hand'; src: url('assets/fonts/NothingYouCouldDo-Regular.ttf') format('truetype'); }
      * { margin: 0; padding: 0; box-sizing: border-box; }
      html, body { width: 1080px; height: 1920px; overflow: hidden; background: #fbf6ee; }
      #root {
        position: relative; width: 1080px; height: 1920px; overflow: hidden;
        font-family: 'Baloo 2', sans-serif; font-weight: 800; color: #111;
        background:
          repeating-linear-gradient(0deg, rgba(0,0,0,0.055) 0 2px, transparent 2px 54px),
          repeating-linear-gradient(90deg, rgba(0,0,0,0.055) 0 2px, transparent 2px 54px),
          radial-gradient(circle at 50% 36%, #fde3c8 0%, #fbf6ee 62%);
      }
      .ab { position: absolute; }
      #progress { position: absolute; left: 0; top: 0; width: 1080px; height: 12px; background: #ff5c00; transform-origin: left center; z-index: 50; }
      .brand { position: absolute; top: 64px; left: 70px; z-index: 40; background: #111; color: #fff; font-size: 28px; letter-spacing: 0.04em; padding: 12px 30px 6px; border-radius: 40px; }
      .serie { position: absolute; top: 64px; right: 70px; z-index: 40; background: #ffd60a; color: #111; font-size: 28px; padding: 12px 26px 6px; border-radius: 40px; border: 4px solid #111; }
      .card { background: #fff; border: 5px solid #111; border-radius: 36px; box-shadow: 14px 14px 0 #111; }
      .pill { text-align: center; background: #ff5c00; color: #fff; border-radius: 70px; border: 5px solid #111; box-shadow: 10px 10px 0 #111; white-space: nowrap; padding: 18px 40px 6px; }
      .pill.y { background: #ffd60a; color: #111; }
      .pill.k { background: #111; color: #fff; box-shadow: 10px 10px 0 #ff5c00; }
      .pill.w { background: #fff; color: #111; }
      .hl { background: #ffd60a; color: #c94200; border-radius: 18px; padding: 0 14px; }
      .spark { position: absolute; width: 70px; height: 70px; z-index: 15; }
      .spark svg { width: 100%; height: 100%; fill: #111; }
      .center { left: 0; width: 1080px; text-align: center; }
      .ico { display: flex; align-items: center; justify-content: center; border-radius: 50%; border: 6px solid #111; box-shadow: 10px 10px 0 #111; background: #fff; }
      .ico svg { width: 60%; height: 60%; }

      /* téléphones de créateurs */
      .ph { width: 320px; height: 600px; border-radius: 44px; background: #111; padding: 10px; box-shadow: 0 30px 60px rgba(60,30,0,0.3); }
      .sc { position: relative; width: 100%; height: 100%; border-radius: 34px; overflow: hidden; }
      .chip { position: absolute; left: 14px; top: 14px; z-index: 3; background: rgba(0,0,0,0.65); color: #fff; font-family: 'Work Sans'; font-weight: 700; font-size: 20px;
              padding: 6px 14px; border-radius: 20px; }
      .side { position: absolute; right: 12px; bottom: 70px; z-index: 3; display: flex; flex-direction: column; gap: 18px; }
      .side i { display: block; width: 42px; height: 42px; border-radius: 50%; background: rgba(255,255,255,0.85); border: 3px solid rgba(0,0,0,0.25); }
      .paper { background: repeating-linear-gradient(0deg, #fdfbf5 0 46px, #c9d7ee 46px 48px); }
      .hand { position: absolute; left: 26px; font-family: 'Hand'; color: #1a2a6c; white-space: nowrap; overflow: hidden; line-height: 1.3; }
      #hw1 { top: 140px; font-size: 76px; width: 0; }
      #hw2 { top: 280px; font-size: 52px; color: #d12a1f; width: 0; }
      #pen { position: absolute; left: 30px; top: 170px; width: 90px; height: 150px; z-index: 2; }
      .motion { background: radial-gradient(circle at 50% 40%, #2b2f63, #15183a); display: flex; flex-direction: column; justify-content: center; padding-left: 30px; }
      .motion span { display: block; font-size: 78px; line-height: 0.95; }
      .scr { background: #fff; }
      .scr .bar { height: 60px; background: #f1f4f9; border-bottom: 2px solid #e2e6ee; }
      .scr .lines { position: absolute; left: 22px; right: 60px; top: 90px; }
      .scr .t { font-family: 'Work Sans'; font-weight: 700; font-size: 30px; line-height: 1.15; color: #202124; margin-bottom: 18px; }
      .scr .l { height: 14px; border-radius: 7px; background: #dfe3ea; margin-bottom: 18px; }
      .scr .cur { display: inline-block; width: 3px; height: 30px; background: #1a73e8; vertical-align: -4px; margin-left: 4px; }
      .sc video, .vc video { width: 100%; height: 100%; object-fit: cover; display: block; }
      #pv { left: 380px; top: 230px; }
      #pm { left: 380px; top: 250px; }
      #desk .vc { width: 100%; height: 560px; border-radius: 22px; overflow: hidden; border: 4px solid #111; }
      #free .vc { height: 230px; border-radius: 18px; overflow: hidden; border: 4px solid #111; margin-bottom: 14px; }
      .sk { width: 460px; height: 420px; overflow: hidden; }
      .sk .vc { position: absolute; inset: 0; }
      .sk .lb { position: absolute; left: 50%; bottom: 18px; transform: translateX(-50%); font-size: 40px; padding: 12px 30px 4px; }
      #k1 { left: 60px; top: 230px; } #k2 { left: 560px; top: 230px; } #k3 { left: 60px; top: 700px; } #k4 { left: 560px; top: 700px; }
      .nf { position: absolute; left: 50%; bottom: -34px; margin-left: -48px; width: 96px; height: 96px; z-index: 6; }
      #p1 { left: 30px; top: 290px; } #p2 { left: 380px; top: 250px; } #p3 { left: 730px; top: 290px; }
      #flipper { left: 380px; top: 250px; width: 320px; height: 600px; transform-style: preserve-3d; }
      #flipper .face { position: absolute; inset: 0; backface-visibility: hidden; -webkit-backface-visibility: hidden; }
      #back { transform: rotateY(180deg); border-radius: 44px; background: #ff5c00; border: 8px solid #111; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 20px; }
      #back svg { width: 200px; height: 200px; }
      #back .q { font-size: 64px; color: #fff; line-height: 1; }
      #bub { left: 150px; top: 960px; width: 780px; height: 200px; font-size: 76px; display: flex; align-items: center; justify-content: center; }
      #bub::after { content: ""; position: absolute; left: 110px; bottom: -44px; border: 22px solid transparent; border-top: 26px solid #111; }
      #toi { left: 330px; top: 960px; font-size: 64px; }

      /* C. likes et besoin */
      #vid { left: 390px; top: 280px; width: 300px; height: 540px; }
      .hrt { width: 90px; height: 90px; z-index: 5; }
      .hrt svg { width: 100%; height: 100%; }
      .man { width: 110px; height: 126px; color: #111; z-index: 4; }
      .man svg { width: 100%; height: 100%; }
      #need { left: 690px; top: 900px; width: 120px; height: 120px; background: #ffd60a; font-size: 90px; z-index: 6; padding-top: 16px; }

      /* D. Grâce */
      #gr { left: 70px; top: 250px; width: 440px; height: 600px; overflow: hidden; }
      #gr svg { width: 100%; height: 100%; }
      #grTag { left: 110px; top: 190px; font-size: 56px; z-index: 6; }
      #desk { left: 70px; top: 230px; width: 940px; height: 740px; padding: 26px; }
      #desk .ong { position: absolute; right: 46px; top: 46px; background: #1c5bd6; color: #fff; font-size: 34px; padding: 8px 20px 0; border-radius: 16px; border: 4px solid #111; }
      #desk svg { width: 170px; height: 190px; }
      #desk .rq { font-family: 'Work Sans'; font-weight: 700; font-size: 46px; line-height: 1.2; margin-top: 16px; background: #eef2fb; border-radius: 22px; padding: 18px 22px; }
      #gb { left: 640px; top: 560px; width: 260px; height: 150px; font-size: 90px; line-height: 1; display: flex; align-items: center; justify-content: center; letter-spacing: 0.1em; z-index: 6; }
      #drop { left: 600px; top: 520px; width: 60px; height: 80px; z-index: 6; }
      #blk { left: 600px; top: 920px; font-size: 64px; transform: rotate(-4deg); z-index: 6; }

      /* E. ampoule */
      #bulb { left: 340px; top: 420px; width: 400px; height: 400px; background: #ffd60a; }

      /* F. lecteur audio */
      #ap { left: 250px; top: 220px; width: 580px; height: 960px; border-radius: 60px; background: #111; padding: 16px; box-shadow: 0 40px 90px rgba(60,30,0,0.35); }
      #ap .in { width: 100%; height: 100%; border-radius: 46px; background: linear-gradient(#fff6ec, #fff); padding: 50px 40px; position: relative; }
      #ap .ttl { font-size: 46px; line-height: 1.02; }
      #ap .sub { font-family: 'Work Sans'; font-weight: 700; font-size: 24px; color: #b83c00; letter-spacing: .08em; margin-top: 10px; }
      #wave { display: flex; align-items: center; gap: 8px; height: 150px; margin-top: 30px; }
      #wave i { flex: 1; background: #ff5c00; border-radius: 6px; height: 30%; }
      .st { display: flex; align-items: center; gap: 20px; margin-top: 26px; padding: 18px 20px; border: 4px solid #111; border-radius: 26px; background: #fff; font-size: 40px; line-height: 1; }
      .st .n { width: 70px; height: 70px; border-radius: 50%; background: #111; color: #fff; display: flex; align-items: center; justify-content: center; font-size: 44px; padding-top: 6px; flex: none; }
      #s3 .n { background: #1faa59; }
      #free { left: 660px; top: 330px; width: 390px; padding: 22px; transform: rotate(4deg); z-index: 5; }
      #free .th { height: 110px; border-radius: 18px; background: #2b2f63; margin-bottom: 14px; display: flex; align-items: center; justify-content: center; }
      #free .th svg { width: 54px; height: 54px; }
      #free .lab { text-align: center; font-size: 40px; color: #1faa59; }
      #cartA { left: 720px; top: 760px; width: 220px; height: 220px; background: #ff5c00; z-index: 6; }
      .coin { width: 90px; height: 90px; border-radius: 50%; background: #ffd60a; border: 5px solid #111; font-size: 56px; display: flex; align-items: center; justify-content: center; padding-top: 8px; z-index: 7; }
      #co1 { left: 900px; top: 720px; } #co2 { left: 880px; top: 1010px; }

      /* G. formats de produit */
      .fmt { left: 190px; width: 700px; height: 210px; display: flex; align-items: center; gap: 34px; padding: 0 40px; }
      .fmt .ic { width: 130px; height: 130px; border-radius: 30px; border: 5px solid #111; display: flex; align-items: center; justify-content: center; flex: none; }
      .fmt .ic svg { width: 70%; height: 70%; }
      .fmt .tx { font-size: 64px; line-height: 1; }
      #f1 { top: 280px; } #f2 { top: 560px; } #f3 { top: 840px; }

      /* I. téléphone */
      #tel { left: 290px; top: 960px; font-size: 60px; }

      /* J. ce soir */
      #night { left: 190px; top: 330px; width: 700px; height: 560px; background: #15183a; border-color: #111; color: #fff; display: flex; flex-direction: column; align-items: center; justify-content: center; }
      #night svg { width: 170px; height: 170px; }
      #night .t { font-size: 90px; line-height: 1; margin-top: 20px; }
      #night .row { display: flex; gap: 40px; margin-top: 40px; }
      #night .row div { width: 110px; height: 110px; border-radius: 50%; background: #ffd60a; color: #111; border: 5px solid #fff; font-size: 70px; display: flex; align-items: center; justify-content: center; padding-top: 10px; }

      /* K. CTA */
      #cbLab { top: 280px; font-size: 100px; line-height: 1.02; }
      #cbox { left: 70px; top: 560px; width: 940px; height: 170px; display: flex; align-items: center; gap: 26px; padding: 0 30px; }
      #cbox .av { width: 100px; height: 100px; border-radius: 50%; background: #ffd60a; border: 5px solid #111; flex: none; }
      #cbox .in { flex: 1; height: 100px; border-radius: 50px; background: #f1ede6; display: flex; align-items: center; padding: 8px 34px 0; font-size: 60px; white-space: nowrap; overflow: hidden; }
      #cbox .in span { opacity: 0; }
      #cbox .send { width: 100px; height: 100px; border-radius: 50%; background: #ff5c00; border: 5px solid #111; flex: none; display: flex; align-items: center; justify-content: center; }
      #cbox .send svg { width: 50px; height: 50px; }
      #dm { left: 130px; top: 800px; width: 820px; height: 190px; display: flex; align-items: center; gap: 26px; padding: 0 30px; }
      #dm img { width: 120px; height: 120px; border-radius: 50%; flex: none; }
      #dm .b { flex: 1; height: 110px; border-radius: 30px 30px 30px 8px; background: #eef2fb; display: flex; align-items: center; gap: 16px; padding: 0 30px; }
      #dm .b i { width: 26px; height: 26px; border-radius: 50%; background: #9aa6c2; }
      #rev { left: 260px; top: 1060px; font-size: 60px; }
      #c3 { left: 780px; top: 1030px; } #c4 { left: 140px; top: 1080px; }

      /* L. abonnement */
      #sub { left: 140px; top: 360px; width: 800px; height: 620px; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 30px; }
      #sub img { width: 300px; height: 300px; border-radius: 50%; }
      #subBtn { font-size: 64px; padding: 22px 70px 10px; }
      #cursor { left: 640px; top: 900px; width: 110px; height: 130px; z-index: 8; }
      #cursor svg { width: 100%; height: 100%; }

      /* sous-titres karaoké */
      #caps { position: absolute; left: 60px; right: 60px; top: 1440px; height: 330px; z-index: 30; }
      .grp { position: absolute; inset: 0; display: flex; flex-wrap: wrap; justify-content: center; align-content: flex-start; column-gap: 18px; row-gap: 4px; text-align: center; font-size: 70px; line-height: 1.22; }
      .w { position: relative; display: inline-block; opacity: 0.3; }
      .w .h { position: absolute; left: -10px; right: -10px; top: 6px; bottom: 2px; background: #ffd60a; border-radius: 14px; transform: scaleX(0); z-index: 0; }
      .w .t { position: relative; z-index: 1; }
      .w.acc .t { color: #c94200; }
      #flash { position: absolute; inset: 0; background: #fff; z-index: 45; opacity: 0; }
    </style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="__DUR__" data-width="1080" data-height="1920">
      <div id="progress"></div>
      <div class="brand">DIGITALMIKAELSON</div>
      <div class="serie">JOUR 5 · ANGLAIS</div>

      <!-- A. les téléphones des créateurs -->
      <div class="ab ph" id="p1"><div class="sc">
        <video id="vH1" class="clip" src="assets/video/hook1.mp4" data-start="__S_H1__" data-duration="__D_H1__" data-track-index="1" muted playsinline></video>
        <div class="chip" data-layout-allow-overlap data-layout-allow-occlusion>TikTok</div>
      </div></div>
      <div class="ab" id="flipper">
        <div class="face ph" id="p2"><div class="sc">
          <video id="vH2" class="clip" src="assets/video/hook2.mp4" data-start="__S_H2__" data-duration="__D_H2__" data-track-index="2" muted playsinline></video>
          <div class="chip" data-layout-allow-overlap data-layout-allow-occlusion>Facebook</div>
        </div></div>
        <div class="face" id="back"><svg viewBox="0 0 100 100"><circle cx="50" cy="30" r="17" fill="#fff" stroke="#111" stroke-width="5"/><path d="M18 94 C18 64 32 52 50 52 C68 52 82 64 82 94 Z" fill="#fff" stroke="#111" stroke-width="5"/></svg><div class="q" data-layout-allow-overlap data-layout-allow-occlusion>Un client</div></div>
      </div>
      <div class="ab ph" id="p3"><div class="sc scr">
        <div class="chip" data-layout-allow-overlap data-layout-allow-occlusion>TikTok</div>
        <div class="bar"></div>
        <div class="lines" id="scrl"><div class="t">Tell me about yourself<span class="cur"></span></div><div class="l" style="width:90%"></div><div class="l" style="width:75%"></div>
          <div class="t">Why do you want this job ?</div><div class="l" style="width:85%"></div><div class="l" style="width:60%"></div>
          <div class="t">What are your strengths ?</div><div class="l" style="width:80%"></div><div class="l" style="width:70%"></div></div>
        <div class="side"><i></i><i></i></div>
      </div></div>
      <div class="ab ph" id="pv"><div class="sc">
        <video id="vVis" class="clip" src="assets/video/visage.mp4" data-start="__S_VIS__" data-duration="__D_VIS__" data-track-index="3" muted playsinline></video>
      </div></div>
      <div class="ab ph" id="pm"><div class="sc motion">
        <div class="chip" data-layout-allow-overlap data-layout-allow-occlusion>TikTok</div>
        <span id="m1" style="color:#ffd60a">HOW</span><span id="m2" style="color:#fff">ARE</span><span id="m3" style="color:#ff8a3d">YOU ?</span>
        <div class="side"><i></i><i></i></div>
      </div></div>
      <div class="ab nf" id="nf1">__NOFACE__</div>
      <div class="ab card" id="bub">Moi aussi !</div>
      <div class="ab pill y" id="toi">Toi aussi</div>

      <!-- C. likes et besoin -->
      <div class="ab hrt" id="h1" style="left:700px;top:620px">__HEART__</div>
      <div class="ab hrt" id="h2" style="left:760px;top:480px">__HEART__</div>
      <div class="ab hrt" id="h3" style="left:290px;top:560px">__HEART__</div>
      <div class="ab man" id="m1p" style="left:80px;top:950px">__MAN__</div>
      <div class="ab man" id="m2p" style="left:260px;top:1010px">__MAN__</div>
      <div class="ab man" id="m3p" style="left:480px;top:1030px">__MAN__</div>
      <div class="ab man" id="m4p" style="left:700px;top:1010px">__MAN__</div>
      <div class="ab man" id="m5p" style="left:880px;top:950px">__MAN__</div>
      <div class="ab ico" id="need">!</div>

      <!-- D. Grâce -->
      <div class="ab pill k" id="grTag">Grâce, 24 ans</div>
      <div class="ab card" id="desk"><div class="vc"><video id="vInt" class="clip" src="assets/video/entretien.mp4" data-start="__S_INT__" data-duration="__D_INT__" data-track-index="4" muted playsinline></video></div>
        <div class="ong">ONG</div><div class="rq">« Tell me about yourself. »</div></div>
      <div class="ab card" id="gb">…</div>
      <svg class="ab" id="drop" viewBox="0 0 60 80"><path d="M30 4 C44 30 54 42 54 54 A24 24 0 0 1 6 54 C6 42 16 30 30 4 Z" fill="#7ec8f0" stroke="#111" stroke-width="4"/></svg>
      <div class="ab pill" id="blk">Elle bloque</div>

      <!-- E. ampoule -->
      <div class="ab ico" id="bulb"><svg viewBox="0 0 100 100"><path d="M50 8 C30 8 18 23 18 40 C18 53 26 60 32 67 C35 71 36 74 36 78 H64 C64 74 65 71 68 67 C74 60 82 53 82 40 C82 23 70 8 50 8 Z" fill="#fff" stroke="#111" stroke-width="5"/><rect x="36" y="80" width="28" height="12" rx="4" fill="#111"/></svg></div>

      <!-- F. lecteur audio -->
      <div class="ab" id="ap"><div class="in">
        <div class="ttl">Simulation<br />d'entretien</div><div class="sub">EN ANGLAIS · AUDIO</div>
        <div id="wave">__BARS__</div>
        <div class="st" id="s1"><div class="n">1</div>La question</div>
        <div class="st" id="s2"><div class="n">2</div>Elle répond</div>
        <div class="st" id="s3"><div class="n">3</div>Ta réponse modèle</div>
      </div></div>
      <div class="ab card" id="free"><div class="vc"><video id="vFree" class="clip" src="assets/video/gratuit.mp4" data-start="__S_FREE__" data-duration="__D_FREE__" data-track-index="5" muted playsinline></video></div><div class="lab">GRATUIT</div></div>
      <div class="ab ico" id="cartA">__CART__</div>
      <div class="ab coin" id="co1">$</div>
      <div class="ab coin" id="co2">$</div>

      <!-- G. formats de produit -->
      <div class="ab card fmt" id="f1"><div class="ic" style="background:#ff5c00">__PLAY__</div><div class="tx">Mini cours vidéo</div></div>
      <div class="ab card fmt" id="f2"><div class="ic" style="background:#ffd60a">__BOOK__</div><div class="tx">Guide d'anglais</div></div>
      <div class="ab card fmt" id="f3"><div class="ic" style="background:#1faa59">__LIST__</div><div class="tx">Check-list</div></div>

      <!-- I. téléphone -->
      <div class="ab pill k" id="tel">Juste ton téléphone</div>

      <!-- J. ce soir -->
      <div class="ab card" id="night"><svg viewBox="0 0 100 100"><path d="M64 10 A42 42 0 1 0 90 64 A34 34 0 1 1 64 10 Z" fill="#ffd60a"/></svg><div class="t">CE SOIR</div>
        <div class="row"><div id="n1">1</div><div id="n2">2</div><div id="n3">3</div></div></div>

      <!-- K. CTA -->
      <div class="ab card sk" id="k1"><div class="vc"><video id="vK1" class="clip" src="assets/video/sk_cuisine.mp4" data-start="__S_SK__" data-duration="__D_SK__" data-track-index="6" muted playsinline></video></div><div class="pill y lb">Cuisine</div></div>
      <div class="ab card sk" id="k2"><div class="vc"><video id="vK2" class="clip" src="assets/video/sk_compta.mp4" data-start="__S_SK__" data-duration="__D_SK__" data-track-index="7" muted playsinline></video></div><div class="pill y lb">Comptabilité</div></div>
      <div class="ab card sk" id="k3"><div class="vc"><video id="vK3" class="clip" src="assets/video/sk_menuiserie.mp4" data-start="__S_SK__" data-duration="__D_SK__" data-track-index="8" muted playsinline></video></div><div class="pill y lb">Menuiserie</div></div>
      <div class="ab card sk" id="k4"><div class="vc"><video id="vK4" class="clip" src="assets/video/sk_anglais.mp4" data-start="__S_SK__" data-duration="__D_SK__" data-track-index="9" muted playsinline></video></div><div class="pill y lb">Anglais</div></div>
      <div class="ab center" id="cbLab">Ta <span class="hl">compétence</span> ?</div>
      <div class="ab card" id="cbox"><div class="av"></div><div class="in">__TYPED__</div>
        <div class="send"><svg viewBox="0 0 24 24" fill="#fff"><path d="M3 20.5 21 12 3 3.5l3 8.5-3 8.5Zm3-8.5h9"/></svg></div></div>
      <div class="ab card" id="dm"><img src="assets/img/logo_rond.png" /><div class="b"><i id="d1"></i><i id="d2"></i><i id="d3"></i></div></div>
      <div class="ab pill y" id="rev">→ un revenu</div>
      <div class="ab coin" id="c3">$</div>
      <div class="ab coin" id="c4">$</div>

      <!-- L. abonnement -->
      <div class="ab card" id="sub"><img src="assets/img/logo_rond.png" /><div class="pill" id="subBtn">S'abonner</div></div>
      <div class="ab" id="cursor"><svg viewBox="0 0 60 70"><path d="M6 4 L6 56 L20 44 L30 66 L40 61 L30 40 L48 40 Z" fill="#fff" stroke="#111" stroke-width="4" stroke-linejoin="round"/></svg></div>

      <div class="spark" id="s1x" style="left:50px;top:180px">__STAR__</div>
      <div class="spark" id="s2x" style="left:960px;top:200px">__STAR__</div>
      <div class="spark" id="s3x" style="left:60px;top:1290px;width:50px;height:50px">__STAR__</div>
      <div class="spark" id="s4x" style="left:960px;top:1300px;width:56px;height:56px">__STAR__</div>

      <div id="caps"></div>
      <div id="flash"></div>
      <audio id="mix" src="assets/audio/mix.wav" data-start="0" data-duration="__DUR__" data-track-index="10" data-volume="1"></audio>
    </div>

    <script>
      window.__timelines = window.__timelines || {};
      const T = __T__;
      const CAPS = __CAPS__;
      const tl = gsap.timeline({ paused: true });
      const IN = (sel, from, to, at) => tl.fromTo(sel, { ...from, autoAlpha: 0 }, { ...to, autoAlpha: 1, immediateRender: false }, at);
      const OUT = (sel, to, at) => tl.to(sel, to, at);
      const HIDE = ["#p1","#flipper","#p3","#pv","#pm","#nf1","#k1","#k2","#k3","#k4","#bub","#toi","#h1","#h2","#h3","#m1p","#m2p","#m3p","#m4p","#m5p","#need",
        "#grTag","#desk","#gb","#drop","#blk","#bulb","#ap","#s1","#s2","#s3","#free","#cartA","#co1","#co2","#f1","#f2","#f3","#tel",
        "#night","#n1","#n2","#n3","#cbLab","#cbox","#dm","#rev","#c3","#c4","#sub","#cursor","#s1x","#s2x","#s3x","#s4x","#flash"];
      gsap.set(HIDE, { autoAlpha: 0 });
      gsap.set(["#m1","#m2","#m3"], { autoAlpha: 0 });
      tl.fromTo("#progress", { scaleX: 0 }, { scaleX: 1, duration: __DUR__, ease: "none" }, 0);
      const flash = (at) => { tl.set("#flash", { autoAlpha: 0.85 }, at); tl.to("#flash", { autoAlpha: 0, duration: 0.22 }, at + 0.04); };
      let lastSparks = 0;
      const SP = ["#s1x","#s2x","#s3x","#s4x"];
      const sparks = (at) => { lastSparks = at; SP.forEach((s, i) => IN(s, { scale: 0, rotation: -90 }, { scale: 1, rotation: 0, duration: 0.35, ease: "back.out(2.5)" }, at + i * 0.1)); };
      const sparksOut = (at) => OUT(SP, { scale: 0, autoAlpha: 0, duration: 0.2 }, Math.max(at, lastSparks + 0.7));
      const pop = (sel, at, rot = 0) => IN(sel, { scale: 0, rotation: rot + 12 }, { scale: 1, rotation: rot, duration: 0.4, ease: "back.out(2.2)" }, at);
      const slam = (sel, at) => IN(sel, { scale: 2.4 }, { scale: 1, duration: 0.3, ease: "power4.in" }, at);
      const rise = (sel, at, rot = 0) => IN(sel, { y: 800, rotation: rot + 8 }, { y: 0, rotation: rot, duration: 0.5, ease: "back.out(1.3)" }, at);
      const leave = (sels, at) => OUT(sels, { autoAlpha: 0, y: -80, duration: 0.3, ease: "power2.in" }, at);
      const motionWords = (at) => ["#m1","#m2","#m3"].forEach((m, i) => IN(m, { scale: 0.2, x: -60 }, { scale: 1, x: 0, duration: 0.25, ease: "back.out(2.5)" }, at + i * 0.22));

      // ---------- A. HOOK : ces vidéos ----------
      tl.set("#flipper", { transformPerspective: 1600 }, 0);
      IN("#p1", { y: 900, rotation: -18 }, { y: 0, rotation: -6, duration: 0.5, ease: "back.out(1.3)" }, 0.05);
      IN("#flipper", { y: 900 }, { y: 0, duration: 0.5, ease: "back.out(1.3)" }, T.jeunes - 0.35);
      IN("#p3", { y: 900, rotation: 18 }, { y: 0, rotation: 6, duration: 0.5, ease: "back.out(1.3)" }, T.tiktok - 0.5);
      tl.fromTo("#scrl", { y: 0 }, { y: -120, duration: 4, ease: "none", immediateRender: false }, T.tiktok);
      rise("#bub", T.dit - 0.1, -1);
      tl.to("#bub", { scale: 1.06, duration: 0.2, yoyo: true, repeat: 1 }, T.moi);
      sparks(T.moi);
      OUT("#bub", { autoAlpha: 0, scale: 0.6, duration: 0.25 }, T.alors - 0.3);
      sparksOut(T.alors - 0.3);

      // ---------- B. derrière ces vidéos ----------
      OUT("#p1", { x: -700, rotation: -30, autoAlpha: 0, duration: 0.4, ease: "power3.in" }, T.alors - 0.1);
      OUT("#p3", { x: 700, rotation: 30, autoAlpha: 0, duration: 0.4, ease: "power3.in" }, T.alors - 0.1);
      tl.to("#flipper", { scale: 1.25, y: 60, duration: 0.4, ease: "power2.out" }, T.alors);
      tl.to("#flipper", { rotationY: 180, duration: 0.6, ease: "power2.inOut" }, T.derriere - 0.2);
      pop("#toi", T.pareil - 0.2, -3);
      OUT(["#flipper", "#toi"], { autoAlpha: 0, scale: 0.7, duration: 0.3 }, T.bonne - 0.35);

      // ---------- C. likes → besoin ----------
      tl.set("#flipper", { rotationY: 0, scale: 1, y: 0 }, T.bonne - 0.05);
      IN("#flipper", { y: 800 }, { y: 0, duration: 0.45, ease: "back.out(1.3)" }, T.bonne);
      [["#h1", 0], ["#h2", 0.15], ["#h3", 0.3]].forEach(([h, d]) => {
        IN(h, { scale: 0, y: 80 }, { scale: 1, y: 0, duration: 0.3, ease: "back.out(3)" }, T.likes - 0.2 + d);
        OUT(h, { y: -260, autoAlpha: 0, duration: 0.8, ease: "power1.in" }, T.likes + 0.3 + d);
      });
      [["#m1p", -500], ["#m2p", -400], ["#m3p", 0], ["#m4p", 400], ["#m5p", 500]].forEach(([m, x], i) =>
        IN(m, { x, y: 200 }, { x: 0, y: 0, duration: 0.45, ease: "back.out(1.5)" }, T.attire + i * 0.08));
      tl.to("#m4p", { color: "#ff5c00", scale: 1.25, duration: 0.25 }, T.besoin - 0.2);
      pop("#need", T.besoin - 0.1, 8);
      leave(["#flipper", "#h1", "#h2", "#h3", "#m1p", "#m2p", "#m3p", "#m4p", "#m5p", "#need"], T.grace - 0.4);

      // ---------- D. Grâce ----------
      IN("#desk", { y: 900, rotation: 6 }, { y: 0, rotation: -1, duration: 0.5, ease: "back.out(1.3)" }, T.grace - 0.3);
      pop("#grTag", T.grace + 0.05, -3);
      pop("#gb", T.bloque - 0.9, 4);
      IN("#drop", { y: -40 }, { y: 0, duration: 0.3 }, T.bloque - 0.5);
      tl.to("#desk", { x: -10, duration: 0.05, yoyo: true, repeat: 7, ease: "none" }, T.bloque - 0.1);
      pop("#blk", T.bloque - 0.15, -4);
      leave(["#grTag", "#desk", "#gb", "#drop", "#blk"], T.besoinla - 0.35);

      // ---------- E. ampoule ----------
      IN("#bulb", { scale: 0, rotation: -60 }, { scale: 1, rotation: 0, duration: 0.45, ease: "back.out(2)" }, T.besoinla - 0.1);
      sparks(T.besoinla + 0.2);
      tl.to("#bulb", { scale: 1.08, duration: 0.25, yoyo: true, repeat: 1 }, T.repondre);
      OUT("#bulb", { scale: 0, autoAlpha: 0, duration: 0.25 }, T.simulation - 0.45);
      sparksOut(T.simulation - 0.45);

      // ---------- F. simulation audio ----------
      rise("#ap", T.simulation - 0.25);
      document.querySelectorAll("#wave i").forEach((b, i) =>
        tl.fromTo(b, { height: "30%" }, { height: (40 + ((i * 37) % 55)) + "%", duration: 0.25, yoyo: true, repeat: 17, ease: "sine.inOut", immediateRender: false }, T.simulation + 0.3 + (i % 5) * 0.05));
      IN("#s1", { x: 200 }, { x: 0, duration: 0.3, ease: "back.out(2)" }, T.question - 0.25);
      IN("#s2", { x: 200 }, { x: 0, duration: 0.3, ease: "back.out(2)" }, T.haute - 0.5);
      IN("#s3", { x: 200 }, { x: 0, duration: 0.3, ease: "back.out(2)" }, T.modele - 0.4);
      tl.to("#ap", { x: -150, scale: 0.86, duration: 0.4, ease: "power2.inOut" }, T.gratuites - 0.5);
      IN("#free", { x: 500, rotation: 20 }, { x: 0, rotation: 4, duration: 0.45, ease: "back.out(1.4)" }, T.gratuites - 0.3);
      pop("#cartA", T.achete - 0.25, -6);
      pop("#co1", T.achete, 0);
      pop("#co2", T.achete + 0.15, 0);
      leave(["#ap", "#free", "#cartA", "#co1", "#co2"], T.partie - 0.35);

      // ---------- G. formats de produit ----------
      IN("#f1", { x: -900 }, { x: 0, duration: 0.4, ease: "back.out(1.4)" }, T.mini - 0.3);
      IN("#f2", { x: 900 }, { x: 0, duration: 0.4, ease: "back.out(1.4)" }, T.guide - 0.3);
      IN("#f3", { x: -900 }, { x: 0, duration: 0.4, ease: "back.out(1.4)" }, T.check - 0.3);
      sparks(T.check);
      sparksOut(T.comptes - 0.35);
      leave(["#f1", "#f2", "#f3"], T.comptes - 0.35);

      // ---------- H. sans visage ----------
      IN("#pv", { y: 900, scale: 1.3 }, { y: 0, scale: 1.3, duration: 0.45, ease: "back.out(1.3)" }, T.comptes - 0.3);
      tl.set("#nf1", { left: 492, top: 1000 }, 0);
      pop("#nf1", T.visage - 0.3, 0);
      tl.to("#nf1", { scale: 1.25, duration: 0.2, yoyo: true, repeat: 1 }, T.visage + 0.2);

      // ---------- I. les trois formats de publication ----------
      tl.to("#pv", { x: -350, y: 60, scale: 1, rotation: -5, duration: 0.45, ease: "power3.inOut" }, T.main - 0.3);
      tl.to("#nf1", { autoAlpha: 0, duration: 0.2 }, T.main - 0.3);
      IN("#pm", { y: 900 }, { y: 0, duration: 0.4, ease: "back.out(1.3)" }, T.texte - 0.35);
      motionWords(T.texte);
      tl.set("#p3", { x: 0, y: 0, scale: 1, rotation: 6 }, T.ecran - 0.5);
      tl.set("#scrl", { y: 0 }, T.ecran - 0.5);
      IN("#p3", { y: 900 }, { y: 0, duration: 0.4, ease: "back.out(1.3)" }, T.ecran - 0.35);
      tl.to("#scrl", { y: -300, duration: 1.0, ease: "power1.inOut" }, T.ecran);
      pop("#tel", T.telephone - 0.25, -2);
      sparks(T.telephone);
      sparksOut(T.soir - 0.3);
      leave(["#pv", "#pm", "#p3", "#tel"], T.soir - 0.35);

      // ---------- J. ce soir ----------
      rise("#night", T.soir - 0.15, -1);
      ["#n1", "#n2", "#n3"].forEach((n, i) => pop(n, T.trois + i * 0.25, 0));
      leave(["#night", "#n1", "#n2", "#n3"], T.competence - 0.6);

      // ---------- K. CTA ----------
      [["#k1", -1], ["#k2", 1], ["#k3", -1], ["#k4", 1]].forEach(([k, d], i) =>
        IN(k, { scale: 0.3, rotation: 20 * d }, { scale: 1, rotation: 2 * d, duration: 0.4, ease: "back.out(1.8)" }, T.competence - 1.0 + i * 0.25));
      leave(["#k1", "#k2", "#k3", "#k4"], T.commente - 0.4);
      flash(T.commente - 0.35);
      slam("#cbLab", T.commente - 0.3);
      IN("#cbox", { y: 300 }, { y: 0, duration: 0.4, ease: "back.out(1.6)" }, T.commente - 0.15);
      document.querySelectorAll("#cbox .in span").forEach((s, i) => tl.set(s, { opacity: 1 }, T.commente + 0.2 + i * 0.09));
      tl.to("#cbox .send", { scale: 1.2, duration: 0.25, yoyo: true, repeat: 3 }, T.commente + 1.0);
      IN("#dm", { x: -900 }, { x: 0, duration: 0.45, ease: "back.out(1.4)" }, T.prive - 0.3);
      ["#d1", "#d2", "#d3"].forEach((d, i) => tl.fromTo(d, { y: 0 }, { y: -12, duration: 0.25, yoyo: true, repeat: 5, ease: "sine.inOut", immediateRender: false }, T.prive + i * 0.1));
      pop("#rev", T.revenu - 0.2, -2);
      pop("#c3", T.revenu, 0);
      pop("#c4", T.revenu + 0.15, 0);
      sparks(T.revenu + 0.1);
      sparksOut(T.abonne - 0.4);
      leave(["#cbLab", "#cbox", "#dm", "#rev", "#c3", "#c4"], T.abonne - 0.4);

      // ---------- L. abonnement ----------
      IN("#sub", { scale: 0.6 }, { scale: 1, duration: 0.35, ease: "back.out(2)" }, T.abonne - 0.25);
      IN("#cursor", { x: 300, y: 300 }, { x: 0, y: 0, duration: 0.35, ease: "power2.out" }, T.abonne - 0.1);
      tl.to("#subBtn", { scale: 0.9, duration: 0.1, yoyo: true, repeat: 1 }, T.abonne + 0.25);
      tl.to("#subBtn", { backgroundColor: "#1faa59", duration: 0.1 }, T.abonne + 0.35);

      // ---------- SOUS-TITRES KARAOKÉ ----------
      CAPS.forEach((c, ci) => {
        const box = document.createElement("div");
        box.className = "grp";
        box.id = "cap" + ci;
        c.words.forEach((w) => {
          const el = document.createElement("span");
          el.className = "w" + (w.acc ? " acc" : "");
          el.innerHTML = '<span class="h"></span><span class="t"></span>';
          el.querySelector(".t").textContent = w.t;
          box.appendChild(el);
          w.el = el;
        });
        document.getElementById("caps").appendChild(box);
        gsap.set(box, { autoAlpha: 0 });
        tl.fromTo(box, { autoAlpha: 0, y: 20 }, { autoAlpha: 1, y: 0, duration: 0.14, ease: "power2.out", immediateRender: false }, Math.max(0, c.start - 0.08));
        c.words.forEach((w, i) => {
          const hl = w.el.querySelector(".h");
          tl.to(w.el, { opacity: 1, duration: 0.06 }, w.s);
          tl.set(hl, { transformOrigin: "left center" }, w.s);
          tl.to(hl, { scaleX: 1, duration: 0.08, ease: "power1.out" }, w.s);
          if (i < c.words.length - 1) {
            tl.set(hl, { transformOrigin: "right center" }, w.e - 0.06);
            tl.to(hl, { scaleX: 0, duration: 0.08, ease: "power1.in" }, w.e - 0.06);
          }
        });
        tl.to(box, { autoAlpha: 0, duration: 0.1 }, c.hide - 0.1);
      });

      window.__timelines["main"] = tl;
    </script>
  </body>
</html>
