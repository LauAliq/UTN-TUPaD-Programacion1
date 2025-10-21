def fact(x):
    return 1 if x == 1 or x == 0 else x * fact(x - 1)

num = input("Ingrese un número natural: ")
while not num.isdigit():
    num = input("Ingrese un número válido por favor: ")

print([fact(i) for i in range(int(num) + 1)])