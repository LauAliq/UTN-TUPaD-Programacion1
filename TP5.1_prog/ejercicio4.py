# Creamos la lista con posibles elementos repetidos

datos: list = [1, 3, 5, 3, 7, 1, 9, 5, 3]

# Creamos la lista que almacenará los elementos de la lista datos sin repetir

datos_sin_repetir: list = []

# Rellenamos la lista datos_sin_repetir con los elementos de la lista datos sin repetir

for i in range(len(datos)):
    if datos[i] not in datos_sin_repetir:
        datos_sin_repetir.append(datos[i])

# Imprimimos ambas listas

print(f"La lista con posibles elementos repetidos es {datos}.")    
print(f"La lista sin elementos repetidos es {datos_sin_repetir}.")