import userAction from './user.action';

const INITIAL_STATE = {
  isFetchingUser: false,
  user: undefined,
  result: undefined
};

const applyClearResult = (state, action) => {
  return {
    ...state,
    result: undefined
  }
};

const applyFetchUser = (state, action) => {
  return {
    ...state,
    result: undefined,
    isFetchingData: true
  }
};

const applyFetchUserSuccess = (state, action) => {
  return {
    ...state,
    isFetchingUser: false,
    result: {
      type: 'success'
    }
  };
};

const applyFetchUserError = (state, action) => {
  const { payload: { message } } = action;
  return {
    ...state,
    isFetchingUser: false,
    result: {
      type: 'error',
      message
    }
  }
};

const reducer = (state = INITIAL_STATE, action) => {
  switch (action.type) {
    case userAction.CLEAR_RESULT: {
      return applyClearResult(state, action);
    }

    case userAction.FETCH_USER: {
      return applyFetchUser(state, action);
    }

    case userAction.FETCH_USER_SUCCESS: {
      return applyFetchUserSuccess(state, action);
    }

    case userAction.FETCH_USER_ERROR: {
      return applyFetchUserError(state, action);
    }
   
    default: return state;
  }
};

export default reducer;