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
      .serie { position: absolute; top: 64px; right: 70px; z-index: 40; background: #1d7a46; color: #fff; font-size: 28px; padding: 12px 26px 6px; border-radius: 40px; border: 4px solid #111; }
      .card { background: #fff; border: 5px solid #111; border-radius: 36px; box-shadow: 14px 14px 0 #111; }
      .pill { text-align: center; background: #ff5c00; color: #fff; border-radius: 70px; border: 5px solid #111; box-shadow: 10px 10px 0 #111; white-space: nowrap; padding: 18px 40px 6px; }
      .pill.y { background: #ffd60a; color: #111; }
      .pill.k { background: #111; color: #fff; box-shadow: 10px 10px 0 #ff5c00; }
      .pill.g { background: #1d7a46; color: #fff; }
      .spark { position: absolute; width: 70px; height: 70px; z-index: 15; }
      .spark svg { width: 100%; height: 100%; fill: #111; }
      .center { left: 0; width: 1080px; text-align: center; }
      .ico { display: flex; align-items: center; justify-content: center; border-radius: 50%; border: 6px solid #111; box-shadow: 10px 10px 0 #111; background: #fff; }
      .ico svg { width: 60%; height: 60%; }
      .coin { width: 100px; height: 100px; border-radius: 50%; background: #ffd60a; border: 5px solid #111; font-size: 60px; display: flex; align-items: center; justify-content: center; padding-top: 8px; z-index: 7; }
      video { width: 100%; height: 100%; object-fit: cover; display: block; }
      .vcard { left: 70px; top: 230px; width: 940px; height: 560px; padding: 14px; }
      .vcard .vc { width: 100%; height: 100%; border-radius: 22px; overflow: hidden; }
      .tag { position: absolute; left: 40px; bottom: -40px; font-size: 50px; z-index: 6; }
      .aiic { width: 190px; height: 190px; border-radius: 46px; box-shadow: 10px 10px 0 #111; border: 5px solid #111; overflow: hidden; background: #fff; }
      .aiic img { width: 100%; height: 100%; display: block; }
      .shot { border: 5px solid #111; border-radius: 18px; box-shadow: 12px 12px 0 #111; overflow: hidden; background: #fff; }
      .shot img { width: 100%; display: block; }

      /* A. hook */
      #vHookC { left: 70px; top: 220px; width: 470px; height: 835px; padding: 12px; border-radius: 40px; }
      #vHookC .vc { width: 100%; height: 100%; border-radius: 28px; overflow: hidden; }
      #x1 { left: 580px; top: 250px; width: 440px; }
      #x3 { left: 590px; top: 560px; width: 420px; }
      #x4 { left: 610px; top: 870px; width: 390px; }
      #city { left: 590px; top: 300px; width: 420px; height: 560px; display: flex; flex-direction: column; align-items: center; justify-content: flex-end; padding-bottom: 40px; background: #1c2f6b; }
      #city svg { width: 340px; height: 340px; }
      #city .lb { color: #fff; font-size: 52px; line-height: 1; margin-top: 18px; }
      #co1 { left: 880px; top: 230px; } #co2 { left: 560px; top: 820px; } #co3 { left: 930px; top: 760px; }

      /* B. promesse */
      #tagJ { left: 110px; top: 735px; }
      #rev { left: 470px; top: 735px; font-size: 46px; z-index: 6; }
      #ai1 { left: 165px; top: 920px; } #ai2 { left: 445px; top: 920px; } #ai3 { left: 725px; top: 920px; }

      /* C. partie 1 */
      #xlChip { left: 230px; top: 900px; font-size: 56px; display: flex; align-items: center; gap: 20px; padding: 18px 40px 8px 22px; }
      #xlChip .x { width: 80px; height: 80px; border-radius: 16px; background: #1d7a46; color: #fff; font-size: 56px; display: flex; align-items: center; justify-content: center; padding-top: 8px; border: 4px solid #111; }
      #rien { left: 360px; top: 1060px; font-size: 48px; transform: rotate(-3deg); }
      .dep { top: 900px; width: 160px; height: 190px; display: flex; flex-direction: column; align-items: center; justify-content: center; }
      .dep svg { width: 100px; height: 90px; }
      .dep .n { font-size: 34px; line-height: 1; margin-top: 6px; }
      #dp1 { left: 70px; } #dp2 { left: 260px; } #dp3 { left: 450px; } #dp4 { left: 640px; } #dp5 { left: 830px; }
      #pin { left: 640px; top: 250px; font-size: 50px; display: flex; align-items: center; gap: 12px; padding: 16px 34px 6px 22px; z-index: 6; }
      #pin svg { width: 46px; height: 56px; margin-top: -10px; }
      #cal { left: 90px; top: 880px; width: 330px; height: 340px; overflow: hidden; padding: 0; text-align: center; }
      #cal .h { background: #e0161a; color: #fff; font-size: 40px; line-height: 1.1; padding: 16px 0 4px; border-bottom: 5px solid #111; }
      #cal .b { font-size: 84px; line-height: 1.2; padding-top: 26px; }
      #cal .s { font-size: 40px; line-height: 1.1; margin-top: 16px; }
      .sheet { left: 560px; width: 210px; height: 270px; padding: 26px 24px; }
      .sheet i { display: block; height: 14px; border-radius: 7px; background: #c8cfdd; margin-bottom: 18px; }
      .sheet b { display: block; height: 18px; width: 60%; border-radius: 9px; background: #111; margin-bottom: 24px; }
      #sh1 { top: 900px; } #sh2 { left: 640px; top: 920px; } #sh3 { left: 720px; top: 940px; }
      #rap { left: 430px; top: 1180px; font-size: 48px; transform: rotate(-3deg); z-index: 6; }

      /* D. boucle 1 */
      #expert { left: 170px; top: 900px; font-size: 64px; }
      #arrowJ { left: 470px; top: 1040px; width: 140px; height: 120px; }

      /* E. tableau de bord */
      #db { left: 70px; top: 840px; width: 940px; height: 560px; padding: 30px 40px; }
      #db .ttl { font-size: 46px; line-height: 1.15; }
      #db .sub { font-family: 'Work Sans'; font-weight: 700; font-size: 22px; line-height: 1.2; color: #5f6570; letter-spacing: .08em; margin-top: 10px; }
      #bars { position: absolute; left: 50px; right: 50px; bottom: 70px; height: 300px; display: flex; align-items: flex-end; gap: 44px; border-bottom: 5px solid #111; }
      .bar { flex: 1; height: 100%; position: relative; }
      .bar i { position: absolute; left: 0; right: 0; bottom: 0; height: 100%; border-radius: 14px 14px 0 0; border: 4px solid #111; border-bottom: 0; transform-origin: bottom center; }
      .bar .l { position: absolute; left: 0; right: 0; bottom: -56px; text-align: center; font-size: 34px; }
      #crown { left: 0; top: 0; width: 110px; height: 90px; z-index: 6; }
      #alert { left: 610px; top: 1182px; font-size: 36px; font-size: 40px; background: #e0161a; z-index: 6; padding: 14px 30px 4px; }

      /* E2. IA */
      #fouL { top: 260px; font-size: 96px; line-height: 1; }
      #aiB1 { left: 110px; top: 470px; } #aiB2 { left: 415px; top: 470px; } #aiB3 { left: 720px; top: 470px; }
      #aiB1, #aiB2, #aiB3 { width: 250px; height: 250px; border-radius: 60px; }
      #chat { left: 70px; top: 230px; width: 940px; height: 1150px; padding: 34px; background: #f4f1ec; }
      #chat .hd { display: flex; align-items: center; gap: 18px; font-size: 40px; padding-bottom: 20px; border-bottom: 3px solid #ddd6cc; }
      #chat .hd .aiic { width: 70px; height: 70px; border-radius: 18px; box-shadow: none; border-width: 3px; }
      .bub { position: relative; font-family: 'Work Sans'; font-weight: 700; font-size: 40px; line-height: 1.3; padding: 26px 32px; border-radius: 30px; margin-top: 30px; }
      #ub { margin-left: 120px; background: #ff5c00; color: #fff; border-radius: 30px 30px 8px 30px; min-height: 120px; }
      #ub span { display: none; }
      #ab { margin-right: 60px; background: #fff; border: 4px solid #111; border-radius: 30px 30px 30px 8px; }
      #fx { display: inline-block; font-family: 'Work Sans'; font-weight: 700; font-size: 36px; background: #e8f4ec; color: #1d5c37; border: 3px solid #1d7a46; border-radius: 14px; padding: 10px 18px; margin-top: 16px; }
      #mini { display: flex; align-items: flex-end; gap: 22px; height: 220px; margin-top: 26px; padding: 0 20px; border-bottom: 4px solid #111; }
      #mini i { flex: 1; border-radius: 10px 10px 0 0; border: 3px solid #111; border-bottom: 0; transform-origin: bottom center; }

      /* F. à qui le vendre */
      #qDb { left: 190px; top: 330px; width: 520px; height: 380px; padding: 26px; }
      #qDb .mb { display: flex; align-items: flex-end; gap: 20px; height: 280px; border-bottom: 4px solid #111; }
      #qDb .mb i { flex: 1; border-radius: 10px 10px 0 0; border: 3px solid #111; border-bottom: 0; }
      #qMark { left: 690px; top: 560px; width: 240px; height: 240px; font-size: 170px; background: #ffd60a; padding-top: 30px; }
      #qPill { left: 230px; top: 900px; font-size: 64px; }

      /* G. prospection */
      #srch { left: 70px; top: 230px; width: 940px; height: 700px; padding: 34px; }
      #sbar { display: flex; align-items: center; gap: 18px; height: 100px; border-radius: 50px; border: 4px solid #111; padding: 6px 30px 0; font-family: 'Work Sans'; font-weight: 700; font-size: 38px; background: #f4f1ec; white-space: nowrap; overflow: hidden; }
      #sbar svg { width: 44px; height: 44px; flex: none; margin-top: -6px; }
      #sbar span { display: none; }
      .row { display: flex; align-items: center; gap: 22px; margin-top: 22px; padding: 16px 22px; border-radius: 22px; border: 3px solid #e2ddd4; font-family: 'Work Sans'; font-weight: 700; font-size: 34px; }
      .row .b { width: 66px; height: 66px; border-radius: 16px; background: #1c2f6b; flex: none; display: flex; align-items: center; justify-content: center; }
      .row .b svg { width: 40px; height: 40px; }
      .row small { display: block; font-weight: 400; font-size: 26px; color: #5f6570; }
      #ct { left: 110px; top: 970px; width: 860px; height: 170px; display: flex; align-items: center; gap: 26px; padding: 0 30px; }
      #ct .av { width: 110px; height: 110px; border-radius: 50%; background: #ffd60a; border: 4px solid #111; color: #111; display: flex; align-items: flex-end; justify-content: center; overflow: hidden; flex: none; }
      #ct .av svg { width: 80px; height: 90px; }
      #ct .t { font-size: 44px; line-height: 1.05; }
      #ct .t small { display: block; font-family: 'Work Sans'; font-weight: 700; font-size: 26px; color: #5f6570; }
      #target { left: 840px; top: 950px; width: 150px; height: 150px; z-index: 6; }
      #msgc { left: 70px; top: 970px; width: 940px; height: 400px; padding: 30px; }
      #msgc .bub { margin-top: 0; background: #dcf8c6; border-radius: 30px 30px 8px 30px; min-height: 250px; font-size: 38px; }
      #msgc .bub span { display: none; }
      #sendB { left: 880px; top: 1290px; width: 110px; height: 110px; background: #1d7a46; z-index: 6; }
      #sendB svg { width: 54px; height: 54px; }

      /* H. boucle 3 */
      .mt { width: 200px; height: 160px; padding: 18px; display: flex; align-items: flex-end; gap: 12px; }
      .mt i { flex: 1; border-radius: 6px 6px 0 0; border: 3px solid #111; border-bottom: 0; }
      #mt1 { left: 90px; top: 870px; } #mt2 { left: 330px; top: 900px; } #mt3 { left: 570px; top: 870px; }
      .st { width: 120px; height: 140px; color: #111; z-index: 4; }
      .st svg { width: 100%; height: 100%; }
      #st1 { left: 90px; top: 1130px; } #st2 { left: 270px; top: 1170px; } #st3 { left: 480px; top: 1190px; } #st4 { left: 690px; top: 1170px; } #st5 { left: 870px; top: 1130px; }
      #qb { left: 470px; top: 1060px; width: 140px; height: 110px; font-size: 76px; z-index: 6; display: flex; align-items: center; justify-content: center; padding-top: 10px; }

      /* I. CTA */
      #chk { left: 120px; top: 260px; width: 840px; height: 400px; padding: 40px 50px; display: flex; flex-direction: column; justify-content: center; gap: 34px; }
      .ck { display: flex; align-items: center; gap: 26px; font-size: 60px; line-height: 1; }
      .ck .b { width: 86px; height: 86px; border-radius: 22px; border: 5px solid #111; flex: none; position: relative; background: #fff; }
      .ck .b i { position: absolute; left: 22px; top: 6px; width: 30px; height: 52px; border: solid #1d7a46; border-width: 0 12px 12px 0; transform: rotate(45deg); }
      #rocket { left: 450px; top: 720px; width: 180px; height: 240px; z-index: 9; }
      #rocket svg { width: 100%; height: 100%; }
      #bizPill { left: 220px; top: 990px; font-size: 60px; }
      #cbLab { top: 250px; font-size: 96px; line-height: 1; }
      #cbox { left: 70px; top: 420px; width: 940px; height: 170px; display: flex; align-items: center; gap: 26px; padding: 0 30px; }
      #cbox .av { width: 100px; height: 100px; border-radius: 50%; background: #ffd60a; border: 5px solid #111; flex: none; }
      #cbox .in { flex: 1; height: 100px; border-radius: 50px; background: #f1ede6; display: flex; align-items: center; padding: 8px 34px 0; font-size: 64px; white-space: pre; overflow: hidden; }
      #cbox .in span { opacity: 0; }
      #cbox .send { width: 100px; height: 100px; border-radius: 50%; background: #ff5c00; border: 5px solid #111; flex: none; display: flex; align-items: center; justify-content: center; }
      #cbox .send svg { width: 50px; height: 50px; }
      #dm { left: 130px; top: 660px; width: 820px; height: 190px; display: flex; align-items: center; gap: 26px; padding: 0 30px; }
      .dmav { width: 120px; height: 120px; border-radius: 50%; flex: none; background: #fff; border: 4px solid #111; overflow: hidden; display: flex; align-items: center; justify-content: center; }
      .dmav img { width: 86%; height: 86%; object-fit: contain; }
      #dm .b { flex: 1; height: 110px; border-radius: 30px 30px 30px 8px; background: #eef2fb; display: flex; align-items: center; gap: 16px; padding: 0 30px; }
      #dm .b i { width: 26px; height: 26px; border-radius: 50%; background: #9aa6c2; }
      #g1 { left: 150px; top: 930px; width: 360px; height: 300px; padding: 26px; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 10px; font-size: 40px; text-align: center; line-height: 1; }
      #g2 { left: 570px; top: 930px; width: 360px; height: 300px; padding: 26px; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 10px; font-size: 40px; text-align: center; line-height: 1; }
      #g1 .mb { display: flex; align-items: flex-end; gap: 12px; width: 200px; height: 130px; border-bottom: 4px solid #111; }
      #g1 .mb i { flex: 1; border-radius: 6px 6px 0 0; border: 3px solid #111; border-bottom: 0; }
      #g2 svg { width: 150px; height: 150px; }
      #sub { left: 140px; top: 460px; width: 800px; height: 480px; display: flex; align-items: center; justify-content: center; }
      .sublogo { width: 660px; height: auto; }

      /* sous-titres karaoké */
      #caps { position: absolute; left: 60px; right: 60px; top: 1450px; height: 330px; z-index: 30; }
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
      <div class="serie">EXCEL + IA</div>

      <!-- A. HOOK -->
      <div class="ab card" id="vHookC"><div class="vc"><video id="vHook" class="clip" src="assets/video/hook_excel.mp4" data-start="__S_HOOK__" data-duration="__D_HOOK__" data-track-index="1" muted playsinline></video></div></div>
      <div class="ab shot" id="x1"><img src="assets/img/xl1.png" /></div>
      <div class="ab shot" id="x3"><img src="assets/img/xl3.jpg" /></div>
      <div class="ab shot" id="x4"><img src="assets/img/xl4.jpg" /></div>
      <div class="ab card" id="city"><svg viewBox="0 0 200 200"><g stroke="#111" stroke-width="5" stroke-linejoin="round"><rect x="14" y="70" width="56" height="126" fill="#ffd60a"/><rect x="72" y="20" width="62" height="176" fill="#fff"/><rect x="136" y="96" width="50" height="100" fill="#ff5c00"/></g><g fill="#1c2f6b"><rect x="84" y="36" width="12" height="14"/><rect x="110" y="36" width="12" height="14"/><rect x="84" y="64" width="12" height="14"/><rect x="110" y="64" width="12" height="14"/><rect x="84" y="92" width="12" height="14"/><rect x="110" y="92" width="12" height="14"/><rect x="84" y="120" width="12" height="14"/><rect x="110" y="120" width="12" height="14"/><rect x="28" y="88" width="12" height="14"/><rect x="46" y="88" width="12" height="14"/><rect x="28" y="116" width="12" height="14"/><rect x="46" y="116" width="12" height="14"/></g></svg><div class="lb">Grandes entreprises</div></div>
      <div class="ab coin" id="co1">$</div><div class="ab coin" id="co2">$</div><div class="ab coin" id="co3">$</div>

      <!-- B. PROMESSE -->
      <div class="ab card vcard" id="vcBib"><div class="vc"><video id="vBib" class="clip" src="assets/video/jonathan_biblio.mp4" data-start="__S_BIB__" data-duration="__D_BIB__" data-track-index="2" muted playsinline></video></div></div>
      <div class="ab pill k" id="tagJ" style="font-size:52px">Jonathan</div>
      <div class="ab pill g" id="rev">Savoir-faire → revenu</div>
      <div class="ab aiic" id="ai1"><img src="assets/img/ic_chatgpt.png" /></div>
      <div class="ab aiic" id="ai2"><img src="assets/img/ic_claude.png" /></div>
      <div class="ab aiic" id="ai3"><img src="assets/img/ic_gemini.svg" /></div>

      <!-- C. PARTIE 1 -->
      <div class="ab card vcard" id="vcJon"><div class="vc"><video id="vJon" class="clip" src="assets/video/jonathan.mp4" data-start="__S_JON__" data-duration="__D_JON__" data-track-index="3" muted playsinline></video></div></div>
      <div class="ab pill k" id="tagE" style="left:110px;top:735px;font-size:52px">Étudiant</div>
      <div class="ab pill y" id="xlChip"><div class="x">X</div>Les bases d'Excel</div>
      <div class="ab pill k" id="rien">rien de plus</div>
      <div class="ab card vcard" id="vcDep"><div class="vc"><video id="vDep" class="clip" src="assets/video/depot.mp4" data-start="__S_DEP__" data-duration="__D_DEP__" data-track-index="4" muted playsinline></video></div></div>
      <div class="ab pill y" id="pin"><svg viewBox="0 0 40 50"><path d="M20 48 C8 32 2 24 2 17 A18 18 0 0 1 38 17 C38 24 32 32 20 48Z" fill="#e0161a" stroke="#111" stroke-width="3"/><circle cx="20" cy="17" r="7" fill="#fff" stroke="#111" stroke-width="3"/></svg>Kinshasa</div>
      <div class="ab card dep" id="dp1"><svg viewBox="0 0 100 90"><path d="M6 40 L50 6 L94 40 V86 H6 Z" fill="#ffd60a" stroke="#111" stroke-width="5" stroke-linejoin="round"/><rect x="34" y="50" width="32" height="36" fill="#fff" stroke="#111" stroke-width="5"/></svg><div class="n">Dépôt 1</div></div>
      <div class="ab card dep" id="dp2"><svg viewBox="0 0 100 90"><path d="M6 40 L50 6 L94 40 V86 H6 Z" fill="#ff5c00" stroke="#111" stroke-width="5" stroke-linejoin="round"/><rect x="34" y="50" width="32" height="36" fill="#fff" stroke="#111" stroke-width="5"/></svg><div class="n">Dépôt 2</div></div>
      <div class="ab card dep" id="dp3"><svg viewBox="0 0 100 90"><path d="M6 40 L50 6 L94 40 V86 H6 Z" fill="#1d7a46" stroke="#111" stroke-width="5" stroke-linejoin="round"/><rect x="34" y="50" width="32" height="36" fill="#fff" stroke="#111" stroke-width="5"/></svg><div class="n">Dépôt 3</div></div>
      <div class="ab card dep" id="dp4"><svg viewBox="0 0 100 90"><path d="M6 40 L50 6 L94 40 V86 H6 Z" fill="#1c5bd6" stroke="#111" stroke-width="5" stroke-linejoin="round"/><rect x="34" y="50" width="32" height="36" fill="#fff" stroke="#111" stroke-width="5"/></svg><div class="n">Dépôt 4</div></div>
      <div class="ab card dep" id="dp5"><svg viewBox="0 0 100 90"><path d="M6 40 L50 6 L94 40 V86 H6 Z" fill="#b36cd0" stroke="#111" stroke-width="5" stroke-linejoin="round"/><rect x="34" y="50" width="32" height="36" fill="#fff" stroke="#111" stroke-width="5"/></svg><div class="n">Dépôt 5</div></div>
      <div class="ab card vcard" id="vcResp"><div class="vc"><video id="vResp" class="clip" src="assets/video/responsable.mp4" data-start="__S_RESP__" data-duration="__D_RESP__" data-track-index="5" muted playsinline></video></div></div>
      <div class="ab card" id="cal"><div class="h">CHAQUE SEMAINE</div><div class="b">2 jours</div><div class="s" data-layout-allow-overlap>pour un rapport</div></div>
      <div class="ab card sheet" id="sh1"><b></b><i></i><i style="width:80%"></i><i></i><i style="width:60%"></i></div>
      <div class="ab card sheet" id="sh2"><b></b><i></i><i style="width:70%"></i><i></i><i style="width:85%"></i></div>
      <div class="ab card sheet" id="sh3"><b></b><i style="width:90%"></i><i></i><i style="width:65%"></i><i></i></div>
      <div class="ab pill" id="rap">Rapport au directeur</div>

      <!-- D. BOUCLE 1 -->
      <div class="ab card vcard" id="vcJon2"><div class="vc"><video id="vJon2" class="clip" src="assets/video/jonathan_biblio.mp4" data-start="__S_JON2__" data-duration="__D_JON2__" data-track-index="6" muted playsinline></video></div></div>
      <div class="ab pill k" id="tagJ2" style="left:110px;top:735px;font-size:52px">Jonathan</div>
      <div class="ab pill y" id="expert">Pas besoin d'être expert</div>

      <!-- E. TABLEAU DE BORD -->
      <div class="ab card vcard" id="vcDash"><div class="vc"><video id="vDash" class="clip" src="assets/video/dashboard.mp4" data-start="__S_DASH__" data-duration="__D_DASH__" data-track-index="7" muted playsinline></video></div></div>
      <div class="ab pill g" id="tagD" style="left:110px;top:735px;font-size:52px">Tableau de bord</div>
      <div class="ab card vcard" id="vcDir"><div class="vc"><video id="vDir" class="clip" src="assets/video/directeur.mp4" data-start="__S_DIR__" data-duration="__D_DIR__" data-track-index="8" muted playsinline></video></div></div>
      <div class="ab pill k" id="tagDir" style="left:110px;top:735px;font-size:52px">Le directeur</div>
      <div class="ab card" id="db"><div class="ttl">Ventes par dépôt</div><div class="sub">MIS À JOUR AUTOMATIQUEMENT</div>
        <div id="bars">
          <div class="bar"><i id="b1" style="background:#ffd60a"></i><div class="l">D1</div></div>
          <div class="bar"><i id="b2" style="background:#ff5c00"></i><div class="l">D2</div></div>
          <div class="bar"><i id="b3" style="background:#1d7a46"></i><div class="l">D3</div></div>
          <div class="bar"><i id="b4" style="background:#1c5bd6"></i><div class="l">D4</div></div>
          <div class="bar"><i id="b5" style="background:#b36cd0"></i><div class="l">D5</div></div>
        </div></div>
      <svg class="ab" id="crown" viewBox="0 0 110 90"><path d="M8 80 L14 24 L36 50 L55 10 L74 50 L96 24 L102 80 Z" fill="#ffd60a" stroke="#111" stroke-width="6" stroke-linejoin="round"/></svg>
      <div class="ab pill" id="alert">Stock bas</div>

      <!-- E2. IA -->
      <div class="ab center" id="fouL">Le plus fou ?</div>
      <div class="ab aiic" id="aiB1"><img src="assets/img/ic_chatgpt.png" /></div>
      <div class="ab aiic" id="aiB2"><img src="assets/img/ic_claude.png" /></div>
      <div class="ab aiic" id="aiB3"><img src="assets/img/ic_gemini.svg" /></div>
      <div class="ab card" id="chat">
        <div class="hd"><div class="aiic"><img src="assets/img/ic_claude.png" /></div><div class="aiic"><img src="assets/img/ic_chatgpt.png" /></div><div class="aiic"><img src="assets/img/ic_gemini.svg" /></div>Ton assistant IA</div>
        <div class="bub" id="ub">__PROMPT__</div>
        <div class="bub" id="ab">Voici ta formule :<br /><span id="fx">=SOMME.SI(Dépôt ; "D1" ; Ventes)</span>
          <div id="mini"><i id="m1" style="background:#ffd60a"></i><i id="m2" style="background:#ff5c00"></i><i id="m3" style="background:#1d7a46"></i><i id="m4" style="background:#1c5bd6"></i><i id="m5" style="background:#b36cd0"></i></div></div>
      </div>

      <!-- F. À QUI LE VENDRE -->
      <div class="ab card" id="qDb"><div class="mb"><i style="height:55%;background:#ffd60a"></i><i style="height:80%;background:#ff5c00"></i><i style="height:40%;background:#1d7a46"></i><i style="height:95%;background:#1c5bd6"></i><i style="height:65%;background:#b36cd0"></i></div></div>
      <div class="ab ico" id="qMark">?</div>
      <div class="ab pill k" id="qPill">À qui le vendre ?</div>

      <!-- G. PROSPECTION -->
      <div class="ab card" id="srch">
        <div id="sbar"><svg viewBox="0 0 24 24" fill="none" stroke="#111" stroke-width="3"><circle cx="10" cy="10" r="7"/><path d="M15 15 L22 22" stroke-linecap="round"/></svg><div class="q">__SEARCH__</div></div>
        <div class="row" id="r1"><div class="b"><svg viewBox="0 0 40 40" fill="#fff"><rect x="6" y="10" width="28" height="26" rx="2"/></svg></div><div>Distribution de boissons<small>Kinshasa · 5 dépôts</small></div></div>
        <div class="row" id="r2"><div class="b"><svg viewBox="0 0 40 40" fill="#fff"><rect x="6" y="10" width="28" height="26" rx="2"/></svg></div><div>Grossiste alimentaire<small>Lubumbashi · 3 dépôts</small></div></div>
        <div class="row" id="r3"><div class="b"><svg viewBox="0 0 40 40" fill="#fff"><rect x="6" y="10" width="28" height="26" rx="2"/></svg></div><div>Import-export<small>Matadi · 4 dépôts</small></div></div>
        <div class="row" id="r4"><div class="b"><svg viewBox="0 0 40 40" fill="#fff"><rect x="6" y="10" width="28" height="26" rx="2"/></svg></div><div>Distribution pharmaceutique<small>Kinshasa · 6 dépôts</small></div></div>
      </div>
      <div class="ab card" id="ct"><div class="av">__MAN__</div><div class="t">Responsable commercial<small>LA BONNE PERSONNE À CONTACTER</small></div></div>
      <svg class="ab" id="target" viewBox="0 0 100 100"><circle cx="50" cy="50" r="44" fill="#fff" stroke="#111" stroke-width="6"/><circle cx="50" cy="50" r="30" fill="#e0161a" stroke="#111" stroke-width="5"/><circle cx="50" cy="50" r="14" fill="#fff" stroke="#111" stroke-width="5"/></svg>
      <div class="ab card" id="msgc"><div class="bub" id="mb">__MSG__</div></div>
      <div class="ab ico" id="sendB"><svg viewBox="0 0 24 24" fill="#fff"><path d="M3 20.5 21 12 3 3.5l3 8.5-3 8.5Zm3-8.5h9"/></svg></div>

      <!-- H. BOUCLE 3 -->
      <div class="ab card vcard" id="vcJon3"><div class="vc"><video id="vJon3" class="clip" src="assets/video/jonathan.mp4" data-start="__S_JON3__" data-duration="__D_JON3__" data-track-index="9" muted playsinline></video></div></div>
      <div class="ab card mt" id="mt1"><i style="height:50%;background:#ffd60a"></i><i style="height:85%;background:#ff5c00"></i><i style="height:65%;background:#1d7a46"></i></div>
      <div class="ab card mt" id="mt2"><i style="height:70%;background:#1c5bd6"></i><i style="height:40%;background:#ffd60a"></i><i style="height:90%;background:#ff5c00"></i></div>
      <div class="ab card mt" id="mt3"><i style="height:60%;background:#b36cd0"></i><i style="height:95%;background:#1d7a46"></i><i style="height:45%;background:#1c5bd6"></i></div>
      <div class="ab st" id="st1">__MAN__</div><div class="ab st" id="st2">__MAN__</div><div class="ab st" id="st3">__MAN__</div><div class="ab st" id="st4">__MAN__</div><div class="ab st" id="st5">__MAN__</div>
      <div class="ab card" id="qb">?</div>

      <!-- I. CTA -->
      <div class="ab card" id="chk">
        <div class="ck" id="ck1"><div class="b"><i id="ci1"></i></div>Des bases en Excel</div>
        <div class="ck" id="ck2"><div class="b"><i id="ci2"></i></div>Partant</div>
      </div>
      <div class="ab" id="rocket"><svg viewBox="0 0 100 130"><path d="M50 4 C74 24 80 58 72 90 H28 C20 58 26 24 50 4 Z" fill="#fff" stroke="#111" stroke-width="6" stroke-linejoin="round"/><circle cx="50" cy="48" r="12" fill="#1c5bd6" stroke="#111" stroke-width="5"/><path d="M28 70 L10 94 L30 90 Z M72 70 L90 94 L70 90 Z" fill="#ff5c00" stroke="#111" stroke-width="5" stroke-linejoin="round"/><path d="M38 94 C40 108 50 124 50 124 C50 124 60 108 62 94 Z" fill="#ffd60a" stroke="#111" stroke-width="5" stroke-linejoin="round"/></svg></div>
      <div class="ab pill" id="bizPill">Ton business, maintenant</div>
      <div class="ab card" id="sub"><img class="sublogo" src="assets/img/logo_dm.png" /></div>

      <div class="spark" id="s1x" style="left:50px;top:180px">__STAR__</div>
      <div class="spark" id="s2x" style="left:960px;top:200px">__STAR__</div>
      <div class="spark" id="s3x" style="left:60px;top:1300px;width:50px;height:50px">__STAR__</div>
      <div class="spark" id="s4x" style="left:960px;top:1310px;width:56px;height:56px">__STAR__</div>

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
      const HIDE = ["#vHookC","#x1","#x3","#x4","#city","#co1","#co2","#co3","#vcBib","#tagJ","#rev","#ai1","#ai2","#ai3",
        "#vcJon","#tagE","#xlChip","#rien","#vcDep","#pin","#dp1","#dp2","#dp3","#dp4","#dp5","#vcResp","#cal","#sh1","#sh2","#sh3","#rap",
        "#vcJon2","#tagJ2","#expert","#vcDash","#tagD","#vcDir","#tagDir","#db","#crown","#alert",
        "#fouL","#aiB1","#aiB2","#aiB3","#chat","#ab","#qDb","#qMark","#qPill","#srch","#r1","#r2","#r3","#r4","#ct","#target","#msgc","#sendB",
        "#vcJon3","#mt1","#mt2","#mt3","#st1","#st2","#st3","#st4","#st5","#qb",
        "#chk","#ci1","#ci2","#rocket","#bizPill","#sub","#s1x","#s2x","#s3x","#s4x","#flash"];
      gsap.set(HIDE, { autoAlpha: 0 });
      gsap.set(["#b1","#b2","#b3","#b4","#b5"], { scaleY: 0 });
      gsap.set(["#m1","#m2","#m3","#m4","#m5"], { height: "0%" });
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
      const swapIn = (sel, at) => IN(sel, { x: 1100 }, { x: 0, duration: 0.45, ease: "power3.out" }, at);
      const swapOut = (sel, at) => OUT(sel, { x: -1100, autoAlpha: 0, duration: 0.45, ease: "power3.in" }, at);
      const typeSpans = (sel, from, to) => { const sp = document.querySelectorAll(sel); sp.forEach((s, i) => tl.set(s, { display: "inline" }, from + (to - from) * i / sp.length)); };

      // ---------- A. HOOK ----------
      rise("#vHookC", 0.05, -2);
      [["#x1", 4], ["#x3", -3], ["#x4", 3]].forEach(([x, r], i) => IN(x, { x: 500, rotation: r + 15 }, { x: 0, rotation: r, duration: 0.4, ease: "back.out(1.6)" }, Math.max(0.15, T.excel - 0.35) + i * 0.22));
      OUT(["#x1", "#x3", "#x4"], { x: 600, autoAlpha: 0, duration: 0.35, ease: "power2.in" }, T.entreprises - 0.35);
      IN("#city", { y: 700, rotation: 6 }, { y: 0, rotation: 2, duration: 0.45, ease: "back.out(1.4)" }, T.entreprises - 0.15);
      [["#co1", 0], ["#co2", 0.15], ["#co3", 0.3]].forEach(([c, d]) => pop(c, T.paieraient + d, 0));
      sparks(T.paieraient);
      sparksOut(T.montre - 0.4);
      leave(["#vHookC", "#city", "#co1", "#co2", "#co3"], T.montre - 0.4);

      // ---------- B. PROMESSE ----------
      rise("#vcBib", T.montre - 0.3, -1);
      pop("#tagJ", T.jonathan1, -3);
      pop("#rev", T.revenu - 0.25, 2);
      [["#ai1", -6], ["#ai2", 0], ["#ai3", 6]].forEach(([a, r], i) => pop(a, T.ia - 0.35 + i * 0.15, r));
      leave(["#vcBib", "#tagJ", "#rev", "#ai1", "#ai2", "#ai3"], T.etudiant - 0.95);

      // ---------- C. PARTIE 1 ----------
      swapIn("#vcJon", T.etudiant - 0.85);
      pop("#tagE", T.etudiant - 0.1, -3);
      pop("#xlChip", T.bases2 - 0.2, -2);
      slam("#rien", T.bases2 + 0.9);
      OUT(["#tagE", "#xlChip", "#rien"], { autoAlpha: 0, duration: 0.25 }, T.pendant - 0.35);
      swapOut("#vcJon", T.pendant - 0.35);
      swapIn("#vcDep", T.pendant - 0.3);
      ["#dp1", "#dp2", "#dp3", "#dp4", "#dp5"].forEach((d, i) => IN(d, { y: 300, scale: 0.5 }, { y: 0, scale: 1, duration: 0.35, ease: "back.out(2)" }, T.cinq - 0.15 + i * 0.12));
      pop("#pin", T.kinshasa - 0.15, 3);
      OUT(["#dp1", "#dp2", "#dp3", "#dp4", "#dp5", "#pin"], { autoAlpha: 0, y: 200, duration: 0.3, ease: "power2.in" }, T.responsable - 0.35);
      swapOut("#vcDep", T.responsable - 0.35);
      swapIn("#vcResp", T.responsable - 0.3);
      rise("#cal", T.jours - 0.3, -3);
      [["#sh1", -6], ["#sh2", 3], ["#sh3", 8]].forEach(([s, r], i) => IN(s, { y: -500, rotation: r + 30 }, { y: 0, rotation: r, duration: 0.4, ease: "bounce.out" }, T.rassembler + i * 0.35));
      pop("#rap", T.directeur - 0.4, -3);
      leave(["#vcResp", "#cal", "#sh1", "#sh2", "#sh3", "#rap"], T.ce_rapport - 0.4);

      // ---------- D. BOUCLE 1 ----------
      rise("#vcJon2", T.ce_rapport - 0.3, 1);
      pop("#tagJ2", T.place - 0.6, -3);
      slam("#expert", T.expert - 0.4);
      sparks(T.expert);
      sparksOut(T.cree - 0.4);
      leave(["#vcJon2", "#tagJ2", "#expert"], T.cree - 0.4);

      // ---------- E. TABLEAU DE BORD ----------
      rise("#vcDash", T.cree - 0.3, -1);
      pop("#tagD", T.cree + 0.5, -3);
      rise("#db", T.chaque2 - 0.3, 0);
      const H1 = [0.45, 0.7, 0.35, 0.55, 0.3], H2 = [0.6, 0.85, 0.5, 0.2, 0.45];
      H1.forEach((h, i) => tl.fromTo("#b" + (i + 1), { scaleY: 0 }, { scaleY: h, duration: 0.5, ease: "back.out(1.6)", immediateRender: false }, T.graph1 - 0.1 + i * 0.08));
      H2.forEach((h, i) => tl.to("#b" + (i + 1), { scaleY: h, duration: 0.6, ease: "power2.inOut" }, T.seuls - 0.1));
      OUT(["#vcDash", "#tagD"], { x: -1100, autoAlpha: 0, duration: 0.45, ease: "power3.in" }, T.voit - 0.4);
      swapIn("#vcDir", T.voit - 0.35);
      pop("#tagDir", T.voit + 0.2, -3);
      // couronne au-dessus de D2 (la barre la plus haute), alerte sur D4
      tl.set("#crown", { left: 310, top: 975 }, 0);
      IN("#crown", { y: -200, rotation: -30 }, { y: 0, rotation: 0, duration: 0.45, ease: "bounce.out" }, T.vend);
      tl.to("#b4", { backgroundColor: "#e0161a", duration: 0.2, yoyo: true, repeat: 3 }, T.stock);
      pop("#alert", T.stock, 3);
      leave(["#vcDir", "#tagDir", "#db", "#crown", "#alert"], T.fou - 0.4);

      // ---------- E2. IA ----------
      slam("#fouL", T.fou - 0.25);
      [["#aiB1", -6], ["#aiB2", 0], ["#aiB3", 6]].forEach(([a, r], i) => pop(a, T.intelligence - 0.3 + i * 0.18, r));
      sparks(T.intelligence);
      sparksOut(T.suffit - 0.4);
      leave(["#fouL", "#aiB1", "#aiB2", "#aiB3"], T.suffit - 0.4);
      rise("#chat", T.suffit - 0.3, 0);
      typeSpans("#ub span", T.decrire - 0.1, T.decrire + 1.6);
      IN("#ab", { y: 80 }, { y: 0, duration: 0.35, ease: "back.out(1.6)" }, T.formules - 0.6);
      tl.fromTo("#fx", { scale: 0.6 }, { scale: 1, duration: 0.3, ease: "back.out(2.5)", immediateRender: false }, T.formules - 0.2);
      [0.5, 0.9, 0.65, 0.3, 0.75].forEach((h, i) => tl.fromTo("#m" + (i + 1), { height: "0%" }, { height: h * 100 + "%", duration: 0.4, ease: "back.out(1.6)", immediateRender: false }, T.graph2 - 0.15 + i * 0.07));
      leave(["#chat", "#ab"], T.mais - 0.4);

      // ---------- F. À QUI LE VENDRE ----------
      rise("#qDb", T.mais - 0.3, -3);
      slam("#qMark", T.vendre - 0.6);
      pop("#qPill", T.vendre - 0.3, -2);
      leave(["#qDb", "#qMark", "#qPill"], T.la_aussi - 0.4);

      // ---------- G. PROSPECTION ----------
      rise("#srch", T.la_aussi - 0.3, 0);
      typeSpans("#sbar span", T.trouve - 0.2, T.societes + 0.8);
      ["#r1", "#r2", "#r3", "#r4"].forEach((r, i) => IN(r, { x: 300 }, { x: 0, duration: 0.3, ease: "back.out(1.8)" }, T.societes + 0.9 + i * 0.18));
      IN("#ct", { y: 300 }, { y: 0, duration: 0.4, ease: "back.out(1.6)" }, T.personne - 0.4);
      tl.to("#r1", { backgroundColor: "#fff3cf", borderColor: "#111", duration: 0.2 }, T.personne - 0.3);
      IN("#target", { scale: 3, rotation: -90 }, { scale: 1, rotation: 0, duration: 0.35, ease: "power4.in" }, T.personne + 0.1);
      OUT(["#ct", "#target"], { autoAlpha: 0, y: 200, duration: 0.3, ease: "power2.in" }, T.ecrire - 0.5);
      IN("#msgc", { y: 400 }, { y: 0, duration: 0.4, ease: "back.out(1.4)" }, T.ecrire - 0.4);
      typeSpans("#mb span", T.ecrire - 0.2, T.message + 0.9);
      pop("#sendB", T.message + 0.3, 0);
      tl.to("#sendB", { scale: 1.2, duration: 0.15, yoyo: true, repeat: 1 }, T.message + 0.8);
      leave(["#srch", "#r1", "#r2", "#r3", "#r4", "#msgc", "#sendB"], T.quand - 0.4);

      // ---------- H. BOUCLE 3 ----------
      rise("#vcJon3", T.quand - 0.3, 1);
      [["#mt1", -5], ["#mt2", 2], ["#mt3", 6]].forEach(([m, r], i) => pop(m, T.quand + 0.4 + i * 0.2, r));
      OUT(["#mt1", "#mt2", "#mt3"], { autoAlpha: 0, y: 150, duration: 0.3 }, T.etudiants - 0.35);
      [["#st1", -400], ["#st2", -300], ["#st3", 0], ["#st4", 300], ["#st5", 400]].forEach(([m, x], i) =>
        IN(m, { x, y: 200 }, { x: 0, y: 0, duration: 0.45, ease: "back.out(1.5)" }, T.etudiants - 0.2 + i * 0.08));
      pop("#qb", T.comment2 - 0.2, 4);
      leave(["#vcJon3", "#st1", "#st2", "#st3", "#st4", "#st5", "#qb"], T.si - 0.4);

      // ---------- I. CTA ----------
      rise("#chk", T.si - 0.3, -1);
      pop("#ci1", T.bases3, 45);
      pop("#ci2", T.partant, 45);
      IN("#rocket", { y: 400, scale: 0.5 }, { y: 0, scale: 1, duration: 0.45, ease: "back.out(1.8)" }, T.tout - 0.2);
      pop("#bizPill", T.business - 0.2, -2);
      sparks(T.business);
      tl.to("#rocket", { y: -1400, duration: 0.7, ease: "power3.in" }, DUR - 1.6);
      sparksOut(DUR - 1.35);
      leave(["#chk", "#ci1", "#ci2", "#bizPill"], DUR - 1.35);
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
