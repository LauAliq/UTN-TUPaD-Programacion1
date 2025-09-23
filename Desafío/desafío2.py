from random import randint
puntos_usuario = 0
puntos_computadora = 0
bandera = True
bucles = 0

print("Estás por jugar a piedra, papel o tijera con la computadora. La partida acaba cuando alguien llegue a tres puntos, o cuando transcurran cinco rondas. ¡Buena suerte!")

while bandera:
    bucles += 1
    usuario = int(input("Seleccione un número: 1 para piedra, 2 para papel o 3 para tijera: "))
    while usuario != 1 and usuario != 2 and usuario != 3:
        usuario = int(input("Seleccione un número: 1 para piedra, 2 para papel o 3 para tijera: "))

    computadora = randint(1, 3)

    if (usuario == 1 and computadora == 3) or (usuario == 2 and computadora == 1) or (usuario == 3 and computadora == 2):
        puntos_usuario += 1
        print(f"¡Ganaste esta ronda! La computadora eligió {computadora}.")
    elif (usuario == 1 and computadora == 1) or (usuario == 2 and computadora == 2) or (usuario == 3 and computadora == 3):
        pass
        print(f"Empatas esta ronda, ambos eligieron {usuario}.")
    else:
        puntos_computadora += 1
        print(f"Pierdes esta ronda, la computadora eligió {computadora}.")

    if puntos_computadora > 2 or puntos_usuario > 2:
        bandera = False

    if bucles > 4:
        bandera = False
    
if puntos_computadora > puntos_usuario:
    print(f"Te ganó la computadora {puntos_computadora} a {puntos_usuario}.")
elif puntos_computadora < puntos_usuario:
    print(f"Le has ganado a la computadora {puntos_usuario} a {puntos_computadora}.")
else:
    print(f"Has empatado con la computadora {puntos_usuario} a {puntos_computadora}.")