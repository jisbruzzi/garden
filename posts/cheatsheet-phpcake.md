---
title: Cheatsheet PHPCake
date: '2021-05-17T19:32:20.803Z'
tags:
    - technical
    - cheatsheet
---
# Dependency injection
Se incluyen los servicios inyectables como argumentos de los métodos de los controllers. Pueden ser abstractos o concretos. A partir del tipo CakePHP deduce cuál es el inyectable.

You can use the service container to define ‘application services’. These classes can use models and interact with other objects like loggers and mailers to build re-usable workflows and business logic for your application.

Los servicios se agregan en el método `services` de la `Application`.

Service providers: agrupan servicios que pueden inyectar y permiten inyectarlos lazily.

# routing

`routes.php`
como en django, si no es el fallback hay que pasar por kwargs controller, action, params.

# Controllers
definen actions, settean variables de las views (`$this->set`) a partir del `$this->request`. Renderiza el contenido de los templates (php de toda la vida).

# Components
inyectados en el constructor de los controllers usando `$this->loadComponent($name)`. Agregan métodos al controller.

# Views
algo más groso
## Templates
Archivos php que reciben las variables setteadas. Tienen herencia y viewblocks para evitar repetir código (parece jinja).
## Elements
componentes react ssr
## Layouts
templates que envuelven todo
## Helpers
Components como en los controllers pero en la view.
## Cells
Mini-controllers y views.
## Themes
plugins que incluyen tamplates
## JSON and XML views
`$this->loadComponent('RequestHandler');`
```
// Set the view vars that have to be serialized.
$this->set(compact('articles', 'comments'));

// Specify which view vars JsonView should serialize.
$this->viewBuilder()->setOption('serialize', ['articles', 'comments']);
```
# ORM
## Tables
pueden no tener nada y cargarse de la db
These objects provide access to collections of data. They allow you to save new records, modify/delete existing ones, define relations, and perform bulk operations.
## Entities
Entities represent individual records and allow you to define row/record level behavior & functionality. CakePHP uses naming conventions to link the Table and Entity class together. 
## querys
`$query = $articles->find();`
```
// Inside ArticlesController.php

$query = $this->Articles->find()
    ->where(['id >' => 1])
    ->all();;
```
## Behaviors
lifecycle hooks agrupados para las `Table`
## Validating data
métodos que construyen validadores en las `Table`. Pueden llamar a métodos de la entidad.
## Saving data
```php
$article = $articlesTable->newEmptyEntity();
$articlesTable->save($article);
```
By default the save() method will also save one level of associations
## Deleting data
```php
// In a controller.
$entity = $this->Articles->get(2);
$result = $this->Articles->delete($entity);
```
## Asociations - linking Tables together
```php
$this->hasMany('Comments')
```
# Events system
```php
$event = new Event('Model.Order.afterPlace', $this, [
    'order' => $order
]);
$this->getEventManager()->dispatch($event);
```
```php
$this->Orders->getEventManager()->on('Model.Order.afterPlace', function ($event) {
    Log::write(
        'info',
        'A new order was placed with id: ' . $event->getSubject()->id
    );
});
```
# REST
```php
$routes->scope('/api', function (RouteBuilder $routes) {
    $routes->resources('Articles', function (RouteBuilder $routes) {
        $routes->resources('Comments');
    });
});
```
Para que traduzca bien los verbos HTTP.

# Plugins
Son paquetes externos que incluyen todo y hacés en bootstrap ` $this->addPlugin('AcmeCorp/ContactManager');` 
Son las apps de django.

# Auth
plugin de authentication, hay que hacer acciones de login