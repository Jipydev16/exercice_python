def est_premier(n):
    if n < 2:
        return False
    diviseur = 2
    while diviseur * diviseur <= n:
        if n % diviseur == 0:
            return False
        diviseur += 1
    return True

def premiers_jusqua(limite):
    return [n for n in range(2, limite + 1) if est_premier(n)]

def crible(limite):
    if limite < 2:
        return []
    premier = [True] * (limite + 1)
    premier[0] = premier[1] = False
    for i in range(2, int(limite ** .5) + 1):
        if premier[i]:
            for j in range(i*i, limite+1, i):
                premier[j] = False
    return [i for i in range(limite+1) if premier[i]]

if __name__ == "__main__":
    n = int(input("Entier à tester : "))
    limite = int(input("Lister les nombres premiers jusqu'à : "))
    print("Premier ?", est_premier(n))
    print("Liste :", premiers_jusqua(limite))
    print("Crible identique ?", crible(limite) == premiers_jusqua(limite))
