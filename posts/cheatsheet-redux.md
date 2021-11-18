---
title: Cheatsheet Redux
date: '2021-05-17T19:32:20.803Z'
tags:
    - technical
    - cheatsheet
---
# React - redux

## Concepts
- state: the state of the entire application
- action: POJO with a "type" key and needed information.
- reducer: `function (state=initialState,action):State`. Pure function.
- store:
	- Stores current state
	- API: `getState()`, `dispatch(action)`, `subscribe(listener)` + unsubscribe
	- composition: application state can be large so multiple reducers can have different responsibilities affecting a different part of the state
- enhancer: decorator around store
- middleware: `store => next => action => {}` decorates only `dispatch()` and there can be many. Set up by the `applyMiddleware` enhancer.

## react-redux API
- `useDispatch()`: returns `dispatch(action)`
- `useSelector(store=>store.x.y)`: returns that value from the store and triggers updates.
- `<Provider store={store}>`: provides a store for hooks

## redux async
Using `redux-thunk` middleware one can use async functions as if they were actions. The async functions receive `dispatch` and `getState`.

```js
export async function fetchTodos(dispatch, getState) {
	const response = await client.get('/fakeApi/todos')
	dispatch({ type: 'todos/todosLoaded', payload: response.todos })
}
```
