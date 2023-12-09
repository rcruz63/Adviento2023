import os
import pandas as pd

def process_seeds(line, verbose: bool = False):
    "Procesar la linea de semillas"
    if verbose:
        print(f'Processing seeds line: {line}')
    _, text_seeds = line.split(":")
    seeds = [int(num) for num in text_seeds.split()]
    if verbose:
        print(f'seeds = "{seeds}"')
    return seeds

def process_from_to(line, verbose: bool = False):
    """ Procesar una linea del archivo que define el origen y el destino. """
    if verbose:
        print(f'Processing from_to line: {line}')

    text_from_to, _ = line.split(" ")

    origen, _, destino = text_from_to.split("-")

    if verbose:
        print(f'origen = "{origen}"')
        print(f'destino = "{destino}"')

    return origen, destino

def process_map(origen, destino, line, verbose: bool = False):
    """ Procesar una linea del archivo. """
    if verbose:
        print(f'Processing line: {line}')

    inicio_destino, inicio_origen, size = [int(num) for num in line.split()]
    return {"origen":origen, "destino":destino, "inicio_origen":inicio_origen,
        "fin_origen":inicio_origen+size, "inicio_destino":inicio_destino,
        "fin_destino":inicio_destino+size}

def path_seed(seed, map_seeds, verbose: bool = False):
    """ Procecesar una semilla y el mapa de semillas. """
    if verbose:
        print(f'Processing seed: {seed}')
    path = []
    origen = "seed"
    while origen != "location":
        path.append(seed)
        submap = map_seeds[map_seeds["origen"] == origen]
        if verbose:
            print('submap')
            print(submap)
        rango = submap[(submap["inicio_origen"] <= seed) & (submap["fin_origen"] > seed)]
        if verbose:
            print('rango')
            print(rango)
        if rango.empty:
            if verbose:
                print(f'No hay rango para seed = "{seed}"')
            new_seed = seed
        else:
            diff = seed - rango.iloc[0]["inicio_origen"]
            new_seed = rango.iloc[0]["inicio_destino"] + diff
            if verbose:
                print(f'diff = "{diff}"')
                print(f'{submap.iloc[0]["destino"]} = "{new_seed}"')

        origen = submap.iloc[0]["destino"]
        seed = new_seed
    path.append(seed)
    if verbose:
        print(f'path = "{path}"')
    return path

def where_is_seed(seeds, map_seeds, verbose: bool = False):
    """ Procecesar las semillas y el mapa de semillas. """
    seed_path = []
    for seed in seeds:
        seed_path.append(path_seed(seed, map_seeds, verbose))
    return seed_path
        

def dia5_1(data, verbose: bool = False):
    """ Función principal del día 5-1. """

    current_dir = os.path.dirname(os.path.realpath(__file__))
    data_path = os.path.join(current_dir, data)
    if verbose:
        print(f'Opening file {data_path}')
    result = 0
    lista_mapa = []
    origen, destino = "", ""
    
    # Leer el archivo
    with open(data_path, "r", encoding="utf-8") as file:
        # Leer cada linea del archivo

        for line in file:
            if line == '\n' or line == '':
                continue
            if line.startswith("seeds"):
                seeds = process_seeds(line, verbose)
            elif line[0].isdigit():
                lista_mapa.append (process_map(origen, destino, line, verbose))
            else:
                origen, destino = process_from_to(line, verbose)      

    map_seeds = pd.DataFrame(lista_mapa)

    path_seeds = where_is_seed(seeds, map_seeds, verbose)
    if verbose:
        print(f'path_seeds = "{path_seeds}"')

    result = min(locations[-1] for locations in path_seeds)
    # Imprimir el resultado
    print(f'resultado dia 5 - 1 = "{result}"')
    return seeds, map_seeds


def expand_seeds(seeds, verbose: bool = False):
    """ Expandir una lista de semillas. """
    new_seeds = []
    for i in range(0, len(seeds), 2):
        inicio = seeds[i]
        longitud = seeds[i+1]
        new_seeds.extend(range(inicio, inicio + longitud))
    if verbose:
        print(f'new_seeds = "{new_seeds}"')
    return new_seeds


def dia5_2(seeds, map_seeds, verbose: bool = False):
    """ Función principal del día 5-2. """

    new_seeds = expand_seeds(seeds, verbose)
    path_seeds = where_is_seed(new_seeds, map_seeds, verbose)
    if verbose:
        print(f'path_seeds = "{path_seeds}"')

    result = min(locations[-1] for locations in path_seeds)

    # Imprimir el resultado

    print(f'resultado dia 5 - 2 = "{result}"')

if __name__ == "__main__":
    seeds, map_seeds = dia5_1("test5_1.txt", verbose=True)
    dia5_2(seeds, map_seeds, verbose=True)
