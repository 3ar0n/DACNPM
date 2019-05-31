const getRoom = ({ roomState }) => roomState.room;
const getGuest = ({ roomState }) => roomState.guest;
const getIsFetchingRoom = ({ roomState }) => roomState.isFetchingRoom;
  
  export {
    getRoom,
    getGuest,
    getIsFetchingRoom
  };