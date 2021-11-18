---
title: Cómo uso docker con mi disco externo
excerpt: mi setup para usar docker en un disco externo
date: '2021-02-25T02:37:30.187Z'
tags:
    - nerd
---
Como docker me llenaba el disco de mi computadora, decidí pasarlo a un disco sólido externo.
- Disco sólido externo de 128Gb formateado ext4
- Configuración de docker daemon:
```bash
echo '{
    "data-root":"/media/<username>/<disco>/docker-root"
}' > /etc/docker/daemon.json
```
- Hacer que docker no inicie al prender la computadora. Este paso es importante porque docker puede crear la carpeta `/media/<username>/<disco>/docker-root` antes de que se monte el disco.
```
systemctl disable docker.socket
systemctl disable docker.service
```
- instalar udiskie
- hacer que udiskie se ejecute al iniciar X:
```bash
echo '( sleep 1 && udiskie --smart-tray --menu nested ) &' >> .xprofile
```


Ahora, al empezar a trabajar hay que correr `sudo service docker start` antes de ejecutar cualquier comando de docker o docker compose.