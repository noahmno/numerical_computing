import numpy as np

def solve_circuit(Ug, fg, R1, R2, C, L):
    # Fréquence en rad/s
    omega = 2 * np.pi * fg
    
    # Matrice des coefficients pour le système d'équations
    A = np.array([[R1, 1/(1j * omega * C), 0],
                  [0, -1/(1j * omega * C), R2 + 1j * omega * L],
                  [1, -1, -1]])
    
    # Vecteur des résultats
    B = np.array([Ug, 0, 0])
    
    # Résolution du système d'équations
    currents = np.linalg.solve(A, B)
    
    # Retourner les courants I1, I2, I3
    return currents[0], currents[1], currents[2]

# Paramètres du circuit
Ug = 230  # Tension de la source en V
fg = 50   # Fréquence en Hz
R1 = 10   # Résistance R1 en Ohms
R2 = 10   # Résistance R2 en Ohms
C = 10e-6 # Capacité en Farads
L = 100e-3 # Inductance en Henries

# Appel de la fonction
I1, I2, I3 = solve_circuit(Ug, fg, R1, R2, C, L)

print(f"Courant I1: {I1}")
print(f"Courant I2: {I2}")
print(f"Courant I3: {I3}")