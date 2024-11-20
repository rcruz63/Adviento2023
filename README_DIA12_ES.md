# Día 12: Aguas Termales
¡Finalmente llegas a las aguas termales! Puedes ver vapor elevándose desde áreas apartadas conectadas al edificio principal y ornamentado.

Cuando te giras para entrar, el investigador te detiene.
—"Espera, ¿no estabas buscando las aguas termales?"
Le indicas que esto definitivamente parece serlo.

—"¡Oh, lo siento! Es un error común. Esto es en realidad un onsen. Las aguas termales están al lado."

Miras en la dirección que el investigador señala y de repente notas las enormes hélices metálicas que se alzan hacia el cielo.
—"¡Por aquí!"

Solo necesitas unos pocos pasos más para llegar a la puerta principal del área vallada que contiene las aguas termales. Cruzas la puerta y entras en un pequeño edificio administrativo.

—"¡Hola! ¿Qué te trae por las aguas termales hoy? Perdón, no están muy calientes ahora; estamos teniendo una escasez de lava en este momento."
Preguntas sobre las piezas de máquina faltantes para la Isla del Desierto.

—"¡Oh! Toda la Isla del Engranaje está fuera de servicio actualmente. Nada se está fabricando en este momento, no hasta que consigamos más lava para calentar nuestras forjas... y nuestras termas. ¡Las termas no son muy termales si no están calientes!"

—"Oye, ¿podrías subir y ver por qué la lava dejó de fluir? Las termas están demasiado frías para operar normalmente, pero deberíamos poder encontrar una lo suficientemente activa para lanzarte allí arriba."

Hay solo un problema: muchas de las termas están en mal estado, ¡así que no están seguros de cuáles serían seguras para usar! Peor aún, sus registros de condiciones de las termas dañadas (tu entrada del rompecabezas) también están dañados. Necesitarás ayudarles a reparar esos registros.

En el campo gigante justo afuera, las termas están dispuestas en filas. Para cada fila, los registros de condiciones muestran cada terma y si está operativa (.) o dañada (#). Esta es la parte de los registros de condiciones que está dañada; para algunas termas, simplemente no se sabe (?) si están operativas o dañadas.

Sin embargo, el ingeniero que produjo los registros de condiciones también duplicó parte de esta información en un formato diferente. Después de la lista de termas para una fila dada, se detalla el tamaño de cada grupo contiguo de termas dañadas en el orden en que aparecen en la fila. Esta lista siempre incluye todas las termas dañadas, y cada número representa el tamaño total de un grupo contiguo (es decir, los grupos siempre están separados por al menos una terma operativa: #### siempre será 4, nunca 2,2).

Por ejemplo, los registros de condiciones sin termas desconocidas podrían verse así:

```text
#.#.### 1,1,3  
.#...#....###. 1,1,3  
.#.###.#.###### 1,3,1,6  
####.#...#... 4,1,1  
#....######..#####. 1,6,5  
.###.##....# 3,2,1  
```

Sin embargo, los registros de condiciones están parcialmente dañados; algunas de las termas tienen condiciones desconocidas (?). Por ejemplo:

```text
???.### 1,1,3  
.??..??...?##. 1,1,3  
?#?#?#?#?#?#?#? 1,3,1,6  
????.#...#... 4,1,1  
????.######..#####. 1,6,5  
?###???????? 3,2,1  
```

Con esta información, tu tarea es averiguar cuántas configuraciones diferentes de termas operativas y dañadas cumplen con los criterios dados en cada fila.

En la primera línea (???.### 1,1,3), hay exactamente una forma de separar grupos de uno, uno y tres termas dañadas (en ese orden) en esa fila: las primeras tres termas desconocidas deben estar dañadas, luego operativas, luego dañadas (#.#), haciendo que la fila completa sea #.#.###.

La segunda línea es más interesante: .??..??...?##. 1,1,3 podría tener un total de cuatro configuraciones diferentes. El último ? debe estar siempre dañado (para cumplir con el grupo contiguo final de tres termas dañadas), y cada ?? debe ocultar exactamente una de las dos termas dañadas. (Ningún ?? puede contener ambas termas dañadas o formarían un único grupo contiguo de dos; si eso fuera cierto, los números serían 2,3 en lugar de 1,1,3). Como cada ?? puede ser #. o .#, hay cuatro configuraciones posibles.

La última línea es consistente con diez configuraciones diferentes. Debido a que el primer número es 3, los dos primeros ? deben ser . (si alguno fuera #, el primer número tendría que ser 4 o más). Sin embargo, la siguiente sección de condiciones desconocidas tiene muchas maneras diferentes de contener grupos de dos y uno termas dañadas:

```text
?###???????? 3,2,1  
.###.##.#...  
.###.##..#..  
.###.##...#.  
.###.##....#  
.###..##.#..  
.###..##..#.  
.###..##...#  
.###...##.#.  
.###...##..#  
.###....##.#  
```

En este ejemplo, el número de configuraciones posibles para cada fila es:

```text
???.### 1,1,3 - 1 configuración  
.??..??...?##. 1,1,3 - 4 configuraciones  
?#?#?#?#?#?#?#? 1,3,1,6 - 1 configuración  
????.#...#... 4,1,1 - 1 configuración  
????.######..#####. 1,6,5 - 4 configuraciones  
?###???????? 3,2,1 - 10 configuraciones  
```

Sumando todas las configuraciones posibles se obtiene un total de 21 configuraciones.

Para cada fila, cuenta todas las configuraciones diferentes de termas operativas y dañadas que cumplan con los criterios dados. ¿Cuál es la suma de esas configuraciones?

## Parte Dos

Mientras observas el campo de termas, sientes que hay muchas más termas de las que aparecen en los registros de condiciones. Al examinar los registros, descubres que en realidad estuvieron plegados todo este tiempo.

Para desplegar los registros, en cada fila, reemplaza la lista de condiciones de las termas por cinco copias de sí misma (separadas por ?) y reemplaza la lista de grupos contiguos de termas dañadas por cinco copias de sí misma (separadas por ,).

Por ejemplo, esta fila:

```
.# 1
```
Se convertiría en:

```
.#?.#?.#?.#?.# 1,1,1,1,1
```

La primera línea del ejemplo anterior se convertiría en:

```
???.###????.###????.###????.###????.### 1,1,3,1,1,3,1,1,3,1,1,3,1,1,3
```
En el ejemplo anterior, después de desplegar, el número de configuraciones posibles para algunas filas ahora es mucho mayor:

```
???.### 1,1,3 - 1 configuración  
.??..??...?##. 1,1,3 - 16384 configuraciones  
?#?#?#?#?#?#?#? 1,3,1,6 - 1 configuración  
????.#...#... 4,1,1 - 16 configuraciones  
????.######..#####. 1,6,5 - 2500 configuraciones  
?###???????? 3,2,1 - 506250 configuraciones
```

Después de desplegar los registros, la suma total de configuraciones posibles es 525152.

Despliega los registros de condiciones y calcula la nueva suma de posibles configuraciones.

