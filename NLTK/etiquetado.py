# ETIQUETADO: Asigna etiquetas a las palabras en un texto para indicar su funcion gramatical o su categoria semantica

import nltk
nltk.download("averaged_perceptron_tagger")
from nltk import pos_tag
from nltk.tokenize import word_tokenize

sentence = "NLTK es una biblioteca de procesamiento de lenguaje natural"
tokens = word_tokenize(sentence)
tagged_word = pos_tag(tokens)
print (tagged_word)

