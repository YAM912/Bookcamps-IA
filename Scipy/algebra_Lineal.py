import numpy as np
import scipy.linalg as la

# Coeficientes de la ecuaciones lineales
A = np.array([[2, 1], [1, 1]])
b = np.array([4, 3])

# Resolver el sistema de ecuaciones lineales
x = la.solve (A, b)

# Imprimir la solucion
print("Solucion del sistema de ecuaciones lineales: ", x)


