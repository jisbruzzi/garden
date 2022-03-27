---
title: 'Cómo medir el salto de tu personaje plataformero '
post_type: 'post'
source: 'https://pepenachohacejuegos.wordpress.com/2012/09/01/como-medir-el-salto-de-tu-personaje-plataformero/'
pub_date: 'Sat, 01 Sep 2012 19:44:22 +0000'
post_date: '2012-09-01 19:44:22'
post_modified_gmt: '2012-09-01 19:44:22'
post_name: 'como-medir-el-salto-de-tu-personaje-plataformero'
date: '2012-09-01T19:44:22'
post_id: '298'
tags:
    - pepenachohacejuegos
    - teenage
    - nerd
---
Éste es un post que publiqué en <a href="http://www.comunidadgm.org/index.php?topic=15011.0" target="_blank">Comunidad GM</a>. Lo copio acá porque sé que puede ser muy útil. Estoy pensando en juntar en este blog todo el material escrito que haya creado, así que probablemente clone todo lo que publiqué en Taringa.
<blockquote>  Ya te debe haber pasado varias veces -como a mí- que estás haciendo un juego de plataformas y símplemente "pateas" cualquier número para hacer que tu personaje salte. Después cuando vos mismo -u otra persona- se pone a hacer niveles para el juego que programaste, viene el problema de no saber cuantos pixeles salta tu personaje. Y justamente ese problema vengo a resolverte.

Si tenés un grado de escolaridad más o menos alto (rondás los 14)te diría que sigas, sino, salteate la explicación y leé las fórmulas del final.

Primero, transformá los códigos que usas para hacer saltar a tu personaje en una función lineal (o de primer grado), que tenga la siguiente forma:
<pre>f(x)=ax+b</pre>
Tenés que reemplazar la "a" por la velocidad que adopta tu personaje cuando -estando en el piso- apretás el botón para saltar. Por lo general este número es negativo y suele ser bastante más grande que el que vamos a usar como "b". Para el uso que vamos a darle, te sugiero que le cambies el signo: vamos a medir la altura del personaje como si el piso fuera 0 y con altura positiva. En los juegos es al revés porque los negativos suelen estar para arriba, en cambio, en un eje cartesiano los positivos son los que estan arriba (pero ya te debés haber dado cuenta de eso hace bastante tiempo).
Ahora pasemos a hablar sobre el valor "b": éste es un poco más complicado porque se obtiene de restarle la gravedad a la cantidad de velocidad que gana por cada "step" que apretás el botón para saltar. Acordate de cambiar los signos por el tema que te comentaba antes (la verdad, podrías dejar todos los valores con el signo que tienen, así en el gráfico que viene te quedaría una representación de la altura digamos que "mas fiel a la realidad", pero sino se nos complica para calcular las áreas y todas esas cosas raras que vamos a hacer).
Entonces, sustituyendo la "x" por el tiempo y aplicando la función lineal a los videojuegos, tenemos:
<pre>Velocidad(tiempo)=SaltoInicial+(EmpujonEnElAire-Gravedad)*tiempo</pre>
Para simplificar esa asquerosidad de fórmula, vamos a usar:
<pre>velocidad(t)=Si+(Sa-G)t</pre>
(ah, y aclaro que con esta fórmula en realidad obtenemos la velocidad máxima en el momento t, para conseguir la mínima, hacé como si Sa=0)

Voy a hacer un paréntesis acá y hablar un poco de game design. Por lo general, en los juegos de plataformas bien hardcore, vemos un "Si" pequeño y un "Sa" enorme: esto sirve para que el jugador pueda hacer saltos más dificiles, controlando con mucha precisión cuánto quiere saltar. Si querés pruebas fijate en el Cave Story o en el Mario Bross -o peor todavía, en Super Meat Boy-. En contraposición, en los juegos de plataformas orientados al público casual, tenemos un "Si" enorme y un "Sa" muy cercano a 0; esto es porque una persona que no es demasiado veterana necesita saber hasta dónde va a llegar su salto y saber predecirlo.

Volviendo al tema de las matemáticas, acá tenemos el gráfico de la función:

<a href="http://img15.imageshack.us/img15/8105/cartesiano1.png"><img class="alignnone" src="http://img15.imageshack.us/img15/8105/cartesiano1.png" alt="" width="500" height="300" /></a>

Esto estaria correcto: tiene que ir para abajo, a menos que quieras que tu personaje se vaya volando hasta el infinito y más allá.
Ahora te estarás preguntando qué tiene que ver esto con la altura. Y en seguida te respondo: Intentá construir la fórmula de la altura. quedaría algo así:
<pre>Altura(t)=Velocidad(t)+Altura(t-1)
Condición de existencia: t incluido en los Naturales y Altura(0) en los reales</pre>
Esta fórmula es bastante tediosa de hacer: no sólo tiene esa molesta condición de existencia, sino que también te obliga a buscar todos los valores anteriores de Velocidad y de Altura. Es más, la función Altura no es otra cosa que un recolector de todas los valores de Velocidad hasta t. Se podría escribir así:
<pre>Altura(t)={todos los valores de Velocidad cuando , en Velocidad(X), X es mayor que 0 y menor o igual a t}</pre>
<strong>Nota:</strong> Si querés saber la altura en determinado momento, hay una fórmula de cinemática que es S=Si+ViT+(AT<sup>2</sup>)/2, pero voy a seguir por donde empecé.

¿Y para obtener todos los valores de Velocidad para obtener la altura máxima? Sacamos el área del triángulo que en la primera imagen está en naranja usando la fórmula (base*altura)/2 .La base entonces seria el valor de X cuando Y es igual a 0 -o, mejor dicho, el valor de t cuando el resultado de Velocidad es 0-. Y la altura seria Velocidad(0). Entonces, reemplazando, quedaría:

Velocidad(0)*Velocidad(0)<sup>-1</sup>/2

Ahora viene una parte bastante tediosa de buscar la función inversa de Velocidad, desarmar las dos funciones y ponerse a hacer álgebra. Y entonces, la fórmula que nos queda es:

<strong>-Si<sup>2</sup>/(Sa-G)/2=altura máxima del salto</strong>

<strong>[Si=Salto Inicial (empujón inicial)</strong>

<strong>Sa=Salto en el aire (empujón mientras se presiona el botón del salto)</strong>

<strong>G=Gravedad</strong>

<strong>Todo está en pixeles(distancias) y pixeles/actualización del game loop(velocidades)]</strong>

&nbsp;

Ahora, podés decidir la altura máxima del personaje de tu juego resolviendo una simple ecuación. Para hacerlo, te recomiendo que primero elijas la altura a la que querés que tu personaje salte. En seguida, modificá la ecuación de arriba para que (Sa-G) sea una sola incógnita (yo que sé, "Q"), después podés elegir dos números que tengan una diferencia igual a "Q", después de todo esos dos valores no cambian nada, pero sí su diferencia. Luego, si querés que tu personaje tenga un salto predecible, elegís un valor para "Q" que sea bajo y te queda una ecuación en la que descubrís Si. De lo contrario si estás haciendo un videojuego bien hardcore, reemplazá Si por un valor bajo y despejá.

Espero que esto les haya servido para cuando hagan juegos de plataformas ^_^

Soyyo.</blockquote>
&nbsp;

Pido disculpas si no se entiende, en esa época no escribía tan bien como ahora. Creo que en su momento tampoco revisé el texto, así que no sé cuán facil puede ser entenderlo.

Saludos.