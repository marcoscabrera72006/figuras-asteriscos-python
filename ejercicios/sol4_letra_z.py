# ==================================================
#  EJERCICIO 4 (SOLUCIÓN): LETRA Z
# ==================================================
#  Así se ve con n = 5 (los puntos · son espacios):
#
#     *****
#     ···*
#     ··*
#     ·*
#     *****
#
#  Casilla por casilla (fila i, columna j), hay asterisco si:
#     i == 1           (la raya de arriba)
#     i == n           (la raya de abajo)
#     j == n - i + 1   (la diagonal  /  )
# ==================================================

n = int(input("Tamaño de la figura (n): "))

print("Casilla por casilla")
# ===== FORMA 1: casilla por casilla =====
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == 1 or i == n or j == n - i + 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
# ===== FIN FORMA 1 =====
