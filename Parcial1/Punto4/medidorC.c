#include <stdio.h>
#include <time.h>

int main() {
    clock_t inicio, final;
    double tiempo;
  
    int n =100000000;
    inicio = clock();

    for (long i = 0; i < n; i++);

    final = clock();
    tiempo = ((double) (final - inicio)) / CLOCKS_PER_SEC;
    printf("Tiempo de ejecución en C: %f segundos\n", tiempo);

    return 0;
}

