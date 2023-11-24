import random

# Exercice 7 - Tri de Liste
# Consignes : Écrivez une fonction qui prend une liste de nombres et retourne une liste triée sans utiliser la méthode .sort().

# Crée une liste de 10 nombres aléatoires entre 1 et 100

liste = [random.randint(1, 100) for _ in range(10)]

print("\n----------------------------")  # Séparateur
print("       Tri de liste") 
print("----------------------------\n")  # Séparateur

# Demande à l'utilisateur d'entrer un nombre entier et l'ajoute à la liste

liste.append(int(input("Entrez un nombre entier : ")))

# Affiche la liste non triée

print("\nVoici la liste non triée :", liste,"\n")

# Définition de la fonction pour trier la liste

def trier_liste(liste):
    # Crée une liste vide pour stocker les nombres triés
    liste_triee = []

    # Tant que la liste n'est pas vide
    while liste:
        # Définit le nombre minimum comme étant le premier élément de la liste
        min = liste[0]

        # Pour chaque élément de la liste
        for x in liste:
            # Si l'élément est plus petit que le nombre minimum
            if x < min:
                # Définit le nombre minimum comme étant l'élément
                min = x

        # Ajoute le nombre minimum à la liste triée
        liste_triee.append(min)

        # Supprime le nombre minimum de la liste
        liste.remove(min)

    # Retourne la liste triée
    return liste_triee

# Affiche la liste triée

print("Voici la liste triée :", trier_liste(liste),"\n")