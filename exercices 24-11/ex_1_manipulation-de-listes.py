import random

# Exercice 1 - Manipulation de Listes
# Consignes : Créez une liste de nombres, ajoutez-y des éléments, puis triez-la.

print("\n---------------------------------------")  # Séparateur
print("   Tri de liste par ordre croissant")
print("---------------------------------------\n")  # Séparateur

# Crée une liste de 10 nombres aléatoires entre 1 et 100
maListe = [random.randint(1, 100) for _ in range(10)]

# Demande à l'utilisateur d'entrer un nombre entier et l'ajoute à la liste
maListe.append(int(input("Entrez un nombre entier : ")))

# Affiche la liste non triée
print("Voici la liste :", maListe)

# Trie la liste par ordre croissant
maListe.sort()

# Affiche la liste triée
print("La liste triée par ordre croissant :", maListe)
