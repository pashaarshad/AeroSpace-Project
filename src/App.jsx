import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './pages/Home';
import Chat from './pages/Chat';
import Graph from './pages/Graph';
import About from './pages/About';
import Header from './components/Header';
import Footer from './components/Footer';
import DebugChat from './components/DebugChat';
import ChatFetch from './components/ChatFetch';
import './App.css';

function App() {
  return (
    <Router>
      <div className="App flex flex-col min-h-screen font-sans">
        <Header />
        <main className="flex-grow">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/chat" element={<Chat />} />
            <Route path="/chat-fetch" element={<ChatFetch />} />
            <Route path="/graph" element={<Graph />} />
            <Route path="/about" element={<About />} />
            <Route path="/debug" element={<DebugChat />} />
          </Routes>
        </main>
        <Footer />
      </div>
    </Router>
  );
}

export default App;
