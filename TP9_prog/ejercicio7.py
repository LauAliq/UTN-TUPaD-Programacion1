def suma_todos(n):
    if n == 0:
        return 0
    else:
        return n + suma_todos(n - 1)
    
num = input("Ingrese un número natural: ")
while not num.isdigit():
    num = input("Ingrese un número válido por favor: ")

print(suma_todos(int(num)))