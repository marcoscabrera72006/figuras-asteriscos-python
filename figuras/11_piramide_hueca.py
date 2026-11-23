# ==================================================
#  PIRÁMIDE HUECA (combina los dos métodos)
# ==================================================
#  Así se ve con n = 4 (los puntos · son espacios):
#
#     ···*          fila 1: la punta
#     ··*·*         fila 2: borde, hueco, borde
#     ·*···*        fila 3: borde, hueco, borde
#     *******       fila 4: la base, llena
#
#  Método 1 para los espacios de la izquierda:  n - i
#  Método 2 para el resto de la fila: la fila mide 2*i - 1,
#  y en la posición j hay asterisco si
#     j == 1  (borde izquierdo)
#     j == 2 * i - 1  (borde derecho)
#     i == n  (la base va llena)
# ==================================================

n = int(input("Tamaño de la figura (n): "))

print("Forma 1: bucles anidados")
# ===== FORMA 1: bucles anidados =====
for i in range(1, n + 1):
    for j in range(n - i):                       # espacios de la izquierda
        print(" ", end="")
    for j in range(1, 2 * i):                    # j = 1, 2, ..., 2*i - 1
        if j == 1 or j == 2 * i - 1 or i == n:   # borde o base
            print("*", end="")
        else:
            print(" ", end="")
    print()
# ===== FIN FORMA 1 =====

print()
print("Forma 2: forma corta")
# ===== FORMA 2: forma corta =====
for i in range(1, n + 1):
    if i == 1:
        print(" " * (n - 1) + "*")                              # la punta
    elif i == n:
        print("*" * (2 * n - 1))                                # la base
    else:
        print(" " * (n - i) + "*" + " " * (2 * i - 3) + "*")    # borde, hueco, borde
# ===== FIN FORMA 2 =====
