from datetime import date
import json

def extraire_ventes(lignes, *, montant_minimum=0):
    if montant_minimum < 0:
        raise ValueError("Seuil négatif")
    for numero, ligne in enumerate(lignes, 1):
        ligne = ligne.strip().lstrip("\ufeff")
        if not ligne or ligne.lower() == "date;produit;quantite;prix_unitaire":
            continue
        champs = [x.strip() for x in ligne.split(";")]
        if len(champs) != 4:
            raise ValueError(f"Ligne {numero} mal formée")
        jour, produit, quantite_txt, prix_txt = champs
        try:
            jour = date.fromisoformat(jour).isoformat()
            if len(champs[0]) != 10 or not champs[0][4:5] == '-' or not champs[0][7:8] == '-':
                raise ValueError()
            quantite = int(quantite_txt)
            prix = float(prix_txt)
            if not produit or quantite <= 0 or prix < 0 or prix != prix or prix == float('inf'):
                raise ValueError()
        except ValueError:
            raise ValueError(f"Ligne {numero} invalide") from None
        montant = quantite * prix
        if montant >= montant_minimum:
            yield {"date": jour, "produit": produit, "quantite": quantite, "prix_unitaire": prix, "montant": round(montant, 2)}

def resumer_flux(lignes, *, montant_minimum=0):
    nombre, total, par_produit = 0, 0, {}
    for vente in extraire_ventes(lignes, montant_minimum=montant_minimum):
        nombre += 1
        total += vente["montant"]
        produit = vente["produit"]
        par_produit[produit] = par_produit.get(produit, 0) + vente["montant"]
    return {"nombre_ventes": nombre, "total": round(total, 2), "par_produit": {k: round(v, 2) for k, v in par_produit.items()}}

if __name__ == "__main__":
    chemin = input("Chemin du CSV (Entrée = exemple intégré) : ").strip()
    seuil = float(input("Montant minimum [3000] : ") or 3000)
    if chemin:
        with open(chemin, encoding="utf-8") as fichier:
            rapport = resumer_flux(fichier, montant_minimum=seuil)
    else:
        exemple = ["date;produit;quantite;prix_unitaire", "2026-10-01;Stylo;2;1500", "2026-10-02;Cahier;1;4000", "2026-10-03;Stylo;1;2000"]
        rapport = resumer_flux(exemple, montant_minimum=seuil)
    print(json.dumps(rapport, ensure_ascii=False, indent=2))
    with open("resume_ventes.json", "w", encoding="utf-8") as fichier:
        json.dump(rapport, fichier, ensure_ascii=False, indent=2)
    print("Résumé enregistré dans resume_ventes.json")
