import os

def follow_gost(moves, mappings):
    origen = [key for key in mappings if key.endswith('A')]
    print (f'origen: {origen}')
    num_moves = 0
    while True:
        for move in moves:
            left_right =  [mappings[key] for key in origen if key in mappings]
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

def follow_path(moves, mappings):
    origen = "AAA"
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
        result = follow_gost(moves, mappings)

        print(f'resultado dia 8 - 2 = "{result}"')

if __name__ == "__main__":
    dia8_1(1, "test8_2.txt", verbose=False)
    dia8_1(2, "test8_3.txt", verbose=True)
