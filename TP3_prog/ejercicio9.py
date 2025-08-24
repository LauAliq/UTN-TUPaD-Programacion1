# Definimos la variable magnitud, la cual guarda información sobre la magnitud del terremoto.

magnitud: float = float(input("Ingrese la magnitud de un terremoto: "))

# Dependiendo de la magnitud del terremoto se imprimirán distintos mensajes por pantalla.

if magnitud < 3:
    print("Muy leve.")
elif magnitud >= 3 and magnitud < 4:
    print("Leve.")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado.")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte.")
elif magnitud >= 6 and magnitud < 7:
    print("Muy fuerte.")
else:
    print("Extremo.")