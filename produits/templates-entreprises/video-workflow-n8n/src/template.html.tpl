<!doctype html>
<html lang="fr" data-resolution="portrait">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1080, height=1920" />
    <script src="assets/gsap.min.js"></script>
    <style>
      :root { --ink: #0b1033; --ink2: #4a5275; --blue: #2342ff; --orange: #ff9d1c; --navy: #030722; }
      * { margin: 0; padding: 0; box-sizing: border-box; }
      html, body { width: 1080px; height: 1920px; overflow: hidden; background: var(--navy); }
      #root { position: relative; width: 100%; height: 100%; overflow: hidden; font-family: 'Poppins', sans-serif; background: var(--navy); }
      .ab { position: absolute; }
      .sc, .bgL, .bgD { position: absolute; left: 0; top: 0; width: 1080px; height: 1920px; overflow: hidden; }
      .w { display: inline-block; }
      .bgL { background: #f5f7fc; }
      .grid { left: 0; top: 0; width: 1080px; height: 1920px; background-image: radial-gradient(circle, rgba(35,66,255,0.22) 2.5px, transparent 3px); background-size: 48px 48px; }
      .blobA { left: -300px; top: -260px; width: 1100px; height: 1100px; border-radius: 50%; background: radial-gradient(circle, rgba(116,146,255,0.40) 0%, rgba(116,146,255,0) 65%); }
      .blobB { left: 200px; top: 1100px; width: 1100px; height: 1100px; border-radius: 50%; background: radial-gradient(circle, rgba(255,214,130,0.50) 0%, rgba(255,214,130,0) 62%); }
      .bgD { background: radial-gradient(circle at 50% 46%, #0c1d9a 0%, #061060 34%, #030722 72%); }
      .rings { left: 0; top: 0; width: 1080px; height: 1920px; }
      .rings circle { fill: none; stroke: rgba(110,140,255,0.28); stroke-width: 2.5; }
      .pill { position: absolute; left: 0; top: 220px; width: 1080px; text-align: center; }
      .pill span { display: inline-block; padding: 14px 40px; border-radius: 60px; font-size: 32px; font-weight: 700; letter-spacing: 0.05em; }
      .pillL span { background: rgba(35,66,255,0.10); color: var(--blue); border: 2px solid rgba(35,66,255,0.25); }
      .pillD span { background: rgba(255,255,255,0.10); color: #dfe5ff; border: 2px solid rgba(255,255,255,0.22); }
      .title { position: absolute; left: 70px; width: 940px; text-align: center; font-weight: 700; line-height: 1.22; }
      .tL { color: var(--ink); } .tD { color: #fff; }
      .acc { color: var(--orange); white-space: nowrap; }
      .bluebtn { background: linear-gradient(180deg, #3a5bff 0%, #1428e0 100%); box-shadow: 0 18px 50px rgba(35,66,255,0.55), inset 0 2px 0 rgba(255,255,255,0.35); color: #fff; }

      .cap { position: absolute; left: 70px; top: 320px; width: 940px; text-align: center; font-weight: 700; font-size: 72px; line-height: 1.12; }
      .links { left: 0; top: 0; width: 1080px; height: 1920px; }
      #wf1 .links path { stroke: #9fb0ff; stroke-width: 6; fill: none; stroke-linecap: round; }
      #wf2 .links path { stroke: rgba(255,255,255,0.45); stroke-width: 6; fill: none; stroke-linecap: round; }
      .node { position: absolute; left: 150px; width: 780px; height: 128px; border-radius: 34px; background: #fff; box-shadow: 0 20px 50px rgba(11,16,51,0.14); }
      #wf2 .node { box-shadow: 0 20px 50px rgba(0,0,0,0.45); }
      .nring { position: absolute; left: -8px; top: -8px; width: 796px; height: 144px; border-radius: 40px; border: 6px solid var(--blue); box-shadow: 0 0 40px rgba(35,66,255,0.55); opacity: 0; }
      #wf2 .nring { border-color: var(--orange); box-shadow: 0 0 40px rgba(255,157,28,0.7); }
      .nic { position: absolute; left: 20px; top: 20px; width: 88px; height: 88px; border-radius: 26px; }
      .nic svg { position: absolute; left: 14px; top: 14px; width: 60px; height: 60px; }
      .nt { position: absolute; left: 130px; top: 22px; font-size: 31px; font-weight: 700; color: var(--ink); white-space: nowrap; }
      .ns { position: absolute; left: 130px; top: 70px; font-size: 24px; color: #5c6380; }
      .ok { position: absolute; left: 706px; top: 36px; width: 56px; height: 56px; border-radius: 28px; background: #15803d; color: #fff; font-size: 32px; font-weight: 700; line-height: 56px; text-align: center; }
      .dot { left: 524px; top: 0; width: 32px; height: 32px; border-radius: 50%; background: var(--blue); box-shadow: 0 0 24px 8px rgba(35,66,255,0.6); }
      #dot2 { background: var(--orange); box-shadow: 0 0 24px 8px rgba(255,157,28,0.7); }
      #oui { left: 570px; top: 1645px; padding: 4px 22px; border-radius: 24px; background: #b85400; color: #fff; font-size: 26px; font-weight: 700; }
      #toast { left: 150px; top: 1700px; width: 780px; height: 110px; border-radius: 55px; background: #15803d; color: #fff; text-align: center; line-height: 110px; font-size: 38px; font-weight: 700; box-shadow: 0 20px 50px rgba(0,0,0,0.45); }

      #s1t { top: 1090px; font-size: 92px; }
      #orb { left: 390px; top: 640px; width: 300px; height: 300px; border-radius: 50%; border: 22px solid var(--orange); box-shadow: 0 0 80px 20px rgba(255,157,28,0.65), inset 0 0 50px 10px rgba(255,157,28,0.55); }
      #orbT { left: 390px; top: 640px; width: 300px; height: 300px; line-height: 300px; text-align: center; color: #fff; font-size: 64px; font-weight: 700; }

      #s4t { top: 330px; font-size: 84px; }
      #logoGlow { left: 240px; top: 720px; width: 600px; height: 600px; border-radius: 50%; background: radial-gradient(circle, rgba(244,197,24,0.35) 0%, rgba(244,197,24,0) 62%); }
      #logo { left: 320px; top: 800px; width: 440px; height: 348px; background: url('assets/img/logo_adg.png') center / contain no-repeat; }
      #s4b { top: 1240px; font-size: 60px; font-weight: 400; color: #dfe5ff; }
      #s4c { left: 160px; top: 1500px; width: 760px; height: 140px; border-radius: 70px; line-height: 140px; text-align: center; font-size: 46px; font-weight: 700; }
    </style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="35" data-width="1080" data-height="1920">

      <!-- S1 : intro -->
      <div id="s1" class="clip sc" data-start="0" data-duration="4" data-track-index="1">
        <div class="bgD"><svg class="rings ab" id="rings1" viewBox="0 0 1080 1920"><circle cx="540" cy="790" r="260" /><circle cx="540" cy="790" r="420" /><circle cx="540" cy="790" r="600" /><circle cx="540" cy="790" r="800" /></svg></div>
        <div id="s1w" class="sc">
          <div id="orb" class="ab"></div>
          <div id="orbT" class="ab">n8n</div>
          <div id="s1t" class="title tD">Que se passe-t-il quand une <span class="acc">commande arrive ?</span></div>
        </div>
      </div>

      <!-- S2 : workflow 1 -->
      <div id="s2" class="clip sc" data-start="4" data-duration="16" data-track-index="1">
        <div class="bgL"><div class="ab grid"></div><div class="ab blobA"></div><div class="ab blobB"></div></div>
        <div id="wf1" class="sc">
          <div class="pill pillL" id="p1"><span>AUTOMATISATION 1 · À CHAQUE COMMANDE</span></div>
          %%CAP1%%
          <svg class="links ab" viewBox="0 0 1080 1920">%%WF1LINKS%%</svg>
          <div id="oui" class="ab">oui</div>
          %%WF1NODES%%
          <div id="dot1" class="ab dot"></div>
        </div>
      </div>

      <!-- S3 : workflow 2 -->
      <div id="s3" class="clip sc" data-start="20" data-duration="9" data-track-index="1">
        <div class="bgD"><svg class="rings ab" id="rings3" viewBox="0 0 1080 1920"><circle cx="540" cy="1100" r="300" /><circle cx="540" cy="1100" r="480" /><circle cx="540" cy="1100" r="680" /></svg></div>
        <div id="wf2" class="sc">
          <div class="pill pillD" id="p2"><span>AUTOMATISATION 2 · CHAQUE SOIR</span></div>
          %%CAP2%%
          <svg class="links ab" viewBox="0 0 1080 1920">%%WF2LINKS%%</svg>
          %%WF2NODES%%
          <div id="dot2" class="ab dot"></div>
          <div id="toast" class="ab">✓ Bilan envoyé sur WhatsApp</div>
        </div>
      </div>

      <!-- S4 : fin -->
      <div id="s4" class="clip sc" data-start="29" data-duration="6" data-track-index="1">
        <div class="bgD"><svg class="rings ab" id="rings4" viewBox="0 0 1080 1920"><circle cx="540" cy="970" r="320" /><circle cx="540" cy="970" r="480" /><circle cx="540" cy="970" r="660" /></svg></div>
        <div id="s4w" class="sc">
          <div id="s4t" class="title tD">Deux automatisations qui tournent <span class="acc">toutes seules</span></div>
          <div id="logoGlow" class="ab"></div>
          <div id="logo" class="ab"></div>
          <div id="s4b" class="title">On les installe et on les règle avec vous.</div>
          <div id="s4c" class="ab bluebtn">Répondez à ce message</div>
        </div>
      </div>
    </div>

    <script>
      const tl = gsap.timeline({ paused: true });
      const Y1 = %%Y1%%, Y2 = %%Y2%%, T1 = %%T1%%, T2 = %%T2%%;

      function words(sel) {
        const el = document.querySelector(sel);
        const walk = (node) => {
          Array.from(node.childNodes).forEach((c) => {
            if (c.nodeType === 3) {
              const frag = document.createDocumentFragment();
              c.textContent.split(/(\s+)/).forEach((p) => {
                if (!p) return;
                if (/^\s+$/.test(p)) { frag.appendChild(document.createTextNode(p)); return; }
                const s = document.createElement('span'); s.className = 'w'; s.textContent = p; frag.appendChild(s);
              });
              node.replaceChild(frag, c);
            } else if (c.nodeType === 1) walk(c);
          });
        };
        walk(el);
        return el.querySelectorAll('.w');
      }
      function blurIn(sel, at, stag) {
        tl.fromTo(words(sel), { opacity: 0, y: 40, filter: 'blur(14px)' }, { opacity: 1, y: 0, filter: 'blur(0px)', duration: 0.6, stagger: stag || 0.07, ease: 'power3.out' }, at);
      }
      const sceneOut = (w, at) => tl.to(w, { opacity: 0, filter: 'blur(18px)', scale: 0.97, duration: 0.35, ease: 'power2.in' }, at);
      function drawLinks(pref, n, at) {
        for (let i = 0; i < n - 1; i++) {
          const p = document.getElementById(pref + 'l' + i);
          const L = p.getTotalLength();
          p.style.strokeDasharray = String(L);
          tl.fromTo(p, { strokeDashoffset: L }, { strokeDashoffset: 0, duration: 0.25, ease: 'none' }, at + i * 0.12);
        }
      }
      // Une étape : la légende change, le nœud s'allume, la coche apparaît, le point part vers le nœud suivant
      function runFlow(pref, Y, T, dotSel, capPref, tEnd) {
        T.forEach((t, i) => {
          const cap = '#' + capPref + i;
          tl.fromTo(cap, { opacity: 0, y: 30, filter: 'blur(12px)' }, { opacity: 1, y: 0, filter: 'blur(0px)', duration: 0.45, ease: 'power3.out' }, t);
          if (i < T.length - 1) tl.to(cap, { opacity: 0, y: -24, filter: 'blur(12px)', duration: 0.3, ease: 'power2.in' }, T[i + 1] - 0.3);
          tl.fromTo('#' + pref + 'r' + i, { opacity: 0 }, { opacity: 1, duration: 0.25 }, t);
          tl.to('#' + pref + 'n' + i, { scale: 1.04, duration: 0.2, ease: 'power2.out', yoyo: true, repeat: 1 }, t);
          tl.fromTo('#' + pref + 'k' + i, { opacity: 0 }, { opacity: 1, duration: 0.06 }, t + 0.55);
          tl.fromTo('#' + pref + 'k' + i, { scale: 0 }, { scale: 1, duration: 0.35, ease: 'expo.out' }, t + 0.55);
          tl.to('#' + pref + 'r' + i, { opacity: 0, duration: 0.3 }, (i < T.length - 1 ? T[i + 1] : tEnd) - 0.1);
          if (i < T.length - 1) {
            tl.set(dotSel, { y: Y[i] + 128 - 16, opacity: 1 }, t + 0.85);
            tl.to(dotSel, { y: Y[i + 1] - 16, duration: (T[i + 1] - t) - 1.0, ease: 'power1.inOut' }, t + 0.85);
            tl.set(dotSel, { opacity: 0 }, T[i + 1] - 0.1);
          }
        });
      }

      // fonds vivants
      gsap.utils.toArray('.blobA').forEach((b) => tl.fromTo(b, { x: 0, y: 0 }, { x: 140, y: 120, duration: 5, ease: 'sine.inOut', yoyo: true, repeat: 6 }, 0));
      gsap.utils.toArray('.blobB').forEach((b) => tl.fromTo(b, { x: 0, y: 0 }, { x: -160, y: -90, duration: 6, ease: 'sine.inOut', yoyo: true, repeat: 5 }, 0));
      ['#rings1', '#rings3', '#rings4'].forEach((r) => tl.fromTo(r, { scale: 0.92, transformOrigin: '50% 50%' }, { scale: 1.06, duration: 4, ease: 'sine.inOut', yoyo: true, repeat: 7 }, 0));
      tl.fromTo('.grid', { y: 0 }, { y: -48, duration: 16, ease: 'none' }, 4);

      // S1 (0 - 4)
      tl.fromTo('#orb', { opacity: 0, scale: 0.2 }, { opacity: 1, scale: 1, duration: 0.8, ease: 'expo.out' }, 0.2);
      tl.fromTo('#orbT', { opacity: 0, filter: 'blur(14px)', scale: 0.7 }, { opacity: 1, filter: 'blur(0px)', scale: 1, duration: 0.6, ease: 'expo.out' }, 0.6);
      tl.to('#orb', { scale: 1.06, duration: 0.6, ease: 'sine.inOut', yoyo: true, repeat: 3 }, 1.2);
      blurIn('#s1t', 0.9, 0.08);
      sceneOut('#s1w', 3.65);

      // S2 : automatisation 1 (4 - 20)
      tl.fromTo('#wf1', { opacity: 0, filter: 'blur(16px)' }, { opacity: 1, filter: 'blur(0px)', duration: 0.5 }, 4.0);
      tl.fromTo('#p1', { opacity: 0, y: -30 }, { opacity: 1, y: 0, duration: 0.5, ease: 'power3.out' }, 4.2);
      for (let i = 0; i < 7; i++) tl.fromTo('#an' + i, { opacity: 0, x: -120, filter: 'blur(10px)' }, { opacity: 1, x: 0, filter: 'blur(0px)', duration: 0.6, ease: 'expo.out' }, 4.5 + i * 0.1);
      drawLinks('a', 7, 5.3);
      tl.fromTo('#oui', { opacity: 0, scale: 0.5 }, { opacity: 1, scale: 1, duration: 0.4, ease: 'expo.out' }, T1[5] + 0.9);
      runFlow('a', Y1, T1, '#dot1', 'ac', 19.6);
      sceneOut('#wf1', 19.65);

      // S3 : automatisation 2 (20 - 29)
      tl.fromTo('#wf2', { opacity: 0, filter: 'blur(16px)' }, { opacity: 1, filter: 'blur(0px)', duration: 0.5 }, 20.0);
      tl.fromTo('#p2', { opacity: 0, y: -30 }, { opacity: 1, y: 0, duration: 0.5, ease: 'power3.out' }, 20.2);
      for (let i = 0; i < 5; i++) tl.fromTo('#bn' + i, { opacity: 0, x: 120, filter: 'blur(10px)' }, { opacity: 1, x: 0, filter: 'blur(0px)', duration: 0.6, ease: 'expo.out' }, 20.5 + i * 0.1);
      drawLinks('b', 5, 21.1);
      runFlow('b', Y2, T2, '#dot2', 'bc', 28.6);
      tl.fromTo('#toast', { opacity: 0, y: 80, scale: 0.9 }, { opacity: 1, y: 0, scale: 1, duration: 0.6, ease: 'expo.out' }, T2[4] + 0.7);
      sceneOut('#wf2', 28.65);

      // S4 : fin (29 - 35)
      tl.fromTo('#s4w', { opacity: 0, filter: 'blur(16px)' }, { opacity: 1, filter: 'blur(0px)', duration: 0.5 }, 29.0);
      blurIn('#s4t', 29.15, 0.07);
      tl.fromTo('#logoGlow', { opacity: 0, scale: 0.5 }, { opacity: 1, scale: 1, duration: 1.2, ease: 'power2.out' }, 29.6);
      tl.fromTo('#logo', { opacity: 0, scale: 0.7, filter: 'blur(16px)' }, { opacity: 1, scale: 1, filter: 'blur(0px)', duration: 0.9, ease: 'expo.out' }, 29.7);
      blurIn('#s4b', 30.6, 0.05);
      tl.fromTo('#s4c', { opacity: 0, scale: 0.7 }, { opacity: 1, scale: 1, duration: 0.6, ease: 'expo.out' }, 31.4);
      tl.to('#s4c', { scale: 1.04, duration: 0.5, ease: 'sine.inOut', yoyo: true, repeat: 3 }, 32.1);

      window.__timelines['main'] = tl;
    </script>
  </body>
</html>
