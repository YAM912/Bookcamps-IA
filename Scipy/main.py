import scipy
import scipy.optimize

# Definir la función objetivo (rosenbrock)
def rosenbrok(x):
    return (1 - x[0])**2 + 100 * (x[1] - x[0]**2)**2

# Minimizar la función objetivo
result = scipy.optimize.minimize(rosenbrok, (2, 2))
print("Mínimo encontrado: ", result.x)


