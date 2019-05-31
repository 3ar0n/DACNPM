import React from 'react';
import ReactDOM from 'react-dom';
import { connect } from 'react-redux';
import App from './App';
import { Provider } from "react-redux";
import './index.css';
import * as serviceWorker from './serviceWorker';
import store from './store';

ReactDOM.render(
    <Provider store={store}>
      <App />
    </Provider>,
    document.getElementById('root')
  );
  
serviceWorker.unregister();  
