<!doctype html>
<html lang="fr" data-resolution="portrait">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1080, height=1920" />
    <script src="assets/gsap.min.js"></script>
    <style>
      @font-face { font-family: 'Baloo 2'; font-weight: 800; src: url('assets/fonts/Baloo2-ExtraBold.ttf') format('truetype'); }
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
      .pill { text-align: center; background: #ff5c00; color: #fff; border-radius: 70px; border: 5px solid #111; box-shadow: 10px 10px 0 #111; white-space: nowrap; }
      .pill.y { background: #ffd60a; color: #111; }
      .pill.k { background: #111; color: #fff; box-shadow: 10px 10px 0 #ff5c00; }
      .hl { background: #ffd60a; color: #c94200; border-radius: 18px; padding: 0 14px; }
      .spark { position: absolute; width: 70px; height: 70px; z-index: 15; }
      .spark svg { width: 100%; height: 100%; fill: #111; }
      .num { width: 170px; height: 170px; border-radius: 50%; background: #ff5c00; color: #fff; border: 6px solid #111; box-shadow: 10px 10px 0 #111;
             display: flex; align-items: center; justify-content: center; font-size: 130px; padding-top: 18px; }
      .vt { font-size: 72px; line-height: 1.02; }

      /* hook */
      #cap { left: 70px; top: 250px; width: 440px; height: 954px; border-radius: 34px; border: 10px solid #fff; overflow: hidden; box-shadow: 0 40px 80px rgba(60,30,0,0.30); }
      #cap img { width: 100%; height: 100%; display: block; }
      #capTag { left: 110px; top: 1150px; font-size: 30px; padding: 12px 26px 4px; }
      #big { left: 470px; top: 470px; width: 560px; padding: 36px 36px 30px; }
      #big .l { font-family: 'Work Sans'; font-size: 30px; color: #666; }
      #big .v { font-size: 80px; line-height: 1; margin-top: 10px; white-space: nowrap; }
      #big .v small { font-size: 40px; color: #ff5c00; }
      #big .c { font-family: 'Work Sans'; font-size: 30px; margin-top: 12px; }
      #gain { left: 540px; top: 860px; font-size: 62px; padding: 20px 44px 8px; }

      /* titre */
      #t3 { left: 0; width: 1080px; top: 480px; text-align: center; font-size: 230px; line-height: .9; }
      #t3 span { color: #ff5c00; }
      #t3s { left: 0; width: 1080px; top: 740px; text-align: center; font-size: 78px; }

      /* vérité 1 */
      #n1, #n2, #n3 { left: 70px; top: 230px; }
      #v1t, #v2t, #v3t { left: 280px; top: 250px; width: 740px; }
      #barLab { left: 90px; top: 640px; font-size: 44px; }
      #bar { left: 90px; top: 710px; width: 900px; height: 170px; display: flex; border: 6px solid #111; border-radius: 26px; overflow: hidden; background: #fff; box-shadow: 12px 12px 0 #111; }
      #bar .b { height: 100%; border-right: 4px solid #111; }
      #bar .b:last-child { border-right: 0; }
      .drop { top: 930px; font-size: 40px; padding: 12px 26px 4px; }
      #reste { left: 90px; top: 950px; width: 900px; text-align: center; font-size: 96px; line-height: 1; }
      #reste small { display: block; font-size: 40px; color: #666; font-family: 'Work Sans'; margin-top: 16px; }

      /* vérité 2 */
      #brut { left: 60px; top: 560px; width: 450px; height: 560px; padding: 40px 34px; text-align: center; transform: rotate(-3deg); }
      #benef { left: 570px; top: 600px; width: 450px; height: 560px; padding: 40px 34px; text-align: center; transform: rotate(3deg); }
      .lab { font-size: 44px; }
      .val { font-size: 76px; line-height: 1; margin-top: 70px; white-space: nowrap; }
      .sub { font-family: 'Work Sans'; font-size: 30px; color: #666; margin-top: 60px; }
      #censor { left: 60px; top: 190px; width: 330px; height: 110px; background: #111; border-radius: 16px; transform-origin: left center; }
      #cache { left: 610px; top: 1000px; font-size: 64px; padding: 16px 40px 6px; transform: rotate(-8deg); }

      /* vérité 3 */
      #tel { left: 70px; top: 470px; width: 480px; height: 660px; border-radius: 34px; border: 10px solid #fff; overflow: hidden; box-shadow: 0 40px 80px rgba(60,30,0,0.30); transform: rotate(-3deg); }
      #tel img { width: 100%; height: 100%; object-fit: cover; display: block; }
      .ch { left: 590px; width: 440px; font-size: 44px; padding: 20px 20px 10px; }
      #ch1 { top: 560px; } #ch2 { top: 740px; } #ch3 { top: 920px; }

      /* CTA */
      #cover { left: 240px; top: 230px; width: 600px; height: 600px; border-radius: 30px; border: 12px solid #fff; overflow: hidden; box-shadow: 0 40px 80px rgba(60,30,0,0.32); }
      #cover img { width: 100%; height: 100%; display: block; }
      #plan { left: 140px; top: 900px; width: 800px; font-size: 64px; padding: 22px 0 10px; }
      #zero { left: 240px; top: 1060px; width: 600px; font-size: 64px; padding: 22px 0 10px; }
      #cbox { left: 70px; top: 520px; width: 940px; height: 170px; display: flex; align-items: center; gap: 26px; padding: 0 30px; }
      #cbox .av { width: 100px; height: 100px; border-radius: 50%; background: #ffd60a; border: 5px solid #111; flex: none; }
      #cbox .in { flex: 1; height: 100px; border-radius: 50px; background: #f1ede6; display: flex; align-items: center; padding: 8px 34px 0; font-size: 64px; }
      #cbox .in span { opacity: 0; }
      #cbox .send { width: 100px; height: 100px; border-radius: 50%; background: #ff5c00; border: 5px solid #111; flex: none; display: flex; align-items: center; justify-content: center; }
      #cbox .send svg { width: 50px; height: 50px; }
      #cbLab { left: 0; width: 1080px; top: 330px; text-align: center; font-size: 92px; line-height: 1; }
      #acc { left: 190px; top: 820px; width: 700px; font-size: 58px; padding: 22px 0 10px; }

      /* sous-titres karaoké */
      #caps { position: absolute; left: 60px; right: 60px; top: 1430px; height: 330px; z-index: 30; }
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
      <div class="serie">LES VÉRITÉS DU LUNDI</div>

      <!-- HOOK -->
      <div class="ab" id="cap"><img src="assets/img/capture_floutee.jpg" /></div>
      <div class="ab pill k" id="capTag">Exemple : un vendeur sur Chariow</div>
      <div class="ab card" id="big"><div class="l">Total des ventes</div><div class="v">12 190 000 <small>FCFA</small></div><div class="c">1 004 clients</div></div>
      <div class="ab pill" id="gain">Gagné : ???</div>

      <!-- TITRE -->
      <div class="ab" id="t3"><span>3</span> VÉRITÉS</div>
      <div class="ab" id="t3s">qu'on ne vous dit <span class="hl">pas</span></div>

      <!-- VÉRITÉ 1 -->
      <div class="ab num" id="n1">1</div>
      <div class="ab vt" id="v1t">Chiffre d'affaires<br /><span class="hl">≠ bénéfice</span></div>
      <div class="ab" id="barLab">100 % des ventes</div>
      <div class="ab" id="bar">
        <div class="b" id="b1" style="width:20%;background:#ff8a3d"></div>
        <div class="b" id="b2" style="width:24%;background:#ffb27a"></div>
        <div class="b" id="b3" style="width:10%;background:#ff8a3d"></div>
        <div class="b" id="b4" style="width:12%;background:#ffb27a"></div>
        <div class="b" id="b5" style="width:14%;background:#ff8a3d"></div>
        <div class="b" id="b6" style="width:20%;background:#ffd60a"></div>
      </div>
      <div class="ab pill y drop" id="d1" style="left:90px">− la pub</div>
      <div class="ab pill y drop" id="d2" style="left:230px">− commissions</div>
      <div class="ab pill y drop" id="d3" style="left:300px">− remboursements</div>
      <div class="ab pill y drop" id="d4" style="left:560px">− frais</div>
      <div class="ab pill y drop" id="d5" style="left:660px">− impôts</div>
      <div class="ab" id="reste">Il reste <span class="hl">10 à 30 %</span><small>souvent, sur un gros lancement (illustration)</small></div>

      <!-- VÉRITÉ 2 -->
      <div class="ab num" id="n2">2</div>
      <div class="ab vt" id="v2t">Ce qu'on<br /><span class="hl">vous montre</span></div>
      <div class="ab card" id="brut"><div class="lab">CHIFFRE BRUT</div><div class="val" style="font-size:66px">12 190 000</div><div class="sub">ce qui fait rêver</div></div>
      <div class="ab card" id="benef"><div class="lab">BÉNÉFICE</div><div class="val">? ? ?</div><div class="sub">ce qu'on garde pour soi</div><div class="ab" id="censor"></div></div>
      <div class="ab pill k" id="cache">CACHÉ</div>

      <!-- VÉRITÉ 3 -->
      <div class="ab num" id="n3">3</div>
      <div class="ab vt" id="v3t">Ce qui vous reste<br /><span class="hl">sur chaque vente</span></div>
      <div class="ab" id="tel"><img src="assets/img/mains_telephone.jpg" style="object-position:center 35%" /></div>
      <div class="ab pill y ch" id="ch1">Créé au téléphone</div>
      <div class="ab pill ch" id="ch2">0 $ de pub</div>
      <div class="ab pill k ch" id="ch3">Frais au plus bas</div>

      <!-- CTA -->
      <div class="ab" id="cover"><img src="assets/ebook_cover.png" /></div>
      <div class="ab pill" id="plan">PLAN DE 7 JOURS</div>
      <div class="ab pill y" id="zero">0 $ DE PUB</div>
      <div class="ab" id="cbLab">Commentez<br /><span class="hl">« EBOOK »</span></div>
      <div class="ab card" id="cbox"><div class="av"></div><div class="in"><span>E</span><span>B</span><span>O</span><span>O</span><span>K</span></div>
        <div class="send"><svg viewBox="0 0 24 24" fill="#fff"><path d="M3 20.5 21 12 3 3.5l3 8.5-3 8.5Zm3-8.5h9"/></svg></div></div>
      <div class="ab pill k" id="acc">Je vous accompagne</div>

      <div class="spark" id="s1" style="left:60px;top:300px">__STAR__</div>
      <div class="spark" id="s2" style="left:950px;top:360px">__STAR__</div>
      <div class="spark" id="s3" style="left:100px;top:1260px;width:50px;height:50px">__STAR__</div>
      <div class="spark" id="s4" style="left:940px;top:1250px;width:56px;height:56px">__STAR__</div>

      <div id="caps"></div>
      <div id="flash"></div>
      <audio id="mix" src="assets/audio/mix.wav" data-start="0" data-duration="__DUR__" data-track-index="10" data-volume="1"></audio>
    </div>

    <script>
      window.__timelines = window.__timelines || {};
      const T = __T__;
      const CAPS = __CAPS__;
      const tl = gsap.timeline({ paused: true });
      const IN = (sel, from, to, at) => tl.fromTo(sel, from, to, at);
      const OUT = (sel, to, at) => tl.to(sel, to, at);
      const HIDE = ["#cap","#capTag","#big","#gain","#t3","#t3s","#n1","#v1t","#barLab","#bar","#d1","#d2","#d3","#d4","#d5","#reste",
              "#n2","#v2t","#brut","#benef","#cache","#n3","#v3t","#tel","#ch1","#ch2","#ch3",
              "#cover","#plan","#zero","#cbLab","#cbox","#acc","#s1","#s2","#s3","#s4","#flash"];
      tl.set(HIDE, { autoAlpha: 0 }, 0);
      tl.set("#censor", { scaleX: 0 }, 0);
      tl.fromTo("#progress", { scaleX: 0 }, { scaleX: 1, duration: __DUR__, ease: "none" }, 0);
      const flash = (at) => { tl.set("#flash", { autoAlpha: 0.85 }, at); tl.to("#flash", { autoAlpha: 0, duration: 0.22 }, at + 0.04); };
      const sparks = (at) => ["#s1","#s2","#s3","#s4"].forEach((s, i) =>
        IN(s, { autoAlpha: 1, scale: 0, rotation: -90 }, { scale: 1, rotation: 0, duration: 0.35, ease: "back.out(2.5)" }, at + i * 0.1));
      const sparksOut = (at) => OUT(["#s1","#s2","#s3","#s4"], { scale: 0, autoAlpha: 0, duration: 0.2 }, at);
      const pop = (sel, at, rot = 0) => IN(sel, { autoAlpha: 1, scale: 0, rotation: rot + 12 }, { scale: 1, rotation: rot, duration: 0.4, ease: "back.out(2.2)" }, at);
      const numIn = (sel, at) => IN(sel, { autoAlpha: 1, scale: 0, rotation: -120 }, { scale: 1, rotation: -6, duration: 0.5, ease: "back.out(2)" }, at);
      const titleIn = (sel, at) => IN(sel, { autoAlpha: 1, x: 120 }, { x: 0, duration: 0.45, ease: "power3.out" }, at);

      // ---------- HOOK ----------
      IN("#cap", { autoAlpha: 1, y: 900, rotation: 8 }, { y: 0, rotation: -4, duration: 0.6, ease: "back.out(1.3)" }, 0.05);
      tl.to("#cap", { scale: 1.04, duration: 8, ease: "sine.inOut" }, 0.7);
      pop("#big", 0.5, 3);
      pop("#capTag", 1.3, -2);
      sparks(T.reve);
      pop("#gain", T.gagne + 0.5, -5);
      tl.to("#gain", { scale: 1.08, duration: 0.4, yoyo: true, repeat: 3, ease: "sine.inOut" }, T.gagne + 1.0);
      OUT("#cap", { x: -900, rotation: -20, autoAlpha: 0, duration: 0.4, ease: "power3.in" }, T.title - 0.35);
      OUT(["#big", "#gain", "#capTag"], { x: 900, rotation: 15, autoAlpha: 0, duration: 0.4, ease: "power3.in" }, T.title - 0.35);
      sparksOut(T.title - 0.3);

      // ---------- TITRE ----------
      flash(T.title);
      IN("#t3", { autoAlpha: 1, scale: 2.6 }, { scale: 1, duration: 0.32, ease: "power4.in" }, T.title + 0.02);
      IN("#t3s", { autoAlpha: 1, y: 80 }, { y: 0, duration: 0.4, ease: "back.out(2)" }, T.title + 0.6);
      OUT(["#t3", "#t3s"], { autoAlpha: 0, scale: 0.7, duration: 0.25 }, T.v1 - 0.05);

      // ---------- VÉRITÉ 1 ----------
      numIn("#n1", T.v1);
      titleIn("#v1t", T.v1 + 0.15);
      IN("#barLab", { autoAlpha: 1, y: 30 }, { y: 0, duration: 0.3 }, T.benef1 + 0.3);
      IN("#bar", { autoAlpha: 1, scaleX: 0, transformOrigin: "left center" }, { scaleX: 1, duration: 0.6, ease: "power3.out" }, T.benef1 + 0.3);
      [["#b1", "#d1", T.c1], ["#b2", "#d2", T.c2], ["#b3", "#d3", T.c3], ["#b4", "#d4", T.c4], ["#b5", "#d5", T.c5]].forEach(([b, d, at], i) => {
        tl.to(b, { backgroundColor: "#e9e2d6", duration: 0.15 }, at);
        IN(d, { autoAlpha: 1, y: -60, scale: 0.6 }, { y: 0, scale: 1, duration: 0.3, ease: "back.out(2)" }, at);
        OUT(d, { y: 260, rotation: i % 2 ? 14 : -14, autoAlpha: 0, duration: 0.5, ease: "power2.in" }, at + 0.55);
      });
      tl.to(["#b1", "#b2", "#b3", "#b4", "#b5"], { width: 0, borderRightWidth: 0, duration: 0.5, ease: "power3.inOut" }, T.lanc);
      tl.to("#b6", { width: "100%", duration: 0.5, ease: "power3.inOut" }, T.lanc);
      tl.to("#barLab", { autoAlpha: 0, duration: 0.2 }, T.lanc);
      pop("#reste", T.reste - 0.1, -2);
      OUT(["#n1", "#v1t", "#bar", "#reste"], { autoAlpha: 0, y: -80, duration: 0.3, ease: "power2.in" }, T.v2 - 0.1);

      // ---------- VÉRITÉ 2 ----------
      numIn("#n2", T.v2);
      titleIn("#v2t", T.v2 + 0.15);
      IN("#brut", { autoAlpha: 1, x: -700, rotation: -20 }, { x: 0, rotation: -3, duration: 0.5, ease: "back.out(1.4)" }, T.brut);
      sparks(T.reveBrut);
      IN("#benef", { autoAlpha: 1, x: 700, rotation: 20 }, { x: 0, rotation: 3, duration: 0.5, ease: "back.out(1.4)" }, T.benef2 - 0.1);
      tl.to("#censor", { scaleX: 1, duration: 0.35, ease: "power3.out" }, T.benef2 + 0.6);
      pop("#cache", T.jamais, -8);
      sparksOut(T.v3 - 0.2);
      OUT(["#n2", "#v2t", "#brut", "#benef", "#cache"], { autoAlpha: 0, y: -80, duration: 0.3, ease: "power2.in" }, T.v3 - 0.1);

      // ---------- VÉRITÉ 3 ----------
      numIn("#n3", T.v3);
      titleIn("#v3t", T.v3 + 0.15);
      IN("#tel", { autoAlpha: 1, y: 900, rotation: 10 }, { y: 0, rotation: -3, duration: 0.55, ease: "back.out(1.3)" }, T.compte);
      pop("#ch1", T.tel - 0.1, 2);
      pop("#ch2", T.pub3 - 0.1, -2);
      pop("#ch3", T.frais3 - 0.1, 2);
      OUT(["#n3", "#v3t", "#tel", "#ch1", "#ch2", "#ch3"], { autoAlpha: 0, y: -80, duration: 0.3, ease: "power2.in" }, T.cta - 0.1);

      // ---------- CTA ----------
      IN("#cover", { autoAlpha: 1, y: 900, rotationY: 60, transformPerspective: 1400 }, { y: 0, rotationY: -10, duration: 0.6, ease: "power3.out" }, T.cta);
      tl.to("#cover", { rotationY: 8, duration: 4, ease: "sine.inOut" }, T.cta + 0.6);
      pop("#plan", T.sept - 0.1, -2);
      pop("#zero", T.franc - 0.1, 3);
      sparks(T.franc + 0.2);
      OUT(["#cover", "#plan", "#zero"], { autoAlpha: 0, scale: 0.6, duration: 0.3, ease: "back.in(1.5)" }, T.ebook - 0.05);
      flash(T.ebook);
      IN("#cbLab", { autoAlpha: 1, scale: 2.2 }, { scale: 1, duration: 0.3, ease: "power4.in" }, T.ebook + 0.05);
      IN("#cbox", { autoAlpha: 1, y: 300 }, { y: 0, duration: 0.45, ease: "back.out(1.6)" }, T.ebook + 0.3);
      document.querySelectorAll("#cbox .in span").forEach((s, i) => tl.set(s, { opacity: 1 }, T.ebookWord + i * 0.14));
      tl.to("#cbox .send", { scale: 1.2, duration: 0.3, yoyo: true, repeat: 5, ease: "sine.inOut" }, T.ebookWord + 0.9);
      pop("#acc", T.accomp - 0.1, -2);

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
        tl.set(box, { autoAlpha: 0 }, 0);
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
