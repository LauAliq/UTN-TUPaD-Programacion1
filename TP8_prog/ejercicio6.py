with open("productos.txt", "r") as archivo:
    productos = [0, 1, 2, 3]
    encabezado = archivo.readline().strip()
    primera_linea = archivo.readline().strip().split(",")
    segunda_linea = archivo.readline().strip().split(",")
    tercera_linea = archivo.readline().strip().split(",")
    cuarta_linea = archivo.readline().strip().split(",")

    productos[0] = {"Producto" : primera_linea[0], "Precio" : primera_linea[1], "Cantidad" : primera_linea[2]}
    productos[1] = {"Producto" : segunda_linea[0], "Precio" : segunda_linea[1], "Cantidad" : segunda_linea[2]}
    productos[2] = {"Producto" : tercera_linea[0], "Precio" : tercera_linea[1], "Cantidad" : tercera_linea[2]}
    productos[3] = {"Producto" : cuarta_linea[0], "Precio" : cuarta_linea[1], "Cantidad" : cuarta_linea[2]}

with open("productos.txt", "r") as archivo:

    productos_lista = []
    for i in range(len(productos)):
        productos_lista.append(f"{productos[i]["Producto"]},{productos[i]["Precio"]},{productos[i]["Cantidad"]}\n") 
    
    decision = input("¿Desea agregar un producto a la lista? S/N: ")
    while decision.lower() not in ("s", "n"):
        decision = input("Por favor, ingrese una opción válida. S/N:")
    
    while decision.lower() == "s":
        n_p = input("Ingrese el nombre del producto a agregar: ")
        while n_p == "" or n_p.lower() in [productos_lista[i].split(",")[0] for i in range(len(productos_lista))]:
            n_p = input("Es posible que el producto ingresado ya exista en la lista. Intente con otro: ")
        
        p_p = input("Ingrese el precio del producto a ingresar: ")
        while p_p == "" or not p_p.isdigit():
            p_p = input("Ingrese un valor válido para el precio: ")
        
        c_p = input("Ingrese la cantidad de unidades del producto a ingresar: ")
        while c_p == "" or not c_p.isdigit():
            c_p = input("Ingrese un valor válido para la cantidad de unidades: ")
        
        productos_lista.append(f"{n_p},{p_p},{c_p}\n")

        decision = input("¿Desea agregar otro producto? S/N: ")
        while decision.lower() not in ("s", "n"):
            decision = input("Por favor, ingrese una opción válida. S/N:")
        
    print("¡Adiós!")

with open("productos.txt", "w") as archivo:
    archivo.write("producto,precio,cantidad\n")
    archivo.writelines(productos_lista)