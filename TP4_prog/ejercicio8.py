cantidad_de_numeros: int = 5
lst: list = [int(input("Ingrese un número: ")) for i in range(cantidad_de_numeros)]
pares: int = 0
impares: int = 0
positivos: int = 0
negativos: int = 0
for i in range(5):
    if lst[i] % 2 == 0:
        pares += 1
    else:
        pass
    if lst[i] > 0:
        positivos += 1
    elif lst[i] < 0:
        negativos += 1
    else:
        pass

impares = cantidad_de_numeros - pares
ceros: int = cantidad_de_numeros - (positivos + negativos)

print(f"Se ingresaron {pares} números pares, {impares} impares, {positivos} números positivos y {negativos} números negativos. De los números ingresados, {ceros} fueron el número 0.")