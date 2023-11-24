# Exercice 2 - Gestion d'un Dictionnaire
# Consignes : Créez un dictionnaire représentant une personne, incluant des informations telles que le nom, l'âge, et l'adresse.

monDictionnaire = {"nom": "John Doe", "age": 42, "adresse": "1 rue du Python"}
nom = monDictionnaire["nom"] # Récupère la valeur de la clé "nom"
age = monDictionnaire["age"] # Récupère la valeur de la clé "age"
adresse = monDictionnaire["adresse"] # Récupère la valeur de la clé "adresse"

print("\n---------------------------------------")  # Séparateur
print("   Fiche d'identité d'une personne")
print("---------------------------------------\n")  # Séparateur

# Affiche les informations de la personne

print("Nom :", nom)
print("Age :", age, "ans")
print("Adresse :", adresse)
