"""Exercice 11 — Produire un rapport de ventes avec des fonctions modulaires.

Notions : décomposition fonctionnelle, *args, **kwargs, arguments par défaut,
arguments nommés et réutilisation des fonctions.
"""


def montant_ligne(produit: str, quantite: int, prix_unitaire: float) -> float:
    """Une fonction ne fait qu'une chose : calculer le montant d'une ligne."""
    if not isinstance(produit, str) or not produit.strip():
        raise ValueError("Produit non vide requis.")
    if not isinstance(quantite, int) or quantite <= 0 or prix_unitaire < 0:
        raise ValueError("Quantité > 0 et prix >= 0 requis.")
    return quantite * prix_unitaire


def analyser_ventes(*ventes: dict, tva_pct: float = 0.0, **contexte) -> dict:
    """Accepte un nombre variable de ventes et des métadonnées optionnelles.

    *ventes collecte les arguments positionnels dans un tuple.
    tva_pct est un argument nommé (placé après *ventes).
    **contexte recueille les autres arguments nommés dans un dictionnaire.
    """
    if not 0 <= tva_pct <= 100:
        raise ValueError("TVA comprise entre 0 et 100.")

    sous_total = 0.0
    quantite_articles = 0
    par_produit = {}

    for vente in ventes:
        # La fonction spécialisée vérifie également les données d'entrée.
        montant = montant_ligne(vente["produit"], vente["quantite"], vente["prix_unitaire"])
        sous_total += montant
        quantite_articles += vente["quantite"]
        produit = vente["produit"]
        par_produit[produit] = par_produit.get(produit, 0) + montant

    tva = sous_total * tva_pct / 100
    return {
        "sous_total": round(sous_total, 2),
        "tva": round(tva, 2),
        "total_ttc": round(sous_total + tva, 2),
        "quantite_articles": quantite_articles,
        "par_produit": {nom: round(valeur, 2) for nom, valeur in par_produit.items()},
        "contexte": dict(contexte),
    }


if __name__ == "__main__":
    rapport = analyser_ventes(
        {"produit": "Stylo", "quantite": 2, "prix_unitaire": 2500},
        {"produit": "Cahier", "quantite": 1, "prix_unitaire": 1000},
        tva_pct=16, magasin="Centre", responsable="Amina"
    )
    print(rapport)
