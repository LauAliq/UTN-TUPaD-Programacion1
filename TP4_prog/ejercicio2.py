numero: str = input("Ingrese un número entero: ")
digitos: int = 0
for i in numero:
    digitos += 1

print(f"El número ingresado tiene {digitos} dígitos.")