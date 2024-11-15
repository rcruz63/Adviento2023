import os
import copy

# Diccionario que define las conexiones válidas para cada dirección
CAMINOS = {
    'N': ['|', '7', 'F'],  # Conexiones válidas para ir al norte
    'E': ['-', '7', 'J'],  # Conexiones válidas para ir al este
    'S': ['|', 'L', 'J'],  # Conexiones válidas para ir al sur
    'W': ['-', 'L', 'F']}  # Conexiones válidas para ir al oeste

def go_north(coordinates):
    """Devuelve las coordenadas al moverse hacia el norte."""
    return (coordinates[0] - 1, coordinates[1])

def go_south(coordinates):
    """Devuelve las coordenadas al moverse hacia el sur."""
    return (coordinates[0] + 1, coordinates[1])

def go_east(coordinates):
    """Devuelve las coordenadas al moverse hacia el este."""
    return (coordinates[0], coordinates[1] + 1)

def go_west(coordinates):
    """Devuelve las coordenadas al moverse hacia el oeste."""
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

    if not new_coordinates:
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

def flood_fill_exterior(rutas, x, y, verbose):
    """
    Marca todas las celdas accesibles desde el exterior del mapa como 'o'.

    Args:
        rutas (list): Mapa con las rutas marcadas.
        x (int): Coordenada X inicial.
        y (int): Coordenada Y inicial.
        verbose (bool): Si es True, imprime información de depuración.
    """
    stack = [(x, y)]
    while stack:
        cx, cy = stack.pop()
        # Ignorar si está fuera de los límites
        if cx < 0 or cy < 0 or cx >= len(rutas) or cy >= len(rutas[0]):
            continue
        # Marcar como exterior si es un punto libre o ya marcado
        if rutas[cx][cy] == '.' or rutas[cx][cy] == 'o':
            rutas[cx][cy] = 'o'
            # Añadir los puntos adyacentes a la pila
            stack.extend([(cx + 1, cy), (cx - 1, cy), (cx, cy + 1), (cx, cy - 1)])

    if verbose:
        print("Mapa después de flood_fill_exterior:")
        for fila in rutas:
            print(''.join(fila))

def calculate_area(rutas, verbose):
    """
    Calcula el área encerrada dentro del bucle principal.

    Args:
        rutas (list): Copia del mapa con las rutas marcadas.
        verbose (bool): Si es True, imprime información de depuración.

    Returns:
        int: Área encerrada dentro del bucle principal.
    """
    # Copiar el mapa de rutas para preservar el original
    rutas_copia = copy.deepcopy(rutas)

    # Marcar el exterior del mapa usando flood fill
    for x, _ in enumerate(rutas_copia):
        if rutas_copia[x][0] == '.':
            flood_fill_exterior(rutas_copia, x, 0, verbose)
        if rutas_copia[x][len(rutas_copia[0]) - 1] == '.':
            flood_fill_exterior(rutas_copia, x, len(rutas_copia[0]) - 1, verbose)
    for y, _ in enumerate(rutas_copia[0]):
        if rutas_copia[0][y] == '.':
            flood_fill_exterior(rutas_copia, 0, y, verbose)
        if rutas_copia[len(rutas_copia) - 1][y] == '.':
            flood_fill_exterior(rutas_copia, len(rutas_copia) - 1, y, verbose)

    if verbose:
        print("Mapa después de flood_fill_exterior:")
        for fila in rutas_copia:
            print(''.join(fila))

    # Contar las celdas no conectadas al exterior (encerradas)
    area_encerrada = sum(row.count('.') for row in rutas_copia)

    return area_encerrada

def dia10_1(data, verbose: bool = False):
    """ Función principal del día 10-1. """

    current_dir = os.path.dirname(os.path.realpath(__file__))
    data_path = os.path.join(current_dir, data)
    if verbose:
        print(f'Opening file {data_path}')

    # Leer el fichero de entrada y generar una matriz con el mapa
    mapa = [list(linea) for linea in open(data_path, encoding="utf-8").read().split('\n')]
    if verbose:
        print("Mapa:")
        for fila in mapa:
            print(fila)

    # Crear una copia del mapa inicial con '.'
    rutas = [['.' for _ in fila] for fila in mapa]

    # Encontrar la posición inicial marcada con 'S'
    inicio = next((mapa.index(fila), fila.index('S')) for fila in mapa if 'S' in fila)
    if verbose:
        print(f'posicion_S = {inicio}')

    # Marcar el inicio en el mapa de rutas
    rutas[inicio[0]][inicio[1]] = 0

    # Inicializar el bucle principal y caminos
    loop = [['S', inicio, 0]]
    reverse_loop = []

    # Buscar caminos iniciales posibles a partir de S
    caminos_posibles = []
    if inicio[0] > 0 and mapa[inicio[0]-1][inicio[1]] in CAMINOS['N']:
        caminos_posibles.append(['N', (inicio[0]-1, inicio[1]), 1])
    if inicio[1] < len(mapa[inicio[1]])-1 and mapa[inicio[0]][inicio[1]+1] in CAMINOS['E']:
        caminos_posibles.append(['E', (inicio[0], inicio[1]+1), 1])
    if inicio[0] < len(mapa)-1 and mapa[inicio[0]+1][inicio[1]] in CAMINOS['S']:
        caminos_posibles.append(['S', (inicio[0]+1, inicio[1]), 1])
    if inicio[1] > 0 and mapa[inicio[0]][inicio[1]-1] in CAMINOS['W']:
        caminos_posibles.append((['W', (inicio[0], inicio[1]-1), 1]))

    coinciden = False
    # Añadir los primeros caminos posibles al bucle y caminos inversos
    loop.append(caminos_posibles[0])
    reverse_loop.append(caminos_posibles[1])
    for camino in caminos_posibles:
        rutas[camino[1][0]][camino[1][1]] = camino[2]

    # Explorar caminos hasta encontrar el cierre del bucle
    while not coinciden:
        new_caminos_posibles = []
        ida = True
        for camino in caminos_posibles:
            next_step = get_next_step(mapa, camino, verbose)
            if next_step:
                if ida:
                    loop.append(next_step)
                    ida = False
                else:
                    reverse_loop.append(next_step)
                    ida = True
                new_caminos_posibles.append(next_step)
                rutas[next_step[1][0]][next_step[1][1]] = next_step[2]
        caminos_posibles = new_caminos_posibles
        if len(caminos_posibles) < 2:
            print("ERROR: Todos los caminos son invalidos.")
            exit(1)
        if verbose:
            print("Caminos posibles:", caminos_posibles)

        # Verificar si algún camino posible coincide con otro, cerrando el bucle
        for camino in caminos_posibles:
            for camino2 in caminos_posibles:
                if camino[1] == camino2[1] and camino != camino2:
                    coinciden = True
                    break
            if coinciden:
                break

    if verbose:
        print("Rutas:")
        for fila in rutas:
            print(fila)

    # Combinar el bucle principal con los caminos inversos
    loop.extend(reverse_loop[::-1])
    if verbose:
        print("Loop:", loop)

    # Calcular el área encerrada
    rutas_copia = copy.deepcopy(rutas)
    result2 = calculate_area(rutas, verbose)

    # Marcar puntos internos en el mapa de rutas
    for fila in rutas_copia:
        for i, _ in enumerate(fila):
            if fila[i] == '.':
                fila[i] = 0
    if verbose:
        print("Ruta 2:")
        for fila in rutas_copia:
            print(fila)

    # Calcular la distancia máxima
    result = max(max(fila) for fila in rutas_copia)

    # Imprimir los resultados
    print(f'resultado dia 10 - 1 = "{result}"')
    print(f'resultado dia 10 - 2 = "{result2}"')

if __name__ == "__main__":
    dia10_1("data10_1.txt", verbose=False)
