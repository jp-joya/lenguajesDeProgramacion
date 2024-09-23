#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_LINE_LENGTH 1024

int count_occurrences(const char *line, const char *key) {
    int count = 0;
    const char *temp = line;
    while ((temp = strstr(temp, key)) != NULL) {
        count++;
        temp += strlen(key); // Move past the last found occurrence
    }
    return count;
}

int main(int argc, char *argv[]) {
    if (argc != 3) {
        fprintf(stderr, "Usage: %s <archivo> <clave>\n", argv[0]);
        return 1;
    }

    const char *filename = argv[1];
    const char *key = argv[2];
    FILE *file = fopen(filename, "r");
    
    if (file == NULL) {
        perror("Error al abrir el archivo");
        return 1;
    }

    char line[MAX_LINE_LENGTH];
    int total_count = 0;

    while (fgets(line, sizeof(line), file)) {
        total_count += count_occurrences(line, key);
    }

    fclose(file);

    printf("La palabra clave '%s' aparece %d veces en el archivo '%s'.\n", key, total_count, filename);

    return 0;
}

