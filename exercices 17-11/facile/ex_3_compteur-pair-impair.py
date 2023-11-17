# Exercice Facile 3 - Compteur Pair Impair
# Consignes : Écrivez un programme qui utilise une boucle pour afficher les nombres de 1 à 10 et indique si chaque nombre est pair ou impair.

# Définition de la fonction pour vérifier si un nombre est pair ou impair
def verifier_pair_impair():
    # Utilisation d'une boucle for pour itérer de 1 à 10
    for nombre in range(1, 11):
        # Vérifier si le nombre est pair ou impair
        if nombre % 2 == 0:
            print(nombre, "est un nombre pair.")
        else:
            print(nombre, "est un nombre impair.")

# Appel de la fonction pour exécuter le code
verifier_pair_impair()