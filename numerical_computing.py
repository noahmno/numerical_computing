import numpy as np

R = 1000
C = 20*10**(-9)
w= 2*np.pi*50
Zc = 1/(1j)*w*C

print(Zc)
