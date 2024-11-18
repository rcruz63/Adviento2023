import os


def dia12_1(data, verbose: bool = False):
    """ Función principal del día 12-1. """

    current_dir = os.path.dirname(os.path.realpath(__file__))
    data_path = os.path.join(current_dir, data)
    if verbose:
        print(f'Opening file {data_path}')

    instalacion = open(data_path, encoding="utf-8").read().split('\n')
    result = 0
    for terma in instalacion:
        # Decodificar la linea
        termas, configuracion = terma.split(' ')
        pass
            
    # Imprimir el resultado

    print(f'resultado dia 12 - 1 = "{result}"')


def dia12_2(data, verbose: bool = False):
    """ Función principal del día 12-2. """

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

    print(f'resultado dia 12 - 2 = "{result}"')

if __name__ == "__main__":
    dia12_1("test12_1.txt", verbose=False)
    dia12_2("test12_2.txt", verbose=True)
