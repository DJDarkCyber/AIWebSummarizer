import React from 'react';
import { Navbar, Container, Nav } from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';

const Header = () => {
  return (
    <Navbar expand="lg" className="shadow-sm bg-[#9e767698]">
      <Container fluid>
        <Navbar.Brand href="#" style={{ paddingLeft: '20px' }}>
          <img
            src="/logo.png"
            alt="Logo"
            width="30"
            height="30"
            className="d-inline-block align-top"
          />
        </Navbar.Brand>

        <Navbar.Brand className="mx-auto">
          <h3 style={{ margin: 0 }}><span style={{fontWeight: 600, color: '#594545'}}>AI</span><span style={{color: '#9E7676'}}> Web Summarizer</span></h3>
        </Navbar.Brand>

        <Nav>
          <Nav.Link href="#about-us" style={{ paddingRight: '20px' }}>
            About us
          </Nav.Link>
        </Nav>
      </Container>
    </Navbar>
  );
};

export default Header;