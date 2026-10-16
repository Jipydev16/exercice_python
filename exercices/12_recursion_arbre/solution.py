"""Exercice 12 — Parcourir un arbre de catégories avec la récursivité.

Notions : cas de base, appel récursif, arborescence, parcours préfixe, O(n).
"""


def analyser_arbre(racine: dict) -> dict:
    """Calcule la somme des montants et les noms dans l'ordre préfixe."""
    noms = []
    total = 0.0

    def visiter(noeud: dict) -> None:
        nonlocal total  # Indique qu'on modifie le total de la fonction englobante.
        nom = noeud["nom"]
        montant = noeud["montant"]
        if not isinstance(nom, str) or not nom.strip() or montant < 0:
            raise ValueError("Chaque nœud doit avoir un nom et un montant >= 0.")

        # Étape d'entrée : traiter d'abord le nœud actuel (parcours préfixe).
        noms.append(nom)
        total += montant

        # Cas de base implicite : si enfants=[], la boucle ne fait rien.
        # Sinon, chaque enfant est un problème identique, mais plus petit.
        for enfant in noeud.get("enfants", []):
            visiter(enfant)

    visiter(racine)
    # Pour n nœuds, une visite chacun => O(n) en temps.
    # La profondeur de la récursion dépend de la hauteur de l'arbre.
    return {"total": round(total, 2), "noms": noms, "nombre_noeuds": len(noms)}


if __name__ == "__main__":
    donnees = {
        "nom": "Boutique", "montant": 100,
        "enfants": [
            {"nom": "Papeterie", "montant": 50, "enfants": [
                {"nom": "Stylos", "montant": 20, "enfants": []}
            ]},
            {"nom": "Informatique", "montant": 200, "enfants": []},
        ],
    }
    print(analyser_arbre(donnees))
