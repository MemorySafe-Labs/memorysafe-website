"""French (Québec) text for memorysafe.ca, added 16 Nov 2026.

A translation of the English pages, nothing more: no new claims, no new numbers.
Individual memories are "souvenirs", as in the cloud's own French pages; the store is "la mémoire".
French spacing (before : ; ? ! and inside « ») is applied at the bottom, so write plain spaces here.
"""
import re

CT = 'https://memory.memorysafe.ca'

COPY_FR = {
'lang':'fr-CA','code':'fr','prefix':'/fr/','skip':'Aller au contenu',
'nav':['Le problème','Fonctionnement','Tarifs','Recherche','Valeur','À propos'],
'cta':'Télécharger la bêta gratuite','cta_short':'Télécharger',
'value':{'eyebrow':'MEMORYSAFE LABS / SIMULATEUR DE PLANIFICATION','title':'Que pourrait changer MemorySafe pour vous ?',
'intro':'Deux petits modèles de planification : un pour les personnes qui utilisent des assistants, un pour les équipes qui entraînent des modèles. Vos chiffres, une arithmétique simple, aucune promesse.',
'film':'Simulateur d’avantages · vos hypothèses','tab1':'Assistants','tab2':'Équipes de modèles',
'p1_lead':'Combien de temps une équipe perd-elle à tout réexpliquer ? Le scénario médian suppose que la moitié peut être évitée.',
'p1_fields':[['people','Personnes qui utilisent des assistants IA','10','1'],['minutes','Minutes passées à réexpliquer, par personne / semaine','20','1'],['rate','Valeur d’une heure de travail ($ US)','50','1']],
'p1_outs':[['lost','Répétition / an'],['returned','Temps récupéré / an'],['value','Valeur indicative / an']],
'p1_formula':'personnes × minutes × 52 semaines → heures ; la moitié évitée dans le scénario médian.',
'p2_lead':'Que fait économiser en calcul un tampon de rejeu plus petit ? L’hypothèse : un tampon 30 % plus petit — 500 échantillons deviennent environ 350.',
'p2_fields':[['runs','Exécutions de rejeu ou de mise à jour / jour','200','1'],['mins','Minutes pour une exécution de rejeu','12','1'],['cost','Coût de calcul par heure ($ US)','2.50','0.1']],
'p2_outs':[['avoided','Temps d’exécution évité / an'],['gross','Valeur brute indicative / an']],
'p2_formula':'exécutions × minutes × 365 jours × 30 %, au tarif de votre calcul. Ce modèle porte seulement sur le temps d’exécution — jamais sur la qualité du modèle.',
'hours':'h',
'caption':'Un modèle de planification avec vos hypothèses. Les résultats réels dépendent du flux de travail, de la configuration et de la qualité des réponses.'},
'hero_eyebrow':'Une seule mémoire pour tous vos assistants IA',
'hero_title':'Arrêtez de tout réexpliquer à votre IA.',
'hero_intro':'MemorySafe est une mémoire que vos assistants IA partagent. Ils lisent et enregistrent les mêmes faits, alors vous n’expliquez jamais deux fois. Gratuit sur votre ordinateur pour Claude et Codex, dans un seul fichier qui n’en sort jamais. Ou dans le nuage, où Cursor et vos autres applications se joignent, sur tous vos appareils.',
'hero_primary':'Télécharger la bêta gratuite','hero_secondary':'Voir comment ça marche',
'hero_sub':'Aucun compte. Aucune inscription par courriel.','hero_code':'Code source ouvert sur GitHub','privacy_code':'Lire le code sur GitHub','source_code':'Code source sur GitHub','github_label':'MemorySafe sur GitHub','linkedin_label':'MemorySafe Labs sur LinkedIn',
'demo':{'without':'Lundi, sans MemorySafe','with':'Lundi, avec MemorySafe','chip':'3 souvenirs rappelés','you':'Vous','assistant':'Assistant',
'u1':'Petit rappel du contexte, puisque vous ne vous en souviendrez pas : je suis Carla, l’échéance est le 14 novembre, on déploie avec Docker et on utilise Vue — arrêtez de suggérer React, s’il vous plaît.',
'a1':'Merci pour le contexte ! Pouvez-vous aussi me rappeler sur quoi nous avons travaillé la dernière fois ?',
'u2':'Reprenons où nous en étions.',
'a2':'C’est parti — échéance du 14 novembre, interface en Vue, déploiement Docker. Nous nous sommes arrêtés au bogue de connexion vendredi.',
'step1':'Sans','step2':'Avec','pause':'Mettre l’exemple en pause','play':'Lire l’exemple',
'label':'Une mémoire, deux lundis','steps_label':'Explorer l’exemple',
'note':'Conversation illustrative · aucune donnée n’est enregistrée.'},
'compatible':'EXTENSION LOCALE GRATUITE POUR',
'ch_problem':'01 — LE PROBLÈME','problem_title':'L’IA a un problème de mémoire. Trois, en fait.',
'problems':[['refresh','Le jour de la marmotte','Chaque conversation repart de zéro. Vous retapez vos outils, vos règles, vos échéances — à chaque session, dans chaque application.'],['scatter','Une mémoire éparpillée','Claude en sait une partie, Codex une autre, Cursor rien. Votre contexte est fragmenté entre des fournisseurs qui ne se parlent pas.'],['lock','Une mémoire qui ne vous appartient pas','La mémoire des fournisseurs vit sur leurs serveurs, à leurs conditions. Vous ne pouvez ni l’ouvrir, ni la sauvegarder, ni l’emporter.']],
'ch_how':'02 — COMMENT ÇA MARCHE','how_title':'Un fichier. Trois verbes.',
'how_lead':'Une infrastructure volontairement simple : capter des faits, les garder dans un fichier qui vous appartient, les rappeler quand ils comptent.',
'verbs':[['capture','1 · Capter','Pendant que vous travaillez, MemorySafe enregistre des faits concis et durables — décisions, préférences, échéances. Automatiquement si vous l’activez, ou seulement quand vous dites « retiens ceci ».'],['store','2 · Conserver','Tout se retrouve dans un seul fichier de base de données sur votre ordinateur. Ouvrez-le, sauvegardez-le, passez-le en revue dans le tableau de bord local.'],['recall','3 · Rappeler','Votre assistant consulte la mémoire avant de répondre, et seuls les faits nécessaires entrent dans la conversation. Les souvenirs ne sont jamais supprimés parce qu’ils sont anciens.']],
'how_strip':'<strong>Les verbes restent les vôtres.</strong> Protégez ce qui ne doit pas changer. Retirez un souvenir du rappel. Examinez les conflits quand des faits se contredisent — rien n’est écrasé en silence.',
'ch_learn':'03 — ELLE CONTINUE DE VOUS APPRENDRE','learn_title':'Pas seulement mémorisé. Appris.',
'learn_lead':'Les modèles sont figés le jour de leur sortie. Votre mémoire est la partie qui continue d’apprendre — chaque décision et chaque préférence que vous confirmez s’additionne.',
'learn_steps':[['SEMAINE 1','Connaît l’essentiel.','Votre nom, vos outils, vos règles du jeu. Fini les présentations.'],['MOIS 2','Connaît vos décisions.','Ce que vous avez choisi, ce que vous avez écarté, et pourquoi — les questions réglées restent réglées.'],['MOIS 6','Connaît votre façon de travailler.','Vos exigences, vos cas particuliers. Les réponses partent de votre contexte, pas de zéro.']],
'learn_strip':'<strong>Et cet apprentissage est portable.</strong> Comme il vit dans un fichier qui vous appartient, il survit aux nouvelles versions de modèle, aux nouveaux outils, même à un changement d’assistant.',
'ch_editions':'03 — OÙ ELLE VIT','edition_title':'Votre mémoire. À votre façon.',
'edition_lead':'Commencez sur votre ordinateur aujourd’hui, ou laissez votre mémoire vous suivre : MemorySafe Cloud est offert dès maintenant, avec un forfait gratuit.',
'local_status':'BÊTA LOCALE GRATUITE · OFFERTE MAINTENANT','local_title':'Sur votre ordinateur. Entre vos mains.',
'local_body':'Un endroit commun où vos assistants de bureau compatibles enregistrent et rappellent le contexte utile.',
'local_points':['Claude Desktop, Claude Code et Codex','Passez les souvenirs en revue, protégez des faits, consultez l’historique','Votre base de souvenirs reste sur votre ordinateur'],
'local_cta':'Télécharger la bêta gratuite','local_fine':'Gratuit. Code source ouvert (Apache 2.0), pour toujours.<br>C’est une bêta parce que nous la testons encore.<br>Les fonctions avancées sont en construction dans MemorySafe Cloud.',
'hosted_status':'CLOUD BÊTA · OFFERT MAINTENANT · FORFAIT GRATUIT','hosted_title':'Votre mémoire vous suit.',
'hosted_body':'Une mémoire partagée entre les applications d’IA et les appareils compatibles — Claude, Codex, Cursor et d’autres — tenue à jour partout où vous travaillez.',
'hosted_points':['Une seule adresse à laquelle vos applications se connectent','Portable, téléphone, ordinateur de bureau','Hébergé au Canada'],'hosted_cta':'Créer votre compte gratuit',
'hosted_fine':'Gratuit jusqu’à 1 000 souvenirs. De la place pour 20 000 : 10 $ US par mois.<br>C’est une bêta parce que nous la testons encore.<br>Des questions ? <a href="mailto:contact@memorysafe.ca">Écrivez-nous</a>.',
'band_note':'L’extension locale garde votre mémoire sur un seul ordinateur. MemorySafe Cloud est l’endroit où tous vos assistants retrouvent une seule mémoire, sur tous vos appareils.',
'research_label':'UNE AUTRE ÉCHELLE.<br>LA MÊME QUESTION.',
'research_title':'Qu’est-ce qui mérite de rester ?',
'research_body':'La question derrière le produit, posée à l’échelle de l’entraînement : nous étudions comment les modèles d’IA choisissent les exemples d’entraînement passés à revoir quand le stockage est limité. Un axe de recherche distinct, la même question de fond.',
'research_cta':'Découvrir la recherche',
'ch_privacy':'04 — CONFIDENTIALITÉ','privacy_title':'Privée par son architecture, pas par une promesse.',
'privacy_lead':'Sur votre ordinateur, vous n’avez pas à faire confiance à une politique : vous pouvez regarder le chemin d’un fichier. Dans MemorySafe Cloud, vos souvenirs sont conservés au Canada, et vous pouvez les exporter ou les effacer.',
'tiles':[['shield','L’extension locale ne téléverse rien','Votre base de souvenirs reste sur votre ordinateur. Aucun compte, aucune synchronisation, aucun serveur MemorySafe derrière l’extension gratuite.'],['key','Vous tenez les clés','Protéger verrouille un souvenir contre toute modification. Oublier le retire du rappel. Le tableau de bord local montre ce qui est enregistré et ce qui a changé.'],['eyeoff','Aucune capture sensible','Secrets, identifiants, données de paiement, pièces d’identité, données de santé : jamais captés, dans aucun mode.'],['scale','Des limites dites franchement','Un service d’IA connecté traite quand même le contexte que vous choisissez de partager, et oublier retire un souvenir du rappel — pas de l’historique ni des sauvegardes. Nous disons les deux clairement.']],
'founder_eyebrow':'UNE QUESTION HUMAINE, D’ABORD','founder_heading':'Une meilleure mémoire.<br>Moins de recommencements.',
'founder_name':'Carla Centeno · Fondatrice et PDG',
'founder_description':'MemorySafe Labs part d’une question simple : qu’est-ce qui vaut la peine d’être retenu ? Nous en faisons des choses que nous pouvons construire et tester. Le contexte utile mérite une continuité. Et la personne derrière mérite d’en garder le contrôle.',
'contact':'Dites bonjour','team_heading':'Conseillers','supported_heading':'Avec le soutien de',
'faq_eyebrow':'AVANT DE DEMANDER','faq_heading':'Quelques points, mis au clair.',
'faqs':[
['La version gratuite fonctionne-t-elle sur tous mes appareils ?','L’extension gratuite garde sa base de données sur l’ordinateur où vous l’installez. Les assistants compatibles de cet ordinateur peuvent la partager. La mémoire sur plusieurs appareils, c’est ce que fait MemorySafe Cloud ; il est offert dès maintenant, avec un forfait gratuit.'],
['Que veut dire « local », au juste ?','La base de souvenirs reste sur votre ordinateur. Un service d’IA connecté peut quand même traiter le contexte que vous choisissez de partager, selon ses propres conditions. Un stockage local ne signifie pas que le service d’IA lui-même fonctionne localement.'],
['Puis-je changer d’avis au sujet d’un souvenir ?','Dans le tableau de bord local, vous pouvez passer en revue les souvenirs enregistrés, voir les changements, gérer la protection et retirer des souvenirs du rappel. Retirer un souvenir du rappel n’efface pas complètement l’historique ni les sauvegardes.'],
['Les fonctions avancées de mémoire sont-elles déjà offertes ?','Nous testons des outils pour prioriser les souvenirs automatiquement : quoi garder, quoi revoir, quoi mettre de côté. Ils sont en construction dans MemorySafe Cloud et ne font pas partie de l’extension locale gratuite.'],
],
'footer_eyebrow':'MOINS DE RECOMMENCEMENTS. PLUS D’AVANCEMENT.','footer_title':'Reprenez là où vous en étiez.',
'privacy':'Confidentialité','signin':'Connexion','cloud_terms':'Conditions du Cloud','github':'GitHub','copyright':'MemorySafe Labs Inc. · 2026',
'download_title':'Faites de la place à la mémoire.',
'download_intro':'Choisissez votre assistant. Installez la bêta locale gratuite. Aucune inscription, aucune mise en route compliquée.',
'download_eyebrow':'BÊTA LOCALE GRATUITE','desktop_download':'Télécharger pour Claude Desktop','desktop_steps':'Dans Claude Desktop : Settings → Extensions → Advanced settings → Install Extension… Sélectionnez le fichier téléchargé. Sous Windows, ne double-cliquez pas sur le fichier.',
'terminal_intro':'Une fois l’outil en ligne de commande de votre assistant installé, exécutez :','copy':'Copier les commandes',
'after_title':'Ensuite, reprenez le fil.','after_body':'Redémarrez votre assistant. La première configuration peut prendre quelques minutes. Ouvrez le tableau de bord local pour vérifier votre configuration et connecter les assistants compatibles de cet ordinateur.',
'dashboard':'Ouvrir le tableau de bord local','test_body':'Demandez à votre assistant de retenir une préférence sans importance. Ouvrez une nouvelle conversation et demandez-lui de la rappeler.',
'guide':'Vous préférez les images ? Voir le guide visuel (en anglais)',
'download_legal':'Gratuit, à code source ouvert sous la licence Apache 2.0. Les fonctions avancées de mémoire en construction pour MemorySafe Cloud ne sont pas incluses. Votre base de données reste sur cet ordinateur ; les services d’IA connectés peuvent traiter le contexte sélectionné. Oublier retire un souvenir du rappel, mais pas complètement de l’historique ni des sauvegardes.',
'notes':'Notes de version (en anglais)','product_privacy':'Confidentialité du produit (en anglais)','terms':'Conditions de la bêta (en anglais)',
'upd_label':'Facultatif','upd_title':'Envie de suivre les nouvelles versions ?','upd_body':'Laissez un courriel et nous vous écrirons seulement à la sortie d’une nouvelle version — rien d’autre. Le téléchargement ne l’exige jamais.','upd_cta':'M’aviser','upd_short':'Un courriel par version. Rien d’autre.',
'thanks_title':'Vous êtes sur la liste.','thanks_body':'Nous vous écrirons à la sortie d’une nouvelle version — et c’est tout. La bêta elle-même reste sans inscription.','thanks_back':'Retour au téléchargement',
'research_eyebrow':'MEMORYSAFE LABS / RECHERCHE EN APPRENTISSAGE CONTINU',
'research_page_title':'L’apprentissage continue. Qu’est-ce qui reste ?',
'research_page_intro':'Un modèle ne peut pas revoir tout ce qu’il a déjà vu. Nous étudions comment choisir ce qu’il revoit.',
'research_note':'Il s’agit de recherche sur l’entraînement de modèles. Elle est distincte de l’extension locale gratuite pour assistants et de MemorySafe Cloud. Aucun résultat de performance n’est présenté sur cette page.',
'research_contact':'Parlons de votre question de recherche',
'cases_label':'CADRE DE RECHERCHE · APPLICATIONS POSSIBLES','cases_title':'Là où l’oubli a des conséquences.',
'cases_lead':'Notre évaluation en apprentissage continu utilise des images médicales. Les modèles financiers, les appareils en périphérie et la robotique sont des applications possibles à explorer avec des partenaires.',
'cases':[['use-medical-ai','IA médicale','Les cas cliniques rares peuvent être écrasés à mesure que les modèles absorbent de nouvelles données.','Prioriser les échantillons vulnérables et cliniquement importants.'],['use-fraud-detection','Risque de modèle et réentraînement','L’évolution des données peut faire dériver des modèles financiers jusque-là fiables.','Préserver les éléments importants d’un cycle de réentraînement à l’autre.'],['use-edge-ai','IA en périphérie','Des limites strictes de stockage et de calcul rendent chaque échantillon conservé important.','Allouer une mémoire limitée de façon délibérée.'],['use-robotics','Robotique','De nouveaux environnements peuvent nuire à des habiletés déjà apprises.','Protéger les capacités fragiles pendant l’adaptation.']],
}

DEMO_FR = {'title':'Dites-le à un assistant. Continuez avec un autre.','save':'Dire','store':'Garder','recall':'Rappeler','pause':'Pause','play':'Lire','you':'Vous','first':'UNE CONVERSATION DANS CLAUDE DESKTOP','second':'UNE NOUVELLE CONVERSATION DANS CODEX','u1':'Retiens ceci : notre lancement est reporté à vendredi.','a1':'Enregistré dans MemorySafe.','fact':'Lancement → reporté à vendredi','shared':'Une mémoire partagée','source':'Disponible pour vos assistants connectés','u2':'Qu’est-ce que je devrais terminer en premier ?','a2':'Le lancement est vendredi, alors commencez par la page d’inscription.','chip':'Récupéré de MemorySafe','end':'Un autre assistant. Le même contexte.','note':'Exemple illustratif · Claude Desktop et Codex connectés au même MemorySafe local. Aucune donnée n’est enregistrée.'}

PRICING_FR = {'eyebrow':'TARIFS','title':'Un seul MemorySafe. Vos souvenirs sur votre ordinateur, ou dans votre compte.',
'intro':'Le même produit dans les deux cas. Choisissez où vivent vos souvenirs, et changez d’avis quand vous voulez.',
'for_you':'Pour vous','for_companies':'Pour les entreprises','pending':'Lien de paiement à venir','beta_note':'MemorySafe est en bêta : nous le testons encore.',
'cards':[
 {'status':'GRATUIT · DISPONIBLE','name':'Gratuit','price':'0 $ US','per':'','includes':'Ce qui est inclus','body':'Illimité sur cet ordinateur, pour toujours. 1 000 souvenirs gratuits dans le nuage.',
  'points':['Claude et Codex sur votre ordinateur','Cursor et d’autres applications dans le nuage','Compte dans le nuage hébergé au Canada','Passez en revue, protégez, exportez et effacez','Code source ouvert'],
  'buttons':[('Télécharger','download',''),('Créer votre compte gratuit','hosted','ghost')],'fine':''},
 {'status':'FORFAIT PAYANT','name':'Personnel','price':'10 $ US','per':'/ mois','includes':'Tout le forfait Gratuit, plus','body':'Plus de place dans le nuage, sur tous vos appareils.',
  'points':['Jusqu’à 20 000 souvenirs','Paiement mensuel, annulez quand vous voulez'],
  'buttons':[('Obtenir Personnel','paid','')],'fine':'Taxes en sus, ajoutées au paiement. Passez au forfait payant dans les Paramètres de votre compte.'},
 {'status':'ACCÈS ANTICIPÉ','name':'Team','price':'29 $ US','per':'/ personne / mois','includes':'Tout le forfait Personnel, plus','body':'Une seule mémoire pour toute votre équipe.',
  'points':['Les membres se joignent sur invitation','Mise en route avec nos fondateurs','Plus grande entreprise ? Prix fixe sur demande'],
  'buttons':[('Obtenir Team','team','')],'fine':'Créez un compte gratuit, puis payez à partir de la page de votre organisation.'},
 {'status':'GRATUIT AU DÉPART','name':'Audits et pilotes','price':'Gratuit','per':'au départ','includes':'Ce qui est inclus','body':'Nous testons gratuitement votre agent ou votre modèle et montrons où il oublie. Ensuite, nous proposons la prochaine étape.',
  'points':['Test de fragilité gratuit : un agent ou un modèle','Audit de mémoire : rapport indépendant, à partir de 5 500 $ US','Projet pilote d’apprentissage continu : 3 mois, 7 500 $ US'],
  'buttons':[('Réserver un test gratuit','test','')],'fine':'Les travaux médicaux et réglementés font l’objet d’un devis distinct.'}],
'note':'Prix en dollars américains, avant taxes. Stripe traite les paiements ; nous ne voyons jamais votre numéro de carte. <a href="'+CT+'/terms?lang=fr">Conditions</a> et <a href="'+CT+'/privacy?lang=fr">politique de confidentialité</a> de MemorySafe Cloud. Des questions : <a href="mailto:contact@memorysafe.ca">contact@memorysafe.ca</a>'}

STORY_FR = {
 'eyebrow':'MVI · PROTECTSCORE · REPLAY',
 'title':'Qu’est-ce qui mérite une autre chance ?',
 'film':'À l’intérieur d’une mémoire qui apprend',
 'play':'Lire l’animation','pause':'Mettre l’animation en pause','replay':'Rejouer l’animation',
 'steps_label':'Explorer le mécanisme de recherche',
 'steps':[
  ('La limite','LA CONTRAINTE','De nouvelles données. Le même budget de mémoire.',
   'À mesure qu’un modèle continue d’apprendre, de nouveaux exemples arrivent. Seule une sélection limitée d’exemples antérieurs peut rester dans son tampon de rejeu.'),
  ('MVI','INDICE DE VULNÉRABILITÉ DE LA MÉMOIRE','Remarquer ce qui peut être fragile.',
   'Le MVI suit un signal lissé tiré de la perte d’entraînement de chaque exemple. C’est un signal de vulnérabilité qui aide à repérer les exemples à revoir.'),
  ('ProtectScore','RÉTENTION + PRIORITÉ DE REJEU','Donner une raison à la sélection.',
   'ProtectScore combine le MVI avec des signaux configurés de valeur, de rareté, de criticité et d’ancienneté de la tâche. Il guide la rétention et le rejeu ; des quotas distincts fixent une rétention minimale pour des groupes choisis.'),
  ('L’effet','L’EFFET VISÉ','Changer ce qui est pratiqué.',
   'Dans la même limite de mémoire, des exemples antérieurs choisis reviennent à l’entraînement avec les nouvelles données. Leurs pertes au rejeu rafraîchissent le MVI, ce qui alimente la décision suivante.'),
 ],
 'incoming':'Nouveaux exemples','budget':'Budget de mémoire fixe','model':'Modèle en apprentissage',
 'earlier':'Antérieur','rare':'Rare','recent':'Récent','new':'Nouveau',
 'floor':'Plancher de rétention distinct','mvi_flag':'MVI',
 'buffer_notes':['Connaissances antérieures, espace limité','La vulnérabilité devient visible','Priorité + contraintes de rétention','Les exemples choisis sont revus'],
 'model_notes':['L’apprentissage continue','L’apprentissage continue','L’apprentissage continue','Nouvelles données + rejeu'],
 'feedback':'La perte au rejeu rafraîchit le MVI',
 'audit_title':'La piste d’audit',
 'audit_label':'EXEMPLES D’ENTRÉES',
 'audit_rows':[
  ('0','ADMIT','A reste','Une place libre était disponible.','free_capacity'),
  ('2','REJECT','H reste dehors','Son ProtectScore est inférieur à celui du résident admissible.','protect_below_victim'),
  ('2','EVICT','F → G','G surclasse F dans leur groupe. Le groupe de B conserve son plancher.','lowest_protect_in_group'),
 ],
 'audit_note':'Les registres d’exécution peuvent inclure la règle, les scores, l’étape d’entraînement et l’état du tampon, pour que la sélection puisse être examinée.',
 'caption':'Exemples d’entraînement illustratifs. Une explication visuelle de la méthode de recherche.',
 'diagram_label':'De nouveaux exemples entrent dans un tampon de rejeu limité. Le MVI alimente ProtectScore. Les contraintes de rétention et les scores déterminent quels exemples reviennent à l’entraînement du modèle.',
}

META_FR = {'':'Une mémoire que vos assistants IA partagent. Gratuit et à code source ouvert sur votre ordinateur ; MemorySafe Cloud vous suit sur tous vos appareils, avec un forfait gratuit.',
 'pricing/':'Tarifs de MemorySafe : gratuit et illimité sur votre ordinateur, 1 000 souvenirs gratuits dans le nuage, 10 $ US par mois pour 20 000. Forfaits Team et audits pour les entreprises.',
 'download/':'Téléchargez l’extension gratuite MemorySafe pour Claude Desktop, Claude Code et Codex. Code source ouvert, aucun compte, vos souvenirs restent sur votre ordinateur.',
 'research/':'La recherche de MemorySafe Labs en apprentissage continu : comment un modèle choisit les exemples passés à revoir quand la mémoire est limitée.',
 'value/':'Un petit simulateur de planification : combien de temps coûte le fait de tout réexpliquer, et ce qu’un tampon de rejeu plus petit fait économiser en calcul.',
 'privacy/':'Avis de confidentialité du site memorysafe.ca.'}

NB = ' '
def _fr(s):
    """French spacing: no line break before : ; ? ! or inside « », in amounts and thousands."""
    s = re.sub(r' ([:;?!»])', NB + r'\1', s)
    s = s.replace('« ', '«' + NB)
    s = re.sub(r'(\d) (\d{3})\b', r'\1' + NB + r'\2', s)
    s = s.replace(' $ US', NB + '$' + NB + 'US').replace('($ US)', '($' + NB + 'US)').replace(' %', NB + '%')
    return s
def _walk(x):
    if isinstance(x, str): return _fr(x)
    if isinstance(x, list): return [_walk(i) for i in x]
    if isinstance(x, tuple): return tuple(_walk(i) for i in x)
    if isinstance(x, dict): return {k: _walk(v) for k, v in x.items()}
    return x

COPY_FR, DEMO_FR, PRICING_FR, STORY_FR, META_FR = (_walk(d) for d in (COPY_FR, DEMO_FR, PRICING_FR, STORY_FR, META_FR))
# Things the spacing rule must not touch: codes, addresses and field defaults.
COPY_FR.update(lang='fr-CA', code='fr', prefix='/fr/')
