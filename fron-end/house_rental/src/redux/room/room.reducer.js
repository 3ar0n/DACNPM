import roomAction from './room.action';

const INITIAL_STATE = {
  isFetchingRoom: false,
  room: {},
  guest: [],
  result: undefined,
  isUpdating: false
};

const applyClearResult = (state, action) => {
  return {
    ...state,
    result: undefined
  };
};

const applyFetchRoom = (state, action) => {
  return {
    ...state,
    isFetchingRoom: true,
    result: undefined
  };
};

const applyFetchRoomSucces = (state, action) => {
  const { payload: { room } } = action;
  return {
    ...state,
    isFetchingRoom: false,
    result: {
      type: 'success',
    },
    room
  };
};

const applyFetchRoomsError = (state, action) => {
  const { payload: { message } } = action;
  return {
    ...state,
    isFetchingRoom: false,
    result: {
      type: 'error',
      message
    }
  };
};

const reducer = (state = INITIAL_STATE, action) => {
  switch (action.type) {
    case roomAction.CLEAR_RESULT: {
      return applyClearResult(state, action);
    }

    case roomAction.FETCH_ROOM: {
      return applyFetchRoom(state, action);
    }

    case roomAction.FETCH_ROOM_SUCCESS: {
      return applyFetchRoomSucces(state, action);
    }

    case roomAction.FETCH_ROOM_ERROR: {
      return applyFetchRoomsError(state, action);
    }
   
    default: return state;
  }
};

export default reducer;