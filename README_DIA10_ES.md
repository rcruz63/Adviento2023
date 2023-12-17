# Día 10: Laberinto de Tuberías ---

Utilizas el ala delta para elevarte con el aire caliente desde Desert Island hasta la isla flotante de metal. Esta isla es sorprendentemente fría y definitivamente no hay termales para planear, así que dejas tu ala delta atrás.

Vagas por un tiempo, pero no encuentras a ninguna persona ni animal. Sin embargo, ocasionalmente encuentras carteles indicando "Aguas Termales" apuntando en una dirección aparentemente consistente; quizás puedas encontrar a alguien en las aguas termales y preguntarles dónde se fabrican las piezas de la máquina del desierto.

El paisaje aquí es alienígena; incluso las flores y árboles están hechos de metal. Mientras te detienes para admirar un pasto metálico, notas algo metálico que se escabulle en tu visión periférica ¡y salta dentro de un gran tubo! No parecía ningún animal que hayas visto antes; si quieres verlo mejor, tendrás que adelantarte.

Escaneando el área, descubres que todo el campo en el que estás parado está densamente lleno de tuberías; fue difícil de ver al principio porque son del mismo color plateado metálico que el "suelo". Haces un rápido dibujo de todas las tuberías superficiales que puedes ver (tu entrada de rompecabezas).

Las tuberías están dispuestas en una rejilla bidimensional de casillas:

| es una tubería vertical que conecta norte y sur.
- es una tubería horizontal que conecta este y oeste.
L es un codo de 90 grados que conecta norte y este.
J es un codo de 90 grados que conecta norte y oeste.
7 es un codo de 90 grados que conecta sur y oeste.
F es un codo de 90 grados que conecta sur y este.
. es el suelo; no hay tubería en esta casilla.
S es la posición de inicio del animal; hay una tubería en esta casilla, pero tu dibujo no muestra qué forma tiene la tubería.
Basado en la acústica del correr del animal, estás seguro de que la tubería que contiene al animal es un gran bucle continuo.

Por ejemplo, aquí hay un bucle cuadrado de tuberías:

.....
.F-7.
.|.|.
.L-J.
.....
Si el animal hubiera entrado en este bucle en la esquina noroeste, el dibujo se vería así:

.....
.S-7.
.|.|.
.L-J.
.....
En el diagrama anterior, la casilla S sigue siendo un codo F de 90 grados: puedes decirlo por cómo se conectan las tuberías adyacentes a ella.

¡Desafortunadamente, también hay muchas tuberías que no están conectadas al bucle! Este dibujo muestra el mismo bucle que el anterior:

-L|F7
7S-7|
L|7||
-L-J|
L|-JF
En el diagrama anterior, aún puedes averiguar qué tuberías forman el bucle principal: son las que están conectadas a S, las tuberías a las que se conectan esas tuberías, las tuberías a las que se conectan esas tuberías, y así sucesivamente. Cada tubería en el bucle principal se conecta a sus dos vecinas (incluyendo a S, que tendrá exactamente dos tuberías conectadas a ella, y se asume que se conecta nuevamente a esas dos tuberías).

Aquí hay un dibujo que contiene un bucle principal ligeramente más complejo:

..F7.
.FJ|.
SJ.L7
|F--J
LJ...
Aquí está el mismo dibujo de ejemplo con las casillas extra, que no forman parte del bucle principal, también mostradas:

7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ
Si quieres adelantarte al animal, deberías encontrar la casilla en el bucle que está más lejos de la posición de inicio. Dado que el animal está en la tubería, no tiene sentido medir esto por distancia directa. En lugar de eso, necesitas encontrar la casilla a la que se tardaría el mayor número de pasos a lo largo del bucle en llegar desde el punto de inicio, sin importar en qué dirección haya ido el animal alrededor del bucle.

En el primer ejemplo con el bucle cuadrado:

.....
.S-7.
.|.|.
.L-J.
.....
Puedes contar la distancia que cada casilla del bucle tiene desde el punto de inicio de esta manera:

.....
.012.
.1.3.
.234.
.....
En este ejemplo, el punto más lejano desde el inicio está a 4 pasos de distancia.

Aquí está de nuevo el bucle más complejo:

..F7.
.FJ|.
SJ.L7
|F--J
LJ...
Aquí están las distancias para cada casilla en ese bucle:

..45.
.236.
01.78
14567
23...
Encuentra el único bucle gigante que comienza en S. ¿Cuántos pasos a lo largo del bucle se necesitan para llegar desde la posición de inicio al punto más alejado de la posición de inicio?

##  Parte Dos ---

Llegas rápidamente al punto más lejano del bucle, pero el animal nunca aparece. ¿Quizás su nido está dentro del área encerrada por el bucle?

Para determinar si vale la pena tomarse el tiempo para buscar tal nido, debes calcular cuántas casillas están contenidas dentro del bucle. Por ejemplo:

...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
...........
El bucle anterior encierra solo cuatro casillas: los dos pares de . en el suroeste y sureste (marcados como I abajo). Las casillas . centrales (marcadas como O abajo) no están en el bucle. Aquí está el mismo bucle nuevamente con esas regiones marcadas:

...........
.S-------7.
.|F-----7|.
.||OOOOO||.
.||OOOOO||.
.|L-7OF-J|.
.|II|O|II|.
.L--JOL--J.
.....O.....
De hecho, ni siquiera es necesario que haya un camino completo hacia afuera para que las casillas cuenten como fuera del bucle; ¡se permite el paso entre tuberías! Aquí, I todavía está dentro del bucle y O todavía está fuera del bucle:

..........
.S------7.
.|F----7|.
.||OOOO||.
.||OOOO||.
.|L-7F-J|.
.|II||II|.
.L--JL--J.
..........
En ambos ejemplos anteriores, 4 casillas están encerradas por el bucle.

Aquí tienes un ejemplo más grande:

.F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ...
El boceto anterior tiene muchos trozos aleatorios de suelo, algunos de los cuales están en el bucle (I) y algunos de los cuales están fuera (O):

OF----7F7F7F7F-7OOOO
O|F--7||||||||FJOOOO
O||OFJ||||||||L7OOOO
FJL7L7LJLJ||LJIL-7OO
L--JOL7IIILJS7F-7L7O
OOOOF-JIIF7FJ|L7L7L7
OOOOL7IF7||L7|IL7L7|
OOOOO|FJLJ|FJ|F7|OLJ
OOOOFJL-7O||O||||OOO
OOOOL---JOLJOLJLJOOO
En este ejemplo más grande, 8 casillas están encerradas por el bucle.

Cualquier casilla que no sea parte del bucle principal puede contar como si estuviera encerrada por el bucle. Aquí tienes otro ejemplo con muchos trozos de tubería que no están conectados al bucle principal en absoluto:

FF7FSF7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L
Aquí solo se marcan las casillas que están encerradas por el bucle con I:

FF7FSF7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJIF7FJ-
L---JF-JLJIIIIFJLJJ7
|F|F-JF---7IIIL7L|7|
|FFJF7L7F-JF7IIL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L
En este último ejemplo, 10 casillas están encerradas por el bucle.

Calcula si tienes tiempo para buscar el nido calculando el área dentro del bucle. ¿Cuántas casillas están encerradas por el bucle?
