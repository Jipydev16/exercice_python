# Cahier d'exercices — Python et pensée algorithmique



## Exercice 01 — Un vrai ticket de caisse

**Situation :** une petite boutique vend un produit en plusieurs exemplaires. Le client peut bénéficier d'une remise et une TVA doit ensuite être ajoutée. Vous devez calculer le détail exact du ticket.

**Travail demandé :** écrivez `calculer_ticket(prix_unitaire, quantite, remise_pct, tva_pct=16)` qui retourne un dictionnaire comportant **exactement** `sous_total`, `remise`, `montant_ht`, `tva`, `total_ttc`. Calculez dans cet ordre : sous-total = prix × quantité ; remise = sous-total × taux de remise ; montant HT après remise ; TVA sur le montant remisé ; total TTC. Arrondissez chaque champ du résultat à 2 décimales.

**Exemple :** `calculer_ticket(2500, 3, 10)` → `{'sous_total': 7500.0, 'remise': 750.0, 'montant_ht': 6750.0, 'tva': 1080.0, 'total_ttc': 7830.0}`.

**Cas limites :** quantité entière ≥ 1, prix ≥ 0 et taux compris entre 0 et 100. Le programme doit signaler une valeur invalide par `ValueError`.

**À réfléchir :** pourquoi applique-t-on la TVA **après** la remise ? Quel problème pourrait créer un arrondi intermédiaire ?

**Défi supplémentaire :** faire afficher un ticket lisible sur plusieurs lignes, sans changer les calculs.

## Exercice 02 — Le moteur de tarification des livraisons

**Niveau :** 1/5 · **Notions :** comparaisons, `if`/`elif`/`else`, priorité des règles.

**Situation :** une plateforme de vente livre ses commandes selon un barème précis.

**Règles (dans cet ordre) :** si le panier vaut **au moins 100 000 CDF**, les frais sont nuls ; sinon, distance ≤ 5 km : **2 000 CDF** ; distance entre 5 et 20 km, 5 exclu et 20 inclus : **5 000 CDF** ; au-delà de 20 km : **9 000 CDF**. Un client **premium** paie seulement la moitié des frais non nuls.

**Travail demandé :** écrire `calculer_livraison(montant_panier, distance_km, premium=False)` → `{'frais': ..., 'total': ...}`. Refuser les montants et distances négatifs.

**Exemples :** `(50_000, 5, False)` → frais `2000` et total `52000` ; `(50_000, 21, True)` → frais `4500` et total `54500` ; `(100_000, 50, False)` → frais `0`.

**À réfléchir :** que se passe-t-il exactement à **5 km**, **20 km**, **100 000 CDF** ? Pourquoi tester d'abord la gratuité ?

**Défi supplémentaire :** créer un tableau de tests pour les 6 frontières : 0, 5, un peu plus de 5, 20, un peu plus de 20 km et 100 000 CDF.

## Exercice 03 — Un tableau de bord budgétaire, sans `sum()`

**Niveau :** 1/5 · **Notions :** boucles, accumulateurs, compteurs, invariant, listes vides.

**Situation :** vous devez étudier une liste de dépenses quotidiennes et déterminer si un budget fixé a été dépassé.

**Travail demandé :** coder `bilan_budget(depenses, budget)` renvoyant `nombre`, `total`, `moyenne`, `plus_grosse`, `reste`, `depasse`. Le résultat doit être calculé **avec une seule boucle `for`**, sans `sum()` ni `max()`. `depasse` vaut `True` uniquement lorsque `total > budget`. Retourner une moyenne de `0` si la liste est vide.

**Exemple :** `bilan_budget([1200, 1800, 900], 5000)` → total `3900`, moyenne `1300`, plus grosse `1800`, reste `1100`, dépassement `False`.

**Cas limites :** aucune dépense, budget nul, dépense exactement égale au budget, valeur négative à refuser.

**À réfléchir :** quelles valeurs doivent avoir les variables **avant** le premier passage dans la boucle ? Comment savez-vous que la boucle a bien compté tous les éléments ?

**Défi supplémentaire :** compter combien de dépenses dépassent la moyenne, sans recourir à `sum()`.

## Exercice 04 — Détecteur de nombres premiers

**Niveau :** 2/5 · **Notions :** modulo, boucles `while`, optimisation, réutilisation.

**Situation :** vous construisez un outil mathématique pour décider si un entier est premier et lister les nombres premiers jusqu'à une limite.

**Travail demandé :** implémenter `est_premier(n)` → booléen et `premiers_jusqua(limite)` → liste. Aucun nombre inférieur à 2 n'est premier. Pour déterminer si `n` possède un diviseur, **inutile de tester au-delà de la racine carrée** : utilisez `diviseur * diviseur <= n`.

**Exemples :** `est_premier(1)` → `False`, `est_premier(29)` → `True`, `est_premier(35)` → `False`, `premiers_jusqua(20)` → `[2, 3, 5, 7, 11, 13, 17, 19]`.

**À réfléchir :** pourquoi trouver **un seul diviseur** suffit-il ? Pourquoi `√n` est-elle une borne correcte ? Comparez le nombre de tentatives pour 10 007 avec et sans optimisation.

**Défi supplémentaire :** comparer cette solution avec le crible d'Ératosthène (sans modifier la solution de base).

## Exercice 05 — Le chiffrement de César

**Niveau :** 2/5 · **Notions :** parcours de chaîne, codes de caractères, modulo, fonctions inverses.

**Situation :** vous voulez coder un message en décalant chaque lettre de l'alphabet d'un certain nombre de positions.

**Travail demandé :** écrire `chiffrer_cesar(message, decalage)` et `dechiffrer_cesar(message, decalage)`. Déplacez les lettres **A-Z** et **a-z** en préservant majuscules/minuscules. Après Z, revenez à A. Les espaces, chiffres, signes et lettres accentuées restent inchangés. Un décalage négatif est permis. Utilisez `ord()`, `chr()` et `% 26`.

**Exemple :** `chiffrer_cesar('Bonjour, Python!', 3)` → `'Erqmrxu, Sbwkrq!'`; le déchiffrement redonne le message initial.

**À réfléchir :** pourquoi `decalage % 26` ne modifie-t-il pas le résultat ? À quoi sert l'opération modulo dans la rotation de l'alphabet ?

**Défi supplémentaire :** réaliser un test de propriété : `dechiffrer_cesar(chiffrer_cesar(texte, k), k) == texte` pour plusieurs valeurs de `k`.

**Attention :** ce chiffrement historique n'est pas adapté à la sécurité réelle.

## Exercice 06 — Le classement d'un tournoi, sans `sorted()`

**Niveau :** 2/5 · **Notions :** indexation, recherche du maximum, tri par sélection, stabilité.

**Situation :** les organisateurs d'un tournoi veulent classer les joueurs selon leur score, du plus grand au plus petit.

**Travail demandé :** implémenter `classer_scores(scores)` où `scores` est une liste de `(nom, points)`. **Interdiction d'utiliser `sort()`, `sorted()` ou `max()`**. Répétez : chercher le meilleur élément dans ceux qui restent, l'extraire, puis l'ajouter au classement. Si deux joueurs ont le même score, conserver leur **ordre initial**. La liste reçue ne doit pas être modifiée.

**Exemple :** `[('Ada',12), ('Lin',18), ('Max',12), ('Eva',20)]` → `[('Eva',20), ('Lin',18), ('Ada',12), ('Max',12)]`.

**Cas limites :** liste vide, égalités, score 0 ; signaler une entrée de format invalide.

**À réfléchir :** comment éviter de déplacer un joueur ex æquo devant l'autre ? Combien de comparaisons faut-il approximativement pour classer `n` joueurs ?

**Défi supplémentaire :** écrire ensuite un tri par insertion et comparer les performances.

## Exercice 07 — La recherche binaire de la première occurrence

**Niveau :** 3/5 · **Notions :** tableau trié, dichotomie, bornes, preuve de terminaison.

**Situation :** on recherche une valeur dans une très longue liste déjà triée **par ordre croissant**.

**Travail demandé :** écrire `recherche_premiere_occurrence(valeurs, cible)` qui renvoie **l'indice de la première occurrence** ou `-1`. Utiliser la recherche dichotomique (indices `gauche`, `droite`, `milieu`) et ne pas parcourir linéairement toute la liste. Quand la valeur est trouvée, continuez à rechercher à gauche.

**Exemples :** `([2,4,4,4,9,11],4)` → `1` ; `([2,4,9],7)` → `-1` ; `([],5)` → `-1`.

**À réfléchir :** que savez-vous de la moitié éliminée à chaque tour ? Pourquoi l'algorithme serait-il faux sur une liste non triée ? Comparez sa complexité `O(log n)` à `O(n)`.

**Défi supplémentaire :** trouver également la **dernière occurrence** et en déduire le nombre d'apparitions.

## Exercice 08 — Analyser les mots d'un texte

**Niveau :** 3/5 · **Notions :** normalisation, dictionnaires, comptages, égalités.

**Situation :** une application doit identifier les mots les plus fréquents dans une description, un commentaire ou un article.

**Travail demandé :** coder `compter_mots(texte)` renvoyant `{mot: nombre}` en ignorant la casse. Les mots sont des séquences de caractères pour lesquels `str.isalnum()` est vraie (les accents et chiffres sont acceptés) ; tout autre caractère est un séparateur. Coder également `mot_dominant(texte)` renvoyant `(mot, fréquence)` ou `None` si aucun mot n'existe. En cas d'égalité, choisir le mot **alphabétiquement premier**.

**Exemple :** `'Python, python ! L\'analyse des données avec Python.'` donne une fréquence de `3` pour `python` ; mot dominant `('python', 3)`.

**À réfléchir :** pourquoi un dictionnaire est-il plus adapté qu'une liste de compteurs ? Pourquoi normaliser le texte **avant** de compter ?

**Défi supplémentaire :** afficher les 5 mots les plus fréquents et expliquer votre règle de départage.

## Exercice 09 — Les mouvements de stock d'une boutique

**Niveau :** 3/5 · **Notions :** dictionnaires, listes de dictionnaires, état, validation, effet de bord.

**Situation :** un magasin reçoit des produits (`entree`) et en vend (`sortie`). On doit suivre les soldes sans autoriser un stock négatif.

**Travail demandé :** coder `appliquer_mouvements(stock_initial, mouvements)` : le premier argument est `{'Stylo': 10, 'Cahier': 4}`, le second une liste d'objets `{'produit': 'Stylo', 'type': 'sortie', 'quantite': 3}`. Les entrées peuvent créer de nouveaux produits ; les sorties ne peuvent pas dépasser le solde. Refusez une quantité non entière ou non positive, un type inconnu ou un nom vide. **Ne jamais modifier** `stock_initial` : en cas d'erreur à mi-parcours, il doit rester entièrement inchangé.

**Exemple :** après la sortie de 3 stylos puis l'entrée de 2 classeurs, résultat `{'Stylo': 7, 'Cahier': 4, 'Classeur': 2}`.

**À réfléchir :** pourquoi une copie est-elle nécessaire ? Quelle différence existe-t-il entre un algorithme qui modifie son argument et un algorithme qui renvoie un nouvel état ? Comment garantir un traitement « tout ou rien » ?

**Défi supplémentaire :** calculer un journal des soldes intermédiaires **sans** exposer un état partiellement validé.

## Exercice 10 — Le voisinage dans une grille 2D

**Niveau :** 4/5 · **Notions :** matrices, boucles imbriquées, coordonnées, vérification des bornes.

**Situation :** vous développez le moteur d'un jeu ou d'un automate cellulaire. Une cellule active vaut `1`, inactive vaut `0`. Chaque cellule peut avoir **huit voisines** (y compris diagonales).

**Travail demandé :** écrire `compter_voisins(grille)` retournant **une nouvelle matrice** avec, à chaque position, le nombre de voisines actives, **sans compter la cellule elle-même**. Un voisin hors grille ne doit pas être compté. Vérifiez que les lignes ont toutes la même taille et que les valeurs valent 0 ou 1.

**Exemple :** `[[1,0,0],[0,1,0],[0,0,1]]` → `[[1,2,1],[2,2,2],[1,2,1]]`.

**À réfléchir :** comment représenter les huit déplacements relatifs autour d'une case `(i, j)` ? Pourquoi `-1` comme indice pourrait-il produire un résultat trompeur en Python ? Quel est le coût si la grille comporte L lignes et C colonnes ?

**Défi supplémentaire :** programmer une génération du **Jeu de la vie de Conway** à partir du résultat.

## Exercice 11 — Un rapport de ventes avec `*args` et `**kwargs`

**Niveau :** 4/5 · **Notions :** conception modulaire, paramètres par défaut, `*args`, `**kwargs`.

**Situation :** vous devez produire des rapports pour une boutique, sans connaître à l'avance le nombre de lignes de vente ni le nombre d'informations contextuelles à conserver.

**Travail demandé :** écrire d'abord `montant_ligne(produit, quantite, prix_unitaire)` ; puis `analyser_ventes(*ventes, tva_pct=0.0, **contexte)`. Chaque vente est un dictionnaire avec `produit`, `quantite`, `prix_unitaire`. Le rapport contient `sous_total`, `tva`, `total_ttc`, `quantite_articles`, `par_produit` (CA par nom de produit), `contexte` (métadonnées libres : magasin, responsable…). Les montants sont arrondis à 2 décimales. Quantités entières strictement positives et prix non négatifs.

**Exemple :** deux stylos à 2500 et un cahier à 1000, TVA 16 %, donnent sous-total `6000`, TVA `960`, TTC `6960`, 3 articles ; `par_produit={'Stylo':5000.0,'Cahier':1000.0}`.

**À réfléchir :** dans quel cas préférer `*args` à une liste passée comme paramètre ? En quoi `**kwargs` est-il différent de `*args` ? Comment isoler les calculs réutilisables ?

**Défi supplémentaire :** accepter plusieurs ventes du **même produit** et vérifier qu'elles sont bien regroupées.

## Exercice 12 — Calculer un total dans un arbre de catégories

**Niveau :** 4/5 · **Notions :** récursivité, cas de base, parcours d'arbre, fonctions imbriquées.

**Situation :** une organisation représente ses catégories et sous-catégories en arborescence. Chaque nœud possède un nom, un montant local et des enfants.

**Travail demandé :** `analyser_arbre(racine)` renvoie `total`, `noms` (ordre de parcours **préfixe** : parent avant enfants) et `nombre_noeuds`. Un nœud a la forme `{'nom':'...', 'montant':100, 'enfants':[... ]}`. Le total est la **somme des montants de tous les nœuds**, pas uniquement celui des feuilles. Valider les noms non vides et les montants non négatifs. On suppose un arbre fini et sans cycle.

**Exemple :** Boutique(100) → Papeterie(50) → Stylos(20), et Boutique → Informatique(200) : total `370`, ordre `['Boutique','Papeterie','Stylos','Informatique']`, nombre de nœuds `4`.

**À réfléchir :** quel est le **cas de base** ? Pourquoi chaque appel récursif travaille-t-il sur un problème plus petit ? Quelle serait la conséquence d'une référence cyclique ?

**Défi supplémentaire :** calculer la profondeur maximale de l'arbre et la liste des feuilles.

## Exercice 13 — Un pipeline avec `filter()`, `map()` et `reduce()`

**Niveau :** 5/5 · **Notions :** fonctions d'ordre supérieur, `lambda`, composition, immutabilité.

**Situation :** les analystes veulent calculer rapidement un chiffre d'affaires sur n'importe quel ensemble de ventes, selon des règles variables (région, produit, volume…).

**Travail demandé :** coder `total_ventes_filtrees(ventes, predicat, transformation=None)` : `predicat` est une **fonction reçue en argument** qui décide si une vente est gardée ; `transformation` est une fonction optionnelle qui transforme une vente en montant. Par défaut, le montant vaut quantité × prix unitaire. Chaînez `filter()`, `map()` et `functools.reduce()`, puis arrondissez le résultat à 2 décimales. Retournez `0` si aucune vente ne correspond ; ne modifiez pas la liste source.

**Exemple :** ventes Nord : 2×1000 et 3×500 ; Sud : 1×800. Avec `lambda v: v['region'] == 'Nord'` → total `3500.0`.

**À réfléchir :** qu'est-ce qu'une fonction d'ordre supérieur ? Pourquoi fournit-on une valeur initiale à `reduce()` ? Que gagne-t-on en passant un **comportement** comme argument ?

**Défi supplémentaire :** fournir un transformateur qui applique une remise de 10 % seulement sur les ventes retenues.

## Exercice 14 — Une fabrique de fonctions avec closure et décorateur

**Niveau :** 5/5 · **Notions :** closure, état conservé, décorateur, `@wraps`, `*args`, `**kwargs`.

**Situation :** une plateforme applique différents taux de remise et de TVA selon le type de client. Vous voulez fabriquer une fonction spécialisée pour chaque configuration, et suivre combien de fois elle est appelée.

**Travail demandé :** écrire `fabriquer_tarificateur(remise_pct, tva_pct=16)` qui **retourne une fonction** `tarifer(prix_ht)`. Chaque fonction produite doit conserver ses propres taux et retourner `(prix_ht × (1 - remise/100)) × (1 + TVA/100)`, arrondi à 2 décimales. Écrire le décorateur général `compter_appels(fonction)` qui ajoute un attribut `.nb_appels`, initialisé à zéro puis incrémenté à chaque invocation ; employer `functools.wraps` et une enveloppe acceptant `*args, **kwargs`. Les taux doivent être dans [0, 100], le prix ≥ 0.

**Exemple :** `tarif = fabriquer_tarificateur(10,16)` ; `tarif(1000)` → `1044.0`, `tarif(500)` → `522.0`, `tarif.nb_appels` → `2`. Deux tarificateurs créés séparément doivent conserver **des compteurs indépendants**.

**À réfléchir :** pourquoi une fonction interne peut-elle encore accéder à `remise_pct` après la fin de la fonction externe ? Qu'ajoute réellement le décorateur : un nouveau résultat ou un comportement autour du calcul ?

**Défi supplémentaire :** écrire un décorateur de journalisation qui stocke les arguments sans enregistrer de mots de passe.

## Exercice 15 — Construire un mini-pipeline ETL avec des générateurs

**Niveau :** 5/5 · **Notions :** itérables, `yield`, validation, flux de données, fonctions composées.

**Situation :** vous recevez un très grand fichier de ventes. Le charger d'un seul coup dans une liste serait coûteux. Vous devez extraire et transformer les enregistrements **un à un**, puis construire un résumé.

**Format des lignes :** `date;produit;quantite;prix_unitaire`, avec dates `AAAA-MM-JJ`, quantités entières > 0, prix ≥ 0 ; des lignes vides sont possibles, et l'en-tête est facultatif.

**Travail demandé :** écrire `extraire_ventes(lignes, *, montant_minimum=0)` comme un **générateur** utilisant `yield`, qui renvoie des dictionnaires avec `date` (normalisée), `produit`, `quantite`, `prix_unitaire` et `montant`. Ignorer lignes vides et en-tête ; rejeter par `ValueError` les lignes mal formées. Émettre uniquement les ventes de montant ≥ seuil. Puis écrire `resumer_flux(lignes, *, montant_minimum=0)` qui consomme le générateur pour produire `nombre_ventes`, `total`, `par_produit`. Ne pas stocker toutes les ventes en mémoire.

**Exemple d'entrée :**

```text
date;produit;quantite;prix_unitaire
2026-10-01;Stylo;2;1500
2026-10-02;Cahier;1;4000
2026-10-03;Stylo;1;2000
```

**Exemple de sortie :** avec `montant_minimum=3000` → `{'nombre_ventes': 2, 'total': 7000.0, 'par_produit': {'Stylo': 3000.0, 'Cahier': 4000.0}}`.

**À réfléchir :** en quoi `yield` est-il différent de `return` ? À quel moment une erreur sur la 100e ligne est-elle effectivement levée ? Quelle mémoire utiliserait l'algorithme sur 1 million de lignes (hors stockage du résumé par produit) ?

**Défi supplémentaire :** traiter directement un vrai fichier CSV avec `with open(..., encoding='utf-8') as fichier:` en passant le fichier au générateur, puis écrire le résumé en JSON.

---

## Auto-évaluation finale (sans consulter les solutions)

- Puis-je identifier sans ambiguïté les **entrées, sorties, préconditions et cas limites** ?
- Puis-je expliquer le rôle de chaque **accumulateur**, **boucle** et **test** ?
- Puis-je justifier que ma **recherche binaire** et ma **récursivité** terminent ?
- Puis-je choisir une **liste**, un **dictionnaire**, une **matrice**, un **arbre** ou un **générateur** selon le problème ?
- Puis-je écrire une fonction qui reçoit **d'autres fonctions en arguments** ?
- Puis-je estimer la **complexité temporelle** et reconnaître les effets de bord ?
- Puis-je adapter mes algorithmes à de **nouvelles données** sans copier-coller ?

### Barème de progression conseillé

Chaque exercice peut recevoir 10 points : **2** pour le pseudocode, **4** pour la correction, **2** pour les tests (dont un cas limite), **1** pour les commentaires qui expliquent la logique, **1** pour l'analyse de complexité. Travaillez jusqu'à comprendre l'erreur, pas jusqu'à obtenir uniquement une sortie correcte.

**Fin du cahier :** 15 exercices ; les solutions commentées sont dans `exercices/`, les tests automatiques dans `tests/`.
