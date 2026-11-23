# ==================================================
#  TRIÁNGULO ALINEADO A LA DERECHA
# ==================================================
#  Así se ve con n = 4 (los puntos · son espacios):
#
#     ···*      fila 1: 3 espacios, 1 asterisco
#     ··**      fila 2: 2 espacios, 2 asteriscos
#     ·***      fila 3: 1 espacio,  3 asteriscos
#     ****      fila 4: 0 espacios, 4 asteriscos
#
#  Fórmulas para la fila i (i va de 1 a n):
#     espacios   = n - i
#     asteriscos = i
# ==================================================

n = int(input("Tamaño de la figura (n): "))

print("Forma 1: bucles anidados")
# ===== FORMA 1: bucles anidados =====
for i in range(1, n + 1):
    for j in range(n - i):     # primero los espacios: n - i
        print(" ", end="")
    for j in range(i):         # después los asteriscos: i
        print("*", end="")
    print()
# ===== FIN FORMA 1 =====

print()
print("Forma 2: forma corta")
# ===== FORMA 2: forma corta =====
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * i)    # el + pega los dos textos
# ===== FIN FORMA 2 =====
