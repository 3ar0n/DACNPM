const CLEAR_RESULT = '@@user/CLEAR_RESULT';
const FETCH_USER = '@@user/FETCH_USER';
const FETCH_USER_SUCCESS = '@@user/FETCH_USER_SUCCESS';
const FETCH_USER_ERROR = '@@user/FETCH_USER_ERROR';

export default {
  CLEAR_RESULT,
  FETCH_USER,
  FETCH_USER_SUCCESS,
  FETCH_USER_ERROR,
  };
  
  const doClearResult = () => ({
    type: CLEAR_RESULT
  });
  
  const doFetchUser = id => ({
    type: FETCH_USER,
    payload: {
      id
    }
  });
  
  const doFetchUserSuccess = () => ({
    type: FETCH_USER_SUCCESS
  });
  
  const doFetchUserError = message => ({
    type: FETCH_USER_ERROR,
    payload: {
      message
    }
  });
  
  export {
    doClearResult,
    doFetchUser,
    doFetchUserSuccess,
    doFetchUserError
  };