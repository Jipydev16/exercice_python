
def calculer_ticket(prix_unitaire, quantite, remise_pct, tva_pct=16):

    if type(prix_unitaire) not in (int, float) or not 0 <= prix_unitaire < float("inf"):
        raise ValueError("Le prix doit être un nombre positif ou nul.")

    if type(quantite) is not int or quantite < 1:
        raise ValueError("La quantité doit être un entier supérieur ou égal à 1.")

    if type(remise_pct) not in (int, float) or not 0 <= remise_pct <= 100:
        raise ValueError("La remise doit être comprise entre 0 et 100.")

    if type(tva_pct) not in (int, float) or not 0 <= tva_pct <= 100:
        raise ValueError("La TVA doit être comprise entre 0 et 100.")

    sous_total = prix_unitaire * quantite

    remise = sous_total * remise_pct / 100

    montant_ht = sous_total - remise

    tva = montant_ht * tva_pct / 100

    total_ttc = montant_ht + tva

    return {
        "sous_total": round(sous_total, 2),
        "remise": round(remise, 2),
        "montant_ht": round(montant_ht, 2),
        "tva": round(tva, 2),
        "total_ttc": round(total_ttc, 2)
    }


print("===== BIENVENUE DANS NOTRE BOUTIQUE =====")

try:
    prix = float(input("Prix unitaire (CDF) : "))

    quantite = int(input("Quantité : "))

    remise_pct = float(input("Remise (%) : "))

    saisie_tva = input("TVA (%) [Entrée = 16] : ").strip()

    if saisie_tva == "":
        tva_pct = 16
    else:
        tva_pct = float(saisie_tva)

    ticket = calculer_ticket(
        prix,
        quantite,
        remise_pct,
        tva_pct
    )
    

    print("\n======================================")
    print("            TICKET DE CAISSE")
    print("======================================")

    print(f"Prix unitaire :    {prix:.2f} CDF")
    print(f"Quantité :         {quantite}")
    print(f"Remise appliquée : {remise_pct}%")
    print(f"TVA appliquée :    {tva_pct}%")

    print("--------------------------------------")

    print(f"Sous-total :       {ticket['sous_total']:.2f} CDF")
    print(f"Remise :           {ticket['remise']:.2f} CDF")
    print(f"Montant HT :       {ticket['montant_ht']:.2f} CDF")
    print(f"TVA :              {ticket['tva']:.2f} CDF")

    print("--------------------------------------")

    print(f"TOTAL TTC :        {ticket['total_ttc']:.2f} CDF")

    print("======================================")
    print("         MERCI POUR VOTRE ACHAT !")
    print("======================================")

except ValueError as erreur:
    print("\nERREUR :", erreur)
