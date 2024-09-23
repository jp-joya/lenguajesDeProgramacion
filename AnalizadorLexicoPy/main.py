import sys
from lexer import lex

def write_tokens_to_file(tokens, output_file):
    with open(output_file, 'w') as f:
        for token in tokens:
            if len(token) == 3:
                f.write(f'<{token[0]},{token[1]},{token[2]}>\n')
            else:
                f.write(f'<{token[0]},{token[1]},{token[2]},{token[3]}>\n')

# Función principal
def main():
    if len(sys.argv) != 3:
        print("Uso: python main.py <archivo_entrada> <archivo_salida>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    tokens = lex(input_file)  # Aquí pasamos el nombre del archivo de entrada
    if tokens:
        write_tokens_to_file(tokens, output_file)  # Aquí pasamos el nombre del archivo de salida

if __name__ == "__main__":
    main()
