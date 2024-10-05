# Metodos para la manipulacion de ndarray
import numpy as np
arr= np.array([1, 2, 3])
print (np.sum(arr))

array = np.array ([[1, 2, 3],[4, 5, 6]])
print ("Array original: ")
print (array)
# Reshape(): Permite cambiar la forma de un array sin cambiar sus datos
reshape_array = array.reshape(3, 2) 
print ("Array reshape: ")
print (reshape_array)
# Flaten(): Convierte un array multidimencional en un array unidimencional
flaten_array = array.flatten()
print("Array Flaten: ")
print(flaten_array)
# Transpose(): Permite cambiar el orden de las dimenciones de un array
transpose_array = array.transpose()
print("Array transpose: ")
print (transpose_array)