# Exercice Intermédiaire 1 - Factorielle
# Consignes : Écrivez un programme qui demande à l'utilisateur un nombre entier n, puis calcule et affiche la factorielle de n en utilisant une boucle.

# Création de la fonction factorielle

# Définition de la fonction factorielle avec un paramètre n
def factorielle(n):

    # Si n est égal à 0 ou 1, la factorielle est toujours 1
    if n == 0 or n == 1:
        return 1
    
    else:
        # Initialisation de la variable résultat à 1
        resultat = 1

        # Utilisation d'une boucle for pour multiplier les nombres de 2 à n inclus
        for i in range(2, n + 1):
            resultat *= i  # Multiplier le résultat par chaque nombre de la séquence
        
        # Retourner le résultat de la factorielle
        return resultat

# Utilisation de la fonction factorielle

print("\n-----------------------------------------------")  # Séparateur
print("     Utilisation de la fonction factorielle")
print("-----------------------------------------------\n")  # Séparateur

# Demande à l'utilisateur un nombre entier
n = int(input("Entrez un nombre entier : "))

# Affiche la factorielle de n
print("\nFactorielle de", n, ":", factorielle(n), "\n")

# Appel de la fonction pour exécuter le code
factorielle()