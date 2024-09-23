%{
#include <stdio.h>
#include <stdlib.h>

void yyerror(const char *s);
int yylex(void);
%}

%option noyywrap

// Definiciones de tokens
IDENTIFIER [a-zA-Z_][a-zA-Z0-9_]*
NUMBER [0-9]+
WHITESPACE [ \t\n]+

%%

{IDENTIFIER}      { /* Detecta identificadores */ }
lambda            { /* Detecta la palabra clave lambda */ }
:                 { /* Detecta el separador ':' */ }
\*\*              { /* Detecta el operador '**' */ }
=                 { /* Detecta el signo '=' */ }
{NUMBER}          { /* Detecta números */ }
{WHITESPACE}      { /* Ignora espacios en blanco y saltos de línea */ }

.                 { /* Cualquier otro carácter no reconocido */ }

%%

void yyerror(const char *s) {
    fprintf(stderr, "Error: %s\n", s);
}

int main(int argc, char **argv) {
    if (argc < 2) {
        fprintf(stderr, "Usage: %s <file>\n", argv[0]);
        exit(1);
    }

    FILE *file = fopen(argv[1], "r");
    if (!file) {
        perror("Error opening file");
        exit(1);
    }

    yyin = file;
    yylex();  // Analiza el archivo
    fclose(file);

    return 0;
}

