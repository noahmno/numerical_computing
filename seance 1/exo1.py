import numpy as np

R = 1000 
C = 20e-9
w= 2*np.pi*50
Zc = 1/(1j)*w*C
Zeq1 = Zc + R
Zeq2= (Zc*R)/Zc + R

print(Zc)

Z = np.array([R, Zc, Zeq1, Zeq2])
Z_conj= np.conj(Z)
print(Z)



print(np.abs(Zc))

print(np.real(Z))
print(np.imag(Z))
print(np.angle(Z))
print(Z_conj)
print(Zeq2)