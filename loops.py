
# Consignes : 
# Mettre dans ‘esd-python’ un fichier “loops.py” dans lequel :
#    - Vous écrirez une fonction “multiplie” qui multiplie deux nombres en paramètre par additions successives.
#    - Faire aussi une fonction “puissance” qui calcule les puissances par multiplication successives.

import time

def multiplie(a, b):

    # Multiplie deux nombres par additions successives.
    
    # :param a: Premier nombre
    # :param b: Deuxième nombre
    # :return: Résultat de la multiplication

    resultat = 0
    for _ in range(b):
        resultat += a
    return resultat

def puissance(base, exposant):

    # Calcule les puissances par multiplication successives.
    
    # :param base: Base de la puissance
    # :param exposant: Exposant de la puissance
    # :return: Résultat de la puissance

    resultat = 1
    for _ in range(exposant):
        resultat = multiplie(resultat, base)
    return resultat

# Utilisation de la fonction multiplie

print("\n-----------------------------------------------") # Séparateur
print("     Utilisation de la fonction multiplie")
print("-----------------------------------------------\n") # Séparateur

a = int(input("Entrez le premier nombre : "))
b = int(input("Entrez le second nombre : "))

resultat_multiplication = multiplie(a, b)
print(f"\n{a} * {b} = {resultat_multiplication}\n")
print("Le résultat de", a,"fois", b, "est", resultat_multiplication, "\n")

time.sleep(1) # Pause d'une seconde

# Utilisation de la fonction puissance

print("\n-----------------------------------------------") # Séparateur
print("     Utilisation de la fonction puissance")
print("-----------------------------------------------\n") # Séparateur

base_puissance = int(input("Entrez la base de la puissance : "))
exposant_puissance = int(input("Entrez l'exposant de la puissance : "))

resultat_puissance = puissance(base_puissance, exposant_puissance)
print(f"\n{base_puissance}^{exposant_puissance} = {resultat_puissance}\n")
print("Le résultat de", base_puissance,"exposant", exposant_puissance, "est", resultat_puissance, "\n")
