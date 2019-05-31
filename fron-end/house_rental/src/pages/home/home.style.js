import styled from 'styled-components';
import { Row, Col } from 'antd';

const Wrapper = styled.div`
  display: flex;
  flex-direction: column;
  overflow-x: hidden;
  min-height: 100vh;
  margin-bottom: 2rem;
`;

const Content = styled.div`
  width: 100%;
  max-width: 1200px;
  margin: 0 auto;
  @media (min-width: 992px) {
    margin-top: 3rem;
  }
`;

const ContentInner = styled(Row).attrs(({ gutter }) => ({
  gutter: 24 || gutter
}))``;

const Section = styled(Col).attrs(({ xs, lg }) => ({
  xs: 24 || xs,
  lg: 24 || lg
}))`
`;


export {
  Wrapper,
  Content,
  ContentInner,
  Section
}