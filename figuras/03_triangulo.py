# ==================================================
#  TRIÁNGULO RECTÁNGULO
# ==================================================
#  Así se ve con n = 4:
#
#     *         fila 1: 1 asterisco
#     **        fila 2: 2 asteriscos
#     ***       fila 3: 3 asteriscos
#     ****      fila 4: 4 asteriscos
#
#  Fórmula para la fila i (i va de 1 a n):
#     asteriscos = i      (la fila 3 tiene 3 asteriscos)
# ==================================================

n = int(input("Tamaño de la figura (n): "))

print("Forma 1: bucles anidados")
# ===== FORMA 1: bucles anidados =====
for i in range(1, n + 1):      # i = 1, 2, 3, ..., n
    for j in range(i):         # en la fila i van i asteriscos
        print("*", end="")
    print()
# ===== FIN FORMA 1 =====

print()
print("Forma 2: forma corta")
# ===== FORMA 2: forma corta =====
for i in range(1, n + 1):
    print("*" * i)
# ===== FIN FORMA 2 =====
