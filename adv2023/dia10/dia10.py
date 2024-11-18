import os
import copy

# Diccionario que define las conexiones válidas para cada dirección
CAMINOS = {
    'N': ['|', '7', 'F'],  # Conexiones válidas para ir al norte
    'E': ['-', '7', 'J'],  # Conexiones válidas para ir al este
    'S': ['|', 'L', 'J'],  # Conexiones válidas para ir al sur
    'W': ['-', 'L', 'F']}  # Conexiones válidas para ir al oeste

DIRECCIONES = {
    'N': (-1, 0),
    'E': (0, 1),
    'S': (1, 0),
    'W': (0, -1)
}

def change_inicio(mapa, inicio):
    """ Cambia el inicio de la ruta por su tipo correspondiente (|, -, etc.) """
    x, y = inicio
    if y > 0 and y < len(mapa) - 2 and mapa[y - 1][x] in CAMINOS['N'] and mapa[y + 1][x] in CAMINOS['S']:
        mapa[y][x] = '|'
    elif x > 0 and x < len(mapa[0]) - 2 and mapa[y][x - 1] in CAMINOS['W'] and mapa[y][x + 1] in CAMINOS['E']:
        mapa[y][x] = '-'
    elif y > 0 and x > 0 and mapa[y - 1][x] in CAMINOS['N'] and mapa[y][x - 1] in CAMINOS['W']:
        mapa[y][x] = 'J'
    elif y > 0 and x < len(mapa[0]) - 2 and mapa[y - 1][x] in CAMINOS['N'] and mapa[y][x + 1] in CAMINOS['E']:
        mapa[y][x] = 'L'
    elif y < len(mapa) - 2 and x > 0 and mapa[y + 1][x] in CAMINOS['S'] and mapa[y][x - 1] in CAMINOS['W']:
        mapa[y][x] = '7'
    elif y < len(mapa) - 2 and x < len(mapa[0]) - 2 and mapa[y + 1][x] in CAMINOS['S'] and mapa[y][x + 1] in CAMINOS['E']:
        mapa[y][x] = 'F'
    return mapa

def flood_fill_exterior(mapa, x, y):
    """
    Marca todas las celdas accesibles desde el exterior con 'O'.

    Args:
        mapa: El mapa del laberinto.
        x, y: Coordenadas iniciales desde donde iniciar el relleno.
    """
    stack = [(x, y)]
    while stack:
        cx, cy = stack.pop()
        if 0 <= cx < len(mapa[0]) and 0 <= cy < len(mapa) and mapa[cy][cx] == '.':
            mapa[cy][cx] = 'O'
            stack.extend([(cx + 1, cy), (cx - 1, cy), (cx, cy + 1), (cx, cy - 1)])
        elif 0 <= cx < len(mapa[0]) and 0 <= cy < len(mapa):
            # Verificar conexiones válidas de tuberías
            for direccion, (dy, dx) in DIRECCIONES.items():
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < len(mapa[0]) and 0 <= ny < len(mapa):
                    if mapa[cy][cx] in CAMINOS[direccion] and mapa[ny][nx] in CAMINOS[opposite_direction(direccion)]:
                        stack.append((nx, ny))

def opposite_direction(direction):
    """ Devuelve la dirección opuesta a la dada. """
    return {
        'N': 'S',
        'E': 'W',
        'S': 'N',
        'W': 'E'
    }[direction]

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

    # Encontrar la posición inicial marcada con 'S'
    inicio = next((mapa.index(fila), fila.index('S')) for fila in mapa if 'S' in fila)
    if verbose:
        print(f'posicion_S = {inicio}')

    y, x = inicio
    steps = 0

    # Determinar dirección inicial
    if x < len(mapa[0]) - 1 and mapa[y][x + 1] in CAMINOS['E']:
        direccion = 'E'
    elif y < len(mapa) - 1 and mapa[y + 1][x] in CAMINOS['S']:
        direccion = 'S'
    elif x > 0 and mapa[y][x - 1] in CAMINOS['W']:
        direccion = 'W'
    elif y > 0 and mapa[y - 1][x] in CAMINOS['N']:
        direccion = 'N'
    else:
        print("ERROR: No se encontró una dirección válida.")
        exit(1)

    # Recorrer el bucle principal
    while True:
        match direccion:
            case 'N':
                y -= 1
            case 'E':
                x += 1
            case 'S':
                y += 1
            case 'W':
                x -= 1
        match mapa[y][x]:
            case 'L':
                direccion = 'E' if direccion == 'S' else 'N'
            case 'J':
                direccion = 'W' if direccion == 'S' else 'N'
            case '7':
                direccion = 'W' if direccion == 'N' else 'S'
            case 'F':
                direccion = 'E' if direccion == 'N' else 'S'
        steps += 1

        if inicio == (y, x):
            print(f'resultado dia 10 - 1 = "{steps // 2 + (1 if steps % 2 == 1 else 0)}"')
            break

    # Cambiar el inicio para identificarlo correctamente
    mapa = change_inicio(mapa, inicio)

    # Realizar relleno desde el exterior
    for y in range(len(mapa)):
        if mapa[y][0] == '.':
            flood_fill_exterior(mapa, 0, y)
        if mapa[y][len(mapa[0]) - 1] == '.':
            flood_fill_exterior(mapa, len(mapa[0]) - 1, y)
    for x in range(len(mapa[0])):
        if mapa[0][x] == '.':
            flood_fill_exterior(mapa, x, 0)
        if mapa[len(mapa) - 1][x] == '.':
            flood_fill_exterior(mapa, x, len(mapa) - 1)

    # Contar áreas interiores (no marcadas como 'O')
    total = 0
    for y, line in enumerate(mapa):
        for x, cell in enumerate(line):
            if cell == '.':
                mapa[y][x] = 'I'
                total += 1

    print("Mapa con los puntos interiores marcados:")
    for fila in mapa:
        print(''.join(fila))

    print(f'resultado dia 10 - 2 = "{total}"')

if __name__ == "__main__":
    dia10_1("test10_3.txt", verbose=False)
