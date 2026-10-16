def calculer_livraison(montant_panier, distance_km, premium=False):
    if montant_panier < 0 or distance_km < 0:
        raise ValueError("Montant et distance doivent être positifs ou nuls")
    if montant_panier >= 100000:
        frais = 0
    elif distance_km <= 5:
        frais = 2000
    elif distance_km <= 20:
        frais = 5000
    else:
        frais = 9000
    if premium and frais:
        frais /= 2
    return {"frais": frais, "total": montant_panier + frais}

if __name__ == "__main__":
    montant = float(input("Montant du panier (CDF) : "))
    distance = float(input("Distance (km) : "))
    premium = input("Premium ? (oui/non) : ").strip().lower() == "oui"
    print(calculer_livraison(montant, distance, premium))
    print("\nTests des frontières :")
    for panier, km, attendu in [(50000, 0, 2000), (50000, 5, 2000), (50000, 5.01, 5000), (50000, 20, 5000), (50000, 20.01, 9000), (100000, 25, 0)]:
        obtenu = calculer_livraison(panier, km)["frais"]
        print(f"Panier={panier}, distance={km} : {'OK' if obtenu == attendu else 'ÉCHEC'} ({obtenu} CDF)")
