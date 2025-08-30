from random import randint

rndm: int = randint(1, 100)
contador = 1
bandera: bool = False

num: int = int(input("Ingrese cuántos intentos desea tener (0 para intentos infinitos): "))
if num == 0:
    intentos: int = 999999999
else:
    intentos = num
    
adivstring: str = input("Adivina el número en que esto pensando (entre 1 y 100): ")
while "." in adivstring:
    adivstring =  input("El número debe ser entero!: ")
if rndm == int(adivstring):
    print("Adivinaste al primer intento!")
else:
    bandera = True
while bandera:
    if "." not in adivstring:
        if int(adivstring) > rndm:
            adivstring = input("Más chico!: ")
        elif int(adivstring) < rndm:
            adivstring = input("Más grande!: ")
        contador += 1
        if int(adivstring) == rndm:
            print(f"Acertaste mi número en {contador} intentos.")
            break
        if contador >= intentos:
            print(f"Te quedaste sin intentos, el número era {rndm}.")
            break
    else:
        adivstring = input("El número debe ser entero!: ")