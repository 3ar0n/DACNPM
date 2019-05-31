import React from 'react';
import { Link } from 'react-router-dom';

const Menu = ({ menuItem }) => {

  const items =  menuItem.map(item => (
    <Link className='menu-item' to={item.linkTo}>
      <span className='menu-item-inner'>
        {item.title}
      </span>
    </Link>
  ));
    return (
      <div className='menu-root'>
        {
          items
        }
      </div>
    );
}

export default Menu;