//footer.js
import React from 'react';
import './Footer.css';
const FooterLinks = () => (
  <div>
    <a href="https://darknetdiaries.com/episode/">Darknet Diaries</a>
    <a href="#">Link 2</a>
    <a href="#">Link 3</a>
  </div>
);

const Footer = () => (
  <footer>
    <FooterLinks />
    <p>Copyright &copy; {new Date().getFullYear()}</p>
  </footer>
);

export default Footer;
