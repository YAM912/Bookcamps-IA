# Operadores numericos
a = 10
b = 3
c = 0
print (a > b)
print (a < b)
print (a >= b)
print (a <= b)
print (a == b)
print (a != b)
print ("Suma: ", a + b)
print ("Resta: ", a - b)
print ("Multiplicacion: ", a * b)
print ("Division: ", a / b)

print("modulo: ", a % b) # En Phyton el operador de modulo (%) se utiliza para obtener el residuo de una division entre dos numeros
print("Division entera: ", a // b) # El signo doble division (//) entrega como resultado la parte entera
print ("Potenciacion: ", a ** b) # Potencicion (a elevado a la b)
print ("Potenciacion: ", b ** a) # Potencicion (b elevado a la a)

a += 2  #Otra forma de sumarle dos a la variable, normalmente a = a + 2 o de esta forma puede ser mejor
print(a)


print ("Suma: ", a + c)
print ("Resta: ", a - c)
print ("Multiplicacion: ", a * c)
#print ("Division: ", a / c) # Error de division por cero

operacion1 = 2 + 3 + 4
operacion2 = 2 + (3 * 4)
print (operacion1)
print (operacion2)

operacion3 = 2 + 3 * 4
operacion4 = (2 + 3) * 4
print (operacion3)
print (operacion4)

operacion5 = (2 + 3) * (4**2) / 8 - 1
print (operacion5)



