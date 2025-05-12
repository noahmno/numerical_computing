import numpy as np 
import matplotlib.pyplot as plt
matrix1= np.array([[1,7,3],[8,5,2],[7,4,9]])
print(matrix1 )

inverse_matrix = np.linalg.inv(matrix1)
print("l'inverse de la matrice est ",
       inverse_matrix)
print(np.linalg.det(matrix1))
print(np.linalg.eig(matrix1))
matrix2 = matrix1 * matrix1
matrix3 = matrix1**2
print(matrix1[2,1])
sous_matrix= matrix1[1:2,0:1]
