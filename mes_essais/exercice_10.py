def compter_voisins(grille):
    if not isinstance(grille, list) or any(not isinstance(ligne, list) for ligne in grille):
        raise ValueError("La grille doit être une liste de lignes")
    colonnes = len(grille[0]) if grille else 0
    if any(len(ligne) != colonnes or any(type(v) is not int or v not in (0, 1) for v in ligne) for ligne in grille):
        raise ValueError("Grille irrégulière ou valeurs autres que 0 et 1")
    resultat = [[0] * colonnes for _ in grille]
    for i in range(len(grille)):
        for j in range(colonnes):
            for di in (-1, 0, 1):
                for dj in (-1, 0, 1):
                    ni, nj = i + di, j + dj
                    if (di or dj) and 0 <= ni < len(grille) and 0 <= nj < colonnes:
                        resultat[i][j] += grille[ni][nj]
    return resultat

def generation_suivante(grille):
    voisins = compter_voisins(grille)
    return [[int(voisins[i][j] == 3 or (grille[i][j] == 1 and voisins[i][j] == 2)) for j in range(len(ligne))] for i, ligne in enumerate(grille)]

if __name__ == "__main__":
    grille = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    print("Grille :", grille)
    print("Voisins :", compter_voisins(grille))
    print("Génération suivante :", generation_suivante(grille))
