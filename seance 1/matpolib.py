import matplotlib.pyplot as plt
import numpy as np

# Créer les données
x = np.arange(-np.pi, np.pi, 0.1)
y = np.sin(x)

# Tracer la fonction
plt.plot(x, y, label="sin(x)")

# Ajouter le titre et les légendes
plt.title("sin(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.text(1, 0, "Hello World!")

# Ajouter la légende
plt.legend()

# Afficher le graphique
plt.show()
