import os

def cargar_mapa(data_path):
    """Carga el mapa desde un archivo y lo devuelve como una lista de listas."""
    with open(data_path, "r", encoding="utf-8") as file:
        return [list(line.strip()) for line in file.readlines()]

def obtener_universo(mapa):
    """Obtiene las coordenadas de las galaxias del mapa."""
    universo = {}
    galaxy_id = 0
    for y, fila in enumerate(mapa):
        for x, celda in enumerate(fila):
            if celda == '#':
                universo[galaxy_id] = (y, x)
                galaxy_id += 1
    return universo

def ajustar_filas_vacias(universo, mapa, factor_expansion):
    """Reemplaza filas vacías por su tamaño absoluto en las coordenadas Y."""
    filas_vacias = [y for y, fila in enumerate(mapa) if '#' not in fila]
    nueva_coordenada_y = {}
    fila_actual = 0

    for y in range(len(mapa)):
        if y in filas_vacias:
            fila_actual += factor_expansion  # Expandimos por el factor
        else:
            nueva_coordenada_y[y] = fila_actual
            fila_actual += 1

    # Reasignamos las coordenadas Y en el universo
    for galaxy_id, (galaxy_y, galaxy_x) in universo.items():
        universo[galaxy_id] = (nueva_coordenada_y[galaxy_y], galaxy_x)
    return universo

def ajustar_columnas_vacias(universo, mapa, factor_expansion):
    """Reemplaza columnas vacías por su tamaño absoluto en las coordenadas X."""
    columnas_vacias = [x for x, columna in enumerate(zip(*mapa)) if '#' not in columna]
    nueva_coordenada_x = {}
    columna_actual = 0

    for x in range(len(mapa[0])):
        if x in columnas_vacias:
            columna_actual += factor_expansion  # Expandimos por el factor
        else:
            nueva_coordenada_x[x] = columna_actual
            columna_actual += 1

    # Reasignamos las coordenadas X en el universo
    for galaxy_id, (galaxy_y, galaxy_x) in universo.items():
        universo[galaxy_id] = (galaxy_y, nueva_coordenada_x[galaxy_x])
    return universo

def calcular_distancias(universo):
    """Calcula la suma de las distancias mínimas entre todas las galaxias."""
    distancia_total = 0
    galaxias = list(universo.values())
    for i, (y1, x1) in enumerate(galaxias):
        for j in range(i + 1, len(galaxias)):
            y2, x2 = galaxias[j]
            distancia_total += abs(y1 - y2) + abs(x1 - x2)
    return distancia_total

def dia11_2(data, factor_expansion=1_000_000, verbose=False):
    """Resuelve la segunda parte del día 11."""
    current_dir = os.path.dirname(os.path.realpath(__file__))
    data_path = os.path.join(current_dir, data)

    if verbose:
        print(f"Cargando archivo {data_path}")

    mapa = cargar_mapa(data_path)
    universo = obtener_universo(mapa)

    if verbose:
        print("Universo inicial:", universo)

    # Ajustar el universo según las filas y columnas vacías
    universo = ajustar_filas_vacias(universo, mapa, factor_expansion)
    universo = ajustar_columnas_vacias(universo, mapa, factor_expansion)

    if verbose:
        print("Universo ajustado:", universo)

    # Calcular distancias
    resultado = calcular_distancias(universo)

    print(f"Resultado día 11 - 2 con factor {factor_expansion} = {resultado}")

if __name__ == "__main__":
    # Prueba con datos del enunciado
    dia11_2("test11_1.txt", factor_expansion=10, verbose=True)  # Debe dar 1030
    dia11_2("test11_1.txt", factor_expansion=100, verbose=True)  # Debe dar 8410
    dia11_2("test11_1.txt", factor_expansion=1_000_000, verbose=True)
    dia11_2("data11_1.txt", factor_expansion=1_000_000, verbose=True)