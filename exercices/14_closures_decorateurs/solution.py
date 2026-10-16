"""Exercice 14 — Fabrique de tarificateurs, fermeture et décorateur.

Notions : closure (fermeture), fonctions comme valeurs, @decorator, wraps,
*args/**kwargs, état persistant entre appels.
"""

from functools import wraps


def compter_appels(fonction):
    """Décorateur : ajoute un compteur à toute fonction sans changer son calcul."""
    @wraps(fonction)  # Conserve __name__ et la documentation de la fonction.
    def enveloppe(*args, **kwargs):
        # *args et **kwargs rendent le décorateur indépendant de la signature.
        enveloppe.nb_appels += 1
        return fonction(*args, **kwargs)

    enveloppe.nb_appels = 0
    return enveloppe


def fabriquer_tarificateur(remise_pct: float, tva_pct: float = 16.0):
    """Construit une nouvelle fonction qui MÉMORISE remise et TVA."""
    if not 0 <= remise_pct <= 100 or not 0 <= tva_pct <= 100:
        raise ValueError("Remise et TVA doivent être entre 0 et 100.")

    @compter_appels
    def tarifer(prix_ht: float) -> float:
        if prix_ht < 0:
            raise ValueError("Prix négatif interdit.")
        # Fermeture : remise_pct et tva_pct restent disponibles après le return.
        apres_remise = prix_ht * (1 - remise_pct / 100)
        return round(apres_remise * (1 + tva_pct / 100), 2)

    return tarifer  # On retourne une FONCTION, pas son résultat.


if __name__ == "__main__":
    tarif_etudiant = fabriquer_tarificateur(remise_pct=10, tva_pct=16)
    print("Prix final :", tarif_etudiant(1000))  # 1044.0
    print("Prix final :", tarif_etudiant(500))   # 522.0
    print("Nombre d'appels :", tarif_etudiant.nb_appels)  # 2
