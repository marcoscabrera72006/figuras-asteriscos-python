# ==================================================
#  ROMBO (DIAMANTE)
# ==================================================
#  Así se ve con n = 4 (los puntos · son espacios):
#
#     ···*          arriba, i = 1
#     ··***         arriba, i = 2
#     ·*****        arriba, i = 3
#     *******       arriba, i = 4   <- la fila más ancha
#     ·*****        abajo,  i = 3
#     ··***         abajo,  i = 2
#     ···*          abajo,  i = 1
#
#  Truco: es una pirámide (i de 1 a n) y debajo la MISMA
#  pirámide al revés (i de n-1 a 1). Las fórmulas no cambian:
#     espacios   = n - i
#     asteriscos = 2 * i - 1
#  Abajo empezamos en n-1 para no repetir la fila del medio.
# ==================================================

n = int(input("Tamaño de la figura (n): "))

print("Forma 1: bucles anidados")
# ===== FORMA 1: bucles anidados =====
# Parte de arriba: una pirámide (i = 1, 2, ..., n)
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        print("*", end="")
    print()
# Parte de abajo: la misma pirámide al revés (i = n-1, ..., 1)
for i in range(n - 1, 0, -1):
    for j in range(n - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        print("*", end="")
    print()
# ===== FIN FORMA 1 =====

print()
print("Forma 2: forma corta")
# ===== FORMA 2: forma corta =====
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))
# ===== FIN FORMA 2 =====
