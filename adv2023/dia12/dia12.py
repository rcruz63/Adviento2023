import os

def contar_configuraciones2(cadena, grupos):
    """ Calcula el valor de las configuraciones ampliadas * 5 """
    cadena = cadena*5
    grupos = [int(y) for y in ((','.join(str(x) for x in grupos))*5).split(',')]
    return contar_configuraciones(cadena, grupos)

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
    def validar_configuracion(cadena, grupos):
        """Valida si una configuración específica cumple con los grupos."""
        contador = []
        actual = 0
        for char in cadena:
            if char == "#":
                actual += 1
            elif actual > 0:
                contador.append(actual)
                actual = 0
        if actual > 0:
            contador.append(actual)
        return contador == grupos

    def generar_combinaciones(cadena, indice=0):
        """Genera todas las combinaciones posibles reemplazando `?`."""
        if indice == len(cadena):
            if validar_configuracion(cadena, grupos):
                return 1
            return 0
        
        if cadena[indice] == "?":
            # Sustituir `?` por `.` y `#`
            return (
                generar_combinaciones(cadena[:indice] + "." + cadena[indice + 1:], indice + 1) +
                generar_combinaciones(cadena[:indice] + "#" + cadena[indice + 1:], indice + 1)
            )
        # Continuar si el carácter no es `?`
        return generar_combinaciones(cadena, indice + 1)

    # Inicia la generación de combinaciones
    return generar_combinaciones(cadena)


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
        termas = termas*5
        confs = confs*5
        configuraciones = [int(x) for x in confs.split(",")]
        result += contar_configuraciones(termas, configuraciones)

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
    assert contar_configuraciones2("???.###", [1, 1, 3]) == 1, "Test 1 fallido. Se esperaba 1 y ha dado " + str(contar_configuraciones("???.###", [1, 1, 3]))
    assert contar_configuraciones2(".??..??...?##.", [1, 1, 3]) == 16384, "Test 2 fallido. Se esperaba 16384 y ha dado " + str(contar_configuraciones(".??..??...?##.", [1, 1, 3]))
    assert contar_configuraciones2("?#?#?#?#?#?#?#?", [1, 3, 1, 6]) == 1, "Test 3 fallido. Se esperaba 1 y ha dado " + str(contar_configuraciones("?#?#?#?#?#?#?", [1, 3, 1, 6]))
    assert contar_configuraciones2("????.#...#...", [4, 1, 1]) == 16, "Test 4 fallido. Se esperaba 16 y ha dado " + str(contar_configuraciones("????.#...#...", [4, 1, 1]))
    assert contar_configuraciones2("????.######..#####.", [1, 6, 5]) == 2500, "Test 5 fallido. Se esperaba 2500 y ha dado " + str(contar_configuraciones("????.######..#####.", [1, 6, 5]))
    assert contar_configuraciones2("?###????????", [3, 2, 1]) == 506250, "Test 6 fallido. Se esperaba 506250 y ha dado " + str(contar_configuraciones("?###????????", [3, 2, 1]))
    print("Todos los tests pasaron correctamente.")

if __name__ == "__main__":

    # test_contar_configuraciones()
    # test_contar_configuraciones2()
    # dia12_1("test12_1.txt", verbose=False)
    dia12_1("data12_1.txt", verbose=False)
    # dia12_2("test12_2.txt", verbose=True)
