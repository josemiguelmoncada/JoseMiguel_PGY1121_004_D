import os


def menu():
    os.system("cls")
    print("""
1. Comprar departamento
2. Mostrar departamentos disponibles
3. Ver listado de compradores
4. Mostrar ganancias totales
5. Salir""")
    while True:
        try:
            op = int(input("\tSeleccione una opcion: "))
            if op > 0 and op < 6:
                return op
            else:
                print("debe ingresa un numero entra 1 y 5")
        except ValueError:
            print("opcion invalida")


def comprar(matriz, comprador, cantidad1, cantidad2, cantidad3, cantidad4, total1, total2, total3, total4):
    os.system("cls")
    print(matriz,
          """\n
•Tipo A, 3.800 UF
•Tipo B, 3.000 UF
•Tipo C, 2.800 UF
•Tipo D, 3.500 UF
""")

    while True:
        departamento = input("ingrese un departamento:\n").upper()
        if departamento in matriz:

            for i in range(10):
                for j in range(4):
                    if matriz[i, j] == departamento:
                        matriz[i, j] = "X"
                        # costos
                        if matriz[i, 0]:
                            cantidad1 += 1
                            costo = 3800
                            total1 += costo
                        elif matriz[i, 1]:
                            cantidad2 += 1
                            costo = 3000
                            total2 += costo
                        elif matriz[i, 2]:
                            cantidad3 += 1
                            costo = 2800
                            total3 += costo
                        elif matriz[i, 3]:
                            cantidad4 += 1
                            costo = 3500
                            total4 += costo

            break
        else:
            print("El departamento seleccionado no se encuentra disponible")

    rut = ""
    while len(rut) < 3:
        rut = input("Ingrese su rut sin puntos ni guiones (., -):\n")
        if len(rut.strip()) <= 8:
            print("rut no valido")
        else:
            comprador.append(rut)
            break
    print("La operación ha sido exitosa")
    print(
        f"Ha comprado el departamento {departamento}, su costo es de {costo}UF")
    os.system("pause")


def mostrar(matriz):
    os.system("cls")
    print(matriz)
    os.system("pause")


def ver(comprador):
    os.system("cls")
    comprador.sort()
    print("Rut < a > ")
    for i in range(len(comprador)):
        print(comprador[i])
    os.system("pause")


def mostrart(cantidad1, cantidad2, cantidad3, cantidad4, total1, total2, total3, total4):
    total = cantidad1 + cantidad2 + cantidad3 + cantidad4
    tt = total1 + total2 + total3 + total4
    print(
        f"""
 ________________________________________
| Tipo de Departamento | Cantidad |Total |
|________________________________________|
| Tipo A 3800 UF       |{cantidad1}|{total1}|
| Tipo A 3000 UF       |{cantidad2}|{total2}|
| Tipo A 2800 UF       |{cantidad3}|{total3}|
| Tipo A 3500 UF       |{cantidad4}|{total4}|
| Total                |{total}    |{tt}    |
|___________________________________________|
""")
    os.system("pause")
