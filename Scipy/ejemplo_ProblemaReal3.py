# Ejemplo rel para el analisis de datos

import numpy as np
import pandas as pd
from scipy.stats import pearsonr

# Cargar datos de ejemplo
data = pd.read_csv ("datos.csv")

# Calcular el coeficiente de correlacion de Pearson entre dos variables
coeficiente_de_corelacion, p_value = pearsonr(data["varieble1"], data["variable2"])

# Calcular el coeficiente de correlacion
print ("Coeficiente de correlacion de Pearson: ", coeficiente_de_corelacion)

# Imprimir el coeficiente de correlacion
print ("Coeficiente de correlacion de Pearson: ", coeficiente_de_corelacion)

