//footer.js
import React from 'react';
import './Footer.css';
const FooterLinks = () => (
  <div>
    <a href="https://darknetdiaries.com/episode/">Darknet Diaries</a>
    <a href="#">Have I Been Pwned</a>
    <a href="#"></a>
  </div>
);

const Footer = () => (
  <footer>
    <FooterLinks />
    <p>Copyright &copy; {new Date().getFullYear()}</p>
  </footer>
);

export default Footer;
