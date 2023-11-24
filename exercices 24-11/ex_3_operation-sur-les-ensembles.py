# Exercice 3 - Opérations sur les Ensembles
# Consignes : Définissez deux ensembles et effectuez des opérations comme l'union et l'intersection.

# Définir deux ensembles
ensemble1 = {1, 2, 3, 4, 5}
ensemble2 = {4, 5, 6, 7, 8}

# Effectuer l'union des ensembles
union = ensemble1.union(ensemble2)

print("\n-------------------------------------")  # Séparateur
print("         Union des ensembles")
print("-------------------------------------\n")  # Séparateur

print("Union:", union)

# Effectuer l'intersection des ensembles
intersection = ensemble1.intersection(ensemble2)

print("\n---------------------------------------")  # Séparateur
print("      Intersection des ensembles")
print("---------------------------------------\n")  # Séparateur

print("Intersection:", intersection)

