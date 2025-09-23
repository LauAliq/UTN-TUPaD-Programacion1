from random import randint

lista = [randint(1, 100) for i in range(15)]
lista_par = []
lista_impar = []
for i in range(len(lista)):
    if lista[i] % 2 == 0:
        lista_par.append(lista[i])
    else:
        lista_impar.append(lista[i])

print(f"La lista creada fue {lista}.")
print(f"De dicha lista, {len(lista_par)} son números pares, y {len(lista_impar)} son impares.")