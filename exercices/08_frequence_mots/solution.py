"""Exercice 08 — Compter les mots d'un texte.

Notions : normalisation, chaînes, dictionnaires, comptage, règle d'égalité.
"""


def compter_mots(texte: str) -> dict[str, int]:
    """Compte les séquences alphanumériques, en ignorant la casse."""
    caracteres_normalises = []
    for caractere in texte.lower():
        # isalnum() inclut les lettres accentuées et les chiffres.
        # Une ponctuation devient espace afin de séparer les mots.
        caracteres_normalises.append(caractere if caractere.isalnum() else " ")

    mots = "".join(caracteres_normalises).split()
    frequences = {}
    for mot in mots:
        frequences[mot] = frequences.get(mot, 0) + 1
    return frequences


def mot_dominant(texte: str) -> tuple[str, int] | None:
    """Renvoie (mot, fréquence), avec départage alphabétique en cas d'égalité."""
    frequences = compter_mots(texte)
    meilleur_mot = None
    meilleur_nombre = 0
    for mot, nombre in frequences.items():
        if (nombre > meilleur_nombre or
                (nombre == meilleur_nombre and (meilleur_mot is None or mot < meilleur_mot))):
            meilleur_mot = mot
            meilleur_nombre = nombre
    if meilleur_mot is None:
        return None  # Un texte sans aucun mot est un cas à part.
    return meilleur_mot, meilleur_nombre


if __name__ == "__main__":
    phrase = "Python, python ! L'analyse des données avec Python."
    print(compter_mots(phrase))
    print("Mot dominant :", mot_dominant(phrase))
