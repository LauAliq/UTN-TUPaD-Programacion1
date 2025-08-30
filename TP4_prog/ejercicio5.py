from random import randint

rndm: int = randint(0,9)
contador: int = 0
bandera = True
while bandera:
    adiv: int = int(input("Adivina el número en que estoy pensando (entre el 0 y el 9): "))
    contador += 1
    if adiv == rndm:
        bandera = False

print(f"Adivinaste mi número en {contador} intento(s).")