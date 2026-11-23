# ==================================================
#  TRIÁNGULO INVERTIDO
# ==================================================
#  Así se ve con n = 4:
#
#     ****      i = 4: 4 asteriscos
#     ***       i = 3: 3 asteriscos
#     **        i = 2: 2 asteriscos
#     *         i = 1: 1 asterisco
#
#  Truco: es el triángulo de antes, pero con i contando
#  hacia atrás. range(n, 0, -1) da n, n-1, ..., 1
#  (el 0 no se incluye).
#
#  Otra forma: dejar i de 1 a n y usar
#     asteriscos = n - i + 1
# ==================================================

n = int(input("Tamaño de la figura (n): "))

print("Forma 1: bucles anidados")
# ===== FORMA 1: bucles anidados =====
for i in range(n, 0, -1):      # i = n, n-1, ..., 1 (cuenta hacia atrás)
    for j in range(i):         # i asteriscos
        print("*", end="")
    print()
# ===== FIN FORMA 1 =====

print()
print("Forma 2: forma corta")
# ===== FORMA 2: forma corta =====
for i in range(n, 0, -1):
    print("*" * i)
# ===== FIN FORMA 2 =====
