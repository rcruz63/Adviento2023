import os
import copy
from collections import deque

# Diccionario que define las conexiones válidas para cada dirección
CAMINOS = {
    'N': ['|', '7', 'F'],  # Conexiones válidas para ir al norte
    'E': ['-', '7', 'J'],  # Conexiones válidas para ir al este
    'S': ['|', 'L', 'J'],  # Conexiones válidas para ir al sur
    'W': ['-', 'L', 'F']}  # Conexiones válidas para ir al oeste


def change_inicio(mapa, inicio):
    """ Cambia el inicio de la ruta por '|' si es un punto vertical """
    y, x = inicio
    filas = len(mapa)
    columnas = len(mapa[0])

    if y > 0 and y < filas - 1 and mapa[y - 1][x] in CAMINOS['N'] and mapa[y + 1][x] in CAMINOS['S']:
        mapa[y][x] = '|'
    elif x > 0 and x < columnas - 1 and mapa[y][x - 1] in CAMINOS['W'] and mapa[y][x + 1] in CAMINOS['E']:
        mapa[y][x] = '-'
    elif y > 0 and x > 0 and y < filas - 1 and x < columnas - 1 and mapa[y - 1][x] in CAMINOS['N'] and mapa[y][x - 1] in CAMINOS['W']:
        mapa[y][x] = '|'
    elif y > 0 and x < columnas - 1 and y < filas - 1 and mapa[y - 1][x] in CAMINOS['N'] and mapa[y][x + 1] in CAMINOS['E']:
        mapa[y][x] = '-'
    elif y < filas - 1 and x > 0 and y > 0 and mapa[y + 1][x] in CAMINOS['S'] and mapa[y][x - 1] in CAMINOS['W']:
        mapa[y][x] = '|'
    elif y < filas - 1 and x < columnas - 1 and y > 0 and mapa[y + 1][x] in CAMINOS['S'] and mapa[y][x + 1] in CAMINOS['E']:
        mapa[y][x] = '-'

    return mapa

def marcar_exteriores(mapa):
    """ Marca las celdas exteriores del mapa. 
        Realiza una búsqueda en anchura (BFS) desde todas las celdas del borde que son accesibles ('.'). 
        Luego, en la función principal, se utiliza la matriz exteriores para determinar si una celda es 
        interior o exterior. Las celdas interiores se marcan con 'I' y se cuentan para el resultado final.
    """
    filas = len(mapa)
    columnas = len(mapa[0])
    visitado = [[False] * columnas for _ in range(filas)]
    cola = deque()

    # Añadir todas las celdas del borde a la cola
    for x in range(columnas):
        if mapa[0][x] == '.':
            cola.append((0, x))
        if mapa[filas - 1][x] == '.':
            cola.append((filas - 1, x))
    for y in range(filas):
        if mapa[y][0] == '.':
            cola.append((y, 0))
        if mapa[y][columnas - 1] == '.':
            cola.append((y, columnas - 1))

    # Realizar BFS desde las celdas del borde
    while cola:
        y, x = cola.popleft()
        if visitado[y][x]:
            continue
        visitado[y][x] = True
        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ny, nx = y + dy, x + dx
            if 0 <= ny < filas and 0 <= nx < columnas and not visitado[ny][nx] and mapa[ny][nx] == '.':
                cola.append((ny, nx))

    return visitado

def dia10_1(data, verbose: bool = False):
    """ Función principal del día 10-1. """

    current_dir = os.path.dirname(os.path.realpath(__file__))
    data_path = os.path.join(current_dir, data)
    if verbose:
        print(f'Opening file {data_path}')

    # Leer el fichero de entrada y generar una matriz con el mapa
    mapa = [list(linea) for linea in open(data_path, encoding="utf-8").read().split('\n')]
    mapa_limpio = [['.' for _ in fila] for fila in mapa]
    # field_marked = [[False for i in range(len(mapa[0]))] for j in range(len(mapa))]
    if verbose:
        print("Mapa:")
        for fila in mapa:
            print(fila)

    # Encontrar la posición inicial marcada con 'S' x, y
    inicio = next((mapa.index(fila), fila.index('S')) for fila in mapa if 'S' in fila)
    if verbose:
        print(f'posicion_S = {inicio}')

    mapa_limpio[inicio[1]][inicio[0]] = 'S'

    y, x = inicio
    steps = 0

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
        mapa_limpio[y][x] = mapa[y][x]
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

    mapa = change_inicio(mapa_limpio, inicio)
    mapa_copy = copy.deepcopy(mapa_limpio)
    total = 0

    exteriores = marcar_exteriores(mapa_limpio)

    for y, line in enumerate(mapa_limpio):
        for x, _ in enumerate(line):
            if mapa_limpio[y][x] == '.':
                if exteriores[y][x]:
                    mapa_copy[y][x] = 'O'
                else:
                    mapa_copy[y][x] = 'I'
                    total += 1

    print("Mapa con los puntos interiores marcados:")
    for fila in mapa_copy:
        print(''.join(fila))

    print(f'resultado dia 10 - 2 = "{total}"')

if __name__ == "__main__":
    dia10_1("data10_1.txt", verbose=False)
