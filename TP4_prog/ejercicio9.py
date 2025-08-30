cantidad_de_numeros: int = 5
lst: list = [int(input("Ingrese un número entero: ")) for i in range(cantidad_de_numeros)]
media = 0
for i in range(cantidad_de_numeros):
    media += lst[i]

media = media / cantidad_de_numeros
print(f"La media de los números ingresados es {media}.")