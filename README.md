# Atelier Python — 15 exercices d'algorithmique

Ce projet autonome vous entraîne **des variables et boucles jusqu'aux fonctions avancées**, avec un **énoncé détaillé**, **15 corrigés Python abondamment commentés**, des **tests unitaires** et un **espace de travail personnel**.

## Démarrage rapide

**Pré-requis :** Python 3.10 ou version plus récente. Aucune dépendance externe (`pip install` inutile).

1. Décompressez le fichier ZIP et ouvrez le dossier dans **VS Code**, PyCharm ou un terminal.
2. Lisez [EXERCICES.md](EXERCICES.md), puis choisissez la question n° 01.
3. Programmez votre tentative dans `mes_essais/exercice_01.py` avant d'ouvrir le corrigé.
4. Consultez `exercices/01_ticket_de_caisse/solution.py` **après** avoir essayé.
5. Lancez les tests et comparez les cas normaux et les cas limites.

### Commandes utiles

Depuis la racine du projet :

```bash
# Afficher la version installée
python --version

# Exécuter un corrigé concret
python exercices/01_ticket_de_caisse/solution.py

# Exécuter le mini-pipeline final
python exercices/15_generateurs_etl/solution.py

# Lancer tous les tests automatiques
python -m unittest discover -s tests -v
```

Sur Windows, si la commande `python` n'est pas reconnue, essayez `py` à la place.

## Structure du dossier

```text
projet_python_15_exercices/
├── README.md                  # Guide de démarrage
├── EXERCICES.md               # Les 15 énoncés, progressifs et sans corrigés
├── exercices/
│   ├── 01_ticket_de_caisse/
│   │   └── solution.py        # Corrigé commenté + démo exécutable
│   ├── 02_tarif_livraison/
│   ├── ...
│   └── 15_generateurs_etl/
│       └── solution.py
├── mes_essais/                # Fichiers de départ à compléter
│   ├── exercice_01.py
│   ├── ...
│   └── exercice_15.py
└── tests/
    └── test_corriges.py      # Tests unitaires pour les 15 solutions
```

## Progression pédagogique

- **01 à 03 :** exprimer des règles commerciales avec calculs, conditions et boucles.
- **04 à 06 :** bâtir un algorithme pour les nombres, le texte et le classement.
- **07 à 09 :** maîtriser recherche dichotomique, fréquences et stock.
- **10 à 12 :** décomposer matrices, fonctions variadiques et arbres récursifs.
- **13 à 15 :** fonctions d'ordre supérieur, closures, décorateurs et générateurs ETL.

## Pour progresser sans tricher

Rédigez un pseudocode, testez votre hypothèse sur papier, faites au moins trois tests, puis lisez le corrigé. Les tests fournis vérifient les solutions de référence : pour contrôler **vos propres réponses**, adaptez leurs imports pour pointer vers `mes_essais/` lorsque votre code est prêt.

**Point pédagogique important :** les exemples commerciaux emploient des `float` pour rester accessibles ; pour de vrais paiements, utilisez `decimal.Decimal` et les règles d'arrondi propres au métier. Les données des exercices sont fictives.
