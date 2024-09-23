grammar Trig;

parse
    : expr EOF
    ;

expr
    : function '(' number ')'
    ;

function
    : 'Sin'
    | 'Cos'
    | 'Tan'
    ;

number
    : DIGIT+ ('.' DIGIT+)?
    ;

fragment DIGIT
    : '0'..'9'
    ;

