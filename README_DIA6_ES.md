# Día 6: Espera por ello ---
El ferry te lleva rápidamente a través de Island Island. Después de preguntar por ahí, descubres que normalmente hay una gran pila de arena por aquí, pero no ves nada más que mucha agua y la pequeña isla donde ha atracado el ferry.

Mientras intentas averiguar qué hacer a continuación, ves un cartel en una pared cerca del muelle del ferry. "¡Carreras de barcos! ¡Abiertas al público! ¡El gran premio es un viaje con todos los gastos pagados a Desert Island!" ¡Eso debe ser de donde viene la arena! Lo mejor de todo es que las carreras de barcos están empezando en solo unos minutos.

Logras inscribirte como competidor en las carreras de barcos justo a tiempo. El organizador explica que no es realmente una carrera tradicional: en cambio, tendrás un tiempo fijo durante el cual tu barco debe viajar lo más lejos posible, y ganas si tu barco va más lejos.

Como parte de la inscripción, recibes una hoja de papel (tu entrada del rompecabezas) que lista el tiempo permitido para cada carrera y también la mejor distancia jamás registrada en esa carrera. Para garantizar que ganes el gran premio, debes asegurarte de ir más lejos en cada carrera que el poseedor actual del récord.

El organizador te lleva al área donde se llevan a cabo las carreras de barcos. Los barcos son mucho más pequeños de lo que esperabas: en realidad, son barcos de juguete, cada uno con un gran botón en la parte superior. Mantener presionado el botón carga el barco, y soltar el botón permite que el barco se mueva. Los barcos se mueven más rápido si su botón se ha mantenido durante más tiempo, pero el tiempo que se pasa sosteniendo el botón cuenta en el tiempo total de la carrera. Solo puedes mantener presionado el botón al comienzo de la carrera, y los barcos no se mueven hasta que se suelta el botón.

Por ejemplo:

Tiempo:      7  15   30
Distancia:  9  40  200
Este documento describe tres carreras:

La primera carrera dura 7 milisegundos. La distancia récord en esta carrera es de 9 milímetros.
La segunda carrera dura 15 milisegundos. La distancia récord en esta carrera es de 40 milímetros.
La tercera carrera dura 30 milisegundos. La distancia récord en esta carrera es de 200 milímetros.
Tu barco de juguete tiene una velocidad inicial de cero milímetros por milisegundo. Por cada milisegundo completo que pases al principio de la carrera sosteniendo el botón, la velocidad del barco aumenta en un milímetro por milisegundo.

Así que, como la primera carrera dura 7 milisegundos, solo tienes algunas opciones:

No sostener el botón en absoluto (es decir, mantenerlo durante 0 milisegundos) al inicio de la carrera. El barco no se moverá; habrá viajado 0 milímetros al final de la carrera.
Mantener presionado el botón durante 1 milisegundo al inicio de la carrera. Luego, el barco viajará a una velocidad de 1 milímetro por milisegundo durante 6 milisegundos, alcanzando una distancia total recorrida de 6 milímetros.
Mantener presionado el botón durante 2 milisegundos, dando al barco una velocidad de 2 milímetros por milisegundo. Luego obtendrá 5 milisegundos para moverse, alcanzando una distancia total de 10 milímetros.
Mantener presionado el botón durante 3 milisegundos. Después de sus restantes 4 milisegundos de tiempo de viaje, el barco habrá recorrido 12 milímetros.
Mantener presionado el botón durante 4 milisegundos. Después de sus restantes 3 milisegundos de tiempo de viaje, el barco habrá recorrido 12 milímetros.
Mantener presionado el botón durante 5 milisegundos, haciendo que el barco viaje un total de 10 milímetros.
Mantener presionado el botón durante 6 milisegundos, haciendo que el barco viaje un total de 6 milímetros.
Mantener presionado el botón durante 7 milisegundos. Esa es toda la duración de la carrera. Nunca sueltas el botón. El barco no puede moverse hasta que sueltes el botón. Por favor, asegúrate de soltar el botón para que el barco pueda moverse. 0 milímetros.
Como el récord actual para esta carrera es de 9 milímetros, en realidad hay 4 formas diferentes en las que podrías ganar: podrías mantener presionado el botón durante 2, 3, 4 o 5 milisegundos al inicio de la carrera.

En la segunda carrera, podrías mantener presionado el botón durante al menos 4 milisegundos y como máximo 11 milisegundos y batir el récord, un total de 8 formas diferentes de ganar.

En la tercera carrera, podrías mantener presionado el botón durante al menos 11 milisegundos y como máximo 19 milisegundos y aún así superar el récord, un total de 9 formas en las que podrías ganar.

Para ver cuánto margen de error tienes, determina el número de formas en que puedes superar el récord en cada carrera; en este ejemplo, si multiplicas estos valores juntos, obtienes 288 (4 * 8 * 9).

Determina el número de formas en que podrías superar el récord en cada carrera. ¿Qué obtienes si multiplicas estos números entre sí?

# Parte Dos ---
Mientras la carrera está a punto de comenzar, te das cuenta de que el trozo de papel con los tiempos de la carrera y las distancias récord que obtuviste antes tiene un espaciado realmente malo. En realidad, solo hay una carrera; ignora los espacios entre los números en cada línea.

Así que, el ejemplo anterior:

Tiempo: 7 15 30
Distancia: 9 40 200
...ahora significa esto:

Tiempo: 71530
Distancia: 940200
Ahora, tienes que descubrir cuántas formas existen para ganar esta única carrera. En este ejemplo, la carrera dura 71530 milisegundos y la distancia récord que debes superar es de 940200 milímetros. Podrías mantener pulsado el botón en cualquier lugar desde 14 hasta 71516 milisegundos y superar el récord, ¡un total de 71503 formas!

¿Cuántas formas puedes superar el récord en esta única y mucho más larga carrera?