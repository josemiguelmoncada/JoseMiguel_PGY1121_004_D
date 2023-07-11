import funcion as fn
import numpy as np

cantidad1 = 0
cantidad2 = 0
cantidad3 = 0
cantidad4 = 0

total1=0
total2=0
total3=0
total4=0

comprador = []
matriz = np.empty([10, 4], type(str))
cont = 10

for i in range(10):
    for j in range(4):
        matriz[i, 0] = f"A{cont}"
        matriz[i, 1] = f"B{cont}"
        matriz[i, 2] = f"C{cont}"
        matriz[i, 3] = f"D{cont}"
    cont -= 1

while True:
    menu = fn.menu()
    if menu == 1:
        fn.comprar(matriz, comprador, cantidad1, cantidad2, cantidad3, cantidad4, total1, total2, total3, total4)
    elif menu==2:
        fn.mostrar(matriz)
    elif menu==3:
        fn.ver(comprador)
    elif menu == 4:
        fn.mostrart(cantidad1, cantidad2, cantidad3, cantidad4, total1, total2, total3, total4)

    elif menu == 5:
        break
