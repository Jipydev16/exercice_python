def analyser_arbre(racine):
    noms, feuilles = [], []
    def visiter(noeud, profondeur):
        if not isinstance(noeud, dict):
            raise ValueError("Nœud invalide")
        nom, montant, enfants = noeud.get("nom"), noeud.get("montant"), noeud.get("enfants")
        if not isinstance(nom, str) or not nom.strip() or isinstance(montant, bool) or not isinstance(montant, (int, float)) or montant < 0 or not isinstance(enfants, list):
            raise ValueError("Nœud invalide")
        noms.append(nom)
        total, nombre, maximum = montant, 1, profondeur
        if not enfants:
            feuilles.append(nom)
        for enfant in enfants:
            t, n, p = visiter(enfant, profondeur + 1)
            total += t
            nombre += n
            maximum = max(maximum, p)
        return total, nombre, maximum
    total, nombre, profondeur = visiter(racine, 1)
    return {"total": total, "noms": noms, "nombre_noeuds": nombre, "profondeur_max": profondeur, "feuilles": feuilles}

if __name__ == "__main__":
    arbre = {"nom": "Boutique", "montant": 100, "enfants": [{"nom": "Papeterie", "montant": 50, "enfants": [{"nom": "Stylos", "montant": 20, "enfants": []}]}, {"nom": "Informatique", "montant": 200, "enfants": []}]}
    print(analyser_arbre(arbre))
