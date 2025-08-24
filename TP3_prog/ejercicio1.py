# Se le pide al usuario que ingrese su edad, y se almacena ese valor en la variable edad.

edad = int(input("Ingrese su edad en años: "))

# Si el usuario tiene más de (o exactamente) 18 años, se imprime por pantalla que es mayor de edad.

if edad >= 18:
    print("Es mayor de edad.")