import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

# Datos de ejemplo (función seno)
x = np.linspace(0, 2 * np.pi, 10)
y = np.sin(x)

# Interpolación lineal
f = interp1d(x, y)

# Nuevo conjunto de puntos por la interpolación
x_new = np.linspace(0, 2 * np.pi, 100)
y_new = f(x_new)

# Graficar los datos originales y la interpolación
plt.plot(x, y, 'o', label = 'Datos originales')
plt.plot(x_new, y_new, '-', label = 'Interpolación')
plt.legend()
plt.show()