import os

def contar_configuraciones(cadena, grupos):
    """
    Calcula el número de configuraciones posibles para una cadena con interrogaciones 
    y una lista de grupos de parrillas.
    
    Args:
        cadena (str): Cadena con puntos ".", parrillas "#" e interrogaciones "?".
        grupos (list[int]): Lista de números que representan los tamaños de los grupos contiguos de "#".
    
    Returns:
        int: Número de configuraciones posibles que cumplen con los grupos dados.
    """
    memo = {}

    def dp(indice, grupo_actual):
        """
        Función recursiva con memoización para calcular configuraciones posibles.
        
        Args:
            indice (int): Índice actual en la cadena.
            grupo_actual (int): Grupo actual que estamos intentando satisfacer.
        
        Returns:
            int: Número de configuraciones válidas desde este punto.
        """
        # Caso base: Si hemos completado todos los grupos, el resto debe ser "."
        if grupo_actual == len(grupos):
            return all(c == '.' or c == '?' for c in cadena[indice:])

        # Si hemos terminado la cadena antes de completar los grupos, no es válido
        if indice >= len(cadena):
            return 0

        # Verificar si ya hemos calculado este estado
        estado = (indice, grupo_actual)
        if estado in memo:
            return memo[estado]

        # Contador de configuraciones válidas
        total_configuraciones = 0

        # Opción 1: Intentar satisfacer el grupo actual
        tam_grupo = grupos[grupo_actual]
        if indice + tam_grupo <= len(cadena):
            subcadena = cadena[indice:indice + tam_grupo]
            if all(c == '#' or c == '?' for c in subcadena) and (
                indice + tam_grupo == len(cadena) or cadena[indice + tam_grupo] in ('.', '?')
            ):
                # Avanzar al siguiente grupo
                total_configuraciones += dp(indice + tam_grupo + 1, grupo_actual + 1)

        # Opción 2: Saltar el carácter actual si es "."
        if cadena[indice] in ('.', '?'):
            total_configuraciones += dp(indice + 1, grupo_actual)

        # Guardar en memo y retornar
        memo[estado] = total_configuraciones
        return total_configuraciones

    # Iniciar la recursión desde el índice 0 y el primer grupo
    return dp(0, 0)


def contar_configuraciones2(cadena, grupos):
    """
    Calcula el número de configuraciones posibles para una cadena y grupos extendidos.
    Extiende la cadena y los grupos según las reglas de la parte dos.
    
    Args:
        cadena (str): Cadena inicial con puntos ".", parrillas "#" e interrogaciones "?".
        grupos (list[int]): Lista inicial de grupos de parrillas "#".
    
    Returns:
        int: Número de configuraciones posibles con la cadena y los grupos extendidos.
    """
    print(f"Contar configuraciones 2 Inicio: {cadena} - {grupos}")
    cadena = '?'.join([cadena] * 5)
    grupos = grupos*5
    print(f"Contar configuraciones 2 Llamada: {cadena} - {grupos}")
    return contar_configuraciones(cadena, grupos)

def dia12_1(data, verbose: bool = False):
    """ Función principal del día 12-1. """

    current_dir = os.path.dirname(os.path.realpath(__file__))
    data_path = os.path.join(current_dir, data)
    if verbose:
        print(f'Opening file {data_path}')

    registros = open(data_path, encoding="utf-8").read().split('\n')
    result = 0
    for registro in registros:
        # Decodificar la linea
        termas, confs = registro.split()
        configuraciones = [int(x) for x in confs.split(",")]
        result += contar_configuraciones(termas, configuraciones)
            
    # Imprimir el resultado

    print(f'resultado dia 12 - 1 = "{result}"')


def dia12_2(data, verbose: bool = False):
    """ Función principal del día 12-1. """

    current_dir = os.path.dirname(os.path.realpath(__file__))
    data_path = os.path.join(current_dir, data)
    if verbose:
        print(f'Opening file {data_path}')

    registros = open(data_path, encoding="utf-8").read().split('\n')
    result = 0
    for registro in registros:
        # Decodificar la linea
        termas, confs = registro.split()
        configuraciones = [int(x) for x in confs.split(",")]
        result += contar_configuraciones2(termas, configuraciones)

    # Imprimir el resultado

    print(f'resultado dia 12 - 2 = "{result}"')

def test_contar_configuraciones():
    """Testea la función contar_configuraciones con diferentes casos de prueba."""
    assert contar_configuraciones("???.###", [1, 1, 3]) == 1, "Test 1 fallido. Se esperaba 1 y ha dado " + str(contar_configuraciones("???.###", [1, 1, 3]))
    assert contar_configuraciones(".??..??...?##.", [1, 1, 3]) == 4, "Test 2 fallido. Se esperaba 4 y ha dado " + str(contar_configuraciones(".??..??...?##.", [1, 1, 3]))
    assert contar_configuraciones("?#?#?#?#?#?#?#?", [1, 3, 1, 6]) == 1, "Test 3 fallido. Se esperaba 1 y ha dado " + str(contar_configuraciones("?#?#?#?#?#?#?", [1, 3, 1, 6]))
    assert contar_configuraciones("????.#...#...", [4, 1, 1]) == 1, "Test 4 fallido. Se esperaba 1 y ha dado " + str(contar_configuraciones("????.#...#...", [4, 1, 1]))
    assert contar_configuraciones("????.######..#####.", [1, 6, 5]) == 4, "Test 5 fallido. Se esperaba 4 y ha dado " + str(contar_configuraciones("????.######..#####.", [1, 6, 5]))
    assert contar_configuraciones("?###????????", [3, 2, 1]) == 10, "Test 6 fallido. Se esperaba 10 y ha dado " + str(contar_configuraciones("?###????????", [3, 2, 1]))
    print("Todos los tests pasaron correctamente.")

def test_contar_configuraciones2():
    """Testea la función contar_configuraciones con diferentes casos de prueba."""
    assert contar_configuraciones2("???.###", [1, 1, 3]) == 1, "Test 1 fallido. Se esperaba 1 y ha dado " + str(contar_configuraciones2("???.###", [1, 1, 3]))
    assert contar_configuraciones2(".??..??...?##.", [1, 1, 3]) == 16384, "Test 2 fallido. Se esperaba 16384 y ha dado " + str(contar_configuraciones2(".??..??...?##.", [1, 1, 3]))
    assert contar_configuraciones2("?#?#?#?#?#?#?#?", [1, 3, 1, 6]) == 1, "Test 3 fallido. Se esperaba 1 y ha dado " + str(contar_configuraciones2("?#?#?#?#?#?#?", [1, 3, 1, 6]))
    assert contar_configuraciones2("????.#...#...", [4, 1, 1]) == 16, "Test 4 fallido. Se esperaba 16 y ha dado " + str(contar_configuraciones2("????.#...#...", [4, 1, 1]))
    assert contar_configuraciones2("????.######..#####.", [1, 6, 5]) == 2500, "Test 5 fallido. Se esperaba 2500 y ha dado " + str(contar_configuraciones2("????.######..#####.", [1, 6, 5]))
    assert contar_configuraciones2("?###????????", [3, 2, 1]) == 506250, "Test 6 fallido. Se esperaba 506250 y ha dado " + str(contar_configuraciones2("?###????????", [3, 2, 1]))
    print("Todos los tests pasaron correctamente.")

if __name__ == "__main__":

    # test_contar_configuraciones()
    # test_contar_configuraciones2()
    # dia12_1("test12_1.txt", verbose=False)
    dia12_2("data12_1.txt", verbose=False)
    # dia12_2("test12_1.txt", verbose=False)
