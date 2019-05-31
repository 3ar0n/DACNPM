import { combineReducers } from 'redux';
import { authReducer } from './auth';
import { userReducer } from './user';
import { roomReducer } from './room';
 
const rootReducer = combineReducers({
  authState: authReducer,
  roomState: roomReducer,
  userState: userReducer
});

export default rootReducer;