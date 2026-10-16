"""Exercice 04 — Tester et énumérer des nombres premiers.

Notions : booléens, modulo (%), boucles, condition d'arrêt, complexité.
"""


def est_premier(n: int) -> bool:
    """Vrai si et seulement si n possède exactement deux diviseurs positifs."""
    if n < 2:  # 0, 1 et les nombres négatifs ne sont pas premiers.
        return False
    diviseur = 2
    # Si n = a*b, l'un des deux facteurs est <= sqrt(n).
    # On peut donc arrêter dès que diviseur² dépasse n.
    while diviseur * diviseur <= n:
        if n % diviseur == 0:  # Un diviseur suffit pour conclure : composé.
            return False
        diviseur += 1
    return True


def premiers_jusqua(limite: int) -> list[int]:
    """Réutilise est_premier plutôt que de dupliquer l'algorithme."""
    resultat = []
    for nombre in range(2, limite + 1):
        if est_premier(nombre):
            resultat.append(nombre)
    return resultat


if __name__ == "__main__":
    print("29 est premier ?", est_premier(29))
    print("Premiers jusqu'à 20 :", premiers_jusqua(20))
