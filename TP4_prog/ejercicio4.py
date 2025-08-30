bandera: bool = True
suma: int = 0
while bandera:
    numero = int(input("Ingrese un número (cero para terminar el proceso): "))
    suma += numero
    if numero == 0:
        bandera = False
print(f"La suma de los números ingresados es {suma}.")
