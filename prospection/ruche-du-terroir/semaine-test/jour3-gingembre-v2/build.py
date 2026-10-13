"""Jour 3 : miel au gingembre (~30 s). Construit index.html et la liste des bruitages de mix.py."""
import os, re
HERE = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(HERE, "..", "jour1-cannelle-v2", "index.html")).read()
DUR = 30.0
css = src[:src.index('    </style>')].replace('data-duration="25"', f'data-duration="{DUR:g}"') + '''
      .duo { position: absolute; top: 640px; width: 420px; height: 560px; border-radius: 44px; background: #fff; border: 3px solid #eadfcb; box-shadow: 0 18px 36px rgba(60,30,0,0.12); text-align: center; }
      .duo img { position: absolute; left: 85px; top: 50px; width: 250px; height: 250px; filter: drop-shadow(0 18px 20px rgba(60,30,0,0.25)); }
      .duo b { position: absolute; left: 0; top: 340px; width: 420px; font-size: 92px; font-weight: 900; letter-spacing: -0.04em; color: #f29a0e; text-shadow: 0 5px 0 #9c5200; }
      .duo em { position: absolute; left: 0; top: 460px; width: 420px; font-style: normal; font-size: 34px; font-weight: 600; color: #8a6a3a; }
      #plus { left: 490px; top: 850px; width: 100px; height: 100px; border-radius: 50%; background: #1c1206; color: #ffd60a; font-size: 80px; font-weight: 900; line-height: 92px; text-align: center; }
      .root-ic { position: absolute; width: 170px; height: 170px; filter: drop-shadow(0 16px 20px rgba(60,30,0,0.3)); }
      .use { height: 190px; } .use img { top: 20px; }
      #u1 { top: 640px; } #u2 { top: 860px; } #u3 { top: 1080px; } #u4 { top: 1300px; }
    </style>
  </head>'''
comb = lambda n: f'<svg class="comb" viewBox="0 0 1080 1920"><defs><pattern id="hx{n}" width="90" height="156" patternUnits="userSpaceOnUse"><path d="M45 0l45 26v52l-45 26-45-26V26zM0 104l45 26v52M90 104L45 130" fill="none" stroke="#c98a1c" stroke-width="3"/></pattern></defs><rect width="1080" height="1920" fill="url(#hx{n})"/></svg>'
T = {"s1": 0, "s2": 3.6, "s3": 7.0, "s4": 11.6, "s5": 15.0, "s6": 22.6, "s7": 25.8}
USES = [("lemon", "En citronnade", "bien fraîche"), ("teacup_without_handle", "Dans le thé", "chaud ou glacé"), ("pancakes", "Sur les crêpes", "au petit-déjeuner"), ("cuillere_miel", "À la cuillère", "")]
uses = "".join(f'<div class="use" id="u{i+1}"><img src="assets/img/{ic}{"" if ic == "cuillere_miel" else "_3d"}.png" /><b>{t}</b>' + (f'<em>{e}</em>' if e else '') + f'<i id="ck{i+1}"></i></div>' for i, (ic, t, e) in enumerate(USES))
body = f'''
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="{DUR:g}" data-width="1080" data-height="1920">

      <!-- 1. Il fait chaud -->
      <div class="scene cream" id="s1"><div class="cam" id="k1">
        {comb(1)}
        <img class="obj" id="sun" src="assets/img/sun_3d.png" style="left:200px; top:330px; width:300px; height:300px" />
        <img class="obj" id="thm" src="assets/img/thermometer_3d.png" style="left:600px; top:350px; width:260px; height:260px" />
        <div class="line" style="top:760px"><span class="w sm" id="a1">Il</span><span class="w sm" id="a2">fait</span><span class="w sm" id="a3">chaud…</span></div>
        <div class="line" style="top:870px"><span class="w sm" id="a4">envie</span><span class="w sm" id="a5">de</span></div>
        <div class="line" style="top:980px" data-layout-allow-overlap><span class="w ext" id="a6" style="font-size:160px">fraîcheur ?</span></div>
        <img class="obj" id="cup" src="assets/img/cup_with_straw_3d.png" style="left:410px; top:1270px; width:260px; height:260px" />
      </div></div>

      <!-- 2. Un peu de piquant -->
      <div class="scene white" id="s2"><div class="cam" id="k2">
        <svg class="swoosh" viewBox="0 0 1680 2520"><path d="M200 -100 C 700 700, 1000 1300, 1500 2600" fill="none" stroke="#efe6d6" stroke-width="230" stroke-linecap="round"/></svg>
        <img class="obj" id="gr" src="assets/img/ginger_root_3d.png" style="left:340px; top:380px; width:400px; height:400px" />
        <img class="obj" id="fi" src="assets/img/fire_3d.png" style="left:720px; top:330px; width:180px; height:180px" />
        <div class="line" style="top:880px"><span class="w sm" id="b1">Et</span><span class="w sm" id="b2">si</span><span class="w sm" id="b3">on</span><span class="w sm" id="b4">ajoutait</span></div>
        <div class="line" style="top:990px" data-layout-allow-overlap><span class="w big" id="b5">du piquant ?</span></div>
      </div></div>

      <!-- 3. Miel au gingembre -->
      <div class="scene cream" id="s3"><div class="cam" id="k3">
        {comb(3)}
        <div class="ab" id="band"></div>
        <div class="drip" id="dr1" style="left:70px; height:260px"></div>
        <div class="drip" id="dr2" style="left:250px; height:150px"></div>
        <div class="drip" id="dr3" style="left:770px; height:200px"></div>
        <div class="drip" id="dr4" style="left:950px; height:300px"></div>
        <div class="line" style="top:250px"><span class="w sm" id="c1">Miel</span><span class="w sm" id="c2">au</span></div>
        <div class="line" style="top:345px" data-layout-allow-overlap><span class="w ext" id="c4">gingembre</span></div>
        <img class="root-ic" id="g1" src="assets/img/ginger_root_3d.png" style="left:60px; top:820px" />
        <img class="root-ic" id="g2" src="assets/img/ginger_root_3d.png" style="left:850px; top:900px" />
        <img class="root-ic" id="g3" src="assets/img/ginger_root_3d.png" style="left:100px; top:1300px" />
        <div class="ab" id="potw"><div id="pot"></div><div id="shine"></div></div>
        <img class="obj" id="sp1" src="assets/img/sparkles_3d.png" style="left:800px; top:600px; width:170px; height:170px" />
        <img class="obj" id="sp2" src="assets/img/sparkles_3d.png" style="left:110px; top:560px; width:130px; height:130px" />
      </div></div>

      <!-- 4. Doux et piquant -->
      <div class="scene white" id="s4"><div class="cam" id="k4">
        <svg class="swoosh" viewBox="0 0 1680 2520"><path d="M1500 -100 C 900 800, 700 1300, 200 2600" fill="none" stroke="#efe6d6" stroke-width="230" stroke-linecap="round"/></svg>
        <div class="line" style="top:330px"><span class="w sm" id="d1">Un</span><span class="w sm" id="d2">goût</span><span class="w sm" id="d3">unique</span></div>
        <div class="duo" id="dd1" style="left:60px"><img src="assets/img/honey_pot_3d.png" /><b>Doux</b><em>comme le miel</em></div>
        <div class="ab" id="plus">+</div>
        <div class="duo" id="dd2" style="left:600px"><img src="assets/img/ginger_root_3d.png" /><b>Piquant</b><em>comme le gingembre</em></div>
        <div class="pill pa" id="d7" style="left:290px; top:1300px; width:500px">à la fois</div>
      </div></div>

      <!-- 5. Comment le savourer -->
      <div class="scene cream" id="s5"><div class="cam" id="k5">
        {comb(5)}
        <div class="line" style="top:300px"><span class="w sm" id="e1">Comment</span><span class="w sm" id="e2">le</span></div>
        <div class="line" style="top:410px" data-layout-allow-overlap><span class="w big" id="e3">savourer ?</span></div>
        {uses}
      </div></div>

      <!-- 6. Gustatif et soignant -->
      <div class="scene white" id="s6"><div class="cam" id="k6">
        <svg class="swoosh" viewBox="0 0 1680 2520"><path d="M200 -100 C 700 700, 1000 1300, 1500 2600" fill="none" stroke="#efe6d6" stroke-width="230" stroke-linecap="round"/></svg>
        <div class="ab" id="logo2" style="left:390px; top:260px; width:300px; height:300px; border-radius:50%; background:#fff url('assets/img/logo.png') center / 88% no-repeat; box-shadow:0 30px 60px rgba(60,30,0,0.22)"></div>
        <div class="line" style="top:640px"><span class="w sm" id="f1">La</span><span class="w sm" id="f2">Ruche</span><span class="w sm" id="f3">du</span><span class="w sm" id="f4">Terroir</span></div>
        <div class="line" style="top:770px" data-layout-allow-overlap><span class="w big" id="f6" style="font-size:108px">un miel gustatif</span></div>
        <div class="pill pa" id="f7" style="left:290px; top:950px; width:500px">et soignant</div>
        <img class="obj" id="pot2" src="assets/img/pot.png" style="left:400px; top:1120px; width:280px; height:400px; object-fit:contain" />
      </div></div>

      <!-- 7. WhatsApp -->
      <div class="scene white" id="s7"><div class="cam" id="k7">
        <svg class="swoosh" viewBox="0 0 1680 2520"><path d="M200 -100 C 900 600, 500 1500, 1500 2600" fill="none" stroke="#efe6d6" stroke-width="230" stroke-linecap="round"/></svg>
        <div class="ab" id="ph"><div id="scr">
          <div id="hd"><div class="lg"></div><b>La Ruche du Terroir</b><span>Un miel gustatif et soignant</span></div>
          <div id="bub" data-layout-allow-overlap>Bonjour, je veux le miel au gingembre 🍯<span id="tm">13:05</span><span class="tk" id="tk0">✓✓</span><span class="tk" id="tk1">✓✓</span></div>
          <div id="inp"><span id="inp0">Message</span><span id="inp1">Je veux le miel au gingembre 🍯</span></div>
          <div id="send"></div>
        </div></div>
        <div class="line" style="top:1225px" data-layout-allow-overlap><span class="w big" id="f8">Commandez</span></div>
        <div class="line" style="top:1385px"><span class="w sm" id="f9">sur</span><span class="w sm" id="f10">WhatsApp</span></div>
        <div class="pill pg" id="num">+243 859 072 956</div>
      </div></div>

      <svg class="ab" id="hex" viewBox="0 0 1080 1920"></svg>
      <div class="ab" id="fade"></div>
      <audio id="mix" src="assets/audio/mix.wav" data-start="0" data-duration="{DUR:g}" data-track-index="1" data-volume="1"></audio>
    </div>
'''
s = src[src.index('    <script>'):]
helpers = s[:s.index('      const SC =')]
keys = list(T)
SC = ", ".join(f'["#{k}", "#k{k[1]}", {T[k]}, {round((T[keys[i+1]] if i + 1 < len(keys) else DUR) - T[k], 2)}]' for i, k in enumerate(keys))
hexblock = src[src.index('      const hex = document.getElementById("hex")'):src.index('      IN("#band"')]
hexblock = hexblock.replace("9.65 + dist", f'{T["s3"] - 0.35} + dist')
u0 = T["s5"] + 1.0
js = helpers + f'''      const SC = [{SC}];
      SC.forEach(([s, c, a, d], i) => {{
        HIDE.push(s);
        tl.set(s, {{ autoAlpha: 1 }}, a);
        if (i !== SC.length - 1) tl.set(s, {{ autoAlpha: 0 }}, a + d);
        FT(c, {{ scale: 1.14 }}, {{ scale: 1.0, duration: 0.45, ease: "expo.out" }}, a);
        FT(c, {{ rotation: 0, x: 0 }}, {{ rotation: i % 2 ? 0.8 : -0.8, x: i % 2 ? -20 : 20, duration: d, ease: "sine.inOut" }}, a);
      }});

      // 1. il fait chaud
      IN("#sun", {{ y: 200, scale: 0.5 }}, {{ y: 0, scale: 1, duration: 0.6, ease: "back.out(1.6)" }}, 0.1);
      FT("#sun", {{ rotation: 0 }}, {{ rotation: 40, duration: 3.4, ease: "none" }}, 0.1);
      pop("#thm", 0.4); FT("#thm", {{ rotation: 0 }}, {{ rotation: 8, duration: 0.12, yoyo: true, repeat: 5 }}, 1.0);
      words(["#a1", "#a2", "#a3"], 0.6); words(["#a4", "#a5"], 1.2);
      IN("#a6", {{ y: -300, scale: 1.4 }}, {{ y: 0, scale: 1, duration: 0.5, ease: "bounce.out" }}, 1.6);
      pop("#cup", 2.2); float("#cup", 2.6, 1.0, -18);

      // 2. du piquant
      IN("#gr", {{ scale: 0.2, rotation: -60 }}, {{ scale: 1, rotation: 0, duration: 0.6, ease: "back.out(1.8)" }}, {T["s2"] + 0.1});
      pop("#fi", {T["s2"] + 0.7}); FT("#fi", {{ scale: 1 }}, {{ scale: 1.15, duration: 0.2, yoyo: true, repeat: 5 }}, {T["s2"] + 1.2});
      words(["#b1", "#b2", "#b3", "#b4"], {T["s2"] + 0.5}, 0.12);
      slam("#b5", {T["s2"] + 1.2});
      FT("#k2", {{ x: 0 }}, {{ x: 14, duration: 0.05, yoyo: true, repeat: 7 }}, {T["s2"] + 1.55});

      // transition alvéoles
{hexblock}
      // 3. miel au gingembre
      IN("#band", {{ y: -80 }}, {{ y: 0, duration: 0.3, ease: "power2.out" }}, {T["s3"] + 0.15});
      ["#dr1", "#dr2", "#dr3", "#dr4"].forEach((d, i) => {{ HIDE.push(d); FT(d, {{ autoAlpha: 1, scaleY: 0 }}, {{ scaleY: 1, duration: 1.6, ease: "power1.in" }}, {T["s3"] + 0.3} + i * 0.15); }});
      IN("#potw", {{ y: -1500, rotation: -12 }}, {{ y: 0, rotation: 0, duration: 0.6, ease: "bounce.out" }}, {T["s3"] + 0.4});
      FT("#k3", {{ scale: 1 }}, {{ scale: 1.06, duration: 0.12, yoyo: true, repeat: 1, ease: "power2.out" }}, {T["s3"] + 0.85});
      ["#g1", "#g2", "#g3"].forEach((g, i) => IN(g, {{ y: -1400, rotation: -80 + i * 60 }}, {{ y: 0, rotation: [-18, 22, 10][i], duration: 0.7, ease: "power2.in" }}, {T["s3"] + 0.8} + i * 0.15));
      words(["#c1", "#c2"], {T["s3"] + 1.1}, 0.12);
      IN("#c4", {{ y: -300, scale: 1.4 }}, {{ y: 0, scale: 1, duration: 0.5, ease: "bounce.out" }}, {T["s3"] + 1.4});
      FT("#shine", {{ backgroundPosition: "100% 0%" }}, {{ backgroundPosition: "-50% 0%", duration: 0.9, ease: "power2.inOut" }}, {T["s3"] + 1.9});
      pop("#sp1", {T["s3"] + 2.1}); pop("#sp2", {T["s3"] + 2.3});
      float("#potw", {T["s3"] + 2.4}, 2.0, -20);
      FT("#shine", {{ backgroundPosition: "100% 0%" }}, {{ backgroundPosition: "-50% 0%", duration: 0.9, ease: "power2.inOut" }}, {T["s3"] + 3.4});

      // 4. doux et piquant
      words(["#d1", "#d2", "#d3"], {T["s4"] + 0.1}, 0.12);
      IN("#dd1", {{ x: -700, rotation: -8 }}, {{ x: 0, rotation: -2, duration: 0.5, ease: "expo.out" }}, {T["s4"] + 0.5});
      pop("#plus", {T["s4"] + 1.1});
      IN("#dd2", {{ x: 700, rotation: 8 }}, {{ x: 0, rotation: 2, duration: 0.5, ease: "expo.out" }}, {T["s4"] + 1.5});
      FT("#dd2", {{ x: 0 }}, {{ x: 10, duration: 0.05, yoyo: true, repeat: 5 }}, {T["s4"] + 2.0});
      IN("#d7", {{ scale: 0.4 }}, {{ scale: 1, duration: 0.4, ease: "back.out(2.2)" }}, {T["s4"] + 2.3});

      // 5. comment le savourer (un par un)
      words(["#e1", "#e2"], {T["s5"] + 0.1}, 0.15); word("#e3", {T["s5"] + 0.4}, 0.35);
      [["#u1", "#ck1"], ["#u2", "#ck2"], ["#u3", "#ck3"], ["#u4", "#ck4"]].forEach(([u, c], i) => {{
        IN(u, {{ x: i % 2 ? 900 : -900 }}, {{ x: 0, duration: 0.45, ease: "expo.out" }}, {u0} + i * 1.4);
        FT(u + " img", {{ scale: 0.2, rotation: -40 }}, {{ scale: 1, rotation: 0, duration: 0.45, ease: "back.out(2.5)" }}, {u0 + 0.1} + i * 1.4);
        IN(c, {{ scale: 0, rotation: -90 }}, {{ scale: 1, rotation: 0, duration: 0.4, ease: "back.out(2.5)" }}, {u0 + 0.6} + i * 1.4);
      }});

      // 6. gustatif et soignant
      IN("#logo2", {{ scale: 0.3, rotation: -30 }}, {{ scale: 1, rotation: 0, duration: 0.55, ease: "back.out(1.8)" }}, {T["s6"] + 0.05});
      words(["#f1", "#f2", "#f3", "#f4"], {T["s6"] + 0.45}, 0.12); word("#f6", {T["s6"] + 1.05}, 0.35);
      IN("#f7", {{ scale: 0.4 }}, {{ scale: 1, duration: 0.4, ease: "back.out(2.2)" }}, {T["s6"] + 1.55});
      IN("#pot2", {{ y: 900 }}, {{ y: 0, duration: 0.5, ease: "back.out(1.4)" }}, {T["s6"] + 1.8});
'''
shift = T["s7"] - 21.4
wjs = src[src.index('      // 7. WhatsApp'):]
wjs = re.sub(r'((?:\}|"|\]), )(2[1-4]\.\d+)(\)|, )', lambda m: f'{m.group(1)}{round(float(m.group(2)) + shift, 2)}{m.group(3)}', wjs)
wjs = wjs.replace('"#f1"', '"#f8"').replace('["#f2", "#f3"]', '["#f9", "#f10"]')
js += wjs
open(os.path.join(HERE, "index.html"), "w").write(css + body + js)

S = T["s2"]; C = T["s3"]; D = T["s4"]; E = T["s5"]; G = T["s6"]
SFX = [(0.1, "whoosh", 0.25), (0.4, "pop", 0.2), (1.0, "click-soft", 0.2), (1.6, "impact-bass-1", 0.25), (2.2, "pop", 0.2),
       (S, "whoosh", 0.3), (S + 0.1, "pop", 0.22), (S + 0.7, "pop", 0.18), (S + 1.2, "impact-bass-2", 0.3), (S + 1.55, "riser", 0.2),
       (C - 0.4, "riser", 0.22), (C, "whoosh-cinematic", 0.35), (C + 0.85, "impact-bass-2", 0.3), (C + 0.9, "pop", 0.15), (C + 1.05, "pop", 0.15), (C + 1.4, "whoosh-short", 0.25), (C + 1.9, "sparkle", 0.25), (C + 2.1, "pop", 0.18), (C + 3.4, "sparkle", 0.18),
       (D, "whoosh", 0.3), (D + 0.5, "whoosh-short", 0.25), (D + 1.1, "pop", 0.25), (D + 1.5, "whoosh-short", 0.25), (D + 2.3, "pop", 0.22),
       (E, "whoosh", 0.3)] + [(round(u0 + i * 1.4, 2), "whoosh-short", 0.22) for i in range(4)] + [(round(u0 + 0.6 + i * 1.4, 2), "ping", 0.2) for i in range(4)] + [
       (G, "whoosh", 0.3), (G + 0.05, "pop", 0.22), (G + 1.05, "whoosh-short", 0.22), (G + 1.55, "pop", 0.22), (G + 1.8, "whoosh-short", 0.2)] + [
       (round(t + shift, 2), n, v) for t, n, v in [(21.4, "whoosh-cinematic", 0.3), (21.9, "typing", 0.3), (22.9, "click", 0.25), (23.05, "notification", 0.3), (23.2, "impact-bass-1", 0.2), (23.8, "pop", 0.25), (24.3, "chime", 0.3)]]
m = open(os.path.join(HERE, "mix.py")).read()
m = m.replace("du jour 1 v2 (texte du client, 25 s)", "du jour 3 v2 (miel au gingembre, 30 s)")
m = re.sub(r'DUR = [\d.]+', f'DUR = {DUR}', m)
m = re.sub(r'SFX = \[.*?\]\n\nos', 'SFX = ' + repr(sorted((round(t, 2), n, v) for t, n, v in SFX)) + '\n\nos', m, flags=re.S)
open(os.path.join(HERE, "mix.py"), "w").write(m)
print("ok")
