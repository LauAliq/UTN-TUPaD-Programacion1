def a_binario(x):
    if x == 0:
        return ""
    else:
        resto = str(x % 2)
        return a_binario(x // 2) + resto

num = input("Ingrese un número natural: ")
while not num.isdigit():
    num = input("Ingrese un número válido por favor: ")

print(a_binario(int(num)))