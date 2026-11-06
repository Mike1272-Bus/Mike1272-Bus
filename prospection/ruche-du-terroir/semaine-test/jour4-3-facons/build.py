"""Jour 4 : 3 façons d'utiliser le miel au quotidien (~32 s)."""
import os, re
HERE = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(HERE, "..", "jour1-cannelle-v2", "index.html")).read()
DUR = 32.0
css = src[:src.index('    </style>')] + '''
      .badge { position: absolute; left: 440px; top: 170px; width: 200px; height: 200px; border-radius: 50%; background: #1c1206; color: #ffd60a; font-size: 130px; font-weight: 900; line-height: 196px; text-align: center; box-shadow: 0 20px 36px rgba(0,0,0,0.3); }
      .fpot { position: absolute; left: 380px; top: 600px; width: 320px; height: 460px; object-fit: contain; filter: drop-shadow(0 30px 34px rgba(60,30,0,0.32)); }
      .use { height: 190px; } .use img { top: 20px; }
      .ua { top: 1120px; } .ub { top: 1340px; }
      .gpot { position: absolute; top: 780px; width: 190px; height: 300px; object-fit: contain; filter: drop-shadow(0 24px 26px rgba(60,30,0,0.3)); }
      #logo2 { left: 400px; top: 200px; width: 280px; height: 280px; border-radius: 50%; background: #fff url('assets/img/logo.png') center / 88% no-repeat; box-shadow: 0 30px 60px rgba(60,30,0,0.22); }
    </style>
  </head>'''
comb = lambda n: f'<svg class="comb" viewBox="0 0 1080 1920"><defs><pattern id="hx{n}" width="90" height="156" patternUnits="userSpaceOnUse"><path d="M45 0l45 26v52l-45 26-45-26V26zM0 104l45 26v52M90 104L45 130" fill="none" stroke="#c98a1c" stroke-width="3"/></pattern></defs><rect width="1080" height="1920" fill="url(#hx{n})"/></svg>'
swoosh = lambda d: f'<svg class="swoosh" viewBox="0 0 1680 2520"><path d="{d}" fill="none" stroke="#efe6d6" stroke-width="230" stroke-linecap="round"/></svg>'
T = {"s1": 0, "s2": 3.6, "s3": 6.6, "s4": 12.0, "s5": 17.4, "s6": 22.8, "s7": 27.6}
F = [  # (scène, numéro, titre, pot, [(icône, texte, sous-texte)])
    ("s3", 1, "Le matin", "cannelle", [("bread", "Sur le pain", "au petit-déjeuner"), ("pancakes", "Sur les crêpes", "ou les beignets")]),
    ("s4", 2, "Dans vos boissons", "gingembre", [("hot_beverage", "Thé ou café", "à la place du sucre"), ("lemon", "En citronnade", "bien fraîche")]),
    ("s5", 3, "En cuisine", "poivre-noir", [("poultry_leg", "En marinade", "pour le poulet ou le poisson"), ("green_salad", "Dans la salade", "une touche sucrée")]),
]
def facon(sc, n, title, pot, items):
    k = sc[1]
    rows = "".join(f'<div class="use {"ua" if j == 0 else "ub"}" id="u{k}{j}"><img src="assets/img/{ic}_3d.png" /><b>{t}</b><em>{e}</em><i id="ck{k}{j}"></i></div>' for j, (ic, t, e) in enumerate(items))
    size = 132 if len(title) < 10 else 104
    return f'''
      <div class="scene {"cream" if n % 2 else "white"}" id="{sc}"><div class="cam" id="k{k}">
        {comb(k) if n % 2 else swoosh("M1500 -100 C 900 800, 700 1300, 200 2600")}
        <div class="badge" id="n{k}">{n}</div>
        <div class="line" style="top:420px" data-layout-allow-overlap><span class="w big" id="t{k}" style="font-size:{size}px">{title}</span></div>
        <img class="fpot" id="p{k}" src="assets/img/pot-{pot}.png" />
        <img class="obj" id="sp{k}" src="assets/img/sparkles_3d.png" style="left:740px; top:620px; width:150px; height:150px" />
        {rows}
      </div></div>'''
gamme = ["cannelle", "gingembre", "hibiscus", "moringa", "poivre-noir", "clou-de-girofle", "sauvage-mai-ndombe"]
gx = [40 + i * 135 for i in range(7)]
gpots = "".join(f'<img class="gpot" id="gp{i}" src="assets/img/pot-{p}.png" style="left:{x}px; top:{760 + (i % 2) * 70}px; z-index:{10 - abs(3 - i)}" />' for i, (p, x) in enumerate(zip(gamme, gx)))
body = f'''
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="{DUR:g}" data-width="1080" data-height="1920">

      <!-- 1. Seulement pour le thé ? -->
      <div class="scene cream" id="s1"><div class="cam" id="k1">
        {comb(1)}
        <img class="obj" id="tea" src="assets/img/teacup_without_handle_3d.png" style="left:220px; top:380px; width:320px; height:320px" />
        <img class="obj" id="qm" src="assets/img/red_question_mark_3d.png" style="left:600px; top:330px; width:260px; height:260px" />
        <div class="line" style="top:820px"><span class="w sm" id="a1">Le</span><span class="w sm" id="a2">miel,</span><span class="w sm" id="a3">c'est</span><span class="w sm" id="a4">seulement</span></div>
        <div class="line" style="top:930px" data-layout-allow-overlap><span class="w big" id="a5">pour le thé ?</span></div>
      </div></div>

      <!-- 2. 3 façons -->
      <div class="scene white" id="s2"><div class="cam" id="k2">
        {swoosh("M200 -100 C 700 700, 1000 1300, 1500 2600")}
        <img class="obj" id="sr" src="assets/img/sunrise_3d.png" style="left:390px; top:360px; width:300px; height:300px" />
        <div class="line" style="top:740px"><span class="w sm" id="b1">Voici</span></div>
        <div class="line" style="top:840px" data-layout-allow-overlap><span class="w ext" id="b2">3 façons</span></div>
        <div class="line" style="top:1060px"><span class="w sm" id="b3">de</span><span class="w sm" id="b4">le</span><span class="w sm" id="b5">savourer</span></div>
        <div class="line" style="top:1150px"><span class="w sm" id="b6">chaque</span><span class="w sm" id="b7">jour</span></div>
      </div></div>
{"".join(facon(*f) for f in F)}

      <!-- 6. La gamme -->
      <div class="scene cream" id="s6"><div class="cam" id="k6">
        {comb(6)}
        <div class="ab" id="logo2"></div>
        <div class="line" style="top:530px"><span class="w sm" id="g1">Quel</span><span class="w sm" id="g2">parfum</span></div>
        <div class="line" style="top:630px" data-layout-allow-overlap><span class="w big" id="g3">pour vous ?</span></div>
        {gpots}
        <div class="line" style="top:1240px"><span class="w sm" id="g4">La</span><span class="w sm" id="g5">Ruche</span><span class="w sm" id="g6">du</span><span class="w sm" id="g7">Terroir</span></div>
        <div class="line" style="top:1350px" data-layout-allow-overlap><span class="w big" id="g8" style="font-size:100px">un miel gustatif</span></div>
        <div class="pill pa" id="g9" style="left:290px; top:1510px; width:500px">et soignant</div>
      </div></div>

      <!-- 7. WhatsApp -->
      <div class="scene white" id="s7"><div class="cam" id="k7">
        {swoosh("M200 -100 C 900 600, 500 1500, 1500 2600")}
        <div class="ab" id="ph"><div id="scr">
          <div id="hd"><div class="lg"></div><b>La Ruche du Terroir</b><span>Un miel gustatif et soignant</span></div>
          <div id="bub" data-layout-allow-overlap>Bonjour, je veux un pot de miel 🍯<span id="tm">08:10</span><span class="tk" id="tk0">✓✓</span><span class="tk" id="tk1">✓✓</span></div>
          <div id="inp"><span id="inp0">Message</span><span id="inp1">Je veux un pot de miel 🍯</span></div>
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
hexblock = src[src.index('      const hex = document.getElementById("hex")'):src.index('      IN("#band"')].replace("9.65 + dist", f'{T["s3"] - 0.35} + dist')
SFX = []
js = helpers + f'''      const SC = [{SC}];
      SC.forEach(([s, c, a, d], i) => {{
        HIDE.push(s);
        tl.set(s, {{ autoAlpha: 1 }}, a);
        if (i !== SC.length - 1) tl.set(s, {{ autoAlpha: 0 }}, a + d);
        FT(c, {{ scale: 1.14 }}, {{ scale: 1.0, duration: 0.45, ease: "expo.out" }}, a);
        FT(c, {{ rotation: 0, x: 0 }}, {{ rotation: i % 2 ? 0.8 : -0.8, x: i % 2 ? -20 : 20, duration: d, ease: "sine.inOut" }}, a);
      }});

      // 1. seulement pour le thé ?
      pop("#tea", 0.1); pop("#qm", 0.5); FT("#qm", {{ rotation: 0 }}, {{ rotation: 12, duration: 0.15, yoyo: true, repeat: 5 }}, 1.0);
      words(["#a1", "#a2", "#a3", "#a4"], 0.6, 0.12);
      slam("#a5", 1.3);

      // 2. 3 façons
      IN("#sr", {{ y: 200, scale: 0.5 }}, {{ y: 0, scale: 1, duration: 0.6, ease: "back.out(1.6)" }}, {T["s2"] + 0.05});
      word("#b1", {T["s2"] + 0.3});
      IN("#b2", {{ y: -300, scale: 1.4 }}, {{ y: 0, scale: 1, duration: 0.5, ease: "bounce.out" }}, {T["s2"] + 0.55});
      words(["#b3", "#b4", "#b5", "#b6", "#b7"], {T["s2"] + 1.1}, 0.12);

      // transition alvéoles
{hexblock}'''
SFX += [(0.1, "pop", 0.2), (0.5, "pop", 0.22), (1.3, "impact-bass-1", 0.28), (T["s2"], "whoosh", 0.3), (T["s2"] + 0.55, "impact-bass-2", 0.28), (T["s3"] - 0.4, "riser", 0.22), (T["s3"], "whoosh-cinematic", 0.35)]
for sc, n, title, pot, items in F:
    k = sc[1]; a = T[sc]
    js += f'''
      // façon {n}
      IN("#n{k}", {{ scale: 3, rotation: -30 }}, {{ scale: 1, rotation: 0, duration: 0.4, ease: "power4.out" }}, {a + 0.1});
      word("#t{k}", {a + 0.4}, 0.35);
      IN("#p{k}", {{ y: -1400, rotation: -10 }}, {{ y: 0, rotation: 0, duration: 0.6, ease: "bounce.out" }}, {a + 0.7});
      pop("#sp{k}", {a + 1.3}); float("#p{k}", {a + 1.4}, 3.0, -18);
      [0, 1].forEach(j => {{ IN("#u{k}" + j, {{ x: j ? 900 : -900 }}, {{ x: 0, duration: 0.45, ease: "expo.out" }}, {a + 1.6} + j * 1.5); FT("#u{k}" + j + " img", {{ scale: 0.2, rotation: -40 }}, {{ scale: 1, rotation: 0, duration: 0.45, ease: "back.out(2.5)" }}, {a + 1.7} + j * 1.5); IN("#ck{k}" + j, {{ scale: 0, rotation: -90 }}, {{ scale: 1, rotation: 0, duration: 0.4, ease: "back.out(2.5)" }}, {a + 2.2} + j * 1.5); }});'''
    SFX += [(a, "whoosh", 0.28), (a + 0.1, "impact-bass-1", 0.28), (a + 0.7, "whoosh-short", 0.2), (a + 1.3, "sparkle", 0.2),
            (a + 1.6, "whoosh-short", 0.22), (a + 2.2, "ping", 0.2), (a + 3.1, "whoosh-short", 0.22), (a + 3.7, "ping", 0.2)]
G = T["s6"]
js += f'''

      // 6. la gamme
      IN("#logo2", {{ scale: 0.3, rotation: -30 }}, {{ scale: 1, rotation: 0, duration: 0.5, ease: "back.out(1.8)" }}, {G + 0.05});
      words(["#g1", "#g2"], {G + 0.3}, 0.12); word("#g3", {G + 0.55}, 0.35);
      [0, 1, 2, 3, 4, 5, 6].forEach(i => IN("#gp" + i, {{ y: -1300, rotation: -15 + i * 5 }}, {{ y: 0, rotation: 0, duration: 0.5, ease: "bounce.out" }}, {G + 0.9} + i * 0.18));
      words(["#g4", "#g5", "#g6", "#g7"], {G + 2.4}, 0.1); word("#g8", {G + 2.85}, 0.35);
      IN("#g9", {{ scale: 0.4 }}, {{ scale: 1, duration: 0.4, ease: "back.out(2.2)" }}, {G + 3.3});
'''
SFX += [(G, "whoosh", 0.3), (G + 0.05, "pop", 0.22), (G + 0.55, "whoosh-short", 0.2)] + [(round(G + 0.95 + i * 0.18, 2), "pop", 0.14) for i in range(7)] + [(G + 2.85, "whoosh-short", 0.2), (G + 3.3, "pop", 0.22)]
shift = T["s7"] - 21.4
wjs = src[src.index('      // 7. WhatsApp'):]
wjs = re.sub(r'((?:\}|"|\]), )(2[1-4]\.\d+)(\)|, )', lambda m: f'{m.group(1)}{round(float(m.group(2)) + shift, 2)}{m.group(3)}', wjs)
wjs = wjs.replace('"#f1"', '"#f8"').replace('["#f2", "#f3"]', '["#f9", "#f10"]')
js += wjs
open(os.path.join(HERE, "index.html"), "w").write(css + body + js)
SFX += [(round(t + shift, 2), n, v) for t, n, v in [(21.4, "whoosh-cinematic", 0.3), (21.9, "typing", 0.3), (22.9, "click", 0.25), (23.05, "notification", 0.3), (23.2, "impact-bass-1", 0.2), (23.8, "pop", 0.25), (24.3, "chime", 0.3)]]
m = open(os.path.join(HERE, "mix.py")).read()
m = re.sub(r'"""Musique.*?"""', '"""Musique + bruitages du jour 4 (3 façons d\'utiliser le miel, 32 s), sans voix."""', m, flags=re.S)
m = re.sub(r'DUR = [\d.]+', f'DUR = {DUR}', m)
m = re.sub(r'SFX = \[.*?\]\n\nos', 'SFX = ' + repr(sorted((round(t, 2), n, v) for t, n, v in SFX)) + '\n\nos', m, flags=re.S)
open(os.path.join(HERE, "mix.py"), "w").write(m)
print("ok")
