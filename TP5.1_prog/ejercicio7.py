from random import randint

lista: list = [[randint(10, 30) for i in range(2)] for j in range(7)]

for j in range(len(lista)):
    if lista[j][0] > lista[j][1]:
        lista[j][0], lista[j][1] = lista[j][1], lista[j][0]

print(f"De lunes a domingo, se registraron las siguientes temperaturas máximas y mínimas: {lista}.")

prom_min: int = 0
prom_max: int = 0
amplitud_max: int = 0
lista_amplitudes: list = []

for j in range(len(lista)):
    prom_min += lista[j][0]
    prom_max += lista[j][1]
    if lista[j][1] - lista[j][0] > amplitud_max:
        amplitud_max = lista[j][1] - lista[j][0]
    lista_amplitudes.append(lista[j][1] - lista[j][0])

prom_max = prom_max / len(lista)
prom_min = prom_min / len(lista)

print(f"El promedio de las mínimas fue de {round(prom_min, 2)}°C, mientras que el de las máximas fue de {round(prom_max, 2)}°C.")

dia: int = lista_amplitudes.index(amplitud_max)

if dia == 0:
    print(f"El lunes se registró la mayor amplitud térmica, siendo esta de {amplitud_max}°C.")
elif dia == 1:
    print(f"El martes se registró la mayor amplitud térmica, siendo esta de {amplitud_max}°C.")
elif dia == 1:
    print(f"El miércoles se registró la mayor amplitud térmica, siendo esta de {amplitud_max}°C.")
elif dia == 1:
    print(f"El jueves se registró la mayor amplitud térmica, siendo esta de {amplitud_max}°C.")
elif dia == 1:
    print(f"El viernes se registró la mayor amplitud térmica, siendo esta de {amplitud_max}°C.")
elif dia == 1:
    print(f"El sábado se registró la mayor amplitud térmica, siendo esta de {amplitud_max}°C.")
else:
    print(f"El domingo se registró la mayor amplitud térmica, siendo esta de {amplitud_max}°C.")