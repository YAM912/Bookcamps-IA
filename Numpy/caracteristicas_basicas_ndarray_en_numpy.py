import numpy as np

#Creación de un ndarray 2D   
matriz = np.array([[1, 2, 3], [4, 5, 6]])
print(matriz)
#Acceso a un elemento específico (fila 1, columna 2)
elemento = matriz[1, 2]
print(elemento)

#Selección de una fila (fila 0)
fila = matriz[0, :]
print(fila)

#Selección de una columna (columna 1)
columna = matriz [:, 1]
print(columna)