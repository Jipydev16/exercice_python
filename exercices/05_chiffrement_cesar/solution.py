"""Exercice 05 — Chiffrer puis déchiffrer un message (chiffrement de César).

Notions : chaînes, ord/chr, modulo, fonctions inverses, tests aller-retour.
Ce procédé n'est PAS destiné à sécuriser de vraies données.
"""


def chiffrer_cesar(message: str, decalage: int) -> str:
    """Décale seulement les lettres ASCII A-Z et a-z, en gardant les autres."""
    resultat = []
    decalage = decalage % 26  # Un tour complet de l'alphabet ne change rien.

    for caractere in message:
        if "A" <= caractere <= "Z":
            base = ord("A")
        elif "a" <= caractere <= "z":
            base = ord("a")
        else:
            # Ponctuation, espaces et accents sont recopiés tels quels.
            resultat.append(caractere)
            continue

        # ord transforme la lettre en entier ; % 26 assure le retour à A/a.
        position = ord(caractere) - base
        nouvelle_position = (position + decalage) % 26
        resultat.append(chr(base + nouvelle_position))

    return "".join(resultat)  # Plus efficace que concaténer dans une boucle.


def dechiffrer_cesar(message: str, decalage: int) -> str:
    """Le déchiffrement est simplement le décalage opposé."""
    return chiffrer_cesar(message, -decalage)


if __name__ == "__main__":
    code = chiffrer_cesar("Bonjour, Python!", 3)
    print("Chiffré :", code)
    print("Original :", dechiffrer_cesar(code, 3))
