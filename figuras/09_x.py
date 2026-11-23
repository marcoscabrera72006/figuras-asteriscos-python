# ==================================================
#  LETRA X
# ==================================================
#  Así se ve con n = 5 (los puntos · son espacios):
#
#     *···*
#     ·*·*
#     ··*
#     ·*·*
#     *···*
#
#  Aquí contar espacios por fila es incómodo, así que
#  decidimos casilla por casilla (fila i, columna j):
#     diagonal  \  :  j == i
#     diagonal  /  :  j == n - i + 1
#  Usa un n impar (3, 5, 7...) para que la X tenga centro.
# ==================================================

n = int(input("Tamaño de la figura (n): "))

print("Casilla por casilla")
# ===== FORMA 1: casilla por casilla =====
for i in range(1, n + 1):              # i = fila
    for j in range(1, n + 1):          # j = columna
        if j == i or j == n - i + 1:   # ¿estoy en alguna diagonal?
            print("*", end="")
        else:
            print(" ", end="")
    print()
# ===== FIN FORMA 1 =====
