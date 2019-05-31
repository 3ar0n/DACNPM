const CLEAR_RESULT = '@@auth/CLEAR_RESULT';
const LOGIN = '@@auth/LOGIN';
const LOGIN_SUCCESS = '@@auth/LOGIN_SUCCESS';
const LOGIN_ERROR = '@@auth/LOGIN_ERROR';
const LOGOUT = '@@auth/LOGOUT';
const TOKEN_VERIFY = '@@auth/TOKEN_VERIFY';
const TOKEN_VERIFY_SUCCESS = '@@auth/TOKEN_VERIFY_SUCCESS';
const TOKEN_VERIFY_ERROR = '@@auth/TOKEN_VERIFY_ERROR';

export default {
    CLEAR_RESULT,
    LOGIN,
    LOGIN_ERROR,
    LOGIN_SUCCESS,
    LOGOUT,
    TOKEN_VERIFY,
    TOKEN_VERIFY_SUCCESS,
    TOKEN_VERIFY_ERROR
  };
  
  const doClearResult = () => ({
    type: CLEAR_RESULT
  });
  
  const doLogin = (username, password) => ({
    type: LOGIN,
    payload: {
      username,
      password
    }
  });
  
  const doLoginSuccess = () => ({
    type: LOGIN_SUCCESS
  });
  
  const doLoginError = message => ({
    type: LOGIN_ERROR,
    payload: {
      message
    }
  });
  
  const doLogout = () => ({
    type: LOGOUT
  });
  
  const doTokenVerify = token => ({
    type: TOKEN_VERIFY,
    payload: {
      token
    }
  });
  
  const doTokenVerifySuccess = () => ({
    type: TOKEN_VERIFY_SUCCESS
  });
  
  const doTokenVerifyError = message => ({
    type: TOKEN_VERIFY_ERROR,
    payload: {
      message
    }
  });
  
  export {
    doClearResult,
    doLogin,
    doLoginError,
    doLoginSuccess,
    doLogout,
    doTokenVerify,
    doTokenVerifySuccess,
    doTokenVerifyError
  };