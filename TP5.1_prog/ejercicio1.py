# Creamos la variable tipo lista que contiene las notas

lista_notas = [5, 8, 6, 9, 9, 10, 6, 7, 7, 8]

# Imprimimos por pantalla la lista completa

print("La lista de las notas del curso es: ")
for i in range(len(lista_notas) - 1):
    print(lista_notas[i], end = ", ")
print(f"{lista_notas[-1]}.")

#Creamos la variable promedio

promedio = 0

# Calculamos el promedio de las notas

for i in range(len(lista_notas)):
    promedio += lista_notas[i]
promedio = promedio / len(lista_notas)

# imprimimos el promedio de la lista

print(f"El promedio de dicha lista es {promedio}.")

# Creamos las variables max y min, las cuales van a almacenar las notas máxima y mínima, respectivamente

max = 0
min = 10

# Calculamos e imprimimos las notas máxima y mínima

for i in range(len(lista_notas)):
    if lista_notas[i] > max:
        max = lista_notas[i]
    if lista_notas[i] < min:
        min = lista_notas[i]
print(f"La nota máxima fue de {max}, mientras que la nota mínima fue de {min}.")