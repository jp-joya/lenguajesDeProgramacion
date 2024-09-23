import time

comienzo = time.time()

#cambiar n para medir.
n=100000000
for i in range(n):
    pass

final = time.time()
print(f"Tiempo de ejecución en Python: {final - comienzo} segundos")

