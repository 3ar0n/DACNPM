import { createStore, applyMiddleware } from "redux";
import { createLogger } from 'redux-logger';
import rootReducer from '../redux';
import rootSaga from '../sagas';
import createSagaMiddleware from 'redux-saga';

const saga = createSagaMiddleware();

const middlewares = [saga];

if (process.env.NODE_ENV === 'development') {
  middlewares.push(createLogger());
}

const store = createStore(
  rootReducer,
  undefined,
  applyMiddleware(...middlewares)
);

saga.run(rootSaga);

export default store;