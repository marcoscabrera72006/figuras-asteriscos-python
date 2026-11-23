# ==================================================
#  CUADRADO HUECO
# ==================================================
#  Así se ve con n = 5 (los puntos · son espacios):
#
#     *****     fila 1: borde de arriba, todo lleno
#     *···*     filas del medio: borde, hueco, borde
#     *···*
#     *···*
#     *****     fila n: borde de abajo, todo lleno
#
#  Regla para la casilla (fila i, columna j):
#     hay asterisco si  i == 1  o  i == n  o  j == 1  o  j == n
#     (es decir: si la casilla está en el borde)
# ==================================================

n = int(input("Tamaño de la figura (n): "))

print("Forma 1: casilla por casilla")
# ===== FORMA 1: casilla por casilla =====
for i in range(1, n + 1):          # i = fila
    for j in range(1, n + 1):      # j = columna
        if i == 1 or i == n or j == 1 or j == n:   # ¿estoy en el borde?
            print("*", end="")
        else:
            print(" ", end="")
    print()
# ===== FIN FORMA 1 =====

print()
print("Forma 2: forma corta")
# ===== FORMA 2: forma corta =====
for i in range(1, n + 1):
    if i == 1 or i == n:                    # primera y última fila: llenas
        print("*" * n)
    else:                                   # filas del medio
        print("*" + " " * (n - 2) + "*")    # borde + hueco + borde
# ===== FIN FORMA 2 =====
