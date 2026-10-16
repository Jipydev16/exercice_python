"""Exercice 03 — Suivre un budget avec une boucle.

Notions : boucle for, accumulateur, compteur, maximum et cas de liste vide.
"""


def bilan_budget(depenses: list[float], budget: float) -> dict:
    """Retourne des indicateurs en parcourant les dépenses une seule fois."""
    if budget < 0:
        raise ValueError("Le budget ne peut pas être négatif.")

    total = 0.0         # Accumulateur : somme progressivement toutes les dépenses.
    nombre = 0          # Compteur : combien d'éléments ont été traités ?
    plus_grosse = 0.0   # Valeur neutre appropriée si toute dépense >= 0.

    for depense in depenses:
        if depense < 0:
            raise ValueError("Chaque dépense doit être positive ou nulle.")
        total += depense
        nombre += 1
        if depense > plus_grosse:
            plus_grosse = depense

    # Une liste vide n'a pas de moyenne mathématique ; on choisit 0 par convention.
    moyenne = total / nombre if nombre > 0 else 0.0
    return {
        "nombre": nombre,
        "total": round(total, 2),
        "moyenne": round(moyenne, 2),
        "plus_grosse": round(plus_grosse, 2),
        "reste": round(budget - total, 2),
        "depasse": total > budget,
    }


if __name__ == "__main__":
    print(bilan_budget([1200, 1800, 900], 5000))
