import networkx as nx
import matplotlib.pyplot as plt
import re

# Leer la gramática desde un archivo
def leer_gramatica(archivo):
    with open(archivo, 'r') as file:
        gramatica = {}
        simbolo_inicial = None

        for linea in file:
            linea = linea.strip()
            if '->' in linea:
                izquierda, derecha = linea.split('->')
                izquierda = izquierda.strip()

                # Si el símbolo inicial no está definido, tomar el primer símbolo
                if simbolo_inicial is None:
                    simbolo_inicial = izquierda

                producciones = [prod.strip() for prod in derecha.split('|')]
                gramatica[izquierda] = producciones

        return gramatica, simbolo_inicial

# Construir el árbol desde la gramática
def construir_arbol(gramatica, simbolo_inicial, G, nodo_padre=None, profundidad=0, profundidad_maxima=10):
    if profundidad > profundidad_maxima:
        return

    if nodo_padre is None:
        nodo_padre = simbolo_inicial
        G.add_node(nodo_padre)

    producciones = gramatica.get(simbolo_inicial, [])

    for produccion in producciones:
        for nodo_hijo in produccion.split():
            G.add_node(nodo_hijo)
            G.add_edge(nodo_padre, nodo_hijo)

            if nodo_hijo in gramatica:
                construir_arbol(gramatica, nodo_hijo, G, nodo_hijo, profundidad + 1, profundidad_maxima)

def mostrar_arbol(G):
    #pos = nx.kamada_kawai_layout(G)
    pos = nx.spectral_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', font_weight='bold', node_size=3000)
    plt.show()

# Evaluar si una parte de la cadena coincide con una expresión regular
def evaluar_expresion_regular(expresion, cadena):
    try:
        # Intentar hacer una coincidencia desde el principio
        match = re.match(expresion, cadena)
        if match:
            return match.group(0), cadena[match.end():]  # Devuelve la coincidencia y la cadena restante
        return None, cadena
    except re.error:
        return None, cadena

# Función principal para verificar si una cadena es aceptada por la gramática
def verificar_cadena(gramatica, simbolo_inicial, cadena):
    def analizar(symbol, cadena_restante):
        # Si llegamos al final de la cadena y el símbolo es vacío
        if symbol == '' and cadena_restante == '':
            return True
        if symbol not in gramatica:
            # Si el símbolo es una expresión regular, evaluarlo
            match, cadena_restante = evaluar_expresion_regular(symbol, cadena_restante)
            return match is not None

        # Probar cada producción para este símbolo
        for produccion in gramatica[symbol]:
            cadena_actual = cadena_restante
            valido = True

            # Dividimos la producción en partes
            for parte in produccion.split():
                match, cadena_actual = evaluar_expresion_regular(parte, cadena_actual)
                if not match:
                    valido = False
                    break

            if valido and cadena_actual == '':
                return True

        return False

    return analizar(simbolo_inicial, cadena)

if __name__ == "__main__":
    archivo_gramatica = "gramatica.txt"

    # Leer la gramática del archivo
    gramatica, simbolo_inicial = leer_gramatica(archivo_gramatica)

    # Construir el árbol desde el símbolo inicial
    G = nx.DiGraph()
    construir_arbol(gramatica, simbolo_inicial, G, profundidad_maxima=10)

    # Mostrar el árbol generado
    mostrar_arbol(G)

    while True:
        # Pedir al usuario una cadena para verificar
        cadena = input("Introduce una cadena para verificar: ").strip()
        if verificar_cadena(gramatica, simbolo_inicial, cadena):
            print("La cadena es aceptada por la gramática.")
        else:
            print("La cadena NO es aceptada por la gramática.")