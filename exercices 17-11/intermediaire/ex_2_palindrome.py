# Exercice Intermédiaire 2 - Palindrome
# Consignes : Écrivez un programme qui vérifie si un mot saisi par l'utilisateur est un palindrome (se lit de la même manière de gauche à droite et de droite à gauche).

# Création de la fonction palindrome

def palindrome(mot):
    # Convertir le mot en minuscules pour ignorer la casse
    mot = mot.lower()

    # Supprimer les espaces blancs du mot
    mot = mot.replace(" ", "")

    # Utiliser une boucle for pour comparer les caractères de gauche à droite et de droite à gauche
    for compteur in range(len(mot) // 2):
        # Comparer le caractère de gauche avec celui de droite
        if mot[compteur] != mot[len(mot) - compteur - 1]:
            # Si les caractères ne correspondent pas, le mot n'est pas un palindrome
            return False

    # Si la boucle se termine sans retourner False, le mot est un palindrome
    return True

print("\n-----------------------------------------------")  # Séparateur
print("     Utilisation de la fonction palindrome")
print("-----------------------------------------------\n")  # Séparateur

# Demander à l'utilisateur de saisir un mot
mot = input("Entrez un mot : ")

# Appeler la fonction palindrome et afficher le résultat
if  palindrome(mot):
    print("\nLe mot : ",mot," est un palindrome.")
else:
    print("\nLe mot : ",mot," n'est pas un palindrome.")

