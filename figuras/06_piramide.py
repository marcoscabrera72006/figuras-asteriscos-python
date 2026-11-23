# ==================================================
#  PIRÁMIDE
# ==================================================
#  Así se ve con n = 4 (los puntos · son espacios):
#
#     ···*          fila 1: 3 espacios, 1 asterisco
#     ··***         fila 2: 2 espacios, 3 asteriscos
#     ·*****        fila 3: 1 espacio,  5 asteriscos
#     *******       fila 4: 0 espacios, 7 asteriscos
#
#  Fórmulas para la fila i (i va de 1 a n):
#     espacios   = n - i        (baja de 1 en 1)
#     asteriscos = 2 * i - 1    (sube de 2 en 2: 1, 3, 5, 7)
# ==================================================

n = int(input("Tamaño de la figura (n): "))

print("Forma 1: bucles anidados")
# ===== FORMA 1: bucles anidados =====
for i in range(1, n + 1):        # i = número de fila: 1, 2, ..., n
    for j in range(n - i):       # primero, n - i espacios
        print(" ", end="")
    for j in range(2 * i - 1):   # después, 2*i - 1 asteriscos
        print("*", end="")
    print()                      # fin de la fila
# ===== FIN FORMA 1 =====

print()
print("Forma 2: forma corta")
# ===== FORMA 2: forma corta =====
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))
# ===== FIN FORMA 2 =====
