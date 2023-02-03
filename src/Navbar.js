import React from 'react';
import './Navbar.css';
import logo from './logo192.png';

const Navbar = () => (
  <nav>
    <img src={logo} alt="Logo" />
    <ul>
      <li><a href="#">Home</a></li>
      <li><a href="#">About</a></li>
      <li><a href="#">Contact</a></li>
    </ul>
  </nav>
);

export default Navbar;
