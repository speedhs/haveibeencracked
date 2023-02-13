import logo from './hibc.png';
import './About.css';

function About() {
  return (
    <div className="About">
      <header className="About-header">
        <img src={logo} className="About-logo" alt="logo" />
      </header>
      <body>
  
      <div className='about'>
        <p>
          Have you ever wondered if your password has been leaked in any data breaches? Our website helps you find out if your password has been compromised in any data breaches.
        </p>
        <p>
          We use the latest technology to constantly monitor for new data breaches and update our database. Our algorithm then checks your password against this database, ensuring that you are always up to date on the security of your password.
        </p>
        <p>
          Keep your online accounts secure and protected by regularly checking if your password has been leaked with us.
        </p>
    </div>
    

  </body>
</div>

        
)
     
}

export default About;
