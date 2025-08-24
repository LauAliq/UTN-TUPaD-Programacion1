# Se le pide al usuario que ingrese su edad, y se guarda ese valor en la variable edad.

edad = int(input("Ingrese su edad: "))

# Según la edad del usuario, se lo clasifica en niño, adolescente, adulto joven o adulto.

if edad < 12:
    print("Es un niño.")
elif edad < 18:
    print("Es un adolescente.")
elif edad < 30:
    print("Es un adulto joven.")
else:
    print("Es un adulto.")