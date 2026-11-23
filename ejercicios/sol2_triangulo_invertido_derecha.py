# ==================================================
#  EJERCICIO 2 (SOLUCIÓN): TRIÁNGULO INVERTIDO A LA DERECHA
# ==================================================
#  Así se ve con n = 4 (los puntos · son espacios):
#
#     ****      i = 4: 0 espacios, 4 asteriscos
#     ·***      i = 3: 1 espacio,  3 asteriscos
#     ··**      i = 2: 2 espacios, 2 asteriscos
#     ···*      i = 1: 3 espacios, 1 asterisco
#
#  Es el triángulo alineado a la derecha, pero con i
#  contando hacia atrás (de n a 1). Mismas fórmulas:
#     espacios   = n - i
#     asteriscos = i
# ==================================================

n = int(input("Tamaño de la figura (n): "))

print("Forma 1: bucles anidados")
# ===== FORMA 1: bucles anidados =====
for i in range(n, 0, -1):
    for j in range(n - i):
        print(" ", end="")
    for j in range(i):
        print("*", end="")
    print()
# ===== FIN FORMA 1 =====

print()
print("Forma 2: forma corta")
# ===== FORMA 2: forma corta =====
for i in range(n, 0, -1):
    print(" " * (n - i) + "*" * i)
# ===== FIN FORMA 2 =====
