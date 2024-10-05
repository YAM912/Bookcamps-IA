import pandas as pd

data = [1, 2, 3, 4, 5]
etiquetas = ["a", "b","c","d","e"]

serie = pd.Series(data, index = etiquetas)
print (serie)
