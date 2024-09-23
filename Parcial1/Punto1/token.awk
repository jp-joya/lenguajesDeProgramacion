# token.awk

# Reglas para el token INCR
/\+\+/ {
    print "TOKEN INCR"
    next
}

# Reglas para el token SUMA
/\+/ {
    print "TOKEN SUMA"
    next
}

# Reglas para el token ENTERO
/^[0-9]+$/ {
    print "TOKEN ENTERO"
    next
}

# Reglas para el token REAL
/^[0-9]+\.[0-9]+$/ {
    print "TOKEN REAL"
    next
}

# Caso por defecto para cualquier otro input
{
    print "TOKEN DESCONOCIDO"
}

