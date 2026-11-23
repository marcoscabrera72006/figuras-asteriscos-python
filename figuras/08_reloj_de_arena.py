# ==================================================
#  RELOJ DE ARENA
# ==================================================
#  Así se ve con n = 4 (los puntos · son espacios):
#
#     *******       arriba, i = 4
#     ·*****        arriba, i = 3
#     ··***         arriba, i = 2
#     ···*          arriba, i = 1   <- la cintura
#     ··***         abajo,  i = 2
#     ·*****        abajo,  i = 3
#     *******       abajo,  i = 4
#
#  Truco: es el rombo "al revés". Arriba va una pirámide
#  invertida (i de n a 1) y abajo una pirámide normal
#  (i de 2 a n). Las fórmulas son las de la pirámide:
#     espacios   = n - i
#     asteriscos = 2 * i - 1
#  Abajo empezamos en 2 para no repetir la cintura.
# ==================================================

n = int(input("Tamaño de la figura (n): "))

print("Forma 1: bucles anidados")
# ===== FORMA 1: bucles anidados =====
# Parte de arriba: pirámide invertida (i = n, n-1, ..., 1)
for i in range(n, 0, -1):
    for j in range(n - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        print("*", end="")
    print()
# Parte de abajo: pirámide normal (i = 2, 3, ..., n)
for i in range(2, n + 1):
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
for i in range(2, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))
# ===== FIN FORMA 2 =====
