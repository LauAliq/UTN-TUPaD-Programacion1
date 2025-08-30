num: str = input("Ingrese un número entero de varios dígitos: ")
num_invertido: str = ""
for i in range(len(num)):
    num_invertido += num[- i - 1]

print(f"El número invertido al que ingresó es {num_invertido}.")