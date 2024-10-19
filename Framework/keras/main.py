import numpy as np
import keras 

# Build a simple Sequential model 
# Construya un modelo secuencial simple
model = keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])

# Compile the model  
# Compilar el modelo
model.compile(optimizer='sgd', loss='mean_squared_error')

# Declare model inputs and outputs for training
# Declare las entradas y salidas del modelo para el entrenamiento
x = np.array([1.0, 2.0, 3.0, 4.0, 5.0], dtype=float)
y = np.array([11.0, 21.0, 31.0, 41.0, 51.0], dtype=float)

# Train the model
# Entrenar el modelo
model.fit(x, y, epochs=100)

# Make prediction
# Realizar predicciones
print(model.predict(np.array([10.0])))  # Convertir a array de NumPy

















