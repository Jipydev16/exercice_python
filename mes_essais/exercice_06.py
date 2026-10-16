def classer_scores(scores):
    restants = list(scores)
    for element in restants:
        if not isinstance(element, (tuple, list)) or len(element) != 2 or not isinstance(element[0], str) or not element[0].strip() or isinstance(element[1], bool) or not isinstance(element[1], (int, float)) or element[1] < 0:
            raise ValueError("Chaque score doit être (nom non vide, points >= 0)")
    classement = []
    while restants:
        meilleur = 0
        for i in range(1, len(restants)):
            if restants[i][1] > restants[meilleur][1]:
                meilleur = i
        classement.append(restants.pop(meilleur))
    return classement

def tri_insertion(scores):
    resultat = []
    for joueur in scores:
        i = len(resultat)
        while i > 0 and resultat[i-1][1] < joueur[1]:
            i -= 1
        resultat.insert(i, joueur)
    return resultat

if __name__ == "__main__":
    scores = []
    n = int(input("Nombre de joueurs : "))
    for _ in range(n):
        scores.append((input("Nom : "), float(input("Points : "))))
    print("Classement :", classer_scores(scores))
    print("Tri insertion identique ?", tri_insertion(scores) == classer_scores(scores))
