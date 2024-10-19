import tensorflow as tf 

# Crear un tensor constante
tensor_constante = tf.constant([[1,2,3], [4,5,6]])

# Crear un tensor variable
tensor_variable = tf.Variable ([[1.0, 2.0], [3.0, 4.0]])

# Operaciones con tensores
suma = tf.add(tensor_constante, 10)
producto = tf.multiply(tensor_variable, 2)

print("Tensor constante:")
print(tensor_constante.numpy())

print("\nTensor variable:")
print(tensor_variable.numpy())

print("\nSuma:")
print(suma.numpy())

print("\nProducto:")
print(producto.numpy())