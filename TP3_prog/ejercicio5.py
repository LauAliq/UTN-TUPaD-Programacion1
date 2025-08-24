# Se define la variable contraseña, la cual es ingresada por el usuario.

contraseña = input("Por favor, ingrese su contraseña de entre 8 y 14 caracteres inclusive: ")

# Se le pide al usuario que ingrese una contraseña de 8 a 14 caracteres de largo, hasta que el usuario lo haga.

while len(contraseña) < 8 or len(contraseña) > 14:
    contraseña = input("Por favor, ingrese una contraseña válida: ")
print("Ha ingresado una contraseña correcta.")