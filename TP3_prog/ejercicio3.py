# Se define la variable num, la cual debe almacenar un número par.

num = int(input("Ingrese un número par: "))

# Se le pide al usuario que ingrese un número par para la variable num hasta que lo haga.

while num % 2 != 0:
    num = int(input("Por favor, ingrese un número par: "))
print("Ha ingresado un número par")