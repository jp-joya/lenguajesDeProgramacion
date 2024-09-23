%{
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void yyerror(const char *s);
int yylex(void);

%}

%union {
    double val;
}

%token <val> NUMBER
%token ADD SUB MUL DIV EXP ABS OP CP EOL

%left ADD SUB
%left MUL DIV
%left EXP
%left ABS
%right UMINUS

%type <val> expr

%%

calculo:
    /* vacío */
    | calculo linea
    ;

linea:
    expr EOL    { printf("Resultado: %.2f\n", $1); }
    | EOL
    ;

expr:
    NUMBER          { $$ = $1; }
    | expr ADD expr { $$ = $1 + $3; }
    | expr SUB expr { $$ = $1 - $3; }
    | expr MUL expr { $$ = $1 * $3; }
    | expr DIV expr {
        if ($3 == 0) {
            yyerror("Error: División por cero");
            $$ = 0;  // or handle this case as needed
        } else {
            $$ = $1 / $3;
        }
    }
    | expr EXP expr { $$ = pow($1, $3); } // Handling exponentiation
    | SUB expr %prec UMINUS { $$ = -$2; }
    | OP expr CP    { $$ = $2; }
    | ABS expr ABS  { $$ = fabs($2); }
    ;

%%

void yyerror(const char *s) {
    fprintf(stderr, "%s\n", s);
}

int main(void) {
    printf("Ingrese una expresión matemática:\n");
    return yyparse();
}

