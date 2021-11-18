---
title: Nombres en vez de IP en tu LAN
excerpt: No hace falta instalar y configurar un servidor DNS para acceder servidores locales usando nombres.
date: '2021-02-16T22:24:10.328Z'
---
No hace falta instalar y configurar un servidor DNS para acceder servidores locales usando nombres.
Se puede usar [Avahi](https://www.avahi.org/). Avahi es un protocolo  estandarizado recientemente, no todos los sistemas lo soportan. Así, hay que instalar daemon y servidores en los equipos que participan de la red. Es más facil configurar Avahi que configurar un DNS local.

Los siguientes comandos instalan avahi daemon y server. Funcionan en raspberry pi, ubuntu 18 y 20.
```bash
sudo apt install openssh-server
sudo apt install avahi-daemon
sudo cp /usr/share/doc/avahi-daemon/examples/ssh.service /etc/avahi/services/
view /etc/hostname
```
Ahora, en un equipo que tenga instalado `avahi-daemon`, puede acceder usando el hostname del servidor ssh. Así, si en `/etc/hostname` dice `fooserver`, accedemos como `ssh usuario@fooserver.local`. 

El despliegue toma 5 minutos, en casa tengo todas las computadoras linux accesibles desde todas las otras.