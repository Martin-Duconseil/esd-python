# Exercice Facile 2 - Table de Multiplication
# Consignes : Écrivez un programme qui demande à l'utilisateur un nombre entier n, puis affiche la table de multiplication de ce nombre de 1 à 10.
# Sous forme de fonction 

# Définit la fonction table_de_multiplication

def table_de_multiplication():

    # Demande à l'utilisateur un nombre entier
    n = int(input("Entrez un nombre entier : "))  # L'utilisateur est invité à entrer un nombre entier et il est converti en entier (int)

    # Affiche l'en-tête de la table de multiplication
    
    print("\n---------------------------------------")  # Séparateur
    print("         Table de multiplication de", n)
    print("---------------------------------------\n")  # Séparateur

    # Calcule et affiche la table de multiplication de N de 1 à 10
    for compteur in range(1, 11):  # Utilise une boucle 'for' pour itérer à travers les nombres de 1 à 10 inclus
        print(n, "x", compteur, "=", n * compteur)  # Affiche chaque ligne de la table de multiplication de N de 1 à 10

# Appelle la fonction pour exécuter le code
table_de_multiplication()