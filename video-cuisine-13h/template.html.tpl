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
      .pill.w { background: #fff; color: #111; }
      .hl { background: #ffd60a; color: #c94200; border-radius: 18px; padding: 0 14px; }
      .spark { position: absolute; width: 70px; height: 70px; z-index: 15; }
      .spark svg { width: 100%; height: 100%; fill: #111; }
      .center { left: 0; width: 1080px; text-align: center; }

      /* A. hook */
      #hookW { left: 70px; top: 220px; width: 940px; height: 800px; transform: rotate(-2deg); }
      #q { left: 110px; top: 930px; font-size: 104px; padding: 26px 50px 10px; }
      #prod { left: 150px; top: 1130px; font-size: 62px; }

      /* B. promesse */
      #b1 { top: 470px; font-size: 130px; line-height: 1; }
      #b2 { top: 680px; font-size: 96px; line-height: 1.1; }
      #b3 { left: 330px; top: 900px; font-size: 56px; }

      /* C. Nadine */
      #nad { left: 60px; top: 230px; width: 480px; height: 853px; transform: rotate(-3deg); }
      #idc { left: 590px; top: 300px; width: 430px; padding: 34px 34px 26px; transform: rotate(2deg); }
      #idc .n { font-size: 84px; line-height: 1; }
      #idc .l { font-family: 'Work Sans'; font-weight: 700; font-size: 44px; line-height: 1.2; margin-top: 18px; }
      #idc .n + .l { margin-top: 26px; }
      #idc .l span { color: #ff5c00; }
      #mince { left: 440px; top: 760px; z-index: 5; font-size: 50px; transform: rotate(-3deg); }
      #souf { left: 560px; top: 930px; font-size: 50px; }

      /* D. marché */
      #goal { left: 70px; top: 210px; width: 940px; font-size: 64px; }
      #mar { left: 120px; top: 380px; width: 840px; height: 860px; }
      #qq1 { left: 50px; top: 1010px; font-size: 64px; transform: rotate(-5deg); }
      #qq2 { left: 620px; top: 1160px; font-size: 64px; transform: rotate(4deg); }

      /* E. et toi */
      #toiT { top: 220px; font-size: 150px; line-height: 1; }
      #toiW { left: 140px; top: 440px; width: 800px; height: 620px; transform: rotate(2deg); }
      #repP { left: 170px; top: 1130px; width: 740px; font-size: 66px; }

      /* F. livre */
      #book { left: 80px; top: 230px; width: 540px; height: 760px; border-radius: 20px 36px 36px 20px; overflow: hidden; background: #fff; border: 6px solid #111;
              box-shadow: 16px 16px 0 #111; transform: rotate(-4deg); }
      #book .ph { height: 430px; overflow: hidden; border-bottom: 6px solid #111; }
      #book .ph img { width: 100%; height: 100%; object-fit: cover; }
      #book .spine { position: absolute; left: 0; top: 0; bottom: 0; width: 22px; background: #ff5c00; border-right: 4px solid #111; }
      #book .txt { position: absolute; left: 50px; right: 28px; top: 452px; bottom: 22px; display: flex; flex-direction: column; }
      #book .kick { font-family: 'Work Sans'; font-weight: 700; font-size: 26px; color: #ff5c00; letter-spacing: .08em; line-height: 1.2; }
      #book .tt { font-size: 56px; line-height: 1.04; margin-top: 12px; }
      #book .ft { margin-top: auto; font-family: 'Work Sans'; font-weight: 700; font-size: 24px; color: #666; line-height: 1.2; }
      #stamp { position: absolute; right: 30px; top: 330px; border: 8px solid #e0161a; color: #e0161a; font-size: 90px; padding: 18px 28px 0; border-radius: 16px;
               transform: rotate(-14deg); background: rgba(255,255,255,0.85); }
      .plate { width: 330px; height: 330px; border-radius: 50%; border: 10px solid #fff; overflow: hidden; box-shadow: 0 30px 60px rgba(60,30,0,0.3); }
      .plate img { width: 100%; height: 100%; object-fit: cover; }
      #p1 { left: 680px; top: 240px; } #p2 { left: 700px; top: 560px; width: 300px; height: 300px; }
      #plan4 { left: 80px; top: 1030px; width: 920px; height: 300px; padding: 26px 30px; }
      #plan4 .h { font-size: 44px; line-height: 1; }
      #plan4 .row { display: flex; gap: 20px; margin-top: 22px; }
      #plan4 .wk { flex: 1; height: 150px; border: 5px solid #111; border-radius: 22px; background: #fff3e6; text-align: center; padding-top: 18px; font-size: 40px; position: relative; }
      #plan4 .wk small { display: block; font-family: 'Work Sans'; font-weight: 700; font-size: 22px; color: #666; margin-top: 2px; }
      #plan4 .wk .ok { position: absolute; right: -14px; top: -18px; width: 56px; height: 56px; border-radius: 50%; background: #1faa59; border: 4px solid #111; }
      #plan4 .wk .ok svg { width: 100%; height: 100%; }
      #crs { left: 600px; top: 900px; font-size: 48px; transform: rotate(4deg); }

      /* G. WhatsApp */
      #wa { left: 150px; top: 200px; width: 780px; height: 1150px; border-radius: 44px; overflow: hidden; background: #efe7dc; border: 6px solid #111; box-shadow: 16px 16px 0 #111; }
      #wa .top { height: 150px; background: #0b6b5d; display: flex; align-items: center; gap: 22px; padding: 0 34px; color: #fff; }
      #wa .av { width: 92px; height: 92px; border-radius: 50%; overflow: hidden; border: 4px solid #fff; flex: none; }
      #wa .av img { width: 100%; height: 100%; object-fit: cover; }
      #wa .nm { font-size: 48px; line-height: 1; }
      #wa .st { font-family: 'Work Sans'; font-weight: 400; font-size: 26px; opacity: .85; margin-top: 6px; }
      #wa .body { position: absolute; left: 0; right: 0; top: 150px; bottom: 0; padding: 36px 30px; display: flex; flex-direction: column; gap: 22px; }
      .bb { max-width: 600px; font-family: 'Work Sans'; font-weight: 700; font-size: 36px; line-height: 1.25; padding: 20px 28px; border-radius: 26px; box-shadow: 0 3px 0 rgba(0,0,0,.12); }
      .bb .d { color: #0b6b5d; font-family: 'Baloo 2'; font-weight: 800; font-size: 40px; display: block; line-height: 1; margin-bottom: 4px; }
      .bb.me { align-self: flex-start; background: #fff; border-top-left-radius: 6px; }
      .bb.her { align-self: flex-end; background: #d9fdd3; border-top-right-radius: 6px; }
      .bb .tk { color: #34b7f1; font-size: 28px; margin-left: 10px; }
      #waTag { left: 560px; top: 1270px; font-size: 44px; transform: rotate(5deg); z-index: 5; }

      /* H. outils */
      #trois { top: 200px; font-size: 84px; line-height: 1; }
      #mc { left: 60px; top: 360px; width: 480px; height: 700px; transform: rotate(-2deg); }
      #mc .layer { position: absolute; inset: 0; }
      #docs { background: #fff; font-family: 'Work Sans'; }
      #docs .bar { height: 84px; display: flex; align-items: center; gap: 16px; padding: 0 22px; border-bottom: 2px solid #e3e3e3; }
      #docs .ic { width: 40px; height: 52px; border-radius: 5px; background: #4285f4; position: relative; flex: none; }
      #docs .ic i { position: absolute; left: 9px; right: 9px; height: 4px; background: #fff; border-radius: 2px; }
      #docs .fn { font-weight: 400; font-size: 28px; color: #202124; }
      #docs .tb { height: 62px; display: flex; align-items: center; gap: 26px; padding: 0 26px; border-bottom: 2px solid #e3e3e3; background: #f1f4f9; font-size: 30px; color: #444; }
      #docs .tb b, #docs .tb em, #docs .tb u { width: 44px; height: 44px; border-radius: 10px; display: flex; align-items: center; justify-content: center; font-style: normal; }
      #docs .tb em { font-style: italic; font-family: serif; }
      #docs .pg { padding: 30px 30px; color: #202124; }
      #docs .h1 { font-weight: 700; font-size: 34px; line-height: 1.2; min-height: 42px; }
      #docs .p { font-weight: 400; font-size: 25px; line-height: 1.4; margin-top: 10px; min-height: 35px; }
      #docs .h2 { font-weight: 700; font-size: 29px; margin-top: 26px; min-height: 36px; }
      #docs .li { font-weight: 400; font-size: 26px; line-height: 1.5; padding-left: 30px; position: relative; }
      #docs .li::before { content: ""; position: absolute; left: 6px; top: 15px; width: 10px; height: 10px; border-radius: 50%; background: #202124; }
      #docs .c { opacity: 0; }
      #docs .cur { display: inline-block; width: 3px; height: 30px; background: #1a73e8; vertical-align: -5px; }
      .tool { left: 580px; width: 450px; height: 190px; padding: 22px 26px; display: flex; align-items: center; gap: 22px; }
      .tool .nb { width: 96px; height: 96px; border-radius: 50%; background: #ff5c00; color: #fff; border: 5px solid #111; font-size: 64px; flex: none;
                  display: flex; align-items: center; justify-content: center; padding-top: 10px; }
      .tool .tx { font-size: 50px; line-height: 1; }
      .tool .tx small { display: block; font-family: 'Work Sans'; font-weight: 700; font-size: 28px; color: #555; margin-top: 10px; line-height: 1.15; }
      #tl1 { top: 380px; } #tl2 { top: 620px; } #tl3 { top: 860px; }

      /* I. boucle */
      #cuis { left: 70px; top: 610px; width: 940px; height: 627px; transform: rotate(-2deg); }
      #how { left: 250px; top: 1200px; font-size: 60px; transform: rotate(-3deg); z-index: 5; }

      /* J. CTA */
      #cbLab { top: 250px; font-size: 100px; line-height: 1.02; }
      #cbox { left: 70px; top: 520px; width: 940px; height: 170px; display: flex; align-items: center; gap: 26px; padding: 0 30px; }
      #cbox .av { width: 100px; height: 100px; border-radius: 50%; background: #ffd60a; border: 5px solid #111; flex: none; }
      #cbox .in { flex: 1; height: 100px; border-radius: 50px; background: #f1ede6; display: flex; align-items: center; padding: 8px 34px 0; font-size: 64px; }
      #cbox .in span { opacity: 0; }
      #cbox .send { width: 100px; height: 100px; border-radius: 50%; background: #ff5c00; border: 5px solid #111; flex: none; display: flex; align-items: center; justify-content: center; }
      #cbox .send svg { width: 50px; height: 50px; }
      #prive { left: 170px; top: 770px; width: 740px; font-size: 58px; }
      #cover { left: 360px; top: 920px; width: 360px; height: 360px; border-radius: 24px; border: 10px solid #fff; overflow: hidden; box-shadow: 0 30px 70px rgba(60,30,0,0.32); }
      #cover img { width: 100%; height: 100%; display: block; }
      #rev { left: 110px; top: 1290px; width: 860px; font-size: 54px; z-index: 5; }

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
      <div class="serie">JOUR 1 · CUISINE</div>

      <!-- A. HOOK -->
      <div class="ab photo" id="hookW">
        <video id="vHook" class="clip" src="assets/video/mains_hook.mp4" data-start="0" data-duration="4.4" data-track-index="0" muted playsinline></video>
      </div>
      <div class="ab pill k" id="q">Tu sais cuisiner ?</div>
      <div class="ab pill y" id="prod">= un produit qui se vend</div>

      <!-- B. PROMESSE -->
      <div class="ab center" id="b1">Je te montre</div>
      <div class="ab center" id="b2">avec <span class="hl">1 exemple</span><br />précis</div>
      <div class="ab pill" id="b3">Regarde bien</div>

      <!-- C. NADINE -->
      <div class="ab photo" id="nad"><img src="assets/img/nadine_floutee.jpg" /></div>
      <div class="ab card" id="idc"><div class="n">Nadine</div><div class="l" id="l1"><span>›</span> 24 ans</div><div class="l" id="l2"><span>›</span> étudiante</div></div>
      <div class="ab pill y" id="mince">Se trouve trop mince</div>
      <div class="ab pill k" id="souf">Elle en souffre</div>

      <!-- D. MARCHÉ -->
      <div class="ab pill" id="goal">Prendre du poids sainement</div>
      <div class="ab photo" id="mar"><img src="assets/img/marche.jpg" style="object-position:center 60%" /></div>
      <div class="ab pill w" id="qq1">Quoi manger ?</div>
      <div class="ab pill y" id="qq2">Combien ?</div>

      <!-- E. ET TOI -->
      <div class="ab center" id="toiT">Et <span class="hl">toi</span> ?</div>
      <div class="ab photo" id="toiW">
        <video id="vToi" class="clip" src="assets/video/mains_toi.mp4" data-start="__TOI_START__" data-duration="3.3" data-track-index="1" muted playsinline></video>
      </div>
      <div class="ab pill k" id="repP">Tu as la réponse</div>

      <!-- F. LIVRE -->
      <div class="ab plate" id="p1"><img src="assets/img/plat_riz.jpg" /></div>
      <div class="ab plate" id="p2"><img src="assets/img/plat_moamba.jpg" /></div>
      <div class="ab" id="book">
        <div class="ph"><img src="assets/img/plat_gombo.jpg" style="object-position:center 40%" /></div>
        <div class="spine"></div>
        <div class="txt"><div class="kick">LIVRE DE RECETTES</div>
        <div class="tt">Prendre du poids <span class="hl">sainement</span></div>
        <div class="ft">avec les aliments du marché</div></div>
        <div id="stamp" data-layout-allow-overlap>VENDU</div>
      </div>
      <div class="ab card" id="plan4">
        <div class="h">Plan de repas · 4 semaines</div>
        <div class="row">
          <div class="wk" id="w1">SEM. 1<small>7 jours</small><div class="ok"><svg viewBox="0 0 24 24"><path d="M6 12.5l4 4 8-9" fill="none" stroke="#fff" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"/></svg></div></div>
          <div class="wk" id="w2">SEM. 2<small>7 jours</small><div class="ok"><svg viewBox="0 0 24 24"><path d="M6 12.5l4 4 8-9" fill="none" stroke="#fff" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"/></svg></div></div>
          <div class="wk" id="w3">SEM. 3<small>7 jours</small><div class="ok"><svg viewBox="0 0 24 24"><path d="M6 12.5l4 4 8-9" fill="none" stroke="#fff" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"/></svg></div></div>
          <div class="wk" id="w4">SEM. 4<small>7 jours</small><div class="ok"><svg viewBox="0 0 24 24"><path d="M6 12.5l4 4 8-9" fill="none" stroke="#fff" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"/></svg></div></div>
        </div>
      </div>
      <div class="ab pill y" id="crs">+ liste de courses</div>

      <!-- G. WHATSAPP -->
      <div class="ab" id="wa">
        <div class="top"><div class="av"><img src="assets/img/marche.jpg" /></div><div><div class="nm">Défi 30 jours · Cuisine</div><div class="st">Groupe WhatsApp</div></div></div>
        <div class="body">
          <div class="bb me" id="m1"><span class="d">Jour 1</span>Riz à la viande, la recette complète</div>
          <div class="bb her" id="m2">C'est fait ! <span class="tk">✓✓</span></div>
          <div class="bb me" id="m3"><span class="d">Jour 2</span>Soupe de gombo</div>
          <div class="bb her" id="m4">Fait aussi, merci ! <span class="tk">✓✓</span></div>
          <div class="bb me" id="m5"><span class="d">Jour 3</span>Poulet moamba</div>
        </div>
      </div>
      <div class="ab pill" id="waTag">1 recette / jour</div>

      <!-- H. OUTILS -->
      <div class="ab center" id="trois">Il te faut <span class="hl">3 choses</span></div>
      <div class="ab photo" id="mc">
        <video id="vCanva" class="clip" src="assets/video/canva.mp4" data-start="__CANVA_START__" data-duration="8.4" data-track-index="2" muted playsinline></video>
        <img class="layer" id="mtel" src="assets/img/mains_telephone.jpg" style="object-position:center 55%" />
        <div class="layer" id="docs">
          <div class="bar"><div class="ic"><i style="top:14px"></i><i style="top:23px"></i><i style="top:32px"></i></div><div class="fn">Recettes de Nadine</div></div>
          <div class="tb"><b id="bB">B</b><em>I</em><u>U</u><span>☰</span></div>
          <div class="pg">
            <div class="h1" data-type="h1">Haricots au poisson</div>
            <div class="p" data-type="p">Cuire les haricots, ajouter le poisson et les oignons.</div>
            <div class="h2" data-type="h2">Liste de courses</div>
            <div class="li" data-type="li">Haricots</div>
            <div class="li" data-type="li">Poisson</div>
            <div class="li" data-type="li">Oignons</div>
            <div class="li" data-type="li">Sel</div>
          </div>
        </div>
      </div>
      <div class="ab card tool" id="tl1"><div class="nb">1</div><div class="tx">Canva<small>mettre le livre en page</small></div></div>
      <div class="ab card tool" id="tl2"><div class="nb">2</div><div class="tx">Téléphone<small>photographier tes plats</small></div></div>
      <div class="ab card tool" id="tl3"><div class="nb">3</div><div class="tx">Google Docs<small>recettes et courses</small></div></div>

      <!-- I. BOUCLE -->
      <div class="ab photo" id="cuis"><img src="assets/img/cuisiniere.jpg" style="object-position:center 30%" /></div>
      <div class="ab pill k" id="how">« Comment tu as fait ? »</div>

      <!-- J. CTA -->
      <div class="ab center" id="cbLab">Commente<br /><span class="hl">ta compétence</span></div>
      <div class="ab card" id="cbox"><div class="av"></div><div class="in"><span>C</span><span>U</span><span>I</span><span>S</span><span>I</span><span>N</span><span>E</span></div>
        <div class="send"><svg viewBox="0 0 24 24" fill="#fff"><path d="M3 20.5 21 12 3 3.5l3 8.5-3 8.5Zm3-8.5h9"/></svg></div></div>
      <div class="ab pill k" id="prive">Je te réponds en privé</div>
      <div class="ab" id="cover"><img src="assets/img/ebook_cover.png" /></div>
      <div class="ab pill y" id="rev">Ta compétence → un revenu</div>

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
      const HIDE = ["#hookW","#q","#prod","#b1","#b2","#b3","#nad","#idc","#l1","#l2","#mince","#souf","#goal","#mar","#qq1","#qq2",
              "#toiT","#toiW","#repP","#p1","#p2","#book","#stamp","#plan4","#crs","#wa","#m1","#m2","#m3","#m4","#m5","#waTag",
              "#trois","#mc","#mtel","#docs","#tl1","#tl2","#tl3","#cuis","#how","#cbLab","#cbox","#prive","#cover","#rev",
              "#s1","#s2","#s3","#s4","#flash","#w1","#w2","#w3","#w4"];
      gsap.set(HIDE, { autoAlpha: 0 });
      gsap.set("#plan4 .ok", { scale: 0 });
      tl.fromTo("#progress", { scaleX: 0 }, { scaleX: 1, duration: __DUR__, ease: "none" }, 0);
      const flash = (at) => { tl.set("#flash", { autoAlpha: 0.85 }, at); tl.to("#flash", { autoAlpha: 0, duration: 0.22 }, at + 0.04); };
      const sparks = (at) => ["#s1","#s2","#s3","#s4"].forEach((s, i) =>
        IN(s, { autoAlpha: 1, scale: 0, rotation: -90 }, { scale: 1, rotation: 0, duration: 0.35, ease: "back.out(2.5)" }, at + i * 0.1));
      const sparksOut = (at) => OUT(["#s1","#s2","#s3","#s4"], { scale: 0, autoAlpha: 0, duration: 0.2 }, at);
      const pop = (sel, at, rot = 0) => IN(sel, { autoAlpha: 1, scale: 0, rotation: rot + 12 }, { scale: 1, rotation: rot, duration: 0.4, ease: "back.out(2.2)" }, at);
      const card = (sel, at, rot, fromY = 900) => IN(sel, { autoAlpha: 1, y: fromY, rotation: rot + 10 }, { y: 0, rotation: rot, duration: 0.55, ease: "back.out(1.3)" }, at);
      const leave = (sels, at) => OUT(sels, { autoAlpha: 0, y: -80, duration: 0.3, ease: "power2.in" }, at);

      // ---------- A. HOOK ----------
      card("#hookW", 0.02, -2);
      pop("#q", 0.2, -2);
      pop("#prod", T.produit - 0.1, 2);
      sparks(T.vend + 0.1);
      OUT("#hookW", { x: -1000, rotation: -18, autoAlpha: 0, duration: 0.4, ease: "power3.in" }, T.montre - 0.4);
      OUT(["#q", "#prod"], { x: 1000, rotation: 12, autoAlpha: 0, duration: 0.4, ease: "power3.in" }, T.montre - 0.4);
      sparksOut(T.montre - 0.4);

      // ---------- B. PROMESSE ----------
      IN("#b1", { autoAlpha: 1, scale: 2.4 }, { scale: 1, duration: 0.32, ease: "power4.in" }, T.montre);
      IN("#b2", { autoAlpha: 1, y: 80 }, { y: 0, duration: 0.4, ease: "back.out(2)" }, T.exemple - 0.35);
      pop("#b3", T.exemple + 0.6, -3);
      leave(["#b1", "#b2", "#b3"], T.nadine - 0.35);

      // ---------- C. NADINE ----------
      card("#nad", T.nadine - 0.1, -3);
      tl.to("#nad img", { scale: 1.06, duration: 8, ease: "sine.inOut" }, T.nadine);
      IN("#idc", { autoAlpha: 1, x: 500, rotation: 12 }, { x: 0, rotation: 2, duration: 0.5, ease: "back.out(1.5)" }, T.nadine + 0.2);
      IN("#l1", { autoAlpha: 1, x: 40 }, { x: 0, duration: 0.3, ease: "power3.out" }, T.age);
      IN("#l2", { autoAlpha: 1, x: 40 }, { x: 0, duration: 0.3, ease: "power3.out" }, T.etud);
      pop("#mince", T.mince - 0.15, -3);
      pop("#souf", T.souffre - 0.1, 2);
      tl.to("#souf", { x: -8, duration: 0.06, yoyo: true, repeat: 5, ease: "none" }, T.souffre + 0.35);
      OUT(["#nad"], { x: -900, autoAlpha: 0, duration: 0.4, ease: "power3.in" }, T.poids - 0.4);
      OUT(["#idc", "#mince", "#souf"], { x: 900, autoAlpha: 0, duration: 0.4, ease: "power3.in" }, T.poids - 0.4);

      // ---------- D. MARCHÉ ----------
      IN("#goal", { autoAlpha: 1, y: -200 }, { y: 0, duration: 0.45, ease: "back.out(1.6)" }, T.poids);
      card("#mar", T.marche - 0.15, 2);
      tl.fromTo("#mar img", { scale: 1.18 }, { scale: 1.0, duration: 5, ease: "sine.out" }, T.marche - 0.15);
      pop("#qq1", T.quoi - 0.1, -5);
      pop("#qq2", T.quant - 0.1, 4);
      leave(["#goal", "#mar", "#qq1", "#qq2"], T.toi - 0.35);

      // ---------- E. ET TOI ----------
      flash(T.toi - 0.05);
      IN("#toiT", { autoAlpha: 1, scale: 2.6 }, { scale: 1, duration: 0.3, ease: "power4.in" }, T.toi);
      card("#toiW", T.toi + 0.15, 2, 700);
      pop("#repP", T.rep - 0.1, -2);
      sparks(T.rep);
      sparksOut(T.livre - 0.35);
      leave(["#toiT", "#toiW", "#repP"], T.livre - 0.35);

      // ---------- F. LIVRE ----------
      IN("#book", { autoAlpha: 1, y: 900, rotationY: 50, transformPerspective: 1400 }, { y: 0, rotationY: 0, rotation: -4, duration: 0.6, ease: "power3.out" }, T.livre - 0.1);
      IN("#p1", { autoAlpha: 1, scale: 0, rotation: 90 }, { scale: 1, rotation: 0, duration: 0.45, ease: "back.out(1.8)" }, T.recettes - 0.1);
      IN("#p2", { autoAlpha: 1, scale: 0, rotation: -90 }, { scale: 1, rotation: 0, duration: 0.45, ease: "back.out(1.8)" }, T.recettes + 0.25);
      IN("#plan4", { autoAlpha: 1, y: 400 }, { y: 0, duration: 0.5, ease: "back.out(1.4)" }, T.plan - 0.15);
      ["#w1", "#w2", "#w3", "#w4"].forEach((w, i) => IN(w, { scale: 0.4, autoAlpha: 0 }, { scale: 1, autoAlpha: 1, duration: 0.3, ease: "back.out(2)" }, T.plan + 0.15 + i * 0.12));
      tl.to("#w1, #w2, #w3, #w4", { backgroundColor: "#ffd60a", duration: 0.2, stagger: 0.08 }, T.sem - 0.1);
      pop("#crs", T.courses - 0.15, 4);
      tl.fromTo("#plan4 .ok", { scale: 0 }, { scale: 1, duration: 0.3, ease: "back.out(3)", stagger: 0.15, immediateRender: false }, T.chaque - 0.1);
      sparks(T.chaque);
      sparksOut(T.defi - 0.35);
      leave(["#book", "#p1", "#p2", "#plan4", "#crs"], T.defi - 0.35);

      // ---------- G. WHATSAPP ----------
      IN("#wa", { autoAlpha: 1, y: 1200 }, { y: 0, duration: 0.55, ease: "power3.out" }, T.defi - 0.05);
      pop("#waTag", T.wa - 0.1, 5);
      [["#m1", 0.4], ["#m2", 0.9], ["#m3", 1.3], ["#m4", 1.75], ["#m5", 2.1]].forEach(([m, d]) =>
        IN(m, { autoAlpha: 1, y: 40, scale: 0.85 }, { y: 0, scale: 1, duration: 0.3, ease: "back.out(2)" }, T.defi + d));
      leave(["#wa", "#waTag"], T.tools - 0.35);

      // ---------- H. OUTILS ----------
      IN("#trois", { autoAlpha: 1, scale: 2 }, { scale: 1, duration: 0.32, ease: "power4.in" }, T.tools - 0.05);
      card("#mc", T.tools + 0.1, -2);
      pop("#tl1", T.canva - 0.1, 0);
      IN("#mtel", { x: 520 }, { x: 0, duration: 0.4, ease: "power3.out" }, T.tel - 0.15);
      pop("#tl2", T.tel - 0.1, 0);
      tl.to("#tl1", { autoAlpha: 0.45, scale: 0.94, duration: 0.25 }, T.tel - 0.1);
      IN("#docs", { x: 520 }, { x: 0, duration: 0.4, ease: "power3.out" }, T.docs - 0.15);
      pop("#tl3", T.docs - 0.1, 0);
      tl.to("#tl2", { autoAlpha: 0.45, scale: 0.94, duration: 0.25 }, T.docs - 0.1);
      // saisie Google Docs
      (() => {
        const lines = [...document.querySelectorAll("#docs .pg > div")];
        const cursor = document.createElement("span");
        cursor.className = "cur";
        const chars = [];
        lines.forEach((ln) => {
          const txt = ln.textContent;
          ln.textContent = "";
          [...txt].forEach((ch) => { const s = document.createElement("span"); s.className = "c"; s.textContent = ch; ln.appendChild(s); chars.push(s); });
        });
        const n1 = lines[0].children.length + lines[1].children.length;
        const t0 = T.docs + 0.35, t1 = T.courses2 - 0.2, t2 = T.boucle - 0.5;
        chars.forEach((c, i) => {
          const at = i < n1 ? t0 + (t1 - t0) * i / n1 : t1 + (t2 - t1) * (i - n1) / (chars.length - n1);
          tl.set(c, { opacity: 1 }, at);
        });
        tl.to("#bB", { backgroundColor: "#d2e3fc", duration: 0.1, yoyo: true, repeat: 1 }, t0 - 0.2);
      })();
      tl.to("#tl3", { scale: 1.05, duration: 0.3, yoyo: true, repeat: 1, ease: "sine.inOut" }, T.courses2);
      leave(["#trois", "#mc", "#tl1", "#tl2", "#tl3"], T.boucle - 0.35);

      // ---------- I. BOUCLE ----------
      tl.set("#book", { x: 440, y: -210, scale: 0.6, rotation: 6, rotationY: 0, zIndex: 6 }, T.boucle - 0.3);
      IN("#book", { y: -450 }, { y: -210, duration: 0.45, ease: "back.out(1.5)" }, T.boucle - 0.1);
      IN("#stamp", { autoAlpha: 1, scale: 3, rotation: -30 }, { scale: 1, rotation: -14, duration: 0.25, ease: "power4.in" }, T.vendra - 0.05);
      card("#cuis", T.cuisinieres - 0.2, -2);
      pop("#how", T.comment - 0.1, -3);
      leave(["#book", "#cuis", "#how"], T.cta - 0.3);

      // ---------- J. CTA ----------
      flash(T.cta - 0.05);
      IN("#cbLab", { autoAlpha: 1, scale: 2.2 }, { scale: 1, duration: 0.3, ease: "power4.in" }, T.cta);
      IN("#cbox", { autoAlpha: 1, y: 300 }, { y: 0, duration: 0.45, ease: "back.out(1.6)" }, T.cta + 0.25);
      document.querySelectorAll("#cbox .in span").forEach((s, i) => tl.set(s, { opacity: 1 }, T.cta + 0.6 + i * 0.13));
      tl.to("#cbox .send", { scale: 1.2, duration: 0.3, yoyo: true, repeat: 3, ease: "sine.inOut" }, T.cta + 1.5);
      pop("#prive", T.prive - 0.15, -2);
      IN("#cover", { autoAlpha: 1, y: 500, rotationY: 60, transformPerspective: 1400 }, { y: 0, rotationY: -8, duration: 0.55, ease: "power3.out" }, T.guide - 0.1);
      tl.to("#cover", { rotationY: 8, duration: 3, ease: "sine.inOut" }, T.guide + 0.5);
      pop("#rev", T.revenu - 0.2, -2);
      sparks(T.revenu);

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
        tl.fromTo(box, { autoAlpha: 0, y: 20 }, { autoAlpha: 1, y: 0, duration: 0.14, ease: "power2.out" }, Math.max(0, c.start - 0.08));
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
