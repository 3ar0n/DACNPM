import React from 'react';
import { Link } from 'react-router-dom';

const Menu = ({ menuItem }) => {
    return (
      <div className='menu-root'>
        <img/>
        {
          menuItem.map(item => {
            <Link className='menu-item' to={item.linkTo}>
              <span className='menu-item-inner'>
                {item.title}
              </span>
            </Link>
          })
        }
      </div>
    );
}