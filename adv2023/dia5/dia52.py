import os
import pandas as pd

from functools import reduce

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



def expand_seeds(seeds, map_seeds, verbose: bool = False):
    """ Expandir una lista de semillas. """
    min_location = -1
    for i in range(0, len(seeds), 2):
        inicio = seeds[i]
        longitud = seeds[i+1]
        print(f'Processing seeds "{inicio}" and "{inicio + longitud}"')
        for new_seed in range(inicio, inicio + longitud):
            if (new_seed - inicio) % 10000 == 0:
                print(f'new_seed = "{new_seed}"')
            if verbose:
                print(f'New seed = "{new_seed}"')
            new_path=path_seed(new_seed, map_seeds, verbose)
            if min_location == -1 or new_path[-1] < min_location:
                min_location = new_path[-1]
                print("")
                print(f'New min for seed "{new_seed}" min_location = "{min_location}"')
    return min_location

def lookup(inputs, mapping):
    for start, length in inputs:
        while length > 0:
            for m in mapping.split('\n')[1:]:
                dst, src, len = map(int, m.split())
                delta = start - src
                if delta in range(len):
                    len = min(len - delta, length)
                    yield (dst + delta, len)
                    start += len
                    length -= len
                    break
            else: yield (start, length); break


def dia5_2(data, verbose: bool = False):
    """ Función principal del día 5-2. """

    current_dir = os.path.dirname(os.path.realpath(__file__))
    data_path = os.path.join(current_dir, data)

    seeds, *mappings = open(data_path).read().split('\n\n')
    seeds = list(map(int, seeds.split()[1:]))

    print('resultado dia 5 - 2 = ')
    print(*[min(reduce(lookup, mappings, s))[0] for s in [
    zip(seeds, [1] * len(seeds)),
    zip(seeds[0::2], seeds[1::2])]])

if __name__ == "__main__":
    dia5_1("data5_1.txt", verbose=False)
    dia5_2("data5_1.txt", verbose=False)
