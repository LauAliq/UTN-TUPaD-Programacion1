def fib(x):
    return 0 if x == 0 else 1 if x == 1 else fib(x - 1) + fib(x - 2)

num = input("Ingrese un número natural: ")
while not num.isdigit():
    num = input("Ingrese un número válido por favor: ")

print([fib(i) for i in range(int(num) + 1)])