import os

CAMINOS = {
    'N': ['|', '7', 'F'],
    'E': ['-', '7', 'J'],
    'S': ['|', 'L', 'J'],
    'W': ['-', 'L', 'F']}


def go_north(coordinates):
    return (coordinates[0] - 1, coordinates[1])


def go_south(coordinates):
    return (coordinates[0] + 1, coordinates[1])


def go_east(coordinates):
    return (coordinates[0], coordinates[1] + 1)


def go_west(coordinates):
    return (coordinates[0], coordinates[1] - 1)


def get_next_step(mapa, current_point, verbose):
    """
    Obtiene el siguiente paso en el camino o -1 si no lo hay.

    Args:
        mapa: El mapa del juego.
        current_point: El punto actual.

    Returns:
        El siguiente punto en el camino o [] si no lo hay.
    """

    new_orientation = orientation = current_point[0]
    coordinates = current_point[1]
    num_steps = current_point[2]

    # Obtener el símbolo del camino del mapa.
    symbol = mapa[coordinates[0]][coordinates[1]]

    # Calcular el siguiente punto del camino.
    if symbol == '|':
        if orientation == 'N':
            new_coordinates = go_north(coordinates)
        elif orientation == 'S':
            new_coordinates = go_south(coordinates)
        else:
            new_coordinates = ()

    elif symbol == '-':
        if orientation == 'E':
            new_coordinates = go_east(coordinates)
        elif orientation == 'W':
            new_coordinates = go_west(coordinates)
        else:
            new_coordinates = ()

    elif symbol == '7':
        if orientation == 'N':
            new_orientation = 'W'
            new_coordinates = go_west(coordinates)
        elif orientation == 'E':
            new_orientation = 'S'
            new_coordinates = go_south(coordinates)
        else:
            new_coordinates = ()

    elif symbol == 'F':
        if orientation == 'N':
            new_orientation = 'E'
            new_coordinates = go_east(coordinates)
        elif orientation == 'W':
            new_orientation = 'S'
            new_coordinates = go_south(coordinates)
        else:
            new_coordinates = ()

    elif symbol == 'L':
        if orientation == 'S':
            new_orientation = 'E'
            new_coordinates = go_east(coordinates)
        elif orientation == 'W':
            new_orientation = 'N'
            new_coordinates = go_north(coordinates)
        else:
            new_coordinates = ()

    elif symbol == 'J':
        if orientation == 'S':
            new_orientation = 'W'
            new_coordinates = go_west(coordinates)
        elif orientation == 'E':
            new_orientation = 'N'
            new_coordinates = go_north(coordinates)
        else:
            new_coordinates = ()
    else:
        new_coordinates = ()

    if new_coordinates == ():
        if verbose:
            print(f'Symbol: {symbol}, Orientation: {orientation}, Coordinates: {coordinates}')
        return []

    # Comprobar si el siguiente punto está dentro del mapa.
    if not (0 <= new_coordinates[0] < len(mapa) and 0 <= new_coordinates[1] < len(mapa[0])):
        if verbose:
            print(f'New coordinates out of bounds: {new_coordinates}')
        return []

    # Comprobar si el siguiente punto es un camino válido.
    if mapa[new_coordinates[0]][new_coordinates[1]] not in CAMINOS[new_orientation]:
        if verbose:
            print(f'New coordinates: {mapa[new_coordinates[0]][new_coordinates[1]]} not in {CAMINOS[new_orientation]}')
        return []

    # Devolver el siguiente punto del camino.
    return [new_orientation, new_coordinates, num_steps + 1]


def dia10_1(data, verbose: bool = False):
    """ Función principal del día 10-1. """

    current_dir = os.path.dirname(os.path.realpath(__file__))
    data_path = os.path.join(current_dir, data)
    if verbose:
        print(f'Opening file {data_path}')

    # leer el fichero de entrada y generar una matriz de filas y columnas
    # con cada linea del fichero en una fila de la matriz y cada letra de la matriz
    # en una columna
    mapa = [list(linea) for linea in open(data_path, encoding="utf-8").read().split('\n')]
    if verbose:
        print(mapa)

    # genero una representación del mapa vacio con el caracter '.' en todos los elementos
    rutas = [['.' for _ in fila] for fila in mapa]

    inicio = next((mapa.index(fila), fila.index('S')) for fila in mapa if 'S' in fila)
    if verbose:
        print(f'posicion_S = {inicio}')

    rutas[inicio[0]][inicio[1]] = 0

    # Buscar los caminos posibles a partir de S
    caminos_posibles = []
    # Norte
    if inicio[0] > 0 and mapa[inicio[0]-1][inicio[1]] in CAMINOS['N']:
        caminos_posibles.append(['N', (inicio[0]-1, inicio[1]), 1])
    # Este
    if inicio[1] < len(mapa[inicio[1]])-1 and mapa[inicio[0]][inicio[1]+1] in CAMINOS['E']:
        caminos_posibles.append(['E', (inicio[0], inicio[1]+1), 1])
    # Sur
    if inicio[0] < len(mapa)-1 and mapa[inicio[0]+1][inicio[1]] in CAMINOS['S']:
        caminos_posibles.append(['S', (inicio[0]+1, inicio[1]), 1])
    # Oeste
    if inicio[1] > 0 and mapa[inicio[0]][inicio[1]-1] in CAMINOS['W']:
        caminos_posibles.append((['W', (inicio[0], inicio[1]-1), 1]))

    if verbose:
        print("Caminos posibles:", caminos_posibles)

    coinciden = False
    for camino in caminos_posibles:
        rutas[camino[1][0]][camino[1][1]] = camino[2]
    while not coinciden:
        new_caminos_posibles = []
        for camino in caminos_posibles:
            next_step = get_next_step(mapa, camino, verbose)
            if next_step != []:
                new_caminos_posibles.append(next_step)
                rutas[next_step[1][0]][next_step[1][1]] = next_step[2]
        caminos_posibles = new_caminos_posibles
        if len(caminos_posibles) < 2:
            print("ERROR: Todos los caminos son invalidos.")
            exit(1)
        if verbose:
            print("Caminos posibles:", caminos_posibles)
        # comprobar si coinciden algún camino posible mirando si el segundo elemento
        # de cada camino es igual al segundo elemento de los otros caminos
        for camino in caminos_posibles:
            for camino2 in caminos_posibles:
                if camino[1] == camino2[1] and camino != camino2:
                    coinciden = True
                    break
            if coinciden:
                break

    # el resultado es igual al mayor valor en rutas ignorando los '.'
    if verbose:
        print("Rutas:")
        for fila in rutas:
            print(fila)

    for fila in rutas:
        for i in range(len(fila)):
            if fila[i] == '.':
                fila[i] = 0
    if verbose:
        print("Ruta 2:")
        for fila in rutas:
            print(fila)
        
    # Calcular el resultado
    result = max(max(fila) for fila in rutas)
            
    # Imprimir el resultado
    print(f'resultado dia 10 - 1 = "{result}"')


# def dia10_2(data, verbose: bool = False):
#     """ Función principal del día 10-2. """

#     current_dir = os.path.dirname(os.path.realpath(__file__))
#     data_path = os.path.join(current_dir, data)
#     if verbose:
#         print(f'Opening file {data_path}')

#     # Leer el archivo
#     with open(data_path, "r", encoding="utf-8") as file:
#         # Leer cada linea del archivo
#         result = 0
#         num_line = 1
#         jugadas = []
#         for line in file:
#             # Decodificar la linea
#             pass

#     # Imprimir el resultado

#     print(f'resultado dia 10 - 2 = "{result}"')


if __name__ == "__main__":
    dia10_1("test10_1.txt", verbose=True)
    # dia10_2("test10_2.txt", verbose=True)
