from functools import wraps

def compter_appels(fonction):
    @wraps(fonction)
    def enveloppe(*args, **kwargs):
        enveloppe.nb_appels += 1
        return fonction(*args, **kwargs)
    enveloppe.nb_appels = 0
    return enveloppe

def fabriquer_tarificateur(remise_pct, tva_pct=16):
    if not 0 <= remise_pct <= 100 or not 0 <= tva_pct <= 100:
        raise ValueError("Taux hors de [0, 100]")
    @compter_appels
    def tarifer(prix_ht):
        if prix_ht < 0:
            raise ValueError("Prix négatif")
        return round(prix_ht * (1 - remise_pct / 100) * (1 + tva_pct / 100), 2)
    return tarifer

if __name__ == "__main__":
    remise = float(input("Remise (%) : "))
    tva = float(input("TVA (%) [16] : ") or 16)
    tarif = fabriquer_tarificateur(remise, tva)
    prix = float(input("Prix HT : "))
    print("Prix TTC :", tarif(prix))
    print("Nombre d'appels :", tarif.nb_appels)
    autre = fabriquer_tarificateur(remise, tva)
    print("Compteur indépendant du second tarificateur :", autre.nb_appels)
