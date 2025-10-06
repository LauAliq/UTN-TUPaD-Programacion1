# Creamos la lista
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
# Modificamos un poco la lista
compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")
# Imprimimos la lista
print(compras)