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
      .pill.g { background: #1faa59; color: #fff; }
      .spark { position: absolute; width: 70px; height: 70px; z-index: 15; }
      .spark svg { width: 100%; height: 100%; fill: #111; }
      .center { left: 0; width: 1080px; text-align: center; }
      .ico { display: flex; align-items: center; justify-content: center; border-radius: 50%; border: 6px solid #111; box-shadow: 10px 10px 0 #111; background: #fff; }
      .ico svg { width: 62%; height: 62%; }
      .num { display: flex; align-items: center; justify-content: center; border-radius: 50%; border: 6px solid #111; box-shadow: 8px 8px 0 #111; padding-top: 12px; }

      /* téléphones */
      .ph { width: 320px; height: 600px; border-radius: 44px; background: #111; padding: 10px; box-shadow: 0 30px 60px rgba(60,30,0,0.3); }
      .ph.big { width: 390px; height: 720px; border-radius: 52px; padding: 12px; }
      .sc { position: relative; width: 100%; height: 100%; border-radius: 34px; overflow: hidden; }
      .ph.big .sc { border-radius: 40px; }
      .chip { position: absolute; left: 14px; top: 14px; z-index: 3; background: rgba(0,0,0,0.65); color: #fff; font-family: 'Work Sans'; font-weight: 700; font-size: 22px; padding: 6px 14px; border-radius: 20px; }
      .sc video, .vc video { width: 100%; height: 100%; object-fit: cover; display: block; }
      .nf { position: absolute; width: 110px; height: 110px; z-index: 6; }
      .nf svg { width: 100%; height: 100%; }

      /* A. hook */
      #sunTag { left: 340px; top: 170px; z-index: 12; font-size: 56px; display: flex; align-items: center; gap: 16px; }
      #sunTag svg { width: 60px; height: 60px; margin-top: -8px; }
      #p1 { left: 50px; top: 320px; } #p2 { left: 710px; top: 320px; } #pv { left: 380px; top: 280px; }
      #nf0 { left: 485px; top: 1000px; }
      #night { left: 190px; top: 300px; width: 700px; height: 640px; background: #15183a; color: #fff; display: flex; flex-direction: column; align-items: center; justify-content: center; }
      #night svg { width: 170px; height: 170px; }
      #night .t { font-size: 96px; line-height: 1; margin-top: 20px; }
      #night .row { display: flex; gap: 40px; margin-top: 40px; }
      #night .row div { width: 120px; height: 120px; border-radius: 50%; background: #ffd60a; color: #111; border: 5px solid #fff; font-size: 76px; display: flex; align-items: center; justify-content: center; padding-top: 10px; }

      /* B. promesse */
      #hello { left: 290px; top: 230px; width: 500px; height: 280px; display: flex; align-items: center; justify-content: center; font-size: 120px; color: #1c5bd6; }
      #hello::after { content: ""; position: absolute; left: 90px; bottom: -48px; border: 24px solid transparent; border-top: 28px solid #111; }
      #cam { left: 150px; top: 700px; width: 320px; height: 320px; }
      #nfB { left: 610px; top: 700px; width: 320px; height: 320px; }
      #nfB svg { width: 100%; height: 100%; }
      .x { position: absolute; left: -20px; top: 140px; width: 360px; height: 40px; background: #e0161a; border: 5px solid #111; border-radius: 20px; transform: rotate(-38deg); }
      #t1 { left: 90px; top: 330px; background: #ffd60a; } #t2 { left: 430px; top: 330px; background: #ff5c00; color: #fff; } #t3 { left: 770px; top: 330px; background: #1faa59; color: #fff; }
      .tn { width: 220px; height: 220px; font-size: 150px; z-index: 6; }
      #bigPh { left: 390px; top: 640px; width: 300px; height: 560px; border-radius: 50px; background: #111; padding: 14px; box-shadow: 14px 14px 0 #ff5c00; }
      #bigPh .scr { width: 100%; height: 100%; border-radius: 38px; background: linear-gradient(#fff6ec, #fff); }

      /* C. comptes sans visage */
      #q1 { left: 30px; top: 300px; } #q2 { left: 380px; top: 260px; } #q3 { left: 730px; top: 300px; }
      #nq1 { left: 135px; top: 850px; } #nq2 { left: 485px; top: 810px; } #nq3 { left: 835px; top: 850px; }
      #never { left: 250px; top: 1020px; font-size: 64px; }

      /* D. toi aussi */
      #ils { left: 70px; top: 420px; width: 420px; height: 380px; display: flex; flex-wrap: wrap; align-items: center; justify-content: center; gap: 20px; padding: 20px; }
      #ils .m { width: 110px; height: 130px; position: relative; color: #111; }
      #ils .m svg { width: 100%; height: 100%; }
      #ils .ok { position: absolute; right: -14px; bottom: -6px; width: 54px; height: 54px; border-radius: 50%; background: #1faa59; border: 4px solid #111; }
      #ils .ok::after { content: ""; position: absolute; left: 14px; top: 8px; width: 14px; height: 24px; border: solid #fff; border-width: 0 6px 6px 0; transform: rotate(45deg); }
      #eq { left: 505px; top: 520px; font-size: 150px; line-height: 1; }
      #you { left: 640px; top: 380px; width: 360px; height: 420px; display: flex; flex-direction: column; align-items: center; justify-content: center; background: #ff5c00; }
      #you .m { width: 180px; height: 210px; color: #fff; }
      #you .m svg { width: 100%; height: 100%; }
      #toi { left: 660px; top: 860px; font-size: 64px; }
      #arrow { left: 470px; top: 1010px; width: 140px; height: 200px; }

      /* E. les trois formats */
      .fh { left: 70px; top: 180px; display: flex; align-items: center; gap: 24px; }
      .fh .num { width: 140px; height: 140px; font-size: 100px; }
      .fh .pill { font-size: 60px; }
      #vT { left: 70px; top: 360px; width: 940px; height: 620px; padding: 16px; }
      #vT .vc { width: 100%; height: 100%; border-radius: 22px; overflow: hidden; }
      #vT video { object-position: left center; }
      #icp { left: 800px; top: 440px; width: 170px; height: 170px; z-index: 5; }
      #icm { left: 800px; top: 650px; width: 170px; height: 170px; z-index: 5; }
      #recPh { left: 830px; top: 300px; width: 150px; height: 230px; z-index: 6; }
      #paperC { left: 110px; top: 1020px; width: 860px; height: 370px; overflow: hidden; }
      .paper { background: repeating-linear-gradient(0deg, #fdfbf5 0 58px, #c9d7ee 58px 61px); }
      .hand { position: absolute; left: 50px; font-family: 'Hand'; color: #1a2a6c; white-space: nowrap; overflow: hidden; line-height: 1.25; width: 0; }
      #hw1 { top: 40px; font-size: 104px; }
      #hw2 { top: 190px; font-size: 84px; color: #d12a1f; }
      #pc { left: 70px; top: 340px; }
      #kin { left: 510px; top: 340px; width: 500px; height: 720px; background: radial-gradient(circle at 50% 40%, #2b2f63, #15183a); display: flex; flex-direction: column; justify-content: center; padding-left: 40px; }
      #kin span { display: block; font-size: 88px; line-height: 1.02; }
      #voice { left: 70px; top: 1110px; width: 940px; height: 200px; display: flex; align-items: center; gap: 30px; padding: 0 40px; }
      #voice .mic { width: 130px; height: 130px; border-radius: 50%; background: #ff5c00; border: 5px solid #111; display: flex; align-items: center; justify-content: center; flex: none; }
      #voice .mic svg { width: 64px; height: 64px; }
      #wave { flex: 1; display: flex; align-items: center; gap: 12px; height: 130px; }
      #wave i { flex: 1; background: #111; border-radius: 8px; height: 25%; }
      #gd { left: 60px; top: 360px; width: 960px; height: 960px; overflow: hidden; padding: 0; }
      #gd .top { height: 110px; display: flex; align-items: center; gap: 22px; padding: 0 30px; border-bottom: 3px solid #e2e6ee; }
      #gd .doc { width: 56px; height: 72px; border-radius: 8px; background: #4285f4; position: relative; flex: none; }
      #gd .doc::after { content: ""; position: absolute; left: 12px; right: 12px; top: 22px; height: 30px; background: repeating-linear-gradient(0deg, #fff 0 5px, transparent 5px 11px); }
      #gd .nm { font-family: 'Work Sans'; font-weight: 400; font-size: 36px; color: #202124; }
      #gd .tools { height: 64px; background: #eef2f9; margin: 18px 30px; border-radius: 32px; }
      #gd .page { position: absolute; left: 90px; right: 90px; top: 230px; bottom: 0; background: #fff; box-shadow: 0 0 0 3px #e2e6ee; padding: 60px 56px; }
      #gq { font-family: 'Work Sans'; font-weight: 700; font-size: 54px; line-height: 1.2; color: #202124; min-height: 140px; }
      #gq span { display: none; }
      #gq .cur { display: inline-block; width: 4px; height: 56px; background: #1a73e8; vertical-align: -8px; margin-left: 4px; }
      .ga { position: relative; font-family: 'Work Sans'; font-weight: 400; font-size: 46px; line-height: 1.3; color: #3c4043; margin-top: 30px; }
      .ga b { position: absolute; left: -8px; right: -8px; top: 4px; bottom: 0; background: #ffe98a; border-radius: 10px; transform-origin: left center; transform: scaleX(0); z-index: 0; font-weight: 400; }
      .ga span { position: relative; z-index: 1; }
      #rec { left: 700px; top: 380px; font-size: 44px; background: #e0161a; z-index: 8; display: flex; align-items: center; gap: 14px; padding: 14px 30px 4px; }
      #rec i { width: 26px; height: 26px; border-radius: 50%; background: #fff; margin-top: -8px; }

      /* F. une cliente */
      .mt { top: 250px; width: 250px; height: 250px; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 8px; }
      .mt svg { width: 120px; height: 120px; }
      .mt .n { font-size: 48px; line-height: 1; }
      #mt1 { left: 80px; } #mt2 { left: 415px; } #mt3 { left: 750px; }
      #arrs { left: 0; top: 520px; width: 1080px; height: 300px; }
      #cli { left: 390px; top: 810px; width: 300px; height: 300px; background: #fff3e6; }
      #cli .w { width: 190px; height: 210px; }
      #cliH { left: 640px; top: 800px; width: 110px; height: 100px; z-index: 6; }
      #cliH svg { width: 100%; height: 100%; }
      #cliL { left: 350px; top: 1170px; font-size: 64px; }

      /* G. Grâce */
      #cal { left: 70px; top: 230px; width: 320px; height: 330px; overflow: hidden; padding: 0; text-align: center; }
      #cal .h { background: #e0161a; color: #fff; font-size: 52px; padding: 22px 0 8px; border-bottom: 5px solid #111; }
      #cal .b { font-size: 150px; line-height: 1; padding-top: 30px; }
      #desk { left: 430px; top: 230px; width: 580px; height: 430px; padding: 16px; }
      #desk .vc { width: 100%; height: 100%; border-radius: 22px; overflow: hidden; }
      #grT { left: 480px; top: 610px; font-size: 56px; z-index: 6; }
      #pl { left: 350px; top: 740px; }
      #pl .scr { background: linear-gradient(#fff6ec, #fff); padding: 60px 26px 0; }
      #pl .lt { font-size: 34px; line-height: 1.05; }
      #pl .ls { font-family: 'Work Sans'; font-weight: 700; font-size: 20px; color: #b83c00; letter-spacing: .08em; margin-top: 6px; }
      #pl .pb { margin: 40px auto 0; width: 150px; height: 150px; border-radius: 50%; background: #ff5c00; border: 5px solid #111; display: flex; align-items: center; justify-content: center; }
      #pl .pb svg { width: 70px; height: 70px; margin-left: 8px; }
      #pl .bar { margin-top: 44px; height: 14px; border-radius: 7px; background: #eadfd2; overflow: hidden; }
      #pl .bar i { display: block; height: 100%; width: 100%; background: #ff5c00; transform-origin: left center; transform: scaleX(0); }
      #cnt { left: 740px; top: 820px; width: 250px; height: 250px; }
      #cnt svg { position: absolute; left: 25px; top: 25px; width: 190px; height: 190px; }
      #cnt .xn { position: absolute; left: 0; top: 0; width: 240px; height: 240px; display: flex; align-items: center; justify-content: center; font-size: 76px; padding-top: 10px; }
      #wa { left: 70px; top: 230px; width: 940px; height: 720px; overflow: hidden; padding: 0; background: #efeae2; }
      #wa .hd { height: 140px; background: #075e54; display: flex; align-items: center; gap: 26px; padding: 0 34px; color: #fff; }
      #wa .av { width: 92px; height: 92px; border-radius: 50%; background: #ffd60a; color: #111; border: 4px solid #fff; display: flex; align-items: center; justify-content: center; font-size: 56px; padding-top: 8px; }
      #wa .nm { font-size: 52px; line-height: 1; }
      #wa .st { font-family: 'Work Sans'; font-weight: 400; font-size: 26px; opacity: .85; }
      #typ { left: 40px; top: 190px; width: 190px; height: 100px; border-radius: 30px 30px 30px 6px; background: #fff; display: flex; align-items: center; justify-content: center; gap: 14px; }
      #typ i { width: 22px; height: 22px; border-radius: 50%; background: #9aa6c2; }
      #msg { left: 40px; top: 190px; width: 760px; border-radius: 36px 36px 36px 8px; background: #fff; font-family: 'Work Sans'; font-weight: 700; font-size: 60px; line-height: 1.18; padding: 30px 40px; box-shadow: 0 6px 0 rgba(0,0,0,0.12); }
      #msg .tm { display: block; text-align: right; font-weight: 400; font-size: 24px; color: #8a8f98; margin-top: 6px; }
      #sale { left: 290px; top: 1020px; font-size: 68px; }
      #cartB { left: 80px; top: 990px; width: 170px; height: 170px; background: #ff5c00; }
      .coin { width: 100px; height: 100px; border-radius: 50%; background: #ffd60a; border: 5px solid #111; font-size: 60px; display: flex; align-items: center; justify-content: center; padding-top: 8px; z-index: 7; }
      #co1 { left: 860px; top: 980px; } #co2 { left: 900px; top: 1130px; }

      /* H. CTA */
      #cbLab { top: 210px; font-size: 104px; line-height: 1; }
      #o1 { left: 130px; top: 380px; background: #ffd60a; } #o2 { left: 430px; top: 380px; background: #ff5c00; color: #fff; } #o3 { left: 730px; top: 380px; background: #1faa59; color: #fff; }
      .on { width: 200px; height: 200px; font-size: 130px; }
      #cbox { left: 70px; top: 680px; width: 940px; height: 170px; display: flex; align-items: center; gap: 26px; padding: 0 30px; }
      #cbox .av { width: 100px; height: 100px; border-radius: 50%; background: #ffd60a; border: 5px solid #111; flex: none; }
      #cbox .in { flex: 1; height: 100px; border-radius: 50px; background: #f1ede6; display: flex; align-items: center; padding: 8px 34px 0; font-size: 60px; white-space: pre; overflow: hidden; }
      #cbox .in span { opacity: 0; }
      #cbox .send { width: 100px; height: 100px; border-radius: 50%; background: #ff5c00; border: 5px solid #111; flex: none; display: flex; align-items: center; justify-content: center; }
      #cbox .send svg { width: 50px; height: 50px; }
      #dm { left: 130px; top: 920px; width: 820px; height: 190px; display: flex; align-items: center; gap: 26px; padding: 0 30px; }
      .dmav { width: 120px; height: 120px; border-radius: 50%; flex: none; background: #fff; border: 4px solid #111; overflow: hidden; display: flex; align-items: center; justify-content: center; }
      .dmav img { width: 86%; height: 86%; object-fit: contain; }
      #dm .b { flex: 1; height: 110px; border-radius: 30px 30px 30px 8px; background: #eef2fb; display: flex; align-items: center; gap: 16px; padding: 0 30px; }
      #dm .b i { width: 26px; height: 26px; border-radius: 50%; background: #9aa6c2; }
      #rocket { left: 450px; top: 1150px; width: 180px; height: 240px; z-index: 9; }
      #rocket svg { width: 100%; height: 100%; }
      #sub { left: 140px; top: 460px; width: 800px; height: 480px; display: flex; align-items: center; justify-content: center; }
      .sublogo { width: 660px; height: auto; }

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

      <!-- A. HOOK : ce matin / ce soir -->
      <div class="ab pill y" id="sunTag"><svg viewBox="0 0 100 100"><circle cx="50" cy="50" r="22" fill="#ff5c00" stroke="#111" stroke-width="6"/><g stroke="#111" stroke-width="8" stroke-linecap="round"><path d="M50 6V16M50 84V94M6 50H16M84 50H94M19 19L26 26M74 74L81 81M81 19L74 26M26 74L19 81"/></g></svg>Ce matin</div>
      <div class="ab ph" id="p1"><div class="sc">
        <video id="vH1" class="clip" src="assets/video/hook1.mp4" data-start="__S_H1__" data-duration="__D_H1__" data-track-index="1" muted playsinline></video>
      </div></div>
      <div class="ab ph" id="p2"><div class="sc">
        <video id="vH2" class="clip" src="assets/video/hook2.mp4" data-start="__S_H2__" data-duration="__D_H2__" data-track-index="2" muted playsinline></video>
      </div></div>
      <div class="ab ph" id="pv"><div class="sc">
        <video id="vVis" class="clip" src="assets/video/visage.mp4" data-start="__S_VIS__" data-duration="__D_VIS__" data-track-index="3" muted playsinline></video>
      </div></div>
      <div class="ab nf" id="nf0">__NOFACE__</div>
      <div class="ab card" id="night"><svg viewBox="0 0 100 100"><path d="M64 10 A42 42 0 1 0 90 64 A34 34 0 1 1 64 10 Z" fill="#ffd60a"/></svg><div class="t">CE SOIR</div>
        <div class="row"><div id="n1">1</div><div id="n2">2</div><div id="n3">3</div></div></div>

      <!-- B. PROMESSE -->
      <div class="ab card" id="hello">Hello !</div>
      <div class="ab ico" id="cam"><svg viewBox="0 0 100 100"><rect x="8" y="28" width="62" height="48" rx="10" fill="#fff" stroke="#111" stroke-width="6"/><path d="M70 44 L92 32 V72 L70 60 Z" fill="#fff" stroke="#111" stroke-width="6" stroke-linejoin="round"/><circle cx="39" cy="52" r="12" fill="#111"/></svg><div class="x"></div></div>
      <div class="ab" id="nfB">__NOFACE__</div>
      <div class="ab num tn" id="t1">1</div>
      <div class="ab num tn" id="t2">2</div>
      <div class="ab num tn" id="t3">3</div>
      <div class="ab" id="bigPh"><div class="scr"></div></div>

      <!-- C. COMPTES SANS VISAGE -->
      <div class="ab ph" id="q1"><div class="sc">
        <video id="vQ1" class="clip" src="assets/video/visage.mp4" data-start="__S_Q1__" data-duration="__D_Q1__" data-track-index="4" muted playsinline></video>
      </div></div>
      <div class="ab ph" id="q2"><div class="sc">
        <video id="vQ2" class="clip" src="assets/video/capcut.mp4" data-start="__S_Q2__" data-duration="__D_Q2__" data-track-index="5" muted playsinline></video>
      </div></div>
      <div class="ab ph" id="q3"><div class="sc">
        <video id="vQ3" class="clip" src="assets/video/tableau.mp4" data-start="__S_Q3__" data-duration="__D_Q3__" data-track-index="6" muted playsinline></video>
      </div></div>
      <div class="ab nf" id="nq1">__NOFACE__</div>
      <div class="ab nf" id="nq2">__NOFACE__</div>
      <div class="ab nf" id="nq3">__NOFACE__</div>
      <div class="ab pill k" id="never">Zéro visage</div>

      <!-- D. TOI AUSSI -->
      <div class="ab card" id="ils">
        <div class="m">__MAN__<div class="ok"></div></div><div class="m">__MAN__<div class="ok"></div></div><div class="m">__MAN__<div class="ok"></div></div>
      </div>
      <div class="ab" id="eq">=</div>
      <div class="ab card" id="you"><div class="m">__MAN__</div></div>
      <div class="ab pill y" id="toi">Toi aussi</div>
      <svg class="ab" id="arrow" viewBox="0 0 70 100"><path d="M35 6 V74 M10 52 L35 86 L60 52" fill="none" stroke="#111" stroke-width="12" stroke-linecap="round" stroke-linejoin="round"/></svg>

      <!-- E1. FORMAT 1 : main + feuille -->
      <div class="ab fh" id="fh1"><div class="num" style="background:#ffd60a">1</div><div class="pill k">Main + feuille</div></div>
      <div class="ab card" id="vT"><div class="vc"><video id="vTab" class="clip" src="assets/video/tableau.mp4" data-start="__S_TAB__" data-duration="__D_TAB__" data-track-index="7" muted playsinline></video></div></div>
      <div class="ab ico" id="icp"><svg viewBox="0 0 100 100"><path d="M22 8 H64 L80 24 V92 H22 Z" fill="#fff" stroke="#111" stroke-width="6" stroke-linejoin="round"/><path d="M34 40 H68 M34 56 H68 M34 72 H58" stroke="#9aa6c2" stroke-width="6" stroke-linecap="round"/></svg></div>
      <div class="ab ico" id="icm"><svg viewBox="0 0 100 100"><g transform="rotate(40 50 50)"><rect x="38" y="4" width="24" height="64" rx="6" fill="#e0161a" stroke="#111" stroke-width="6"/><path d="M38 68 H62 L56 86 H44 Z" fill="#fff" stroke="#111" stroke-width="6" stroke-linejoin="round"/><path d="M46 86 L50 96 L54 86" fill="#111"/></g></svg></div>
      <svg class="ab" id="recPh" viewBox="0 0 60 92"><rect x="4" y="4" width="52" height="84" rx="10" fill="#111"/><rect x="10" y="12" width="40" height="64" rx="4" fill="#2b2f63"/><circle cx="30" cy="44" r="9" fill="#e0161a"/></svg>
      <div class="ab card paper" id="paperC"><div class="hand" id="hw1">I'm ready !</div><div class="hand" id="hw2">Je suis prête !</div></div>

      <!-- E2. FORMAT 2 : texte animé -->
      <div class="ab fh" id="fh2"><div class="num" style="background:#ff5c00;color:#fff">2</div><div class="pill k">Texte animé</div></div>
      <div class="ab ph big" id="pc"><div class="sc">
        <video id="vCap" class="clip" src="assets/video/capcut.mp4" data-start="__S_CAP__" data-duration="__D_CAP__" data-track-index="8" muted playsinline></video>
        <div class="chip" data-layout-allow-overlap data-layout-allow-occlusion>CapCut</div>
      </div></div>
      <div class="ab card" id="kin"><span id="k1" style="color:#ffd60a">Tell</span><span id="k2" style="color:#fff">me</span><span id="k3" style="color:#ff8a3d">about</span><span id="k4" style="color:#7ee0a1">yourself?</span></div>
      <div class="ab card" id="voice"><div class="mic"><svg viewBox="0 0 100 100"><rect x="34" y="8" width="32" height="54" rx="16" fill="#fff" stroke="#111" stroke-width="6"/><path d="M20 46 C20 64 34 74 50 74 C66 74 80 64 80 46 M50 74 V92 M34 92 H66" fill="none" stroke="#111" stroke-width="6" stroke-linecap="round"/></svg></div><div id="wave">__BARS__</div></div>

      <!-- E3. FORMAT 3 : écran -->
      <div class="ab fh" id="fh3"><div class="num" style="background:#1faa59;color:#fff">3</div><div class="pill k">Ton écran</div></div>
      <div class="ab card" id="gd">
        <div class="top"><div class="doc"></div><div class="nm">Entretien en anglais</div></div>
        <div class="tools"></div>
        <div class="page">
          <div id="gq">__GQ__<i class="cur" id="gcur"></i></div>
          <div class="ga" id="ga1"><b id="gh1"></b><span>I'm a hard worker.</span></div>
          <div class="ga" id="ga2"><b id="gh2"></b><span>I learn fast and I love teamwork.</span></div>
        </div>
      </div>
      <div class="ab pill" id="rec"><i id="recDot"></i>REC</div>

      <!-- F. UNE CLIENTE -->
      <div class="ab card mt" id="mt1"><svg viewBox="0 0 100 100"><path d="M18 14 H72 L84 26 V88 H18 Z" fill="#fff" stroke="#111" stroke-width="6" stroke-linejoin="round"/><path d="M30 44 C38 36 44 52 52 44 S66 38 72 46" fill="none" stroke="#1a2a6c" stroke-width="6" stroke-linecap="round"/><g transform="rotate(35 70 66)"><rect x="64" y="40" width="14" height="44" rx="4" fill="#e0161a" stroke="#111" stroke-width="5"/></g></svg><div class="n">1</div></div>
      <div class="ab card mt" id="mt2"><svg viewBox="0 0 100 100"><rect x="14" y="8" width="72" height="84" rx="14" fill="#15183a" stroke="#111" stroke-width="6"/><text x="50" y="62" text-anchor="middle" font-family="Baloo 2" font-weight="800" font-size="40" fill="#ffd60a">Aa</text></svg><div class="n">2</div></div>
      <div class="ab card mt" id="mt3"><svg viewBox="0 0 100 100"><rect x="8" y="14" width="84" height="58" rx="8" fill="#fff" stroke="#111" stroke-width="6"/><path d="M20 32 H70 M20 46 H58" stroke="#4285f4" stroke-width="7" stroke-linecap="round"/><path d="M36 88 H64 M50 72 V88" stroke="#111" stroke-width="6" stroke-linecap="round"/></svg><div class="n">3</div></div>
      <svg class="ab" id="arrs" viewBox="0 0 1080 300"><g fill="none" stroke="#111" stroke-width="10" stroke-linecap="round" stroke-linejoin="round">
        <path id="a1" d="M205 10 C220 170 380 230 470 280"/><path id="a2" d="M540 10 V280"/><path id="a3" d="M875 10 C860 170 700 230 610 280"/></g></svg>
      <div class="ab ico" id="cli"><svg class="w" viewBox="0 0 100 110"><circle cx="50" cy="16" r="12" fill="#1d1410"/><circle cx="50" cy="38" r="21" fill="#86502f"/><path d="M29 36 C30 20 42 14 52 15 C64 16 72 24 71 38 C64 28 52 26 42 28 C36 30 32 32 29 36 Z" fill="#1d1410"/><path d="M14 110 C14 76 30 64 50 64 C70 64 86 76 86 110 Z" fill="#ff5c00"/></svg></div>
      <div class="ab" id="cliH">__HEART__</div>
      <div class="ab pill y" id="cliL">Une cliente</div>

      <!-- G. GRÂCE -->
      <div class="ab card" id="cal"><div class="h">DEMAIN</div><div class="b">J-1</div></div>
      <div class="ab card" id="desk"><div class="vc"><video id="vInt" class="clip" src="assets/video/entretien.mp4" data-start="__S_INT__" data-duration="__D_INT__" data-track-index="9" muted playsinline></video></div></div>
      <div class="ab pill k" id="grT">Grâce</div>
      <div class="ab ph" id="pl"><div class="sc scr">
        <div class="lt">Tell me about yourself</div><div class="ls">LEÇON · ENTRETIEN</div>
        <div class="pb">__PLAY__</div>
        <div class="bar"><i id="plBar"></i></div>
      </div></div>
      <div class="ab ico" id="cnt"><svg viewBox="0 0 100 100"><path d="M78 50 A28 28 0 1 1 64 26" fill="none" stroke="#ff5c00" stroke-width="8" stroke-linecap="round"/><path d="M58 14 L70 26 L56 36" fill="none" stroke="#ff5c00" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/></svg>
        <div class="xn" id="x1">x1</div><div class="xn" id="x2">x2</div><div class="xn" id="x3">x3</div></div>
      <div class="ab card" id="wa">
        <div class="hd"><div class="av">G</div><div><div class="nm">Grâce</div><div class="st">en ligne</div></div></div>
        <div class="ab" id="typ"><i id="y1"></i><i id="y2"></i><i id="y3"></i></div>
        <div class="ab" id="msg">Tu as d'autres questions comme ça ?<span class="tm">21:04 ✓✓</span></div>
      </div>
      <div class="ab ico" id="cartB">__CART__</div>
      <div class="ab pill g" id="sale">Première vente</div>
      <div class="ab coin" id="co1">$</div>
      <div class="ab coin" id="co2">$</div>

      <!-- H. CTA -->
      <div class="ab center" id="cbLab">Ton format ?</div>
      <div class="ab num on" id="o1">1</div>
      <div class="ab num on" id="o2">2</div>
      <div class="ab num on" id="o3">3</div>
      <div class="ab card" id="cbox"><div class="av"></div><div class="in">__TYPED__</div>
        <div class="send"><svg viewBox="0 0 24 24" fill="#fff"><path d="M3 20.5 21 12 3 3.5l3 8.5-3 8.5Zm3-8.5h9"/></svg></div></div>
      <div class="ab card" id="dm"><div class="dmav"><img src="assets/img/logo_dm_icone.png" /></div><div class="b"><i id="d1"></i><i id="d2"></i><i id="d3"></i></div></div>
      <div class="ab" id="rocket"><svg viewBox="0 0 100 130"><path d="M50 4 C74 24 80 58 72 90 H28 C20 58 26 24 50 4 Z" fill="#fff" stroke="#111" stroke-width="6" stroke-linejoin="round"/><circle cx="50" cy="48" r="12" fill="#1c5bd6" stroke="#111" stroke-width="5"/><path d="M28 70 L10 94 L30 90 Z M72 70 L90 94 L70 90 Z" fill="#ff5c00" stroke="#111" stroke-width="5" stroke-linejoin="round"/><path d="M38 94 C40 108 50 124 50 124 C50 124 60 108 62 94 Z" fill="#ffd60a" stroke="#111" stroke-width="5" stroke-linejoin="round"/></svg></div>
      <div class="ab card" id="sub"><img class="sublogo" src="assets/img/logo_dm.png" /></div>

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
      const DUR = __DUR__;
      const tl = gsap.timeline({ paused: true });
      const IN = (sel, from, to, at) => tl.fromTo(sel, { ...from, autoAlpha: 0 }, { ...to, autoAlpha: 1, immediateRender: false }, at);
      const OUT = (sel, to, at) => tl.to(sel, to, at);
      const HIDE = ["#sunTag","#p1","#p2","#pv","#nf0","#night","#n1","#n2","#n3","#hello","#cam","#nfB","#t1","#t2","#t3","#bigPh",
        "#q1","#q2","#q3","#nq1","#nq2","#nq3","#never","#ils","#eq","#you","#toi","#arrow",
        "#fh1","#vT","#icp","#icm","#recPh","#paperC","#fh2","#pc","#kin","#k1","#k2","#k3","#k4","#voice","#fh3","#gd","#ga1","#ga2","#rec",
        "#mt1","#mt2","#mt3","#arrs","#cli","#cliH","#cliL","#cal","#desk","#grT","#pl","#cnt","#x1","#x2","#x3","#wa","#typ","#msg","#cartB","#sale","#co1","#co2",
        "#cbLab","#o1","#o2","#o3","#cbox","#dm","#rocket","#sub","#s1x","#s2x","#s3x","#s4x","#flash"];
      gsap.set(HIDE, { autoAlpha: 0 });
      gsap.set(["#cam .x", "#ils .ok"], { autoAlpha: 0 });
      tl.fromTo("#progress", { scaleX: 0 }, { scaleX: 1, duration: DUR, ease: "none" }, 0);
      const flash = (at) => { tl.set("#flash", { autoAlpha: 0.85 }, at); tl.to("#flash", { autoAlpha: 0, duration: 0.22 }, at + 0.04); };
      let lastSparks = 0;
      const SP = ["#s1x","#s2x","#s3x","#s4x"];
      const sparks = (at) => { lastSparks = at; SP.forEach((s, i) => IN(s, { scale: 0, rotation: -90 }, { scale: 1, rotation: 0, duration: 0.35, ease: "back.out(2.5)" }, at + i * 0.1)); };
      const sparksOut = (at) => OUT(SP, { scale: 0, autoAlpha: 0, duration: 0.2 }, Math.max(at, lastSparks + 0.7));
      const pop = (sel, at, rot = 0) => IN(sel, { scale: 0, rotation: rot + 12 }, { scale: 1, rotation: rot, duration: 0.4, ease: "back.out(2.2)" }, at);
      const slam = (sel, at) => IN(sel, { scale: 2.4 }, { scale: 1, duration: 0.3, ease: "power4.in" }, at);
      const rise = (sel, at, rot = 0) => IN(sel, { y: 900, rotation: rot + 8 }, { y: 0, rotation: rot, duration: 0.5, ease: "back.out(1.3)" }, at);
      const leave = (sels, at) => OUT(sels, { autoAlpha: 0, y: -80, duration: 0.3, ease: "power2.in" }, at);
      const reveal = (sel, at, dur) => tl.fromTo(sel, { width: 0 }, { width: 800, duration: dur, ease: "none", immediateRender: false }, at);

      // ---------- A. HOOK : ce matin → ce soir ----------
      pop("#sunTag", 0.05, -2);
      rise("#p1", 0.1, -6);
      rise("#p2", T.jeunes - 0.4, 6);
      IN("#pv", { y: 900, scale: 1.1 }, { y: 0, scale: 1.1, duration: 0.45, ease: "back.out(1.3)" }, T.visage - 0.9);
      tl.to(["#p1", "#p2"], { scale: 0.9, filter: "brightness(0.8)", duration: 0.4 }, T.visage - 0.9);
      pop("#nf0", T.visage - 0.1, 0);
      OUT("#p1", { x: -700, rotation: -30, autoAlpha: 0, duration: 0.4, ease: "power3.in" }, T.soir - 0.35);
      OUT("#p2", { x: 700, rotation: 30, autoAlpha: 0, duration: 0.4, ease: "power3.in" }, T.soir - 0.35);
      leave(["#pv", "#nf0", "#sunTag"], T.soir - 0.35);
      rise("#night", T.soir - 0.1, -1);
      ["#n1", "#n2", "#n3"].forEach((n, i) => pop(n, T.comment + i * 0.2, 0));
      leave(["#night", "#n1", "#n2", "#n3"], T.veux - 0.35);

      // ---------- B. PROMESSE ----------
      pop("#hello", T.veux - 0.15, -3);
      tl.to("#hello", { scale: 1.07, duration: 0.18, yoyo: true, repeat: 1 }, T.lecons);
      pop("#cam", T.camera - 0.25, -6);
      IN("#cam .x", { scaleX: 0 }, { scaleX: 1, duration: 0.2, ease: "power3.out" }, T.camera + 0.1);
      pop("#nfB", T.visage2 - 0.3, 6);
      leave(["#hello", "#cam", "#nfB"], T.trois - 0.4);
      [["#t1", -8], ["#t2", 0], ["#t3", 8]].forEach(([n, r], i) => pop(n, T.trois - 0.1 + i * 0.2, r));
      rise("#bigPh", T.telephone - 0.35);
      [["#t1", 470 - 200], ["#t2", 540 - 540], ["#t3", 610 - 880]].forEach(([n, dx]) =>
        tl.to(n, { x: dx, y: 480, scale: 0.36, rotation: 0, duration: 0.45, ease: "power3.inOut" }, T.telephone + 0.1));
      sparks(T.telephone + 0.2);
      sparksOut(T.regarde - 0.4);
      leave(["#t1", "#t2", "#t3", "#bigPh"], T.regarde - 0.4);

      // ---------- C. COMPTES SANS VISAGE ----------
      rise("#q1", T.regarde - 0.3, -6);
      rise("#q2", T.regarde - 0.15, 0);
      rise("#q3", T.regarde, 6);
      ["#nq1", "#nq2", "#nq3"].forEach((n, i) => pop(n, T.visage3 - 0.2 + i * 0.15, 0));
      slam("#never", T.jamais - 0.1);
      tl.to(["#q1", "#q2", "#q3"], { x: -8, duration: 0.05, yoyo: true, repeat: 5, ease: "none" }, T.jamais + 0.15);
      leave(["#q1", "#q2", "#q3", "#nq1", "#nq2", "#nq3", "#never"], T.sils - 0.35);

      // ---------- D. TOI AUSSI ----------
      IN("#ils", { x: -600 }, { x: 0, duration: 0.4, ease: "back.out(1.4)" }, T.sils - 0.2);
      IN("#ils .ok", { scale: 0 }, { scale: 1, duration: 0.25, ease: "back.out(3)", stagger: 0.1 }, T.sils + 0.3);
      pop("#eq", T.peux - 0.5, 0);
      IN("#you", { x: 600 }, { x: 0, duration: 0.4, ease: "back.out(1.4)" }, T.peux - 0.35);
      pop("#toi", T.peux, -3);
      sparks(T.peux);
      IN("#arrow", { y: -60 }, { y: 0, duration: 0.3, ease: "back.out(2)" }, T.regarde2 - 0.1);
      tl.to("#arrow", { y: 30, duration: 0.2, yoyo: true, repeat: 3, ease: "sine.inOut" }, T.regarde2 + 0.25);
      sparksOut(T.un - 0.45);
      leave(["#ils", "#eq", "#you", "#toi", "#arrow"], T.un - 0.45);

      // ---------- E1. FORMAT 1 ----------
      flash(T.un - 0.2);
      IN("#fh1", { x: -700 }, { x: 0, duration: 0.35, ease: "back.out(1.6)" }, T.un - 0.2);
      rise("#vT", T.un, -1);
      pop("#icp", T.feuille - 0.2, -8);
      pop("#icm", T.feutre - 0.2, 8);
      OUT(["#icp", "#icm"], { scale: 0, autoAlpha: 0, duration: 0.25 }, T.filme - 0.3);
      pop("#recPh", T.filme - 0.15, 8);
      tl.to("#recPh circle", { autoAlpha: 0.2, duration: 0.2, yoyo: true, repeat: 5 }, T.filme + 0.3);
      IN("#paperC", { y: 500 }, { y: 0, duration: 0.4, ease: "back.out(1.3)" }, T.main - 0.3);
      tl.set(["#hw1", "#hw2"], { autoAlpha: 1 }, 0);
      reveal("#hw1", T.ecrit, T.traduction - T.ecrit - 0.2);
      reveal("#hw2", T.traduction, 0.9);
      leave(["#fh1", "#vT", "#recPh", "#paperC"], T.deux - 0.35);

      // ---------- E2. FORMAT 2 ----------
      flash(T.deux - 0.15);
      IN("#fh2", { x: -700 }, { x: 0, duration: 0.35, ease: "back.out(1.6)" }, T.deux - 0.15);
      rise("#pc", T.deux + 0.05, -3);
      IN("#kin", { x: 600 }, { x: 0, duration: 0.4, ease: "back.out(1.4)" }, T.anime - 0.3);
      [["#k1", T.mots - 0.1], ["#k2", T.unpar - 0.1], ["#k3", T.unpar + 0.25], ["#k4", T.unpar + 0.6]].forEach(([k, at]) =>
        IN(k, { scale: 0.2, x: -60 }, { scale: 1, x: 0, duration: 0.25, ease: "back.out(2.5)" }, at));
      IN("#voice", { y: 400 }, { y: 0, duration: 0.4, ease: "back.out(1.4)" }, T.voix - 0.35);
      document.querySelectorAll("#wave i").forEach((b, i) =>
        tl.fromTo(b, { height: "25%" }, { height: (45 + ((i * 37) % 50)) + "%", duration: 0.2, yoyo: true, repeat: 7, ease: "sine.inOut", immediateRender: false }, T.voix + (i % 4) * 0.05));
      leave(["#fh2", "#pc", "#kin", "#voice"], T.troisF - 0.35);

      // ---------- E3. FORMAT 3 ----------
      flash(T.troisF - 0.15);
      IN("#fh3", { x: -700 }, { x: 0, duration: 0.35, ease: "back.out(1.6)" }, T.troisF - 0.15);
      rise("#gd", T.ecran - 0.3, 0);
      const gq = document.querySelectorAll("#gq span");
      const tEnd = T.docs + 0.3;
      gq.forEach((s, i) => tl.set(s, { display: "inline" }, T.tapes + (tEnd - T.tapes) * i / gq.length));
      pop("#rec", T.enregistres - 0.1, 3);
      tl.to("#recDot", { autoAlpha: 0.15, duration: 0.25, yoyo: true, repeat: 5 }, T.enregistres + 0.3);
      IN("#ga1", { y: 30 }, { y: 0, duration: 0.25 }, T.lis - 0.3);
      IN("#ga2", { y: 30 }, { y: 0, duration: 0.25 }, T.lis - 0.1);
      tl.fromTo("#gh1", { scaleX: 0 }, { immediateRender: false, scaleX: 1, duration: 0.5, ease: "none" }, T.lis);
      tl.fromTo("#gh2", { scaleX: 0 }, { immediateRender: false, scaleX: 1, duration: 0.7, ease: "none" }, T.reponse);
      leave(["#fh3", "#gd", "#rec"], T.chacune - 0.35);

      // ---------- F. UNE CLIENTE ----------
      ["#mt1", "#mt2", "#mt3"].forEach((m, i) => pop(m, T.chacune - 0.15 + i * 0.15, [-4, 0, 4][i]));
      tl.set("#arrs", { autoAlpha: 1 }, T.amener - 0.3);
      ["#a1", "#a2", "#a3"].forEach((a) => {
        const L = document.querySelector(a).getTotalLength();
        gsap.set(a, { strokeDasharray: L, strokeDashoffset: L });
        tl.fromTo(a, { strokeDashoffset: L }, { strokeDashoffset: 0, duration: 0.45, ease: "power2.out", immediateRender: false }, T.amener - 0.3);
      });
      pop("#cli", T.cliente - 0.35, 0);
      pop("#cliH", T.cliente, 10);
      pop("#cliL", T.cliente + 0.1, -2);
      sparks(T.cliente);
      sparksOut(T.veille - 0.4);
      leave(["#mt1", "#mt2", "#mt3", "#arrs", "#cli", "#cliH", "#cliL"], T.veille - 0.4);

      // ---------- G. GRÂCE ----------
      pop("#cal", T.veille - 0.2, -4);
      IN("#desk", { x: 700 }, { x: 0, duration: 0.45, ease: "back.out(1.3)" }, T.entretien - 0.3);
      pop("#grT", T.grace - 0.15, -3);
      IN("#pl", { y: 900 }, { y: 0, duration: 0.45, ease: "back.out(1.3)" }, T.tombe - 0.1);
      tl.fromTo("#plBar", { scaleX: 0 }, { scaleX: 1, duration: 0.55, ease: "none", immediateRender: false }, T.ecoute - 0.1);
      tl.fromTo("#plBar", { scaleX: 0 }, { scaleX: 1, duration: 0.55, ease: "none", immediateRender: false }, T.ecoute + 0.5);
      tl.fromTo("#plBar", { scaleX: 0 }, { scaleX: 1, duration: 0.55, ease: "none", immediateRender: false }, T.ecoute + 1.1);
      pop("#cnt", T.ecoute - 0.2, 0);
      tl.fromTo("#cnt svg", { rotation: 0 }, { rotation: 720, duration: 1.8, ease: "none", immediateRender: false }, T.ecoute - 0.1);
      tl.set("#x1", { autoAlpha: 1 }, T.ecoute - 0.1);
      tl.set("#x1", { autoAlpha: 0 }, T.ecoute + 0.5);
      tl.set("#x2", { autoAlpha: 1 }, T.ecoute + 0.5);
      tl.set("#x2", { autoAlpha: 0 }, T.ecoute + 1.1);
      tl.set("#x3", { autoAlpha: 1 }, T.ecoute + 1.1);
      tl.to("#cnt", { scale: 1.2, duration: 0.15, yoyo: true, repeat: 1 }, T.ecoute + 1.1);
      leave(["#cal", "#desk", "#grT", "#pl", "#cnt", "#x3"], T.ecrit2 - 0.45);
      rise("#wa", T.ecrit2 - 0.3, 0);
      tl.set("#typ", { autoAlpha: 1 }, T.ecrit2 + 0.1);
      ["#y1", "#y2", "#y3"].forEach((d, i) => tl.fromTo(d, { y: 0 }, { y: -12, duration: 0.2, yoyo: true, repeat: 3, ease: "sine.inOut", immediateRender: false }, T.ecrit2 + 0.1 + i * 0.08));
      tl.set("#typ", { autoAlpha: 0 }, T.autres - 0.45);
      IN("#msg", { scale: 0.5, transformOrigin: "left bottom" }, { scale: 1, duration: 0.3, ease: "back.out(2)" }, T.autres - 0.45);
      tl.to("#msg", { scale: 1.06, duration: 0.2, yoyo: true, repeat: 1 }, T.message);
      IN("#cartB", { x: -300 }, { x: 0, duration: 0.35, ease: "back.out(1.6)" }, T.debut - 0.2);
      slam("#sale", T.vente - 0.3);
      pop("#co1", T.vente, 0);
      pop("#co2", T.vente + 0.15, 0);
      sparks(T.vente);
      sparksOut(T.commente - 0.4);
      leave(["#wa", "#msg", "#cartB", "#sale", "#co1", "#co2"], T.commente - 0.4);

      // ---------- H. CTA ----------
      flash(T.commente - 0.3);
      slam("#cbLab", T.commente - 0.25);
      [["#o1", -6], ["#o2", 0], ["#o3", 6]].forEach(([o, r], i) => pop(o, T.commente + 0.1 + i * 0.15, r));
      IN("#cbox", { y: 300 }, { y: 0, duration: 0.4, ease: "back.out(1.6)" }, T.numero - 0.3);
      document.querySelectorAll("#cbox .in span").forEach((s, i) => tl.set(s, { opacity: 1 }, T.numero + i * 0.08));
      tl.to("#o2", { scale: 1.25, duration: 0.25, ease: "back.out(3)" }, T.numero + 0.6);
      tl.to(["#o1", "#o3"], { scale: 0.8, duration: 0.25 }, T.numero + 0.6);
      tl.to("#cbox .send", { scale: 1.2, duration: 0.2, yoyo: true, repeat: 1 }, T.essayer);
      IN("#dm", { x: -900 }, { x: 0, duration: 0.45, ease: "back.out(1.4)" }, T.prive - 0.35);
      ["#d1", "#d2", "#d3"].forEach((d, i) => tl.fromTo(d, { y: 0 }, { y: -12, duration: 0.2, yoyo: true, repeat: 5, ease: "sine.inOut", immediateRender: false }, T.prive + i * 0.08));
      pop("#rocket", T.aider - 0.1, 0);
      tl.to("#rocket", { y: -1400, duration: 0.7, ease: "power3.in" }, T.lancer + 0.1);
      sparks(T.lancer);
      sparksOut(DUR - 1.35);
      leave(["#cbLab", "#o1", "#o2", "#o3", "#cbox", "#dm"], DUR - 1.35);
      IN("#sub", { scale: 0.6 }, { scale: 1, duration: 0.35, ease: "back.out(2)" }, DUR - 1.1);

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
