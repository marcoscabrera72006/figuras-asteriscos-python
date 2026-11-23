# ==================================================
#  EJERCICIO 5: ESTRELLA CON CRUZ (Método 2, casilla por casilla)
# ==================================================
#  Cuadrícula de n x n (n impar). Hay asterisco si:
#     i == centro  -> línea horizontal
#     j == centro  -> línea vertical
#     j == i       -> diagonal  \
#     j == n-i+1   -> diagonal  /
# ==================================================

n = int(input("Tamaño impar de la estrella (n): "))
while n % 2 == 0:
    n = int(input("Tiene que ser impar. Tamaño (n): "))

centro = (n + 1) // 2                  # con n = 13, centro = 7

for i in range(1, n + 1):              # i = fila
    for j in range(1, n + 1):          # j = columna
        cruz = i == centro or j == centro
        diagonal = j == i or j == n - i + 1
        if cruz or diagonal:
            print("*", end="")
        else:
            print(" ", end="")
    print()
