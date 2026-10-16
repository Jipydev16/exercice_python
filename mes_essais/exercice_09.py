def appliquer_mouvements(stock_initial, mouvements):
    stock = stock_initial.copy()
    for produit, quantite in stock.items():
        if not isinstance(produit, str) or not produit.strip() or type(quantite) is not int or quantite < 0:
            raise ValueError("Stock initial invalide")
    for mouvement in mouvements:
        if not isinstance(mouvement, dict):
            raise ValueError("Mouvement invalide")
        produit = mouvement.get("produit")
        type_mouvement = mouvement.get("type")
        quantite = mouvement.get("quantite")
        if not isinstance(produit, str) or not produit.strip() or type(quantite) is not int or quantite <= 0 or type_mouvement not in ("entree", "sortie"):
            raise ValueError("Mouvement invalide")
        if type_mouvement == "entree":
            stock[produit] = stock.get(produit, 0) + quantite
        else:
            if quantite > stock.get(produit, 0):
                raise ValueError("Stock insuffisant pour " + produit)
            stock[produit] -= quantite
    return stock

def journal_mouvements(stock_initial, mouvements):
    journal = []
    for i in range(len(mouvements)):
        journal.append(appliquer_mouvements(stock_initial, mouvements[:i+1]))
    appliquer_mouvements(stock_initial, mouvements)  # Validation intégrale avant exposition
    return journal

if __name__ == "__main__":
    stock = {"Stylo": 10, "Cahier": 4}
    mouvements = [{"produit": "Stylo", "type": "sortie", "quantite": 3}, {"produit": "Classeur", "type": "entree", "quantite": 2}]
    print("Stock initial :", stock)
    print("Stock final :", appliquer_mouvements(stock, mouvements))
    print("Journal :", journal_mouvements(stock, mouvements))
