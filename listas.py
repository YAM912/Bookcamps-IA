lista = ["Numpy",
         "Pandas",
         "Scikit-learn",
         "TensorFlow",
         "Keras"
]
print (lista)

numbers = [1, 2, 3, 4]
print (numbers)
print (type (numbers))
mix = ["uno", 2, 3.14, True, [1, 2, 3]]
print (mix)
print(len(mix))
print ("Imprimir el primer elemento de la lista mix: ", mix[0])
print ("Imprimir el segundo elemento de la lista mix: ", mix[1])
print ("Imprimir el primer elemento de la lista mix: ", mix[-1])

string = "Numpy"
print ("Primer elemento: ", string[0])
print ("Primer elemento: ", string[1])
print ("Primer elemento: ", string[-1])

print (mix[0:2]) #Imprime de la lista mix desde la posicion 0 hasta la 2
print (mix[:2]) #Otra forma
print (mix[2:]) #Imprime del la posiscion 2 hacia adelante
print (mix[2:-2]) #Imprime de la posiscion 2 hasta el penultimo elmento

mix.append (["Romulo", "Nancy"]) #Inserta este elemento al final de la lista
mix.insert(0, "Jheyson Galvis") #Inserta este elemento en la primera posicion de la lista
print (mix)
print(mix.index("Jheyson Galvis")) #Indica la posiscion en la lista de el lelemnto "Jheyson Galvis"

print (numbers)
print (type (numbers))
print("mayor: ", max(numbers))
print("menor: ", min(numbers))
print (numbers)
del numbers [-1] #Elimina el ultimo elemento
print (numbers)
del numbers # Elimina la lista
# print (numbers) # No puede imprimir algo que no existe, dado que se elimino




