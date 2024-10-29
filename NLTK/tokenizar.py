#TOKENIZACION: Proceso de dividir un texto en unidades mas pequeñas, llamadas tokens. Estos tokens pueden ser palbras individuales,
#fraces, simbolos de puntuacion, o incluso caracteres

# Division de una oracion en palabras individuales
import nltk
from nltk.tokenize import word_tokenize
nltk.download("punkt")

sentence = "NLTK es una biblioteca de procesamiento de lenguaje natural"
tokens = word_tokenize (sentence)
print (tokens)


