import React from 'react';
import logo from './logo.svg';
import './App.css';
import axios from 'axios';

function App() {
  function apiCall(e:any){

    // fetch("http://127.0.0.1:3000/api").then((res)=>console.log(res))
    axios.get('http://192.168.0.45:3000/api').then((res)=>{
      let a:any = res.data
      alert(a.temp);
      
    })
    
  }


  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p
          className="App-link"
          // href="https://reactjs.org"
          onClick={apiCall}
          // target="_blank"
          // rel="noopener noreferrer"
        >
          Call API
        </p>
      </header>
    </div>
  );
}

export default App;
