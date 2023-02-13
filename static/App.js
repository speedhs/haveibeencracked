import logo from './hibc.png';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
      </header>
      <body>
  
        <div className='cracked'>
        <form className='input'>
          <label >
          <input type="text" placeholder="password" name="name" />
          </label>
          <input type="submit"  value="cracked?" />
        </form>
        </div>
        
  
      </body>
    </div>
  );
}

export default App;
