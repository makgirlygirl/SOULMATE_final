import React from 'react';
import { BrowserRouter, Routes, Route, Router } from "react-router-dom";
import './App.css'; 
import MainPage from './pages/MainPage';
import BankPage from './pages/BankPage';
import CreatorPage from './pages/CreatorPage';
import BankResultPage from './pages/BankResultPage';
import CreatorResultPage from './pages/CreatorResultPage';

const App = () => {
    return (
      <>
      <Routes>
          <Route element={<MainPage/>} exact path="/"/>
          <Route element={<BankPage/>} exact path="/bank"/>
          <Route element={<CreatorPage/>} exact path="/creator"/>
          <Route element={<BankResultPage/>} exact path="/bank/result"/>
          <Route element={<CreatorResultPage/>} exact path="/creator/result"/>
      </Routes>
      </>
    );
}

export default App;