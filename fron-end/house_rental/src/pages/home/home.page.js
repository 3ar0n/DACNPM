import React from 'react';
import { connect } from 'react-redux';
import { Switch, Route } from 'react-router-dom';
import {
    Menu,
    RoomList,
    GuestList
} from './component';
import { Wrapper, Content, ContentInner, Section } from './home.style';
import { getUser } from '../../redux/user';

const HomePage = ({ user }) => {

  let menuItem = [
    {
      linkTo: '/guest-list',
      title: 'Khách trọ'
    },
    {
      linkTo: '/room-list',
      title: 'Phòng trọ'
    }
  ]

  return (
    <Wrapper>
      <Content>
        <ContentInner>
          <Section xs={24} lg={5}>
            <Menu menuItem={menuItem}/>
          </Section>
          <Section xs={24} lg={19}>
            <Switch>
              <Route exact path='/home/' component={RoomList} />
              <Route path='/home/guest-list' component={GuestList} />
              <Route path='/home/room-list' component={RoomList} />
            </Switch>
          </Section>
        </ContentInner>
      </Content>
    </Wrapper>
  );
};

const mapStateToProps = state => ({
    user: getUser(state)
});

export default connect(mapStateToProps)(HomePage);