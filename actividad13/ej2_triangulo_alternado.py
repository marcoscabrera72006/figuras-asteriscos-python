# ==================================================
#  EJERCICIO 2: TRIÁNGULO INVERTIDO CON BORDE Y RELLENO ALTERNADO
# ==================================================
#  La fila i mide n - i + 1 casillas (cada fila, una menos).
#  Hay asterisco si:
#     i == 1 o j == 1 o j == ancho   -> el borde del triángulo
#     i par  y  j impar              -> relleno: en las filas pares,
#                                       un asterisco sí y otro no
#  Las filas impares quedan vacías por dentro.
# ==================================================

n = int(input("Altura del triángulo (n): "))

for i in range(1, n + 1):              # i = fila
    ancho = n - i + 1                  # cuántas casillas tiene esta fila
    for j in range(1, ancho + 1):      # j = columna, de 1 a ancho
        borde = i == 1 or j == 1 or j == ancho
        relleno = i % 2 == 0 and j % 2 == 1
        if borde or relleno:
            print("*", end="")
        else:
            print(" ", end="")
    print()
