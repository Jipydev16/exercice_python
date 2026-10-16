def bilan_budget(depenses, budget):
    if budget < 0:
        raise ValueError("Budget négatif")
    nombre, total, plus_grosse = 0, 0, 0
    for depense in depenses:
        if depense < 0:
            raise ValueError("Dépense négative")
        nombre += 1
        total += depense
        if depense > plus_grosse:
            plus_grosse = depense
    moyenne = total / nombre if nombre else 0
    return {"nombre": nombre, "total": total, "moyenne": moyenne, "plus_grosse": plus_grosse, "reste": budget-total, "depasse": total > budget}

if __name__ == "__main__":
    depenses = [float(x.strip()) for x in input("Dépenses séparées par des virgules (vide = aucune) : ").split(",") if x.strip()]
    budget = float(input("Budget : "))
    print(bilan_budget(depenses, budget))
    resultat = bilan_budget(depenses, budget)
    print("Dépenses supérieures à la moyenne :", len([d for d in depenses if d > resultat["moyenne"]]))
