import React from 'react';
import logo from './logo.svg';
import './App.css';
import { connect } from 'react-redux';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import { getUser } from './reducers/user';
import {
  HomePage,
  LoginPage,
  ProfilePage
} from './pages';

const App = () => {
  return (
    <BrowserRouter>
      <Switch>
        <Route exact path='/' component={HomePage}/>
        <Route path='/login' component={LoginPage}/>
        <Route path='/profile' component={ProfilePage}/>
      </Switch>
    </BrowserRouter>
  );
}

export default App;
