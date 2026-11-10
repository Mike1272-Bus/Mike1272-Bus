<!doctype html>
<html lang="fr" data-resolution="portrait">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1080, height=1920" />
    <script src="assets/gsap.min.js"></script>
    <style>
      @font-face { font-family: 'Baloo 2'; font-weight: 800; src: url('assets/fonts/Baloo2-ExtraBold.ttf') format('truetype'); }
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
      .abs { position: absolute; }
      #progress { position: absolute; left: 0; top: 0; width: 1080px; height: 12px; background: #ff5c00; transform-origin: left center; z-index: 50; }
      .brand { position: absolute; top: 64px; left: 70px; z-index: 40; background: #111; color: #fff; font-size: 28px; letter-spacing: 0.04em; padding: 12px 30px 6px; border-radius: 40px; }
      .stage { position: absolute; inset: 0; perspective: 1600px; }

      /* cartes photo portrait (hook) */
      .pcard { position: absolute; width: 262px; height: 360px; }
      .flip { position: absolute; inset: 0; transform-style: preserve-3d; }
      .face { position: absolute; inset: 0; border-radius: 30px; border: 10px solid #fff; overflow: hidden; backface-visibility: hidden; box-shadow: 0 34px 60px rgba(60,30,0,0.28); }
      .face img { width: 100%; height: 100%; object-fit: cover; display: block; }
      .back { background: #111; transform: rotateY(180deg); display: flex; align-items: center; justify-content: center; color: #ff5c00; font-size: 240px; line-height: 1; }
      .tag { position: absolute; left: 16px; bottom: 16px; background: #111; color: #fff; font-size: 28px; padding: 8px 20px 2px; border-radius: 30px; z-index: 3; white-space: nowrap; }
      .pcard .tag { font-size: 24px; left: 12px; bottom: 14px; padding: 7px 16px 1px; }
      #h1 { left: 40px; top: 470px; } #h2 { left: 290px; top: 390px; z-index: 2; } #h3 { left: 530px; top: 430px; z-index: 3; } #h4 { left: 778px; top: 490px; }
      .back { font-size: 190px; }

      .pill { position: absolute; z-index: 20; text-align: center; background: #ff5c00; color: #fff; border-radius: 70px; border: 5px solid #111; box-shadow: 12px 12px 0 #111; }
      #badge { left: 230px; top: 900px; width: 620px; font-size: 64px; padding: 26px 0 14px; }

      .cover { position: absolute; border-radius: 30px; border: 12px solid #fff; overflow: hidden; box-shadow: 0 40px 80px rgba(60,30,0,0.32); }
      .cover img { width: 100%; height: 100%; object-fit: cover; display: block; }
      #cover { left: 250px; top: 330px; width: 580px; height: 580px; }
      #timer { position: absolute; left: 740px; top: 250px; width: 190px; height: 190px; z-index: 6; background: #fff; border: 5px solid #111; border-radius: 50%; box-shadow: 10px 10px 0 #111; }
      #timer svg { width: 100%; height: 100%; }

      .spark { position: absolute; width: 70px; height: 70px; z-index: 15; }
      .spark svg { width: 100%; height: 100%; fill: #111; }

      /* qui : salarié / étudiant / sans emploi */
      .who { position: absolute; top: 440px; width: 300px; height: 420px; }
      .who .tag { font-size: 32px; }
      #w1 { left: 45px; } #w2 { left: 390px; top: 400px; z-index: 2; } #w3 { left: 735px; }

      /* cartes vidéo */
      .vcard { position: absolute; }
      .vcard .inner { position: absolute; inset: 0; border-radius: 30px; border: 12px solid #fff; overflow: hidden; box-shadow: 0 34px 60px rgba(60,30,0,0.30); background: #222; }
      .vcard video, .vcard .poster { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; display: block; }
      .vcard.stack { left: 90px; width: 900px; height: 506px; }
      #k1 { top: 210px; } #k2 { top: 350px; } #k3 { top: 490px; } #k4 { top: 630px; }
      .vcard.big { left: 60px; top: 400px; width: 960px; height: 540px; }

      #net { position: absolute; left: 0; top: 300px; width: 1080px; height: 900px; }
      #net svg { width: 100%; height: 100%; overflow: visible; }
      .netlab { position: absolute; font-size: 44px; background: #fff; border: 5px solid #111; border-radius: 40px; padding: 10px 28px 2px; box-shadow: 8px 8px 0 #111; }
      #labA { left: 90px; top: 1000px; } #labB { left: 560px; top: 520px; }

      #flash { position: absolute; inset: 0; background: #fff; z-index: 45; opacity: 0; visibility: hidden; }

      #kmBadge { left: 180px; top: 1000px; width: 720px; font-size: 58px; padding: 24px 0 12px; }
      #davidTag { left: 60px; top: 300px; font-size: 46px; padding: 16px 36px 6px; background: #111; box-shadow: 10px 10px 0 #ff5c00; }
      #budgetBadge { left: 300px; top: 1000px; width: 620px; font-size: 62px; padding: 24px 0 12px; background: #ffd60a; color: #111; }

      #cover2 { left: 240px; top: 360px; width: 600px; height: 600px; z-index: 5; }
      #inside { position: absolute; left: 370px; top: 250px; font-size: 70px; line-height: 1; }
      #inside small { display: block; font-size: 34px; color: #c94200; margin-top: 10px; }
      .step { position: absolute; left: 90px; width: 900px; height: 118px; background: #fff; border: 5px solid #111; border-radius: 60px; box-shadow: 10px 10px 0 #111; display: flex; align-items: center; gap: 28px; padding-left: 16px; font-size: 48px; }
      .step .num { width: 84px; height: 84px; border-radius: 50%; background: #ff5c00; color: #fff; border: 4px solid #111; display: flex; align-items: center; justify-content: center; font-size: 50px; padding-top: 8px; }
      #st1 { top: 470px; } #st2 { top: 608px; } #st3 { top: 746px; } #st4 { top: 884px; } #st5 { top: 1022px; }
      #fmt { position: absolute; left: 90px; top: 1190px; width: 900px; display: flex; gap: 12px; justify-content: center; }
      #fmt span { background: #111; color: #fff; font-size: 30px; padding: 10px 20px 4px; border-radius: 30px; }

      #chk { position: absolute; left: 90px; top: 380px; width: 900px; background: #fff; border: 5px solid #111; border-radius: 44px; box-shadow: 14px 14px 0 #111; padding: 50px 50px 30px; }
      #chk h2 { font-size: 62px; line-height: 1.05; margin-bottom: 26px; }
      .row { display: flex; align-items: center; gap: 30px; margin-bottom: 26px; font-size: 44px; line-height: 1.12; }
      .box { flex: 0 0 76px; height: 76px; border: 5px solid #111; border-radius: 16px; position: relative; background: #fff; }
      .box svg { position: absolute; left: -6px; top: -14px; width: 92px; height: 92px; fill: none; stroke: #ff5c00; stroke-width: 12; stroke-linecap: round; stroke-linejoin: round; }

      .sig { position: absolute; left: 0; width: 1080px; text-align: center; line-height: 1; }
      #sg1 { top: 520px; font-size: 130px; }
      #sg2 { top: 720px; font-size: 76px; }
      #sg3 { top: 860px; font-size: 128px; }
      #sg3 span { background: #ffd60a; padding: 18px 34px 0; border-radius: 24px; color: #c94200; display: inline-block; }

      #bubble { position: absolute; left: 150px; top: 700px; width: 780px; display: flex; align-items: flex-end; gap: 24px; }
      #bubble img { width: 130px; height: 130px; }
      #bubble .b { flex: 1; background: #fff; border: 5px solid #111; border-radius: 44px 44px 44px 10px; box-shadow: 10px 10px 0 #111; height: 150px; display: flex; align-items: center; justify-content: center; gap: 22px; }
      #bubble .dot { width: 30px; height: 30px; border-radius: 50%; background: #111; }

      #ctaPanel { position: absolute; left: 70px; top: 420px; width: 940px; background: #111; border-radius: 50px; padding: 60px 50px 70px; display: flex; flex-direction: column; align-items: center; gap: 44px; box-shadow: 16px 16px 0 #ff5c00; }
      #ctaPanel .wa { display: flex; align-items: center; gap: 28px; color: #fff; font-size: 66px; }
      #ctaPanel .wa img { width: 120px; height: 120px; }
      #ctaBtn { background: #25d366; color: #111; font-size: 60px; padding: 30px 60px 18px; border-radius: 80px; border: 5px solid #fff; }
      #ctaPanel .sub { color: #ffd60a; font-size: 44px; }

      /* sous-titres karaoké */
      #caps { position: absolute; left: 60px; right: 60px; top: 1430px; height: 330px; z-index: 30; }
      #capsBig { position: absolute; left: 60px; right: 60px; top: 600px; height: 760px; z-index: 30; }
      .grp { position: absolute; inset: 0; display: flex; flex-wrap: wrap; justify-content: center; align-content: flex-start; column-gap: 18px; row-gap: 4px; text-align: center; }
      #caps .grp { font-size: 70px; line-height: 1.22; }
      #capsBig .grp { font-size: 120px; line-height: 1.12; align-content: center; }
      .w { position: relative; display: inline-block; opacity: 0.3; }
      .w .hl { position: absolute; left: -10px; right: -10px; top: 6px; bottom: 2px; background: #ffd60a; border-radius: 14px; transform: scaleX(0); z-index: 0; }
      .w .t { position: relative; z-index: 1; }
      .w.acc .t { color: #c94200; }
    </style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="__DUR__" data-width="1080" data-height="1920">
      <div id="progress"></div>
      <div class="brand">DIGITALMIKAELSON</div>

      <div class="stage">
        <!-- HOOK -->
        <div class="pcard" id="h1"><div class="flip" id="f1">
          <div class="face" id="fr1"><img src="assets/img/hook_or_d.jpg" /><div class="tag">Couture</div></div>
          <div class="face back" id="bk1">?</div></div></div>
        <div class="pcard" id="h2"><div class="flip" id="f2">
          <div class="face" id="fr2"><img src="assets/img/hook_or_b.jpg" /><div class="tag">Menuiserie</div></div>
          <div class="face back" id="bk2">?</div></div></div>
        <div class="pcard" id="h3"><div class="flip" id="f3">
          <div class="face" id="fr3"><img src="assets/img/hook_or_a.jpg" /><div class="tag">Comptabilité</div></div>
          <div class="face back" id="bk3">?</div></div></div>
        <div class="pcard" id="h4"><div class="flip" id="f4">
          <div class="face" id="fr4"><img src="assets/img/hook_montage.jpg" /><div class="tag">Montage vidéo</div></div>
          <div class="face back" id="bk4">?</div></div></div>

        <!-- PROMESSE -->
        <div class="cover" id="cover"><img src="assets/ebook_cover.png" /></div>

        <!-- PARTIE 1 -->
        <div class="who" id="w1"><div class="face"><img src="assets/img/who_salarie.jpg" style="object-position: 72% 50%" /><div class="tag">Salarié</div></div></div>
        <div class="who" id="w2"><div class="face"><img src="assets/img/who_etudiant.jpg" style="object-position: 46% 50%" /><div class="tag">Étudiant</div></div></div>
        <div class="who" id="w3"><div class="face"><img src="assets/img/who_sans_emploi.jpg" style="object-position: 66% 50%" /><div class="tag">Sans emploi</div></div></div>
        __CARDS_P1__

        <div id="net"><svg viewBox="0 0 1080 900">
          <circle cx="540" cy="430" r="380" fill="none" stroke="rgba(0,0,0,0.10)" stroke-width="4" />
          <ellipse cx="540" cy="430" rx="160" ry="380" fill="none" stroke="rgba(0,0,0,0.08)" stroke-width="4" />
          <line x1="160" y1="430" x2="920" y2="430" stroke="rgba(0,0,0,0.08)" stroke-width="4" />
          <path id="arc" d="M230 640 Q 470 40 850 250" fill="none" stroke="#ff5c00" stroke-width="10" stroke-linecap="round" stroke-dasharray="1000" stroke-dashoffset="1000" />
          <circle id="dotA" cx="230" cy="640" r="26" fill="#111" />
          <circle id="dotB" cx="850" cy="250" r="26" fill="#ff5c00" stroke="#111" stroke-width="6" />
        </svg></div>
        <div class="netlab" id="labA">VOUS</div>
        <div class="netlab" id="labB">QUELQU'UN</div>

        <!-- PARTIE 2 -->
        __P2__

        <!-- PARTIE 3 -->
        <div class="cover" id="cover2"><img src="assets/ebook_cover.png" /></div>
        <div id="inside">Dans le guide<small>5 étapes, concrètes</small></div>
        <div class="step" id="st1"><div class="num">1</div>Pas besoin de diplôme</div>
        <div class="step" id="st2"><div class="num">2</div>Se faire connaître</div>
        <div class="step" id="st3"><div class="num">3</div>Choisir son produit</div>
        <div class="step" id="st4"><div class="num">4</div>Créer et vendre</div>
        <div class="step" id="st5"><div class="num">5</div>Tester en 7 jours</div>
        <div id="fmt"><span>Petit livre</span><span>Vidéo</span><span>Modèle</span><span>Checklist</span><span>Kit</span></div>

        <div id="chk">
          <h2>En suivant le guide</h2>
          <div class="row"><div class="box"><svg viewBox="0 0 100 100"><path id="tk1" d="M18 52 L42 76 L86 22" stroke-dasharray="120" stroke-dashoffset="120"/></svg></div><div id="r1">Vous savez ce que vous vendez, et à qui</div></div>
          <div class="row"><div class="box"><svg viewBox="0 0 100 100"><path id="tk2" d="M18 52 L42 76 L86 22" stroke-dasharray="120" stroke-dashoffset="120"/></svg></div><div id="r2">Vous avez un premier produit</div></div>
          <div class="row"><div class="box"><svg viewBox="0 0 100 100"><path id="tk3" d="M18 52 L42 76 L86 22" stroke-dasharray="120" stroke-dashoffset="120"/></svg></div><div id="r3">Vous savez si des gens sont prêts à payer</div></div>
        </div>

        <div class="sig" id="sg1">PAS DE BLABLA.</div>
        <div class="sig" id="sg2">JUSTE CE QU'IL FAUT FAIRE,</div>
        <div class="sig" id="sg3"><span>CONCRÈTEMENT.</span></div>

        <div id="bubble"><img src="assets/wa_icon_clean.png" /><div class="b"><div class="dot" id="dt1"></div><div class="dot" id="dt2"></div><div class="dot" id="dt3"></div></div></div>

        <!-- CTA -->
        __CTA__
        <div id="ctaPanel">
          <div class="wa"><img src="assets/wa_icon_clean.png" />+243 831 710 181</div>
          <div id="ctaBtn">ENVOYER UN MESSAGE</div>
          <div class="sub">Je vous accompagne</div>
        </div>
      </div>

      <div class="pill" id="badge">VAUT DE L'ARGENT</div>
      <div id="timer"><svg viewBox="0 0 100 100">
        <circle cx="50" cy="50" r="34" fill="none" stroke="#eee" stroke-width="9" />
        <circle id="ring" cx="50" cy="50" r="34" fill="none" stroke="#ff5c00" stroke-width="9" stroke-linecap="round" stroke-dasharray="213.6" stroke-dashoffset="213.6" transform="rotate(-90 50 50)" />
        <line id="hand" x1="50" y1="50" x2="50" y2="26" stroke="#111" stroke-width="6" stroke-linecap="round" />
        <circle cx="50" cy="50" r="5" fill="#111" /></svg></div>
      <div class="pill" id="kmBadge">À DES MILLIERS DE KM</div>
      <div class="pill" id="davidTag">ONCLE DAVID · MENUISIER</div>
      <div class="pill" id="budgetBadge">SANS BUDGET PUB</div>

      <div class="spark" id="s1" style="left:60px;top:300px">__STAR__</div>
      <div class="spark" id="s2" style="left:950px;top:340px">__STAR__</div>
      <div class="spark" id="s3" style="left:110px;top:1230px;width:50px;height:50px">__STAR__</div>
      <div class="spark" id="s4" style="left:930px;top:1180px;width:56px;height:56px">__STAR__</div>

      <div id="caps"></div>
      <div id="capsBig"></div>
      <div id="flash"></div>

      <audio id="mix" src="assets/audio/mix_final.wav" data-start="0" data-duration="__DUR__" data-track-index="10" data-volume="1"></audio>
    </div>

    <script>
      window.__timelines = window.__timelines || {};
      const T = __T__;
      const CAPS = __CAPS__;
      const tl = gsap.timeline({ paused: true });
      const IN = (sel, from, to, at) => tl.fromTo(sel, from, to, at);
      const OUT = (sel, to, at) => tl.to(sel, to, at);
      const hideAll = ["#h1","#h2","#h3","#badge","#cover","#timer","#w1","#w2","#w3","#k1","#k2","#k3","#k4",
        "#net","#labA","#labB","#d1","#d2","#dv","#kmBadge","#davidTag","#budgetBadge","#cover2","#inside",
        "#st1","#st2","#st3","#st4","#st5","#fmt","#chk","#sg1","#sg2","#sg3","#bubble","#cv","#ctaPanel",
        "#s1","#s2","#s3","#s4","#flash","#bk1","#bk2","#bk3","#h4","#bk4"];
      tl.set(hideAll, { autoAlpha: 0 }, 0);

      // barre de progression
      tl.fromTo("#progress", { scaleX: 0 }, { scaleX: 1, duration: __DUR__, ease: "none" }, 0);
      const flash = (at) => { tl.set("#flash", { autoAlpha: 0.85 }, at); tl.to("#flash", { autoAlpha: 0, duration: 0.22 }, at + 0.04); };
      const sparks = (at) => ["#s1","#s2","#s3","#s4"].forEach((s, i) => {
        IN(s, { autoAlpha: 1, scale: 0, rotation: -90 }, { scale: 1, rotation: 0, duration: 0.35, ease: "back.out(2.5)" }, at + i * 0.1);
      });
      const sparksOut = (at) => OUT(["#s1","#s2","#s3","#s4"], { scale: 0, duration: 0.2 }, at);

      // ---------- HOOK ----------
      [["#h1", -9, 0.08], ["#h2", 3, 0.24], ["#h3", -4, 0.4], ["#h4", 9, 0.56]].forEach(([s, r, at]) =>
        IN(s, { autoAlpha: 1, y: 380, scale: 0.55, rotation: r * -2, rotationX: -55, transformPerspective: 1400 },
              { y: 0, scale: 1, rotation: r, rotationX: 0, duration: 0.5, ease: "back.out(1.5)" }, at));
      sparks(0.6);
      IN("#badge", { autoAlpha: 1, scale: 0, rotation: 12 }, { scale: 1, rotation: -4, duration: 0.4, ease: "back.out(2.2)" }, T.argent - 0.05);
      OUT("#badge", { scale: 0, duration: 0.2, ease: "back.in(2)" }, T.hookFlip - 0.25);
      [1, 2, 3, 4].forEach((n, i) => {
        const at = T.hookFlip + i * 0.1;
        IN("#f" + n, { rotationY: 0 }, { rotationY: 180, duration: 0.5, ease: "power2.inOut" }, at);
        tl.set("#bk" + n, { autoAlpha: 1 }, at + 0.25);
        tl.set("#fr" + n, { autoAlpha: 0 }, at + 0.25);
      });
      OUT("#h1", { x: -1000, rotation: -35, duration: 0.4, ease: "power3.in" }, T.promise - 0.1);
      OUT(["#h3", "#h4"], { x: 1000, rotation: 35, duration: 0.4, ease: "power3.in" }, T.promise - 0.1);
      OUT("#h2", { y: -1300, rotation: 15, duration: 0.4, ease: "power3.in" }, T.promise - 0.05);
      sparksOut(T.promise - 0.1);

      // ---------- PROMESSE ----------
      IN("#cover", { autoAlpha: 1, y: 900, rotationY: 75, rotationX: 20, scale: 0.7, transformPerspective: 1400 },
                   { y: 0, rotationY: -12, rotationX: 0, scale: 1, duration: 0.55, ease: "power3.out" }, T.promise + 0.1);
      tl.to("#cover", { rotationY: 8, rotation: -2, duration: T.promiseEnd - T.promise - 0.6, ease: "sine.inOut" }, T.promise + 0.65);
      IN("#timer", { autoAlpha: 1, scale: 0, rotation: -30 }, { scale: 1, rotation: 0, duration: 0.35, ease: "back.out(2.4)" }, T.promise + 0.5);
      const cd = T.promiseEnd - T.promise - 0.9;
      tl.fromTo("#ring", { attr: { "stroke-dashoffset": 213.6 } }, { attr: { "stroke-dashoffset": 0 }, duration: cd, ease: "none" }, T.promise + 0.7);
      tl.fromTo("#hand", { rotation: 0, svgOrigin: "50 50" }, { rotation: 360, svgOrigin: "50 50", duration: cd, ease: "none" }, T.promise + 0.7);
      OUT(["#cover", "#timer"], { scale: 0.2, autoAlpha: 0, rotation: 20, duration: 0.3, ease: "back.in(1.6)" }, T.promiseEnd - 0.1);

      // ---------- PARTIE 1 : qui ----------
      [["#w1", T.salarie, -4], ["#w2", T.etudiant, 2], ["#w3", T.sansEmploi, 5]].forEach(([s, at, r]) =>
        IN(s, { autoAlpha: 1, y: -700, rotation: r * 4 }, { y: 0, rotation: r, duration: 0.45, ease: "back.out(1.4)" }, at - 0.15));
      OUT(["#w1", "#w2", "#w3"], { y: 1800, rotation: 20, autoAlpha: 0, duration: 0.4, ease: "power3.in", stagger: 0.06 }, T.p1b - 0.2);

      // ---------- PARTIE 1 : compétences (cartes vidéo empilées) ----------
      [["#k1", T.p1b, -3], ["#k2", T.coudre - 0.35, 2.5], ["#k3", T.langue - 0.35, -2], ["#k4", T.compta - 0.35, 3]].forEach(([s, at, r], i) =>
        IN(s, { autoAlpha: 1, x: i % 2 ? 1100 : -1100, rotation: r * 5 }, { x: 0, rotation: r, duration: 0.42, ease: "power3.out" }, at));
      IN("#k1-tag", { scale: 0 }, { scale: 1, duration: 0.3, ease: "back.out(2)" }, T.cuisiner - 0.1);
      IN("#k2-tag", { scale: 0 }, { scale: 1, duration: 0.3, ease: "back.out(2)" }, T.coudre);
      IN("#k3-tag", { scale: 0 }, { scale: 1, duration: 0.3, ease: "back.out(2)" }, T.langue);
      IN("#k4-tag", { scale: 0 }, { scale: 1, duration: 0.3, ease: "back.out(2)" }, T.compta);
      OUT(["#k4", "#k3", "#k2", "#k1"], { y: -1500, rotation: -12, duration: 0.45, ease: "power3.in", stagger: 0.05 }, T.p1c - 0.15);

      // ---------- PARTIE 1 : quelqu'un, quelque part ----------
      IN("#net", { autoAlpha: 0 }, { autoAlpha: 1, duration: 0.3 }, T.p1c);
      IN("#dotA", { scale: 0, svgOrigin: "230 640" }, { scale: 1, svgOrigin: "230 640", duration: 0.3, ease: "back.out(3)" }, T.p1c);
      IN("#labA", { autoAlpha: 1, scale: 0 }, { scale: 1, duration: 0.3, ease: "back.out(2)" }, T.p1c + 0.1);
      tl.fromTo("#arc", { attr: { "stroke-dashoffset": 1000 } }, { attr: { "stroke-dashoffset": 0 }, duration: T.besoin - T.quelquePart + 0.2, ease: "power1.inOut" }, T.quelquePart);
      IN("#dotB", { scale: 0, svgOrigin: "850 250" }, { scale: 1, svgOrigin: "850 250", duration: 0.35, ease: "back.out(3)" }, T.besoin + 0.1);
      IN("#labB", { autoAlpha: 1, scale: 0 }, { scale: 1, duration: 0.3, ease: "back.out(2)" }, T.besoin + 0.2);
      tl.to("#dotB", { scale: 1.35, svgOrigin: "850 250", duration: 0.25, yoyo: true, repeat: 3 }, T.besoin + 0.6);
      OUT(["#net", "#labA", "#labB"], { autoAlpha: 0, scale: 0.8, duration: 0.25 }, T.b1);

      // ---------- BOUCLE 1 ----------
      flash(T.b1 + 0.2);

      // ---------- PARTIE 2 : distance ----------
      IN("#d1", { autoAlpha: 1, y: 900, rotationY: 60, rotation: 8, transformPerspective: 1400 },
                { y: 0, rotationY: 0, rotation: -2, duration: 0.55, ease: "power3.out" }, T.p2);
      tl.to("#d1", { scale: 1.04, duration: T.distB - T.p2 - 0.6, ease: "sine.inOut" }, T.p2 + 0.55);
      IN("#kmBadge", { autoAlpha: 1, scale: 0, rotation: -14 }, { scale: 1, rotation: -4, duration: 0.4, ease: "back.out(2.2)" }, T.km);
      IN("#d2", { autoAlpha: 1, x: 1200, rotation: 12 }, { x: 0, rotation: 2, duration: 0.45, ease: "power3.out" }, T.distB - 0.2);
      OUT("#d1", { x: -1200, rotation: -14, duration: 0.45, ease: "power3.in" }, T.distB - 0.2);

      // ---------- PARTIE 2 : oncle David ----------
      OUT(["#d2", "#kmBadge"], { x: -1200, rotation: -14, duration: 0.4, ease: "power3.in" }, T.david - 0.05);
      IN("#dv", { autoAlpha: 1, x: 1200, rotation: 10 }, { x: 0, rotation: -1.5, duration: 0.45, ease: "power3.out" }, T.david);
      tl.to("#dv", { scale: 1.05, duration: T.b2 - T.david - 0.6, ease: "sine.inOut" }, T.david + 0.45);
      IN("#davidTag", { autoAlpha: 1, x: -700 }, { x: 0, duration: 0.4, ease: "back.out(1.6)" }, T.david + 0.25);
      IN("#budgetBadge", { autoAlpha: 1, scale: 2.6, rotation: 18 }, { scale: 1, rotation: 5, duration: 0.3, ease: "power4.in" }, T.budget - 0.1);
      OUT(["#dv", "#davidTag", "#budgetBadge"], { y: 1800, rotation: 15, autoAlpha: 0, duration: 0.4, ease: "power3.in", stagger: 0.04 }, T.b2 - 0.1);

      // ---------- BOUCLE 2 ----------
      flash(T.b2 + 0.2);

      // ---------- PARTIE 3 : le guide ----------
      IN("#cover2", { autoAlpha: 1, y: 900, rotationY: -70, scale: 0.7, transformPerspective: 1400 },
                    { y: 0, rotationY: 10, scale: 1, duration: 0.6, ease: "power3.out" }, T.guide);
      tl.to("#cover2", { rotationY: -6, duration: T.step1 - T.guide - 0.95, ease: "sine.inOut" }, T.guide + 0.6);
      sparks(T.guide + 0.4);
      sparksOut(T.step1 - 0.2);
      tl.to("#cover2", { x: -150, y: -170, scale: 0.4167, rotationY: 0, rotation: -4, transformOrigin: "0 0", duration: 0.5, ease: "power3.inOut" }, T.step1 - 0.3);
      IN("#inside", { autoAlpha: 1, x: 300 }, { x: 0, duration: 0.4, ease: "power3.out" }, T.step1 - 0.1);
      [["#st1", T.step1], ["#st2", T.step2], ["#st3", T.step3], ["#st4", T.step4], ["#st5", T.step5]].forEach(([s, at]) =>
        IN(s, { autoAlpha: 1, x: 1150, rotation: 6 }, { x: 0, rotation: 0, duration: 0.42, ease: "back.out(1.3)" }, at - 0.05));
      IN("#fmt span", { autoAlpha: 0, y: 40 }, { autoAlpha: 1, y: 0, duration: 0.25, stagger: 0.12, ease: "back.out(2)" }, T.step3 + 0.4);
      tl.set("#fmt", { autoAlpha: 1 }, T.step3 + 0.35);
      OUT("#fmt", { autoAlpha: 0, duration: 0.2 }, T.step4 - 0.2);
      OUT(["#st5", "#st4", "#st3", "#st2", "#st1"], { x: -1150, duration: 0.35, ease: "power3.in", stagger: 0.04 }, T.check - 0.2);
      OUT(["#cover2", "#inside"], { autoAlpha: 0, duration: 0.25 }, T.check - 0.2);

      // ---------- PARTIE 3 : ce que vous aurez ----------
      IN("#chk", { autoAlpha: 1, y: 900, rotation: 6 }, { y: 0, rotation: -1.5, duration: 0.5, ease: "back.out(1.2)" }, T.check);
      [["#tk1", T.tick1], ["#tk2", T.tick2], ["#tk3", T.tick3]].forEach(([s, at]) =>
        tl.fromTo(s, { attr: { "stroke-dashoffset": 120 } }, { attr: { "stroke-dashoffset": 0 }, duration: 0.25, ease: "power2.out" }, at));
      OUT("#chk", { y: -1400, rotation: -8, duration: 0.4, ease: "power3.in" }, T.sig - 0.15);

      // ---------- SIGNATURE ----------
      IN("#sg1", { autoAlpha: 1, scale: 2.4 }, { scale: 1, duration: 0.28, ease: "power4.in" }, T.sig + 0.1);
      IN("#sg2", { autoAlpha: 1, y: 60 }, { y: 0, duration: 0.3, ease: "back.out(2)" }, T.sig2 - 0.05);
      IN("#sg3", { autoAlpha: 1, scale: 2.4, rotation: -6 }, { scale: 1, rotation: -3, duration: 0.28, ease: "power4.in" }, T.sig3 - 0.05);
      OUT(["#sg1", "#sg2", "#sg3"], { autoAlpha: 0, scale: 0.7, duration: 0.25 }, T.b3);

      // ---------- BOUCLE 3 ----------
      flash(T.b3 + 0.2);
      IN("#bubble", { autoAlpha: 1, scale: 0, transformOrigin: "10% 100%" }, { scale: 1, duration: 0.4, ease: "back.out(2)" }, T.bubble - 0.2);
      ["#dt1", "#dt2", "#dt3"].forEach((s, i) => tl.to(s, { y: -22, duration: 0.22, yoyo: true, repeat: 5, ease: "sine.inOut" }, T.bubble + i * 0.12));
      OUT("#bubble", { scale: 0, autoAlpha: 0, duration: 0.25 }, T.cta - 0.1);

      // ---------- CTA ----------
      IN("#cv", { autoAlpha: 1, scale: 0.4, rotation: -10 }, { scale: 1, rotation: -1, duration: 0.45, ease: "back.out(1.6)" }, T.cta);
      OUT("#cv", { scale: 0.3, autoAlpha: 0, rotation: 10, duration: 0.3, ease: "back.in(1.5)" }, T.ctaCard - 0.1);
      IN("#ctaPanel", { autoAlpha: 1, y: 900, rotation: 5 }, { y: 0, rotation: -1, duration: 0.5, ease: "back.out(1.3)" }, T.ctaCard);
      tl.to("#ctaBtn", { scale: 1.07, duration: 0.45, yoyo: true, repeat: 5, ease: "sine.inOut" }, T.ctaCard + 0.5);
      sparks(T.ctaCard + 0.3);

      // ---------- SOUS-TITRES KARAOKÉ ----------
      CAPS.forEach((c, ci) => {
        const box = document.createElement("div");
        box.className = "grp";
        box.id = "cap" + ci;
        c.words.forEach((w, wi) => {
          const el = document.createElement("span");
          el.className = "w" + (w.acc ? " acc" : "");
          el.innerHTML = '<span class="hl"></span><span class="t"></span>';
          el.querySelector(".t").textContent = w.t;
          box.appendChild(el);
          w.el = el;
        });
        document.getElementById(c.mode === "big" ? "capsBig" : "caps").appendChild(box);
        tl.set(box, { autoAlpha: 0 }, 0);
        tl.fromTo(box, { autoAlpha: 0, y: c.mode === "big" ? 40 : 20, scale: c.mode === "big" ? 0.92 : 1 },
                       { autoAlpha: 1, y: 0, scale: 1, duration: 0.14, ease: "power2.out" }, Math.max(0, c.start - 0.08));
        c.words.forEach((w, i) => {
          const hl = w.el.querySelector(".hl");
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
