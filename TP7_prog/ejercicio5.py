frase = input("¡Hola usuario! Por favor, ingresa una frase: ")
palabras = frase.lower().split()
palabras2 = set(palabras)
dict = {}
for palabra in palabras:
    if palabra not in dict:
        dict[palabra] = 1
    else:
        dict[palabra] += 1

print(f"El diccionario queda así: {dict}.")
print(f"Las palabras utilizadas en la frase fueron: {palabras2}.")