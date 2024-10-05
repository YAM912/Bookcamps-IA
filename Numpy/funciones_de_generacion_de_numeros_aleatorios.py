# Generacion de numeros aleatorios
import numpy as np
# Genera numeros aleatorios entre 0 y 1 con distribucion uniforme
numeros_aleatorios_uniformes = np.random.rand(3)
# Genera numeros enteros aleatorios dentro de un rango especificado
numeros_aleatorios_enteros = np.random.randint(1, 10, size=5)
# Genera numeros aleatorios con una distribucion normal (gaussiana) con meia 0 y desviacion estandar 1
numeros_aleatorios_normales = np.random.randn(2, 2)
print("Numeros aleatorios uniformes:")
print(numeros_aleatorios_uniformes)
print("Numeros aleatorios enteros:")
print(numeros_aleatorios_enteros)
print("Numeros aleatorios normales:")
print(numeros_aleatorios_normales)

#Operaciones aritmeticas elemento por elemento

#Funciones Universales (ufuncs):
#NumPy proporciona funciones universales (ufuncs) que operan eficientemente en ndarrays
#Estas funciones realizan operaciones elemento por elemento y estan optimizadas para el rendimiento
#Ejemplos: np.sin(), np.cos(), np.exp(), etc

arr1 = np.array ([1, 2, 3])
arr2 = np.array ([4, 5, 6])

#Suma elemento por elemento
resultado = arr1 + arr2  # Salida [5, 7, 9]
print ("Resultado suma de elemento por elemento")
print (resultado)

# Multiplicacion por una constante
resultado2 = 2 * arr1 # Salida [2, 4, 6]
print ("Resultado multiplicacionn por constante")
print (resultado2)

#Operaciones matriciales
# Suma de matrices
arr3 = np.array ([[1, 2],[3, 4]])
arr4 = np.array ([[5, 6],[7, 8]])
resultado3 = arr3 + arr4  # Salida [[6, 8],[10, 12]]
print ("Resultado de suma de matrices")
print (resultado3)

#reshape(): Permite cambiar la forma (dimenciones) de un arreglo sin cambiar sus datos
arr5 = np.array ([1, 2, 3, 4, 5, 6])
reshape_arr5 = arr5.reshape((2, 3)) # Salida array ([[1, 2, 3],[4, 5, 6]])
print("Resultado reshape:")
print (reshape_arr5)

#sum(): Calcula la suma de los elementos a lo largo de un eje especifico o de todo el ndarray
Arr6 = np.array([[1, 2, 3],[4, 5, 6]])
total_suma = Arr6.sum() #Salida 21
print("Calculo")
print (total_suma)

# mean(): Calcula la media de los elmentos a lo largo de un eje especifico de todo el ndarray
Arr6 = np.array([[1, 2, 3],[4, 5, 6]])
average = Arr6.mean() #Salida 3.5
print ("Calculo de averange:")
print(average)

# min() y max(): Devuelve el valor minimo y maximo del ndarray a lo largo de un eje especifico
Arr6 = np.array([[1, 2, 3],[4, 5, 6]])
min_val = Arr6.min() #Salida min_val = 1
max_val = Arr6.max() #Salida max_val = 6
print ("Valor minimo y maximo respectivamente:")
print(min_val)
print (max_val)

# argmin() y arg max(): Devuelve los indices del valor minimo y maximo respectivamente
arr7 = np.array ([5, 2, 8, 1, 7])
idx_min = arr7.argmin() #Salida 3
idx_max = arr7.argmax() #Salida 2
print ("idex_min =")
print (idx_min)
print ("idex_max =")
print (idx_min)

#std(): Calcula la desviacion estandar de los elementos a lo largo de un eje espacifico o de todo el ndarray
arr8 = np.array([1, 2, 3, 4, 5])
std_dev = arr8.std() #Salida 1.414
print ("std_dev =")
print (std_dev)






