# Ejemplo real para prblemas de optimizacion

import numpy as np
from scipy.optimize import minimize

# Definir la funcion objetivo y las restricciones
def objetivo(x):
    return x[0]**2 + x[1]**2

constraints = ({"type": "ineq", "fun": lambda x: x[0]+ x[1] - 1})

#Resolver el problema de optimizacion
pregunta_inicial = [0.5, 0.5]
resultado = minimize(objetivo, pregunta_inicial, constraints=constraints)

# Imprimir resultado
print ("Solucion encontrada: ", resultado.x)


