import React from 'react';
import logo from './logo.svg';
import './App.css';
import { connect } from 'react-redux';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import { getUser } from './redux/user';
import {
  HomePage,
  //LoginPage,
  //ProfilePage
} from './pages';

const App = () => {
  return (
    <BrowserRouter>
      <Switch>
        <Route exact path='/' component={HomePage}/>
        
      </Switch>
    </BrowserRouter>
  );
}

export default App;
