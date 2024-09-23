 # Palabras reservadas de Python
reserved_words = {
    'False', 'await', 'else', 'import', 'pass',
    'None', 'break', 'except', 'in', 'raise',
    'True', 'class', 'finally', 'is', 'return',
    'and', 'continue', 'for', 'lambda', 'try',
    'as', 'def', 'from', 'nonlocal', 'while',
    'assert', 'del', 'global', 'not', 'with',
    'async', 'elif', 'if', 'or', 'yield','range'
}

# Palabras claves suaves
soft_keywords = {'match', 'case', 'type', '_'}

# Operadores
operators = {
    '+', '-', '*', '**', '/', '//', '%', '@',
    '<<', '>>', '&', '|', '^', '~', ':=',
    '<', '>', '<=', '>=', '==', '!=',"!"
}

# Delimitadores
delimiters = {
    '(', ')', '[', ']', '{', '}', ',', ':', '.', ';', '@', '=',
    '->', '+=', '-=', '*=', '/=', '//=', '%=', '@=', '&=', '|=', '^=',
    '>>=', '<<=', '**='
}

# Identificar tipos de caracteres
def is_digit(c):
    return '0' <= c <= '9'

def is_letter(c):
    return 'a' <= c <= 'z' or 'A' <= c <= 'Z'

def is_whitespace(c):
    return c in ' \t'

def is_operator(c):
    return c in operators

def is_delimiter(c):
    return c in delimiters

def is_valid_start(c):
    return is_letter(c) or c == '_'

def is_valid_identifier(s):
    return s[0] == '_' or is_letter(s[0])

# Analizador léxico
def lex(file_input):
    with open(file_input, 'r') as file:
        content = file.read()

    tokens = []
    i = 0
    line_num = 1
    column_num = 1

    while i < len(content):
        char = content[i]

        # Ignorar espacios en blanco y tabulaciones
        if is_whitespace(char):
            column_num += 1
            i += 1
            continue

        # Saltos de línea
        if char == '\n':
            line_num += 1
            column_num = 1
            i += 1
            continue

        # Comentarios (ignorar línea)
        if char == '#':
            while i < len(content) and content[i] != '\n':
                i += 1
            continue

        # Palabras reservadas y identificadores
        if is_letter(char) or char == '_':
            start = i
            while i < len(content) and (is_letter(content[i]) or is_digit(content[i]) or content[i] == '_'):
                i += 1
            lexeme = content[start:i]
            if not is_valid_identifier(lexeme):
                # Identificador no válido (empieza con un número)
                print(f'>>> Error léxico (línea {line_num}, posición {column_num}): identificador no válido "{lexeme}".')
                tokens.append(('tk_error', f'identificador no válido: {lexeme}', line_num, column_num))
            elif lexeme in reserved_words:
                tokens.append((lexeme, line_num, column_num))
            elif lexeme in soft_keywords:
                tokens.append(('tk_soft_keyword', lexeme, line_num, column_num))
            else:
                tokens.append(('id', lexeme, line_num, column_num))
            column_num += (i - start)
            continue

        # Números enteros y flotantes
        if is_digit(char):
            start = i
            is_float = False
            while i < len(content) and is_digit(content[i]):
                i += 1
            if i < len(content) and content[i] == '.':
                is_float = True
                i += 1
                while i < len(content) and is_digit(content[i]):
                    i += 1
            if i < len(content) and (content[i] == 'e' or content[i] == 'E'):
                is_float = True
                i += 1
                if content[i] == '+' or content[i] == '-':
                    i += 1
                while i < len(content) and is_digit(content[i]):
                    i += 1
            lexeme = content[start:i]
            token_type = 'tk_float' if is_float else 'tk_entero'
            tokens.append((token_type, lexeme, line_num, column_num))
            column_num += (i - start)
            continue

        # Literales imaginarios
        if is_digit(char) or char == '.':
            start = i
            while i < len(content) and (is_digit(content[i]) or content[i] == '.'):
                i += 1
            if i < len(content) and (content[i] == 'j' or content[i] == 'J'):
                i += 1
                tokens.append(('tk_imag', content[start:i], line_num, column_num))
                column_num += (i - start)
            else:
                lexeme = content[start:i]
                token_type = 'tk_float' if '.' in lexeme else 'tk_entero'
                tokens.append((token_type, lexeme, line_num, column_num))
            continue

        # Operadores
        if char in operators:
            start = i
            i += 1
            while i < len(content) and content[start:i] in operators:
                i += 1
            lexeme = content[start:i-1]
            tokens.append((f'tk_op_{lexeme}', line_num, column_num))
            column_num += (i - start)
            continue

        # Delimitadores
        if char in delimiters:
            tokens.append((f'tk_delim_{char}', line_num, column_num))
            column_num += 1
            i += 1
            continue

        # Cadenas de texto (entre comillas)
        if char == '"':
            start = i
            i += 1
            while i < len(content) and content[i] != '"':
                i += 1
            if i < len(content):  # Si encontramos la comilla de cierre
                i += 1  # Cerrar la comilla
                lexeme = content[start:i]
                tokens.append(('tk_cadena', lexeme, line_num, column_num))
                column_num += (i - start)
            else:
                # Error de cadena incompleta
                print(f'>>> Error léxico (línea {line_num}, posición {column_num}): cadena de texto sin cierre.')
                tokens.append(('tk_error', 'cadena sin cierre', line_num, column_num))
            continue
        if char == "'":
            start = i
            i += 1
            while i < len(content) and content[i] != "'":
                i += 1
            if i < len(content):  # Si encontramos la comilla de cierre
                i += 1  # Cerrar la comilla
                lexeme = content[start:i]
                tokens.append(('tk_cadena', lexeme, line_num, column_num))
                column_num += (i - start)
            else:
                # Error de cadena incompleta
                print(f'>>> Error léxico (línea {line_num}, posición {column_num}): cadena de texto sin cierre.')
                tokens.append(('tk_error', 'cadena sin cierre', line_num, column_num))
            continue



        # Error léxico para caracteres no reconocidos
        if char.isprintable() and not (is_whitespace(char) or is_letter(char) or is_digit(char) or is_operator(char) or is_delimiter(char)):
            print(f'>>> Error léxico (línea {line_num}, posición {column_num}): caracter no reconocido "{char}".')
            tokens.append(('tk_error', f'caracter no reconocido: {char}', line_num, column_num))
            i += 1
            column_num += 1
            continue

        # Manejo de error general
        print(f'>>> Error léxico (línea {line_num}, posición {column_num}): caracter no reconocido.')
        i += 1
        column_num += 1

    return tokens

def write_tokens_to_file(tokens, output_file):
    with open(output_file, 'w') as f:
        for token in tokens:
            if len(token) == 3:
                f.write(f'<{token[0]},{token[1]},{token[2]}>\n')
            else:
                f.write(f'<{token[0]},{token[1]},{token[2]},{token[3]}>\n')
