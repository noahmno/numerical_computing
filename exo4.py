import numpy as np
import matplotlib.pyplot as plt

# 1. Générer une matrice aléatoire de températures
np.random.seed(42)  # Pour la reproductibilité
n_years = 10  # Nombre d'années (de 2011 à 2020)
n_days = 365  # Nombre de jours dans une année
T_min, T_max = -10, 35  # Températures minimales et maximales (en °C)

# Génération des températures pour chaque jour de chaque année
T = np.random.rand(n_years, n_days) * (T_max - T_min) + T_min

# 2. Calcul du vecteur de températures moyennes pour chaque jour
T_avg = np.mean(T, axis=0)  # Moyenne sur les années (pour chaque jour)

# 3. Tracer le nuage de points avec les températures moyennes
days = np.arange(1, n_days + 1)
plt.scatter(days, T_avg, label='Températures moyennes', color='green', s=10)

# 4. Régression linéaire
p_lin = np.polyfit(days, T_avg, 1)  # Régression linéaire
T_lin = np.polyval(p_lin, days)  # Calculer les valeurs de la régression linéaire
plt.plot(days, T_lin, label='Régression linéaire', color='blue')

# 5. Régression cubique
p_cub = np.polyfit(days, T_avg, 3)  # Régression cubique
T_cub = np.polyval(p_cub, days)  # Calculer les valeurs de la régression cubique
plt.plot(days, T_cub, label='Régression cubique', color='red')

# 6. Interpolation
T_interp = np.interp(days, days, T_avg)  # Interpolation linéaire
plt.plot(days, T_interp, label='Interpolation', color='purple', linestyle='--')

# 7. Affichage des résultats
plt.title("Températures moyennes et régressions")
plt.xlabel("Jour de l'année")
plt.ylabel("Température (°C)")
plt.legend()
plt.grid(True)
plt.show()
