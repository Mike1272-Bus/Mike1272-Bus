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
      .serie { position: absolute; top: 64px; right: 70px; z-index: 40; background: #ffd60a; color: #111; font-size: 28px; padding: 12px 26px 6px; border-radius: 40px; border: 4px solid #111; }
      .card { background: #fff; border: 5px solid #111; border-radius: 36px; box-shadow: 14px 14px 0 #111; }
      .photo { border-radius: 34px; border: 10px solid #fff; overflow: hidden; box-shadow: 0 40px 80px rgba(60,30,0,0.30); background: #ddd; }
      .photo img, .photo video { width: 100%; height: 100%; object-fit: cover; display: block; }
      .pill { text-align: center; background: #ff5c00; color: #fff; border-radius: 70px; border: 5px solid #111; box-shadow: 10px 10px 0 #111; white-space: nowrap; padding: 18px 40px 6px; }
      .pill.y { background: #ffd60a; color: #111; }
      .pill.k { background: #111; color: #fff; box-shadow: 10px 10px 0 #ff5c00; }
      .hl { background: #ffd60a; color: #c94200; border-radius: 18px; padding: 0 14px; }
      .spark { position: absolute; width: 70px; height: 70px; z-index: 15; }
      .spark svg { width: 100%; height: 100%; fill: #111; }
      .center { left: 0; width: 1080px; text-align: center; }
      .ico { display: flex; align-items: center; justify-content: center; border-radius: 50%; border: 6px solid #111; box-shadow: 10px 10px 0 #111; background: #fff; }
      .ico svg { width: 62%; height: 62%; }
      .nb { width: 110px; height: 110px; border-radius: 50%; background: #ff5c00; color: #fff; border: 5px solid #111; font-size: 76px; flex: none;
            display: flex; align-items: center; justify-content: center; padding-top: 12px; }

      /* A. hook */
      #t1 { top: 180px; font-size: 80px; line-height: 1.08; }
      .pk { width: 450px; }
      .pk img { width: 100%; height: 100%; object-fit: cover; }
      #k1 { left: 60px; top: 440px; height: 450px; }
      #k2 { left: 565px; top: 470px; height: 370px; }
      #k3 { left: 70px; top: 930px; height: 440px; }
      #k4 { left: 570px; top: 880px; height: 500px; }
      #t2 { top: 170px; font-size: 64px; line-height: 1; }
      #t3 { top: 300px; font-size: 124px; line-height: 1; color: #ff5c00; }
      #crowd { left: 120px; top: 520px; width: 840px; height: 500px; display: grid; grid-template-columns: repeat(6, 1fr); grid-template-rows: repeat(4, 1fr); }
      .pp { display: flex; align-items: center; justify-content: center; color: #111; }
      .pp svg { width: 104px; height: 118px; }
      #cart0 { left: 390px; top: 1080px; width: 300px; height: 300px; }
      #cart0 .x { position: absolute; right: -24px; top: -24px; width: 110px; height: 110px; border-radius: 50%; background: #e0161a; border: 6px solid #111; }
      #cart0 .x svg { width: 100%; height: 100%; }

      /* B. promesse */
      #b2 { left: 110px; top: 260px; width: 560px; height: 700px; transform: rotate(-4deg); }
      #b2n { left: 70px; top: 220px; z-index: 5; width: 150px; height: 150px; font-size: 104px; }
      #b3 { left: 610px; top: 780px; width: 380px; height: 380px; background: #ff5c00; color: #fff; font-size: 300px; padding-top: 70px; }

      /* C. fil d'actualité */
      #phone { left: 270px; top: 190px; width: 540px; height: 1190px; border-radius: 72px; background: #111; padding: 18px; box-shadow: 0 40px 90px rgba(60,30,0,0.35); }
      #scr { position: relative; width: 100%; height: 100%; border-radius: 56px; overflow: hidden; background: #eef0f3; }
      #scr .bar { position: absolute; left: 0; right: 0; top: 0; height: 110px; background: #fff; z-index: 3; display: flex; align-items: flex-end; padding: 0 30px 18px;
                  font-size: 40px; border-bottom: 2px solid #ddd; }
      #col { position: absolute; left: 0; right: 0; top: 110px; }
      .post { background: #fff; margin: 16px 14px 0; border-radius: 26px; padding: 20px; }
      .post .hd { display: flex; align-items: center; gap: 14px; }
      .post .av { width: 58px; height: 58px; border-radius: 50%; background: #cfd4da; flex: none; display: flex; align-items: center; justify-content: center; color: #fff; font-size: 32px; padding-top: 5px; }
      .post .nm { height: 18px; width: 180px; border-radius: 9px; background: #cfd4da; }
      .post .ln { height: 16px; border-radius: 8px; background: #dde1e6; margin-top: 16px; }
      .post .im { height: 300px; border-radius: 16px; overflow: hidden; margin-top: 18px; background: #cfd4da; }
      .post .im img { width: 100%; height: 100%; object-fit: cover; }
      .post .tt { font-size: 38px; line-height: 1.1; margin-top: 16px; }
      .post .who { font-family: 'Work Sans'; font-weight: 700; font-size: 26px; }
      .post .rx { font-family: 'Work Sans'; font-weight: 700; font-size: 24px; color: #5f6570; margin-top: 14px; }
      #pA { outline: 0 solid #ff5c00; }
      #c0 { left: 760px; top: 700px; width: 200px; height: 200px; z-index: 5; flex-direction: column; font-size: 60px; line-height: 1; }
      #c0 svg { width: 90px; height: 80px; }
      #c1 { left: 30px; top: 330px; width: 330px; height: 260px; z-index: 5; display: grid; grid-template-columns: repeat(3, 1fr); padding: 24px 20px 10px; transform: rotate(-4deg); }
      #c1 .pm { display: flex; align-items: center; justify-content: center; }
      #c1 .pm svg { width: 70px; height: 80px; }
      #c1 .fk { grid-column: 1 / 4; display: flex; justify-content: center; }
      #c1 .fk svg { width: 150px; height: 70px; }
      #c2 { left: 60px; top: 1000px; width: 340px; height: 300px; z-index: 5; }
      #c2 svg { width: 100%; height: 100%; }

      /* D. une phrase */
      #d1 { left: 90px; top: 440px; width: 900px; height: 250px; display: flex; align-items: center; justify-content: center; font-size: 78px; }
      #strike { position: absolute; left: 60px; right: 60px; top: 112px; height: 16px; background: #e0161a; border-radius: 8px; transform-origin: left center; }
      #pen { left: 120px; top: 380px; width: 190px; height: 190px; z-index: 6; }
      #pen svg { width: 100%; height: 100%; }
      #d3 { left: 390px; top: 790px; width: 300px; height: 300px; }
      #d3 svg { width: 100%; height: 100%; }

      /* E. publication ciblée + Nadine */
      #postB { left: 400px; top: 200px; width: 630px; height: 840px; background: #fff; border: 5px solid #111; border-radius: 36px; box-shadow: 14px 14px 0 #111; padding: 26px; z-index: 4; transform-origin: 100% 100%; }
      #postB .av { background: #ff5c00; }
      #postB .tt { font-size: 50px; line-height: 1.22; margin-top: 18px; }
      #postB .mk { border-radius: 12px; padding: 0 8px; }
      #postB .im { height: 340px; margin-top: 22px; }
      #scrollW { left: 60px; top: 200px; width: 960px; height: 800px; transform: rotate(-2deg); z-index: 2; }
      #nadC { left: 70px; top: 870px; width: 250px; height: 250px; border-radius: 50%; border: 10px solid #fff; overflow: hidden; box-shadow: 0 20px 50px rgba(0,0,0,.3); z-index: 5; }
      #nadC img { width: 100%; height: 100%; object-fit: cover; object-position: 41% 44%; transform: scale(1.9); transform-origin: 41% 44%; }
      #nadTag { left: 110px; top: 1135px; font-size: 44px; z-index: 6; }
      #stop { left: 380px; top: 640px; width: 230px; height: 230px; z-index: 7; }
      #stop svg { width: 100%; height: 100%; }
      #heart { left: 250px; top: 810px; width: 170px; height: 170px; z-index: 7; background: #ff5c00; }
      #heart svg { width: 58%; height: 58%; }

      /* F. différence */
      .mini { top: 330px; width: 420px; height: 640px; padding: 20px; }
      .mini .im { height: 330px; border-radius: 18px; overflow: hidden; margin-top: 16px; }
      .mini .im img { width: 100%; height: 100%; object-fit: cover; }
      .mini .tt { font-size: 38px; line-height: 1.1; margin-top: 14px; }
      #mL { left: 70px; transform: rotate(-3deg); }
      #mL .im img { filter: grayscale(1); }
      #mR { left: 580px; transform: rotate(3deg); }
      #zzz { left: 170px; top: 1010px; font-size: 110px; color: #9b948a; line-height: 1; }
      #cartR { left: 650px; top: 1010px; width: 220px; height: 220px; background: #ff5c00; }
      .hrt { width: 90px; height: 90px; z-index: 6; }
      .hrt svg { width: 100%; height: 100%; }
      #h1 { left: 900px; top: 300px; } #h2 { left: 560px; top: 280px; } #h3 { left: 930px; top: 900px; }
      .coin { width: 90px; height: 90px; border-radius: 50%; background: #ffd60a; border: 5px solid #111; font-size: 56px; display: flex; align-items: center; justify-content: center; padding-top: 8px; z-index: 6; }
      #co1 { left: 880px; top: 1060px; } #co2 { left: 600px; top: 1180px; }

      /* G. chaîne + question */
      .node { left: 410px; width: 260px; height: 260px; }
      #n1 { top: 200px; } #n2 { top: 560px; } #n3 { top: 920px; background: #ff5c00; }
      #n2 { overflow: hidden; background: #ddd; }
      #n2 img { width: 100%; height: 100%; object-fit: cover; object-position: 41% 44%; transform: scale(1.9); transform-origin: 41% 44%; }
      .nl { left: 700px; font-size: 58px; line-height: 1; }
      #nl1 { top: 300px; } #nl2 { top: 660px; } #nl3 { top: 1020px; }
      .arr { left: 500px; width: 80px; height: 100px; }
      .arr svg { width: 100%; height: 100%; }
      #ar1 { top: 462px; } #ar2 { top: 822px; }
      #qc { left: 90px; top: 220px; width: 900px; height: 470px; padding: 44px 50px; }
      #qc .big { font-size: 104px; line-height: 1.02; }
      #qc .qm { position: absolute; right: -40px; top: -60px; width: 170px; height: 170px; border-radius: 50%; background: #ff5c00; color: #fff; border: 6px solid #111;
                font-size: 108px; line-height: 1; display: flex; align-items: center; justify-content: center; padding-top: 14px; box-shadow: 10px 10px 0 #111; }
      #tgt { left: 290px; top: 760px; width: 500px; height: 500px; }
      #tgt svg { position: absolute; inset: 0; width: 100%; height: 100%; }
      #tgt .ph { position: absolute; left: 175px; top: 175px; width: 150px; height: 150px; border-radius: 50%; overflow: hidden; border: 6px solid #111; }
      #tgt .ph img { width: 100%; height: 100%; object-fit: cover; object-position: 41% 44%; transform: scale(1.9); transform-origin: 41% 44%; }
      #dart { left: 560px; top: 820px; width: 300px; height: 300px; z-index: 6; }
      #dart svg { width: 100%; height: 100%; }
      #wal { left: 760px; top: 1060px; width: 250px; height: 250px; background: #ffd60a; z-index: 7; }
      #wal .q { position: absolute; right: -20px; top: -30px; width: 100px; height: 100px; border-radius: 50%; background: #111; color: #fff; border: 5px solid #111;
                font-size: 70px; display: flex; align-items: center; justify-content: center; padding-top: 10px; }

      /* I. CTA */
      #cover { left: 240px; top: 230px; width: 600px; height: 600px; border-radius: 30px; border: 12px solid #fff; overflow: hidden; box-shadow: 0 40px 80px rgba(60,30,0,0.32); }
      #cover img { width: 100%; height: 100%; display: block; }
      #plan { left: 140px; top: 900px; width: 800px; font-size: 64px; }
      #zero { left: 240px; top: 1060px; width: 600px; font-size: 64px; }
      #cbLab { top: 330px; font-size: 92px; line-height: 1; }
      #cbox { left: 70px; top: 560px; width: 940px; height: 170px; display: flex; align-items: center; gap: 26px; padding: 0 30px; }
      #cbox .av { width: 100px; height: 100px; border-radius: 50%; background: #ffd60a; border: 5px solid #111; flex: none; }
      #cbox .in { flex: 1; height: 100px; border-radius: 50px; background: #f1ede6; display: flex; align-items: center; padding: 8px 34px 0; font-size: 64px; }
      #cbox .in span { opacity: 0; }
      #cbox .send { width: 100px; height: 100px; border-radius: 50%; background: #ff5c00; border: 5px solid #111; flex: none; display: flex; align-items: center; justify-content: center; }
      #cbox .send svg { width: 50px; height: 50px; }
      #acc { left: 190px; top: 860px; width: 700px; font-size: 58px; }

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
      <div class="serie">CE QU'ON NE VOUS DIT PAS</div>

      <!-- A. HOOK -->
      <div class="ab center" id="t1">Ce qu'on ne vous dit pas<br />sur les <span class="hl">produits digitaux</span></div>
      <div class="ab photo pk" id="k1"><img src="assets/img/pack1.jpg" /></div>
      <div class="ab photo pk" id="k2"><img src="assets/img/pack2.jpg" /></div>
      <div class="ab photo pk" id="k3"><img src="assets/img/pack3.jpg" /></div>
      <div class="ab photo pk" id="k4"><img src="assets/img/pack4.jpg" style="object-position:center 30%" /></div>
      <div class="ab center" id="t2">Un produit pour</div>
      <div class="ab center" id="t3">TOUT LE MONDE</div>
      <div class="ab" id="crowd">__CROWD__</div>
      <div class="ab ico" id="cart0">__CART__<div class="x"><svg viewBox="0 0 100 100"><path d="M30 30 L70 70 M70 30 L30 70" stroke="#fff" stroke-width="12" stroke-linecap="round"/></svg></div></div>

      <!-- B. PROMESSE -->
      <div class="ab photo" id="b2"><img src="assets/img/plat_riz.jpg" /></div>
      <div class="ab nb" id="b2n">1</div>
      <div class="ab ico" id="b3">?</div>

      <!-- C. FIL D'ACTUALITÉ -->
      <div class="ab" id="phone"><div id="scr">
        <div class="bar" data-layout-allow-overlap data-layout-allow-occlusion>Fil d'actualité</div>
        <div id="col">
          <div class="post"><div class="hd"><div class="av"></div><div class="nm"></div></div><div class="ln" style="width:90%"></div><div class="im"><img src="assets/img/feed1.jpg" /></div></div>
          <div class="post" id="pA"><div class="hd"><div class="av" style="background:#ff5c00">V</div><div class="who">Votre page</div></div>
            <div class="tt">Mes recettes de cuisine</div><div class="im"><img src="assets/img/feed3.jpg" /></div><div class="rx">0 j'aime · 0 commentaire</div></div>
          <div class="post"><div class="hd"><div class="av"></div><div class="nm" style="width:140px"></div></div><div class="ln" style="width:80%"></div><div class="im"><img src="assets/img/feed2.jpg" style="object-position:center 30%" /></div></div>
          <div class="post"><div class="hd"><div class="av"></div><div class="nm" style="width:210px"></div></div><div class="ln" style="width:70%"></div><div class="im"><img src="assets/img/feed4.jpg" /></div></div>
          <div class="post"><div class="hd"><div class="av"></div><div class="nm"></div></div><div class="ln" style="width:90%"></div><div class="ln" style="width:50%"></div><div class="im" style="background:#d6dce3"></div></div>
        </div>
      </div></div>
      <div class="ab ico" id="c0">__HEART_GREY__<span>0</span></div>
      <div class="ab card" id="c1">__PERSON__ __PERSON__ __PERSON__<div class="fk"><svg viewBox="0 0 150 70"><g stroke="#111" stroke-width="8" stroke-linecap="round" fill="none"><path d="M20 8 V62 M8 8 V26 Q20 36 32 26 V8"/><path d="M130 8 Q112 22 130 38 V62"/></g><circle cx="75" cy="35" r="26" fill="#ffd60a" stroke="#111" stroke-width="6"/></svg></div></div>
      <div class="ab" id="c2"><svg viewBox="0 0 340 300"><circle cx="40" cy="270" r="16" fill="#fff" stroke="#111" stroke-width="6"/><circle cx="80" cy="235" r="24" fill="#fff" stroke="#111" stroke-width="6"/>
        <ellipse cx="200" cy="120" rx="135" ry="105" fill="#fff" stroke="#111" stroke-width="7"/>
        <circle cx="160" cy="95" r="26" fill="#111"/><path d="M118 180 C118 140 136 128 160 128 C184 128 202 140 202 180 Z" fill="#111"/>
        <circle cx="255" cy="115" r="42" fill="#e0161a" stroke="#111" stroke-width="6"/><path d="M237 97 L273 133 M273 97 L237 133" stroke="#fff" stroke-width="10" stroke-linecap="round"/></svg></div>

      <!-- D. UNE PHRASE -->
      <div class="ab card" id="d1">Mes recettes de cuisine<div id="strike"></div></div>
      <div class="ab" id="pen"><svg viewBox="0 0 100 100"><g transform="rotate(45 50 50)"><rect x="38" y="4" width="24" height="66" rx="4" fill="#ffd60a" stroke="#111" stroke-width="5"/><rect x="38" y="4" width="24" height="14" fill="#ff5c00" stroke="#111" stroke-width="5"/><path d="M38 70 L50 94 L62 70 Z" fill="#fbe3c0" stroke="#111" stroke-width="5" stroke-linejoin="round"/></g></svg></div>
      <div class="ab" id="d3"><svg viewBox="0 0 100 100"><path d="M50 8 V78 M24 54 L50 82 L76 54" fill="none" stroke="#ff5c00" stroke-width="12" stroke-linecap="round" stroke-linejoin="round"/></svg></div>

      <!-- E. PUBLICATION CIBLÉE + NADINE -->
      <div class="ab photo" id="scrollW">
        <video id="vScroll" class="clip" src="assets/video/scroll.mp4" data-start="__SCROLL_START__" data-duration="__SCROLL_DUR__" data-track-index="1" muted playsinline></video>
      </div>
      <div class="ab" id="postB">
        <div class="post" style="margin:0;padding:0">
          <div class="hd"><div class="av">V</div><div class="who">Votre page</div></div>
          <div class="tt">Des recettes pour <span class="mk" id="mkF" data-layout-allow-overlap>les femmes</span> qui veulent <span class="mk" id="mkS">prendre du poids sainement</span></div>
          <div class="im"><img src="assets/img/plat_gombo.jpg" style="object-position:center 40%" /></div>
        </div>
      </div>
      <div class="ab" id="nadC"><img src="assets/img/nadine_floutee.jpg" /></div>
      <div class="ab pill k" id="nadTag">Nadine</div>
      <div class="ab" id="stop"><svg viewBox="0 0 100 100"><polygon points="30,3 70,3 97,30 97,70 70,97 30,97 3,70 3,30" fill="#e0161a" stroke="#111" stroke-width="5"/><text x="50" y="63" text-anchor="middle" font-family="Baloo 2" font-weight="800" font-size="30" fill="#fff">STOP</text></svg></div>
      <div class="ab ico" id="heart">__HEART_WHITE__</div>

      <!-- F. DIFFÉRENCE -->
      <div class="ab card mini" id="mL"><div class="hd" style="display:flex;align-items:center;gap:12px"><div class="nb" style="width:60px;height:60px;font-size:34px;padding-top:6px;background:#9b948a">V</div></div>
        <div class="tt" style="color:#8a8378">Mes recettes de cuisine</div><div class="im"><img src="assets/img/feed3.jpg" /></div></div>
      <div class="ab card mini" id="mR"><div class="hd" style="display:flex;align-items:center;gap:12px"><div class="nb" style="width:60px;height:60px;font-size:34px;padding-top:6px">V</div></div>
        <div class="tt">Prendre du poids <span class="hl">sainement</span></div><div class="im"><img src="assets/img/plat_gombo.jpg" /></div></div>
      <div class="ab" id="zzz">z z z</div>
      <div class="ab ico" id="cartR">__CART_WHITE__</div>
      <div class="ab hrt" id="h1">__HEART_RED__</div>
      <div class="ab hrt" id="h2">__HEART_RED__</div>
      <div class="ab hrt" id="h3">__HEART_RED__</div>
      <div class="ab coin" id="co1">$</div>
      <div class="ab coin" id="co2">$</div>

      <!-- G. CHAÎNE + QUESTION -->
      <div class="ab ico node" id="n1">__TARGET__</div>
      <div class="ab arr" id="ar1"><svg viewBox="0 0 80 100"><path d="M40 6 V78 M14 54 L40 86 L66 54" fill="none" stroke="#111" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/></svg></div>
      <div class="ab ico node" id="n2"><img src="assets/img/nadine_floutee.jpg" /></div>
      <div class="ab arr" id="ar2"><svg viewBox="0 0 80 100"><path d="M40 6 V78 M14 54 L40 86 L66 54" fill="none" stroke="#111" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/></svg></div>
      <div class="ab ico node" id="n3">__CART_WHITE__</div>
      <div class="ab nl" id="nl1">Précise</div>
      <div class="ab nl" id="nl2">Concernée</div>
      <div class="ab nl" id="nl3" style="color:#ff5c00">Achète</div>
      <div class="ab card" id="qc"><div class="big">À qui <span class="hl">exactement</span><br />je le vends ?</div><div class="qm">?</div></div>
      <div class="ab" id="tgt"><svg viewBox="0 0 500 500"><circle cx="250" cy="250" r="240" fill="#fff" stroke="#111" stroke-width="8"/><circle cx="250" cy="250" r="180" fill="#ff5c00" stroke="#111" stroke-width="8"/>
        <circle cx="250" cy="250" r="122" fill="#fff" stroke="#111" stroke-width="8"/></svg><div class="ph"><img src="assets/img/nadine_floutee.jpg" /></div></div>
      <div class="ab" id="dart"><svg viewBox="0 0 300 300"><path d="M40 260 L205 95" stroke="#111" stroke-width="14" stroke-linecap="round"/><path d="M205 95 L236 64 L250 96 Z M190 110 L150 82 L200 70 Z" fill="#111"/>
        <path d="M40 260 L70 200 L100 230 Z M40 260 L100 270 L70 230 Z" fill="#ffd60a" stroke="#111" stroke-width="5" stroke-linejoin="round"/></svg></div>
      <div class="ab ico" id="wal"><svg viewBox="0 0 100 100"><rect x="30" y="8" width="40" height="84" rx="8" fill="#fff" stroke="#111" stroke-width="6"/><circle cx="50" cy="48" r="15" fill="#ffd60a" stroke="#111" stroke-width="5"/><text x="50" y="55" text-anchor="middle" font-family="Baloo 2" font-weight="800" font-size="20" fill="#111">$</text></svg><div class="q">?</div></div>

      <!-- I. CTA -->
      <div class="ab" id="cover"><img src="assets/img/ebook_cover.png" /></div>
      <div class="ab pill" id="plan">PLAN DE 7 JOURS</div>
      <div class="ab pill y" id="zero">0 $ DE PUB</div>
      <div class="ab center" id="cbLab">Commentez<br /><span class="hl">« EBOOK »</span></div>
      <div class="ab card" id="cbox"><div class="av"></div><div class="in"><span>E</span><span>B</span><span>O</span><span>O</span><span>K</span></div>
        <div class="send"><svg viewBox="0 0 24 24" fill="#fff"><path d="M3 20.5 21 12 3 3.5l3 8.5-3 8.5Zm3-8.5h9"/></svg></div></div>
      <div class="ab pill k" id="acc">Je vous accompagne</div>

      <div class="spark" id="s1" style="left:50px;top:180px">__STAR__</div>
      <div class="spark" id="s2" style="left:960px;top:200px">__STAR__</div>
      <div class="spark" id="s3" style="left:60px;top:1290px;width:50px;height:50px">__STAR__</div>
      <div class="spark" id="s4" style="left:960px;top:1300px;width:56px;height:56px">__STAR__</div>

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
      const HIDE = ["#t1","#k1","#k2","#k3","#k4","#t2","#t3","#crowd","#cart0","#b2","#b2n","#b3","#phone","#c0","#c1","#c2","#d1","#pen","#d3",
              "#scrollW","#postB","#nadC","#nadTag","#stop","#heart","#mL","#mR","#zzz","#cartR","#h1","#h2","#h3","#co1","#co2",
              "#n1","#n2","#n3","#ar1","#ar2","#nl1","#nl2","#nl3","#qc","#tgt","#dart","#wal",
              "#cover","#plan","#zero","#cbLab","#cbox","#acc","#s1","#s2","#s3","#s4","#flash"];
      gsap.set(HIDE, { autoAlpha: 0 });
      gsap.set("#crowd .pp", { autoAlpha: 0 });
      gsap.set("#strike", { scaleX: 0 });
      tl.fromTo("#progress", { scaleX: 0 }, { scaleX: 1, duration: __DUR__, ease: "none" }, 0);
      const flash = (at) => { tl.set("#flash", { autoAlpha: 0.85 }, at); tl.to("#flash", { autoAlpha: 0, duration: 0.22 }, at + 0.04); };
      let lastSparks = 0;
      const sparks = (at) => { lastSparks = at; ["#s1","#s2","#s3","#s4"].forEach((s, i) =>
        IN(s, { scale: 0, rotation: -90 }, { scale: 1, rotation: 0, duration: 0.35, ease: "back.out(2.5)" }, at + i * 0.1)); };
      const sparksOut = (at) => OUT(["#s1","#s2","#s3","#s4"], { scale: 0, autoAlpha: 0, duration: 0.2 }, Math.max(at, lastSparks + 0.7));
      const pop = (sel, at, rot = 0) => IN(sel, { scale: 0, rotation: rot + 12 }, { scale: 1, rotation: rot, duration: 0.4, ease: "back.out(2.2)" }, at);
      const slam = (sel, at) => IN(sel, { scale: 2.4 }, { scale: 1, duration: 0.3, ease: "power4.in" }, at);
      const rise = (sel, at, rot = 0) => IN(sel, { y: 700, rotation: rot + 8 }, { y: 0, rotation: rot, duration: 0.5, ease: "back.out(1.3)" }, at);
      const leave = (sels, at) => OUT(sels, { autoAlpha: 0, y: -80, duration: 0.3, ease: "power2.in" }, at);

      // ---------- A. HOOK ----------
      slam("#t1", 0.1);
      [["#k1", -6], ["#k2", 5], ["#k3", 4], ["#k4", -4]].forEach(([k, r], i) =>
        IN(k, { y: -900, rotation: r * 4 }, { y: 0, rotation: r, duration: 0.5, ease: "back.out(1.3)" }, 0.5 + i * 0.45));
      leave(["#t1"], 3.15);
      tl.to(["#k1", "#k2", "#k3", "#k4"], { scale: 0.9, duration: 0.4, ease: "sine.inOut", yoyo: true, repeat: 1 }, 3.4);
      OUT(["#k1", "#k3"], { x: -900, rotation: -25, autoAlpha: 0, duration: 0.4, ease: "power3.in" }, T.tlm - 0.7);
      OUT(["#k2", "#k4"], { x: 900, rotation: 25, autoAlpha: 0, duration: 0.4, ease: "power3.in" }, T.tlm - 0.7);
      IN("#t2", { y: -60 }, { y: 0, duration: 0.35, ease: "power3.out" }, T.tlm - 0.5);
      slam("#t3", T.tlm - 0.3);
      tl.set("#crowd", { autoAlpha: 1 }, T.tlm - 0.35);
      IN("#crowd .pp", { scale: 0 }, { scale: 1, duration: 0.3, ease: "back.out(2.5)", stagger: { each: 0.03, from: "center", grid: [4, 6] } }, T.tlm - 0.3);
      sparks(T.tlm);
      tl.to("#crowd .pp", { color: "#c9c2b8", y: 18, duration: 0.25, stagger: { each: 0.02, from: "random" } }, T.personne - 0.1);
      tl.to("#t3", { color: "#bdb6ab", duration: 0.3 }, T.personne);
      pop("#cart0", T.personne, -4);
      sparksOut(T.personne);
      leave(["#t2", "#t3", "#crowd", "#cart0"], T.montrer - 0.35);

      // ---------- B. PROMESSE ----------
      IN("#b2", { x: -900, rotation: -14 }, { x: 0, rotation: -4, duration: 0.5, ease: "back.out(1.3)" }, T.montrer);
      pop("#b2n", T.exemple - 0.1, -8);
      IN("#b3", { scale: 0, rotation: -120 }, { scale: 1, rotation: 6, duration: 0.5, ease: "back.out(1.8)" }, T.question - 0.15);
      tl.to("#b3", { rotation: -6, duration: 0.3, yoyo: true, repeat: 3, ease: "sine.inOut" }, T.question + 0.5);
      leave(["#b2", "#b2n", "#b3"], T.dites - 0.35);

      // ---------- C. FIL D'ACTUALITÉ ----------
      rise("#phone", T.dites - 0.15);
      tl.fromTo("#col", { y: 0 }, { y: -1700, duration: T.maintenant - T.dites, ease: "none" }, T.dites);
      tl.to("#pA", { outlineWidth: 6, duration: 0.2 }, T.mes);
      tl.to("#pA", { outlineWidth: 0, duration: 0.3 }, T.concerne + 0.8);
      pop("#c0", T.concerne - 0.1, 6);
      pop("#c1", T.mange - 0.35, -4);
      IN("#c2", { scale: 0.2, x: -100, y: 100 }, { scale: 1, x: 0, y: 0, duration: 0.45, ease: "back.out(1.8)" }, T.pasmoi + 0.3);
      tl.to("#c2", { x: -8, duration: 0.06, yoyo: true, repeat: 5, ease: "none" }, T.moi + 0.3);
      leave(["#phone", "#c0", "#c1", "#c2"], T.maintenant - 0.35);

      // ---------- D. UNE PHRASE ----------
      pop("#d1", T.maintenant, -1);
      IN("#pen", { x: -200, y: -200, rotation: -30 }, { x: 0, y: 0, rotation: 0, duration: 0.45, ease: "back.out(1.5)" }, T.maintenant + 0.6);
      tl.to("#pen", { x: 640, duration: 0.4, ease: "power2.inOut" }, T.phrase - 0.15);
      tl.to("#strike", { scaleX: 1, duration: 0.4, ease: "power2.inOut" }, T.phrase - 0.15);
      IN("#d3", { y: -40 }, { y: 0, duration: 0.4, ease: "back.out(2)" }, T.phrase + 0.3);
      tl.to("#d3", { y: 30, duration: 0.4, yoyo: true, repeat: 1, ease: "sine.inOut" }, T.phrase + 0.7);
      leave(["#d1", "#pen", "#d3"], T.plutot - 0.3);

      // ---------- E. PUBLICATION CIBLÉE + NADINE ----------
      IN("#postB", { x: 900, rotation: 10 }, { x: 0, rotation: 2, duration: 0.55, ease: "back.out(1.3)" }, T.postB - 0.3);
      tl.to("#mkF", { backgroundColor: "#ffd60a", duration: 0.2 }, T.femmes);
      tl.to("#mkS", { backgroundColor: "#ffd60a", duration: 0.2 }, T.sainement - 0.5);
      sparks(T.sainement);
      sparksOut(T.nadine - 0.4);
      tl.to("#postB", { scale: 0.5, x: -10, y: 300, rotation: 4, duration: 0.45, ease: "power3.inOut" }, T.nadine - 0.4);
      IN("#scrollW", { y: -900 }, { y: 0, duration: 0.45, ease: "power3.out" }, T.nadine - 0.35);
      IN("#nadC", { scale: 0 }, { scale: 1, duration: 0.4, ease: "back.out(2)" }, T.nadine);
      pop("#nadTag", T.nadine + 0.2, -3);
      IN("#stop", { scale: 3, rotation: -40 }, { scale: 1, rotation: -8, duration: 0.3, ease: "power4.in" }, T.arrete - 0.05);
      tl.to("#postB", { scale: 0.62, duration: 0.3, ease: "back.out(3)" }, T.arrete);
      IN("#heart", { scale: 0 }, { scale: 1, duration: 0.4, ease: "back.out(3)" }, T.delle - 0.1);
      tl.to("#heart", { scale: 1.15, duration: 0.25, yoyo: true, repeat: 3, ease: "sine.inOut" }, T.delle + 0.35);
      leave(["#scrollW", "#postB", "#nadC", "#nadTag", "#stop", "#heart"], T.changement - 0.35);

      // ---------- F. DIFFÉRENCE ----------
      IN("#mL", { x: -800, rotation: -12 }, { x: 0, rotation: -3, duration: 0.5, ease: "back.out(1.3)" }, T.changement - 0.05);
      IN("#mR", { x: 800, rotation: 12 }, { x: 0, rotation: 3, duration: 0.5, ease: "back.out(1.3)" }, T.changement + 0.2);
      tl.to("#mL", { scale: 0.88, duration: 0.4, ease: "power2.out" }, T.difference - 0.2);
      tl.to("#mR", { scale: 1.06, duration: 0.4, ease: "back.out(2)" }, T.difference - 0.2);
      IN("#zzz", { y: 40 }, { y: 0, duration: 0.4 }, T.difference);
      [["#h1", 0], ["#h2", 0.2], ["#h3", 0.4]].forEach(([h, d]) => IN(h, { scale: 0, y: 60 }, { scale: 1, y: 0, duration: 0.35, ease: "back.out(3)" }, T.difference + d));
      pop("#cartR", T.vendre - 0.2, -6);
      pop("#co1", T.vendre + 0.1, 0);
      pop("#co2", T.vendre + 0.3, 0);
      leave(["#mL", "#mR", "#zzz", "#cartR", "#h1", "#h2", "#h3", "#co1", "#co2"], T.precise - 1.1);

      // ---------- G. CHAÎNE + QUESTION ----------
      pop("#n1", T.precise - 0.6);
      IN("#nl1", { x: 60 }, { x: 0, duration: 0.3, ease: "power3.out" }, T.precise - 0.4);
      IN("#ar1", { y: -30 }, { y: 0, duration: 0.3 }, T.concernee - 0.4);
      pop("#n2", T.concernee - 0.3);
      IN("#nl2", { x: 60 }, { x: 0, duration: 0.3, ease: "power3.out" }, T.concernee - 0.1);
      tl.to("#n2", { scale: 1.08, duration: 0.25, yoyo: true, repeat: 1, ease: "sine.inOut" }, T.envie - 1.9);
      IN("#ar2", { y: -30 }, { y: 0, duration: 0.3 }, T.envie - 0.3);
      pop("#n3", T.acheter - 0.25);
      IN("#nl3", { x: 60 }, { x: 0, duration: 0.3, ease: "power3.out" }, T.acheter - 0.05);
      sparks(T.acheter);
      sparksOut(T.alors - 0.3);
      leave(["#n1", "#n2", "#n3", "#ar1", "#ar2", "#nl1", "#nl2", "#nl3"], T.alors - 0.3);
      rise("#qc", T.alors + 0.05, -1);
      tl.to("#qc .qm", { rotation: 20, duration: 0.3, yoyo: true, repeat: 3, ease: "sine.inOut" }, T.question2);
      IN("#tgt", { scale: 0.3, rotation: -90 }, { scale: 1, rotation: 0, duration: 0.5, ease: "back.out(1.6)" }, T.qui - 0.1);

      // ---------- H. BOUCLE ----------
      IN("#dart", { x: 500, y: -500 }, { x: 0, y: 0, duration: 0.3, ease: "power4.in" }, T.reponse - 0.3);
      tl.to("#tgt", { x: -10, duration: 0.05, yoyo: true, repeat: 5, ease: "none" }, T.reponse);
      pop("#wal", T.payer - 0.3, 6);
      tl.to("#wal .q", { scale: 1.3, duration: 0.2, yoyo: true, repeat: 3, ease: "sine.inOut" }, T.payer + 0.2);
      leave(["#qc", "#tgt", "#dart", "#wal"], T.cta - 0.35);

      // ---------- I. CTA ----------
      IN("#cover", { y: 900, rotationY: 60, transformPerspective: 1400 }, { y: 0, rotationY: -10, duration: 0.6, ease: "power3.out" }, T.cta);
      tl.to("#cover", { rotationY: 8, duration: 4, ease: "sine.inOut" }, T.cta + 0.6);
      pop("#plan", T.sept - 0.1, -2);
      pop("#zero", T.pub - 0.2, 3);
      sparks(T.pub);
      OUT(["#cover", "#plan", "#zero"], { autoAlpha: 0, scale: 0.6, duration: 0.3, ease: "back.in(1.5)" }, T.ebook - 0.3);
      sparksOut(T.ebook - 0.3);
      flash(T.ebook - 0.05);
      slam("#cbLab", T.ebook);
      IN("#cbox", { y: 300 }, { y: 0, duration: 0.45, ease: "back.out(1.6)" }, T.ebook + 0.2);
      document.querySelectorAll("#cbox .in span").forEach((s, i) => tl.set(s, { opacity: 1 }, T.ebookWord + 0.2 + i * 0.14));
      tl.to("#cbox .send", { scale: 1.2, duration: 0.3, yoyo: true, repeat: 5, ease: "sine.inOut" }, T.ebookWord + 1.1);
      pop("#acc", T.accomp - 0.3, -2);

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
