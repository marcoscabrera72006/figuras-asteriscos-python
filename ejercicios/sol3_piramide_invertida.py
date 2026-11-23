# ==================================================
#  EJERCICIO 3 (SOLUCIÓN): PIRÁMIDE INVERTIDA
# ==================================================
#  Así se ve con n = 4 (los puntos · son espacios):
#
#     *******       i = 4: 0 espacios, 7 asteriscos
#     ·*****        i = 3: 1 espacio,  5 asteriscos
#     ··***         i = 2: 2 espacios, 3 asteriscos
#     ···*          i = 1: 3 espacios, 1 asterisco
#
#  Es la pirámide con i contando hacia atrás. Mismas fórmulas:
#     espacios   = n - i
#     asteriscos = 2 * i - 1
#  (Es justo la mitad de arriba del reloj de arena.)
# ==================================================

n = int(input("Tamaño de la figura (n): "))

print("Forma 1: bucles anidados")
# ===== FORMA 1: bucles anidados =====
for i in range(n, 0, -1):
    for j in range(n - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        print("*", end="")
    print()
# ===== FIN FORMA 1 =====

print()
print("Forma 2: forma corta")
# ===== FORMA 2: forma corta =====
for i in range(n, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))
# ===== FIN FORMA 2 =====
