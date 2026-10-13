import sys
sys.path.insert(0, '/tmp/claude-0/-home-user-Mike1272-Bus/7c68b9b5-f98d-5769-9dfc-b4f40cf3c57b/scratchpad')
from prospects_data import *
from collections import Counter
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.fonts import addMapping
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, KeepTogether, Image, PageBreak
from reportlab.lib.styles import ParagraphStyle

F = '/home/user/Mike1272-Bus/produits/templates-entreprises/video-automatisation/assets/'
pdfmetrics.registerFont(TTFont('Bri', F + 'fonts/bricolage-800.ttf'))
pdfmetrics.registerFont(TTFont('WS', F + 'fonts/worksans-400.ttf'))
pdfmetrics.registerFont(TTFont('WSB', F + 'fonts/worksans-700.ttf'))
addMapping('WS', 0, 0, 'WS'); addMapping('WS', 1, 0, 'WSB')
NAVY = colors.HexColor('#0b1033'); BLUE = colors.HexColor('#2342ff'); GREY = colors.HexColor('#4a5275'); LIGHT = colors.HexColor('#f3f5fc')
H1 = ParagraphStyle('h1', fontName='Bri', fontSize=23, leading=27, textColor=NAVY, spaceAfter=4)
SUB = ParagraphStyle('sub', fontName='WS', fontSize=11, leading=15, textColor=GREY, spaceAfter=6)
H2 = ParagraphStyle('h2', fontName='Bri', fontSize=15, leading=19, textColor=NAVY, spaceBefore=12, spaceAfter=6, keepWithNext=1)
H3 = ParagraphStyle('h3', fontName='Bri', fontSize=12, leading=15, textColor=NAVY, spaceBefore=4, spaceAfter=3, keepWithNext=1)
B = ParagraphStyle('b', fontName='WS', fontSize=10, leading=14, textColor=NAVY, spaceAfter=2)
SM = ParagraphStyle('sm', fontName='WS', fontSize=8.5, leading=11, textColor=NAVY)
MSG = ParagraphStyle('msg', fontName='WS', fontSize=9.5, leading=13.5, textColor=NAVY, backColor=colors.HexColor('#e7f6ec'),
                     borderPadding=(6, 8, 6, 8), spaceBefore=4, spaceAfter=8)
def bl(items): return [Paragraph('•&nbsp;&nbsp;' + x, B) for x in items]
def table(data, widths, head=True, st=B):
    t = Table([[Paragraph(str(c), st) for c in r] for r in data], colWidths=widths, repeatRows=1 if head else 0)
    s = [('LINEBELOW', (0,0), (-1,-1), 0.5, colors.HexColor('#dde3f5')), ('VALIGN', (0,0), (-1,-1), 'TOP'),
         ('TOPPADDING', (0,0), (-1,-1), 4), ('BOTTOMPADDING', (0,0), (-1,-1), 4)]
    if head: s.append(('BACKGROUND', (0,0), (-1,0), LIGHT))
    t.setStyle(TableStyle(s)); return t
def msg(t): return Paragraph(''.join(ch for ch in t if ord(ch) < 0x2600).replace(' \n', '\n').replace('\n', '<br/>'), MSG)
def footer(c, d):
    c.saveState(); c.setFont('WS', 8); c.setFillColor(GREY)
    c.drawString(18*mm, 10*mm, 'Allegra Digital Ground · Plan de prospection, système de gestion de stock'); c.drawRightString(192*mm, 10*mm, str(d.page)); c.restoreState()

R_ALL = load(); V = Counter(vague(r) for r in R_ALL); R = _load_orig()
doc = SimpleDocTemplate(sys.argv[1], pagesize=A4, leftMargin=18*mm, rightMargin=18*mm, topMargin=16*mm, bottomMargin=18*mm,
                        title='Plan de prospection : système de gestion de stock', author='Allegra Digital Ground')
s = [Image(F + 'img/logo_adg.png', width=24*mm, height=19*mm, hAlign='LEFT'), Spacer(1, 3),
     Paragraph('Plan de prospection et d\'approche', H1),
     Paragraph('Les entreprises du fichier PROSPECTION.xlsx, pour le template « Gestion de stock » et le système automatisé. À utiliser avec le fichier de suivi <font name="WSB">prospection_50_entreprises.xlsx</font>.', SUB)]

s.append(Paragraph('1. Ce que contient le fichier', H2))
s += bl([f'<font name="WSB">{len(R)} entreprises, pas 50</font> : les numéros 4, 18 et 28 sont absents de la liste.',
         f'<font name="WSB">Villes</font> : {Counter(r["ville"] for r in R)["Lubumbashi"]} à Lubumbashi, {Counter(r["ville"] for r in R)["Kinshasa"]} à Kinshasa, 1 sans ville.',
         'Tout se fera <font name="WSB">à distance</font> : message, vidéos, démonstration en appel vidéo WhatsApp et installation en ligne. Lubumbashi n\'est donc pas un frein.'])
seg = Counter(r['seg'] for r in R)
pr = {sg: Counter(r['prio'] for r in R if r['seg'] == sg).most_common(1)[0][0] for sg in seg}
why = {'Téléphones, électronique, informatique': 'Beaucoup de modèles et d\'accessoires, des patrons à l\'aise avec la technologie.',
       'Cosmétique et parfumerie': 'Beaucoup de références, ventes en ligne, joignables sur WhatsApp.',
       'Quincaillerie et peinture': 'Stock qui coûte cher, unités variées (sac, barre, pot).',
       'Habillement': 'Modèles, tailles et couleurs à suivre.',
       'Entrepôt et distribution': 'Beaucoup d\'entrées et de sorties. Entreprises plus grandes, peut-être déjà équipées.',
       'Pharmacie': 'Il manque la date de péremption dans le template : à ajouter avant de les contacter.',
       'À vérifier': 'Traitement d\'eau et construction : pas de boutique, besoin de stock à confirmer.'}
s.append(table([['Segment', 'Nombre', 'Priorité', 'Pourquoi']] + [[sg, seg[sg], pr[sg], why[sg]] for sg in SEG_ORDER], [50*mm, 18*mm, 19*mm, 87*mm]))
s.append(Paragraph('À vérifier avant d\'écrire', H3))
s += bl(['<font name="WSB">PREDI B</font> : pas de ville et un numéro turc (+90). Peut-être un fournisseur, pas une boutique.',
         '<font name="WSB">BRICOKIN</font> : classé « cosmétique » mais le nom évoque le bricolage.',
         '<font name="WSB">BETA CONSTRUCTION</font> et <font name="WSB">EAUCIEL</font> : pas de boutique, le besoin de stock n\'est pas sûr.',
         '<font name="WSB">KEMBEZI PHARMA CARE</font> et <font name="WSB">ZOTTOSPHARMA</font> : attendre la version avec date de péremption.',
         'Deux noms corrigés : ELETRONIC STORE devient ELECTRONIC STORE, XIAIMI devient XIAOMI.'])

s.append(Paragraph('2. Ce qu\'on leur propose', H2))
s += bl(['<font name="WSB">Le template « Gestion de stock »</font> : prêt et testé. On peut le vendre dès maintenant.',
         '<font name="WSB">Le système automatisé</font> : le template + les 4 automatisations (vente, arrivage, point du matin, bilan du soir) sur WhatsApp.',
         '<font name="WSB">L\'installation à distance</font> avec leurs produits, pour ceux qui ne veulent pas le faire eux-mêmes.'])

s.append(Paragraph('3. Avant d\'envoyer le premier message', H2))
s.append(Paragraph('Le message 1 promet des alertes WhatsApp et un bilan du soir. Il faut donc que ça marche avant de l\'envoyer :', B))
for i, x in enumerate(['<font name="WSB">Tester le système sur ton n8n</font> : une vente et un arrivage de test, avec les messages WhatsApp reçus. C\'est la condition pour démarrer.',
                       '<font name="WSB">Compléter ton WhatsApp Business</font> : logo Allegra, description, horaires, et la vidéo en statut le jour de l\'envoi.',
                       '<font name="WSB">Fixer les prix</font> du template, du système et de l\'installation (ils sont encore à [PRIX]).',
                       '<font name="WSB">Décider de l\'offre de lancement</font> (à toi de choisir) : par exemple, une semaine d\'essai gratuite pour les 3 premières entreprises, en échange d\'un avis. Ça donne une raison de dire oui tout de suite et ça nous apporte des preuves.',
                       'Si possible, <font name="WSB">ajouter ta voix</font> sur la vidéo de présentation (le script est prêt). Sans voix, elle reste lisible, puisque tout est écrit à l\'écran.'], 1):
    s.append(Paragraph(f'{i}.&nbsp;&nbsp;{x}', B))

s.append(Paragraph('4. Le parcours, de l\'inconnu au client', H2))
steps = [['Étape', 'Ce que tu fais', 'Ce que tu envoies'],
         ['Jour 0', 'Premier contact, personnalisé avec le nom et le segment.', 'Message 1 + vidéo de présentation (37 s)'],
         ['S\'il répond', 'Tu remercies, tu montres l\'intérieur et tu proposes une démo.', 'Message 2 + vidéo du workflow (35 s)'],
         ['Démo (15 min)', 'Appel vidéo WhatsApp. Prépare avant le tableau avec 3 à 5 de SES produits (trouvés sur sa page) : il se voit déjà dedans.', 'Le tableau rempli, une vente test en direct'],
         ['Offre', 'Tu proposes template seul, système complet ou installation, avec le prix.', 'Fiche de l\'offre + PDF « comment ça marche »'],
         ['Client', 'Installation à distance, puis tu demandes un avis après une semaine.', 'Guide + rappel J+3'],
         ['Pas de réponse', 'Relance 1 au jour 3, relance 2 au jour 7, puis on arrête.', 'Messages courts, sans pression']]
s.append(table(steps, [26*mm, 84*mm, 64*mm]))

s.append(Paragraph('5. Le calendrier', H2))
cal = [['Quand', 'Qui', 'Combien'],
       ['Jours 1 et 2', 'Vague 1 : téléphones, électronique, informatique (priorité A)', f'{V[1]} messages, 10 par jour'],
       ['Jours 3 et 4', 'Vague 2 : cosmétique, parfumerie, quincaillerie (priorité A)', f'{V[2]} messages, 8 par jour'],
       ['Jour 4', 'Relances 1 de la vague 1', 'selon les réponses'],
       ['Jour 5', 'Vague 3 : habillement, entrepôts, puis les « à vérifier » une fois vérifiés', f'{V[3]} messages au plus'],
       ['Jours 6 et 7', 'Relances 1 de la vague 2, démos avec ceux qui ont répondu', '-'],
       ['Jours 8 à 12', 'Relances 2, démos, offres, premières installations', '-'],
       ['Jour 6', 'Vague 4 : 5 entreprises alimentaires de la liste Vibe (voir l\'annexe)', f'{V[4]} messages']]
s.append(table(cal, [30*mm, 100*mm, 44*mm]))
s.append(Paragraph('Pourquoi commencer par les téléphones : on teste le message sur un seul segment. Si les réponses sont faibles, on ajuste la phrase d\'accroche avant la vague 2.', B))

s.append(Paragraph('6. Les messages', H2))
s.append(Paragraph('Dans le fichier de suivi, le bouton « Ouvrir WhatsApp » ouvre la conversation avec le message 1 déjà écrit et personnalisé. Tu ajoutes la vidéo, tu relis, tu envoies.', B))
s.append(Paragraph('Message 1 (jour 0), avec la vidéo de présentation', H3))
s.append(msg(message1('[Nom de l\'entreprise]', 'Téléphones, électronique, informatique')))
s.append(Paragraph('La 3e phrase change selon le segment :', B))
s += [Paragraph(f'•&nbsp;&nbsp;<font name="WSB">{k}</font> : {v}', SM) for k, v in HOOK.items() if k != 'À vérifier']
s.append(Paragraph('Message 2 (s\'il répond), avec la vidéo du workflow', H3)); s.append(msg(MESSAGE2))
s.append(Paragraph('Relance 1 (jour 3)', H3)); s.append(msg(RELANCE1.replace('{nom}', '[Nom]')))
s.append(Paragraph('Relance 2 (jour 7, la dernière)', H3)); s.append(msg(RELANCE2.replace('{nom}', '[Nom]')))

s.append(Paragraph('7. Les réponses aux questions qu\'ils vont poser', H2))
obj = [['Ils disent', 'Tu réponds'],
       ['« C\'est combien ? »', 'Le prix fixé. Si possible, propose d\'abord la démo : « Je vous le montre en 15 minutes avec vos produits, et vous jugez. »'],
       ['« J\'ai déjà un cahier / Excel »', '« Justement, on part de ce que vous avez. La différence : le stock se calcule tout seul et WhatsApp vous prévient. »'],
       ['« Je n\'ai pas le temps »', '« Noter une vente prend environ 20 secondes sur le téléphone. Le reste se fait tout seul. »'],
       ['« On est à Lubumbashi »', '« Tout se fait à distance : la démo en appel vidéo et l\'installation en ligne. »'],
       ['« Ça marche sans internet ? »', '« Il faut internet pour envoyer les formulaires et recevoir les messages, comme pour WhatsApp. »'],
       ['« Envoyez-moi plus d\'infos »', 'Envoie le PDF « comment ça marche » et propose une date de démo.']]
s.append(table(obj, [52*mm, 122*mm]))

s.append(Paragraph('8. Les règles pour ne pas être bloqué par WhatsApp', H2))
s += bl(['Pas plus de 10 à 15 premiers messages par jour, envoyés un par un, espacés de quelques minutes.',
         'Toujours avec le nom de l\'entreprise : jamais exactement le même texte collé à tout le monde.',
         'Un « non » ou « stop » : on remercie et on n\'écrit plus.',
         'Répondre vite quand quelqu\'un répond, c\'est là que la vente se joue.',
         'Pas de message de diffusion (liste) à des gens qui n\'ont pas ton numéro.'])

s.append(Paragraph('9. Le suivi, chaque soir (5 minutes)', H2))
s += bl(['Dans le fichier, mets la <font name="WSB">date du 1er message</font> et le <font name="WSB">statut</font> de chaque entreprise.',
         'La colonne <font name="WSB">Prochaine action</font> te dit quoi faire (relance 1, relance 2, message 2…). En rouge : à faire aujourd\'hui.',
         'L\'onglet <font name="WSB">Suivi</font> compte tout : contactés, réponses, taux de réponse, démos, clients.',
         'On fait le point ensemble après la vague 1 pour ajuster les messages.'])

s.append(PageBreak())
s.append(Paragraph('Annexe : les entreprises par vague', H2))
for v, titre in [(1, 'Vague 1'), (2, 'Vague 2'), (3, 'Vague 3'), (4, 'Vague 4 : liste Vibe (alimentaire)')]:
    s.append(Paragraph(titre, H3))
    rows = sorted([r for r in R_ALL if vague(r) == v], key=lambda r: (SEG_ORDER.index(r['seg']), r['ville'], r['n']))
    s.append(table([['N°', 'Entreprise', 'Ville', 'Segment', 'Prio.']] + [[r['n'], r['nom'], r['ville'], r['seg'], r['prio']] for r in rows],
                   [10*mm, 62*mm, 24*mm, 66*mm, 12*mm], st=SM))
doc.build(s, onFirstPage=footer, onLaterPages=footer); print('ok')
