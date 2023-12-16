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