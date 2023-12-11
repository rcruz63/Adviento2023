# Día 7: Camel Cards ---
Tu viaje con todos los gastos pagados resulta ser un viaje de ida de cinco minutos en un dirigible. (¡Al menos es un dirigible genial!) Te deja en el borde de un vasto desierto y desciende de vuelta a la Isla Isla.

"¿Trajiste las piezas?"

Te giras para ver a un Elfo completamente cubierto de ropa blanca, con gafas y montando un gran camello.

"¿Trajiste las piezas?" pregunta de nuevo, esta vez más fuerte. No estás seguro de qué piezas está buscando; estás aquí para averiguar por qué se detuvo la arena.

"¡Las piezas! Para la arena, ¡sí! Ven conmigo, te lo mostraré". Te invita a subir al camello.

Después de cabalgar un poco por las arenas de la Isla del Desierto, puedes ver lo que parecen ser rocas muy grandes que cubren la mitad del horizonte. El Elfo explica que las rocas están a lo largo de la parte de la Isla del Desierto que está directamente sobre la Isla Isla, lo que dificulta incluso llegar allí. Normalmente, usan grandes máquinas para mover las rocas y filtrar la arena, pero las máquinas se han averiado porque la Isla del Desierto dejó de recibir las piezas que necesitan para arreglarlas.

Ya has asumido que será tu trabajo averiguar por qué se detuvieron las piezas cuando ella pregunta si puedes ayudar. Aceptas automáticamente.

Debido a que el viaje llevará algunos días, ella se ofrece a enseñarte el juego de Camel Cards. Camel Cards es algo similar al póquer excepto que está diseñado para ser más fácil de jugar mientras se monta en un camello.

En Camel Cards, recibes una lista de manos, y tu objetivo es ordenarlas según la fuerza de cada mano. Una mano consta de cinco cartas etiquetadas como A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3 o 2. La fuerza relativa de cada carta sigue este orden, donde A es la más alta y 2 la más baja.

Cada mano es exactamente de un tipo. De más fuerte a más débil, son:

- Cinco iguales, donde las cinco cartas tienen la misma etiqueta: AAAAA
- Cuatro iguales, donde cuatro cartas tienen la misma etiqueta y una carta tiene una etiqueta diferente: AA8AA
- Full, donde tres cartas tienen la misma etiqueta y las dos cartas restantes comparten una etiqueta diferente: 23332
- Tres iguales, donde tres cartas tienen la misma etiqueta y las dos cartas restantes son diferentes entre sí y de cualquier otra carta en la mano: TTT98
- Dos pares, donde dos cartas comparten una etiqueta, otras dos cartas comparten una segunda etiqueta, y la carta restante tiene una tercera etiqueta: 23432
- Un par, donde dos cartas comparten una etiqueta, y las otras tres cartas tienen una etiqueta diferente entre sí y del par: A23A4
- Carta alta, donde todas las etiquetas de las cartas son distintas: 23456

Las manos se ordenan principalmente según su tipo; por ejemplo, cada full es más fuerte que cualquier tres iguales.

Si dos manos tienen el mismo tipo, entra en juego una segunda regla de ordenamiento. Comienza comparando la primera carta de cada mano. Si estas cartas son diferentes, se considera más fuerte la mano con la carta inicial más fuerte. Sin embargo, si la primera carta de cada mano tiene la misma etiqueta, entonces se pasa a considerar la segunda carta de cada mano. Si difieren, la mano con la segunda carta más alta gana; de lo contrario, se continúa con la tercera carta de cada mano, luego la cuarta y, finalmente, la quinta.

Por lo tanto, 33332 y 2AAAA son ambas manos de cuatro iguales, pero 33332 es más fuerte porque su primera carta es más fuerte. De manera similar, 77888 y 77788 son ambos full, pero 77888 es más fuerte porque su tercera carta es más fuerte (y ambas manos tienen la misma primera y segunda carta).

Para jugar a Camel Cards, te dan una lista de manos y su puja correspondiente (tu entrada de rompecabezas). Por ejemplo:

32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
Este ejemplo muestra cinco manos; cada mano va seguida de su cantidad de puja. Cada mano gana una cantidad igual a su puja multiplicada por su rango, donde la mano más débil obtiene el rango 1, la segunda mano más débil obtiene el rango 2, y así sucesivamente hasta la mano más fuerte. Como hay cinco manos en este ejemplo, la mano más fuerte tendrá el rango 5 y su puja será multiplicada por 5.

Así que, el primer paso es ordenar las manos por su fuerza:

32T3K es el único un par y las otras manos son de un tipo más fuerte, por lo que obtiene el rango 1.
KK677 y KTJJT son ambos dos pares. Sus primeras cartas tienen la misma etiqueta, pero la segunda carta de KK677 es más fuerte (K vs T), por lo que KTJJT obtiene el rango 2 y KK677 obtiene el rango 3.
T55J5 y QQQJA son ambos tres iguales. QQQJA tiene una primera carta más fuerte, por lo que obtiene el rango 5 y T55J5 obtiene el rango 4.
Ahora, puedes determinar las ganancias totales de este conjunto de manos sumando el resultado de multiplicar la puja de cada mano por su rango (765 * 1 + 220 * 2 + 28 * 3 + 684 * 4 + 483 * 5). Entonces, las ganancias totales en este ejemplo son 6440.

Encuentra el rango de cada mano en tu conjunto. ¿Cuáles son las ganancias totales?