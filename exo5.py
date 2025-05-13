import numpy as np
import matplotlib.pyplot as plt

A = np.array([21.24, 25.49, 21.91, 22.1, 24.9, 25.1, 24.5, 23.6, 21.31, 21.5,
              21.4, 24.88, 22.7, 24.26, 22.65, 22.2, 21.8, 24.73, 23.8, 16.46,
              0.69, 51.0, 34.0, 22.9, 22.2, 24.6, 20.22, 23.4, 24.1, 22.0, 23.3,
              25.23, 25.02, 21.91, 25.2, 21.91, 24.26, 23.3, 24.0, 22.2, 24.5])

mean_temp = np.mean(A)
std_temp = np.std(A)

threshold = mean_temp + 2 * std_temp
peaks = np.where(A > threshold)[0]

plt.plot(A, label="Température")
plt.scatter(peaks, A[peaks], color='red', marker='*', label="Pics détectés")
plt.xlabel("Temps (h)")
plt.ylabel("Température (°C)")
plt.title("Mesure de température avec mise en évidence des discontinuïtés")
plt.legend()
plt.grid(True)
plt.show()