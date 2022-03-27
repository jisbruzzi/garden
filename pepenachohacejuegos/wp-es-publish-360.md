---
title: 'Color-Absorption'
post_type: 'post'
source: 'https://pepenachohacejuegos.wordpress.com/2013/02/14/color-absorption/'
pub_date: 'Thu, 14 Feb 2013 17:41:29 +0000'
post_date: '2013-02-14 17:41:29'
post_modified_gmt: '2013-02-14 17:41:29'
post_name: 'color-absorption'
date: '2013-02-14T17:41:29'
post_id: '360'
tags:
    - pepenachohacejuegos
    - teenage
    - nerd
---
Color Absorption es un juego que hice para una jam llamada Game Prototyping Challenge v16. Organizan <a href="http://news.gameprototypechallenge.com/faq">una jam</a> cada dos meses en las que tenés que hacer un juego a partir de dos temas que te dan. Estos temas no son necesariamente opuestos... pero tienen poca (si no ninguna) relación entre si.

Hace bastante tiempo tenía una idea de un shooter super-simple, que usaría como promer proyecto en java... pero como nunca me puse a programar java, quedó en el aire. La idea era que cada persona fuera un cuadrado diferente, que se mueva y dispare en 4 direcciones. Así, en un entorno 2D generado al azar o por los mismos usuarios, surgirían diferentes estrategias de equipo (chat de voz o sistema simple de comunicación por medio). Mi idea también vendría acompañada de ciertas mecánicas simples que no voy a postear acá. En una de esas, alguien me roba la idea y se llena de plata.

Bueno, la cosa es que la idea no tenía nada que ver con "cuatro colores" ni "absorbción" (los temas de la jam). Así que terminé mezclando la idea de antes con esos temas y surgió color-absorption.

Topológicamente hablando (que palabrita eh), es bastante parecida a mi idea previa: te movés en 4 direcciones, disparás en 4 direcciones. Pero en términos de las mecánicas, es muy diferente. En vez de ser un juego por equipos, se juega todos contra todos. Además, hay diferentes clases con ventajas distintas. Cada uno supone una forma un poco distinta de jugar.
<ul>
	<li><span style="line-height:13px;">Sniper: Recarga lento, pero el tiro es más rápido.</span></li>
	<li>Lanzacohetes: Dispara balas lentas que explotan.</li>
	<li>Rápido: es el más rápido.</li>
	<li>Sobreviviente: Es la clase que más me gusta. Tiene cuatro escudos, uno para cada lado. Solamente podés matarlo si destruiste el escudo que cubre el lado desde el cual disparás anteriormente.</li>
</ul>
&nbsp;

El giro significativo (que aportó el tema "absorbción" de la GPC) es que, cuando un jugador es asesinado, cambia de clase con el que lo mató. Así, un jugador en cierta situación puede dejarse matar por otro en particular para robarle la clase.

De los 8 días de la jam, sólo pude trabajar en el juego durante 5, después de todo tengo un poco de vida. Así que no pude implementar el onlinbe multiplayer. Mi salida fué hacer IA con un algoritmo de pathfinding. De nuevo, por razones de tiempo, usé uno poco optimizado que encontré en wikipedia, <a href="http://en.wikipedia.org/wiki/Pathfinding#Sample_algorithm">acá</a> (bajo el subtítulo "Sample Algorithm"), que -creo- es el de Dijkstra, explicado sintéticamente en la misma página.

Otra cosa sobre la que quiero llamar la atención es el generador de mapas al azar. Todos los mapas tienen su eje de simetría en el medio para que los jugadores spawneen en igualdad de condiciones. Esto hace que los mapas sean más aburridos, pero me pareció mejor solución (y más interesante de implementar) que hacer los mapas yo mismo. Si hubiera resuelto el tema de los mapas de la segunda forma, podría haber balanceado el spawn point de los jugadores sin recurrir a la simetría.

&nbsp;

Faltaron GFX, faltaron GFX, faltaron GFX. Con ellos, el juego sería muchísimo más visualmente llamativo.

&nbsp;

&nbsp;

Se puede jugar acá:

http://gamejolt.com/games/shooter/color-absorption/12293/

Algunas Imágenes:

&nbsp;

&nbsp;

[caption id="" align="alignnone" width="640"]<a href="http://images2.cdn.gamejolt.com/data/games/12293/screenshots/12293_19731.jpg"><img title="Los cohetes no están del todo bien hechos." alt="Los cohetes no están del todo bien hechos." src="http://images2.cdn.gamejolt.com/data/games/12293/screenshots/12293_19731.jpg" width="640" height="480" /></a> Los cohetes no están del todo bien hechos. Mueven la balanza muy a favor de un jugador en específico.[/caption]

&nbsp;

<img class="alignnone" alt="" src="http://images2.cdn.gamejolt.com/data/games/12293/screenshots/12293_19730.jpg" width="640" height="480" />