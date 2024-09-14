a = 5
b = 8
c = a + b
print (c)
nombre = "Yamid"
nombre = "Yamid Usuario"
#Concluimos que las variables son modificables y toman el ultimo valor
print (nombre)

numero = 10
numero = 10 + 1 # Le sumamaos 1 a la variable numero
numero += 1 # De esta forma le estamos sumando 1 a la variable numero, que tenia el valor de 11
print (numero)

numero = 10
numero += 5 # De esta forma le estamos sumando 1 a la variable numero
print (numero)

numero = 10
numero -= 5 # De esta forma le estamos restando 1 a la variable numero
print (numero)

bienvenida = "Hola " + nombre + " feliz noche"  # De esta forma concatenamos texto con valores almacenados en variables
print (bienvenida)

bienvenida = f"Hola  {nombre}  feliz noche" # Otra forma de concatenar donde todo el contenio esta entre comillas despues de una f y se conoce como f print
print (bienvenida)

#del bienvenida # Borra la variable bienvenida, es decir que ya no esta declarada
#print (bienvenida)

nmbre = True
bienvenida = f" Hola {nombre} feliz noche"
print ("ola" in bienvenida) # recorre la variable para verificar si existe la cadena de texto ola

print ("bety" not in bienvenida)
print ("ola" not in bienvenida)

nombreCompletoTuProfe = "Jheyson Galvis" # Camelcase sirve para definir variables
nomombre_completo_de_tu_profe = "Jheyson Galvis" # Snake, es el recomendado en Phyton segun la recomendacion
print (nomombre_completo_de_tu_profe)
