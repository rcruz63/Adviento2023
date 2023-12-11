import os

def dia6_1(data, verbose: bool = False):
    """ Función principal del día 6-1. """

    current_dir = os.path.dirname(os.path.realpath(__file__))
    data_path = os.path.join(current_dir, data)
    if verbose:
        print(f'Opening file {data_path}')

    # Leer el archivo
    with open(data_path, "r", encoding="utf-8") as file:
        # Leer cada linea del archivo
        result = 0
        for line in file:
            # Decodificar la linea
            pass
            
    # Imprimir el resultado

    print(f'resultado dia 4 - 1 = "{result}"')


def dia6_2(data, verbose: bool = False):
    """ Función principal del día 6-2. """

    current_dir = os.path.dirname(os.path.realpath(__file__))
    data_path = os.path.join(current_dir, data)
    if verbose:
        print(f'Opening file {data_path}')

    # Leer el archivo
    with open(data_path, "r", encoding="utf-8") as file:
        # Leer cada linea del archivo
        result = 0
        num_line = 1
        jugadas = []
        for line in file:
            # Decodificar la linea
            pass

    # Imprimir el resultado

    print(f'resultado dia 4 - 2 = "{result}"')

if __name__ == "__main__":
    dia6_1("test6_1.txt", verbose=False)
    dia6_2("test6_2.txt", verbose=True)
