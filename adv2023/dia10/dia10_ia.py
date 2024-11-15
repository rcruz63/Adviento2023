from collections import deque
from typing import List, Tuple, Dict
import os

# Mapa de conexiones para los distintos tipos de tuberías
PIPE_CONNECTIONS = {
    '|': [(-1, 0), (1, 0)],
    '-': [(0, -1), (0, 1)],
    'L': [(1, 0), (0, 1)],
    'J': [(-1, 0), (0, 1)],
    '7': [(-1, 0), (0, -1)],
    'F': [(1, 0), (0, -1)],
    'S': [(-1, 0), (1, 0), (0, -1), (0, 1)],  # Punto de inicio; se conecta en todas las direcciones
}

def dia10_1(data: str, verbose: bool = False) -> int:
    """
    Encuentra la distancia más lejana desde el punto de inicio en el bucle principal.

    Args:
        data (str): Nombre del fichero que contiene el mapa del laberinto.
        verbose (bool): Imprime resultados intermedios si es True.

    Returns:
        int: Distancia máxima desde el punto de inicio al punto más lejano del bucle.
    """
    grid = read_map(data)
    start_pos = find_start(grid)
    if verbose:
        print("Inicial:", start_pos)
    _, distances = explore_loop(grid, start_pos, verbose)
    
    max_distance = max(distances.values())

    if verbose:
        print("Distancias calculadas:")
        print_distances(grid, distances)

    print(f"La distancia máxima desde el punto de inicio es {max_distance}.")

    return max_distance

def read_map(file_name: str) -> List[List[str]]:
    """Lee el mapa del archivo y lo devuelve como una lista 2D."""
    current_dir = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(current_dir, file_name)
    with open(file_path, 'r', encoding="utf-8") as file:
        return [list(line.strip()) for line in file]

def find_start(grid: List[List[str]]) -> Tuple[int, int]:
    """Encuentra la posición de inicio (marcada como 'S') en el mapa.""" 
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == 'S':
                return y, x
    raise ValueError("No se encontró el punto de inicio 'S' en el mapa.")

def explore_loop(grid: List[List[str]], start_pos: Tuple[int, int], verbose: bool) -> Tuple[Dict[Tuple[int, int], bool], Dict[Tuple[int, int], int]]:
    """
    Explora el bucle principal desde la posición de inicio y calcula las distancias.

    Args:
        grid (List[List[str]]): Mapa del laberinto.
        start_pos (Tuple[int, int]): Posición de inicio.
        verbose (bool): Imprime pasos intermedios si es True.

    Returns:
        Tuple[Dict, Dict]: Diccionario de visitados y distancias desde el inicio.
    """
    queue = deque([start_pos])
    visited = {}
    distances = {start_pos: 0}

    while queue:
        if verbose:
            print("Queue:", queue)
            print("Distances:", distances)
        y, x = queue.popleft()
        visited[(y, x)] = True

        if verbose:
            print(f"Procesando ({y}, {x}), PIPE: {grid[y][x]}")

        for dy, dx in PIPE_CONNECTIONS.get(grid[y][x], []):
            ny, nx = y + dy, x + dx

            if not (0 <= ny < len(grid) and 0 <= nx < len(grid[0])):
                continue  # Fuera de los límites

            if (ny, nx) in visited or grid[ny][nx] == '.':
                continue  # Ya visitado o no es tubería

            if is_connected(grid, (y, x), (ny, nx)):
                queue.append((ny, nx))
                distances[(ny, nx)] = distances[(y, x)] + 1

    return visited, distances

def is_connected(grid: List[List[str]], pos1: Tuple[int, int], pos2: Tuple[int, int]) -> bool:
    """Comprueba si dos posiciones están conectadas según las tuberías."""
    y1, x1 = pos1
    y2, x2 = pos2
    
    for dy, dx in PIPE_CONNECTIONS.get(grid[y1][x1], []):
        if (y1 + dy, x1 + dx) == (y2, x2):
            return True
    return False

def print_distances(grid: List[List[str]], distances: Dict[Tuple[int, int], int]) -> None:
    """Imprime las distancias calculadas en el mapa."""
    for y, row in enumerate(grid):
        print(''.join(
            str(distances.get((y, x), '.')) if grid[y][x] != '.' else '.'
            for x in range(len(row))
        ))

if __name__ == "__main__":
    dia10_1("test10_1.txt", verbose=True)
