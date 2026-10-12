"""Construit index.html du jour 2 (paniers) à partir du modèle jour1-cannelle-v2. Durée ~36 s."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(HERE, "..", "jour1-cannelle-v2", "index.html")).read()
head = src[:src.index('      /* tasse et vapeur */')].replace('data-duration="25"', 'data-duration="36"')
keep = src[src.index('      /* photo client */'):src.index('      /* façons de le savourer */')]
wa = src[src.index('      /* WhatsApp */'):src.index('    </style>')]
DUR = 36.0
css = head + keep.replace("cannelle_photo.jpg", "panier_photo.jpg").replace("width: 660px; height: 660px", "width: 700px; height: 570px") + '''
      #band { left: 0; top: 0; width: 1080px; height: 70px; background: linear-gradient(180deg, #d98200, #f5a623); }
      .drip { position: absolute; top: 40px; width: 52px; border-radius: 0 0 26px 26px; background: linear-gradient(90deg, #e08a00, #f7b23b 40%, #e08a00); transform-origin: 50% 0%; }
      .drip::after { content: ""; position: absolute; left: 12px; top: 10px; width: 10px; height: 40%; border-radius: 5px; background: rgba(255,255,255,0.45); }
      #spoon { left: 270px; top: 720px; width: 540px; height: 540px; filter: drop-shadow(0 36px 40px rgba(60,30,0,0.35)); }
      #logo2 { left: 360px; top: 300px; width: 360px; height: 360px; border-radius: 50%; background: #fff url('assets/img/logo.png') center / 88% no-repeat; box-shadow: 0 30px 60px rgba(60,30,0,0.22); }

      /* paniers */
      .hdr { position: absolute; left: 90px; top: 190px; width: 900px; height: 180px; border-radius: 44px; font-weight: 900; font-size: 104px; letter-spacing: -0.04em; line-height: 180px; text-align: center; white-space: nowrap; }
      .h-or { background: linear-gradient(180deg, #ffe14d, #ffcc00); color: #2a1a00; box-shadow: 0 12px 0 #c99a00, 0 26px 40px rgba(60,30,0,0.25); }
      .h-pl { background: linear-gradient(180deg, #ff3d7f, #d90f57); color: #fff; box-shadow: 0 12px 0 #8f0838, 0 26px 40px rgba(60,0,20,0.25); }
      .h-di { background: linear-gradient(180deg, #ff7a3d, #e04a17); color: #fff; box-shadow: 0 12px 0 #962c08, 0 26px 40px rgba(60,20,0,0.25); }
      .jar { position: absolute; top: 430px; height: 400px; width: 270px; background-position: center bottom; background-size: contain; background-repeat: no-repeat; filter: drop-shadow(0 28px 30px rgba(60,30,0,0.32)); }
      .cnt { position: absolute; left: 860px; top: 360px; width: 170px; height: 170px; border-radius: 50%; background: #1c1206; color: #ffd60a; font-weight: 900; font-size: 92px; line-height: 170px; text-align: center; box-shadow: 0 16px 30px rgba(0,0,0,0.3); letter-spacing: -0.04em; }
      .cnt span { position: absolute; left: 0; top: 0; width: 170px; text-align: center; }
      .box { position: absolute; left: 70px; top: 880px; width: 940px; height: 820px; border-radius: 44px; background: #fff; border: 3px solid #eadfcb; box-shadow: 0 18px 36px rgba(60,30,0,0.12); }
      .box h4 { position: absolute; left: 0; top: 38px; width: 940px; text-align: center; font-size: 40px; font-weight: 800; color: #c66f00; }
      .it { position: absolute; left: 34px; width: 870px; height: 128px; }
      .it img { position: absolute; left: 0; top: 4px; width: 118px; height: 118px; filter: drop-shadow(0 10px 12px rgba(60,30,0,0.25)); }
      .it b { position: absolute; left: 140px; top: 22px; font-size: 46px; font-weight: 900; letter-spacing: -0.03em; color: #1c1206; white-space: nowrap; }
      .it em { position: absolute; left: 142px; top: 80px; font-style: normal; font-size: 30px; font-weight: 600; color: #8a6a3a; white-space: nowrap; }
      .tri { position: absolute; height: 110px; border-radius: 55px; font-weight: 900; font-size: 54px; line-height: 110px; text-align: center; white-space: nowrap; }
''' + wa
P = {"or": ("Panier Or", "h-or", 2, "1 produit d'accompagnement", "1 produit offert"),
     "pl": ("Panier Platine", "h-pl", 3, "1 produit d'accompagnement", "2 produits offerts"),
     "di": ("Panier Diamant", "h-di", 4, "2 produits d'accompagnement", "2 produits offerts")}
ITEMS = lambda pots, acc, off: [("honey_pot", f"{pots} pots de miel", "de variétés différentes"),
                                ("package", acc, "pour accompagner votre miel"),
                                ("wrapped_gift", off, "en cadeau"),
                                ("open_book", "1 guide de consommation", "comment et quand le prendre"),
                                ("page_facing_up", "1 flyer", "")]
def card(k, n):
    name, cls, pots, acc, off = P[k]
    W, gap = (270, -20) if pots < 4 else (235, -5)
    x0 = (1080 - (pots * W + (pots - 1) * gap)) // 2
    jars = "".join(f'<div class="jar" id="{k}j{i}" style="width:{W}px; left:{x0 + i * (W + gap)}px; background-image:url(\'assets/img/pot{i + 1}.png\')"></div>' for i in range(pots))
    cnt = f'<div class="cnt" id="{k}c"' + (' style="top:285px; left:880px"' if pots == 4 else '') + '>' + "".join(f'<span id="{k}c{i + 1}">{i + 1}</span>' for i in range(pots)) + '</div>'
    rows = "".join(f'<div class="it" id="{k}i{j}" style="top:{110 + j * 136}px"><img src="assets/img/{ic}_3d.png" /><b>{t}</b>' + (f'<em>{e}</em>' if e else '') + '</div>' for j, (ic, t, e) in enumerate(ITEMS(pots, acc, off)))
    return f'''
      <div class="scene cream" id="s{n}"><div class="cam" id="k{n}">
        <svg class="comb" viewBox="0 0 1080 1920"><defs><pattern id="hx{n}" width="90" height="156" patternUnits="userSpaceOnUse"><path d="M45 0l45 26v52l-45 26-45-26V26zM0 104l45 26v52M90 104L45 130" fill="none" stroke="#c98a1c" stroke-width="3"/></pattern></defs><rect width="1080" height="1920" fill="url(#hx{n})"/></svg>
        <div class="hdr {cls}" id="{k}h">{name}</div>
        {jars}
        {cnt}
        <div class="box" id="{k}b"><h4>Notre paquet livrable est composé de :</h4>{rows}</div>
      </div></div>'''
comb = lambda n: f'<svg class="comb" viewBox="0 0 1080 1920"><defs><pattern id="hx{n}" width="90" height="156" patternUnits="userSpaceOnUse"><path d="M45 0l45 26v52l-45 26-45-26V26zM0 104l45 26v52M90 104L45 130" fill="none" stroke="#c98a1c" stroke-width="3"/></pattern></defs><rect width="1080" height="1920" fill="url(#hx{n})"/></svg>'
# découpage (s) : 1 offre 0-4 | 2 paniers 4-8 | Or 8-15 | Platine 15-22 | Diamant 22-29.5 | signature 29.5-32.5 | WhatsApp 32.5-36
T = {"s1": 0, "s2": 4.0, "or": 8.0, "pl": 15.0, "di": 22.0, "s6": 29.5, "s7": 32.5}
body = f'''
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="{DUR:g}" data-width="1080" data-height="1920">

      <!-- 1. Offre de vente, miel soignant -->
      <div class="scene cream" id="s1"><div class="cam" id="k1">
        {comb(1)}
        <div class="ab" id="band"></div>
        <div class="drip" id="dr1" style="left:70px; height:260px"></div>
        <div class="drip" id="dr2" style="left:250px; height:150px"></div>
        <div class="drip" id="dr3" style="left:770px; height:200px"></div>
        <div class="drip" id="dr4" style="left:950px; height:300px"></div>
        <div class="line" style="top:330px"><span class="w sm" id="a1">Offre</span><span class="w sm" id="a2">de</span><span class="w sm" id="a3">vente</span></div>
        <div class="line" style="top:440px" data-layout-allow-overlap><span class="w ext" id="a4" style="font-size:150px">Miel soignant</span></div>
        <img class="obj" id="spoon" src="assets/img/cuillere_miel.png" />
        <img class="obj" id="sp1" src="assets/img/sparkles_3d.png" style="left:800px; top:700px; width:170px; height:170px" />
        <img class="obj" id="sp2" src="assets/img/sparkles_3d.png" style="left:110px; top:1250px; width:130px; height:130px" />
      </div></div>

      <!-- 2. Les paniers -->
      <div class="scene white" id="s2"><div class="cam" id="k2">
        <svg class="swoosh" viewBox="0 0 1680 2520"><path d="M1500 -100 C 900 800, 700 1300, 200 2600" fill="none" stroke="#efe6d6" stroke-width="230" stroke-linecap="round"/></svg>
        <div class="ab" id="photo"><div id="phi"></div></div>
        <div class="line" style="top:1000px" data-layout-allow-overlap><span class="w big" id="b1">Les paniers</span></div>
        <div class="tri h-or" id="t1" style="left:90px; top:1240px; width:250px">Or</div>
        <div class="tri h-pl" id="t2" style="left:370px; top:1240px; width:340px">Platine</div>
        <div class="tri h-di" id="t3" style="left:740px; top:1240px; width:250px; font-size:46px">Diamant</div>
        <img class="obj" id="gift" src="assets/img/wrapped_gift_3d.png" style="left:430px; top:1450px; width:220px; height:220px" />
      </div></div>
{card("or", 3)}
{card("pl", 4)}
{card("di", 5)}

      <!-- 6. Gustatif et soignant -->
      <div class="scene white" id="s6"><div class="cam" id="k6">
        <svg class="swoosh" viewBox="0 0 1680 2520"><path d="M200 -100 C 700 700, 1000 1300, 1500 2600" fill="none" stroke="#efe6d6" stroke-width="230" stroke-linecap="round"/></svg>
        <div class="ab" id="logo2"></div>
        <div class="line" style="top:800px"><span class="w sm" id="d1">La</span><span class="w sm" id="d2">Ruche</span><span class="w sm" id="d3">du</span><span class="w sm" id="d4">Terroir</span></div>
        <div class="line" style="top:930px" data-layout-allow-overlap><span class="w big" id="d6" style="font-size:108px">un miel gustatif</span></div>
        <div class="pill pa" id="d7" style="left:290px; top:1110px; width:500px">et soignant</div>
        <img class="obj" id="hp" src="assets/img/honey_pot_3d.png" style="left:420px; top:1300px; width:240px; height:240px" />
      </div></div>

      <!-- 7. Commande sur WhatsApp -->
      <div class="scene white" id="s7"><div class="cam" id="k7">
        <svg class="swoosh" viewBox="0 0 1680 2520"><path d="M200 -100 C 900 600, 500 1500, 1500 2600" fill="none" stroke="#efe6d6" stroke-width="230" stroke-linecap="round"/></svg>
        <div class="ab" id="ph"><div id="scr">
          <div id="hd"><div class="lg"></div><b>La Ruche du Terroir</b><span>Un miel gustatif et soignant</span></div>
          <div id="bub" data-layout-allow-overlap>Bonjour, je veux le Panier Or 🎁<span id="tm">09:15</span><span class="tk" id="tk0">✓✓</span><span class="tk" id="tk1">✓✓</span></div>
          <div id="inp"><span id="inp0">Message</span><span id="inp1">Je veux le Panier Or 🎁</span></div>
          <div id="send"></div>
        </div></div>
        <div class="line" style="top:1225px" data-layout-allow-overlap><span class="w big" id="f1">Commandez</span></div>
        <div class="line" style="top:1385px"><span class="w sm" id="f2">votre</span><span class="w sm" id="f3">panier</span></div>
        <div class="pill pg" id="num">+243 859 072 956</div>
      </div></div>

      <svg class="ab" id="hex" viewBox="0 0 1080 1920"></svg>
      <div class="ab" id="fade"></div>
      <audio id="mix" src="assets/audio/mix.wav" data-start="0" data-duration="{DUR:g}" data-track-index="1" data-volume="1"></audio>
    </div>
'''
s = src[src.index('    <script>'):]
helpers = s[:s.index('      const SC =')]
SFX = []
def cardjs(k, a, pots):
    js = f'''
      // {k}
      IN("#{k}h", {{ scale: 2, filter: "blur(14px)" }}, {{ scale: 1, filter: "blur(0px)", duration: 0.35, ease: "power4.out" }}, {a + 0.05});'''
    SFX.extend([(a, "whoosh", 0.28), (a + 0.05, "impact-bass-1", 0.25)])
    for i in range(pots):
        t = round(a + 0.45 + i * 0.5, 2)
        js += f'''
      IN("#{k}j{i}", {{ y: -1300, rotation: {-12 + i * 8} }}, {{ y: 0, rotation: 0, duration: 0.5, ease: "bounce.out" }}, {t});
      IN("#{k}c{i + 1}", {{ scale: 2.4 }}, {{ scale: 1, duration: 0.3, ease: "back.out(2)" }}, {t + 0.25});'''
        if i == 0:
            js += f'\n      IN("#{k}c", {{ scale: 0 }}, {{ scale: 1, duration: 0.3, ease: "back.out(2)" }}, {t + 0.2});'
        else:
            js += f'\n      FT("#{k}c{i}", {{ autoAlpha: 1 }}, {{ autoAlpha: 0, duration: 0.05 }}, {t + 0.25});'
        SFX.extend([(t + 0.25, "pop", 0.2)])
    b = round(a + 0.45 + pots * 0.5 + 0.1, 2)
    js += f'''
      IN("#{k}b", {{ y: 900 }}, {{ y: 0, duration: 0.45, ease: "expo.out" }}, {b});
      [0, 1, 2, 3, 4].forEach(i => {{ IN("#{k}i" + i, {{ x: i % 2 ? 700 : -700 }}, {{ x: 0, duration: 0.4, ease: "expo.out" }}, {b + 0.45} + i * 0.85); FT("#{k}i" + i + " img", {{ scale: 0.2, rotation: -40 }}, {{ scale: 1, rotation: 0, duration: 0.45, ease: "back.out(2.5)" }}, {b + 0.55} + i * 0.85); }});
      float("#{k}j0", {a + 1.6}, 3.0, -14);'''
    SFX.append((b, "whoosh-short", 0.22))
    SFX.extend([(round(b + 0.45 + i * 0.85, 2), "whoosh-short", 0.18) for i in range(5)])
    SFX.extend([(round(b + 0.6 + i * 0.85, 2), "ping" if i == 2 else "click-soft", 0.2) for i in range(5)])
    return js
SC = [("#s1", "#k1", T["s1"], T["s2"]), ("#s2", "#k2", T["s2"], T["or"]), ("#s3", "#k3", T["or"], T["pl"]), ("#s4", "#k4", T["pl"], T["di"]), ("#s5", "#k5", T["di"], T["s6"]), ("#s6", "#k6", T["s6"], T["s7"]), ("#s7", "#k7", T["s7"], DUR)]
js = helpers + "      const SC = [" + ", ".join(f'["{s}", "{c}", {a}, {round(b - a, 2)}]' for s, c, a, b in SC) + '''];
      SC.forEach(([s, c, a, d], i) => {
        HIDE.push(s);
        tl.set(s, { autoAlpha: 1 }, a);
        if (i !== SC.length - 1) tl.set(s, { autoAlpha: 0 }, a + d);
        FT(c, { scale: 1.14 }, { scale: 1.0, duration: 0.45, ease: "expo.out" }, a);
        FT(c, { rotation: 0, x: 0 }, { rotation: i % 2 ? 0.8 : -0.8, x: i % 2 ? -20 : 20, duration: d, ease: "sine.inOut" }, a);
      });

      // 1. offre de vente, miel soignant, la cuillère de la Ruche
      IN("#band", { y: -80 }, { y: 0, duration: 0.3, ease: "power2.out" }, 0.05);
      ["#dr1", "#dr2", "#dr3", "#dr4"].forEach((d, i) => { HIDE.push(d); FT(d, { autoAlpha: 1, scaleY: 0 }, { scaleY: 1, duration: 1.6, ease: "power1.in" }, 0.2 + i * 0.15); });
      words(["#a1", "#a2", "#a3"], 0.3, 0.14);
      IN("#a4", { y: -300, scale: 1.4 }, { y: 0, scale: 1, duration: 0.5, ease: "bounce.out" }, 0.8);
      IN("#spoon", { y: 1200, rotation: 40 }, { y: 0, rotation: -8, duration: 0.6, ease: "back.out(1.4)" }, 1.3);
      FT("#spoon", { rotation: -8 }, { rotation: 6, duration: 1.2, yoyo: true, repeat: 1, ease: "sine.inOut" }, 1.9);
      pop("#sp1", 1.8); pop("#sp2", 2.0);

      // 2. les paniers
      IN("#photo", { y: 500, rotation: 10, scale: 0.8 }, { y: 0, rotation: -3, scale: 1, duration: 0.55, ease: "back.out(1.4)" }, 4.05);
      FT("#phi", { scale: 1 }, { scale: 1.12, duration: 3.9, ease: "none" }, 4.05);
      IN("#b1", { scale: 2.2, filter: "blur(16px)" }, { scale: 1, filter: "blur(0px)", duration: 0.35, ease: "power4.out" }, 4.7);
      ["#t1", "#t2", "#t3"].forEach((t, i) => IN(t, { scale: 0.3, y: 120 }, { scale: 1, y: 0, duration: 0.4, ease: "back.out(2.2)" }, 5.3 + i * 0.35));
      pop("#gift", 6.6); float("#gift", 6.9, 1.0, -18);
''' + cardjs("or", T["or"], 2) + cardjs("pl", T["pl"], 3) + cardjs("di", T["di"], 4)
o = T["s6"] - 18.4  # décalage par rapport au modèle du jour 1
js += f'''

      // 6. gustatif et soignant
      IN("#logo2", {{ scale: 0.3, rotation: -30 }}, {{ scale: 1, rotation: 0, duration: 0.55, ease: "back.out(1.8)" }}, {T["s6"] + 0.05});
      words(["#d1", "#d2", "#d3", "#d4"], {T["s6"] + 0.45}, 0.12); word("#d6", {T["s6"] + 1.05}, 0.35);
      IN("#d7", {{ scale: 0.4 }}, {{ scale: 1, duration: 0.4, ease: "back.out(2.2)" }}, {T["s6"] + 1.55});
      pop("#hp", {T["s6"] + 1.9}); float("#hp", {T["s6"] + 2.2}, 0.8, -16);
'''
# WhatsApp : on reprend le bloc du jour 1 en décalant ses temps de 21,4 vers T["s7"]
import re
wjs = src[src.index('      // 7. WhatsApp'):]
shift = T["s7"] - 21.4
wjs = re.sub(r'((?:\}|"|\]), )(2[1-4]\.\d+)(\)|, )', lambda m: f'{m.group(1)}{round(float(m.group(2)) + shift, 2)}{m.group(3)}', wjs)
js += wjs
open(os.path.join(HERE, "index.html"), "w").write(css + '    </style>\n  </head>' + body + js)
SFX += [(0.05, "whoosh-short", 0.22), (0.3, "whoosh-short", 0.18), (0.8, "impact-bass-2", 0.28), (1.3, "whoosh", 0.25), (1.8, "sparkle", 0.25),
        (4.0, "whoosh-cinematic", 0.3), (4.05, "whoosh-short", 0.22), (4.7, "impact-bass-1", 0.28), (5.3, "pop", 0.2), (5.65, "pop", 0.2), (6.0, "pop", 0.2), (6.6, "pop", 0.22),
        (T["s6"], "whoosh", 0.3), (T["s6"] + 0.05, "pop", 0.22), (T["s6"] + 1.05, "whoosh-short", 0.22), (T["s6"] + 1.55, "pop", 0.22), (T["s6"] + 1.9, "sparkle", 0.2)]
SFX += [(round(t + shift, 2), n, v) for t, n, v in [(21.4, "whoosh-cinematic", 0.3), (21.9, "typing", 0.3), (22.9, "click", 0.25), (23.05, "notification", 0.3), (23.2, "impact-bass-1", 0.2), (23.8, "pop", 0.25), (24.3, "chime", 0.3)]]
m = open(os.path.join(HERE, "mix.py")).read()
m = re.sub(r'DUR = [\d.]+', f'DUR = {DUR}', m)
m = re.sub(r'SFX = \[.*?\]\n\nos', 'SFX = ' + repr(sorted((round(t, 2), n, v) for t, n, v in SFX)) + '\n\nos', m, flags=re.S)
open(os.path.join(HERE, "mix.py"), "w").write(m)
print("ok")
