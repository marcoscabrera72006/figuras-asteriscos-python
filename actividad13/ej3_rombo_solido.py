# ==================================================
#  EJERCICIO 3: ROMBO SÓLIDO (Método 1, contar por fila)
# ==================================================
#  Una pirámide (i de 1 a n) y debajo la misma al revés
#  (i de n-1 a 1). En cada fila:
#     espacios   = n - i
#     asteriscos = 2 * i - 1
#  Altura total: n + (n - 1) = 2n - 1 filas.
# ==================================================

n = int(input("Tamaño del rombo (n): "))

for i in range(1, n + 1):              # mitad de arriba
    print(" " * (n - i) + "*" * (2 * i - 1))

for i in range(n - 1, 0, -1):          # mitad de abajo
    print(" " * (n - i) + "*" * (2 * i - 1))
