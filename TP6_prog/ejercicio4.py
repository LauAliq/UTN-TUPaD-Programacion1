def calcular_area_circulo(radio):
    print(f" el área del círculo de radio {radio} es {3.1415 * (radio ** 2)}.")

def calcular_perimetro_circulo(radio):
    print(f" el perímetro del círculo de radio {radio} es {3.1415 * radio * 2}.")

radio_u = int(input("Ingrese el radio de un círculo: "))

calcular_area_circulo(radio_u)
calcular_perimetro_circulo(radio_u)