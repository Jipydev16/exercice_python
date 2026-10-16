"""Exercice 09 — Simuler des mouvements de stock.

Notions : dictionnaires, listes d'objets, validation, copie et atomicité.
"""


def appliquer_mouvements(stock_initial: dict[str, int], mouvements: list[dict]) -> dict[str, int]:
    """Renvoie un NOUVEAU stock ; si un mouvement est invalide, lève ValueError.

    L'appelant conserve toujours son dictionnaire d'origine, même si une
    erreur survient après plusieurs mouvements : effet 'tout ou rien'.
    """
    # Vérifier les stocks existants AVANT de commencer les mises à jour.
    for produit, quantite in stock_initial.items():
        if not isinstance(produit, str) or not produit.strip():
            raise ValueError("Nom de produit initial invalide.")
        if not isinstance(quantite, int) or quantite < 0:
            raise ValueError("Chaque quantité initiale doit être un entier >= 0.")

    stock = stock_initial.copy()  # Une copie suffit : les valeurs sont des int.
    for mouvement in mouvements:
        try:
            produit = mouvement["produit"]
            operation = mouvement["type"]
            quantite = mouvement["quantite"]
        except (KeyError, TypeError) as erreur:
            raise ValueError("Mouvement incomplet : produit, type, quantite requis.") from erreur

        if not isinstance(produit, str) or not produit.strip():
            raise ValueError("Nom de produit invalide.")
        if operation not in ("entree", "sortie"):
            raise ValueError("Type de mouvement inconnu.")
        if not isinstance(quantite, int) or quantite <= 0:
            raise ValueError("La quantité d'un mouvement doit être un entier > 0.")

        disponible = stock.get(produit, 0)
        if operation == "entree":
            stock[produit] = disponible + quantite
        else:
            if quantite > disponible:
                raise ValueError(f"Stock insuffisant pour {produit}.")
            stock[produit] = disponible - quantite

    return stock


if __name__ == "__main__":
    initial = {"Stylo": 10, "Cahier": 4}
    ops = [
        {"produit": "Stylo", "type": "sortie", "quantite": 3},
        {"produit": "Classeur", "type": "entree", "quantite": 2},
    ]
    print("Avant :", initial)
    print("Après :", appliquer_mouvements(initial, ops))
