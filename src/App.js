import logo from './hidden.svg';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        
      </header>
      <body>
      <p>
        <div className='cracked'>
        <form className='input'>
          <label >
          <input type="text" placeholder="password" name="name" />
          </label>
          <input type="submit"  value="cracked?" />
        </form>
        </div>
        
        </p>
      </body>
    </div>
  );
}

export default App;
