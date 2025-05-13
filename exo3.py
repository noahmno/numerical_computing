import numpy as np
import matplotlib.pyplot as plt

# Paramètres du plan
tx = 1  # Translation en x
ty = 4 # Translation en y

# Création de l'octogone
t = np.linspace(1/16, 15/16, 8) * 2 * np.pi  # 8 points pour l'octogone
x = np.cos(t)  # Coordonnées x de l'octogone
y = np.sin(t)  # Coordonnées y de l'octogone

# Affichage de l'octogone original (vert)
plt.fill(x, y, 'g', label='Octogone original')

# Application de la translation (Tx, Ty)
x_translated = x + tx
y_translated = y + ty

# Affichage de l'octogone traduit (rouge)
plt.fill(x_translated, y_translated, 'r', label='Octogone traduit')



plt.show()