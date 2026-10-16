def chiffrer_cesar(message, decalage):
    if not isinstance(decalage, int):
        raise ValueError("Décalage entier requis")
    resultat = ""
    for lettre in message:
        if "A" <= lettre <= "Z":
            resultat += chr((ord(lettre) - ord("A") + decalage) % 26 + ord("A"))
        elif "a" <= lettre <= "z":
            resultat += chr((ord(lettre) - ord("a") + decalage) % 26 + ord("a"))
        else:
            resultat += lettre
    return resultat

def dechiffrer_cesar(message, decalage):
    return chiffrer_cesar(message, -decalage)

if __name__ == "__main__":
    texte = input("Message : ")
    k = int(input("Décalage (entier, négatif permis) : "))
    code = chiffrer_cesar(texte, k)
    print("Chiffré :", code)
    print("Déchiffré :", dechiffrer_cesar(code, k))
    for test in [-29, -1, 0, 3, 26, 55]:
        assert dechiffrer_cesar(chiffrer_cesar(texte, test), test) == texte
    print("Tests aller-retour : OK")
