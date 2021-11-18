---
title: Cómo usar una raspberry pi como receptor de spotify
date: '2021-03-24T14:07:12.835Z'
tags:
    - nerd
---
La raspberry pi es una genialidad tecnológica del siglo XXI que no uso para nada tecnológico sino para reproducir canciones de spotify por unos parlantes externos. Y ni siquiera para eso sirve.

# Paso 1: reinstalar raspberry pi OS o como se llame
[Referencia](https://www.raspberrypi.org/documentation/installation/installing-images/)

Simplemente hay que:
- ir a la [página oficial de raspberry pi](https://www.raspberrypi.org/) y descargar el sistema operativo ahí.
- conectar la tarjeta sd y ver qué nombre le asignó linux usando `df -h` (columna `Filesystem`). Supongamos que linux le asignó el archivo `/dev/sdXX` a la tarjeta SD.
- `dd if=<imagen del SO descomprimida> of=/dev/sdXX bs=4M conv=fsync`

# Paso 2: raspotify

Seguir las [instrucciones de instalación](https://github.com/dtcooper/raspotify).

# Paso 3: resolver problema con el volumen
1. correr el comando `alsamixer`
2. Cambiar de dispositivo con `F6`, elegir headphones
3. Subir el volumen a 100%
4. Salir con la tecla ESC
5. Correr el comando `sudo alsactl store` [Referencia](https://askubuntu.com/questions/50067/howto-save-alsamixer-settings)

# Paso 4: resolver otros problemas
Raspotify no va a funcionar! Tuve más problemas pero no recuerdo cómo los arreglé

Issues recomendables:
- [180](https://github.com/dtcooper/raspotify/issues/180)
- [301](https://github.com/dtcooper/raspotify/issues/301)

Para diagnosticar problemas: `journalctl -u raspotify`