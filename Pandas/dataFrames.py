import pandas as pd
datos = {'Nombre': ['Alice', 'Bob', 'Charlie'],
         'Edad': [25, 30, 35],
         'Ciudad': ['A', 'B', 'C']}
df1 = pd.DataFrame(datos)
print (df1)

df = pd.DataFrame(datos, index=['a', 'b', 'c'])
print(df)
#Seleccionar datos con loc[]
seleccion_loc = df.loc['b', 'Edad'] 
print(seleccion_loc)
#Seleccionar datos con at[]
seleccion_at = df.at['b', 'Edad']
print(seleccion_at)

#Seleccionar datos con iat[]
seleccion_iat = df.iat[1, 1]
print(seleccion_iat)

