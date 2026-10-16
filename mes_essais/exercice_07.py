def recherche_premiere_occurrence(valeurs, cible):
    gauche, droite, resultat = 0, len(valeurs)-1, -1
    while gauche <= droite:
        milieu = (gauche + droite) // 2
        if valeurs[milieu] >= cible:
            if valeurs[milieu] == cible:
                resultat = milieu
            droite = milieu - 1
        else:
            gauche = milieu + 1
    return resultat

def recherche_derniere_occurrence(valeurs, cible):
    gauche, droite, resultat = 0, len(valeurs)-1, -1
    while gauche <= droite:
        milieu = (gauche + droite) // 2
        if valeurs[milieu] <= cible:
            if valeurs[milieu] == cible:
                resultat = milieu
            gauche = milieu + 1
        else:
            droite = milieu - 1
    return resultat

if __name__ == "__main__":
    valeurs = [float(x) for x in input("Valeurs triées croissantes (virgules) : ").split(",") if x.strip()]
    cible = float(input("Cible : "))
    debut = recherche_premiere_occurrence(valeurs, cible)
    fin = recherche_derniere_occurrence(valeurs, cible)
    print("Première occurrence :", debut)
    print("Dernière occurrence :", fin)
    print("Nombre d'apparitions :", 0 if debut == -1 else fin-debut+1)
