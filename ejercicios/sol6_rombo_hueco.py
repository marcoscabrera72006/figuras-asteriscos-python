# ==================================================
#  EJERCICIO 6 (SOLUCIÓN): ROMBO HUECO
# ==================================================
#  Así se ve con n = 4 (los puntos · son espacios):
#
#     ···*          arriba, i = 1
#     ··*·*         arriba, i = 2
#     ·*···*        arriba, i = 3
#     *·····*       arriba, i = 4
#     ·*···*        abajo,  i = 3
#     ··*·*         abajo,  i = 2
#     ···*          abajo,  i = 1
#
#  Es el rombo (arriba i de 1 a n, abajo i de n-1 a 1), pero
#  cada fila solo tiene los dos bordes, como la pirámide hueca:
#     espacios de la izquierda = n - i
#     la fila mide 2*i - 1 y hay asterisco si j == 1 o j == 2*i - 1
#  Ojo: aquí ninguna fila va llena, ni siquiera la del medio.
# ==================================================

n = int(input("Tamaño de la figura (n): "))

print("Forma 1: bucles anidados")
# ===== FORMA 1: bucles anidados =====
for i in range(1, n + 1):                  # mitad de arriba
    for j in range(n - i):
        print(" ", end="")
    for j in range(1, 2 * i):
        if j == 1 or j == 2 * i - 1:       # solo los dos bordes
            print("*", end="")
        else:
            print(" ", end="")
    print()
for i in range(n - 1, 0, -1):              # mitad de abajo
    for j in range(n - i):
        print(" ", end="")
    for j in range(1, 2 * i):
        if j == 1 or j == 2 * i - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
# ===== FIN FORMA 1 =====

print()
print("Forma 2: forma corta")
# ===== FORMA 2: forma corta =====
for i in range(1, n + 1):
    if i == 1:
        print(" " * (n - 1) + "*")
    else:
        print(" " * (n - i) + "*" + " " * (2 * i - 3) + "*")
for i in range(n - 1, 0, -1):
    if i == 1:
        print(" " * (n - 1) + "*")
    else:
        print(" " * (n - i) + "*" + " " * (2 * i - 3) + "*")
# ===== FIN FORMA 2 =====
