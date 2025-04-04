import numpy as np

R = 1000 
C = 20e-9
w= 2*np.pi*50
Zc = 1/(1j)*w*C
Zeq1 = Zc + R
Zeq2= (Zc*R)/Zc + R

print(Zc)

A = np.array([R, Zc, Zeq1, Zeq2])
print(A)

print(np.real(R))
print(np.imag(R))
print(np.abs(Zc))
print(np.arg(Zc))