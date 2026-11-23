# ==================================================
#  EJERCICIO 1: LETRA M (Método 2, casilla por casilla)
# ==================================================
#  Cuadrícula de n x n (n impar). Hay asterisco si:
#     j == 1                 -> palo izquierdo
#     j == n                 -> palo derecho
#     j == i  o  j == n-i+1  -> las dos diagonales...
#     ...pero SOLO en la mitad de arriba (i <= centro),
#     para que se junten en el medio y formen la V de la M.
# ==================================================

n = int(input("Tamaño impar de la M (n): "))
while n % 2 == 0:
    n = int(input("Tiene que ser impar. Tamaño (n): "))

centro = (n + 1) // 2                  # con n = 7, centro = 4

for i in range(1, n + 1):              # i = fila
    for j in range(1, n + 1):          # j = columna
        palos = j == 1 or j == n
        v = i <= centro and (j == i or j == n - i + 1)
        if palos or v:
            print("*", end="")
        else:
            print(" ", end="")
    print()
