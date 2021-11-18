---
title: Cheatsheet vue 3
date: '2021-05-17T19:32:20.803Z'
---
# Options
Exportadas por `<script/>` block.

- `data:Function`: init data
- `props:array<string>|Object`: 
    - `array<string>`: nombres
    - `Object`: type ó type-default-required-validator
- `computed:{ [key: string]: Function | { get: Function, set: Function } }`: campos computados
- `methods:{ [key: string]: Function }`: methods
- `watch:{ [key: string]: string | Function | Object | Array}`: observar `data` ó `computed`. pasa `val`   y `oldVal`, o puede ser un nombre de un método, o el key puede ser un path adentro de un objeto
- `emits:Array<string> | Object`: documenta uso de `this.$emit('name'ev)`. Como objeto se puede pasar una función de validación.
- `template:string` ó `render:Function`. En el caso de render usa la función `h` ó jsx
- lifecycle hooks: ver lifecycle
- `directives:Object`: key: directive y value: Object de hooks
- `components:Object`: componentes que se pueden utilizar en el template de este 
- `mixins:Array<Object>`: mixins que se combinan en este componente
- `extends:Object|Function`: un mixin.
- `provide:Object | () => Object`: objetos que pueden ser inyectados por los hijos
- `inject:Array<string> | { [key: string]: string | Symbol | Object }`: ataja los valores provistos y los inyecta en `this`. Como objeto permite un `default`.
- `setup:(props,context)=>void`: entry point to Composition API. Called before the component is created. Devuelve `Data` para el template ó render function.
-  `name`: permite autorreferencia y docs
- `delimiters`: default `['{{', '}}']`
-  `inheritAttrs:boolean` default `true`. Fallthrough de los attrs adicionales desde la invocación del componente al top-level component del template

# lifecycle
![img](https://v3.vuejs.org/images/lifecycle.svg?__WB_REVISION__=f4a90248bd51e5ee6261fd079b5dffb5)

# Instance API interesante
- `$el`: The root DOM element that the component instance is managing.
- `$refs`: An object of DOM elements and component instances, registered with `ref` attributes.
- `$watch:(source:{string | Function},callback:{Function | Object}, options:{deep:boolean,...})`
- `$emit(eventName:string,...args)`

# Directives

- `v-text`
- `v-html`
- `v-show`: toggles `display` CSS property
- `v-if`
- `v-else`
- `v-else-if`
- `v-for`
- `v-on:<evento>`: shorthand `@click`
- `v-bind:<key>`: shorthand: `:href`. Con `clases` y `style` permite objetos y arrays.
- `v-model`!!!!!
- `v-slot:<nombre>`: para pasar contenido como hijo en distintos slots. Permite pasar props.
- `v-pre`: skip compilation
- `v-cloak`: aplicada automaticamente
- `v-once`: rendered once
- `v-is`: permite cambiar el componente on the fly

# Attributes
se usan con `v-bind:` casi siempre (osea `:`)
- `key`: identity for diffing
- `ref`: registers to `$refs`
- `is`: for dynamic components

# Built-in components
- `component`: meta-component usado con attr `is`
- `transition`
- `transition-group`
- `keep-alive`: cachea hijos para que no se reinicialicen siempre
- `slot`: tiene attr `name` renderiza slots que se pasaron.
- `teleport`: attr `to`. Manda los elementos a ese elemento.

# Reactivity API interesante
- `reactive:(Object)=>Proxy`: devuelve copia reactiva. deep. Hay variantes Shallow.
- `readonly:(Object)=>Readonly proxy`: devuelve copia reactiva readonly. deep. Hay variantes Shallow.
- `ref:(v)=> {value:Proxy<v>}`
- `computed:(fn)=>ref` devuelve una reactive ref que cambia automaticamente
-  `watchEffect:fn=>void`: re-runs `fn` cuando las dependencias reactivas cambian
- `watch(fn=>Object|Ref,(val,oldVal)=>void)`: watches fn or Ref and triggers the other fn

# Composition API interesante
- Hooks: se importan desde vue
- provide/inject: se importan desde vue
