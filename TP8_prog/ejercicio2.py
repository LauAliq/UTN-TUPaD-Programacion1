with open("productos.txt", "r") as archivo:
    encabezado = archivo.readline().strip()
    primera_linea = archivo.readline().strip().split(",")
    segunda_linea = archivo.readline().strip().split(",")
    tercera_linea = archivo.readline().strip().split(",")

    print(f"Producto: {primera_linea[0].title()} | Precio: ${primera_linea[1]} | Cantidad: {primera_linea[2]}")
    print(f"Producto: {segunda_linea[0].title()} | Precio: ${segunda_linea[1]} | Cantidad: {segunda_linea[2]}")
    print(f"Producto: {tercera_linea[0].title()} | Precio: ${tercera_linea[1]} | Cantidad: {tercera_linea[2]}")
