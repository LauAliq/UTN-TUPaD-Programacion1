digitos: int = 0
# while numero[0] not in "123456789":
#     numero = numero[1: -1]
bandera: bool = True

while bandera:
    numero: str = input("Ingrese un número entero: ")
    if not numero.isalpha():
        bandera = False
    else:
        bandera = True
for i in numero:
    if i != 0:
        digitos += 1

print(f"El número ingresado tiene {digitos} dígito(s).")