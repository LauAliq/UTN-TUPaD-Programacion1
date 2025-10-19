numeros_telefonicos = {}

for i in range(5):
    nombre = input("Ingrese el nombre del contacto que desea guardar: ")
    while nombre in numeros_telefonicos:
        nombre = input("Ya existe un contacto guardado con ese nombre. Prueba con otro: ")
    numeros_telefonicos[nombre] = input(f"Ingrese el número de teléfono de {nombre}: ")
    while numeros_telefonicos[nombre] == "" or not numeros_telefonicos[nombre].isdigit():
        numeros_telefonicos[nombre] = input(f"Por favor, ingrese un número válido de teléfono para {nombre}: ")
    print(f"El número de {nombre} ha sido guardado correctamente.")

consultar = input("¿De quién es el número que desea consultar? Ingrese su nombre: ")

if consultar in numeros_telefonicos:
    print(f"El número de {consultar} es {numeros_telefonicos[consultar]}.")
else:
    print(f"No tienes guardado un contacto con el nombre de {consultar}.")