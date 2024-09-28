import numpy as np
numeros = [1, 2, 3, 4, 5] #Lista de números
ndarray_numeros = np.array(numeros) #Creación de un ndarray a partir de la lista
print(ndarray_numeros)
matriz_ceros = np.zeros((2, 3))#Creación de un ndarray a partir de 2x3 con ceros
matriz_unos = np.ones((3, 3))#Creación de un ndarray de 3x3 con unos
matriz_personalizada = np.array([[1, 2, 3], [4, 5, 6]]) #Creación de un ndarray con valores específicos

print(matriz_ceros)
print(matriz_unos)
print(matriz_personalizada)