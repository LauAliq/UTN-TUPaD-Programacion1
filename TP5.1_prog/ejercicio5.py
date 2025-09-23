# Creamos la lista con los nombres de los alumnos presentes y la imprimimos

nombres = ["Nahuel", "Facundo", "Lautaro", "Enzo", "Pablo", "Leandro", "Rodrigo", "Bautista"]
print(f"Los alumnos presentes son {nombres}.")

# Creamos la variable modificador, que almacena la información acerca de lo que el usuario quiere hacer con la lista

modificador = input("¿Desea agregar un alumno a la lista (oprima 1), eliminar un alumno (oprima 2), o dejarla como está (oprima 3)?: ")
while modificador != "1" and modificador != "2" and modificador != "3":
    modificador = input("Ingrese un valor adecuado. 1 para agregar, 2 para eliminar o 3 para no modificar: ")
modificador = int(modificador)

# Creamos la variable bandera para iniciar el bucle while

bandera = True
while bandera:

    # Si el usuario quiere agregar un nombre a la lista, este se agrega y se pregunta de nuevo qué se quiere hacer

    if modificador == 1:
        agregar = input("Ingrese el nombre del estudiante que desea agregar a la lista: ")
        while not agregar.isalpha():
            agregar = input("Ingrese un nombre válido")
        nombres.append(agregar)
        print(f"Se agregó el nombre {agregar} con éxito. Ahora la lista de alumnos presentes es: {nombres}.")
        modificador = input("¿Desea agregar un alumno a la lista (oprima 1), eliminar un alumno (oprima 2), o dejarla como está (oprima 3)?: ")
        while modificador != "1" and modificador != "2" and modificador != "3":
            modificador = input("Ingrese un valor adecuado. 1 para agregar, 2 para eliminar o 3 para no modificar: ")
        modificador = int(modificador)

    # Si el usuario quiere eliminar un nombre a la lista, este se elimina y se pregunta de nuevo qué se quiere hacer

    elif modificador == 2:
        eliminar = input("Ingrese el nombre del estudiante que desea eliminar de la lista: ")
        while eliminar not in nombres:
            eliminar = input(f"El nombre ingresado no se encuentra en la lista, intente con otro (la lista de nombres es {nombres}): ")
        nombres.remove(eliminar)
        print(f"Se eliminó el nombre ingresado con éxito. La lista de alumnos presentes ahora es: {nombres}.")
        modificador = input("¿Desea agregar un alumno a la lista (oprima 1), eliminar un alumno (oprima 2), o dejarla como está (oprima 3)?: ")
        while modificador != "1" and modificador != "2" and modificador != "3":
            modificador = input("Ingrese un valor adecuado. 1 para agregar, 2 para eliminar o 3 para no modificar: ")
        modificador = int(modificador)
    
    # Si se desea terminar con el código, se muestra la lista final por pantalla

    else:
        bandera = False
        print(f"La lista final de alumnos presentes es {nombres}.")