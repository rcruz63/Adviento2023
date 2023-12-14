import os

from typing import List
from functools import reduce

def calculate_differences(numbers: List[int]) -> List[int]:
    return [j-i for i, j in zip(numbers[:-1], numbers[1:])]

def process_sequence(sequence: List[int]) -> List[List[int]]:
    results = [sequence]
    while results[-1] != [0] * (len(results[-1])):
        results.append(calculate_differences(results[-1]))
        #print (results)
    return results

def add_elements(lists: List[List[int]]) -> List[int]:
    lists = lists[::-1]
    carry = 0
    for lst in lists:
        carry += lst[-1]
        lst.append(carry)
    lists = lists[::-1]
    return lists[0][-1]

def add_elements_start(lists: List[List[int]]) -> List[int]:
    lists = lists[::-1]
    carry = 0
    for lst in lists:
        carry = lst[0] - carry
        lst.insert(0, carry)
    lists = lists[::-1]
    # print ("Nuevas seceuncias: ", lists)
    return lists[0][0]

def dia9_1(data, verbose: bool = False):
    """ Función principal del día 9-1. """

    current_dir = os.path.dirname(os.path.realpath(__file__))
    data_path = os.path.join(current_dir, data)
    if verbose:
        print(f'Opening file {data_path}')

    # Leer el archivo
    secuencias = [list(map(int, linea.split())) for linea in open(data_path, encoding="utf-8").read().split('\n')]

    trazas = [process_sequence(secuencia) for secuencia in secuencias]
    result1 = reduce(lambda acc, traza: acc + add_elements(traza), trazas, 0)
    result2 = reduce(lambda acc, traza: acc + add_elements_start(traza), trazas, 0)

    # Imprimir el resultado

    print(f'resultado dia 9 - 1 = "{result1}"')
    print(f'resultado dia 9 - 2 = "{result2}"')

if __name__ == "__main__":
    dia9_1("data9_1.txt", verbose=False)
    #dia9_2("test9_2.txt", verbose=True)
