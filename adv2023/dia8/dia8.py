import os
import math

def follow_gost(moves, mappings):
    origen = [key for key in mappings if key.endswith('A')]
    print (f'origen: {origen}')
    num_moves = 0
    while True:
        for move in moves:
            left_right =  [mappings[key] for key in origen if key in mappings]
            if num_moves % 1000000 == 0:
                print (f'n:{num_moves} - origen: {origen}, left_right: {left_right}')
            # print (f'origen: {origen}, left_right: {left_right}')
            # print (f'move: {move}')
            old_origen = origen
            num_moves += 1
            if move == 'L':
                origen = [left[0] for left in left_right]
            else:
                origen = [right[1] for right in left_right]
            if origen == old_origen:
                exit(f'ERROR: origen == old_origen: {origen}')
            if all(cadena.endswith('Z') for cadena in origen):
                return num_moves
            
def bucles(moves, mappings):

    origen = [key for key in mappings if key.endswith('A')]
    bucles = []

    for fantasma in origen:
        print (f'fantasma: {fantasma}')
        inicio = fantasma
        num_moves = 0
        bucle = 0
        while bucle < 2:
            for move in moves:
                left_right =  mappings[inicio]
                #print (f'N: {num_moves} - origen: {inicio}, left_right: {left_right}')
                old_inicio = inicio
                num_moves += 1
                if move == 'L':
                    inicio = left_right[0]
                else:
                    inicio = left_right[1]
                if inicio == old_inicio:
                    exit(f'ERROR: origen == old_origen: {inicio}')
                if inicio.endswith('Z'):
                    bucle += 1
                    if bucle == 1:
                        primero = num_moves
                        primer_fin = inicio
                        num_moves = 0
                    else:
                        bucles.append({fantasma: [primer_fin, primero, inicio, num_moves]})
                        print (f'fantasma: {fantasma}, bucle: {bucle}, primero: {primero}, primer_fin: {primer_fin}, inicio: {inicio}, num_moves: {num_moves}')
                        num_moves = 0

    numeros = [list(bucle.values())[0][3] for bucle in bucles]
    print (f'numeros: {numeros}')

    mcm = lambda a, b: a * b // math.gcd(a, b)
    resultado = 1
    for num in numeros:
        resultado = mcm(resultado, num)

    return resultado

def follow_path(moves, mappings, inicio="AAA"):
    origen = inicio
    num_moves = 0
    while origen != "ZZZ":
        for move in moves:
            left_right = mappings[origen]
            # print (f'origen: {origen}, left_right: {left_right}')
            # print (f'move: {move}')
            old_origen = origen
            num_moves += 1
            if move == 'L':
                origen = left_right[0]
            else:
                origen = left_right[1]
            if origen == old_origen:
                exit(f'ERROR: origen == old_origen: {origen}')
            if origen == "ZZZ":
                return num_moves

def lr_moves(lr_text):
    return [elemento.strip("' ") for elemento in lr_text.replace('(', '').replace(')', '').split(',')]

def dia8_1(tipo: int, data, verbose: bool = False):
    """ Función principal del día 8-1. """

    current_dir = os.path.dirname(os.path.realpath(__file__))
    data_path = os.path.join(current_dir, data)

    moves, list_mappings = open(data_path, encoding="utf-8").read().split('\n\n')
    print (moves)

    mappings = {map.split('=')[0].strip():lr_moves(map.split('=')[1].strip()) for map in list_mappings.split('\n')}
    print (mappings)
            
    # Imprimir el resultado

    if tipo == 1 or tipo == 3:
        result = follow_path(moves, mappings)

        print(f'resultado dia 8 - 1 = "{result}"')

    if tipo == 2 or tipo == 3:
        #result = follow_gost(moves, mappings)
        result = bucles(moves, mappings)

        print(f'resultado dia 8 - 2 = "{result}"')

if __name__ == "__main__":
    #dia8_1(1, "test8_2.txt", verbose=False)
    dia8_1(2, "data8_1.txt", verbose=True)
