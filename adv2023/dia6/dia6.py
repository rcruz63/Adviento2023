import os

def dia6_1(data, verbose: bool = False):
    """ Función principal del día 6-1. """

    current_dir = os.path.dirname(os.path.realpath(__file__))
    data_path = os.path.join(current_dir, data)
    ltimes, ldistances = open(data_path, "r", encoding="utf-8").read().split("\n")

    times = [int(x) for x in ltimes.split() if x.isdigit()]
    distances = [int(x) for x in ldistances.split() if x.isdigit()]
    carreras = zip(times, distances)
    result = 1
    for carrera in carreras:
        productos = 0
        tiempo, max_dist = carrera
        
        for i in range(1, (tiempo // 2) + 1):
            dist = i * (tiempo - i)
            if dist > max_dist:
                if tiempo % 2 == 0 and i == tiempo // 2:
                    productos += 1
                else:
                    productos += 2
            if verbose:
                print(f'carrera = "{carrera}", i = "{i}", dist = "{dist}", productos = "{productos}"')
        if productos > 0:
            result *= productos
            
    # Imprimir el resultado

    print(f'resultado dia 6 - 1 = "{result}"')


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
    dia6_1("test6_1.txt", verbose=True)
    #dia6_2("test6_2.txt", verbose=True)
