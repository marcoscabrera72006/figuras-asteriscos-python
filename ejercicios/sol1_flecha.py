# ==================================================
#  EJERCICIO 1 (SOLUCIÓN): FLECHA HACIA LA DERECHA
# ==================================================
#  Así se ve con n = 4:
#
#     *         arriba, i = 1
#     **        arriba, i = 2
#     ***       arriba, i = 3
#     ****      arriba, i = 4   <- la punta
#     ***       abajo,  i = 3
#     **        abajo,  i = 2
#     *         abajo,  i = 1
#
#  Es un triángulo que crece (i de 1 a n) y otro que
#  decrece (i de n-1 a 1). En los dos: asteriscos = i
# ==================================================

n = int(input("Tamaño de la figura (n): "))

print("Forma 1: bucles anidados")
# ===== FORMA 1: bucles anidados =====
for i in range(1, n + 1):          # el triángulo que crece
    for j in range(i):
        print("*", end="")
    print()
for i in range(n - 1, 0, -1):      # el triángulo que decrece
    for j in range(i):
        print("*", end="")
    print()
# ===== FIN FORMA 1 =====

print()
print("Forma 2: forma corta")
# ===== FORMA 2: forma corta =====
for i in range(1, n + 1):
    print("*" * i)
for i in range(n - 1, 0, -1):
    print("*" * i)
# ===== FIN FORMA 2 =====
