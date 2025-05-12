import numpy as np
import matplotlib.pyplot as plt

# Constants
k = 1.3806e-23  # Boltzmann constant in J/K
q = 1.602e-19  # Charge of an electron in C

# Function to calculate Id
def diode(Is, T, Vak):
    T_kelvin = T + 273.15  # Convert temperature to Kelvin
    Vt = k * T_kelvin / q  # Calculate thermal voltage
    Id = Is * (np.exp(Vak / Vt) - 1)  # Calculate the current Id
    return Id

# Vecteur tension Vak allant de -5V à 0.8V par pas de 0.01V
Vak = np.arange(-5, 0.81, 0.01)

# Paramètres pour la diode
Is = 100e-15  # Is = 100 fA
T = 25  # Température en °C

# Calcul de Id en appelant la fonction diode
Id = diode(Is, T, Vak)

# Affichage du résultat
plt.plot(Vak, Id)
plt.title('Caractéristique Tension-Courant d\'une diode')
plt.xlabel('Tension Vak (V)')
plt.ylabel('Courant Id (A)')
plt.grid(True)
plt.show()

