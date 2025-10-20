with open("productos.txt", "r+") as archivo:
    encabezado = archivo.readline().strip()
    primera_linea = archivo.readline().strip().split(",")
    segunda_linea = archivo.readline().strip().split(",")
    tercera_linea = archivo.readline().strip().split(",")

    print(f"Producto: {primera_linea[0].title()} | Precio: ${primera_linea[1]} | Cantidad: {primera_linea[2]}")
    print(f"Producto: {segunda_linea[0].title()} | Precio: ${segunda_linea[1]} | Cantidad: {segunda_linea[2]}")
    print(f"Producto: {tercera_linea[0].title()} | Precio: ${tercera_linea[1]} | Cantidad: {tercera_linea[2]}")

    nuevo_producto = input("Ingrese un nuevo producto para ingresar a la lista: ")
    while nuevo_producto == "" or nuevo_producto.lower() in (primera_linea[0], segunda_linea[0], tercera_linea[0]):
        nuevo_producto = input("Ese producto ya está en la lista. Ingrese otro producto: ")
    
    precio_n_p = input("Ingrese el precio del producto a añadir a la lista: ")
    while precio_n_p == "" or not precio_n_p.isdigit():
        precio_n_p = input("Por facor, ingrese un valor válido: ")
    
    cantidad_n_p = input("Ingrese la cantidad del producto a añadir a la lista: ")
    while cantidad_n_p == "" or not cantidad_n_p.isdigit():
        cantidad_n_p = input("Por facor, ingrese un valor válido: ")
    
    archivo.write(f"{nuevo_producto.lower()},{int(precio_n_p)},{int(cantidad_n_p)}\n")