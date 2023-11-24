import json

# Exercice 4 - Gestionnaire de Contacts
# Consignes : Écrivez un programme qui stocke les noms et numéros de téléphone des contacts dans un dictionnaire.
# Il permet à l'utilisateur d'ajouter, supprimer, ou rechercher un contact.

contacts = {}  # Crée un dictionnaire vide pour stocker les contacts

def charger_contacts():
    try:
        with open("contacts.json", "r") as file:
            contacts.update(json.load(file))  # Charge les contacts depuis le fichier JSON et les ajoute au dictionnaire
    except FileNotFoundError:
        print("Le fichier contacts.json n'existe pas.\n")

def enregistrer_contacts():
    with open("contacts.json", "w") as file:
        json.dump(contacts, file)  # Enregistre les contacts dans le fichier JSON

def ajouter_contact(nom, numero):
    contacts[nom] = numero  # Ajoute le nom et le numéro de téléphone dans le dictionnaire des contacts
    print("\nContact ajouté avec succès!\n")
    enregistrer_contacts()  # Enregistre les contacts dans le fichier JSON après chaque ajout

def supprimer_contact(nom):
    if nom in contacts:  # Vérifie si le nom existe dans le dictionnaire des contacts
        del contacts[nom]  # Supprime le contact du dictionnaire
        print("\nContact supprimé avec succès!\n")
        enregistrer_contacts()  # Enregistre les contacts dans le fichier JSON après chaque suppression
    else:
        print("\nLe contact n'existe pas.\n")

def rechercher_contact(nom):
    nom = nom.lower()  # Convertit le nom en minuscules
    found_contacts = []
    for contact in contacts:
        if contact.lower() == nom:  # Vérifie si le nom du contact correspond (indépendamment de la casse)
            found_contacts.append(contact)  # Ajoute le contact trouvé à la liste des contacts trouvés
    if found_contacts:
        for contact in found_contacts:
            print(f"Nom: {contact} \nNuméro de téléphone: {contacts[contact]}\n")  # Affiche les informations du contact trouvé
    else:
        print("\nLe contact n'existe pas.\n")

print("\n---------------------------------------")  # Séparateur
print("       Gestionnaire de Contacts")
print("---------------------------------------\n")  # Séparateur

charger_contacts()  # Charge les contacts depuis le fichier JSON au démarrage du programme

while True:
    print("1. Ajouter un contact")          # Affiche l'option pour ajouter un contact
    print("2. Supprimer un contact")        # Affiche l'option pour supprimer un contact
    print("3. Rechercher un contact")       # Affiche l'option pour rechercher un contact
    print("4. Quitter\n")                   # Affiche l'option pour quitter le programme

    choix = input("Choisissez une option: ")  # Demande à l'utilisateur de choisir une option

    if choix == "1":
        nom = input("\nEntrez le nom du contact: ")
        numero = input("Entrez le numéro de téléphone du contact: ")
        ajouter_contact(nom, numero)  # Appelle la fonction pour ajouter un contact
    elif choix == "2":
        nom = input("Entrez le nom du contact à supprimer: ")
        supprimer_contact(nom)  # Appelle la fonction pour supprimer un contact
    elif choix == "3":
        nom = input("Entrez le nom du contact à rechercher: ")
        rechercher_contact(nom)  # Appelle la fonction pour rechercher un contact
    elif choix == "4":
        break  # Sort de la boucle while et termine le programme
    else:
        print("\nOption invalide. Veuillez réessayer.\n")
