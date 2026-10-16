def montant_ligne(produit, quantite, prix_unitaire):
    if not isinstance(produit, str) or not produit.strip() or type(quantite) is not int or quantite <= 0 or prix_unitaire < 0:
        raise ValueError("Ligne de vente invalide")
    return quantite * prix_unitaire

def analyser_ventes(*ventes, tva_pct=0.0, **contexte):
    if not 0 <= tva_pct <= 100:
        raise ValueError("TVA invalide")
    sous_total, quantite_articles, par_produit = 0, 0, {}
    for vente in ventes:
        montant = montant_ligne(vente["produit"], vente["quantite"], vente["prix_unitaire"])
        sous_total += montant
        quantite_articles += vente["quantite"]
        nom = vente["produit"]
        par_produit[nom] = par_produit.get(nom, 0) + montant
    tva = sous_total * tva_pct / 100
    return {"sous_total": round(sous_total, 2), "tva": round(tva, 2), "total_ttc": round(sous_total+tva, 2), "quantite_articles": quantite_articles, "par_produit": {k: round(v, 2) for k, v in par_produit.items()}, "contexte": contexte}

if __name__ == "__main__":
    ventes = [{"produit": "Stylo", "quantite": 2, "prix_unitaire": 2500}, {"produit": "Cahier", "quantite": 1, "prix_unitaire": 1000}, {"produit": "Stylo", "quantite": 1, "prix_unitaire": 500}]
    print(analyser_ventes(*ventes, tva_pct=16, magasin="Boutique A", responsable="Ada"))
