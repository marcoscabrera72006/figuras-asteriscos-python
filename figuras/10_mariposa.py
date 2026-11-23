# ==================================================
#  MARIPOSA
# ==================================================
#  Así se ve con n = 4 (los puntos · son espacios):
#
#     *······*      arriba, i = 1: 1 ast, 6 esp, 1 ast
#     **····**      arriba, i = 2: 2 ast, 4 esp, 2 ast
#     ***··***      arriba, i = 3: 3 ast, 2 esp, 3 ast
#     ********      arriba, i = 4: 4 ast, 0 esp, 4 ast
#     ***··***      abajo,  i = 3
#     **····**      abajo,  i = 2
#     *······*      abajo,  i = 1
#
#  Cada fila tiene 3 partes: ala izquierda, hueco, ala derecha.
#     ala izquierda = i asteriscos
#     hueco         = 2 * (n - i) espacios
#     ala derecha   = i asteriscos
#  Arriba i va de 1 a n; abajo, de n-1 a 1 (igual que el rombo).
#
#  Si tu profe la quiere con DOS filas llenas en el centro,
#  cambia range(n - 1, 0, -1) por range(n, 0, -1).
# ==================================================

n = int(input("Tamaño de la figura (n): "))

print("Forma 1: bucles anidados")
# ===== FORMA 1: bucles anidados =====
# Parte de arriba (i = 1, 2, ..., n)
for i in range(1, n + 1):
    for j in range(i):                 # ala izquierda
        print("*", end="")
    for j in range(2 * (n - i)):       # hueco del centro
        print(" ", end="")
    for j in range(i):                 # ala derecha
        print("*", end="")
    print()
# Parte de abajo (i = n-1, ..., 1): lo mismo al revés
for i in range(n - 1, 0, -1):
    for j in range(i):
        print("*", end="")
    for j in range(2 * (n - i)):
        print(" ", end="")
    for j in range(i):
        print("*", end="")
    print()
# ===== FIN FORMA 1 =====

print()
print("Forma 2: forma corta")
# ===== FORMA 2: forma corta =====
for i in range(1, n + 1):
    print("*" * i + " " * (2 * (n - i)) + "*" * i)
for i in range(n - 1, 0, -1):
    print("*" * i + " " * (2 * (n - i)) + "*" * i)
# ===== FIN FORMA 2 =====
