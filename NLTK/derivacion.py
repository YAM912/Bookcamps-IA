# DERIVACION: Proceso de reducir una palabra en su forma base o raiz
import nltk
from nltk.stem import PorterStemmer

words = ["running","plays", "jumped" ]
stemmer = PorterStemmer()
steam = [stemmer.stem(word) for word in words]
print (steam)
