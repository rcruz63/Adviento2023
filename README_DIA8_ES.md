# Día 8: Tierra Baldía Encantada ---
Todavía estás montando un camello a través de la Isla del Desierto cuando ves una tormenta de arena acercándose rápidamente. ¡Cuando intentas advertirle al Elfo, ella desaparece ante tus ojos! Para ser justos, acababa de terminar de advertirte sobre fantasmas hace unos minutos.

Uno de los bolsillos del camello está etiquetado como "mapas": efectivamente, está lleno de documentos (tu entrada de rompecabezas) sobre cómo navegar por el desierto. Al menos, estás bastante seguro de eso; uno de los documentos contiene una lista de instrucciones de izquierda/derecha, y el resto de los documentos parecen describir algún tipo de red de nodos etiquetados.

Parece que debes usar las instrucciones de izquierda/derecha para navegar por la red. Quizás si haces que el camello siga las mismas instrucciones, ¡puedas escapar de la tierra baldía encantada!

Después de examinar los mapas por un rato, dos nodos destacan: AAA y ZZZ. Sientes que AAA es donde estás ahora, y debes seguir las instrucciones de izquierda/derecha hasta llegar a ZZZ.

Este formato define cada nodo de la red individualmente. Por ejemplo:

RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
Comenzando con AAA, debes buscar el siguiente elemento basado en la siguiente instrucción de izquierda/derecha en tu entrada. En este ejemplo, comienza con AAA y ve a la derecha (R) eligiendo el elemento derecho de AAA, CCC. Luego, L significa elegir el elemento izquierdo de CCC, ZZZ. Siguiendo las instrucciones de izquierda/derecha, llegas a ZZZ en 2 pasos.

Por supuesto, es posible que no encuentres ZZZ de inmediato. Si te quedas sin instrucciones de izquierda/derecha, repite toda la secuencia de instrucciones según sea necesario: RL realmente significa RLRLRLRLRLRLRLRL... y así sucesivamente. Por ejemplo, aquí hay una situación que requiere 6 pasos para llegar a ZZZ:

LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
Comenzando en AAA, sigue las instrucciones de izquierda/derecha. ¿Cuántos pasos se necesitan para llegar a ZZZ?

## Parte Dos ---
La tormenta de arena te rodea y no estás más cerca de escapar del páramo. Hiciste que el camello siguiera las instrucciones, pero apenas has dejado tu posición inicial. ¡Va a tomar significativamente más pasos escapar!

¿Y si el mapa no es para personas, sino para fantasmas? ¿Los fantasmas están incluso atados por las leyes del espacio-tiempo? Solo hay una forma de descubrirlo.

Tras examinar los mapas un poco más, tu atención se dirige a un hecho curioso: ¡el número de nodos con nombres que terminan en A es igual al número que termina en Z! Si fueras un fantasma, probablemente comenzarías en cada nodo que termina con A y seguirías todos los caminos al mismo tiempo hasta que todos terminen simultáneamente en nodos que terminan con Z.

Por ejemplo:

LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)

Aquí, hay dos nodos de inicio, 11A y 22A (porque ambos terminan con A). Al seguir cada instrucción izquierda/derecha, utiliza esa instrucción para navegar simultáneamente lejos de ambos nodos en los que te encuentras actualmente. Repite este proceso hasta que todos los nodos en los que te encuentras actualmente terminen con Z. (Si solo algunos de los nodos en los que estás terminan con Z, actúan como cualquier otro nodo y continúas como normalmente). En este ejemplo, procederías de la siguiente manera:

Paso 0: Estás en 11A y 22A.
Paso 1: Eliges todos los caminos izquierdos, llevándote a 11B y 22B.
Paso 2: Eliges todos los caminos derechos, llevándote a 11Z y 22C.
Paso 3: Eliges todos los caminos izquierdos, llevándote a 11B y 22Z.
Paso 4: Eliges todos los caminos derechos, llevándote a 11Z y 22B.
Paso 5: Eliges todos los caminos izquierdos, llevándote a 11B y 22C.
Paso 6: Eliges todos los caminos derechos, llevándote a 11Z y 22Z.

Así que, en este ejemplo, terminas completamente en nodos que terminan en Z después de 6 pasos.

Comienza simultáneamente en cada nodo que termine con A. ¿Cuántos pasos se necesitan antes de que solo estés en nodos que terminen con Z?