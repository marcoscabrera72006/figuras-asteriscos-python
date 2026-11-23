# ==================================================
#  EJERCICIO 5 (SOLUCIÓN): TABLERO DE AJEDREZ
# ==================================================
#  Así se ve con n = 5 (los puntos · son espacios):
#
#     *·*·*
#     ·*·*
#     *·*·*
#     ·*·*
#     *·*·*
#
#  Casilla por casilla: hay asterisco si i + j es par.
#  En Python, "x es par" se escribe  x % 2 == 0
#  (% da el residuo de la división: 7 % 2 = 1, 8 % 2 = 0).
# ==================================================

n = int(input("Tamaño de la figura (n): "))

print("Casilla por casilla")
# ===== FORMA 1: casilla por casilla =====
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if (i + j) % 2 == 0:      # ¿i + j es par?
            print("*", end="")
        else:
            print(" ", end="")
    print()
# ===== FIN FORMA 1 =====
