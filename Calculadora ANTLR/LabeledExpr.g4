grammar LabeledExpr;

// Reglas de la gramática

stat: expr NEWLINE               // Primera regla: Una expresión seguida de un salto de línea
    | ID '=' expr NEWLINE        // Segunda regla: Una asignación seguida de un salto de línea
    | NEWLINE                    // Tercera regla: Un salto de línea solo
    ;
    
expr: expr op=('*'|'/') expr     // multiplicación o división
    | expr op=('+'|'-') expr     // suma o resta
    | expr op='^' expr           // potenciación
    | 'sqrt(' expr ')'           // Expresión con raíz cuadrada
    | INT                        // Un número entero
    | ID                         // Un identificador
    | '(' expr ')'               // Una expresión entre paréntesis
    ;

// Definición de tokens
MUL : '*' ;        // Operador de multiplicación
DIV : '/' ;        // Operador de división
ADD : '+' ;        // Operador de suma
SUB : '-' ;        // Operador de resta
POW : '^' ;        // Operador de potenciación
SQRT : 'sqrt' ;    // Función de raíz cuadrada
