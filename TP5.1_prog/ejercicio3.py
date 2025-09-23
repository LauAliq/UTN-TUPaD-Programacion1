# Importamos la función randint

from random import randint

# Creamos la lista de 15 elementos aleatorios

lista: list = [randint(1, 100) for i in range(15)]

# Creamos las listas que van a almacenar los números pares y los impares de la lista original

lista_par: list = []
lista_impar: list = []

# Almacenamos los números pares e impares en sus respectivas listas

for i in range(len(lista)):
    if lista[i] % 2 == 0:
        lista_par.append(lista[i])
    else:
        lista_impar.append(lista[i])

# Imprimimos la lista original y la cantidad de números pares e impares de dicha lista

print(f"La lista creada fue {lista}.")
print(f"De dicha lista, {len(lista_par)} son números pares, y {len(lista_impar)} son impares.")