"""Exercice 06 — Classer des scores avec un tri par sélection.

Notions : listes, indices, comparaisons, algorithme de tri, stabilité, O(n²).
Interdit ici : sort(), sorted() et max().
"""


def classer_scores(scores: list[tuple[str, int]]) -> list[tuple[str, int]]:
    """Trie en ordre décroissant ; conserve l'ordre d'entrée en cas d'égalité."""
    # On travaille sur une COPIE : pas d'effet de bord pour le code appelant.
    restants = list(scores)
    classement = []

    for nom, points in restants:
        if not isinstance(nom, str) or not nom.strip() or not isinstance(points, int) or points < 0:
            raise ValueError("Chaque entrée doit être (nom non vide, score entier >= 0).")

    while restants:
        indice_meilleur = 0
        # On cherche l'indice du plus grand score parmi ceux qui restent.
        for i in range(1, len(restants)):
            # Strictement > : en cas d'égalité, le premier gagne (tri stable).
            if restants[i][1] > restants[indice_meilleur][1]:
                indice_meilleur = i
        classement.append(restants.pop(indice_meilleur))

    # n recherches de maximum, chacune sur au plus n éléments : O(n²).
    return classement


if __name__ == "__main__":
    joueurs = [("Ada", 12), ("Lin", 18), ("Max", 12), ("Eva", 20)]
    print(classer_scores(joueurs))
    print("Liste d'origine intacte :", joueurs)
