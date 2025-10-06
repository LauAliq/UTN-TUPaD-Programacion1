def tabla_multiplicar(numero):
    for i in range(10):
        print(f"{i + 1} por {numero} es {(i + 1) * numero}.")

numero_u = int(input("Ingresa un número: "))
tabla_multiplicar(numero_u)