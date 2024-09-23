Aquí tienes el contenido del archivo `README.md` en un solo bloque de texto:

# Generador de Árboles de Derivación y Verificación de Cadenas

Este programa permite leer una gramática desde un archivo, construir el árbol de derivación correspondiente y verificar si una cadena es aceptada por dicha gramática. Además, genera una visualización del árbol utilizando la biblioteca `networkx` y `matplotlib`.

## Requisitos previos

Asegúrate de tener instaladas las siguientes bibliotecas de Python antes de ejecutar el programa:

- `networkx`
- `matplotlib`

Puedes instalarlas usando `pip` con el siguiente comando:

```bash
pip install networkx matplotlib

## Paso a paso para ejecutar el programa en Linux

### 1. Clonar el repositorio (si es necesario)

Si has descargado el código de un repositorio Git, clónalo con el siguiente comando:

```bash
git clone https://github.com/usuario/repositorio.git
```

### 2. Preparar el entorno

Asegúrate de tener Python 3.x instalado en tu sistema. Puedes verificarlo con:

```bash
python3 --version
```

### 3. Crear el archivo de gramática

Crea un archivo llamado `gramatica.txt` en el mismo directorio que el script de Python. El archivo debe seguir el siguiente formato para definir las reglas de la gramática:

```
S -> a A | b B
A -> a
B -> b
```

Donde `S` es el símbolo inicial y `A`, `B` son los símbolos no terminales. Los símbolos terminales son `a` y `b`.

### 4. Ejecutar el programa

Una vez que tengas el archivo de gramática y las dependencias instaladas, puedes ejecutar el programa utilizando el siguiente comando:

```bash
python3 nombre_del_script.py
```

Donde `nombre_del_script.py` es el nombre del archivo Python que contiene el código del programa.

### 5. Ingresar la cadena a verificar

El programa te pedirá que ingreses una cadena para verificar si es aceptada por la gramática. Por ejemplo:

```
Introduce una cadena para verificar: a a
```

Si la cadena es aceptada, verás el mensaje:

```
La cadena es aceptada por la gramática.
```

Si no es aceptada:

```
La cadena NO es aceptada por la gramática.
```

### 6. Visualización del árbol de derivación

Después de verificar la cadena, el programa generará un árbol de derivación basado en la gramática que hayas proporcionado y lo mostrará utilizando `matplotlib`.

### 7. Limitar la profundidad del árbol

El parámetro `profundidad_maxima` en el código limita la profundidad de la recursión para evitar que se generen árboles infinitos. El valor predeterminado es 10, pero puedes modificarlo según tus necesidades.


