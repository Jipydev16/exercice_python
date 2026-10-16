"""Exercice 15 — Mini pipeline ETL paresseux avec un générateur Python.

Notions : parsing, validation, yield, itérables, filtrage, agrégation,
composition de fonctions, mémoire O(1) pour l'extraction.

Entrée : chaînes CSV séparées par « ; » :
    date;produit;quantite;prix_unitaire
    2026-10-01;Stylo;2;1500
"""

from collections.abc import Iterable, Iterator
from datetime import datetime


def extraire_ventes(lignes: Iterable[str], *, montant_minimum: float = 0) -> Iterator[dict]:
    """Transforme les lignes une par une ; ne charge pas toutes les ventes en RAM."""
    if montant_minimum < 0:
        raise ValueError("Le seuil minimal ne peut pas être négatif.")

    for numero, ligne in enumerate(lignes, start=1):
        texte = ligne.strip()
        if not texte:
            continue  # Ignorer les lignes vides.
        if texte.lower().replace(" ", "") == "date;produit;quantite;prix_unitaire":
            continue  # Accepter un en-tête de colonnes facultatif.

        morceaux = [partie.strip() for partie in texte.split(";")]
        if len(morceaux) != 4:
            raise ValueError(f"Ligne {numero} : 4 colonnes attendues.")

        date_brute, produit, q_brute, p_brut = morceaux
        try:
            # Vérifie qu'il s'agit d'une vraie date du calendrier.
            jour = datetime.strptime(date_brute, "%Y-%m-%d").date()
            quantite = int(q_brute)
            prix_unitaire = float(p_brut)
        except ValueError as erreur:
            raise ValueError(f"Ligne {numero} : valeur invalide.") from erreur

        if not produit or quantite <= 0 or prix_unitaire < 0:
            raise ValueError(f"Ligne {numero} : produit, quantité ou prix incorrect.")

        montant = round(quantite * prix_unitaire, 2)
        if montant < montant_minimum:
            continue  # Filtrage réalisé AVANT de produire la valeur.

        # yield suspend la fonction jusqu'à la demande du consommateur.
        yield {
            "date": jour.isoformat(),
            "produit": produit,
            "quantite": quantite,
            "prix_unitaire": prix_unitaire,
            "montant": montant,
        }


def resumer_flux(lignes: Iterable[str], *, montant_minimum: float = 0) -> dict:
    """Consomme le générateur et regroupe les ventes par produit."""
    total = 0.0
    compte = 0
    par_produit = {}
    for vente in extraire_ventes(lignes, montant_minimum=montant_minimum):
        total += vente["montant"]
        compte += 1
        p = vente["produit"]
        par_produit[p] = par_produit.get(p, 0.0) + vente["montant"]

    # Ici, on ne conserve que l'agrégat, pas toute la liste des transactions.
    return {
        "nombre_ventes": compte,
        "total": round(total, 2),
        "par_produit": {p: round(m, 2) for p, m in par_produit.items()},
    }


if __name__ == "__main__":
    fichier_simule = [
        "date;produit;quantite;prix_unitaire",
        "2026-10-01;Stylo;2;1500",
        "2026-10-02;Cahier;1;4000",
        "2026-10-03;Stylo;1;2000",
    ]
    print("Ventes filtrées :", list(extraire_ventes(fichier_simule, montant_minimum=3000)))
    print("Résumé :", resumer_flux(fichier_simule, montant_minimum=3000))
