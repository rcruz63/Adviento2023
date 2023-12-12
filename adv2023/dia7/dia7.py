import os
from functools import total_ordering, reduce

# Definir una clase para representar una jugada
@total_ordering
class Jugada:
    """ Clase para representar una jugada de poker. """
    def __init__(self, mano, apuesta):
        self.mano = mano.upper()
        self.apuesta = int(apuesta)
        self.clase = self.evaluar_mano()
        self.valor = mano.replace("A", "Z").replace("K", "Y").replace("Q", "X").replace("J", "W").replace("T", "V")

    def __repr__(self):
        return f"Jugada({self.mano}, {self.apuesta}, {self.clase}, {self.valor})"

    def __str__(self):
        return f"Jugada({self.mano}, {self.apuesta}, {self.clase}, {self.valor})"

    def __lt__(self, other):
        if self.clase == other.clase:
            return self.valor < other.valor
        else:
            return self.clase < other.clase

    def __eq__(self, other):
        if self.clase == other.clase and self.valor == other.valor:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.clase == other.clase:
            return self.valor > other.valor
        else:
            return self.clase > other.clase

    def __le__(self, other):
        if self.clase == other.clase:
            return self.valor <= other.valor
        else:
            return self.clase <= other.clase

    def __ge__(self, other):
        if self.clase == other.clase:
            return self.valor > other.valor
        else:
            return self.clase > other.clase

    def __ne__(self, other):
        if self.clase != other.clase or self.valor != other.valor:
            return True
        else:
            return False

    def evaluar_mano(self):
        """ Función para evaluar una mano de poker. """
        if len(set(self.mano)) == 1:
            return 6
        elif len(set(self.mano)) == 2:
            counts = {x: self.mano.count(x) for x in set(self.mano)}
            if 3 in counts.values():
                return 4
            else:
                return 5
        elif len(set(self.mano)) == 3:
            counts = {x: self.mano.count(x) for x in set(self.mano)}
            if 3 in counts.values():
                return 3
            else:
                return 2
        elif len(set(self.mano)) == 4:
            return 1
        else:
            return 0


def dia7_1(data, verbose: bool = False):
    """ Función principal del día 7-1. """

    current_dir = os.path.dirname(os.path.realpath(__file__))
    data_path = os.path.join(current_dir, data)
    if verbose:
        print(f'Opening file {data_path}')

    jugadas = open(data_path, encoding="utf-8").read().split('\n')
    manos = [Jugada(jugada.split()[0], jugada.split()[1]) for jugada in jugadas]
    sorted_manos = sorted(manos)
    if verbose:
        print(manos)
        print(sorted_manos)

    result = reduce(lambda acc, jugada: acc + jugada.apuesta * (sorted_manos.index(jugada) + 1), sorted_manos, 0)

    print(f'resultado dia 7 - 1 = "{result}"')


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
    dia7_1("test7_1.txt", verbose=False)
    #dia7_2("test7_2.txt", verbose=True)
