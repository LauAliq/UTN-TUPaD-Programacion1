# Creamos la lista

lista = [0, 0, 0, 0, 0]

#Rellenamos la lista

for i in range(5):
    producto = input("Ingrese un producto a la lista: ")
    while not (producto.isalpha()):
        producto = input("Ingresa in producto válido: ")
    lista[i] = producto

#Imprimimos la lista

print(f"La lista realizada es {lista}.")

# Convertimos la lista a minúsculas

for i in range(len(lista)):
    lista[i] = lista[i].lower()

# Preguntamos qué elemento desea eliminar el usuario

a_eliminar = input("Ingrese un producto de la lista que desea eliminar: ")
while a_eliminar.lower() not in lista:
    a_eliminar = input("El producto ingresado no está en la lista. Intenta con otro producto: ")

# Eliminamos dicho elemento

lista.remove(a_eliminar)

# Acomodamos la lista con mayúsculas

for i in range(len(lista)):
    lista[i] = lista[i].capitalize()

# Imprimimos la lista final

print(f"La lista actualizada es {lista}.")