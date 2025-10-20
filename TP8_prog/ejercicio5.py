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

    bandera = False
    busqueda = input("Por favor, ingrese el nombre de un producto que desea chequear: ")
    while busqueda == "":
        busqueda = input("Por favor, ingrese el nombre de un producto válido: ")
    
    for i in range(len(productos)):
        if busqueda == productos[i]["Producto"]:
            print(f"Producto: {productos[i]["Producto"].title()} | Precio: ${productos[i]["Precio"]} | Cantidad: {productos[i]["Cantidad"]}")
            bandera = True
        
    if bandera == False:
        print(f"El producto {busqueda} no se encuentra en la lista de productos.")
        

