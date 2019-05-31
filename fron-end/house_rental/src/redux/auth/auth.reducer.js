import authAction from './auth.action';

const INITIAL_STATE = {
  isLogging: false,
  isTokenVerifying: false,
  result: undefined
};

const applyLogin = (state, action) => {
  return {
    ...state,
    isLogging: true,
    result: undefined
  };
};

const applyLoginSucces = (state, action) => {
  return {
    ...state,
    isLogging: false,
    result: {
      type: 'success'
    }
  };
};

const applyLoginError = (state, action) => {
  const { payload: { message } } = action;
  return  {
    ...state,
    isLogging: false,
    result: {
      type: 'error',
      message 
    }
  };
};

const applyClearResult = (state, action) => {
  return {
    ...state,
    result: undefined
  }
};

const applyTokenVerify = (state, action) => {
  return {
    ...state,
    result: undefined,
    isTokenVerifying: true
  };
};

const applyTokenVerifySuccess = (state, action) => {
  return {
    ...state,
    isTokenVerifying: false,
  };
};

const applyTokenVerifyError = (state, action) => {
  const { payload: { message } } = action;
  return {
    ...state,
    isTokenVerifying: false,
    result: {
      type: 'error',
      message
    }
  };
};

const reducer = (state = INITIAL_STATE, action) => {
  switch (action.type) {
    case authAction.CLEAR_RESULT: {
      return applyClearResult(state, action);
    }

    case authAction.LOGIN: {
      return applyLogin(state, action);
    }

    case authAction.LOGIN_SUCCESS: {
      return applyLoginSucces(state, action);
    }

    case authAction.LOGIN_ERROR: {
      return applyLoginError(state, action);
    }
  
    case authAction.TOKEN_VERIFY: {
      return applyTokenVerify(state, action);
    }

    case authAction.TOKEN_VERIFY_SUCCESS: {
      return applyTokenVerifySuccess(state, action);
    }

    case authAction.TOKEN_VERIFY_ERROR: {
      return applyTokenVerifyError(state, action);
    }
   
    default: return state;
  }
};

export default reducer;