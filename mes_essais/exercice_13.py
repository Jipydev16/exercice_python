from functools import reduce

def total_ventes_filtrees(ventes, predicat, transformation=None):
    if transformation is None:
        transformation = lambda v: v["quantite"] * v["prix_unitaire"]
    return round(reduce(lambda total, montant: total + montant, map(transformation, filter(predicat, ventes)), 0), 2)

if __name__ == "__main__":
    ventes = [{"region": "Nord", "quantite": 2, "prix_unitaire": 1000}, {"region": "Nord", "quantite": 3, "prix_unitaire": 500}, {"region": "Sud", "quantite": 1, "prix_unitaire": 800}]
    nord = lambda v: v["region"] == "Nord"
    print("Total Nord :", total_ventes_filtrees(ventes, nord))
    print("Nord avec remise 10 % :", total_ventes_filtrees(ventes, nord, lambda v: v["quantite"] * v["prix_unitaire"] * .9))
