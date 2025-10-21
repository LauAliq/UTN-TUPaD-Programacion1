def contar_digito(numero, digito):
    if numero == 0:
        return 0
    else:
        if numero % 10 == digito:
            valor = 1
        else:
            valor = 0
        return valor + contar_digito(numero // 10, digito)
    
num1 = input("Ingrese un número natural: ")
while not num1.isdigit():
    num1 = input("Ingrese un número válido por favor: ")

num2 = input("Ingrese un dígito del 0 al 9: ")
while not num2.isdigit() or len(num2) != 1:
    num2 = input("Ingrese un dígito válido por favor: ")

print(contar_digito(int(num1), int(num2)))