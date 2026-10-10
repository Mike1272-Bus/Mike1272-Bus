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
      #progress { position: absolute; left: 0; top: 0; width: 1080px; height: 12px; background: #ff5c00; transform-origin: left center; z-index: 50; }
      .brand { position: absolute; top: 64px; left: 70px; z-index: 40; background: #111; color: #fff; font-size: 28px; letter-spacing: 0.04em; padding: 12px 30px 6px; border-radius: 40px; }
      .stage { position: absolute; inset: 0; perspective: 1600px; }

      #merci { position: absolute; left: 0; width: 1080px; top: 560px; text-align: center; font-size: 210px; line-height: 1; color: #ff5c00; -webkit-text-stroke: 6px #111; }

      .card { position: absolute; border-radius: 30px; border: 12px solid #fff; overflow: hidden; box-shadow: 0 40px 80px rgba(60,30,0,0.30); background: #fff; }
      .card img { width: 100%; height: 100%; object-fit: cover; display: block; }
      #cover { left: 250px; top: 330px; width: 580px; height: 580px; z-index: 6; }
      .page { left: 90px; top: 300px; width: 900px; height: 900px; }
      #pg10 img, #pg11 img { transform-origin: 50% 50%; }

      .pill { position: absolute; z-index: 20; text-align: center; background: #ff5c00; color: #fff; border-radius: 70px; border: 5px solid #111; box-shadow: 12px 12px 0 #111; white-space: nowrap; }
      #tagCv, #tagCuis { left: 140px; top: 1235px; width: 800px; font-size: 58px; padding: 22px 0 10px; }
      #b7 { left: 70px; top: 1235px; width: 380px; font-size: 50px; padding: 22px 0 10px; }
      #b0 { left: 480px; top: 1235px; width: 540px; font-size: 40px; padding: 28px 0 14px; background: #ffd60a; color: #111; }

      .step { position: absolute; left: 90px; width: 900px; height: 118px; background: #fff; border: 5px solid #111; border-radius: 60px; box-shadow: 10px 10px 0 #111; display: flex; align-items: center; gap: 28px; padding-left: 16px; font-size: 50px; z-index: 8; }
      .step .num { width: 84px; height: 84px; border-radius: 50%; background: #ff5c00; color: #fff; border: 4px solid #111; display: flex; align-items: center; justify-content: center; font-size: 50px; padding-top: 8px; }
      .step img { width: 70px; height: 70px; margin-left: -8px; }
      #st1 { top: 760px; } #st2 { top: 900px; } #st3 { top: 1040px; }

      #week { position: absolute; left: 85px; top: 600px; width: 910px; display: flex; gap: 14px; }
      .day { width: 118px; height: 160px; background: #fff; border: 5px solid #111; border-radius: 24px; box-shadow: 8px 8px 0 #111; display: flex; align-items: center; justify-content: center; font-size: 46px; padding-top: 8px; }
      #weekTitle { position: absolute; left: 0; width: 1080px; top: 440px; text-align: center; font-size: 76px; }
      #ready { left: 190px; top: 900px; width: 700px; font-size: 64px; padding: 26px 0 12px; background: #ffd60a; color: #111; }

      #chat { position: absolute; left: 70px; top: 520px; width: 940px; display: flex; align-items: flex-end; gap: 22px; }
      #chat > img { width: 120px; height: 120px; flex: 0 0 120px; }
      #chat .bubble { flex: 1; background: #fff; border: 5px solid #111; border-radius: 44px 44px 44px 10px; box-shadow: 12px 12px 0 #111; padding: 26px; display: flex; gap: 26px; align-items: center; }
      #chat .bubble img { width: 190px; height: 190px; border-radius: 18px; object-fit: cover; border: 4px solid #111; }
      #chat .ttl { font-size: 46px; line-height: 1.05; }
      #chat .lnk { display: flex; align-items: center; gap: 10px; font-size: 32px; color: #c94200; margin-top: 14px; }
      #chat .lnk svg { width: 40px; height: 40px; fill: none; stroke: #c94200; stroke-width: 9; stroke-linecap: round; }
      #ask { left: 140px; top: 1010px; width: 800px; font-size: 56px; padding: 26px 0 12px; background: #25d366; color: #111; }

      .spark { position: absolute; width: 70px; height: 70px; z-index: 15; }
      .spark svg { width: 100%; height: 100%; fill: #111; }

      #caps { position: absolute; left: 60px; right: 60px; top: 1440px; height: 330px; z-index: 30; }
      .grp { position: absolute; inset: 0; display: flex; flex-wrap: wrap; justify-content: center; align-content: flex-start; column-gap: 18px; row-gap: 4px; text-align: center; font-size: 70px; line-height: 1.22; }
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
        <div id="merci">MERCI !</div>
        <div class="card page" id="pg15"><img src="assets/img/page15.png" /></div>
        <div class="card page" id="pg11"><img src="assets/img/page11.png" /></div>
        <div class="card page" id="pg10"><img src="assets/img/page10.png" /></div>
        <div class="card" id="cover"><img src="assets/img/ebook_cover.png" /></div>

        <div class="step" id="st1"><div class="num">1</div>Ton offre en une phrase</div>
        <div class="step" id="st2"><div class="num">2</div>Tu en parles autour de toi</div>
        <div class="step" id="st3"><div class="num">3</div><img src="assets/img/wa_icon_clean.png" />Statut WhatsApp</div>

        <div id="weekTitle">Une semaine</div>
        <div id="week">
          <div class="day" id="d1">J1</div><div class="day" id="d2">J2</div><div class="day" id="d3">J3</div>
          <div class="day" id="d4">J4</div><div class="day" id="d5">J5</div><div class="day" id="d6">J6</div>
          <div class="day" id="d7">J7</div>
        </div>

        <div id="chat"><img src="assets/img/wa_icon_clean.png" />
          <div class="bubble"><img src="assets/img/ebook_cover.png" />
            <div><div class="ttl">Gagne ta vie sans diplôme</div>
              <div class="lnk"><svg viewBox="0 0 100 100"><path d="M42 58 L58 42"/><path d="M36 50 L26 60 a14 14 0 0 0 20 20 L56 70"/><path d="M64 50 L74 40 a14 14 0 0 0 -20 -20 L44 30"/></svg>Lien du guide</div></div>
          </div>
        </div>
      </div>

      <div class="pill" id="tagCv">MODÈLE DE CV</div>
      <div class="pill" id="tagCuis">MINI-FORMATION CUISINE</div>
      <div class="pill" id="b7">EN 7 JOURS</div>
      <div class="pill" id="b0">SANS DÉPENSER UN CENTIME</div>
      <div class="pill" id="ready">PRÊTS À PAYER ?</div>
      <div class="pill" id="ask">UNE QUESTION ? ÉCRIS-MOI</div>

      <div class="spark" id="s1" style="left:80px;top:360px"><svg viewBox="0 0 100 100"><path d="M50 0 C54 38 62 46 100 50 C62 54 54 62 50 100 C46 62 38 54 0 50 C38 46 46 38 50 0Z"/></svg></div>
      <div class="spark" id="s2" style="left:930px;top:420px"><svg viewBox="0 0 100 100"><path d="M50 0 C54 38 62 46 100 50 C62 54 54 62 50 100 C46 62 38 54 0 50 C38 46 46 38 50 0Z"/></svg></div>
      <div class="spark" id="s3" style="left:140px;top:960px;width:50px;height:50px"><svg viewBox="0 0 100 100"><path d="M50 0 C54 38 62 46 100 50 C62 54 54 62 50 100 C46 62 38 54 0 50 C38 46 46 38 50 0Z"/></svg></div>
      <div class="spark" id="s4" style="left:900px;top:900px;width:56px;height:56px"><svg viewBox="0 0 100 100"><path d="M50 0 C54 38 62 46 100 50 C62 54 54 62 50 100 C46 62 38 54 0 50 C38 46 46 38 50 0Z"/></svg></div>

      <div id="caps"></div>
      <audio id="mix" src="assets/audio/mix_tunnel.wav" data-start="0" data-duration="__DUR__" data-track-index="10" data-volume="1"></audio>
    </div>

    <script>
      window.__timelines = window.__timelines || {};
      const T = __T__;
      const CAPS = __CAPS__;
      const tl = gsap.timeline({ paused: true });
      const IN = (s, f, t, at) => tl.fromTo(s, f, t, at);
      const OUT = (s, t, at) => tl.to(s, t, at);
      tl.set(["#merci","#cover","#pg10","#pg11","#pg15","#tagCv","#tagCuis","#b7","#b0","#st1","#st2","#st3",
              "#weekTitle","#week","#ready","#chat","#ask","#s1","#s2","#s3","#s4"], { autoAlpha: 0 }, 0);
      tl.fromTo("#progress", { scaleX: 0 }, { scaleX: 1, duration: __DUR__, ease: "none" }, 0);
      const sparks = (at) => ["#s1","#s2","#s3","#s4"].forEach((s, i) =>
        IN(s, { autoAlpha: 1, scale: 0, rotation: -90 }, { scale: 1, rotation: 0, duration: 0.35, ease: "back.out(2.5)" }, at + i * 0.08));
      const sparksOut = (at) => OUT(["#s1","#s2","#s3","#s4"], { scale: 0, autoAlpha: 0, duration: 0.2 }, at);

      // merci
      IN("#merci", { autoAlpha: 1, scale: 2.6, rotation: -14 }, { scale: 1, rotation: -4, duration: 0.3, ease: "power4.in" }, T.merci);
      sparks(T.merci + 0.2);
      OUT("#merci", { scale: 0.3, autoAlpha: 0, rotation: 10, duration: 0.25, ease: "back.in(2)" }, T.guide - 0.1);
      sparksOut(T.guide - 0.1);

      // le guide s'ouvre
      IN("#cover", { autoAlpha: 1, y: 900, rotationY: 70, scale: 0.7, transformPerspective: 1400 },
                   { y: 0, rotationY: -8, scale: 1, duration: 0.5, ease: "power3.out" }, T.guide);
      tl.set("#pg10", { autoAlpha: 1, scale: 0.9 }, T.open - 0.05);
      tl.to("#cover", { rotationY: -150, transformOrigin: "left center", autoAlpha: 0, duration: 0.5, ease: "power2.in" }, T.open);
      tl.to("#pg10", { scale: 1, duration: 0.5, ease: "power2.out" }, T.open + 0.1);

      // page 10 : modèle de CV
      tl.to("#pg10 img", { scale: 2.1, x: 275, y: -480, duration: 0.6, ease: "power3.inOut" }, T.cv - 0.35);
      IN("#tagCv", { autoAlpha: 1, scale: 0, rotation: -10 }, { scale: 1, rotation: -3, duration: 0.35, ease: "back.out(2.2)" }, T.cv);
      OUT("#tagCv", { scale: 0, autoAlpha: 0, duration: 0.2 }, T.p11 - 0.1);
      IN("#pg11", { autoAlpha: 1, x: 1200, rotation: 10 }, { x: 0, rotation: 1.5, duration: 0.45, ease: "power3.out" }, T.p11);
      OUT("#pg10", { x: -1200, rotation: -12, autoAlpha: 0, duration: 0.45, ease: "power3.in" }, T.p11);

      // page 11 : mini-formation cuisine
      tl.to("#pg11 img", { scale: 2.1, x: -147, y: -405, duration: 0.6, ease: "power3.inOut" }, T.cuisine - 0.35);
      IN("#tagCuis", { autoAlpha: 1, scale: 0, rotation: 10 }, { scale: 1, rotation: 3, duration: 0.35, ease: "back.out(2.2)" }, T.cuisine);
      OUT(["#pg11", "#tagCuis"], { y: -1500, rotation: -10, autoAlpha: 0, duration: 0.45, ease: "power3.in" }, T.plan - 0.1);

      // page 15 : le test en 7 jours
      IN("#pg15", { autoAlpha: 1, y: 1300, rotation: 8 }, { y: 0, rotation: -1.5, duration: 0.5, ease: "back.out(1.2)" }, T.plan);
      IN("#b7", { autoAlpha: 1, scale: 0, rotation: -12 }, { scale: 1, rotation: -4, duration: 0.35, ease: "back.out(2.2)" }, T.semaine);
      IN("#b0", { autoAlpha: 1, scale: 2.6, rotation: 16 }, { scale: 1, rotation: 4, duration: 0.28, ease: "power4.in" }, T.centime - 0.1);
      OUT(["#b7", "#b0"], { scale: 0, autoAlpha: 0, duration: 0.2 }, T.s1 - 0.35);
      tl.to("#pg15", { scale: 0.46, y: -20, transformOrigin: "50% 0%", duration: 0.45, ease: "power3.inOut" }, T.s1 - 0.35);
      [["#st1", T.s1], ["#st2", T.s2], ["#st3", T.s3]].forEach(([s, at]) =>
        IN(s, { autoAlpha: 1, x: 1150, rotation: 6 }, { x: 0, rotation: 0, duration: 0.4, ease: "back.out(1.3)" }, at - 0.1));
      OUT(["#st3", "#st2", "#st1", "#pg15"], { x: -1200, autoAlpha: 0, duration: 0.35, ease: "power3.in", stagger: 0.04 }, T.week - 0.15);

      // une semaine
      IN("#weekTitle", { autoAlpha: 1, y: -40 }, { y: 0, duration: 0.3, ease: "power2.out" }, T.week);
      IN("#week", { autoAlpha: 1, y: 80 }, { y: 0, duration: 0.35, ease: "back.out(1.5)" }, T.week + 0.1);
      for (let i = 1; i <= 7; i++) {
        tl.to("#d" + i, { backgroundColor: "#ff5c00", color: "#ffffff", scale: 1.08, duration: 0.12 }, T.week + 0.4 + (i - 1) * T.weekStep);
        tl.to("#d" + i, { scale: 1, duration: 0.12 }, T.week + 0.52 + (i - 1) * T.weekStep);
      }
      IN("#ready", { autoAlpha: 1, scale: 1.8, rotation: -12 }, { scale: 1, rotation: -3, duration: 0.25, ease: "power3.in" }, T.sais - 0.05);
      OUT(["#weekTitle", "#week", "#ready"], { y: -1300, autoAlpha: 0, duration: 0.4, ease: "power3.in", stagger: 0.04 }, T.link - 0.15);

      // le lien
      IN("#chat", { autoAlpha: 1, x: 1100, rotation: 6 }, { x: 0, rotation: -1, duration: 0.5, ease: "back.out(1.3)" }, T.link);
      IN("#ask", { autoAlpha: 1, scale: 0, rotation: 8 }, { scale: 1, rotation: -2, duration: 0.35, ease: "back.out(2.2)" }, T.ask);
      tl.to("#ask", { scale: 1.06, duration: 0.4, yoyo: true, repeat: 1, ease: "sine.inOut" }, T.ask + 0.45);
      sparks(T.ask + 0.1);

      // sous-titres karaoké
      CAPS.forEach((c, ci) => {
        const box = document.createElement("div");
        box.className = "grp"; box.id = "cap" + ci;
        c.words.forEach((w) => {
          const el = document.createElement("span");
          el.className = "w" + (w.acc ? " acc" : "");
          el.innerHTML = '<span class="hl"></span><span class="t"></span>';
          el.querySelector(".t").textContent = w.t;
          box.appendChild(el); w.el = el;
        });
        document.getElementById("caps").appendChild(box);
        tl.set(box, { autoAlpha: 0 }, 0);
        tl.fromTo(box, { autoAlpha: 0, y: 20 }, { autoAlpha: 1, y: 0, duration: 0.14, ease: "power2.out" }, Math.max(0, c.start - 0.08));
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
