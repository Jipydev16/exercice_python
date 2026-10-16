def compter_mots(texte):
    frequences, courant = {}, ""
    for caractere in texte.casefold() + " ":
        if caractere.isalnum():
            courant += caractere
        elif courant:
            frequences[courant] = frequences.get(courant, 0) + 1
            courant = ""
    return frequences

def mot_dominant(texte):
    comptes = compter_mots(texte)
    if not comptes:
        return None
    return min(comptes.items(), key=lambda paire: (-paire[1], paire[0]))

if __name__ == "__main__":
    texte = input("Texte à analyser : ")
    print("Fréquences :", compter_mots(texte))
    print("Mot dominant :", mot_dominant(texte))
    print("Top 5 :", sorted(compter_mots(texte).items(), key=lambda p: (-p[1], p[0]))[:5])
