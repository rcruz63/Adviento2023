# ¡Claro! Aquí tienes la traducción al español:

--- Día 9: Mantenimiento de Mirage ---
Cabalgas el camello a través de la tormenta de arena y te detienes donde los mapas del fantasma te indicaron que lo hicieras. ¡La tormenta de arena luego disminuye, de alguna manera viéndote parado en un oasis!

El camello va a buscar agua y tú estiras el cuello. Al mirar hacia arriba, ¡descubres lo que debe ser otra isla flotante gigante, esta hecha de metal! Debe ser de donde vienen las piezas para arreglar las máquinas de arena.

¡Incluso hay un ala delta parcialmente enterrada en la arena aquí! Una vez que salga el sol y caliente la arena, ¡quizás puedas usar el ala delta y el aire caliente para llegar hasta la isla de metal!

Mientras esperas que salga el sol, admiras el oasis escondido aquí en medio de Desert Island. Debe tener un ecosistema delicado; podrías tomar algunas lecturas ecológicas mientras esperas. Tal vez puedas informar cualquier inestabilidad ambiental que encuentres a alguien para que el oasis pueda estar disponible para el próximo viajero agotado por la tormenta de arena.

Sacaste tu práctico Sensor de Estabilidad de Oasis y Arena y analizas tus alrededores. El OASIS produce un informe de muchos valores y cómo están cambiando con el tiempo (tu entrada de rompecabezas). Cada línea en el informe contiene la historia de un solo valor. Por ejemplo:

0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45

Para proteger mejor el oasis, tu informe ambiental debe incluir una predicción del próximo valor en cada historia. Para hacer esto, comienza haciendo una nueva secuencia a partir de la diferencia en cada paso de tu historia. Si esa secuencia no consiste en todo ceros, repite este proceso, utilizando la secuencia que acabas de generar como la secuencia de entrada. Una vez que todos los valores en tu última secuencia son ceros, puedes extrapolar cuál debería ser el próximo valor de la historia original.

En el conjunto de datos anterior, la primera historia es 0 3 6 9 12 15. Debido a que los valores aumentan en 3 en cada paso, la primera secuencia de diferencias que generas será 3 3 3 3 3. Observa que esta secuencia tiene un valor menos que la secuencia de entrada porque en cada paso considera dos números de la entrada. Dado que estos valores no son todos cero, repite el proceso: los valores difieren en 0 en cada paso, por lo que la próxima secuencia es 0 0 0 0. Esto significa que ¡tienes suficiente información para extrapolar la historia! Visualmente, estas secuencias se pueden organizar así:

0   3   6   9  12  15
  3   3   3   3   3
    0   0   0   0

Para extrapolar, comienza agregando un nuevo cero al final de tu lista de ceros; porque los ceros representan diferencias entre los dos valores encima de ellos, esto también significa que ahora hay un marcador de posición en cada secuencia encima de él:

0   3   6   9  12  15   B
  3   3   3   3   3   A
    0   0   0   0   0

Luego, comienza a llenar los marcadores de posición de abajo hacia arriba. A necesita ser el resultado de aumentar 3 (el valor a su izquierda) en 0 (el valor debajo de él); esto significa que A debe ser 3:

0   3   6   9  12  15   B
  3   3   3   3   3   3
    0   0   0   0   0

Finalmente, puedes completar B, que necesita ser el resultado de aumentar 15 (el valor a su izquierda) en 3 (el valor debajo de él), o 18:

0   3   6   9  12  15  18
  3   3   3   3   3   3
    0   0   0   0   0

Entonces, ¡el próximo valor de la primera historia es 18!

Encontrar diferencias de todo ceros para la segunda historia requiere una secuencia adicional:

1   3   6  10  15  21
  2   3   4   5   6
    1   1   1   1
      0   0   0

Luego, siguiendo el mismo proceso que antes, trabaja en el próximo valor de cada secuencia de abajo hacia arriba:

1   3   6  10  15  21  28
  2   3   4   5   6   7
    1   1   1   1   1
      0   0   0   0

Entonces, el próximo valor de la segunda historia es 28.

La tercera historia requiere aún más secuencias, pero su próximo valor se puede encontrar de la misma manera:

10  13  16  21  30  45  68
   3   3   5   9  15  23
     0   2   4   6   8
       2   2   2   2
         0   0   0

Entonces, el próximo valor de la tercera historia es 68.

Si encuentras el próximo valor para cada historia en este ejemplo y los sumas, ¡obtienes 114!

Analiza tu informe OASIS y extrapola el próximo valor para cada historia. ¿Cuál es la suma de estos valores extrapolados?

## --- Parte Dos ---
Por supuesto, sería bueno incluir aún más historial en tu informe. Seguramente, ¿sería seguro simplemente extrapolar hacia atrás también, verdad?

Para cada historial, repite el proceso de encontrar diferencias hasta que la secuencia de diferencias sea completamente cero. Entonces, en lugar de agregar un cero al final y completar los próximos valores de cada secuencia anterior, en cambio deberías agregar un cero al principio de tu secuencia de ceros, luego llenar con nuevos valores iniciales para cada secuencia anterior.

En particular, esto es cómo se ve el tercer ejemplo de historial al extrapolar hacia atrás en el tiempo:

5  10  13  16  21  30  45
  5   3   3   5   9  15
   -2   0   2   4   6
      2   2   2   2
        0   0   0
Añadir los nuevos valores en el lado izquierdo de cada secuencia de abajo hacia arriba eventualmente revela el nuevo valor más a la izquierda del historial: 5.

Hacer esto para los datos de ejemplo restantes resulta en valores anteriores de -3 para el primer historial y 0 para el segundo historial. Sumando los tres nuevos valores da como resultado 2.

Analiza nuevamente tu informe OASIS, esta vez extrapolando el valor anterior para cada historial. ¿Cuál es la suma de estos valores extrapolados?