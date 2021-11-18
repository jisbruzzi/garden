---
title: Cómo usar gcloud con un cliente
excerpt: Empecé a usar gcloud y parte de mi proceso implica que un cliente use la consola
date: '2021-02-17T01:28:38.247Z'
---
Actualmente mi estrategia de venta consiste en delegarle los costos de infraestructura al cliente si así lo desean. Para que los pagos puedan venir de la tarjeta de crédito del cliente, es necesario que éste se registre en google cloud. Mi proceso de desarrollo implica una primera etapa en la que construyo un prototipo y una parte de la infraestructura en google cloud, y luego transfiero todo lo que creé al cliente. 

[Fuente de toda esta información](https://cloud.google.com/billing/docs/how-to/modify-project)

> **Paso previo: cambiar el idioma**
> Para cambiar el idioma, hay que ir al menú superior derecho (3 puntitos) > preferences > lanuage & region

Cada _persona_ que se registra en google cloud tiene vinculada una _billing account_. Cada _proyecto_ tiene **1** _billing account_, y una _billing account_ puede tener **muchos** _proyectos_.

# Proceso general para pasar los gastos al cliente
1. El desarrollador **crea** el _proyecto_, prototipa sobre éste proyecto, puede realizar una pequeña inversión.
2. El cliente se registra en [cloud.google.com](https://cloud.google.com)
3. El cliente va al menú **"sandwich"** (3 líneas) superior izquierdo > **Billing** (tarjeta de crédito) > **Account management** (engranaje)
4. En la barra derecha se muestra toda la información de acceso de cualquier cosa de google cloud. El cliente debe hacer click en **+ADD MEMBER**.
5. El cliente pone en **"New members"** el mail del desarrollador.
6. El cliente Hace click en **Role** y luego donde dice "Type to filter", escribe **"Billing Account User"**, y lo concede al desarrollador haciendo click en **SAVE**
7. El desarrollador va a **sandwich** > **Billing** > **Account management**, y clickea en **"Actions"** > **"Change billing"** del proyecto a transferir. Allí va a poder elegir la billing account del cliente.
8. (PENDIENTE VERIFICAR SI FUNCIONA) El cliente ahora puede desactivar el rol que me concedió sobre su Billing Account para evitar que el desarrollador (malintencionadamente o por error) agregue más proyectos a su billing account

# Proceso para pasar el proyecto al cliente
El desarrollador que creó el proyecto por defecto tiene rol **Owner** en el mismo. Para darle visibilidad absoluta al cliente sobre la infraestructura, debe el desarrollador debe asignarle ese mismo rol al cliente.
1. Loggearse en la [consola de google cloud]((https://console.cloud.google.com))
2. Hamburguesa->IAM
3. Click en el botón "ADD"
4. Aparece un formulario, en "New members" poner el mail del cliente, en Role poner "Owner"