# ==================================================
#  EJERCICIO 4: CUADRADO CON BORDE, DIAGONALES Y CUADRO INTERNO HUECO
# ==================================================
#  Cuadrícula de n x n. Tres piezas, unidas con or:
#     borde     -> primera/última fila o columna
#     diagonal  -> j == i  o  j == n - i + 1
#     interno   -> el borde de un cuadrado más chico, centrado,
#                  que va de la casilla a hasta la b
# ==================================================

n = int(input("Lado del cuadrado (n): "))

a = n // 4 + 1                         # con n = 9: el cuadro de adentro empieza en 3...
b = n - n // 4                         # ...y termina en 7

for i in range(1, n + 1):              # i = fila
    for j in range(1, n + 1):          # j = columna
        borde = i == 1 or i == n or j == 1 or j == n
        diagonal = j == i or j == n - i + 1
        interno = ((i == a or i == b) and a <= j <= b) or ((j == a or j == b) and a <= i <= b)
        if borde or diagonal or interno:
            print("*", end="")
        else:
            print(" ", end="")
    print()
