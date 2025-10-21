def suma_digitos(n):
    if n == 0:
        return 0
    else:
        nu = n % 10
        return nu + suma_digitos(n // 10)

num = input("Ingrese un número natural: ")
while not num.isdigit():
    num = input("Ingrese un número válido por favor: ")

print(suma_digitos(int(num)))