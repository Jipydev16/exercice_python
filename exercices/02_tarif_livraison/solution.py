"""Exercice 02 — Calcul d'un tarif de livraison conditionnel.

Notions : if / elif / else, ordre des règles, frontières d'intervalles.
"""


def calculer_livraison(montant_panier: float, distance_km: float, premium: bool = False) -> dict:
    """Applique les règles métier et calcule le montant final du panier."""
    if montant_panier < 0 or distance_km < 0:
        raise ValueError("Le montant et la distance ne peuvent pas être négatifs.")

    # La gratuité est prioritaire : elle court-circuite tous les autres cas.
    if montant_panier >= 100_000:
        frais = 0.0
    elif distance_km <= 5:
        frais = 2_000.0
    elif distance_km <= 20:
        frais = 5_000.0
    else:
        frais = 9_000.0

    # Le statut premium réduit de moitié les frais qui restent applicables.
    if premium:
        frais *= 0.5

    return {"frais": frais, "total": round(montant_panier + frais, 2)}


if __name__ == "__main__":
    for panier, distance, premium in [(50_000, 5, False), (50_000, 21, True), (100_000, 50, False)]:
        print(panier, distance, premium, "=>", calculer_livraison(panier, distance, premium))
