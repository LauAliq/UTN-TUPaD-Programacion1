def es_palindromo(palabra):
    if len(palabra) == 0 or len(palabra) == 1:
        return True
    else:
        if palabra[0] != palabra[len(palabra) - 1]:
            return False
        else:
            return es_palindromo(palabra[1:len(palabra) - 1])

palabra = input("Por favor, ingrese una palabra sin espacios ni tildes: ")
while " " in palabra or "´" in palabra:
    palabra = input("Ingrese una palabra válida: ")

print(es_palindromo(palabra))