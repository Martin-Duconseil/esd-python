# Exercice Intermédiaire 3 - Carré Magique
# Consignes : Créez un programme qui génère et affiche un carré magique d'ordre n (n est un nombre impair) en utilisant une boucle.
# La constante magique d'un carré magique normal dépend uniquement de n et vaut : n(n2 + 1)/2.

def generer_carre_magique(ordre):
    # Vérifier que l'ordre est impair
    if ordre % 2 == 0:
        print("Veuillez fournir un nombre impair pour l'ordre du carré magique.")
        return

    # Initialiser le carré magique avec des zéros
    carre_magique = [[0] * ordre for _ in range(ordre)]

    # Position initiale
    ligne, colonne = 0, ordre // 2

    # Remplir le carré magique
    for num in range(1, ordre**2 + 1):
        carre_magique[ligne][colonne] = num

        # Trouver la nouvelle position
        ligne -= 1
        colonne += 1

        # Vérifier les bords
        if ligne < 0:
            ligne = ordre - 1
        if colonne == ordre:
            colonne = 0

        # Vérifier si la case est déjà occupée
        if carre_magique[ligne][colonne] != 0:
            ligne += 2
            colonne -= 1

            # Vérifier les bords après ajustement
            if ligne >= ordre:
                ligne -= ordre

    # Afficher le carré magique
    print("Carré magique d'ordre", ordre, ":")
    for ligne in carre_magique:
        print(ligne)

# Demander à l'utilisateur de saisir un nombre impair pour l'ordre du carré magique
ordre_utilisateur = int(input("Veuillez entrer un nombre impair pour l'ordre du carré magique : "))

# Générer et afficher le carré magique
generer_carre_magique(ordre_utilisateur)