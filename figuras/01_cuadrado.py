# ==================================================
#  CUADRADO LLENO
# ==================================================
#  Así se ve con n = 4:
#
#     ****      fila 1: 4 asteriscos
#     ****      fila 2: 4 asteriscos
#     ****      fila 3: 4 asteriscos
#     ****      fila 4: 4 asteriscos
#
#  Fórmula para la fila i (i va de 1 a n):
#     asteriscos = n      (todas las filas son iguales)
# ==================================================

n = int(input("Tamaño de la figura (n): "))

print("Forma 1: bucles anidados")
# ===== FORMA 1: bucles anidados =====
for i in range(1, n + 1):      # una vuelta por cada fila
    for j in range(n):         # n asteriscos en esta fila
        print("*", end="")     # end="" -> no salta de línea
    print()                    # fin de la fila: ahora sí saltamos
# ===== FIN FORMA 1 =====

print()
print("Forma 2: forma corta")
# ===== FORMA 2: forma corta =====
for i in range(1, n + 1):
    print("*" * n)             # "*" * 4 da "****"
# ===== FIN FORMA 2 =====
