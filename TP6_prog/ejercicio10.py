def calcular_promedio(a, b, c):
    print(f"El promedio entre {a}, {b} y {c} es {round((a + b + c) / 3, 2)}.")

num1 = float(input("Ingresa un número: "))
num2 = float(input("Ingresa otro número: "))
num3 = float(input("Ingresa un último número: "))

calcular_promedio(num1, num2, num3)