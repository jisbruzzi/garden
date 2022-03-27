---
title: 'Clase para modificar la velocidad de un sonido mp3: AS3'
post_type: 'post'
source: 'https://pepenachohacejuegos.wordpress.com/2013/01/01/clase-para-modificar-la-velocidad-de-un-sonido-mp3-as3/'
pub_date: 'Tue, 01 Jan 2013 12:24:31 +0000'
post_date: '2013-01-01 12:24:31'
post_modified_gmt: '2013-02-25 15:22:10'
post_name: 'clase-para-modificar-la-velocidad-de-un-sonido-mp3-as3'
date: '2013-02-25T15:22:10'
post_id: '334'
tags:
    - pepenachohacejuegos
    - teenage
    - nerd
---
Para el juego que estuve haciendo (Missile Walker, que postearé acá en aproximadamente dos semanas), necesitaba usar una clase que disminuya la velocidad del audio. Mi primera solución fué tomar este código: http://www.mcfunkypants.com/2011/as3-pitch-shift-mp3/ . Pero hubo un problema: esa clase no consideraba casos en el que el sonido no tenia que loopear. Entonces decidí editarla. Entre mi desconocimiento de la clase Sound y lo ilegible de ese código, estuve cerca de 9 horas frente a mi PC rompiéndome la cabeza y enojándome. Al final, no logré adaptar la clase a las necesidades de un efecto de sonido, terminé usando la clase Sfx de Flashpunk.

En fin, si entran al link que dejé mas arriba, verán que esa clase está muy poco comentada, y que el código no es para nada facil de interpretar... francamente tiene algunas vueltas que me marean mucho. Por lo tanto,agarré el problema por el lado metódico y creé mi propia clase explicando cada detallito que se pueda imaginar.

Aunque el objetivo de la clase es que sea utilizada en juegos donde hay distorción de sonido, cuando se reproduce más de uno, el FPS baja muchísimo. Por eso, para agregarla a mi juego voy a tener que programar un "reproductor de sonidos: una clase que unifique las tareas para que el evento onSampleData suceda sólo una vez.

Es eso, acá está el código:

https://gist.github.com/4424117