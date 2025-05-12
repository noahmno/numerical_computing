import numpy as np

exo1 = np.array([38, 24, 32, 45, 40])  # Temps pour l'exercice 1
exo2 = np.array([23, 25, 31, 29, 15])  # Temps pour l'exercice 2
exo3 = np.array([26, 34, 30, 28, 37])  # Temps pour l'exercice 3

# Calcul du temps total pour chaque étudiant
temps_total = exo1 + exo2 + exo3

# Affichage des résultats
#for i, temps in enumerate(temps_total, start=1):
#   print(f"Étudiant {i}: {temps} minutes")


temps_examen = np.array([105])

temps_restant = temps_examen - temps_total

#for i, temps in enumerate(temps_restant,start=1):
#    print(f"il reste {temps} minutes pour l'etudiant {i} ")


cotes= np.array([15, 8, 13 ,16, 10])

best_produit = temps_restant * cotes 
for i,cote in enumerate(best_produit, start = 1):
   print(f"l'etudiant {i} a un ratio de {cote}")


K = np.array([exo1[0], exo1[2],exo2[1],exo2[2]])
print(K)