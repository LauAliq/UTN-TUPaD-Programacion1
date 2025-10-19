dict = {"leche": 10, "huevos": 30, "manteca": 15, "galletas": 20, "tortitas": 12}
bandera = True

while bandera:

    consulta = input("Ingrese 1 si desea consultar el stock de un producto, ingrese 2 si desea modificar el stock de un producto existente, ingrese 3 si desea agregar un producto nuevo y su stock, o ingrese 4 si desea salir del menú: ")
    while consulta not in ("1", "2", "3", "4"):
        consulta = input("Por favor, ingrese un comando válido: 1, 2 ó 3: ")

    if consulta == "1":
        producto = input("¿De qué producto desea consultar el stock?: ")
        while producto.lower() not in dict:
            producto = input(f"Los productos con stock son {list(dict.keys())}. Ingrese un producto de la lista: ")
        print(f"Hay {dict[producto.lower()]} unidades del producto {producto} en stock.")

    elif consulta == "2":
        producto = input("¿De qué producto desea actualizar el stock?: ")
        while producto.lower() not in dict:
            producto = input(f"Los productos con stock son {list(dict.keys())}. Ingrese un producto de la lista: ")
        unidades = input(f"¿Cuántas unidades de {producto} hay en stock?: ")
        while not unidades.isdigit():
            unidades = input("Ingrese una cantidad válida: ")
        dict[producto.lower()] = unidades
        print(f"Ahora hay {dict[producto.lower()]} unidades del producto {producto} en stock.")

    elif consulta == "3":
        producto = input("¿Qué producto desea agregar al stock?: ")
        while producto.lower() in dict:
            producto = input(f"Los productos con stock son {list(dict.keys())}. Ingrese un producto que no esté en la lista para agregar: ")
        unidades = input(f"¿Cuántas unidades de {producto} hay en stock?: ")
        while not unidades.isdigit():
            unidades = input("Ingrese una cantidad válida: ")
        dict[producto.lower()] = unidades
        print(f"Ahora hay {dict[producto.lower()]} unidades del producto {producto} en stock.")

    else:
        bandera = False
        print("¡Adiós!")