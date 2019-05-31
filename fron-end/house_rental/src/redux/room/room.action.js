const CLEAR_RESULT = '@@auth/CLEAR_RESULT';
const FETCH_ROOM = '@@auth/FETCH_ROOM';
const FETCH_ROOM_SUCCESS = '@@auth/FETCH_ROOM_SUCCESS';
const FETCH_ROOM_ERROR = '@@auth/FETCH_ROOM_ERROR';
export default {
    CLEAR_RESULT,
    FETCH_ROOM,
    FETCH_ROOM_SUCCESS,
    FETCH_ROOM_ERROR
  };
  
  const doClearResult = () => ({
    type: CLEAR_RESULT
  });
  const doFetchRoom = id => ({
    type: FETCH_ROOM,
    payload: {
      id
    }
  });
  
  const doFetchRoomSuccess = (room) => ({
    type: FETCH_ROOM_SUCCESS,
    payload: {
      room
    }
  });
  
  const doFetchRoomslError = message => ({
    type: FETCH_ROOM_ERROR,
    payload: {
      message
    }
  });
  
  export {
    doClearResult,
    doFetchRoom,
    doFetchRoomSuccess,
    doFetchRoomError
  };