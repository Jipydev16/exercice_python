"""Exercice 01 — Calculer un ticket de caisse.

Notions : variables, opérations, pourcentages, validation, ordre des calculs.
Exécuter : python exercices/01_ticket_de_caisse/solution.py
"""


def calculer_ticket(prix_unitaire: float, quantite: int, remise_pct: float, tva_pct: float = 16) -> dict:
    """Calcule les étapes d'une vente et renvoie un ticket explicatif."""
    # On vérifie d'abord les préconditions pour éviter des résultats incohérents.
    if prix_unitaire < 0 or not isinstance(quantite, int) or quantite < 1:
        raise ValueError("Prix >= 0 et quantité entière >= 1 requis.")
    if not 0 <= remise_pct <= 100 or not 0 <= tva_pct <= 100:
        raise ValueError("Les pourcentages doivent être compris entre 0 et 100.")

    # Étape 1 : multiplication. Le sous-total ignore encore remise et taxe.
    sous_total = prix_unitaire * quantite
    # Étape 2 : le pourcentage se convertit en fraction (10 % devient 0,10).
    remise = sous_total * remise_pct / 100
    # Étape 3 : la TVA porte sur la somme après remise, pas avant.
    montant_ht = sous_total - remise
    tva = montant_ht * tva_pct / 100
    total_ttc = montant_ht + tva

    # Arrondir à l'affichage évite de perdre de la précision en cours de calcul.
    return {
        "sous_total": round(sous_total, 2),
        "remise": round(remise, 2),
        "montant_ht": round(montant_ht, 2),
        "tva": round(tva, 2),
        "total_ttc": round(total_ttc, 2),
    }


if __name__ == "__main__":
    exemple = calculer_ticket(2500, 3, 10)
    print("Ticket de caisse (CDF) :", exemple)
    # 7500 - 750 = 6750 ; TVA = 1080 ; TTC = 7830.
