def pot(a, b):
    return 1 if b == 0 else a * pot(a, b - 1)

num1 = input("Ingrese un número natural: ")
while not num1.isdigit():
    num1 = input("Ingrese un número válido por favor: ")

num2 = input("Ingrese otro número natural: ")
while not num2.isdigit():
    num2 = input("Ingrese un número válido por favor: ")

print(f"el resultado de hacer {num1} elevado a la {num2} es {pot(int(num1), int(num2))}.")