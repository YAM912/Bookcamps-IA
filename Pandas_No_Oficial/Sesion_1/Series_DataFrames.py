# Importamos la biblioteca Pandas y la llamamos "pd"
import pandas as pd
# Creamos una serie de Pandas que es como una lista con etiquetas
# Los valores son nombres de jugadores de PSG
# El indice especifica los numeros de camiseta de esos jugadores
psg_players = pd.Series(["Navas", "Mbappe", "Neymar", "Messi"], index=[1, 7, 10, 30] )
#Imprimimos la serie para ver su contenido
print (psg_players)

# Eliminamos el indice, por lo que pandas asigna un indice numerico automatico empezando desde cero
psg_players2 = pd.Series(["Navas", "Mbappe", "Neymar", "Messi"])
print (psg_players2)

#Creamos un diccionario que asocia numeros de camiseta con nombres de jugadores
psg_diccionario = {1: "Navas", 7: "Mbappe", 10: "Neymar", 30: "Messi"}
# Creamos una serie de Pandas usando el diccionario
psg_Players_dict = pd.Series (psg_diccionario)
print (psg_Players_dict) # Imprimimos serie creada a partir del diccionario
print (psg_Players_dict [7]) # Imprime el valor de la posicion (Indice) 7 de la serie creada a partir del diccionario
print (psg_Players_dict [0:3])

#Diccionario con datos de jugadores
dict = {"Jugador": ["Navas", "Mbappe", "Neymar", "Messi"],
        "Altura":  [183.0, 170.0, 170.0, 165.0],
        "Goles":   [2, 200, 150, 200]}
# Crear un DataFrame con el diccionario e indices perzonalizados
df = pd.DataFrame (dict, index=[1, 7, 10, 30])
print (df) #Imprime DataFrame



