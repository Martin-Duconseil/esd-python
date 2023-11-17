# Exercice Facile 1 - Somme des Nombres
# Consignes : Écrivez un programme qui demande à l'utilisateur un nombre entier n, puis calcule et affiche la somme des nombres de 1 à n.

def somme_des_nombres():
    print("\n---------------------------------------")  # Séparateur
    print("         Somme des nombres")
    print("---------------------------------------\n")  # Séparateur

    # Demande à l'utilisateur un nombre entier
    n = int(input("Entrez un nombre entier : "))  # L'utilisateur est invité à entrer un nombre entier et il est converti en entier (int)

    somme = 0  # Initialise la variable 'somme' à zéro pour stocker la somme des nombres de 1 à n

    # Calcule la somme des nombres de 1 à n
    for compteur in range(1, n + 1):  # Utilise une boucle 'for' pour itérer à travers les nombres de 1 à n inclus
        somme += compteur  # Ajoute chaque nombre à la variable 'somme'

    # Affiche le résultat
    print("\nLa somme des nombres de 1 à", n, "est", somme)  # Affiche le résultat de la somme des nombres de 1 à n

# Appel de la fonction
somme_des_nombres()