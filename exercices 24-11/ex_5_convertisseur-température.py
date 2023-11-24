# Exercice 5 - Convertisseur Température
# Consignes : Créez une fonction qui convertit les températures entre Celsius et Fahrenheit.

print("\n---------------------------------------")  # Séparateur
print("     Convertisseur de Température")
print("---------------------------------------\n")  # Séparateur

# Définition de la fonction pour convertir les températures
def convertir_temperature():
    # Demande à l'utilisateur s'il veut convertir de Celsius à Fahrenheit (C) ou de Fahrenheit à Celsius (F)
    choix = input("Voulez-vous convertir de Celsius à Fahrenheit (C) ou de Fahrenheit à Celsius (F): ").upper()

    # Si l'utilisateur choisit Celsius (C)
    if choix == "C":
        # Demande la température en Celsius
        celsius = float(input("\nEntrez la température en Celsius : "))
        # Convertit la température de Celsius à Fahrenheit
        fahrenheit = (celsius * 9/5) + 32
        # Affiche le résultat de la conversion
        print(f"\n{celsius} degrés Celsius équivalent à {fahrenheit} degrés Fahrenheit.")

    # Si l'utilisateur choisit Fahrenheit (F)
    elif choix == "F":
        # Demande la température en Fahrenheit
        fahrenheit = float(input("\nEntrez la température en Fahrenheit : "))
        # Convertit la température de Fahrenheit à Celsius
        celsius = (fahrenheit - 32) * 5/9
        # Affiche le résultat de la conversion
        print(f"\n{fahrenheit} degrés Fahrenheit équivalent à {celsius} degrés Celsius.")

    # Si l'utilisateur fait un choix invalide
    else:
        # Affiche un message d'erreur
        print("Choix invalide. Veuillez entrer 'C' pour Celsius ou 'F' pour Fahrenheit.")

# Appel de la fonction pour convertir les températures
convertir_temperature()

