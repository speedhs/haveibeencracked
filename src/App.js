import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
        <form>
          <label>
            Name:
          <input type="text" defaultValue="password" name="name" />
          </label>
          <input type="submit"  value="cracked?" />
        </form>
        </p>
      </header>
    </div>
  );
}

export default App;
