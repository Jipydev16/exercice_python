"""Exercice 10 — Compter les voisins actifs sur une grille 2D.

Notions : boucles imbriquées, matrices, frontières, invariants, O(lignes*colonnes).
"""


def compter_voisins(grille: list[list[int]]) -> list[list[int]]:
    """Renvoie pour chaque case le nombre de ses 8 voisines contenant 1."""
    if not grille:
        return []
    colonnes = len(grille[0])
    lignes = len(grille)

    # Une matrice non rectangulaire rendrait les index incohérents.
    if any(len(ligne) != colonnes for ligne in grille):
        raise ValueError("Toutes les lignes doivent avoir la même longueur.")
    if any(case not in (0, 1) for ligne in grille for case in ligne):
        raise ValueError("Chaque case doit valoir 0 ou 1.")

    resultat = []
    for i in range(lignes):
        ligne_resultat = []
        for j in range(colonnes):
            total = 0
            # (-1,0,1) représente les positions relatives de la case voisine.
            for delta_i in (-1, 0, 1):
                for delta_j in (-1, 0, 1):
                    if delta_i == 0 and delta_j == 0:
                        continue  # Ne pas compter la case centrale elle-même.
                    ni, nj = i + delta_i, j + delta_j
                    if 0 <= ni < lignes and 0 <= nj < colonnes:
                        total += grille[ni][nj]
            ligne_resultat.append(total)
        resultat.append(ligne_resultat)
    return resultat  # La grille d'origine est intacte.


if __name__ == "__main__":
    grille = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    print(*compter_voisins(grille), sep="\n")
