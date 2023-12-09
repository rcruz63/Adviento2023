# Día 5: Si le das fertilizante a una semilla ---
Coges el barco y encuentras al jardinero justo donde te dijeron que estaría: gestionando un "jardín" gigante que más bien parece una granja.

"¿Una fuente de agua? ¡La isla Isla es la fuente de agua!" Señalas que la Isla Nieve no está recibiendo agua.

"Oh, tuvimos que detener el agua porque nos quedamos sin arena para filtrarla. No se puede hacer nieve con agua sucia. No te preocupes, estoy seguro de que obtendremos más arena pronto; solo apagamos el agua hace unos días... semanas... oh no." Su rostro se hunde en una mirada de horrorosa realización.

"He estado tan ocupado asegurándome de que todos aquí tengan comida que olvidé por completo revisar por qué dejamos de recibir más arena. Hay un ferry que sale pronto en esa dirección, es mucho más rápido que tu barco. ¿Podrías por favor ir a echar un vistazo?"

Apenas tienes tiempo para aceptar esta solicitud cuando menciona otra. "Mientras esperas el ferry, tal vez puedas ayudarnos con nuestro problema de producción de alimentos. Acaba de llegar el último Almanaque de la Isla Isla y tenemos problemas para entenderlo".

El almanaque (tu entrada de rompecabezas) enumera todas las semillas que necesitan ser plantadas. También enumera qué tipo de suelo usar con cada tipo de semilla, qué tipo de fertilizante usar con cada tipo de suelo, qué tipo de agua usar con cada tipo de fertilizante, y así sucesivamente. Cada tipo de semilla, suelo, fertilizante, etc., se identifica con un número, pero los números se reutilizan en cada categoría, es decir, el suelo 123 y el fertilizante 123 no necesariamente están relacionados entre sí.

Por ejemplo:

semillas: 79 14 55 13

mapa-semilla-a-suelo:
50 98 2
52 50 48

mapa-suelo-a-fertilizante:
0 15 37
37 52 2
39 0 15

mapa-fertilizante-a-agua:
49 53 8
0 11 42
42 0 7
57 7 4

mapa-agua-a-luz:
88 18 7
18 25 70

mapa-luz-a-temperatura:
45 77 23
81 45 19
68 64 13

mapa-temperatura-a-humedad:
0 69 1
1 0 69

mapa-humedad-a-ubicación:
60 56 37
56 93 4
El almanaque comienza enumerando las semillas que necesitan ser plantadas: semillas 79, 14, 55 y 13.

El resto del almanaque contiene una lista de mapas que describen cómo convertir números de una categoría de origen en números en una categoría de destino. Es decir, la sección que comienza con el mapa-semilla-a-suelo: describe cómo convertir un número de semilla (el origen) en un número de suelo (el destino). Esto permite al jardinero y su equipo saber qué suelo usar con qué semillas, qué agua usar con qué fertilizante, y así sucesivamente.

En lugar de listar uno por uno cada número de origen y su número de destino correspondiente, los mapas describen rangos enteros de números que pueden ser convertidos. Cada línea dentro de un mapa contiene tres números: el inicio del rango de destino, el inicio del rango de origen y la longitud del rango.

Consideremos nuevamente el ejemplo de mapa-semilla-a-suelo:

50 98 2
52 50 48
La primera línea tiene un inicio de rango de destino de 50, un inicio de rango de origen de 98 y una longitud de rango de 2. Esta línea significa que el rango de origen comienza en 98 y contiene dos valores: 98 y 99. El rango de destino es de la misma longitud, pero comienza en 50, por lo que sus dos valores son 50 y 51. Con esta información, sabes que el número de semilla 98 corresponde al número de suelo 50 y que el número de semilla 99 corresponde al número de suelo 51.

La segunda línea significa que el rango de origen comienza en 50 y contiene 48 valores: 50, 51, ..., 96, 97. Esto corresponde a un rango de destino que comienza en 52 y también contiene 48 valores: 52, 53, ..., 98, 99. Entonces, el número de semilla 53 corresponde al número de suelo 55.

Cualquier número de origen que no esté mapeado corresponde al mismo número de destino. Así, el número de semilla 10 corresponde al número de suelo 10.

Por lo tanto, la lista completa de números de semilla y sus correspondientes números de suelo se ve así:

semilla  suelo
0       0
1       1
...     ...
48      48
49      49
50      52
51      53
...     ...
96      98
97      99
98      50
99      51
Con este mapa, puedes buscar el número de suelo necesario para cada número de semilla inicial:

El número de semilla 79 corresponde al número de suelo 81.
El número de semilla 14 corresponde al número de suelo 14.
El número de semilla 55 corresponde al número de suelo 57.
El número de semilla 13 corresponde al número de suelo 13.
El jardinero y su equipo quieren comenzar lo antes posible, así que les gustaría saber la ubicación más cercana que necesita una semilla. Utilizando estos mapas, encuentra el número de ubicación más bajo que corresponde a cualquiera de los números de semilla iniciales. Para hacer esto, deberás convertir cada número de semilla a través de otras categorías hasta que puedas encontrar su número de ubicación correspondiente. En este ejemplo, los tipos correspondientes son:

Semilla 79, suelo 81, fertilizante 81, agua 81, luz 74, temperatura 78, humedad 78, ubicación 82.
Semilla 14,

 suelo 14, fertilizante 53, agua 49, luz 42, temperatura 42, humedad 43, ubicación 43.
Semilla 55, suelo 57, fertilizante 57, agua 53, luz 46, temperatura 82, humedad 82, ubicación 86.
Semilla 13, suelo 13, fertilizante 52, agua 41, luz 34, temperatura 34, humedad 35, ubicación 35.
Entonces, el número de ubicación más bajo en este ejemplo es 35.

¿Cuál es el número de ubicación más bajo que corresponde a cualquiera de los números de semilla iniciales?

## Parte Dos ---
Todos pasarán hambre si solo siembras un número tan pequeño de semillas. Al releer el almanaque, parece que la línea de semillas: en realidad describe rangos de números de semillas.

Los valores en la línea inicial de semillas: vienen en pares. Dentro de cada par, el primer valor es el comienzo del rango y el segundo valor es la longitud del rango. Entonces, en la primera línea del ejemplo anterior:

seeds: 79 14 55 13
Esta línea describe dos rangos de números de semillas que se plantarán en el jardín. El primer rango comienza con el número de semilla 79 y contiene 14 valores: 79, 80, ..., 91, 92. El segundo rango comienza con el número de semilla 55 y contiene 13 valores: 55, 56, ..., 66, 67.

Ahora, en lugar de considerar cuatro números de semilla, necesitas considerar un total de 27 números de semilla.

En el ejemplo anterior, el número de ubicación más bajo se puede obtener a partir del número de semilla 82, que corresponde a la tierra 84, fertilizante 84, agua 84, luz 77, temperatura 45, humedad 46 y ubicación 46. Entonces, el número de ubicación más bajo es 46.

Considera todos los números de semilla iniciales enumerados en los rangos de la primera línea del almanaque. ¿Cuál es el número de ubicación más bajo que corresponde a cualquiera de los números de semilla iniciales?