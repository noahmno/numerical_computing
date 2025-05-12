import numpy as np
import matplotlib.pyplot as plt

# On commence par définir les données du vecteur numérique y et le nombre total de mesures
y_values = [93, 191, 234, 246, 213, 169, 141, 82, 37, 51, 87, 103, 191, 230, 180, 255, 156, 186, 143, 41, 77, 35, 25, 102, 130, 192, 163, 205, 185, 200, 113, 104, 29, 1, 33, 99, 155, 183, 219, 202, 224, 136, 129, 130, 40, 36, 76, 58, 135]

# On crée un vecteur temps en millisecondes (en supposant un pas de 1 ms entre chaque mesure)
time = np.arange(len(y_values))

# Conversion du signal y (valeur numérique) en volts
voltage = np.array(y_values) * 5 / 255

# Affichage du signal en volts avec l'échelle temporelle correcte
plt.plot(time, voltage)
plt.title("Représentation graphique du signal converti en volts")
plt.xlabel("Temps (ms)")
plt.ylabel("Tension (V)")
plt.grid(True)
plt.show()