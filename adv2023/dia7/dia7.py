import os

def evaluar_mano(mano):
    if len(set(mano)) == 1:
        return 6
    elif len(set(mano)) == 2:
        counts = {x: mano.count(x) for x in set(mano)}
        if 3 in counts.values():
            return 4
        else:
            return 5
    elif len(set(mano)) == 3:
        counts = {x: mano.count(x) for x in set(mano)}
        if 3 in counts.values():
            return 3
        else:
            return 2
    elif len(set(mano)) == 4:
        return 1
    else:
        return 0


def dia7_1(data, verbose: bool = False):
    """ Función principal del día 7-1. """

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


def dia7_2(data, verbose: bool = False):
    """ Función principal del día 7-2. """

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

    # Ejemplo de uso:
    mano = "KKKKK"
    resultado = evaluar_mano(mano)
    print(f"El resultado de la mano {mano} es: {resultado}")
    mano = "A2AAA"
    resultado = evaluar_mano(mano)
    print(f"El resultado de la mano {mano} es: {resultado}")
    mano = "12121"
    resultado = evaluar_mano(mano)
    print(f"El resultado de la mano {mano} es: {resultado}")
    mano = "35336"
    resultado = evaluar_mano(mano)
    print(f"El resultado de la mano {mano} es: {resultado}")
    mano = "99565"
    resultado = evaluar_mano(mano)
    print(f"El resultado de la mano {mano} es: {resultado}")
    mano = "32T3K"
    resultado = evaluar_mano(mano)
    print(f"El resultado de la mano {mano} es: {resultado}")
    mano = "32T3K"
    resultado = evaluar_mano(mano)
    print(f"El resultado de la mano {mano} es: {resultado}")
    mano = "32QAK"
    resultado = evaluar_mano(mano)
    print(f"El resultado de la mano {mano} es: {resultado}")
    mano = "32T3K"
    resultado = evaluar_mano(mano)
    print(f"El resultado de la mano {mano} es: {resultado}")


    #dia7_1("test7_1.txt", verbose=False)
    #dia7_2("test7_2.txt", verbose=True)
