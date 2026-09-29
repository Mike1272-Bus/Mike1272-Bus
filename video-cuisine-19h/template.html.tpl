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
      .photo img { width: 100%; height: 100%; object-fit: cover; display: block; }
      .pill { text-align: center; background: #ff5c00; color: #fff; border-radius: 70px; border: 5px solid #111; box-shadow: 10px 10px 0 #111; white-space: nowrap; padding: 18px 40px 6px; }
      .pill.y { background: #ffd60a; color: #111; }
      .pill.k { background: #111; color: #fff; box-shadow: 10px 10px 0 #ff5c00; }
      .pill.w { background: #fff; color: #111; }
      .hl { background: #ffd60a; color: #c94200; border-radius: 18px; padding: 0 14px; }
      .spark { position: absolute; width: 70px; height: 70px; z-index: 15; }
      .spark svg { width: 100%; height: 100%; fill: #111; }
      .center { left: 0; width: 1080px; text-align: center; }
      .nb { width: 110px; height: 110px; border-radius: 50%; background: #ff5c00; color: #fff; border: 5px solid #111; font-size: 76px; flex: none;
            display: flex; align-items: center; justify-content: center; padding-top: 12px; }

      /* A. hook */
      #t1 { top: 440px; font-size: 88px; line-height: 1.08; }
      #t2 { top: 190px; font-size: 64px; line-height: 1; }
      #t3 { top: 300px; font-size: 124px; line-height: 1; color: #ff5c00; }
      #crowd { left: 120px; top: 540px; width: 840px; height: 520px; display: grid; grid-template-columns: repeat(6, 1fr); grid-template-rows: repeat(4, 1fr); }
      .pp { display: flex; align-items: center; justify-content: center; color: #111; }
      .pp svg { width: 104px; height: 118px; }
      #none { left: 170px; top: 1130px; width: 740px; font-size: 66px; }

      /* B. promesse */
      #b1 { top: 280px; font-size: 92px; line-height: 1; }
      .row { left: 110px; width: 860px; height: 220px; display: flex; align-items: center; gap: 34px; padding: 0 40px; }
      .row .tx { font-size: 62px; line-height: 1.02; }
      #b2 { top: 500px; } #b3 { top: 790px; }

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
      .post .im { height: 290px; border-radius: 16px; overflow: hidden; margin-top: 18px; background: #cfd4da; }
      .post .im img { width: 100%; height: 100%; object-fit: cover; }
      .post .tt { font-size: 38px; line-height: 1.1; margin-top: 16px; }
      .post .who { font-family: 'Work Sans'; font-weight: 700; font-size: 26px; }
      .post .rx { font-family: 'Work Sans'; font-weight: 700; font-size: 24px; color: #5f6570; margin-top: 14px; }
      #pA { outline: 0 solid #ff5c00; }
      #c0 { left: 700px; top: 760px; font-size: 50px; transform: rotate(5deg); z-index: 5; }
      #c1 { left: 40px; top: 360px; font-size: 52px; transform: rotate(-4deg); z-index: 5; }
      #c2 { left: 120px; top: 1080px; font-size: 52px; transform: rotate(3deg); z-index: 5; }
      #c2 .x, #d1 .x { color: #e0161a; }

      /* D. une phrase */
      #d2 { top: 300px; font-size: 86px; line-height: 1; }
      #d1 { left: 90px; top: 520px; width: 900px; height: 250px; display: flex; align-items: center; justify-content: center; font-size: 78px; }
      #strike { position: absolute; left: 60px; right: 60px; top: 112px; height: 16px; background: #e0161a; border-radius: 8px; transform-origin: left center; }
      #d3 { left: 390px; top: 830px; width: 300px; height: 300px; }
      #d3 svg { width: 100%; height: 100%; }

      /* E. publication ciblée */
      #postB { left: 400px; top: 200px; width: 630px; height: 840px; background: #fff; border: 5px solid #111; border-radius: 36px; box-shadow: 14px 14px 0 #111; padding: 26px; z-index: 2; }
      #postB .av { background: #ff5c00; }
      #postB .tt { font-size: 50px; line-height: 1.22; margin-top: 18px; }
      #postB .mk { border-radius: 12px; padding: 0 8px; }
      #postB .im { height: 340px; margin-top: 22px; }
      #nadB { left: 50px; top: 560px; width: 390px; height: 693px; transform: rotate(-4deg); z-index: 3; }
      #stop { left: 150px; top: 440px; width: 200px; height: 200px; z-index: 6; }
      #stop svg { width: 100%; height: 100%; }
      #elle { left: 470px; top: 1100px; font-size: 62px; transform: rotate(-3deg); z-index: 6; }

      /* F. différence */
      #f1 { top: 280px; font-size: 90px; line-height: 1; }
      #bars { left: 90px; top: 490px; width: 900px; height: 600px; padding: 44px 40px; }
      #bars .h { font-size: 50px; line-height: 1; }
      #bars .lb { font-family: 'Work Sans'; font-weight: 700; font-size: 34px; margin-top: 44px; line-height: 1.2; }
      #bars .tr { height: 90px; border: 5px solid #111; border-radius: 24px; background: #f1ede6; margin-top: 14px; overflow: hidden; }
      #bars .fl { height: 100%; transform-origin: left center; border-right: 5px solid #111; }

      /* G. question */
      .step { left: 120px; width: 840px; height: 180px; display: flex; align-items: center; gap: 30px; padding: 0 36px; }
      .step .tx { font-size: 58px; line-height: 1; }
      #g1 { top: 250px; } #g2 { top: 560px; } #g3 { top: 870px; }
      .arr { left: 500px; width: 80px; height: 110px; }
      .arr svg { width: 100%; height: 100%; }
      #ar1 { top: 440px; } #ar2 { top: 750px; }
      #q1 { top: 250px; font-size: 76px; line-height: 1; }
      #qc { left: 90px; top: 430px; width: 900px; height: 520px; padding: 46px 50px; }
      #qc .lab { font-family: 'Work Sans'; font-weight: 700; font-size: 36px; line-height: 1.2; color: #ff5c00; letter-spacing: .06em; }
      #qc .big { font-size: 104px; line-height: 1.02; margin-top: 44px; }
      #qc .qm { position: absolute; right: -40px; top: -60px; width: 170px; height: 170px; border-radius: 50%; background: #ff5c00; color: #fff; border: 6px solid #111;
                font-size: 108px; line-height: 1; display: flex; align-items: center; justify-content: center; padding-top: 14px; box-shadow: 10px 10px 0 #111; }

      /* H. boucle */
      #okR { left: 120px; top: 1030px; font-size: 56px; transform: rotate(-2deg); }
      #pay { left: 150px; top: 1200px; font-size: 56px; transform: rotate(2deg); }

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
      <div class="ab center" id="t1">Ce qu'on ne<br />vous dit pas sur<br />les <span class="hl">produits digitaux</span></div>
      <div class="ab center" id="t2">Un produit pour</div>
      <div class="ab center" id="t3">TOUT LE MONDE</div>
      <div class="ab" id="crowd">__CROWD__</div>
      <div class="ab pill k" id="none">= Personne ne l'achète</div>

      <!-- B. PROMESSE -->
      <div class="ab center" id="b1">Je vous montre <span class="hl">pourquoi</span></div>
      <div class="ab card row" id="b2"><div class="nb">1</div><div class="tx">exemple<br />tout simple</div></div>
      <div class="ab card row" id="b3"><div class="nb">?</div><div class="tx">1 seule question<br />à vous poser</div></div>

      <!-- C. FIL D'ACTUALITÉ -->
      <div class="ab" id="phone"><div id="scr">
        <div class="bar" data-layout-allow-overlap data-layout-allow-occlusion>Fil d'actualité</div>
        <div id="col">
          <div class="post"><div class="hd"><div class="av"></div><div class="nm"></div></div><div class="ln" style="width:90%"></div><div class="ln" style="width:60%"></div><div class="im"><img src="assets/img/marche.jpg" /></div></div>
          <div class="post" id="pA"><div class="hd"><div class="av" style="background:#ff5c00">V</div><div class="who">Votre page</div></div>
            <div class="tt">Mes recettes de cuisine</div><div class="im"><img src="assets/img/plat_riz.jpg" /></div><div class="rx">0 j'aime · 0 commentaire</div></div>
          <div class="post"><div class="hd"><div class="av"></div><div class="nm" style="width:140px"></div></div><div class="ln" style="width:80%"></div><div class="im"><img src="assets/img/plat_moamba.jpg" /></div></div>
          <div class="post"><div class="hd"><div class="av"></div><div class="nm"></div></div><div class="ln" style="width:95%"></div><div class="ln" style="width:85%"></div><div class="ln" style="width:40%"></div></div>
          <div class="post"><div class="hd"><div class="av"></div><div class="nm" style="width:210px"></div></div><div class="ln" style="width:70%"></div><div class="im" style="background:#e3d6c6"></div></div>
          <div class="post"><div class="hd"><div class="av"></div><div class="nm"></div></div><div class="ln" style="width:90%"></div><div class="ln" style="width:50%"></div><div class="im" style="background:#d6dce3"></div></div>
        </div>
      </div></div>
      <div class="ab pill y" id="c0">0 réaction</div>
      <div class="ab pill w" id="c1">Tout le monde mange</div>
      <div class="ab pill w" id="c2">« C'est pour moi » ? <span class="x">✗</span></div>

      <!-- D. UNE PHRASE -->
      <div class="ab center" id="d2">On change <span class="hl">une phrase</span></div>
      <div class="ab card" id="d1">Mes recettes de cuisine<div id="strike"></div></div>
      <div class="ab" id="d3"><svg viewBox="0 0 100 100"><path d="M50 8 V78 M24 54 L50 82 L76 54" fill="none" stroke="#ff5c00" stroke-width="12" stroke-linecap="round" stroke-linejoin="round"/></svg></div>

      <!-- E. PUBLICATION CIBLÉE -->
      <div class="ab" id="postB">
        <div class="post" style="margin:0;padding:0">
          <div class="hd"><div class="av">V</div><div class="who">Votre page</div></div>
          <div class="tt">Des recettes pour <span class="mk" id="mkF" data-layout-allow-overlap>les femmes</span> qui veulent <span class="mk" id="mkS">prendre du poids sainement</span></div>
          <div class="im"><img src="assets/img/plat_gombo.jpg" style="object-position:center 40%" /></div>
        </div>
      </div>
      <div class="ab photo" id="nadB"><img src="assets/img/nadine_floutee.jpg" /></div>
      <div class="ab" id="stop"><svg viewBox="0 0 100 100"><polygon points="30,3 70,3 97,30 97,70 70,97 30,97 3,70 3,30" fill="#e0161a" stroke="#111" stroke-width="5"/><text x="50" y="63" text-anchor="middle" font-family="Baloo 2" font-weight="800" font-size="30" fill="#fff">STOP</text></svg></div>
      <div class="ab pill k" id="elle">On parle d'elle</div>

      <!-- F. DIFFÉRENCE -->
      <div class="ab center" id="f1">Au moment de <span class="hl">vendre</span></div>
      <div class="ab card" id="bars">
        <div class="h">Qui a envie d'acheter ?</div>
        <div class="lb">« Mes recettes de cuisine »</div>
        <div class="tr"><div class="fl" id="fl1" style="width:16%;background:#bdb6ab"></div></div>
        <div class="lb">« Recettes pour prendre du poids sainement »</div>
        <div class="tr"><div class="fl" id="fl2" style="width:88%;background:#ff5c00"></div></div>
      </div>

      <!-- G. QUESTION -->
      <div class="ab card step" id="g1"><div class="nb">1</div><div class="tx">Une personne<br />précise</div></div>
      <div class="ab arr" id="ar1"><svg viewBox="0 0 80 110"><path d="M40 6 V86 M14 62 L40 94 L66 62" fill="none" stroke="#111" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/></svg></div>
      <div class="ab card step" id="g2"><div class="nb">2</div><div class="tx">Elle se sent<br />concernée</div></div>
      <div class="ab arr" id="ar2"><svg viewBox="0 0 80 110"><path d="M40 6 V86 M14 62 L40 94 L66 62" fill="none" stroke="#111" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/></svg></div>
      <div class="ab pill step" id="g3" style="border-radius:36px"><div class="nb" style="background:#fff;color:#ff5c00">3</div><div class="tx">Elle a envie<br />d'acheter</div></div>
      <div class="ab center" id="q1">Avant de créer <span class="hl">votre produit</span></div>
      <div class="ab card" id="qc"><div class="lab">LA SEULE QUESTION</div><div class="big">À qui <span class="hl">exactement</span><br />je le vends ?</div><div class="qm">?</div></div>

      <!-- H. BOUCLE -->
      <div class="ab pill y" id="okR">✓ Vous avez la réponse</div>
      <div class="ab pill k" id="pay">Sont-elles prêtes à payer ?</div>

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
      const HIDE = ["#t1","#t2","#t3","#crowd","#none","#b1","#b2","#b3","#phone","#c0","#c1","#c2","#d1","#d2","#d3",
              "#postB","#nadB","#stop","#elle","#f1","#bars","#g1","#g2","#g3","#ar1","#ar2","#q1","#qc","#okR","#pay",
              "#cover","#plan","#zero","#cbLab","#cbox","#acc","#s1","#s2","#s3","#s4","#flash"];
      gsap.set(HIDE, { autoAlpha: 0 });
      gsap.set(".pp", { autoAlpha: 0 });
      gsap.set("#strike", { scaleX: 0 });
      gsap.set(["#fl1", "#fl2"], { scaleX: 0 });
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
      leave(["#t1"], 3.1);
      IN("#t2", { y: -60 }, { y: 0, duration: 0.35, ease: "power3.out" }, 3.35);
      slam("#t3", T.tlm - 0.3);
      tl.set("#crowd", { autoAlpha: 1 }, T.tlm - 0.35);
      IN(".pp", { scale: 0 }, { scale: 1, duration: 0.3, ease: "back.out(2.5)", stagger: { each: 0.03, from: "center", grid: [4, 6] } }, T.tlm - 0.3);
      sparks(T.tlm);
      tl.to(".pp", { color: "#c9c2b8", y: 18, duration: 0.25, stagger: { each: 0.02, from: "random" } }, T.personne - 0.1);
      tl.to("#t3", { color: "#bdb6ab", duration: 0.3 }, T.personne);
      pop("#none", T.personne, -3);
      sparksOut(T.personne);
      leave(["#t2", "#t3", "#crowd", "#none"], T.montrer - 0.35);

      // ---------- B. PROMESSE ----------
      IN("#b1", { y: 60 }, { y: 0, duration: 0.4, ease: "back.out(2)" }, T.montrer);
      IN("#b2", { x: -1000, rotation: -8 }, { x: 0, rotation: -1, duration: 0.5, ease: "back.out(1.4)" }, T.exemple - 0.15);
      IN("#b3", { x: 1000, rotation: 8 }, { x: 0, rotation: 1, duration: 0.5, ease: "back.out(1.4)" }, T.question - 0.15);
      tl.to("#b3 .nb", { rotation: 360, duration: 0.6, ease: "back.out(1.5)" }, T.question + 0.4);
      leave(["#b1", "#b2", "#b3"], T.dites - 0.35);

      // ---------- C. FIL D'ACTUALITÉ ----------
      rise("#phone", T.dites - 0.15);
      tl.fromTo("#col", { y: 0 }, { y: -2150, duration: T.maintenant - T.dites, ease: "none" }, T.dites);
      tl.to("#pA", { outlineWidth: 6, duration: 0.2 }, T.mes);
      tl.to("#pA", { outlineWidth: 0, duration: 0.3 }, T.concerne + 0.8);
      pop("#c0", T.concerne - 0.1, 5);
      pop("#c1", T.mange - 0.25, -4);
      pop("#c2", T.moi - 0.1, 3);
      tl.to("#c2 .x", { scale: 1.5, duration: 0.15, yoyo: true, repeat: 1 }, T.moi + 0.35);
      leave(["#phone", "#c0", "#c1", "#c2"], T.maintenant - 0.35);

      // ---------- D. UNE PHRASE ----------
      IN("#d2", { y: 60 }, { y: 0, duration: 0.4, ease: "back.out(2)" }, T.maintenant);
      pop("#d1", T.maintenant + 0.4, -1);
      tl.to("#strike", { scaleX: 1, duration: 0.35, ease: "power3.out" }, T.phrase - 0.1);
      IN("#d3", { y: -40 }, { y: 0, duration: 0.4, ease: "back.out(2)" }, T.phrase + 0.3);
      tl.to("#d3", { y: 30, duration: 0.4, yoyo: true, repeat: 1, ease: "sine.inOut" }, T.phrase + 0.7);
      leave(["#d1", "#d2", "#d3"], T.plutot - 0.3);

      // ---------- E. PUBLICATION CIBLÉE ----------
      IN("#postB", { x: 900, rotation: 10 }, { x: 0, rotation: 2, duration: 0.55, ease: "back.out(1.3)" }, T.postB - 0.3);
      tl.to("#mkF", { backgroundColor: "#ffd60a", duration: 0.2 }, T.femmes);
      tl.to("#mkS", { backgroundColor: "#ffd60a", duration: 0.2 }, T.sainement - 0.5);
      sparks(T.sainement);
      sparksOut(T.nadine);
      IN("#nadB", { x: -700, rotation: -14 }, { x: 0, rotation: -4, duration: 0.5, ease: "back.out(1.3)" }, T.nadine - 0.15);
      tl.to("#postB", { y: -60, duration: T.arrete - T.defiler, ease: "none" }, T.defiler);
      tl.to("#postB", { y: -40, duration: 0.25, ease: "back.out(3)" }, T.arrete);
      IN("#stop", { scale: 3, rotation: -40 }, { scale: 1, rotation: -8, duration: 0.3, ease: "power4.in" }, T.arrete - 0.05);
      pop("#elle", T.delle - 0.1, -3);
      leave(["#postB", "#nadB", "#stop", "#elle"], T.changement - 0.35);

      // ---------- F. DIFFÉRENCE ----------
      IN("#f1", { y: 60 }, { y: 0, duration: 0.4, ease: "back.out(2)" }, T.changement);
      rise("#bars", T.changement + 0.3, -1);
      tl.to("#fl1", { scaleX: 1, duration: 0.5, ease: "power3.out" }, T.difference - 0.4);
      tl.to("#fl2", { scaleX: 1, duration: 0.8, ease: "power3.out" }, T.difference);
      sparks(T.vendre);
      sparksOut(T.precise - 1.0);
      leave(["#f1", "#bars"], T.precise - 1.0);

      // ---------- G. QUESTION ----------
      IN("#g1", { x: -900 }, { x: 0, duration: 0.45, ease: "back.out(1.4)" }, T.precise - 0.6);
      IN("#ar1", { y: -30 }, { y: 0, duration: 0.3 }, T.concernee - 0.4);
      IN("#g2", { x: 900 }, { x: 0, duration: 0.45, ease: "back.out(1.4)" }, T.concernee - 0.3);
      tl.to("#g2", { scale: 1.06, duration: 0.25, yoyo: true, repeat: 1, ease: "sine.inOut" }, T.envie - 1.9);
      IN("#ar2", { y: -30 }, { y: 0, duration: 0.3 }, T.envie - 0.3);
      pop("#g3", T.acheter - 0.25, 0);
      sparks(T.acheter);
      sparksOut(T.alors - 0.3);
      leave(["#g1", "#g2", "#g3", "#ar1", "#ar2"], T.alors - 0.3);
      IN("#q1", { y: 60 }, { y: 0, duration: 0.4, ease: "back.out(2)" }, T.alors);
      rise("#qc", T.question2 - 0.1, -1);
      tl.to("#qc .qm", { rotation: 20, duration: 0.3, yoyo: true, repeat: 3, ease: "sine.inOut" }, T.qui);

      // ---------- H. BOUCLE ----------
      pop("#okR", T.reponse - 0.1, -2);
      pop("#pay", T.payer - 0.3, 2);
      leave(["#q1", "#qc", "#okR", "#pay"], T.cta - 0.35);

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
