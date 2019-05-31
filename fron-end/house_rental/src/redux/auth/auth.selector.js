const getStatus = ({authState}) => {
    const { isLoading, failed, hasError, message } = authState;
    return {
      isLoading, failed, hasError, message
    };
  };
  
  const getIsAuth = ({authState}) => {
    const { isAuth } = authState;
    return isAuth;
  };
  
  const getCurrent = ({authState}) => {
    const { current } = authState;
    return current;
  };
  
  // ===========
  
  const getIsLogging = ({ authState }) => authState.isLogging;
  const getResult = ({ authState }) => authState.result;
  
  export {
    getStatus,
    getIsAuth,
    getCurrent,
  
    getIsLogging,
    getResult
  };