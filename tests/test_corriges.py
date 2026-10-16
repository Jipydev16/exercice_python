"""Tests de référence — lancer : python -m unittest discover -s tests -v

Chaque classe vérifie un exercice, incluant cas nominaux ET cas limites.
"""

import importlib
import unittest


def solution(nom):
    # importlib peut importer des dossiers préfixés par un chiffre, sans `import` statique.
    return importlib.import_module(f"exercices.{nom}.solution")


class Exercice01Ticket(unittest.TestCase):
    def setUp(self):
        self.f = solution("01_ticket_de_caisse").calculer_ticket

    def test_ticket_normal(self):
        r = self.f(2500, 3, 10)
        self.assertEqual(r, {"sous_total": 7500, "remise": 750,
                             "montant_ht": 6750, "tva": 1080, "total_ttc": 7830})

    def test_sans_taxation(self):
        self.assertEqual(self.f(10, 2, 0, 0)["total_ttc"], 20)

    def test_contre_entrees_invalides(self):
        with self.assertRaises(ValueError):
            self.f(100, 0, 10)
        with self.assertRaises(ValueError):
            self.f(-1, 2, 10)
        with self.assertRaises(ValueError):
            self.f(100, 1, 105)


class Exercice02Livraison(unittest.TestCase):
    def setUp(self):
        self.f = solution("02_tarif_livraison").calculer_livraison

    def test_frontieres(self):
        self.assertEqual(self.f(50_000, 5)["frais"], 2000)
        self.assertEqual(self.f(50_000, 5.01)["frais"], 5000)
        self.assertEqual(self.f(50_000, 20)["frais"], 5000)
        self.assertEqual(self.f(50_000, 20.01)["frais"], 9000)

    def test_priorite_gratuite_et_premium(self):
        self.assertEqual(self.f(100_000, 500)["frais"], 0)
        self.assertEqual(self.f(50_000, 25, premium=True)["total"], 54500)

    def test_invalide(self):
        with self.assertRaises(ValueError):
            self.f(1, -1)


class Exercice03Budget(unittest.TestCase):
    def setUp(self):
        self.f = solution("03_bilan_budget").bilan_budget

    def test_rapport(self):
        r = self.f([1200, 1800, 900], 5000)
        self.assertEqual((r["nombre"], r["total"], r["moyenne"], r["plus_grosse"]),
                         (3, 3900, 1300, 1800))
        self.assertFalse(r["depasse"])

    def test_vide_et_egalite(self):
        self.assertEqual(self.f([], 200)["moyenne"], 0)
        self.assertFalse(self.f([200], 200)["depasse"])

    def test_depense_invalide(self):
        with self.assertRaises(ValueError):
            self.f([1, -3], 10)


class Exercice04Premiers(unittest.TestCase):
    def setUp(self):
        m = solution("04_nombres_premiers")
        self.p = m.est_premier
        self.l = m.premiers_jusqua

    def test_premiers_non_premiers(self):
        self.assertEqual([self.p(n) for n in (-3, 0, 1, 2, 29, 49, 97)],
                         [False, False, False, True, True, False, True])

    def test_liste(self):
        self.assertEqual(self.l(20), [2, 3, 5, 7, 11, 13, 17, 19])
        self.assertEqual(self.l(1), [])


class Exercice05Cesar(unittest.TestCase):
    def setUp(self):
        m = solution("05_chiffrement_cesar")
        self.c, self.d = m.chiffrer_cesar, m.dechiffrer_cesar

    def test_exemple(self):
        self.assertEqual(self.c("Bonjour, Python!", 3), "Erqmrxu, Sbwkrq!")

    def test_bords_ponctuation_et_accents(self):
        self.assertEqual(self.c("Zz-Aa! été 123", 1), "Aa-Bb! éué 123")
        self.assertEqual(self.c("ABC", 26), "ABC")

    def test_aller_retour(self):
        for k in (-30, 0, 1, 7, 28):
            with self.subTest(decalage=k):
                self.assertEqual(self.d(self.c("Bonjour 2026, Kinshasa!", k), k),
                                 "Bonjour 2026, Kinshasa!")


class Exercice06Classement(unittest.TestCase):
    def setUp(self):
        self.f = solution("06_classement_scores").classer_scores

    def test_stable_et_entree_inalteree(self):
        data = [("Ada", 12), ("Lin", 18), ("Max", 12), ("Eva", 20)]
        self.assertEqual(self.f(data), [("Eva", 20), ("Lin", 18), ("Ada", 12), ("Max", 12)])
        self.assertEqual(data[0], ("Ada", 12))

    def test_liste_vide_et_egalites(self):
        self.assertEqual(self.f([]), [])
        self.assertEqual(self.f([("A", 0), ("B", 0)]), [("A", 0), ("B", 0)])

    def test_invalide(self):
        with self.assertRaises(ValueError):
            self.f([("A", -1)])


class Exercice07Binaire(unittest.TestCase):
    def setUp(self):
        self.f = solution("07_recherche_binaire").recherche_premiere_occurrence

    def test_doublons(self):
        self.assertEqual(self.f([2, 4, 4, 4, 9, 11], 4), 1)
        self.assertEqual(self.f([3, 3, 3], 3), 0)

    def test_absence_et_vide(self):
        self.assertEqual(self.f([], 4), -1)
        self.assertEqual(self.f([1, 3, 5], 4), -1)
        self.assertEqual(self.f([1, 3, 5], 5), 2)


class Exercice08Mots(unittest.TestCase):
    def setUp(self):
        m = solution("08_frequence_mots")
        self.c, self.d = m.compter_mots, m.mot_dominant

    def test_comptage(self):
        self.assertEqual(self.c("Python, python !"), {"python": 2})
        self.assertEqual(self.c("été Été"), {"été": 2})

    def test_departage_et_vide(self):
        self.assertEqual(self.d("zèbre pomme pomme zèbre"), ("pomme", 2))
        self.assertIsNone(self.d("!?, ;"))


class Exercice09Stock(unittest.TestCase):
    def setUp(self):
        self.f = solution("09_gestion_stock").appliquer_mouvements

    def test_mouvements_et_nouveau_produit(self):
        initial = {"Stylo": 10, "Cahier": 4}
        mouvements = [
            {"produit": "Stylo", "type": "sortie", "quantite": 3},
            {"produit": "Classeur", "type": "entree", "quantite": 2},
        ]
        self.assertEqual(self.f(initial, mouvements),
                         {"Stylo": 7, "Cahier": 4, "Classeur": 2})
        self.assertEqual(initial, {"Stylo": 10, "Cahier": 4})

    def test_atomicite_sur_erreur(self):
        initial = {"Stylo": 10}
        ops = [
            {"produit": "Stylo", "type": "entree", "quantite": 2},
            {"produit": "Stylo", "type": "sortie", "quantite": 99},
        ]
        with self.assertRaises(ValueError):
            self.f(initial, ops)
        self.assertEqual(initial, {"Stylo": 10})

    def test_mouvement_invalide(self):
        with self.assertRaises(ValueError):
            self.f({}, [{"produit": "X", "type": "entree", "quantite": 0}])


class Exercice10Grille(unittest.TestCase):
    def setUp(self):
        self.f = solution("10_grille_voisins").compter_voisins

    def test_diagonale(self):
        grille = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        self.assertEqual(self.f(grille), [[1, 2, 1], [2, 2, 2], [1, 2, 1]])
        self.assertEqual(grille[0], [1, 0, 0])

    def test_taille_minimale(self):
        self.assertEqual(self.f([]), [])
        self.assertEqual(self.f([[1]]), [[0]])
        self.assertEqual(self.f([[]]), [[]])

    def test_invalide(self):
        with self.assertRaises(ValueError):
            self.f([[1, 0], [1]])
        with self.assertRaises(ValueError):
            self.f([[2]])


class Exercice11Variadiques(unittest.TestCase):
    def setUp(self):
        m = solution("11_fonctions_variadiques")
        self.f, self.l = m.analyser_ventes, m.montant_ligne

    def test_rapport_et_contexte(self):
        r = self.f({"produit": "Stylo", "quantite": 2, "prix_unitaire": 2500},
                   {"produit": "Cahier", "quantite": 1, "prix_unitaire": 1000},
                   tva_pct=16, magasin="Centre")
        self.assertEqual((r["sous_total"], r["tva"], r["total_ttc"], r["quantite_articles"]),
                         (6000, 960, 6960, 3))
        self.assertEqual(r["par_produit"], {"Stylo": 5000, "Cahier": 1000})
        self.assertEqual(r["contexte"], {"magasin": "Centre"})

    def test_regroupement_et_vide(self):
        vente = {"produit": "Stylo", "quantite": 1, "prix_unitaire": 1000}
        self.assertEqual(self.f(vente, vente)["par_produit"]["Stylo"], 2000)
        self.assertEqual(self.f()["quantite_articles"], 0)

    def test_invalide(self):
        with self.assertRaises(ValueError):
            self.l("Stylo", -1, 100)
        with self.assertRaises(ValueError):
            self.f(tva_pct=200)


class Exercice12Recursion(unittest.TestCase):
    def setUp(self):
        self.f = solution("12_recursion_arbre").analyser_arbre

    def test_arbre(self):
        arbre = {"nom": "Boutique", "montant": 100, "enfants": [
            {"nom": "Papeterie", "montant": 50, "enfants": [
                {"nom": "Stylos", "montant": 20, "enfants": []}
            ]},
            {"nom": "Informatique", "montant": 200, "enfants": []},
        ]}
        self.assertEqual(self.f(arbre), {"total": 370, "noms": [
            "Boutique", "Papeterie", "Stylos", "Informatique"], "nombre_noeuds": 4})

    def test_feuille(self):
        self.assertEqual(self.f({"nom": "Solo", "montant": 12})["nombre_noeuds"], 1)

    def test_invalide(self):
        with self.assertRaises(ValueError):
            self.f({"nom": "", "montant": 1})


class Exercice13Fonctionnel(unittest.TestCase):
    def setUp(self):
        self.f = solution("13_fonctions_ordre_superieur").total_ventes_filtrees
        self.ventes = [
            {"region": "Nord", "quantite": 2, "prix_unitaire": 1000},
            {"region": "Sud", "quantite": 1, "prix_unitaire": 800},
            {"region": "Nord", "quantite": 3, "prix_unitaire": 500},
        ]

    def test_filtre(self):
        self.assertEqual(self.f(self.ventes, lambda v: v["region"] == "Nord"), 3500)

    def test_transformateur_personnalise(self):
        self.assertEqual(self.f(self.ventes, lambda v: True,
                                lambda v: v["quantite"] * v["prix_unitaire"] * 0.9), 3870)
        self.assertEqual(self.f(self.ventes, lambda v: False), 0)
        self.assertEqual(len(self.ventes), 3)


class Exercice14Closures(unittest.TestCase):
    def setUp(self):
        m = solution("14_closures_decorateurs")
        self.f, self.d = m.fabriquer_tarificateur, m.compter_appels

    def test_closure_compteur(self):
        tarif = self.f(10, 16)
        self.assertEqual(tarif(1000), 1044)
        self.assertEqual(tarif(500), 522)
        self.assertEqual(tarif.nb_appels, 2)
        self.assertEqual(tarif.__name__, "tarifer")

    def test_etats_independants(self):
        a = self.f(10, 0)
        b = self.f(20, 0)
        self.assertEqual(a(100), 90)
        self.assertEqual(b(100), 80)
        self.assertEqual((a.nb_appels, b.nb_appels), (1, 1))

    def test_arguments_invalides(self):
        with self.assertRaises(ValueError):
            self.f(110)
        with self.assertRaises(ValueError):
            self.f(10)(-1)


class Exercice15Generateurs(unittest.TestCase):
    def setUp(self):
        m = solution("15_generateurs_etl")
        self.extraire, self.resumer = m.extraire_ventes, m.resumer_flux
        self.lignes = [
            "date;produit;quantite;prix_unitaire",
            "2026-10-01;Stylo;2;1500",
            "2026-10-02;Cahier;1;4000",
            "2026-10-03;Stylo;1;2000",
        ]

    def test_extraction_et_filtrage(self):
        ventes = list(self.extraire(self.lignes, montant_minimum=3000))
        self.assertEqual(len(ventes), 2)
        self.assertEqual(ventes[0]["montant"], 3000)
        self.assertEqual(ventes[0]["date"], "2026-10-01")

    def test_agregation(self):
        self.assertEqual(self.resumer(self.lignes, montant_minimum=3000),
                         {"nombre_ventes": 2, "total": 7000,
                          "par_produit": {"Stylo": 3000, "Cahier": 4000}})

    def test_erreur_evaluee_paresseusement(self):
        generateur = self.extraire(["2026-10-01;Cahier;1;100", "ligne incorrecte"])
        self.assertEqual(next(generateur)["montant"], 100)
        with self.assertRaises(ValueError):
            next(generateur)

    def test_vide(self):
        self.assertEqual(self.resumer([])["total"], 0)


if __name__ == "__main__":
    unittest.main()
