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
    ltimes, ldistances = open(data_path, "r", encoding="utf-8").read().split("\n")

    _, text_timer = ltimes.split(":")
    # eliminar los espacios en blanco y convertir la secuencia de numeros en un unico numero
    tiempo = int("".join(text_timer.split()))

    _, text_distance = ldistances.split(":")
    # eliminar los espacios en blanco y convertir la secuencia de numeros en un unico numero
    max_dist = int("".join(text_distance.split()))

    if verbose:
        print(f'tiempo = "{tiempo}", max_dist = "{max_dist}"')

    result = 0
    
    for i in range(1, (tiempo // 2) + 1):
        dist = i * (tiempo - i)
        if dist > max_dist:
            if tiempo % 2 == 0 and i == tiempo // 2:
                result += 1
            else:
                result += 2
        if verbose:
            print(f'i = "{i}", dist = "{dist}", productos = "{result}"')
            
    # Imprimir el resultado

    print(f'resultado dia 6 - 2 = "{result}"')

if __name__ == "__main__":
    dia6_1("test6_1.txt", verbose=True)
    dia6_2("test6_1.txt", verbose=True)
