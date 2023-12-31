import os
import numpy as np


def file_to_nparray(file_path):
    """Convert a file to a numpy array."""
    with open(file_path, 'r', encoding="utf-8") as file:
        lines_list = [list(line.strip()) for line in file]
    return np.array(lines_list)


def extract_chars(np_array):
    """Extract all the unique chars from a numpy array."""
    char_list = list(set(char for row in np_array for char in row if not char.isdigit() and char != "."))
    return char_list

def look_for_symbol(engine, symbols, row, inicio, fin, verbose: bool = False):
    """Look for a symbol around a number."""
    start_row = row - 1 if row > 0 else row
    end_row = row + 2 if row < len(engine)-1 else row
    start_col = inicio - 1 if inicio > 0 else inicio
    end_col = fin + 1 if fin < len(engine[row]) else fin
    if verbose:
        print(f'Looking for symbol in ({start_row}, {start_col}) and ({end_row}, {end_col})')
    for i in range(start_row, end_row):
        for j in range(start_col, end_col):
            if engine[i][j] in symbols:
                if verbose:
                    print(f'Found symbol {engine[i][j]} at {i},{j}')
                return True
    return False


def procesar_motor(engine, symbols, verbose: bool = False):
    """Procesar el motor."""
    # Recorrer el motor
    #  - Cuando se encuentre un numero hay que buscar los siguientes digitos y formar un numero completo
    #    - Estos numeros no tienen que volver a ser analizados
    #  - Una vez se tenga el número completo hay que buscar si hay algun simbolo adyacente (incluido en diagonal)
    #  - Si el numero tiene un simbolo adyacente se suma al resultado

    result = 0
    dentro=False
    inicio=0
    fin=0
    for i, row in enumerate(engine):
        for j, char in enumerate(row):
            if char.isdigit():
                if not dentro:
                    inicio=j
                    dentro=True
                    number = char
                else:
                    number += char
            else:
                if dentro:
                    fin=j
                    dentro=False
                    # Buscar simbolos adyacentes
                    if verbose:
                        print(f'Number {number} at {i}: {inicio},{fin}')
                    if look_for_symbol(engine, symbols, i, inicio, fin, verbose):
                        result += int(number)
                        if verbose:
                            print(f'Number {number} at {i}: {inicio},{fin} with symbol')
        if dentro:
            fin=len(row)
            dentro=False
            # Buscar simbolos adyacentes
            if verbose:
                print(f'Number {number} at {i}: {inicio},{fin}')
            if look_for_symbol(engine, symbols, i, inicio, fin, verbose):
                result += int(number)
                if verbose:
                    print(f'Number {number} at {i}: {inicio},{fin} with symbol')
        inicio=0
        fin=0
    return result

def dia3_1(data, verbose: bool = False):
    """ Función principal del día 3-1. """

    current_dir = os.path.dirname(os.path.realpath(__file__))
    data_path = os.path.join(current_dir, data)
    if verbose:
        print(f'Opening file {data_path}')

    # Inicializar un np.aary con las lineas del fichero de datos
    engine = file_to_nparray(data_path)

    # Obtener la lista de simbolos únicos del motor
    symbols = extract_chars(engine)
    if verbose:
        print(f'Engine symbols: {symbols}')

    result=procesar_motor(engine, symbols, verbose)

    print(f'resultado dia 3 - 1 = "{result}"')


def producto_valores_adyacentes(valores, i, j, verbose: bool = False):
    """ Calcular el producto de los valores adyacentes a un simbolo """
    valores_adyacentes = []
    for fila, inicio, fin, valor in valores:
        if (fila == i-1 and inicio-1 <= j <= fin):
            if verbose:
                print(f'Fila superior: {fila}, {inicio}, {fin}, {valor} - Sym: {i},{j}')
            valores_adyacentes.append(valor)
        if (fila == i and j in (inicio-1, fin)):
            if verbose:
                print(f'Fila misma: {fila}, {inicio}, {fin}, {valor} - Sym: {i},{j}')
            valores_adyacentes.append(valor)
        if (fila == i+1 and inicio-1 <= j <= fin):
            if verbose:
                print(f'Fila inferior: {fila}, {inicio}, {fin}, {valor} - Sym: {i},{j}')
            valores_adyacentes.append(valor)

    if len(valores_adyacentes) < 2:
        return -1

    if verbose:
        print(f'Valores adyacentes: {valores_adyacentes}')

    producto = 1
    for valor in valores_adyacentes:
        producto *= valor

    return producto

def procesar_numeros(engine, verbose: bool = False):
    """ Generar diccionario por fila ordenada de numeros con sus posiciones """
    lista_numeros=[]
    dentro=False
    inicio=0
    fin=0
    for i, row in enumerate(engine):
        for j, char in enumerate(row):
            if char.isdigit():
                if not dentro:
                    inicio=j
                    dentro=True
                    number = char
                else:
                    number += char
            else:
                if dentro:
                    fin=j
                    dentro=False
                    if verbose:
                        print(f'Number {number} at {i}: {inicio},{fin}')
                    lista_numeros.append([i, inicio, fin, int(number)])
        if dentro:
            fin=len(row)
            dentro=False
            # Buscar simbolos adyacentes
            if verbose:
                print(f'Number {number} at {i}: {inicio},{fin}')
            lista_numeros.append([i, inicio, fin, int(number)])
        inicio=0
        fin=0
    return lista_numeros

def procesar_simblos(engine, lista_numeros, symbols, verbose):
    """ Para cada simbolo buscar si tiene DOS numeros adyacentes. si los tiene los multiplica 
        y los suma al resultado """
    result=0
    for i, row in enumerate(engine):
        for j, char in enumerate(row):
            if char in symbols:
                if verbose:
                    print(f'Found symbol {char} at {i},{j}')
                # Buscar simbolos adyacentes
                producto = producto_valores_adyacentes(lista_numeros, i, j, verbose)
                if verbose:
                    print(f'Producto: {producto}')
                if producto > 0:
                    result += producto

    if verbose:
        print(f'Resultado: {result}')
    return result


def dia3_2(data, verbose: bool = False):
    """ Función principal del día 3-2. """

    current_dir = os.path.dirname(os.path.realpath(__file__))
    data_path = os.path.join(current_dir, data)
    if verbose:
        print(f'Opening file {data_path}')

    # Inicializar un np.aary con las lineas del fichero de datos
    engine = file_to_nparray(data_path)

    # Obtener la lista de simbolos únicos del motor
    symbols = extract_chars(engine)
    if verbose:
        print(f'Engine symbols: {symbols}')

    lista_numeros=procesar_numeros(engine, verbose)

    result = procesar_simblos(engine, lista_numeros, symbols, verbose)

    print(f'resultado dia 3 - 2 = "{result}"')


if __name__ == "__main__":
    dia3_1("test3_1.txt", verbose=True)
    dia3_2("test3_2.txt", verbose=True)
