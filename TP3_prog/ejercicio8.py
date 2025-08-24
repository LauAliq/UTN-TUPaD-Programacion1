# Se definen las variables nombre y num, las cuales almacenan el nombre del usuario y la clave para escribirlos en mayúsculas, minúsculas o tipo título, respectivamente.

nombre = input("Por favor, ingrese su nombre: ")
num = int(input("Por favor, ingrese el número 1 si desea su nombre en mayúsculas, 2 si desea su nombre en minúsculas o 3 si desea que su nombre comience con mayúscula; "))

# Dependiendo del valor de la variable num, se imprime el nombre del usuario en pantalla como él mismo lo desee.

if num == 1:
    print(nombre.upper())
elif num == 2:
    print(nombre.lower())
elif num == 3:
    print(nombre.title())
else:
    print("No se ingresó un comando válido.")
