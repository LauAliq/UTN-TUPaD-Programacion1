from random import randint

lista: list = [[randint(0, 10) for i in range(7)] for j in range(4)]

print(f"Esta lista muestra cuántas unidades vendió cada producto durante una semana: {lista}.")

cant_por_producto: list = [0, 0, 0, 0]
ventas_por_dia: list = [0, 0, 0, 0, 0, 0, 0]
max_venta_por_dia: int = 0
max_venta_por_producto: int = 0

for j in range(len(lista)):
    for i in range(len(lista[j])):
        cant_por_producto[j] += lista[j][i]
        ventas_por_dia[i] += lista[j][i]

for j in range(len(cant_por_producto)):
    if max_venta_por_producto < cant_por_producto[j]:
        max_venta_por_producto = cant_por_producto[j]
    
for i in range(len(ventas_por_dia)):
    if max_venta_por_dia < ventas_por_dia[i]:
        max_venta_por_dia = ventas_por_dia[i]

dia_mas_ventas: int = ventas_por_dia.index(max_venta_por_dia)
prod_mas_vendido: int = cant_por_producto.index(max_venta_por_producto)

print(f"Esta lista muestra las ventas individuales de cada producto durante toda la semana: {cant_por_producto}.")

if dia_mas_ventas == 0:
    print(f"El lunes se registró la mayor cantidad de ventas, siendo esta cantidad {max_venta_por_dia} unidades.")
elif dia_mas_ventas == 1:
    print(f"El martes se registró la mayor cantidad de ventas, siendo esta cantidad {max_venta_por_dia} unidades.")
elif dia_mas_ventas == 2:
    print(f"El miércoles se registró la mayor cantidad de ventas, siendo esta cantidad {max_venta_por_dia} unidades.")
elif dia_mas_ventas == 3:
    print(f"El jueves se registró la mayor cantidad de ventas, siendo esta cantidad {max_venta_por_dia} unidades.")
elif dia_mas_ventas == 4:
    print(f"El viernes se registró la mayor cantidad de ventas, siendo esta cantidad {max_venta_por_dia} unidades.")
elif dia_mas_ventas == 5:
    print(f"El sábado se registró la mayor cantidad de ventas, siendo esta cantidad {max_venta_por_dia} unidades.")
else:
    print(f"El domingo se registró la mayor cantidad de ventas, siendo esta cantidad {max_venta_por_dia} unidades.")

if prod_mas_vendido == 0:
    print(f"El producto A fue el más vendido de la semana, registrando {max_venta_por_producto} unidades vendidas.")
elif prod_mas_vendido == 1:
    print(f"El producto B fue el más vendido de la semana, registrando {max_venta_por_producto} unidades vendidas.")
elif prod_mas_vendido == 2:
    print(f"El producto C fue el más vendido de la semana, registrando {max_venta_por_producto} unidades vendidas.")
else:
    print(f"El producto D fue el más vendido de la semana, registrando {max_venta_por_producto} unidades vendidas.")