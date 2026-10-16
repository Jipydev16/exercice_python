"""Exercice 13 — Pipeline fonctionnel : filter, map, reduce et lambda.

Notions : passer une fonction comme argument, enchaîner les transformations,
réutiliser le même algorithme avec des critères différents, non-mutation.
"""

from functools import reduce
from collections.abc import Callable


def total_ventes_filtrees(
    ventes: list[dict],
    predicat: Callable[[dict], bool],
    transformation: Callable[[dict], float] | None = None,
) -> float:
    """Sélectionne des ventes puis additionne les valeurs transformées.

    predicat(vente) -> True si cette vente est retenue.
    transformation(vente) -> montant à additionner.
    """
    if transformation is None:
        # Fonction par défaut : quantité multipliée par prix unitaire.
        transformation = lambda vente: vente["quantite"] * vente["prix_unitaire"]

    # filter conserve seulement les ventes respectant le prédicat.
    ventes_retenues = filter(predicat, ventes)
    # map applique une fonction à chaque élément retenu (sans changer la source).
    montants = map(transformation, ventes_retenues)
    # reduce accumule les montants en partant de 0 ; évite l'échec sur liste vide.
    total = reduce(lambda cumul, montant: cumul + montant, montants, 0.0)
    return round(total, 2)


if __name__ == "__main__":
    ventes = [
        {"region": "Nord", "quantite": 2, "prix_unitaire": 1000},
        {"region": "Sud", "quantite": 1, "prix_unitaire": 800},
        {"region": "Nord", "quantite": 3, "prix_unitaire": 500},
    ]
    # lambda permet de définir une petite fonction juste au point d'utilisation.
    nord = total_ventes_filtrees(ventes, lambda v: v["region"] == "Nord")
    print("Chiffre d'affaires Nord :", nord)  # 3500.0
