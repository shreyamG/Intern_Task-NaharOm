// import logo from './l/ogo.svg';
import './App.css';
import React from 'react';
// import ReactDOM from 'react-dom';
import Header from './components/header/header';
// import Footer from "./components/footer/footer";
import Craousel from './components/header/MarketCraousel';
import { BrowserRouter as Router, Switch, Route,Routes } from "react-router-dom";


function App() {
  return (
    <>
    <div>
    <Header />
    </div>
    <Router>
      <Routes>
   <Route exact path="/" element={<Craousel />} />
   {/* <Route exact path="/Footer" element={<Footer/>} /> */}
    </Routes>
    </Router>
    </>
  );
}

export default App;
