"""Exercice 07 — Recherche dichotomique dans une liste triée.

Notions : invariants, bornes gauche/droite, division du problème, O(log n).
Précondition : la liste est déjà triée en ordre croissant.
"""


def recherche_premiere_occurrence(valeurs: list[int], cible: int) -> int:
    """Renvoie l'indice de la première occurrence, ou -1 si absente."""
    gauche = 0
    droite = len(valeurs) - 1
    reponse = -1  # On mémorise une occurrence potentielle.

    while gauche <= droite:
        milieu = (gauche + droite) // 2
        if valeurs[milieu] == cible:
            reponse = milieu
            # On ne s'arrête PAS : une occurrence plus à gauche est possible.
            droite = milieu - 1
        elif valeurs[milieu] < cible:
            # La moitié gauche est trop petite : on peut l'écarter.
            gauche = milieu + 1
        else:
            droite = milieu - 1

    # À chaque boucle, l'intervalle de recherche diminue au moins de moitié.
    return reponse


if __name__ == "__main__":
    print(recherche_premiere_occurrence([2, 4, 4, 4, 9, 11], 4))  # 1
    print(recherche_premiere_occurrence([2, 4, 9], 7))           # -1
