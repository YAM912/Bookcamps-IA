# 1. IMPORTACION DE BIBLIOTECAS
import nltk #La biblioteca de lenguaje natural Toolkit, que proporciona herramientas para procesamiento de lenguaje natural
import random # Utilizado aqui para generar muestras aleatorias

# 2. DEFINICION DEL CONJUNTO DE DATOS ETIQUETADOS
  #Data: Lista de tuplas donde cada tupla contiene un texto de comentario de pelicula y su correspondeinte etiqueta de sentimiento
  #(positivo o negativo)
Data = [
("Me encanta esta película", "positivo"),
("Esta película es terrible", "negativa"),
("Esta película es genial", "positiva"),
("No me gusta esta película", "negativo"),
("Esta película es increíble", "positiva"),
("No soporto ver esta película", "negativo"), 
("La actuación en esta película es fenomenal", "positivo"),
("Me arrepiento de haber perdido el tiempo en esta película", "negativo"),
("Disfruté mucho esta película", "positivo"),
("A esta película le falta profundidad y sustancia", "negativo"),
("La trama de esta película fue cautivadora", "positiva"),
("Encontré los personajes de esta película muy atractivos", "positivo"),
("Los efectos especiales de esta película fueron impresionantes", "positivo"), 
("La historia era predecible y poco original", "negativo"),
("Me decepcionó la falta de desarrollo del personaje", "negativo"),
("La fotografía en esta película fue impresionante", "positiva"),
("El diálogo parecía forzado y poco natural", "negativo"),
("El ritmo de la película fue demasiado lento para mi gusto", "negativo"),
("Me sorprendió gratamente lo mucho que disfruté esta película", "positivo"),
("El final me dejó insatisfecho y confundido", "negativo"), 
("Esta película superó mis expectativas", "positivo"),
("Las actuaciones de los actores fueron mediocres", "negativas")
]

# 3. PREPROCESAMIENTO DE DATOS: tokenizacion y extraccion de caracteristicas
  #Preprocess(Text): Funcion que toma un texto como entrada y realiza el procesamiento basico, que en este caso es la tokenizcion
  #Cada token (palbra) en el texto se convierte en una caracteristica con un valor booleano verdadero (True)

def preprocess (text):
    tokens = nltk.word_tokenize(text)
    return {word: True for word in tokens}

# 4. APLICACION DEL PROCESAMIENTO DE DATOS 
  # featuresets: Lista de tuplas donde cada tupla contiene un diccionario de caracteristicas procesadas y su correspondiente etiqueta
  # Las caracteristicas se extraen utilizando la funcion preprocess() y se almacenan como diccionarios
  
featuresets = [(preprocess(text), label) for (text, label) in Data]

# 5. DIVISION DE DATOS: Dividimos los datos en conjuntos de entrenamiento y pruebas
  # train_set, test_set: Se dividen los datos preprocesados en conjuntos de entrenamiento y prueba. Aqui los primeros 16 elementos se
  # utilizan para el conjunto de entrenamiento y el resto para el conjunto d pruebas

train_set, test_set = featuresets[:16], featuresets[16:]

# 6. ENTRENAMIENTO DEL CLASIFICADOR
  # nltk.NaiveBayesClassifier.train(train_set): Se entrena un clasificador Naives Bayes utilizando el conjunto de entrenamiento
  
  #Entrenamos un clasificador utilizando Naive Bayes
classifier = nltk.NaiveBayesClassifier.train(train_set)

# 7. EVALUACION DEL CLASIFICADOR: Evaluamos el clasificador en el conjunto de prueba
  # nltk.classify.accuracy(classifier, test_set): Se evalua la precicion del clasificador en el conjunto de prueba y se imprime el resultado

accuracy = nltk.classify.accuracy(classifier, test_set)
print ("accuracy: ", accuracy)

# 8. CLASIFICACION DE UN NUEVO TEXTO
  # Se proporciona un nuevo texto (new_text) que se desea clasificar
  # Se procesa el nuevo texto (preprocess(new_tex)), para convertirlo rn caracteristicas
  # Se utiliza el clasificador entrenado para predecir la etiqueta del nuevo texto y se imprime el resultado
  
new_text = "Esta pelicula es increible "
new_text_features = preprocess(new_text)
predicted_label = classifier.classify(new_text_features)
print ("predicted label: " , predicted_label)


