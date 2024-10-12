# Ejemplo real para el procesamiento de señales

import numpy as np
from scipy.signal import butter, filtfilt
import matplotlib.pyplot as plt

#Generar una señal de ejemplo
fs = 1000 # Frecuencia de muestreo
t = np.linspace (0, 1, fs, endpoint=False)
x = np.sin(2*np.pi*50*t) + np.random.normal(scale=0.5, size=len(t))

# Filtrar la señal utilizando un filtro pasa bajos
nyq = 0.5 * fs
corte = 30
corte_normal = corte / nyq
b, a = butter (4, corte_normal, btype="low", analog=False)
señal_filtrada = filtfilt (b, a, x)

# Graficar la señal original y la señal filtrada
plt.plot(t, x, label="Señal original")
plt.plot(t, señal_filtrada, label="Señal filtrada")
plt.legend()
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud")
plt.show()
