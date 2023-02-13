import React from 'react';
import './Navbar.css';
import logo from './hidden.svg';
import "./About.js"

const Navbar = () => (
  <nav>
    <img src={logo} alt="Logo" />
    <ul>
      <li><a href="#">Home</a></li>
      <li><a href="./About.js">About</a></li>
      <li><a href="#">Team</a></li>
    </ul>
  </nav>
);

export default Navbar;
