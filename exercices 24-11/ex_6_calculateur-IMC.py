# Exercice 6 - Calculateur d'IMC
# Consignes : Écrivez une fonction qui calcule l'Indice de Masse Corporelle (IMC) à partir de la taille et du poids donnés.
# Il doit aussi interpéter l'IMC et afficher un message approprié, par exemple "Vous êtes en surpoids".

def calculer_imc(poids, taille_cm):
    # Conversion de la taille en mètres
    taille = taille_cm / 100

    # Calcul de l'IMC
    imc = poids / (taille ** 2)

    # Interprétation de l'IMC
    if imc < 18.5:
        message = "Vous êtes en insuffisance pondérale."
    elif imc < 25:
        message = "Votre poids est normal."
    elif imc < 30:
        message = "Vous êtes en surpoids."
    else:
        message = "Vous êtes en obésité."

    # Affichage du résultat
    print(f"Votre IMC est de {imc:.2f}. {message}")

print("\n-------------------------------")  # Séparateur
print("       Calculateur d'IMC") 
print("-------------------------------\n")  # Séparateur

# Utilisation de la fonction pour calculer l'IMC

poids = float(input("Entrez votre poids (kg) : "))  # Demande à l'utilisateur d'entrer son poids en kg
taille_cm = float(input("Entrez votre taille (cm) : "))  # Demande à l'utilisateur d'entrer sa taille en cm
calculer_imc(poids, taille_cm)  # Appelle la fonction pour calculer l'IMC
